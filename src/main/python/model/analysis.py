import logging
import math
import time

import numpy as np
import qtawesome as qta
from mpl_toolkits.axes_grid1 import make_axes_locatable
from qtpy import QtCore
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QDialog

from model.limits import Limits, LimitsDialog
from model.preferences import GRAPH_X_AXIS_SCALE, GRAPH_X_MIN, GRAPH_X_MAX
from model.signal import select_file, readWav
from ui.analysis import Ui_analysisDialog
from ui.spectro import Ui_spectroDialog

logger = logging.getLogger('analysis')


class AnalyseSignalDialog(QDialog, Ui_analysisDialog):
    def __init__(self, preferences, signal_model):
        super(AnalyseSignalDialog, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint | Qt.WindowMinMaxButtonsHint)
        self.__preferences = preferences
        self.filePicker.setIcon(qta.icon('fa.folder-open-o'))
        self.showLimitsButton.setIcon(qta.icon('ei.move'))
        self.showSpectroButton.setIcon(qta.icon('fa.area-chart'))
        self.showSpectroButton.setEnabled(False)
        self.__info = None
        self.__signal = None
        self.__filtered_signals = {}
        self.__spectrum_analyser = MaxSpectrumByTime(self.spectrumChart, self.__preferences, self)
        self.__waveform_analyser = Waveform(self.waveformChart, self)
        self.__signal_model = signal_model
        self.copyFilter.addItem('No Filter')
        for s in signal_model:
            if s.master is None:
                self.copyFilter.addItem(s.name)
        self.__duration = 0
        self.loadButton.setEnabled(False)
        self.__clear()

    def select_wav_file(self):
        '''
        Allows the user to select a file and laods info about it
        '''
        file = select_file(self, ['wav', 'flac'])
        if file is not None:
            self.__clear()
            self.file.setText(file)
            import soundfile as sf
            self.__info = sf.info(file)
            self.channelSelector.clear()
            for i in range(0, self.__info.channels):
                self.channelSelector.addItem(f"{i+1}")
            self.channelSelector.setEnabled(self.__info.channels > 1)
            self.startTime.setTime(QtCore.QTime(0, 0, 0))
            self.startTime.setEnabled(True)
            self.__duration = math.floor(self.__info.duration * 1000)
            self.endTime.setTime(QtCore.QTime(0, 0, 0).addMSecs(self.__duration))
            self.endTime.setEnabled(True)
            self.loadButton.setEnabled(True)
        else:
            self.__signal = None

    def __clear(self):
        self.__spectrum_analyser.clear()
        self.startTime.setEnabled(False)
        self.endTime.setEnabled(False)
        self.loadButton.setEnabled(False)
        self.__signal = None
        self.__info = None
        self.__duration = 0

    def load_file(self):
        '''
        Loads a signal from the given file.
        '''
        start = end = None
        start_millis = self.startTime.time().msecsSinceStartOfDay()
        if start_millis > 0:
            start = start_millis
        end_millis = self.endTime.time().msecsSinceStartOfDay()
        if end_millis < self.__duration or start is not None:
            end = end_millis
        channel = int(self.channelSelector.currentText())
        from model.preferences import ANALYSIS_TARGET_FS
        from app import wait_cursor
        with wait_cursor(f"Loading {self.__info.name}"):
            self.__signal = readWav('analysis', self.__info.name, channel=channel, start=start, end=end,
                                    target_fs=self.__preferences.get(ANALYSIS_TARGET_FS))
            self.show_chart()

    def show_chart(self):
        '''
        Shows the currently selected chart.
        '''
        if self.__signal is not None:
            active_signal = self.__get_filtered_signal()
            idx = self.analysisTabs.currentIndex()
            if idx == 0:
                self.__spectrum_analyser.signal = active_signal
                self.__spectrum_analyser.analyse()
            elif idx == 1:
                self.__waveform_analyser.signal = active_signal
                self.__waveform_analyser.analyse()

    def __get_filtered_signal(self):
        sig = next((s for s in self.__signal_model if s.name == self.copyFilter.currentText()), None)
        if sig is None:
            return self.__signal
        else:
            if sig.name not in self.__filtered_signals:
                start = time.time()
                filt = sig.filter
                self.__filtered_signals[sig.name] = self.__signal.sosfilter(filt.resample(self.__signal.fs).get_sos())
                end = time.time()
                logger.debug(f"Filtered in {round(end - start, 3)}s")
            return self.__filtered_signals[sig.name]

    def show_limits(self):
        idx = self.analysisTabs.currentIndex()
        if idx == 0:
            self.__spectrum_analyser.show_limits()
        elif idx == 1:
            self.__waveform_analyser.show_limits()

    def allow_clip_choice(self):
        if self.clipAtAverage.isChecked():
            self.clipToAbsolute.setEnabled(False)
            self.dbRange.setEnabled(False)
        else:
            self.dbRange.setEnabled(True)
            self.clipToAbsolute.setEnabled(True)
        self.show_chart()

    def clip_to_abs(self):
        if self.clipToAbsolute.isChecked():
            self.clipAtAverage.setEnabled(False)
            self.dbRange.setEnabled(True)
        else:
            self.clipAtAverage.setEnabled(True)
        self.show_chart()

    def show_spectro(self):
        ''' shows the spectrogram. '''
        self.__spectrum_analyser.show_spectro()


class WaveformRange:
    '''
    A range calculator that just returns -1/1 or the signal range
    '''

    def __init__(self, is_db=False):
        self.is_db = is_db

    def calculate(self, y_range):
        if self.is_db is True:
            return y_range[0], 0.0
        else:
            return -1.0, 1.0


class Waveform:
    '''
    An analyser that simply shows the waveform.
    '''

    def __init__(self, chart, ui):
        self.__chart = chart
        self.__ui = ui
        self.__axes = self.__chart.canvas.figure.add_subplot(111)
        self.__waveform_range = WaveformRange(is_db=self.__ui.magnitudeDecibels.isChecked())
        self.__limits = Limits('waveform', self.__redraw, self.__axes, x_axis_configurer=self.configure_time_axis,
                               y_range_calculator=self.__waveform_range, x_lim=(0, 1), x_scale='linear')
        self.__signal = None
        self.__curve = None

    def configure_time_axis(self, axes, x_scale):
        axes.set_xscale(x_scale)
        axes.set_xlabel('Time')

    @property
    def signal(self):
        return self.__signal

    @signal.setter
    def signal(self, signal):
        self.__signal = signal
        self.__limits.x_min = 0
        self.__limits.x_max = 1
        if signal is not None:
            self.__limits.x_max = signal.durationSeconds
            headroom = 20 * math.log(1 / np.nanmax(np.abs(signal.samples)))
        else:
            headroom = 0.0
        self.__ui.headroom.setValue(headroom)
        if self.__curve is not None:
            self.__curve.set_data([], [])
        self.__init_chart()

    def __init_chart(self, draw=False):
        self.__limits.propagate_to_axes(draw=False)
        self.__axes.grid(linestyle='-', which='major', linewidth=1, alpha=0.5)
        self.__axes.grid(linestyle='--', which='minor', linewidth=1, alpha=0.5)
        if draw is True:
            self.__redraw()

    def __redraw(self):
        self.__chart.canvas.draw_idle()

    def clear(self):
        '''
        Resets the analyser.
        '''
        self.signal = None

    def show_limits(self):
        '''
        Shows the graph limits dialog.
        '''
        if self.signal is not None:
            LimitsDialog(self.__limits, x_min=0, x_max=self.signal.durationSeconds, y1_min=-1, y1_max=1).exec()

    def analyse(self):
        '''
        Calculates the spectrum view.
        '''
        from app import wait_cursor
        with wait_cursor(f"Analysing"):
            step = 1.0 / self.signal.fs
            x = np.arange(0, self.signal.durationSeconds, step)
            y = self.signal.samples
            if self.__ui.magnitudeDecibels.isChecked():
                y = np.copy(y)
                y[y == 0.0] = 0.000000001
                y = 20 * np.log10(np.abs(y))
                self.__limits.y1_max = 0.0
                self.__limits.y1_min = math.floor(np.min(y))
            else:
                self.__limits.y1_min = -1.0
                self.__limits.y1_max = 1.0
            self.__waveform_range.is_db = self.__ui.magnitudeDecibels.isChecked()
            if self.__curve is None:
                self.__curve = self.__axes.plot(x, y, linewidth=1, color='cyan')[0]
            else:
                self.__curve.set_data(x, y)
                self.__limits.on_data_change((self.__limits.y1_min, self.__limits.y1_max), [])
            self.__limits.propagate_to_axes(draw=True)


class OnePlusRange:
    def __init__(self):
        pass

    def calculate(self, y_range):
        return y_range[0], y_range[1] + 1


class MaxSpectrumByTime:
    '''
    An analyser that highlights where the heavy hits are in time by frequency
    '''

    def __init__(self, chart, preferences, ui):
        self.__chart = chart
        self.__ui = ui
        self.__preferences = preferences
        self.__axes = self.__chart.canvas.figure.add_subplot(111)
        self.__limits = Limits('spectrum', self.__redraw, self.__axes, y_range_calculator=OnePlusRange(),
                               x_lim=(preferences.get(GRAPH_X_MIN), preferences.get(GRAPH_X_MAX)),
                               x_scale=preferences.get(GRAPH_X_AXIS_SCALE))
        self.__signal = None
        self.__scatter = None
        self.__cb = None

    @property
    def signal(self):
        return self.__signal

    @signal.setter
    def signal(self, signal):
        self.__signal = signal
        self.__limits.y1_min = -1
        self.__limits.y1_max = 1
        if signal is not None:
            self.__limits.y1_max = signal.durationSeconds
        if self.__scatter is not None:
            self.__scatter.set_offsets(np.c_[np.array([]), np.array([])])
            self.__scatter.set_array(np.array([]))
        self.__init_chart()

    def __init_chart(self, draw=False):
        self.__limits.propagate_to_axes(draw=False)
        self.__update_change_chart_button()
        self.__axes.set_ylabel('Time')
        self.__axes.grid(linestyle='-', which='major', linewidth=1, alpha=0.5)
        self.__axes.grid(linestyle='--', which='minor', linewidth=1, alpha=0.5)
        if draw is True:
            self.__redraw()

    def __update_change_chart_button(self):
        ''' if the limit are < 15mins then allow a spectrogram '''
        if (self.__limits.y1_max - self.__limits.y1_min) <= 900 and self.signal is not None:
            self.__ui.showSpectroButton.setEnabled(True)
        else:
            self.__ui.showSpectroButton.setEnabled(False)

    def __redraw(self):
        self.__chart.canvas.draw_idle()

    def clear(self):
        '''
        Resets the analyser.
        '''
        self.signal = None
        self.__update_change_chart_button()

    def show_limits(self):
        '''
        Shows the graph limits dialog.
        '''
        if self.signal is not None:
            LimitsDialog(self.__limits, y1_min=0, y1_max=self.signal.durationSeconds).exec()
            self.__update_change_chart_button()

    def analyse(self):
        '''
        Calculates the spectrum view.
        '''
        from app import wait_cursor
        with wait_cursor(f"Analysing"):
            self.__render_scatter()
            self.__limits.propagate_to_axes(draw=True)

    def __render_scatter(self):
        ''' renders a scatter plot showing the biggest hits '''
        Sxx, f, resolution_shift, t, x, y, z = self.__get_xyz(self.__signal)
        # dump the output for debug purposes
        # np.savetxt('spectro.csv', Sxx, delimiter=',', fmt='%.6f')
        # np.savetxt('test2.csv', np.c_[x,y,z], delimiter=',', fmt='%.6f')
        if self.__ui.clipAtAverage.isChecked():
            _, Pthreshold = self.signal.spectrum(resolution_shift=resolution_shift)
        else:
            if self.__ui.clipToAbsolute.isChecked():
                Pthreshold = np.array([np.max(Sxx) + self.__ui.dbRange.value()]).repeat(f.size)
            else:
                # add the dbRange because it's shown as a negative value
                Pthreshold = Sxx.max(axis=-1) + self.__ui.dbRange.value()
        Pthreshold = np.tile(Pthreshold, t.size)
        vmax = math.ceil(np.max(Sxx.max(axis=-1)))
        vmin = vmax - self.__ui.colourRange.value()
        stack = np.column_stack((x, y, z))
        # filter by signal level
        above_threshold = stack[stack[:, 2] > Pthreshold]
        above_threshold = above_threshold[above_threshold[:, 2] >= vmin]
        # filter by graph limis
        above_threshold = above_threshold[above_threshold[:, 0] >= self.__limits.x_min]
        above_threshold = above_threshold[above_threshold[:, 0] <= self.__limits.x_max]
        above_threshold = above_threshold[above_threshold[:, 1] >= self.__limits.y1_min]
        above_threshold = above_threshold[above_threshold[:, 1] <= self.__limits.y1_max]
        x = above_threshold[:, 0]
        y = above_threshold[:, 1]
        z = above_threshold[:, 2]
        # now plot or update
        if self.__scatter is None:
            self.__scatter = self.__axes.scatter(x, y, c=z, vmin=vmin, vmax=vmax)
            divider = make_axes_locatable(self.__axes)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            self.__cb = self.__axes.figure.colorbar(self.__scatter, cax=cax)
        else:
            new_data = np.c_[x, y]
            self.__scatter.set_offsets(new_data)
            self.__scatter.set_clim(vmin=vmin, vmax=vmax)
            self.__scatter.set_array(z)

    def __get_xyz(self, signal):
        from model.preferences import ANALYSIS_RESOLUTION
        resolution_shift = math.log(self.__preferences.get(ANALYSIS_RESOLUTION), 2)
        f, t, Sxx = signal.spectrogram(resolution_shift=resolution_shift)
        x = f.repeat(t.size)
        y = np.tile(t, f.size)
        z = Sxx.flatten()
        return Sxx, f, resolution_shift, t, x, y, z

    def show_spectro(self):
        ''' shows the spectrogram. '''
        if self.__signal is not None:
            visible_signal = self.__signal.cut(round(max(0, self.__limits.y1_min)),
                                               round(min(self.__limits.y1_max, self.signal.durationSeconds)))
            SpectrogramDialog(self.__ui, visible_signal, self.__preferences,
                              (self.__limits.x_min, self.__limits.x_max)).show()


class SlaveRange:
    def __init__(self, vals):
        self.__vals = vals

    def calculate(self, y_range):
        return self.__vals


class SpectrogramDialog(QDialog, Ui_spectroDialog):
    multipliers = [0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0]

    def __init__(self, parent, signal, preferences, freq_lim):
        super(SpectrogramDialog, self).__init__(parent=parent)
        self.__ui = parent
        self.setupUi(self)
        self.limitsButton.setIcon(qta.icon('ei.move'))
        self.setWindowFlags(self.windowFlags() | Qt.WindowSystemMenuHint | Qt.WindowMinMaxButtonsHint)
        self.__preferences = preferences
        self.__signal = signal
        self.__axes = self.spectroChart.canvas.figure.add_subplot(111)
        self.__limits = Limits('spectro', self.__redraw, self.__axes, freq_lim,
                               x_scale=preferences.get(GRAPH_X_AXIS_SCALE),
                               y_range_calculator=SlaveRange((0, round(self.__signal.durationSeconds))))
        self.__limits.propagate_to_axes(draw=True)
        self.resolution.blockSignals(True)
        self.__nfft = []
        default_length = self.__signal.getSegmentLength()
        for m in self.multipliers:
            freq_res = float(signal.fs) / (default_length * m)
            time_res = (m * default_length) / signal.fs
            self.__nfft.append(int(default_length * m))
            self.resolution.addItem(f"{freq_res:.3f} Hz / {time_res:.3f} s")
        self.resolution.setCurrentIndex(2)
        self.resolution.blockSignals(False)
        self.__specgram = None
        self.__cb = None
        self.update_chart()

    def __redraw(self):
        self.spectroChart.canvas.draw_idle()

    def show_limits(self):
        LimitsDialog(self.__limits, x_min=self.__axes.get_xlim()[0], x_max=self.__axes.get_xlim()[1],
                     y1_min=self.__axes.get_ylim()[0], y1_max=self.__axes.get_ylim()[1]).exec()

    def update_chart(self):
        ''' renders the entire signal as a spectrogram '''
        self.__axes.clear()
        self.__axes.grid(linestyle='-', which='major', linewidth=1, alpha=0.5)
        self.__axes.grid(linestyle='--', which='minor', linewidth=1, alpha=0.5)
        multiplier_idx = self.resolution.currentIndex()
        multiplier = self.multipliers[multiplier_idx]
        f, t, Sxx = self.__signal.spectrogram(resolution_shift=math.log(multiplier, 2))
        vmax = math.ceil(np.max(Sxx.max(axis=-1)))
        vmin = vmax - self.vRange.value()
        self.__specgram = self.__axes.pcolormesh(f, t, Sxx.transpose(), vmin=vmin, vmax=vmax, shading='gouraud')
        if self.__cb is None:
            divider = make_axes_locatable(self.__axes)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            self.__cb = self.__axes.figure.colorbar(self.__specgram, cax=cax)
        else:
            self.__cb.on_mappable_changed(self.__specgram)
        self.__limits.propagate_to_axes(draw=True)
