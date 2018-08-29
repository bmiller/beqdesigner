import collections
import logging
import math
import os
import sys
from contextlib import contextmanager

import matplotlib
import qtawesome as qta
from matplotlib import style

from model.iir import Passthrough
from ui.biquad import Ui_exportBiquadDialog
from ui.savechart import Ui_saveChartDialog

matplotlib.use("Qt5Agg")

from qtpy.QtCore import QSettings
from qtpy.QtGui import QIcon, QFont, QCursor
from qtpy.QtWidgets import QMainWindow, QApplication, QErrorMessage, QAbstractItemView, QDialog, QFileDialog

from model.extract import ExtractAudioDialog
from model.filter import FilterTableModel, FilterModel, FilterDialog
from model.log import RollingLogger
from model.magnitude import MagnitudeModel
from model.preferences import PreferencesDialog, BINARIES, ANALYSIS_TARGET_FS, STYLE_MATPLOTLIB_THEME
from model.signal import SignalModel, SignalTableModel, SignalDialog
from ui.beq import Ui_MainWindow

from qtpy import QtCore

logger = logging.getLogger('beq')


@contextmanager
def wait_cursor(msg=None):
    '''
    Allows long running functions to show a busy cursor.
    :param msg: a message to put in the status bar.
    '''
    try:
        QApplication.setOverrideCursor(QCursor(QtCore.Qt.WaitCursor))
        yield
    finally:
        QApplication.restoreOverrideCursor()


class BeqDesigner(QMainWindow, Ui_MainWindow):
    '''
    The main UI.
    '''

    def __init__(self, app, parent=None):
        super(BeqDesigner, self).__init__(parent)
        self.logger = logging.getLogger('beqdesigner')
        self.app = app
        self.settings = QSettings("3ll3d00d", "beqdesigner")
        if getattr(sys, 'frozen', False):
            self.__style_path_root = sys._MEIPASS
        else:
            self.__style_path_root = os.path.dirname(__file__)
        matplotlib_theme = self.settings.value(STYLE_MATPLOTLIB_THEME)
        if matplotlib_theme is not None:
            if matplotlib_theme.startswith('beq'):
                style.use(os.path.join(self.__style_path_root, 'style', 'mpl', f"{matplotlib_theme}.mplstyle"))
            else:
                style.use(matplotlib_theme)
        self.setupUi(self)
        self.limitsButton.setIcon(qta.icon('ei.move'))
        self.showValuesButton.setIcon(qta.icon('ei.eye-open'))
        # logs
        self.logViewer = RollingLogger(parent=self)
        self.actionShow_Logs.triggered.connect(self.logViewer.show_logs)
        self.actionPreferences.triggered.connect(self.showPreferences)
        # init the filter view/model
        self.filterView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.__filterModel = FilterModel(self.filterView, self.showIndividualFilters, on_update=self.on_filter_change)
        self.__filterTableModel = FilterTableModel(self.__filterModel, parent=parent)
        self.filterView.setModel(self.__filterTableModel)
        self.filterView.selectionModel().selectionChanged.connect(self.changeFilterButtonState)
        # signal model
        self.signalView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.signalView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.__signalModel = SignalModel(self.signalView, self.__filterModel, on_update=self.on_signal_change)
        self.__signalTableModel = SignalTableModel(self.__signalModel, parent=parent)
        self.signalView.setModel(self.__signalTableModel)
        self.signalView.selectionModel().selectionChanged.connect(self.changeSignalButtonState)
        # magnitude
        self.__magnitudeModel = MagnitudeModel('main', self.filterChart, self.__signalModel, 'Signals',
                                               self.__filterModel, 'Filters')
        # processing
        self.ensurePathContainsExternalTools()
        # extraction
        self.actionExtract_Audio.triggered.connect(self.showExtractAudioDialog)
        # export
        self.actionSave_Chart.triggered.connect(self.exportChart)
        self.actionExport_Biquad.triggered.connect(self.exportBiquads)

    def on_signal_change(self, names):
        '''
        Reacts to a change in the signal model by updating the reference and redrawing the chart.
        :param names: the signal names.
        '''
        self.update_reference_series(names, self.signalReference, True)
        self.__magnitudeModel.redraw()

    def on_filter_change(self, names):
        '''
        Reacts to a change in the filter model by updating the reference and redrawing the chart.
        :param names: the signal names.
        '''
        self.update_reference_series(names, self.filterReference, False)
        self.__magnitudeModel.redraw()

    def exportChart(self):
        '''
        Saves the currently selected chart to a file.
        '''
        dialog = SaveChartDialog(self, 'beq', self.filterChart.canvas.figure, self.statusbar)
        dialog.exec()

    def exportBiquads(self):
        '''
        Shows the biquads for the current filter set.
        '''
        dialog = ExportBiquadDialog(self.__filterModel.filter)
        dialog.exec()

    def ensurePathContainsExternalTools(self):
        '''
        Ensures that all external tool paths are on the path.
        '''
        path = os.environ.get('PATH', [])
        paths = path.split(os.pathsep)
        locs = set(filter(None.__ne__, [self.settings.value(f"binaries/{x}") for x in BINARIES]))
        logging.info(f"Adding {locs} to PATH")
        if len(locs) > 0:
            os.environ['PATH'] = os.pathsep.join([l for l in locs if l not in paths]) + os.pathsep + path
        else:
            logger.warning(f"No paths set for {BINARIES}")
            # TODO attempt to call each binary with a test command to test if they are really on the path

    def setupUi(self, mainWindow):
        super().setupUi(self)
        geometry = self.settings.value("geometry")
        if geometry is not None:
            self.restoreGeometry(geometry)
        else:
            screen_geometry = self.app.desktop().availableGeometry()
            if screen_geometry.height() < 800:
                self.showMaximized()
        window_state = self.settings.value("windowState")
        if window_state is not None:
            self.restoreState(window_state)

    def closeEvent(self, *args, **kwargs):
        '''
        Saves the window state on close.
        :param args:
        :param kwargs:
        '''
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
        super().closeEvent(*args, **kwargs)
        self.app.closeAllWindows()

    def showPreferences(self):
        '''
        Shows the preferences dialog.
        '''
        PreferencesDialog(self.settings, self.__style_path_root, parent=self).exec()

    def addFilter(self):
        '''
        Adds a filter via the filter dialog.
        '''
        FilterDialog(self.__filterModel, fs=int(self.settings.value(ANALYSIS_TARGET_FS))).exec()

    def editFilter(self):
        '''
        Edits the currently selected filter via the filter dialog.
        '''
        selection = self.filterView.selectionModel()
        if selection.hasSelection() and len(selection.selectedRows()) == 1:
            FilterDialog(self.__filterModel, filter=self.__filterModel[selection.selectedRows()[0].row()]).exec()

    def deleteFilter(self):
        '''
        Deletes the selected filters.
        '''
        selection = self.filterView.selectionModel()
        if selection.hasSelection():
            self.__filterModel.delete([x.row() for x in selection.selectedRows()])

    def addSignal(self):
        '''
        Adds signals via the signal dialog.
        '''
        SignalDialog(self.settings, self.__signalModel, parent=self).exec()

    def deleteSignal(self):
        '''
        Deletes the currently selected signals.
        '''
        selection = self.signalView.selectionModel()
        if selection.hasSelection():
            self.__signalModel.delete([x.row() for x in selection.selectedRows()])

    def changeFilterButtonState(self):
        '''
        Enables the edit & delete button if there are selected rows.
        '''
        selection = self.filterView.selectionModel()
        self.deleteFilterButton.setEnabled(selection.hasSelection())
        self.editFilterButton.setEnabled(len(selection.selectedRows()) == 1)

    def changeSignalButtonState(self):
        '''
        Enables the edit & delete button if there are selected rows.
        '''
        selection = self.signalView.selectionModel()
        self.deleteSignalButton.setEnabled(selection.hasSelection())
        self.editSignalButton.setEnabled(len(selection.selectedRows()) == 1)

    def update_reference_series(self, names, combo, primary=True):
        '''
        Updates the reference series dropdown with the current curve names.
        '''
        current_reference = combo.currentText()
        try:
            combo.blockSignals(True)
            combo.clear()
            combo.addItem('None')
            for name in names:
                combo.addItem(name)
            idx = combo.findText(current_reference)
            if idx != -1:
                combo.setCurrentIndex(idx)
        finally:
            combo.blockSignals(False)

    def showExtractAudioDialog(self):
        '''
        Show the extract audio dialog.
        '''
        ExtractAudioDialog(self.settings, parent=self).exec()

    def normaliseSignalMagnitude(self):
        '''
        Handles reference series change.
        '''
        if self.signalReference.currentText() == 'None':
            self.__magnitudeModel.normalise(primary=True)
        else:
            self.__magnitudeModel.normalise(primary=True, curve=self.signalReference.currentText())

    def normaliseFilterMagnitude(self):
        '''
        Handles reference series change.
        '''
        if self.filterReference.currentText() == 'None':
            self.__magnitudeModel.normalise(primary=False)
        else:
            self.__magnitudeModel.normalise(primary=False, curve=self.filterReference.currentText())

    def showLimits(self):
        '''
        Shows the limits dialog for the main chart.
        '''
        self.__magnitudeModel.show_limits()

    def showValues(self):
        '''
        Shows the values dialog for the main chart.
        '''
        self.__magnitudeModel.show_values()

    def changeVisibilityOfIndividualFilters(self):
        '''
        Updates the filter reference series selector.
        '''
        self.__filterModel.post_update(filter_change=False)


class SaveChartDialog(QDialog, Ui_saveChartDialog):
    '''
    Save Chart dialog
    '''

    def __init__(self, parent, name, figure, statusbar):
        super(SaveChartDialog, self).__init__(parent)
        self.setupUi(self)
        self.name = name
        self.figure = figure
        self.__dpi = self.figure.dpi
        self.__x, self.__y = self.figure.get_size_inches() * self.figure.dpi
        self.__aspectRatio = self.__x / self.__y
        self.widthPixels.setValue(self.__x)
        self.heightPixels.setValue(self.__y)
        self.statusbar = statusbar
        self.__dialog = QFileDialog(parent=self)

    def accept(self):
        formats = "Portable Network Graphic (*.png)"
        fileName = self.__dialog.getSaveFileName(self, 'Export Chart', f"{self.name}.png", formats)
        if fileName:
            outputFile = str(fileName[0]).strip()
            if len(outputFile) == 0:
                return
            else:
                scaleFactor = self.widthPixels.value() / self.__x
                self.figure.savefig(outputFile, format='png', dpi=self.__dpi * scaleFactor)
                self.statusbar.showMessage(f"Saved {self.name} to {outputFile}", 5000)
        QDialog.accept(self)

    def updateHeight(self, newWidth):
        '''
        Updates the height as the width changes according to the aspect ratio.
        :param newWidth: the new width.
        '''
        self.heightPixels.setValue(int(math.floor(newWidth / self.__aspectRatio)))


class ExportBiquadDialog(QDialog, Ui_exportBiquadDialog):
    '''
    Export Biquads Dialog
    '''

    def __init__(self, filter):
        super(ExportBiquadDialog, self).__init__()
        self.setupUi(self)
        self.__filter = filter
        self.updateBiquads()

    def updateBiquads(self):
        if self.__filter is not None and len(self.__filter) > 0:
            self.__filter = self.__filter.resample(int(self.fs.currentText()))
            biquads = list(flatten([self.__filter.format_biquads(self.minidspFormat.isChecked())]))
            if len(biquads) < self.maxBiquads.value():
                passthrough = [Passthrough()] * (self.maxBiquads.value() - len(biquads))
                biquads.extend(passthrough)
            text = "\n".join([f"biquad{idx},\n{bq}" for idx, bq in enumerate(biquads)])
            self.biquads.setPlainText(text)


def flatten(l):
    '''
    flatten an irregularly shaped list of lists (of lists of lists...)
    solution from https://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists
    '''
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


def make_app():
    app = QApplication(sys.argv)
    if getattr(sys, 'frozen', False):
        icon_path = os.path.join(sys._MEIPASS, 'Icon.ico')
    else:
        icon_path = os.path.abspath(os.path.join(os.path.dirname('__file__'), '../icons/Icon.ico'))
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    return app


if __name__ == '__main__':
    app = make_app()
    form = BeqDesigner(app)
    # setup the error handler
    e_dialog = QErrorMessage(form)
    e_dialog.setWindowModality(QtCore.Qt.WindowModal)
    font = QFont()
    font.setFamily("Consolas")
    font.setPointSize(8)
    e_dialog.setFont(font)
    # add the exception handler so we can see the errors in a QErrorMessage
    sys._excepthook = sys.excepthook


    def dump_exception_to_log(exctype, value, tb):
        import traceback
        global e_dialog
        if e_dialog is not None:
            formatted = traceback.format_exception(etype=exctype, value=value, tb=tb)
            msg = '<br>'.join(formatted)
            e_dialog.setWindowTitle('Unexpected Error')
            e_dialog.showMessage(msg)
            e_dialog.resize(1200, 400)
        else:
            print(exctype, value, tb)


    sys.excepthook = dump_exception_to_log

    # show the form and exec the app
    form.show()
    app.exec_()
