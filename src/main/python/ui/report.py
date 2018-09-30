# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_saveReportDialog(object):
    def setupUi(self, saveReportDialog):
        saveReportDialog.setObjectName("saveReportDialog")
        saveReportDialog.resize(1532, 1145)
        self.gridLayout_2 = QtWidgets.QGridLayout(saveReportDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.widthSpacing = QtWidgets.QDoubleSpinBox(saveReportDialog)
        self.widthSpacing.setMaximum(1.0)
        self.widthSpacing.setSingleStep(0.01)
        self.widthSpacing.setObjectName("widthSpacing")
        self.gridLayout.addWidget(self.widthSpacing, 24, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.x0 = QtWidgets.QDoubleSpinBox(saveReportDialog)
        self.x0.setDecimals(3)
        self.x0.setMaximum(0.999)
        self.x0.setSingleStep(0.001)
        self.x0.setProperty("value", 0.748)
        self.x0.setObjectName("x0")
        self.horizontalLayout_3.addWidget(self.x0)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.x1 = QtWidgets.QDoubleSpinBox(saveReportDialog)
        self.x1.setDecimals(3)
        self.x1.setMaximum(1.0)
        self.x1.setSingleStep(0.001)
        self.x1.setProperty("value", 1.0)
        self.x1.setObjectName("x1")
        self.horizontalLayout_3.addWidget(self.x1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 12, 1, 1, 1)
        self.showTableHeader = QtWidgets.QCheckBox(saveReportDialog)
        self.showTableHeader.setObjectName("showTableHeader")
        self.gridLayout.addWidget(self.showTableHeader, 18, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.imageWidthPixels = QtWidgets.QSpinBox(saveReportDialog)
        self.imageWidthPixels.setEnabled(False)
        self.imageWidthPixels.setMinimum(0)
        self.imageWidthPixels.setMaximum(999999)
        self.imageWidthPixels.setObjectName("imageWidthPixels")
        self.horizontalLayout_6.addWidget(self.imageWidthPixels)
        self.label_3 = QtWidgets.QLabel(saveReportDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.imageHeightPixels = QtWidgets.QSpinBox(saveReportDialog)
        self.imageHeightPixels.setEnabled(False)
        self.imageHeightPixels.setMinimum(0)
        self.imageHeightPixels.setMaximum(999999)
        self.imageHeightPixels.setObjectName("imageHeightPixels")
        self.horizontalLayout_6.addWidget(self.imageHeightPixels)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 1, 1, 1)
        self.titleLabel = QtWidgets.QLabel(saveReportDialog)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 5, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.y0 = QtWidgets.QDoubleSpinBox(saveReportDialog)
        self.y0.setDecimals(3)
        self.y0.setMaximum(0.999)
        self.y0.setSingleStep(0.001)
        self.y0.setProperty("value", 0.75)
        self.y0.setObjectName("y0")
        self.horizontalLayout_4.addWidget(self.y0)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 13, 1, 1, 1)
        self.curvesLabel = QtWidgets.QLabel(saveReportDialog)
        self.curvesLabel.setObjectName("curvesLabel")
        self.gridLayout.addWidget(self.curvesLabel, 28, 0, 1, 1)
        self.filtersLabel = QtWidgets.QLabel(saveReportDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.filtersLabel.setFont(font)
        self.filtersLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.filtersLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.filtersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.filtersLabel.setObjectName("filtersLabel")
        self.gridLayout.addWidget(self.filtersLabel, 9, 0, 1, 3)
        self.layoutLabel = QtWidgets.QLabel(saveReportDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.layoutLabel.setFont(font)
        self.layoutLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.layoutLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.layoutLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.layoutLabel.setObjectName("layoutLabel")
        self.gridLayout.addWidget(self.layoutLabel, 19, 0, 1, 3)
        self.buttonBox = QtWidgets.QDialogButtonBox(saveReportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.RestoreDefaults|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 31, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(saveReportDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.tableAlpha = QtWidgets.QDoubleSpinBox(saveReportDialog)
        self.tableAlpha.setMinimum(0.01)
        self.tableAlpha.setMaximum(1.0)
        self.tableAlpha.setSingleStep(0.01)
        self.tableAlpha.setProperty("value", 1.0)
        self.tableAlpha.setObjectName("tableAlpha")
        self.gridLayout.addWidget(self.tableAlpha, 16, 1, 1, 1)
        self.tableRowHeightLabel = QtWidgets.QLabel(saveReportDialog)
        self.tableRowHeightLabel.setObjectName("tableRowHeightLabel")
        self.gridLayout.addWidget(self.tableRowHeightLabel, 10, 0, 1, 1)
        self.tableAlphaLabel = QtWidgets.QLabel(saveReportDialog)
        self.tableAlphaLabel.setObjectName("tableAlphaLabel")
        self.gridLayout.addWidget(self.tableAlphaLabel, 16, 0, 1, 1)
        self.imageBorder = QtWidgets.QCheckBox(saveReportDialog)
        self.imageBorder.setObjectName("imageBorder")
        self.gridLayout.addWidget(self.imageBorder, 8, 1, 1, 1)
        self.gridOpacity = QtWidgets.QDoubleSpinBox(saveReportDialog)
        self.gridOpacity.setMaximum(1.0)
        self.gridOpacity.setSingleStep(0.01)
        self.gridOpacity.setProperty("value", 0.4)
        self.gridOpacity.setObjectName("gridOpacity")
        self.gridLayout.addWidget(self.gridOpacity, 27, 1, 1, 1)
        self.tableFontSizeLabel = QtWidgets.QLabel(saveReportDialog)
        self.tableFontSizeLabel.setObjectName("tableFontSizeLabel")
        self.gridLayout.addWidget(self.tableFontSizeLabel, 17, 0, 1, 1)
        self.tableFontSize = QtWidgets.QSpinBox(saveReportDialog)
        self.tableFontSize.setMaximum(24)
        self.tableFontSize.setProperty("value", 10)
        self.tableFontSize.setObjectName("tableFontSize")
        self.gridLayout.addWidget(self.tableFontSize, 17, 1, 1, 1)
        self.imageOpacity = QtWidgets.QDoubleSpinBox(saveReportDialog)
        self.imageOpacity.setDecimals(2)
        self.imageOpacity.setMinimum(0.01)
        self.imageOpacity.setMaximum(1.0)
        self.imageOpacity.setSingleStep(0.01)
        self.imageOpacity.setProperty("value", 1.0)
        self.imageOpacity.setObjectName("imageOpacity")
        self.gridLayout.addWidget(self.imageOpacity, 4, 1, 1, 1)
        self.image = QtWidgets.QLineEdit(saveReportDialog)
        self.image.setEnabled(True)
        self.image.setReadOnly(True)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 1, 1, 1, 1)
        self.imagePicker = QtWidgets.QToolButton(saveReportDialog)
        self.imagePicker.setObjectName("imagePicker")
        self.gridLayout.addWidget(self.imagePicker, 1, 2, 1, 1)
        self.imageFileLabel = QtWidgets.QLabel(saveReportDialog)
        self.imageFileLabel.setObjectName("imageFileLabel")
        self.gridLayout.addWidget(self.imageFileLabel, 1, 0, 1, 1)
        self.chartLabel = QtWidgets.QLabel(saveReportDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chartLabel.setFont(font)
        self.chartLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.chartLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.chartLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.chartLabel.setObjectName("chartLabel")
        self.gridLayout.addWidget(self.chartLabel, 26, 0, 1, 3)
        self.showLegend = QtWidgets.QCheckBox(saveReportDialog)
        self.showLegend.setObjectName("showLegend")
        self.gridLayout.addWidget(self.showLegend, 29, 1, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.saveLayout = QtWidgets.QPushButton(saveReportDialog)
        self.saveLayout.setObjectName("saveLayout")
        self.horizontalLayout_5.addWidget(self.saveLayout)
        self.gridLayout.addLayout(self.horizontalLayout_5, 30, 1, 1, 1)
        self.titleFontSizeLabel = QtWidgets.QLabel(saveReportDialog)
        self.titleFontSizeLabel.setObjectName("titleFontSizeLabel")
        self.gridLayout.addWidget(self.titleFontSizeLabel, 6, 0, 1, 1)
        self.tablePositionLabel = QtWidgets.QLabel(saveReportDialog)
        self.tablePositionLabel.setObjectName("tablePositionLabel")
        self.gridLayout.addWidget(self.tablePositionLabel, 11, 0, 5, 1)
        self.majorSplitRatioLabel = QtWidgets.QLabel(saveReportDialog)
        self.majorSplitRatioLabel.setObjectName("majorSplitRatioLabel")
        self.gridLayout.addWidget(self.majorSplitRatioLabel, 20, 0, 1, 1)
        self.limitsButton = QtWidgets.QToolButton(saveReportDialog)
        self.limitsButton.setObjectName("limitsButton")
        self.gridLayout.addWidget(self.limitsButton, 27, 2, 1, 1)
        self.curves = QtWidgets.QListWidget(saveReportDialog)
        self.curves.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.curves.setObjectName("curves")
        self.gridLayout.addWidget(self.curves, 28, 1, 1, 1)
        self.filterRowHeightMultiplier = QtWidgets.QDoubleSpinBox(saveReportDialog)
        self.filterRowHeightMultiplier.setMaximum(3.0)
        self.filterRowHeightMultiplier.setSingleStep(0.01)
        self.filterRowHeightMultiplier.setProperty("value", 1.2)
        self.filterRowHeightMultiplier.setObjectName("filterRowHeightMultiplier")
        self.gridLayout.addWidget(self.filterRowHeightMultiplier, 10, 1, 1, 1)
        self.imageURLLabel = QtWidgets.QLabel(saveReportDialog)
        self.imageURLLabel.setObjectName("imageURLLabel")
        self.gridLayout.addWidget(self.imageURLLabel, 2, 0, 1, 1)
        self.loadURL = QtWidgets.QToolButton(saveReportDialog)
        self.loadURL.setObjectName("loadURL")
        self.gridLayout.addWidget(self.loadURL, 2, 2, 1, 1)
        self.imageAlphaLabel = QtWidgets.QLabel(saveReportDialog)
        self.imageAlphaLabel.setObjectName("imageAlphaLabel")
        self.gridLayout.addWidget(self.imageAlphaLabel, 4, 0, 1, 1)
        self.imageURL = QtWidgets.QLineEdit(saveReportDialog)
        self.imageURL.setObjectName("imageURL")
        self.gridLayout.addWidget(self.imageURL, 2, 1, 1, 1)
        self.titleFontSize = QtWidgets.QSpinBox(saveReportDialog)
        self.titleFontSize.setObjectName("titleFontSize")
        self.gridLayout.addWidget(self.titleFontSize, 6, 1, 1, 1)
        self.title = QtWidgets.QLineEdit(saveReportDialog)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 5, 1, 1, 1)
        self.gridAlphaLabel = QtWidgets.QLabel(saveReportDialog)
        self.gridAlphaLabel.setObjectName("gridAlphaLabel")
        self.gridLayout.addWidget(self.gridAlphaLabel, 27, 0, 1, 1)
        self.imageLabel = QtWidgets.QLabel(saveReportDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.imageLabel.setFont(font)
        self.imageLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.gridLayout.addWidget(self.imageLabel, 0, 0, 1, 3)
        self.widthLabel = QtWidgets.QLabel(saveReportDialog)
        self.widthLabel.setObjectName("widthLabel")
        self.gridLayout.addWidget(self.widthLabel, 7, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.y1 = QtWidgets.QDoubleSpinBox(saveReportDialog)
        self.y1.setDecimals(3)
        self.y1.setMaximum(1.0)
        self.y1.setSingleStep(0.001)
        self.y1.setProperty("value", 1.0)
        self.y1.setObjectName("y1")
        self.horizontalLayout_2.addWidget(self.y1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 11, 1, 1, 1)
        self.chartSplitLabel = QtWidgets.QLabel(saveReportDialog)
        self.chartSplitLabel.setObjectName("chartSplitLabel")
        self.gridLayout.addWidget(self.chartSplitLabel, 21, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(saveReportDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 24, 0, 1, 1)
        self.label = QtWidgets.QLabel(saveReportDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 23, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widthPixels = QtWidgets.QSpinBox(saveReportDialog)
        self.widthPixels.setMinimum(512)
        self.widthPixels.setMaximum(8192)
        self.widthPixels.setObjectName("widthPixels")
        self.horizontalLayout_7.addWidget(self.widthPixels)
        self.label_2 = QtWidgets.QLabel(saveReportDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.heightPixels = QtWidgets.QSpinBox(saveReportDialog)
        self.heightPixels.setMinimum(512)
        self.heightPixels.setMaximum(8192)
        self.heightPixels.setObjectName("heightPixels")
        self.horizontalLayout_7.addWidget(self.heightPixels)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_7, 23, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(saveReportDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 22, 0, 1, 1)
        self.chartSplit = QtWidgets.QComboBox(saveReportDialog)
        self.chartSplit.setObjectName("chartSplit")
        self.chartSplit.addItem("")
        self.chartSplit.addItem("")
        self.gridLayout.addWidget(self.chartSplit, 21, 1, 1, 1)
        self.chartLayout = QtWidgets.QComboBox(saveReportDialog)
        self.chartLayout.setObjectName("chartLayout")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.chartLayout.addItem("")
        self.gridLayout.addWidget(self.chartLayout, 22, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.majorSplitRatio = QtWidgets.QDoubleSpinBox(saveReportDialog)
        self.majorSplitRatio.setDecimals(3)
        self.majorSplitRatio.setMinimum(0.1)
        self.majorSplitRatio.setMaximum(10.0)
        self.majorSplitRatio.setSingleStep(0.001)
        self.majorSplitRatio.setProperty("value", 1.0)
        self.majorSplitRatio.setObjectName("majorSplitRatio")
        self.horizontalLayout_9.addWidget(self.majorSplitRatio)
        self.minorSplitRatio = QtWidgets.QDoubleSpinBox(saveReportDialog)
        self.minorSplitRatio.setDecimals(3)
        self.minorSplitRatio.setMinimum(0.001)
        self.minorSplitRatio.setMaximum(10.0)
        self.minorSplitRatio.setSingleStep(0.001)
        self.minorSplitRatio.setProperty("value", 3.0)
        self.minorSplitRatio.setObjectName("minorSplitRatio")
        self.horizontalLayout_9.addWidget(self.minorSplitRatio)
        self.gridLayout.addLayout(self.horizontalLayout_9, 20, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.nativeImageWidth = QtWidgets.QSpinBox(saveReportDialog)
        self.nativeImageWidth.setEnabled(False)
        self.nativeImageWidth.setMaximum(99999)
        self.nativeImageWidth.setObjectName("nativeImageWidth")
        self.horizontalLayout_8.addWidget(self.nativeImageWidth)
        self.label_5 = QtWidgets.QLabel(saveReportDialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.nativeImageHeight = QtWidgets.QSpinBox(saveReportDialog)
        self.nativeImageHeight.setEnabled(False)
        self.nativeImageHeight.setMaximum(99999)
        self.nativeImageHeight.setObjectName("nativeImageHeight")
        self.horizontalLayout_8.addWidget(self.nativeImageHeight)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(saveReportDialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 25, 0, 1, 1)
        self.heightSpacing = QtWidgets.QDoubleSpinBox(saveReportDialog)
        self.heightSpacing.setMaximum(1.0)
        self.heightSpacing.setSingleStep(0.01)
        self.heightSpacing.setObjectName("heightSpacing")
        self.gridLayout.addWidget(self.heightSpacing, 25, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.preview = MplWidget(saveReportDialog)
        self.preview.setObjectName("preview")
        self.horizontalLayout.addWidget(self.preview)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.retranslateUi(saveReportDialog)
        self.chartSplit.setCurrentIndex(1)
        self.chartLayout.setCurrentIndex(0)
        self.buttonBox.accepted.connect(saveReportDialog.accept)
        self.buttonBox.rejected.connect(saveReportDialog.reject)
        self.curves.itemSelectionChanged.connect(saveReportDialog.set_selected)
        self.widthPixels.valueChanged['int'].connect(saveReportDialog.update_height)
        self.showLegend.clicked.connect(saveReportDialog.redraw)
        self.imagePicker.clicked.connect(saveReportDialog.choose_image)
        self.title.textChanged['QString'].connect(saveReportDialog.set_title)
        self.titleFontSize.valueChanged['int'].connect(saveReportDialog.set_title)
        self.majorSplitRatio.valueChanged['double'].connect(saveReportDialog.redraw_all_axes)
        self.chartSplit.currentIndexChanged['int'].connect(saveReportDialog.redraw_all_axes)
        self.limitsButton.clicked.connect(saveReportDialog.show_limits)
        self.chartSplit.currentIndexChanged['int'].connect(saveReportDialog.redraw_all_axes)
        self.chartLayout.currentIndexChanged['int'].connect(saveReportDialog.redraw_all_axes)
        self.minorSplitRatio.valueChanged['double'].connect(saveReportDialog.redraw_all_axes)
        self.gridOpacity.valueChanged['double'].connect(saveReportDialog.set_grid_opacity)
        self.imageOpacity.valueChanged['double'].connect(saveReportDialog.set_image_opacity)
        self.filterRowHeightMultiplier.valueChanged['double'].connect(saveReportDialog.replace_table)
        self.y0.valueChanged['double'].connect(saveReportDialog.replace_table)
        self.x0.valueChanged['double'].connect(saveReportDialog.replace_table)
        self.y1.valueChanged['double'].connect(saveReportDialog.replace_table)
        self.x1.valueChanged['double'].connect(saveReportDialog.replace_table)
        self.saveLayout.clicked.connect(saveReportDialog.save_layout)
        self.imageURL.textChanged['QString'].connect(saveReportDialog.update_image_url)
        self.loadURL.clicked.connect(saveReportDialog.load_image_from_url)
        self.tableAlpha.valueChanged['double'].connect(saveReportDialog.replace_table)
        self.tableFontSize.valueChanged['int'].connect(saveReportDialog.replace_table)
        self.showTableHeader.clicked.connect(saveReportDialog.replace_table)
        self.imageBorder.clicked.connect(saveReportDialog.set_image_border)
        self.widthSpacing.valueChanged['double'].connect(saveReportDialog.redraw_all_axes)
        self.heightSpacing.valueChanged['double'].connect(saveReportDialog.redraw_all_axes)
        QtCore.QMetaObject.connectSlotsByName(saveReportDialog)
        saveReportDialog.setTabOrder(self.imagePicker, self.imageURL)
        saveReportDialog.setTabOrder(self.imageURL, self.loadURL)
        saveReportDialog.setTabOrder(self.loadURL, self.imageOpacity)
        saveReportDialog.setTabOrder(self.imageOpacity, self.title)
        saveReportDialog.setTabOrder(self.title, self.titleFontSize)
        saveReportDialog.setTabOrder(self.titleFontSize, self.filterRowHeightMultiplier)
        saveReportDialog.setTabOrder(self.filterRowHeightMultiplier, self.x0)
        saveReportDialog.setTabOrder(self.x0, self.y0)
        saveReportDialog.setTabOrder(self.y0, self.x1)
        saveReportDialog.setTabOrder(self.x1, self.y1)
        saveReportDialog.setTabOrder(self.y1, self.tableAlpha)
        saveReportDialog.setTabOrder(self.tableAlpha, self.tableFontSize)
        saveReportDialog.setTabOrder(self.tableFontSize, self.gridOpacity)
        saveReportDialog.setTabOrder(self.gridOpacity, self.curves)
        saveReportDialog.setTabOrder(self.curves, self.showLegend)
        saveReportDialog.setTabOrder(self.showLegend, self.limitsButton)
        saveReportDialog.setTabOrder(self.limitsButton, self.saveLayout)
        saveReportDialog.setTabOrder(self.saveLayout, self.preview)
        saveReportDialog.setTabOrder(self.preview, self.image)

    def retranslateUi(self, saveReportDialog):
        _translate = QtCore.QCoreApplication.translate
        saveReportDialog.setWindowTitle(_translate("saveReportDialog", "Save Report"))
        self.showTableHeader.setText(_translate("saveReportDialog", "Show Header?"))
        self.label_3.setText(_translate("saveReportDialog", "x"))
        self.titleLabel.setText(_translate("saveReportDialog", "Title"))
        self.curvesLabel.setText(_translate("saveReportDialog", "Curves"))
        self.filtersLabel.setText(_translate("saveReportDialog", "Filters"))
        self.layoutLabel.setText(_translate("saveReportDialog", "Layout"))
        self.label_4.setText(_translate("saveReportDialog", "Native Size"))
        self.tableRowHeightLabel.setText(_translate("saveReportDialog", "Row Height"))
        self.tableAlphaLabel.setText(_translate("saveReportDialog", "Alpha"))
        self.imageBorder.setText(_translate("saveReportDialog", "Show Border?"))
        self.tableFontSizeLabel.setText(_translate("saveReportDialog", "Font Size"))
        self.imagePicker.setText(_translate("saveReportDialog", "..."))
        self.imageFileLabel.setText(_translate("saveReportDialog", "File"))
        self.chartLabel.setText(_translate("saveReportDialog", "Chart"))
        self.showLegend.setText(_translate("saveReportDialog", "Show Legend?"))
        self.saveLayout.setText(_translate("saveReportDialog", "Save Layout"))
        self.titleFontSizeLabel.setText(_translate("saveReportDialog", "Font Size"))
        self.tablePositionLabel.setText(_translate("saveReportDialog", "Position"))
        self.majorSplitRatioLabel.setText(_translate("saveReportDialog", "Major/Minor Ratio"))
        self.limitsButton.setText(_translate("saveReportDialog", "..."))
        self.imageURLLabel.setText(_translate("saveReportDialog", "URL"))
        self.loadURL.setText(_translate("saveReportDialog", "..."))
        self.imageAlphaLabel.setText(_translate("saveReportDialog", "Alpha"))
        self.gridAlphaLabel.setText(_translate("saveReportDialog", "Grid Alpha"))
        self.imageLabel.setText(_translate("saveReportDialog", "Image"))
        self.widthLabel.setText(_translate("saveReportDialog", "Actual Size"))
        self.chartSplitLabel.setText(_translate("saveReportDialog", "Split"))
        self.label_6.setText(_translate("saveReportDialog", "Width Spacing"))
        self.label.setText(_translate("saveReportDialog", "Size"))
        self.label_2.setText(_translate("saveReportDialog", "x"))
        self.label_7.setText(_translate("saveReportDialog", "Layout"))
        self.chartSplit.setItemText(0, _translate("saveReportDialog", "Horizontal"))
        self.chartSplit.setItemText(1, _translate("saveReportDialog", "Vertical"))
        self.chartLayout.setItemText(0, _translate("saveReportDialog", "Image | Chart, Filters"))
        self.chartLayout.setItemText(1, _translate("saveReportDialog", "Image | Filters, Chart"))
        self.chartLayout.setItemText(2, _translate("saveReportDialog", "Chart | Image, Filter"))
        self.chartLayout.setItemText(3, _translate("saveReportDialog", "Chart | Filters, Image"))
        self.chartLayout.setItemText(4, _translate("saveReportDialog", "Filters | Image, Chart"))
        self.chartLayout.setItemText(5, _translate("saveReportDialog", "Filters | Chart, Image"))
        self.chartLayout.setItemText(6, _translate("saveReportDialog", "Image, Filters | Chart"))
        self.chartLayout.setItemText(7, _translate("saveReportDialog", "Filters, Image | Chart"))
        self.chartLayout.setItemText(8, _translate("saveReportDialog", "Chart, Image | Filters"))
        self.chartLayout.setItemText(9, _translate("saveReportDialog", "Image, Chart | Filters"))
        self.chartLayout.setItemText(10, _translate("saveReportDialog", "Filters, Chart | Image"))
        self.chartLayout.setItemText(11, _translate("saveReportDialog", "Chart, Filters | Image"))
        self.chartLayout.setItemText(12, _translate("saveReportDialog", "Chart | Filters"))
        self.chartLayout.setItemText(13, _translate("saveReportDialog", "Filters | Chart"))
        self.chartLayout.setItemText(14, _translate("saveReportDialog", "Chart | Image"))
        self.chartLayout.setItemText(15, _translate("saveReportDialog", "Image | Chart"))
        self.chartLayout.setItemText(16, _translate("saveReportDialog", "Pixel Perfect Image | Chart"))
        self.label_5.setText(_translate("saveReportDialog", "x"))
        self.label_8.setText(_translate("saveReportDialog", "Height Spacing"))

from mpl import MplWidget
