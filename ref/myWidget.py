from PySide6 import QtCore, QtWidgets, QtGui
import Outlook

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


        self.button = QtWidgets.QPushButton("Click me!")
        self.button2 = QtWidgets.QPushButton("play")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignLeft)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button)
        
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)
        #self.clicked.connect(self.aaa)

    @QtCore.Slot()
    def magic(self):
        Outlook.display_folder()

    def aaa(self):
        pass
