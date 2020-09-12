from PyQt5 import QtWidgets, uic
import serial.tools.list_ports
app = QtWidgets.QApplication([])
dlg = uic.loadUi("GUI/AS_Watch_APP.ui")

ports = list(serial.tools.list_ports.comports())

if ports != []:
    for p in ports:
        dlg.PortList.addItem(p)

else:
    dlg.PortList.addItem("Nothing is connected!")
    dlg.PortList.setEnabled(False)
    dlg.ActualiseTime.setEnabled(False)


dlg.show()
app.exec()