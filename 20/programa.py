from dizainas import Ui_MainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
# programos paleidimas
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.minus.clicked.connect(self.minusas)
        self.plius.clicked.connect(self.pliusas)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def minusas(self):
        skaicius = int(self.label.text())
        naujas_skaicius = skaicius - 1
        self.label.setText(str(naujas_skaicius))
        self.zodis.setText('sumazinta')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def pliusas(self):
        skaicius = int(self.label.text())
        naujas_skaicius = skaicius + 1
        self.label.setText(str(naujas_skaicius))
        self.zodis.setText('padidinta')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

app = QApplication([])
window = Window()

window.show()
app.exec()


