from PySide6.QtWidgets import QMainWindow, QPushButton, QLineEdit, QMessageBox, QApplication, QVBoxLayout, QWidget
from PySide6.QtGui import QAction
from PySide6.QtWebEngineWidgets import QWebEngineView
class Aken(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pohiwidget = QWidget()
        self.riba = QVBoxLayout(self.pohiwidget)
        self.leheriba = QLineEdit()
        self.leheriba.editingFinished.connect(self.lae_leht)
        self.riba.addWidget(self.leheriba)
        self.lehevaade = QWebEngineView()
        self.lehevaade.loadFinished.connect(self.leht_laetud)
        self.lehevaade.load("https://valenimi4.github.io/puudel_ploom/otsing.html")
        self.riba.addWidget(self.lehevaade)
        self.setCentralWidget(self.pohiwidget)
        self.setWindowTitle(" - puudel ploom")
        self.menuu = self.menuBar()
        self.aken = self.menuu.addMenu("&Aken")
        self.ajalugu = self.menuu.addMenu("&Ajalugu")
        self.abi = self.menuu.addMenu("&Abi")
        self.aken.addAction(QAction("Välju", parent=self, triggered=exit))
        self.ajalugu.addAction(QAction("Tagasi", parent=self, triggered=self.lehevaade.back))
        self.ajalugu.addAction(QAction("Edasi", parent=self, triggered=self.lehevaade.forward))
        self.abi.addAction(QAction("Info puudel ploomi kohta", parent=self, triggered=self.puudel_ploomist))
        self.abi.addAction(QAction("About Qt", parent=self, triggered=self.__about_qt))
    def puudel_ploomist(self):
        QMessageBox.about(self, "puudel ploom", "puudel ploom on ajuvaba brauser, mille tegi valeNimi4 ja mis kasutab pySide6.")
    def __about_qt(self):
        QMessageBox.aboutQt(self)
    def lae_leht(self):
        url = self.leheriba.text()
        if url.startswith("https://") or url.startswith("http://"):
            self.lehevaade.load(url)
        else:
            self.lehevaade.load("http://" + url)
    def leht_laetud(self, ok=True):
        self.setWindowTitle(self.lehevaade.title() + " - puudel ploom")
        self.leheriba.setText(self.lehevaade.url().toString())
programm = QApplication([])
aken = Aken()
aken.show()
programm.exec()