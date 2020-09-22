import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from pathlib import Path
import numpy as np
from numpy import asarray
from numpy import savetxt
import pandas as pd
import csv

def isint(s):
    try:
        print(int(s))
        return True
    except ValueError:
        return False

def isfloat(s):
  try:
    print(float(s))
    return True
  except ValueError:
    return False

class NPYfile():
    def __init__(self,data,filename):
        self.data = data
        self.filename = filename
    def __str__(self):
        if hasattr(self.data, 'dtype'):
            return "Filename = "+str(self.filename )  +" \nDtype = "+str(self.data.dtype)+"\nShape = "+str(self.data.shape)
        else:
            return "Filename = " + str(self.filename) + " \nDtype = "  + "\nShape = " + str(self.data.shape)

class MainApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 640
        self.initUI()




    def saveAs(self):
        home = str(Path.home())
        path = QFileDialog.getSaveFileName(
            self, 'Save File', home, 'NPY (*.npy);;CSV(*.csv)')[0]
        #path = QFileDialog.getSaveFileName(
        #    self, 'Save File', home, 'CSV(*.csv)')[0]
        if  path !="" and ".csv" in path:
            with open((path.replace(".csv","")+".csv"), 'w') as stream:
                writer = csv.writer(stream)
                for row in range(self.tableWidget.rowCount()):
                    rowdata = []
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, column)
                        if item is not None:
                            rowdata.append(item.text())

                        else:
                            rowdata.append('')
                    writer.writerow(rowdata)
        else:
            OutMatrix=[]
            for row in range(self.tableWidget.rowCount()):
                rowdata = []
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    if item is not None:

                        if isfloat(item.text()) and not isint(item.text()):
                            rowdata.append(float(item.text()))
                        if isfloat(item.text()) and isint(item.text()):
                            rowdata.append(int(item.text()))
                        if not isfloat(item.text()) and not isint(item.text()):
                            rowdata.append(item.text())
                    else:
                        rowdata.append('')
                OutMatrix.append(rowdata)
            np.save(path, np.array(OutMatrix))

    def openNPY(self):
        home = str(Path.home())
        filename =  QFileDialog.getOpenFileName(self, 'Open .NPY file', home,".NPY files (*.npy);;.CSV files (*.csv)")[0]
        data=[]
        datafr=[]
        if filename != "":
            if filename != ".npy" in filename:
                data=np.load(filename,allow_pickle=True)
                datafr = pd.DataFrame.from_records(data.tolist())
            else:
                data = np.array(pd.read_csv(filename).values.tolist())

            npyfile=NPYfile(data,filename)
            print(npyfile)
            self.setWindowTitle('NPYViewer:  '+npyfile.filename)
            self.infoLb.setText("NPY Properties:\n"+str(npyfile))
            self.tableWidget.clear()

            rows= npyfile.data.shape[0]
            #print(npyfile.data.shape[0][0])

            if filename != ".npy" in filename:
                self.tableWidget.setRowCount(data.shape[0])
                self.tableWidget.setColumnCount(data.shape[1])
            else:
                self.tableWidget.setRowCount(data.shape[0])
                self.tableWidget.setColumnCount(data.shape[1])
                print (npyfile.data)
            for i, value1 in enumerate(npyfile.data):  # loop over items in first column
                print (value1)
                for j, value in enumerate(value1):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
                    #print(i,j)
                    #print(value)

            #for n, value in enumerate(df['T']):  # loop over items in second column
            #    self.data.setItem(n, 1, QTableWidgetItem(str(value)))



    def createMenu(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        openAct = QAction(QIcon('Open.png'), '&Open', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open .NPY file')
        openAct.triggered.connect(self.openNPY)
        self.statusBar()

        saveAct = QAction(QIcon('Save.png'), '&Save As', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('Save As')
        saveAct.triggered.connect(self.saveAs)
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(exitAct)

    def initUI(self):
        self.createMenu()

        self.infoLb = QLabel("NPY Properties:")
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(100)

        # table selection change
        #self.tableWidget.doubleClicked.connect(self.on_click)

        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('NPYViewer')

        self.widget = QWidget(self)
        layout = QGridLayout()
        layout.addWidget(self.infoLb)
        layout.addWidget(self.tableWidget)
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)
        #self.tableWidget.setItesetTextAlignmentmDelegate(AlignDelegate())


        self.layout = QVBoxLayout()

        self.setLayout(self.layout)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = MainApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
