from PySide6 import QtGui, QtWidgets, QtCore

import client
import test_ui
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
client.init()
class App(QtWidgets.QMainWindow, test_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_liked_tracks()
        self.pushButton.clicked.connect(self.download_track)

    def setup_liked_tracks(self):
        temp = client.get_user_liked_track()
        for i in temp:
            self.listWidget.addItem(f"{i.id} - {i.title} - {i.artists[0]['name']}")


    def download_track(self):
        t = self.listWidget.selectedItems()[0].text().split(" - ")
        client.download_track(int(t[0]), t[1], t[2])




if __name__ == "__main__":
    app = QtWidgets.QApplication()
    win = App()
    win.show()
    app.exec()