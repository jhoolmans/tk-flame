# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_create_dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_ProjectCreateDialog(object):
    def setupUi(self, ProjectCreateDialog):
        ProjectCreateDialog.setObjectName("ProjectCreateDialog")
        ProjectCreateDialog.resize(446, 496)
        ProjectCreateDialog.setStyleSheet("/* this is to force the combo box dropdowns to show all items rather than displaying only a few items and a scroll bar */\n"
"QComboBox QListView {\n"
"height: 100px;\n"
"}")
        self.verticalLayout = QtGui.QVBoxLayout(ProjectCreateDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtGui.QLabel(ProjectCreateDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/tk-flame/icon.png"))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.tabWidget = QtGui.QTabWidget(ProjectCreateDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.project_overview_tab = QtGui.QWidget()
        self.project_overview_tab.setObjectName("project_overview_tab")
        self.formLayout_3 = QtGui.QFormLayout(self.project_overview_tab)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QtGui.QLabel(self.project_overview_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.project_name = QtGui.QLabel(self.project_overview_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_name.sizePolicy().hasHeightForWidth())
        self.project_name.setSizePolicy(sizePolicy)
        self.project_name.setMinimumSize(QtCore.QSize(200, 0))
        self.project_name.setWordWrap(False)
        self.project_name.setObjectName("project_name")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.project_name)
        self.label_7 = QtGui.QLabel(self.project_overview_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.volume = QtGui.QComboBox(self.project_overview_tab)
        self.volume.setObjectName("volume")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.volume)
        self.label_6 = QtGui.QLabel(self.project_overview_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.user_name = QtGui.QLabel(self.project_overview_tab)
        self.user_name.setWordWrap(False)
        self.user_name.setObjectName("user_name")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.user_name)
        self.label_19 = QtGui.QLabel(self.project_overview_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_19)
        self.host_name = QtGui.QLabel(self.project_overview_tab)
        self.host_name.setWordWrap(False)
        self.host_name.setObjectName("host_name")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.host_name)
        self.label_17 = QtGui.QLabel(self.project_overview_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_17)
        self.workspace_name = QtGui.QLabel(self.project_overview_tab)
        self.workspace_name.setWordWrap(False)
        self.workspace_name.setObjectName("workspace_name")
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.workspace_name)
        self.tabWidget.addTab(self.project_overview_tab, "")
        self.resolution_tab = QtGui.QWidget()
        self.resolution_tab.setObjectName("resolution_tab")
        self.formLayout_2 = QtGui.QFormLayout(self.resolution_tab)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtGui.QLabel(self.resolution_tab)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.width = QtGui.QLineEdit(self.resolution_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.width.sizePolicy().hasHeightForWidth())
        self.width.setSizePolicy(sizePolicy)
        self.width.setMinimumSize(QtCore.QSize(50, 0))
        self.width.setMaximumSize(QtCore.QSize(50, 16777215))
        self.width.setObjectName("width")
        self.horizontalLayout.addWidget(self.width)
        self.label_2 = QtGui.QLabel(self.resolution_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.height = QtGui.QLineEdit(self.resolution_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.height.sizePolicy().hasHeightForWidth())
        self.height.setSizePolicy(sizePolicy)
        self.height.setMaximumSize(QtCore.QSize(50, 16777215))
        self.height.setObjectName("height")
        self.horizontalLayout.addWidget(self.height)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_26 = QtGui.QLabel(self.resolution_tab)
        self.label_26.setObjectName("label_26")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_26)
        self.aspect_ratio = QtGui.QComboBox(self.resolution_tab)
        self.aspect_ratio.setMaxVisibleItems(100)
        self.aspect_ratio.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.aspect_ratio.setObjectName("aspect_ratio")
        self.aspect_ratio.addItem("")
        self.aspect_ratio.addItem("")
        self.aspect_ratio.addItem("")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.aspect_ratio)
        self.label_27 = QtGui.QLabel(self.resolution_tab)
        self.label_27.setObjectName("label_27")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_27)
        self.frame_rate = QtGui.QComboBox(self.resolution_tab)
        self.frame_rate.setMaxVisibleItems(100)
        self.frame_rate.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.frame_rate.setObjectName("frame_rate")
        self.frame_rate.addItem("")
        self.frame_rate.addItem("")
        self.frame_rate.addItem("")
        self.frame_rate.addItem("")
        self.frame_rate.addItem("")
        self.frame_rate.addItem("")
        self.frame_rate.addItem("")
        self.frame_rate.addItem("")
        self.frame_rate.addItem("")
        self.frame_rate.addItem("")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.frame_rate)
        self.label_3 = QtGui.QLabel(self.resolution_tab)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.depth = QtGui.QComboBox(self.resolution_tab)
        self.depth.setMaxVisibleItems(100)
        self.depth.setObjectName("depth")
        self.depth.addItem("")
        self.depth.addItem("")
        self.depth.addItem("")
        self.depth.addItem("")
        self.depth.addItem("")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.depth)
        self.label_10 = QtGui.QLabel(self.resolution_tab)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_10)
        self.field_dominance = QtGui.QComboBox(self.resolution_tab)
        self.field_dominance.setMaxVisibleItems(100)
        self.field_dominance.setObjectName("field_dominance")
        self.field_dominance.addItem("")
        self.field_dominance.addItem("")
        self.field_dominance.addItem("")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.field_dominance)
        self.tabWidget.addTab(self.resolution_tab, "")
        self.old_proxy_tab = QtGui.QWidget()
        self.old_proxy_tab.setObjectName("old_proxy_tab")
        self.formLayout = QtGui.QFormLayout(self.old_proxy_tab)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName("formLayout")
        self.proxy_depth_label_2 = QtGui.QLabel(self.old_proxy_tab)
        self.proxy_depth_label_2.setObjectName("proxy_depth_label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.proxy_depth_label_2)
        self.proxy_mode = QtGui.QComboBox(self.old_proxy_tab)
        self.proxy_mode.setMaxVisibleItems(100)
        self.proxy_mode.setObjectName("proxy_mode")
        self.proxy_mode.addItem("")
        self.proxy_mode.addItem("")
        self.proxy_mode.addItem("")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.proxy_mode)
        self.proxy_depth_label = QtGui.QLabel(self.old_proxy_tab)
        self.proxy_depth_label.setObjectName("proxy_depth_label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.proxy_depth_label)
        self.proxy_depth = QtGui.QComboBox(self.old_proxy_tab)
        self.proxy_depth.setMaxVisibleItems(100)
        self.proxy_depth.setObjectName("proxy_depth")
        self.proxy_depth.addItem("")
        self.proxy_depth.addItem("")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.proxy_depth)
        self.proxy_quality_label = QtGui.QLabel(self.old_proxy_tab)
        self.proxy_quality_label.setObjectName("proxy_quality_label")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.proxy_quality_label)
        self.proxy_quality = QtGui.QComboBox(self.old_proxy_tab)
        self.proxy_quality.setMaxVisibleItems(100)
        self.proxy_quality.setObjectName("proxy_quality")
        self.proxy_quality.addItem("")
        self.proxy_quality.addItem("")
        self.proxy_quality.addItem("")
        self.proxy_quality.addItem("")
        self.proxy_quality.addItem("")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.proxy_quality)
        self.proxy_width_hint_label = QtGui.QLabel(self.old_proxy_tab)
        self.proxy_width_hint_label.setObjectName("proxy_width_hint_label")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.proxy_width_hint_label)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.proxy_width_hint = QtGui.QSlider(self.old_proxy_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxy_width_hint.sizePolicy().hasHeightForWidth())
        self.proxy_width_hint.setSizePolicy(sizePolicy)
        self.proxy_width_hint.setMinimumSize(QtCore.QSize(100, 0))
        self.proxy_width_hint.setMinimum(24)
        self.proxy_width_hint.setMaximum(8192)
        self.proxy_width_hint.setSingleStep(4)
        self.proxy_width_hint.setPageStep(400)
        self.proxy_width_hint.setOrientation(QtCore.Qt.Horizontal)
        self.proxy_width_hint.setTickPosition(QtGui.QSlider.TicksBelow)
        self.proxy_width_hint.setTickInterval(400)
        self.proxy_width_hint.setObjectName("proxy_width_hint")
        self.horizontalLayout_6.addWidget(self.proxy_width_hint)
        self.proxy_width_hint_preview = QtGui.QLabel(self.old_proxy_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxy_width_hint_preview.sizePolicy().hasHeightForWidth())
        self.proxy_width_hint_preview.setSizePolicy(sizePolicy)
        self.proxy_width_hint_preview.setObjectName("proxy_width_hint_preview")
        self.horizontalLayout_6.addWidget(self.proxy_width_hint_preview)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.proxy_min_frame_size_label = QtGui.QLabel(self.old_proxy_tab)
        self.proxy_min_frame_size_label.setObjectName("proxy_min_frame_size_label")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.proxy_min_frame_size_label)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.proxy_min_frame_size = QtGui.QSlider(self.old_proxy_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxy_min_frame_size.sizePolicy().hasHeightForWidth())
        self.proxy_min_frame_size.setSizePolicy(sizePolicy)
        self.proxy_min_frame_size.setMinimumSize(QtCore.QSize(100, 0))
        self.proxy_min_frame_size.setMinimum(24)
        self.proxy_min_frame_size.setMaximum(8192)
        self.proxy_min_frame_size.setSingleStep(4)
        self.proxy_min_frame_size.setPageStep(400)
        self.proxy_min_frame_size.setOrientation(QtCore.Qt.Horizontal)
        self.proxy_min_frame_size.setTickPosition(QtGui.QSlider.TicksBelow)
        self.proxy_min_frame_size.setTickInterval(400)
        self.proxy_min_frame_size.setObjectName("proxy_min_frame_size")
        self.horizontalLayout_7.addWidget(self.proxy_min_frame_size)
        self.proxy_min_frame_size_preview = QtGui.QLabel(self.old_proxy_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxy_min_frame_size_preview.sizePolicy().hasHeightForWidth())
        self.proxy_min_frame_size_preview.setSizePolicy(sizePolicy)
        self.proxy_min_frame_size_preview.setObjectName("proxy_min_frame_size_preview")
        self.horizontalLayout_7.addWidget(self.proxy_min_frame_size_preview)
        self.proxy_above_8_bits = QtGui.QCheckBox(self.old_proxy_tab)
        self.proxy_above_8_bits.setObjectName("proxy_above_8_bits")
        self.horizontalLayout_7.addWidget(self.proxy_above_8_bits)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.tabWidget.addTab(self.old_proxy_tab, "")
        self.new_proxy_tab = QtGui.QWidget()
        self.new_proxy_tab.setObjectName("new_proxy_tab")
        self.formLayout_4 = QtGui.QFormLayout(self.new_proxy_tab)
        self.formLayout_4.setObjectName("formLayout_4")
        self.proxy_depth_label_3 = QtGui.QLabel(self.new_proxy_tab)
        self.proxy_depth_label_3.setObjectName("proxy_depth_label_3")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.proxy_depth_label_3)
        self.new_proxy_mode = QtGui.QComboBox(self.new_proxy_tab)
        self.new_proxy_mode.setMaxVisibleItems(100)
        self.new_proxy_mode.setObjectName("new_proxy_mode")
        self.new_proxy_mode.addItem("")
        self.new_proxy_mode.addItem("")
        self.new_proxy_mode.addItem("")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.new_proxy_mode)
        self.proxy_quality_label_2 = QtGui.QLabel(self.new_proxy_tab)
        self.proxy_quality_label_2.setObjectName("proxy_quality_label_2")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.proxy_quality_label_2)
        self.new_proxy_quality = QtGui.QComboBox(self.new_proxy_tab)
        self.new_proxy_quality.setMaxVisibleItems(100)
        self.new_proxy_quality.setObjectName("new_proxy_quality")
        self.new_proxy_quality.addItem("")
        self.new_proxy_quality.addItem("")
        self.new_proxy_quality.addItem("")
        self.new_proxy_quality.addItem("")
        self.new_proxy_quality.addItem("")
        self.new_proxy_quality.addItem("")
        self.new_proxy_quality.addItem("")
        self.new_proxy_quality.addItem("")
        self.new_proxy_quality.addItem("")
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.new_proxy_quality)
        self.proxy_min_frame_size_label_2 = QtGui.QLabel(self.new_proxy_tab)
        self.proxy_min_frame_size_label_2.setObjectName("proxy_min_frame_size_label_2")
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.LabelRole, self.proxy_min_frame_size_label_2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.new_proxy_width = QtGui.QSpinBox(self.new_proxy_tab)
        self.new_proxy_width.setMaximum(65536)
        self.new_proxy_width.setSingleStep(16)
        self.new_proxy_width.setObjectName("new_proxy_width")
        self.horizontalLayout_8.addWidget(self.new_proxy_width)
        self.new_proxy_width_label = QtGui.QLabel(self.new_proxy_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_proxy_width_label.sizePolicy().hasHeightForWidth())
        self.new_proxy_width_label.setSizePolicy(sizePolicy)
        self.new_proxy_width_label.setObjectName("new_proxy_width_label")
        self.horizontalLayout_8.addWidget(self.new_proxy_width_label)
        self.formLayout_4.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.new_generate_proxies = QtGui.QCheckBox(self.new_proxy_tab)
        self.new_generate_proxies.setObjectName("new_generate_proxies")
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.new_generate_proxies)
        self.tabWidget.addTab(self.new_proxy_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.help_link = QtGui.QLabel(ProjectCreateDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help_link.sizePolicy().hasHeightForWidth())
        self.help_link.setSizePolicy(sizePolicy)
        self.help_link.setObjectName("help_link")
        self.horizontalLayout_2.addWidget(self.help_link)
        self.abort = QtGui.QPushButton(ProjectCreateDialog)
        self.abort.setObjectName("abort")
        self.horizontalLayout_2.addWidget(self.abort)
        self.create_project = QtGui.QPushButton(ProjectCreateDialog)
        self.create_project.setObjectName("create_project")
        self.horizontalLayout_2.addWidget(self.create_project)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ProjectCreateDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ProjectCreateDialog)

    def retranslateUi(self, ProjectCreateDialog):
        ProjectCreateDialog.setWindowTitle(QtGui.QApplication.translate("ProjectCreateDialog", "Submit to Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ProjectCreateDialog", "<b>Project Name</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.project_name.setToolTip(QtGui.QApplication.translate("ProjectCreateDialog", "The <b>Flame project name</b> is automatically generated based on your current Shotgun project. ", None, QtGui.QApplication.UnicodeUTF8))
        self.project_name.setText(QtGui.QApplication.translate("ProjectCreateDialog", "xxx", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ProjectCreateDialog", "<b>Storage Volume</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ProjectCreateDialog", "<b>User</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.user_name.setToolTip(QtGui.QApplication.translate("ProjectCreateDialog", "The <b>User Name</b> associated with your new Flame Project is based on the Shotgun user that matches your current login name.\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.user_name.setText(QtGui.QApplication.translate("ProjectCreateDialog", "xxx", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("ProjectCreateDialog", "<b>Host</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.host_name.setText(QtGui.QApplication.translate("ProjectCreateDialog", "xxx", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("ProjectCreateDialog", "<b>Workspace</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.workspace_name.setText(QtGui.QApplication.translate("ProjectCreateDialog", "xxx", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.project_overview_tab), QtGui.QApplication.translate("ProjectCreateDialog", "Project Overview", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.width.setPlaceholderText(QtGui.QApplication.translate("ProjectCreateDialog", "width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ProjectCreateDialog", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.height.setPlaceholderText(QtGui.QApplication.translate("ProjectCreateDialog", "height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Aspect Ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.aspect_ratio.setItemText(0, QtGui.QApplication.translate("ProjectCreateDialog", "4:3", None, QtGui.QApplication.UnicodeUTF8))
        self.aspect_ratio.setItemText(1, QtGui.QApplication.translate("ProjectCreateDialog", "16:9", None, QtGui.QApplication.UnicodeUTF8))
        self.aspect_ratio.setItemText(2, QtGui.QApplication.translate("ProjectCreateDialog", "Based on width/height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Frame Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_rate.setItemText(0, QtGui.QApplication.translate("ProjectCreateDialog", "23.976 fps", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_rate.setItemText(1, QtGui.QApplication.translate("ProjectCreateDialog", "24 fps", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_rate.setItemText(2, QtGui.QApplication.translate("ProjectCreateDialog", "25 fps", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_rate.setItemText(3, QtGui.QApplication.translate("ProjectCreateDialog", "29.97 fps DF", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_rate.setItemText(4, QtGui.QApplication.translate("ProjectCreateDialog", "29.97 fps NDF", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_rate.setItemText(5, QtGui.QApplication.translate("ProjectCreateDialog", "30 fps", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_rate.setItemText(6, QtGui.QApplication.translate("ProjectCreateDialog", "50 fps", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_rate.setItemText(7, QtGui.QApplication.translate("ProjectCreateDialog", "59.94 fps DF", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_rate.setItemText(8, QtGui.QApplication.translate("ProjectCreateDialog", "59.94 fps NDF", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_rate.setItemText(9, QtGui.QApplication.translate("ProjectCreateDialog", "60 fps", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Depth", None, QtGui.QApplication.UnicodeUTF8))
        self.depth.setItemText(0, QtGui.QApplication.translate("ProjectCreateDialog", "16-bit fp", None, QtGui.QApplication.UnicodeUTF8))
        self.depth.setItemText(1, QtGui.QApplication.translate("ProjectCreateDialog", "12-bit", None, QtGui.QApplication.UnicodeUTF8))
        self.depth.setItemText(2, QtGui.QApplication.translate("ProjectCreateDialog", "12-bit u", None, QtGui.QApplication.UnicodeUTF8))
        self.depth.setItemText(3, QtGui.QApplication.translate("ProjectCreateDialog", "10-bit", None, QtGui.QApplication.UnicodeUTF8))
        self.depth.setItemText(4, QtGui.QApplication.translate("ProjectCreateDialog", "8-bit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Field Dominance", None, QtGui.QApplication.UnicodeUTF8))
        self.field_dominance.setItemText(0, QtGui.QApplication.translate("ProjectCreateDialog", "PROGRESSIVE", None, QtGui.QApplication.UnicodeUTF8))
        self.field_dominance.setItemText(1, QtGui.QApplication.translate("ProjectCreateDialog", "FIELD_1", None, QtGui.QApplication.UnicodeUTF8))
        self.field_dominance.setItemText(2, QtGui.QApplication.translate("ProjectCreateDialog", "FIELD_2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.resolution_tab), QtGui.QApplication.translate("ProjectCreateDialog", "Resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_depth_label_2.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_mode.setItemText(0, QtGui.QApplication.translate("ProjectCreateDialog", "Proxies Off", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_mode.setItemText(1, QtGui.QApplication.translate("ProjectCreateDialog", "Proxies Conditional", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_mode.setItemText(2, QtGui.QApplication.translate("ProjectCreateDialog", "Proxies On", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_depth_label.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Depth", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_depth.setItemText(0, QtGui.QApplication.translate("ProjectCreateDialog", "8-bit", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_depth.setItemText(1, QtGui.QApplication.translate("ProjectCreateDialog", "SAME AS HIRES", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_quality_label.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Quality", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_quality.setItemText(0, QtGui.QApplication.translate("ProjectCreateDialog", "draft", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_quality.setItemText(1, QtGui.QApplication.translate("ProjectCreateDialog", "coarse", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_quality.setItemText(2, QtGui.QApplication.translate("ProjectCreateDialog", "medium", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_quality.setItemText(3, QtGui.QApplication.translate("ProjectCreateDialog", "quality", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_quality.setItemText(4, QtGui.QApplication.translate("ProjectCreateDialog", "bicubic", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_width_hint_label.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_width_hint_preview.setText(QtGui.QApplication.translate("ProjectCreateDialog", "720px", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_min_frame_size_label.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Width >", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_min_frame_size_preview.setText(QtGui.QApplication.translate("ProjectCreateDialog", "720px", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_above_8_bits.setText(QtGui.QApplication.translate("ProjectCreateDialog", ">8 bits", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.old_proxy_tab), QtGui.QApplication.translate("ProjectCreateDialog", "Proxy", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_depth_label_3.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.new_proxy_mode.setItemText(0, QtGui.QApplication.translate("ProjectCreateDialog", "Proxy 1/2", None, QtGui.QApplication.UnicodeUTF8))
        self.new_proxy_mode.setItemText(1, QtGui.QApplication.translate("ProjectCreateDialog", "Proxy 1/4", None, QtGui.QApplication.UnicodeUTF8))
        self.new_proxy_mode.setItemText(2, QtGui.QApplication.translate("ProjectCreateDialog", "Proxy 1/8", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_quality_label_2.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Quality", None, QtGui.QApplication.UnicodeUTF8))
        self.new_proxy_quality.setItemText(0, QtGui.QApplication.translate("ProjectCreateDialog", "lanczos", None, QtGui.QApplication.UnicodeUTF8))
        self.new_proxy_quality.setItemText(1, QtGui.QApplication.translate("ProjectCreateDialog", "shannon", None, QtGui.QApplication.UnicodeUTF8))
        self.new_proxy_quality.setItemText(2, QtGui.QApplication.translate("ProjectCreateDialog", "gaussian", None, QtGui.QApplication.UnicodeUTF8))
        self.new_proxy_quality.setItemText(3, QtGui.QApplication.translate("ProjectCreateDialog", "quadratic", None, QtGui.QApplication.UnicodeUTF8))
        self.new_proxy_quality.setItemText(4, QtGui.QApplication.translate("ProjectCreateDialog", "bicubic", None, QtGui.QApplication.UnicodeUTF8))
        self.new_proxy_quality.setItemText(5, QtGui.QApplication.translate("ProjectCreateDialog", "mitchell", None, QtGui.QApplication.UnicodeUTF8))
        self.new_proxy_quality.setItemText(6, QtGui.QApplication.translate("ProjectCreateDialog", "triangle", None, QtGui.QApplication.UnicodeUTF8))
        self.new_proxy_quality.setItemText(7, QtGui.QApplication.translate("ProjectCreateDialog", "impulse", None, QtGui.QApplication.UnicodeUTF8))
        self.new_proxy_quality.setItemText(8, QtGui.QApplication.translate("ProjectCreateDialog", "draft", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_min_frame_size_label_2.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Conditional Width >", None, QtGui.QApplication.UnicodeUTF8))
        self.new_proxy_width_label.setText(QtGui.QApplication.translate("ProjectCreateDialog", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.new_generate_proxies.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Generate Proxies By Default", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.new_proxy_tab), QtGui.QApplication.translate("ProjectCreateDialog", "Proxy", None, QtGui.QApplication.UnicodeUTF8))
        self.help_link.setText(QtGui.QApplication.translate("ProjectCreateDialog", "<small><a style=\'color: #30A7E3;\' href=\'{DOC}\'>How do I customize Project creation?</a></small>", None, QtGui.QApplication.UnicodeUTF8))
        self.abort.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Abort", None, QtGui.QApplication.UnicodeUTF8))
        self.create_project.setText(QtGui.QApplication.translate("ProjectCreateDialog", "Create Project", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
