from PyQt5 import QtWidgets, uic, QtCore, QtGui
from  PyQt5 import *
import serial.tools.list_ports
app = QtWidgets.QApplication([])
dlg = uic.loadUi("GUI/AS_Wath_APP.ui")
dlg.setWindowIcon(QtGui.QIcon('GUI/icon.png'))


def ports():
    ports = list(serial.tools.list_ports.comports())

    if ports != []:
        for p in ports:
            dlg.PortList.addItem(p)

        dlg.PortList.setEnabled(True)
        dlg.ActualiseTime.setEnabled(True)
        dlg.Execute.setEnabled(True)

    else:
        dlg.PortList.addItem("Nothing is connected!")
        dlg.PortList.setEnabled(False)
        dlg.ActualiseTime.setEnabled(False)
        dlg.Execute.setEnabled(False)

dlg.Restart.clicked.connect(ports)
ports()
dlg.show()
app.exec()
