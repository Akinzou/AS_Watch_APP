from PyQt5 import QtWidgets, uic, QtCore, QtGui
from  PyQt5 import *
import serial.tools.list_ports
app = QtWidgets.QApplication([])
dlg = uic.loadUi("GUI/AS_Watch_APP.ui")
dlg.setWindowIcon(QtGui.QIcon('GUI/icon.png'))

def send():
    print(dlg.PortList.currentText())

    if dlg.ActualiseTime.isChecked() == True:
        print("Actualise")

    else:
        print("Dont")

    print(dlg.SeaPressure.value())

def checkPorts():
    ports = list(serial.tools.list_ports.comports())
    dlg.PortList.clear()

    if ports != []:
        for p in ports:
            dlg.PortList.addItem(str(p))

        dlg.PortList.setEnabled(True)
        dlg.ActualiseTime.setEnabled(True)
        dlg.Execute.setEnabled(True)
        dlg.SeaPressure.setEnabled(True)

    else:
        dlg.PortList.addItem("Nothing is connected!")
        dlg.PortList.addItem("Test")
        dlg.PortList.setEnabled(False)
        dlg.ActualiseTime.setEnabled(False)
        dlg.Execute.setEnabled(False)
        dlg.SeaPressure.setEnabled(False)

dlg.Refresh.clicked.connect(checkPorts)
dlg.Execute.clicked.connect(send)
checkPorts()
dlg.show()
app.exec()
