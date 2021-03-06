﻿# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Chiriin3D_reverse
                                 A QGIS plugin
 This plugin reverses a Chiriin Chizu 3D model.
                              -------------------
        begin                : 2014-10-24
        git sha              : $Format:%H$
        copyright            : (C) 2014 by Takayuki Mizutani
        email                : mizutani.takayuki@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon, QFileDialog, QMessageBox
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from chiriin3d_reverse_dialog import Chiriin3D_reverseDialog
import os.path
import reverse
import webbrowser
import platform
from qgis.core import QgsCoordinateReferenceSystem, QgsCoordinateTransform

class Chiriin3D_reverse:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'Chiriin3D_reverse_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = Chiriin3D_reverseDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Chiriin3D reverse')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'Chiriin3D_reverse')
        self.toolbar.setObjectName(u'Chiriin3D_reverse')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('Chiriin3D_reverse', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the InaSAFE toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/Chiriin3D_reverse/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Chiriin3D reverse'),
            callback=self.run,
            parent=self.iface.mainWindow())
        icon_path=""
        self.add_action(
            icon_path,
            text=self.tr(u'help'),
            callback=self.info,
            parent=self.iface.mainWindow(),
            add_to_toolbar=False)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Chiriin3D reverse'),
                action)
            self.iface.removeToolBarIcon(action)


    def run(self):
        """Run method that performs all the real work"""
        self.dlg.pushButton_3.clicked.connect(self.openWeb)
        self.dlg.toolButton.clicked.connect(self.openBrowse)
        self.dlg.pushButton.clicked.connect(self.run_reverse)
        self.dlg.pushButton_2.clicked.connect(self.reject)
        self.dlg.radioButton.toggled.connect(self.change_name)
        self.dlg.radioButton_2.toggled.connect(self.change_name)
        self.dlg.radioButton_3.toggled.connect(self.change_name)
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass
        self.dlg.pushButton_3.clicked.disconnect(self.openWeb)
        self.dlg.toolButton.clicked.disconnect(self.openBrowse)
        self.dlg.pushButton.clicked.disconnect(self.run_reverse)
        self.dlg.pushButton_2.clicked.disconnect(self.reject)
        self.dlg.radioButton.toggled.disconnect(self.change_name)
        self.dlg.radioButton_2.toggled.disconnect(self.change_name)
        self.dlg.radioButton_3.toggled.disconnect(self.change_name)

    def openBrowse(self):
        stlfile =  QFileDialog.getOpenFileName(self.dlg, "stl file", '', 'STL files (*.stl)')
        if stlfile:
            root, ext = os.path.splitext(stlfile)
            self.input = stlfile
            self.output = root + "_reverse_all" + ext
            self.dlg.radioButton_3.setChecked(True)
            self.dlg.lineEdit.setText(self.input)
            self.dlg.lineEdit_2.setText(self.output)

    def change_name(self):
        if self.dlg.radioButton.isChecked():
           type="left"
        elif self.dlg.radioButton_2.isChecked():
           type="right"
        else:
           type="all"
        inputpath = self.dlg.lineEdit.text()
        if inputpath!="":
           root, ext = os.path.splitext(inputpath)
           self.output = root + "_reverse_" + type + ext
           self.dlg.lineEdit_2.setText(self.output)

    def run_reverse(self):
        if self.dlg.radioButton.isChecked():
           type="left"
        elif self.dlg.radioButton_2.isChecked():
           type="right"
        else:
           type="all"
        reverse.run(self.input,self.output,type)
        QMessageBox.information(self.dlg, "", "finished!")

    def reject(self):
        self.dlg.reject()

    def openWeb(self):
        map_canvas = self.iface.mapCanvas()
        extent = map_canvas.mapRenderer().extent()
        if map_canvas.hasCrsTransformEnabled():
           crs_map = map_canvas.mapRenderer().destinationCrs()
        else:
           legend = self.iface.legendInterface()
           if len(legend.layers())==0:
              QMessageBox.information(self.dlg, "", u"please add layer")
              return
           else:
              crs_map = legend.layers()[0].crs()
        if crs_map.authid() != u'EPSG:4326':
           crs_4326 = QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId)
           extent= QgsCoordinateTransform(crs_map, crs_4326).transform(extent)

        lon=(extent.xMinimum()+extent.xMaximum())/2
        lat=(extent.yMinimum()+extent.yMaximum())/2
        url="http://cyberjapandata.gsi.go.jp/3d/site/index.html?lat=" + str(lat) + "&lon=" + str(lon) + "&z=14"
        myos = platform.system()
        #if myos =="Darwin":
        #   browserstr='macosx'
        #else:
        #   browserstr='windows-default'

        #br=webbrowser.get(browserstr)
        #br.open(url,new=2)
        webbrowser.open(url,new=2)

    def info(self):
        html =u"""
        <h1>Chiriin3D reverse</h1>
        <h2>使い方</h2>
        <ol>
        <li>地理院地図3Dのstlファイルを選択します</li> 
        <li>出力したいパーツを選択します。（左、右、左右）</li>
        <li>[run] ボタンを押すと裏返したstlファイルが作成されます </li>
        </ol>
        ※地理院地図3Dのデータを利用する際は、その規約に従ってください。
        """
        QMessageBox.information(self.dlg, "Information:", html)
