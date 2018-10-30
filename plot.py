#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
#from PyQt4.QtGui import *
#from PyQt4.QtCore import *
#from PyQt4 import *
import os, sys
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import datetime
import sip
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class GeneralSetting(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent=parent)
		self.setup_ui()
		
	def open_FileDialog(self):
		current_directory = os.path.dirname(os.path.realpath(__file__))
		filename = QFileDialog.getOpenFileName(self, "Open file", os.path.expanduser('~') + '/Desktop')
		self.file_setting_edit.setText(filename)
		
		
	def setup_ui(self):
		
		title_setting_layout = QHBoxLayout()
		title_setting = QWidget()
		title_setting_label = QLabel("Plot Title : ")
		self.title_setting_edit = QLineEdit()
		self.title_setting_edit.setPlaceholderText("input title")
		#self.title_setting_edit.setMaximumWidth(170)
		self.update_button = QPushButton("Update")
		#self.add_button = QPushButton("Add")
		title_setting_layout.addWidget(title_setting_label)
		title_setting_layout.addWidget(self.title_setting_edit)
		title_setting_layout.addWidget(self.update_button)
		#title_setting_layout.addWidget(self.add_button)
		title_setting.setLayout(title_setting_layout)
		
		nfile_setting_layout = QHBoxLayout()
		nfile_setting = QWidget()
		nfile_setting_label = QLabel("Number of Files : ")
		self.nfile_setting_combo = QComboBox()
		self.nfile_setting_combo.addItem("1")
		self.nfile_setting_combo.addItem("2")
		self.nfile_setting_combo.addItem("3")
		self.nfile_setting_combo.addItem("4")
		self.nfile_setting_combo.setMaximumWidth(50)
		nfile_setting_layout.addWidget(nfile_setting_label)
		nfile_setting_layout.addWidget(self.nfile_setting_combo)
		
		plot_setting_label = QLabel("Plot Form : ")
		self.plot_setting_combo = QComboBox()
		self.plot_setting_combo.addItem("Plot")
		self.plot_setting_combo.addItem("Bar")
		self.plot_setting_combo.setMaximumWidth(100)
		nfile_setting_layout.addWidget(plot_setting_label)
		nfile_setting_layout.addWidget(self.plot_setting_combo)
		
		self.import_button = QPushButton("Import")
		
		legend_setting_label = QLabel("Legend : ")
		self.legend_setting_checkbox = QCheckBox()
		self.legend_position_combo = QComboBox()
		self.legend_position_combo.addItem("Best")
		self.legend_position_combo.addItem("UR")
		self.legend_position_combo.addItem("UL")
		self.legend_position_combo.addItem("LR")
		self.legend_position_combo.addItem("LL")
		nfile_setting_layout.addWidget(legend_setting_label)
		nfile_setting_layout.addWidget(self.legend_setting_checkbox)
		nfile_setting_layout.addWidget(self.legend_position_combo)
		nfile_setting_layout.addWidget(self.import_button)
		nfile_setting.setLayout(nfile_setting_layout)

		#あとでファイル数を変えられるように変更(できたら)
		'''
		file_setting_layout = QHBoxLayout()
		file_setting = QWidget()
		file_setting_label = QLabel("File Name : ")
		self.file_setting_edit = QLineEdit()
		#self.title_setting_edit.setMaximumWidth(170)
		self.file_refference = QPushButton("Refference")
		#self.file_refference.setStyleSheet("QPushButton {background-color: blue}")
		self.file_refference.clicked.connect(self.open_FileDialog)
		file_setting_layout.addWidget(file_setting_label)
		file_setting_layout.addWidget(self.file_setting_edit)
		file_setting_layout.addWidget(self.file_refference)
		file_setting.setLayout(file_setting_layout)
		'''
		self.file_settings = File_Settings()
		
		self.Plot_Button = QPushButton("Plot !")
		
		
		layout = QVBoxLayout()
		layout.addWidget(title_setting)
		layout.addWidget(nfile_setting)
		layout.addWidget(self.file_settings)
		layout.addWidget(self.Plot_Button)
		
		self.setLayout(layout)
		
	
class XSetting(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent=parent)
		self.setup_ui()
		
	def setup_ui(self):
		
		axis_title_layout = QHBoxLayout()
		axis_title = QWidget()
		axis_label = QLabel("Axis Title : ")
		self.axis_edit = QLineEdit()
		self.axis_edit.setMaximumWidth(170)
		self.axis_style_combo = QComboBox()
		self.axis_style_combo.addItem("LaTeX")
		self.axis_style_combo.addItem("Text")
		self.axis_style_combo.setMaximumWidth(80)
		axis_title_layout.addWidget(axis_label)
		axis_title_layout.addWidget(self.axis_edit)
		axis_title_layout.addWidget(self.axis_style_combo)
		axis_title.setLayout(axis_title_layout)
		
		index_setting_layout = QHBoxLayout()
		index_setting = QWidget()
		index_setting_label = QLabel("Data : ")
		self.index_setting_combo = QComboBox()
		self.index_setting_combo.addItem("1")
		self.index_setting_combo.addItem("2")
		self.index_setting_combo.addItem("3")
		self.index_setting_combo.addItem("4")
		self.index_setting_combo.addItem("5")
		self.index_setting_combo.addItem("6")
		self.apply_button = QPushButton("Apply")
		index_setting_layout.addWidget(index_setting_label)
		index_setting_layout.addWidget(self.index_setting_combo)
		index_setting_layout.addWidget(self.apply_button)
		index_setting.setLayout(index_setting_layout)
		
		scale_setting_layout = QHBoxLayout()
		scale_setting = QWidget()
		scale_setting_label = QLabel("Scale : ")
		self.scale_setting_combo = QComboBox(self)
		self.scale_setting_combo.addItem("Linear")
		self.scale_setting_combo.addItem("Log")
		self.scale_setting_combo.setMaximumWidth(75)
		scale_setting_layout.addWidget(scale_setting_label)
		scale_setting_layout.addWidget(self.scale_setting_combo)
		#scale_setting.setLayout(scale_setting_layout)
		#index_setting.setLayout(index_setting_layout)
		
		range_setting_layout = QHBoxLayout()
		range_setting = QWidget()
		range_label = QLabel("X Range : ")
		self.range_edit = QLineEdit()
		self.range_edit.setMaximumWidth(80)
		scale_setting_layout.addWidget(range_label)
		scale_setting_layout.addWidget(self.range_edit)
		scale_setting.setLayout(scale_setting_layout)
		
		
		layout = QVBoxLayout()
		layout.addWidget(axis_title)
		layout.addWidget(index_setting)
		layout.addWidget(scale_setting)
		#layout.addWidget(range_setting)
		
		self.all = QGroupBox("X-Axis")
		self.all.setLayout(layout)
		#self.setLayout(layout)
		
	
	
class YSetting(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent=parent)
		self.setup_ui()
		
	def setup_ui(self):
		axis_title_layout = QHBoxLayout()
		axis_title = QWidget()
		axis_label = QLabel("Axis Title : ")
		self.axis_edit = QLineEdit()
		self.axis_edit.setMaximumWidth(170)
		self.axis_style_combo = QComboBox()
		self.axis_style_combo.addItem("LaTeX")
		self.axis_style_combo.addItem("Text")
		self.axis_style_combo.setMaximumWidth(80)
		axis_title_layout.addWidget(axis_label)
		axis_title_layout.addWidget(self.axis_edit)
		axis_title_layout.addWidget(self.axis_style_combo)
		axis_title.setLayout(axis_title_layout)
		
		index_setting_layout = QHBoxLayout()
		index_setting = QWidget()
		index_setting_label = QLabel("Data : ")
		self.index_setting_combo = QComboBox()
		self.index_setting_combo.addItem("1")
		self.index_setting_combo.addItem("2")
		self.index_setting_combo.addItem("3")
		self.index_setting_combo.addItem("4")
		self.index_setting_combo.addItem("5")
		self.index_setting_combo.addItem("6")
		self.index_setting_combo.setCurrentIndex(1)
		self.apply_button = QPushButton("Apply")
		index_setting_layout.addWidget(index_setting_label)
		index_setting_layout.addWidget(self.index_setting_combo)
		index_setting_layout.addWidget(self.apply_button)
		index_setting.setLayout(index_setting_layout)
		
		scale_setting_layout = QHBoxLayout()
		scale_setting = QWidget()
		scale_setting_label = QLabel("Scale : ")
		self.scale_setting_combo = QComboBox(self)
		self.scale_setting_combo.addItem("Linear")
		self.scale_setting_combo.addItem("Log")
		self.scale_setting_combo.setMaximumWidth(75)
		scale_setting_layout.addWidget(scale_setting_label)
		scale_setting_layout.addWidget(self.scale_setting_combo)
		#scale_setting.setLayout(scale_setting_layout)
		#index_setting.setLayout(index_setting_layout)
		
		range_setting_layout = QHBoxLayout()
		range_setting = QWidget()
		range_label = QLabel("Y Range : ")
		self.range_edit = QLineEdit()
		self.range_edit.setMaximumWidth(80)
		scale_setting_layout.addWidget(range_label)
		scale_setting_layout.addWidget(self.range_edit)
		scale_setting.setLayout(scale_setting_layout)
		
		
		layout = QVBoxLayout()
		layout.addWidget(axis_title)
		layout.addWidget(index_setting)
		layout.addWidget(scale_setting)
		#layout.addWidget(range_setting)
		
		self.all = QGroupBox("Y-Axis")
		self.all.setLayout(layout)
		#self.setLayout(layout)
		
class ZSetting(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent=parent)
		self.setup_ui()
		
	def setup_ui(self):
		
		axis_title_layout = QHBoxLayout()
		axis_title = QWidget()
		axis_label = QLabel("Axis Title : ")
		self.axis_edit = QLineEdit()
		self.axis_edit.setMaximumWidth(170)
		self.axis_style_combo = QComboBox()
		self.axis_style_combo.addItem("LaTeX")
		self.axis_style_combo.addItem("Text")
		self.axis_style_combo.setMaximumWidth(80)
		axis_title_layout.addWidget(axis_label)
		axis_title_layout.addWidget(self.axis_edit)
		axis_title_layout.addWidget(self.axis_style_combo)
		axis_title.setLayout(axis_title_layout)
		
		index_setting_layout = QHBoxLayout()
		index_setting = QWidget()
		index_setting_label = QLabel("Data : ")
		self.index_setting_combo = QComboBox()
		self.index_setting_combo.addItem("1")
		self.index_setting_combo.addItem("2")
		self.index_setting_combo.addItem("3")
		self.index_setting_combo.addItem("4")
		self.index_setting_combo.addItem("5")
		self.index_setting_combo.addItem("6")
		index_setting_layout.addWidget(index_setting_label)
		index_setting_layout.addWidget(self.index_setting_combo)
		index_setting.setLayout(index_setting_layout)
		
		scale_setting_layout = QHBoxLayout()
		scale_setting = QWidget()
		scale_setting_label = QLabel("Scale : ")
		self.scale_setting_combo = QComboBox(self)
		self.scale_setting_combo.addItem("Linear")
		self.scale_setting_combo.addItem("Log")
		self.scale_setting_combo.setMaximumWidth(75)
		scale_setting_layout.addWidget(scale_setting_label)
		scale_setting_layout.addWidget(self.scale_setting_combo)
		#scale_setting.setLayout(scale_setting_layout)
		#index_setting.setLayout(index_setting_layout)
		
		range_setting_layout = QHBoxLayout()
		range_setting = QWidget()
		range_label = QLabel("Z Range : ")
		self.range_edit = QLineEdit()
		self.range_edit.setMaximumWidth(80)
		scale_setting_layout.addWidget(range_label)
		scale_setting_layout.addWidget(self.range_edit)
		scale_setting.setLayout(scale_setting_layout)
		
		
		layout = QVBoxLayout()
		layout.addWidget(axis_title)
		layout.addWidget(index_setting)
		layout.addWidget(scale_setting)
		#layout.addWidget(range_setting)
		
		self.all = QGroupBox("Z-Axis")
		self.all.setLayout(layout)
		#self.setLayout(layout)
		
class Axis_Setting_Widget(QWidget):
	def __init__(self, nAxis, parent=None):
		QWidget.__init__(self, parent=parent)
		if(nAxis == 0):
			self.setup_2axis_ui()
		else:
			self.setup_3axis_ui()
		
	def setup_2axis_ui(self):
		self.XSetting_widget = XSetting()
		self.YSetting_widget = YSetting()
		layout = QHBoxLayout()
		layout.addWidget(self.XSetting_widget.all)
		layout.addWidget(self.YSetting_widget.all)
		
		self.setLayout(layout)
		
	def setup_3axis_ui(self):
		self.XSetting_widget = XSetting()
		self.YSetting_widget = YSetting()
		ZSetting_widget = ZSetting()
		layout = QHBoxLayout()
		layout.addWidget(self.XSetting_widget.all)
		layout.addWidget(self.YSetting_widget.all)
		layout.addWidget(self.ZSetting_widget.all)
		
		self.setLayout(layout)
	
	
	
class File_Setting_Widget(QWidget):
	def __init__(self, number, parent=None):
		QWidget.__init__(self, parent=parent)
		self.setup_ui(number)
		
	def open_FileDialog(self, current_directory = os.path.expanduser('~') + '/Desktop'):
		#current_directory = os.path.dirname(os.path.realpath(__file__))
		#print current_directory
		filename = QFileDialog.getOpenFileName(self, "Open file", current_directory)
		if(filename != ""):
			self.file_setting_edit.setText(filename[0])
		return filename
	
	def setup_ui(self, number):
		self.n = number - 1
		file_setting_layout = QHBoxLayout()
		file_setting = QWidget()
		self.all = QGroupBox("File" + str(number))
		file_setting_label = QLabel("File Name : ")
		self.file_setting_edit = QLineEdit()
		self.file_refference = QPushButton("Reference")
		#self.file_refference.clicked.connect(self.open_FileDialog)
		file_setting_layout.addWidget(file_setting_label)
		file_setting_layout.addWidget(self.file_setting_edit)
		file_setting_layout.addWidget(self.file_refference)
		file_setting.setLayout(file_setting_layout)
		legend_setting_layout = QHBoxLayout()
		legend_setting = QWidget()
		legend_setting_label = QLabel("Legend : ")
		self.legend_setting_edit = QLineEdit()
		plot_setting_label = QLabel("Style : ")
		self.plot_setting_edit = QLineEdit()
		self.plot_setting_edit.setMaximumWidth(60)
		self.color_setting_edit = QLineEdit()
		self.color_setting_edit.setMaximumWidth(60)
		legend_setting_layout.addWidget(legend_setting_label)
		legend_setting_layout.addWidget(self.legend_setting_edit)
		legend_setting_layout.addWidget(plot_setting_label)
		legend_setting_layout.addWidget(self.plot_setting_edit)
		legend_setting_layout.addWidget(self.color_setting_edit)
		legend_setting.setLayout(legend_setting_layout)
		
		file_layout = QVBoxLayout()
		file_layout.addWidget(file_setting)
		file_layout.addWidget(legend_setting)
		
		self.all.setLayout(file_layout)
		
	

class File_Settings(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent=parent)
		self.setup_ui()
		
	def file_reference(self, i):
		filename = self.file_setting[i].open_FileDialog(self.current_directory)
		temp = filename[0].split("/")
		fname = ""
		del temp[len(temp) -1]
		for s in temp:
			fname += s + "/"
		self.current_directory = fname
		#print self.current_directory
		
	def setup_ui(self):
		#self.current_directory = os.path.expanduser('~') + '/Desktop'
		self.current_directory = "./"
		self.file_settings_layout = QGridLayout()
		self.file_setting = []
		self.file_setting.append(File_Setting_Widget(1))
		self.file_setting[0].file_refference.clicked.connect(lambda : self.file_reference(0))
		self.file_settings_layout.addWidget(self.file_setting[0].all, 0, 0)
		self.setLayout(self.file_settings_layout)
		self.n = 1
		self.current = 0
		
	
	def reset_ui(self, n):
		if(self.n < n ):
			for i in range(n - self.n):
				col = (i+self.n) % 2 
				row = (i+self.n) / 2
				self.file_setting.append(File_Setting_Widget(i+self.n+1))
				if(self.n==1):
					if(i==0):
						self.file_setting[1].file_refference.clicked.connect(lambda : self.file_reference(1))
					elif(i==1):
						self.file_setting[2].file_refference.clicked.connect(lambda : self.file_reference(2))
					elif(i==2):
						self.file_setting[3].file_refference.clicked.connect(lambda : self.file_reference(3))
					self.file_settings_layout.addWidget(self.file_setting[self.n+i].all, row, col)
				if(self.n==2):
					if(i==0):
						self.file_setting[2].file_refference.clicked.connect(lambda : self.file_reference(2))
					elif(i==1):
						self.file_setting[3].file_refference.clicked.connect(lambda : self.file_reference(3))
					self.file_settings_layout.addWidget(self.file_setting[self.n+i].all, row, col)
				if(self.n==3):
					if(i==0):
						self.file_setting[3].file_refference.clicked.connect(lambda : self.file_reference(3))
					self.file_settings_layout.addWidget(self.file_setting[self.n+i].all, row, col)
			self.setLayout(self.file_settings_layout)
		'''
		elif(self.n > n):
			for i in range(self.n-n):
				self.file_settings_layout.removeWidget(self.file_setting[self.n-i-1])
				sip.delete(self.file_setting[self.n-i-1])
				self.file_setting[self.n-i-1] = None
			self.setLayout(self.file_settings_layout)
		'''
		self.n = n

class Plot_Widget(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent=parent)
		self.setup_ui()
	def setup_ui(self):
		self.fig = plt.Figure()
		self.axes = self.fig.add_subplot(111)
		self.canvas = FigureCanvas(self.fig)
		self.canvas.setFixedSize(500,400)

	def plot(self, min = -3.14, max = 3.14):
		xrange = [min, max]
		x = np.arange(xrange[0], xrange[1], 0.01)
		y = np.sin(x)
		self.axes.plot(x,y)
		self.canvas.draw()

class line_widget(QWidget):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent=parent)
		self.setup_ui()
		
	def setup_ui(self):
		func = QWidget()
		func_layout = QHBoxLayout()
		func_label = QLabel("f(x) = ")
		self.func_edit = QLineEdit()
		func_layout.addWidget(func_label)
		func_layout.addWidget(self.func_edit)
		func.setLayout(func_layout)
		
		legend = QWidget()
		legend_layout = QHBoxLayout()
		legend_label = QLabel("Legend : ")
		self.legend_edit = QLineEdit()
		
		style_label = QLabel("Style : ")
		self.style_edit = QLineEdit()
		self.color_edit = QLineEdit()
		self.reset_button = QPushButton("Reset")
		legend_layout.addWidget(legend_label)
		legend_layout.addWidget(self.legend_edit)
		legend_layout.addWidget(style_label)
		legend_layout.addWidget(self.style_edit)
		legend_layout.addWidget(self.color_edit)
		legend_layout.addWidget(self.reset_button)
		legend.setLayout(legend_layout)
		
		self.plot_button = QPushButton("Plot")
		
		layout = QVBoxLayout()
		layout.addWidget(func)
		layout.addWidget(legend)
		layout.addWidget(self.plot_button)
		self.setFixedSize(700, 200)
		self.setLayout(layout)
		

class main_widget(QWidget):
	def __init__(self, parent=None):
		#replace_below
		self.dir = "/Users/T.Yoshizawa/Dropbox/PC/plot/"
		QWidget.__init__(self, parent=parent)
		self.setup_ui()
	
	def open_FileDialog(self):
		current_directory = os.path.dirname(os.path.realpath(__file__))
		#filename = QFileDialog.getOpenFileName(self, "Open file", os.path.expanduser('~') + '/Desktop')
		filename = QFileDialog.getOpenFileName(self, "Open file", current_directory)
		self.General.file_settings.file_setting[self.General.file_settings.current].file_setting_edit.setText(filename)
	
	def save_figure(self):
		if(self.save_name_edit.text() != ""):
			filename = self.save_name_edit.text()
			self.p.fig.savefig(str(filename))
		else:
			inputfile = str(self.General.file_settings.file_setting[0].file_setting_edit.text())
			temp = inputfile.split("/")
			index = temp[len(temp)-1].rfind(".")
			filename = temp[len(temp)-1][0:index]
			now = datetime.datetime.today()
			time = str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute) + "-" + str(now.second)
			newfilename = filename + "-" + time + ".pdf"
			#print newfilename
			filename = self.dir + "fig/" + newfilename
			self.p.fig.savefig(filename)
		
	def folder_reference(self):
		filename = QFileDialog.getSaveFileName(directory = self.dir + "fig/")
		self.save_name_edit.setText(filename)
		
	def folder_reference_export(self):
		filename = QFileDialog.getSaveFileName(directory = self.dir + "history/")
		self.Export_edit.setText(filename)
	
	def setup_ui(self):
		self.General = GeneralSetting()
		
		self.axis = Axis_Setting_Widget(0)
		
		left_panel_layout = QVBoxLayout()
		left_panel_layout.addWidget(self.General)
		left_panel_layout.addWidget(self.axis)
		left_panel = QWidget()
		left_panel.setLayout(left_panel_layout)
		self.tab = QTabWidget()
		self.tab.addTab(left_panel, "Main")
		self.test = line_widget()
		self.tab.addTab(self.test, "Line")
		self.test.plot_button.clicked.connect(self.line_plot)
		self.test.reset_button.clicked.connect(self.reset_plot)
		layout = QHBoxLayout()
		right_panel = QWidget()
		right_panel_layout = QVBoxLayout()
		Import = QWidget()
		import_layout = QHBoxLayout()
		#self.import_button = QPushButton("Import")
		export_label = QLabel("Export Plot Setting : ")
		self.Export_edit = QLineEdit()
		self.Export_reference = QPushButton("Reference")
		self.Export_button = QPushButton("Export")
		#import_layout.addWidget(self.import_button)
		import_layout.addWidget(export_label)
		import_layout.addWidget(self.Export_edit)
		import_layout.addWidget(self.Export_reference)
		import_layout.addWidget(self.Export_button)
		Import.setLayout(import_layout)
		self.p = Plot_Widget()
		save_name = QWidget()
		save_name_layout = QHBoxLayout()
		save_name_label = QLabel("Save File name : ")
		self.save_name_edit = QLineEdit()
		self.reference_button = QPushButton("Reference")
		self.save_Button = QPushButton("Save")
		save_name_layout.addWidget(save_name_label)
		save_name_layout.addWidget(self.save_name_edit)
		save_name_layout.addWidget(self.reference_button)
		save_name_layout.addWidget(self.save_Button)
		save_name.setLayout(save_name_layout)
		right_panel_layout.addWidget(Import)
		right_panel_layout.addWidget(self.p.canvas)
		right_panel_layout.addWidget(save_name)
		right_panel.setLayout(right_panel_layout)
		
		#layout.addWidget(left_panel)
		layout.addWidget(self.tab)
		layout.addWidget(right_panel)
		self.setLayout(layout)
		
		self.setFixedSize(1300, 770)
		
		#self.General.add_button.clicked.connect(self.add_tab)
		self.axis.XSetting_widget.index_setting_combo.activated.connect(self.set_X_label)
		self.axis.YSetting_widget.index_setting_combo.activated.connect(self.set_Y_label)
		self.axis.XSetting_widget.apply_button.clicked.connect(self.set_X_label)
		self.axis.YSetting_widget.apply_button.clicked.connect(self.set_Y_label)
		self.Export_reference.clicked.connect(self.folder_reference_export)
		self.reference_button.clicked.connect(self.folder_reference)
		self.Export_button.clicked.connect(self.Export)
		self.General.import_button.clicked.connect(self.Import)
		self.save_Button.clicked.connect(self.save_figure)
		self.General.Plot_Button.clicked.connect(self.sample_plot)
		self.General.update_button.clicked.connect(self.update)
		self.General.nfile_setting_combo.activated.connect(self.add_File_Setting)
		
		if(len(sys.argv) == 2):
			if(sys.argv[1] == "last"):
				filename = self.dir + "history/last_plot.txt"
			else:
				filename = sys.argv[1]
			
			f = open(filename)
			datas = f.readlines()
			f.close()
			self.translation(datas)
			
	def add_tab(self):
		self.test = line_widget()
		self.tab.addTab(self.test, "Line")
		self.test.plot_button.clicked.connect(self.line_plot)
		self.test.reset_button.clicked.connect(self.reset_plot)
		
	def reset_plot(self):
		self.p.axes.clear()
		self.p.canvas.draw()
		
	def line_plot(self):
		plot_func = self.test.func_edit.text()
		if(plot_func[0:2] == "x="):
			if(str(self.test.legend_edit.text()) != ""):
				legend = ", label = '" + str(self.test.legend_edit.text()) + "'"
			else:
				legend = ""
				
			if(str(self.test.style_edit.text()) != ""):
				style = ", linestyle = '" + str(self.test.style_edit.text()) + "'"
			else:
				style = ""
				
			if(str(self.test.color_edit.text()) != ""):
				color = ", color = '" + str(self.test.color_edit.text()) + "'"
			else:
				color = ""
				
			text = "self.p.axes.axvline(" + plot_func+ color + legend  + style  +")"
			#print text
			exec(str(text))
		elif(plot_func[0:2] == "y="):
			if(str(self.test.legend_edit.text()) != ""):
				legend = ", label = '" + str(self.test.legend_edit.text()) + "'"
			else:
				legend = ""
				
			if(str(self.test.style_edit.text()) != ""):
				style = ", linestyle = '" + str(self.test.style_edit.text()) + "'"
			else:
				style = ""
			
			if(str(self.test.color_edit.text()) != ""):
				color = ", color = '" + str(self.test.color_edit.text()) + "'"
			else:
				color = ""
			
			text = "self.p.axes.axhline(" + plot_func + color + legend + style + ")"
			#print text
			exec(str(text))
		else:
			range = self.p.axes.get_xlim()
			x = np.arange(range[0],range[1],(range[1]-range[0])/1000)
			
			text = "y = " + str(plot_func)
			exec(str(text))
				
			legend = str(self.test.legend_edit.text())
			style = str(self.test.style_edit.text())
			if(self.test.color_edit.text() != ""):
				color = str(self.test.color_edit.text())
			else:
				color = "r"
			
			if(legend != ""):
				if(style != ""):
					self.p.axes.plot(x,y, style, color = color, label = legend)
				else:
					self.p.axes.plot(x,y, color = color, label = legend)
				self.p.axes.legend()
			else:
				if(style != ""):
					self.p.axes.plot(x,y, style, color = color)
				else:
					self.p.axes.plot(x,y, color = color)
					
		
		if(self.General.legend_setting_checkbox.isChecked()):
			ll = self.General.legend_position_combo.currentIndex()
			if(ll == 0):
				loc = "best"
			elif(ll == 1):
				loc = "upper right"
			elif(ll == 2):
				loc = "upper left"
			elif(ll == 3):
				loc = "lower right"
			else:
				loc = "lower left"
			self.p.axes.legend(loc = loc)
		
		self.p.canvas.draw()
		
	def Import(self):
		filename = QFileDialog.getOpenFileName(self, "Open file", self.dir + "history/")
		if(filename != ""):
			f = open(str(filename))
			datas = f.readlines()
			f.close()
			self.translation(datas)
		
		
	def translation(self,datas):
		i = 3
		self.General.title_setting_edit.setText(get_data(datas, i))
		i = i + 1
		nfile = int(get_data(datas, i))
		self.General.nfile_setting_combo.setCurrentIndex(nfile-1)
		if(nfile != 1):
			self.General.file_settings.reset_ui(nfile)
		i = i + 1
		plot_form = get_data(datas, i)
		if(plot_form == "Plot"):
			self.General.plot_setting_combo.setCurrentIndex(0)
		else:
			self.General.plot_setting_combo.setCurrentIndex(1)
		i = i + 1
		legend = get_data(datas, i)
		if(legend == "y"):
			self.General.legend_setting_checkbox.setChecked(True)
		else:
			self.General.legend_setting_checkbox.setChecked(False)
		i = i + 1
		legend_pos = get_data(datas, i)
		if(legend_pos == "Best"):
			self.General.legend_position_combo.setCurrentIndex(0)
		elif(legend_pos == "UR"):
			self.General.legend_position_combo.setCurrentIndex(1)
		elif(legend_pos == "UL"):
			self.General.legend_position_combo.setCurrentIndex(2)
		elif(legend_pos == "LR"):
			self.General.legend_position_combo.setCurrentIndex(3)
		else:
			self.General.legend_position_combo.setCurrentIndex(4)
		i = i + 1
		current_directory = get_data(datas, i)
		self.General.file_settings.current_directory = current_directory
		i = i + 3
		
		for j in range(nfile):
			filename = get_data(datas, i)
			self.General.file_settings.file_setting[j].file_setting_edit.setText(str(filename))
			i = i + 1
			legend = get_data(datas, i)
			self.General.file_settings.file_setting[j].legend_setting_edit.setText(str(legend)) 
			i = i + 1
			style = get_data(datas, i)
			self.General.file_settings.file_setting[j].plot_setting_edit.setText(style)
			i = i + 1
			color = get_data(datas, i)
			self.General.file_settings.file_setting[j].color_setting_edit.setText(str(color)) 
			i = i + 3
			
		xtitle = get_data(datas, i)
		self.axis.XSetting_widget.axis_edit.setText(xtitle)
		i = i + 1
		xtitle_form = get_data(datas, i)
		if(xtitle_form == "LaTeX"):
			self.axis.XSetting_widget.axis_style_combo.setCurrentIndex(0)
		else:
			self.axis.XSetting_widget.axis_style_combo.setCurrentIndex(1)
		i = i + 1
		xindex = get_data(datas, i)
		self.axis.XSetting_widget.index_setting_combo.setCurrentIndex(int(xindex)-1)
		i = i + 1
		xscale = get_data(datas, i)
		if(xscale == "Linear"):
			self.axis.XSetting_widget.scale_setting_combo.setCurrentIndex(0)
		else:
			self.axis.XSetting_widget.scale_setting_combo.setCurrentIndex(1)
		i = i + 1
		xrange = get_data(datas, i)
		self.axis.XSetting_widget.range_edit.setText(xrange)
		i = i + 3
		
		ytitle = get_data(datas, i)
		self.axis.YSetting_widget.axis_edit.setText(ytitle)
		i = i + 1
		ytitle_form = get_data(datas, i)
		if(ytitle_form == "LaTeX"):
			self.axis.YSetting_widget.axis_style_combo.setCurrentIndex(0)
		else:
			self.axis.YSetting_widget.axis_style_combo.setCurrentIndex(1)
		i = i + 1
		yindex = get_data(datas, i)
		self.axis.YSetting_widget.index_setting_combo.setCurrentIndex(int(yindex)-1)
		i = i + 1
		yscale = get_data(datas, i)
		if(yscale == "Linear"):
			self.axis.YSetting_widget.scale_setting_combo.setCurrentIndex(0)
		else:
			self.axis.YSetting_widget.scale_setting_combo.setCurrentIndex(1)
		i = i + 1
		yrange = get_data(datas, i)
		self.axis.YSetting_widget.range_edit.setText(yrange)
		i = i + 2
		export_file = get_data(datas, i)
		self.Export_edit.setText(export_file)
		i = i + 1
		save_name = get_data(datas, i)
		self.save_name_edit.setText(save_name)
		self.update()
		self.axis.XSetting_widget.index_setting_combo.setCurrentIndex(int(xindex)-1)
		self.axis.YSetting_widget.index_setting_combo.setCurrentIndex(int(yindex)-1)
		if(self.General.file_settings.file_setting[0].file_setting_edit.text() != ""):
			Plot(self)
		
	def sample_plot(self):
		self.Export_file(self.dir + "history/last_plot.txt")
		self.p.axes.clear()
		Plot(self)
		'''
		t = self.axis.XSetting_widget.range_edit.text()
		if(t != ""):
			range = t.split(":")
			self.p.plot(float(range[0]), float(range[1]))
		else:
			self.p.plot()
		'''
		
	def set_X_label(self):
		filename = self.General.file_settings.file_setting[0].file_setting_edit.text()
		if(filename != ""):
			f = open(filename)
			data = f.readline()
			data = f.readline()
			if(data[0:2] == "##"):
				index = self.axis.XSetting_widget.index_setting_combo.currentIndex()
				label = data.replace("##", "").replace("\n", "").split(" \t")[index]
				self.axis.XSetting_widget.axis_edit.setText(label)
				
	def set_Y_label(self):
		filename = self.General.file_settings.file_setting[0].file_setting_edit.text()
		if(filename != ""):
			f = open(filename)
			data = f.readline()
			data = f.readline()
			if(data[0:2] == "##"):
				index = self.axis.YSetting_widget.index_setting_combo.currentIndex()
				label = data.replace("##", "").replace("\n", "").split(" \t")[index]
				self.axis.YSetting_widget.axis_edit.setText(label)
		
	def add_File_Setting(self):
		self.General.file_settings.reset_ui(self.General.nfile_setting_combo.currentIndex()+1)
		
	def update(self):
		if(self.General.file_settings.file_setting[0].file_setting_edit.text() != ""):
			f = open(self.General.file_settings.file_setting[0].file_setting_edit.text())
			line = f.readline()
			title = f.readline()
			f.close()
			if(line[0:2] == "##" and title[0:2] == "##"):
				self.axis.XSetting_widget.index_setting_combo.clear()
				self.axis.YSetting_widget.index_setting_combo.clear()
				temp = line.replace("#","")
				datas = temp.split(" \t")
				temp = title.replace("#", "")
				temp = temp.replace("\n", "")
				title = temp.split(" \t")
				for data in datas:
					self.axis.XSetting_widget.index_setting_combo.addItem(data)
					self.axis.YSetting_widget.index_setting_combo.addItem(data)
				self.axis.YSetting_widget.index_setting_combo.setCurrentIndex(1)
				self.axis.XSetting_widget.axis_edit.setText(title[0])
				self.axis.YSetting_widget.axis_edit.setText(title[1])
				
				
	def Export(self):
		if(self.Export_edit.text() != ""):
			filename = str(self.Export_edit.text())
			self.Export_file(filename)
		else:
			inputfile = str(self.General.file_settings.file_setting[0].file_setting_edit.text())
			temp = inputfile.split("/")
			newfilename = temp[len(temp)-1].replace(".txt", "_plt.txt")
			filename = self.dir + "history/" + newfilename
			self.Export_file(filename)
			
	def Export_file(self, filename):
		f = open(filename, "w")
		today = datetime.datetime.today()
		date = str(today.year) + "_" + str(today.month) + "_" + str(today.day) + "_" + str(today.hour) + "_" + str(today.minute) + "_"+ str(today.second)
		f.write("Date and Time \t: \t" + date + "\n")
		f.write("\nGeneral\n")
		f.write("Plot Title \t: \t" + self.General.title_setting_edit.text() + "\n")
		f.write("Number of File 	: 	" + str(self.General.nfile_setting_combo.currentIndex()+1) + "\n")
		f.write("Plot Form 	: 	" + self.General.plot_setting_combo.currentText() + "\n")
		if(self.General.legend_setting_checkbox.isChecked()):
			f.write("Legend  	: 	y\n")
		else:
			f.write("Legend  	: 	n\n")
		f.write("Legent Pos 	: 	" + self.General.legend_position_combo.currentText() + "\n")
		f.write("Directory 	: 	" + self.General.file_settings.current_directory + "\n\n")
		for j in range(self.General.nfile_setting_combo.currentIndex() + 1):
			f.write("File" + str(j + 1) + "\n")
			f.write("File Name 	: 	" + self.General.file_settings.file_setting[j].file_setting_edit.text() + "\n")
			f.write("Legend  	: 	" + self.General.file_settings.file_setting[j].legend_setting_edit.text() + "\n")
			f.write("Style   	: 	" + self.General.file_settings.file_setting[j].plot_setting_edit.text() + "\n")
			f.write("Color   	: 	" + self.General.file_settings.file_setting[j].color_setting_edit.text() + "\n")
			f.write("\n")
		
		f.write("X-Axis\n")
		f.write("Axis Title 	: 	" + self.axis.XSetting_widget.axis_edit.text() + "\n")
		f.write("Title Form 	: 	" + self.axis.XSetting_widget.axis_style_combo.currentText() + "\n")
		f.write("Data    	: 	" + str(self.axis.XSetting_widget.index_setting_combo.currentIndex()+1) + "\n")
		f.write("Scale    	: 	" + self.axis.XSetting_widget.scale_setting_combo.currentText() + "\n")
		f.write("X Range 	: 	" + self.axis.XSetting_widget.range_edit.text() + "\n")
		
		f.write("\n")
		
		f.write("Y-Axis\n")
		f.write("Axis Title 	: 	" + self.axis.YSetting_widget.axis_edit.text() + "\n")
		f.write("Title Form 	: 	" + self.axis.YSetting_widget.axis_style_combo.currentText() + "\n")
		f.write("Data    	: 	" + str(self.axis.YSetting_widget.index_setting_combo.currentIndex()+1) + "\n")
		f.write("Scale    	: 	" + self.axis.YSetting_widget.scale_setting_combo.currentText() + "\n")
		f.write("Y Range 	: 	" + self.axis.YSetting_widget.range_edit.text() + "\n")
		
		f.write("\n")
		
		f.write("Export  	: 	" + self.Export_edit.text() + "\n")
		f.write("Save Name 	: 	" + self.save_name_edit.text() + "\n")		
	
def get_data(datas, n):
	return datas[n].split(" \t: \t")[1].replace("\n","")
	
def Plot(w):
	#xrange = [-3.14, 3.14]
	#x = np.arange(xrange[0], xrange[1], 0.01)
	#y = np.sin(x)
	#plt.plot(x,y)
	#ファイル名設定
	for i in range(w.General.file_settings.n):
		if(w.General.file_settings.file_setting[i].file_setting_edit.text() == ""):
			if(i == 0):
				QMessageBox.warning(w, "Message", u"Input file name !")
				return
			else:
				continue
		else:
			filename = w.General.file_settings.file_setting[i].file_setting_edit.text()
		
		#ファイルの読み込み
		try:
			data = np.loadtxt(str(filename))
		except IOError as e:
			QMessageBox.warning(w, "Message", u"File can't open !")
			return
		
		xIndex = int(w.axis.XSetting_widget.index_setting_combo.currentIndex())
		yIndex = int(w.axis.YSetting_widget.index_setting_combo.currentIndex())
		#lines = f.readlines()
		x = []
		y = []
		for line in data:
			x.append(line[xIndex])
			y.append(line[yIndex])
		#凡例の設定
		c = str(w.General.file_settings.file_setting[i].color_setting_edit.text())
		if(c != ""):
			color = c
		else:
			if(i == 0):
				color = "b"
			elif(i == 1):
				color = "limegreen"
			elif(i == 2):
				color = "r"
			elif(i == 3):
				color = "y"
			else:
				color = "m"
			
		if(w.General.file_settings.file_setting[i].plot_setting_edit.text() != ""):
			style = str(w.General.file_settings.file_setting[i].plot_setting_edit.text())
			if(w.General.legend_setting_checkbox.isChecked()):
				label = w.General.file_settings.file_setting[i].legend_setting_edit.text()
				text = label.replace(u"\xa5", "\\")
				if(w.General.plot_setting_combo.currentIndex() == 0):
					w.p.axes.plot(x,y, style, color = color, label = text, linewidth = 1.0)
				elif(w.General.plot_setting_combo.currentIndex() == 1):
					w.p.axes.bar(x,y,color = color, label = text)
				#plt.legend()
			else:
				if(w.General.plot_setting_combo.currentIndex() == 0):
					w.p.axes.plot(x,y, style, color = color)
				elif(w.General.plot_setting_combo.currentIndex() == 1):
					w.p.axes.bar(x,y,color = color)
		else:
			if(w.General.legend_setting_checkbox.isChecked()):
				label = w.General.file_settings.file_setting[i].legend_setting_edit.text()
				text = label.replace(u"\xa5", "\\")
				if(w.General.plot_setting_combo.currentIndex() == 0):
					w.p.axes.plot(x,y, color = color, label = text, linewidth = 1.0)
				elif(w.General.plot_setting_combo.currentIndex() == 1):
					w.p.axes.bar(x,y,color = color, label = text)
				#plt.legend()
			else:
				if(w.General.plot_setting_combo.currentIndex() == 0):
					w.p.axes.plot(x,y,color = color)
				elif(w.General.plot_setting_combo.currentIndex() == 1):
					w.p.axes.bar(x,y,color = color)
	
	#ラベルの設定
	if(w.axis.XSetting_widget.axis_style_combo.currentIndex() == 0):
		if(w.axis.XSetting_widget.axis_edit.text() != ""):
			xlabel = "$" + w.axis.XSetting_widget.axis_edit.text() + "$"
			temp = xlabel.replace(u"\xa5", "\\")
			w.p.axes.set_xlabel(temp, fontsize = 28, fontname = "serif")
	else:
		if(w.axis.XSetting_widget.axis_edit.text() != ""):
			xlabel = w.axis.XSetting_widget.axis_edit.text()
			w.p.axes.set_xlabel(xlabel, fontsize = 28, fontname = "Times New Roman")
	if(w.axis.YSetting_widget.axis_style_combo.currentIndex() == 0):
		if(w.axis.YSetting_widget.axis_edit.text() != ""):
			ylabel = "$" + w.axis.YSetting_widget.axis_edit.text() + "$"
			temp = ylabel.replace(u"\xa5", "\\")
			w.p.axes.set_ylabel(temp, fontsize = 28, fontname = "serif")
	else:
		if(w.axis.YSetting_widget.axis_edit.text() != ""):
			ylabel = w.axis.YSetting_widget.axis_edit.text()
			w.p.axes.set_ylabel(ylabel, fontsize = 28, fontname = "Times New Roman")
	
	#レンジの設定
	if(w.axis.YSetting_widget.range_edit.text() != ""):
		temp1 = w.axis.YSetting_widget.range_edit.text()
		temp2 = temp1.split(":")
		yrange = [float(temp2[0]), float(temp2[1])]
		w.p.axes.set_ylim(yrange[0], yrange[1])
	if(w.axis.XSetting_widget.range_edit.text() != ""):
		temp1 = w.axis.XSetting_widget.range_edit.text()
		temp2 = temp1.split(":")
		xrange = [float(temp2[0]), float(temp2[1])]
		w.p.axes.set_xlim(xrange[0], xrange[1])
	title_temp = w.General.title_setting_edit.text()
	title = title_temp.replace(u"\xa5", "\\")
	#plt.title(str(title), fontsize = 28, fontname = "Helvetica")
	#w.p.axes.title(str(title), fontsize = , fontname = "Helvetica")
	#軸のスケールの設定
	if(w.axis.XSetting_widget.scale_setting_combo.currentIndex() == 1):
		w.p.axes.set_xscale("log")
	if(w.axis.YSetting_widget.scale_setting_combo.currentIndex() == 1):
		w.p.axes.set_yscale("log")
	
	if(w.General.legend_setting_checkbox.isChecked()):
		ll = w.General.legend_position_combo.currentIndex()
		if(ll == 0):
			loc = "best"
		elif(ll == 1):
			loc = "upper right"
		elif(ll == 2):
			loc = "upper left"
		elif(ll == 3):
			loc = "lower right"
		else:
			loc = "lower left"
		w.p.axes.legend(loc = loc)
	#w.p.axes.tick_params(labelsize=22)
	w.p.axes.set_title(str(title), fontsize = 28, fontname = "Arial")
	#plt.show()
	w.p.fig.tight_layout()
	w.p.canvas.draw()
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_widget = main_widget()
	
	main_window = QMainWindow()
	main_window.setWindowTitle("GUI Plot Test")
	main_window.setCentralWidget(main_widget)
	
	main_window.show()
	
	sys.exit(app.exec_())
