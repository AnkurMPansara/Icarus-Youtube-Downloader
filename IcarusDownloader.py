from pytube import YouTube, request
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import math
import requests
import time

url_list = []
i_list = []
loc = "C:/"
is_paused = is_cancelled = False
va = [17, 5, 18, 44, 22, 46]
vo = [160, 133, 134, 135, 136, 137]
ao = [140, 140, 140, 140, 140, 140]
db = [va, ao, vo]
downloaded = 0
filesize = 0
pr = 0
first = True

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainScreen = QtWidgets.QLabel(self.centralwidget)
        self.MainScreen.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.MainScreen.setText("")
        self.MainScreen.setPixmap(QtGui.QPixmap("Images\screen.png"))
        self.MainScreen.setScaledContents(True)
        self.MainScreen.setObjectName("MainScreen")

        self.url = QtWidgets.QLineEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(260, 170, 861, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 42, 42))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.url.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.url.setFont(font)
        self.url.setAutoFillBackground(False)
        self.url.setFrame(False)
        self.url.setObjectName("url")
        self.url.returnPressed.connect(self.data)

        self.VideoTitle = QtWidgets.QLabel(self.centralwidget)
        self.VideoTitle.setGeometry(QtCore.QRect(80, 260, 991, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.VideoTitle.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.VideoTitle.setFont(font)
        self.VideoTitle.setTextFormat(QtCore.Qt.AutoText)
        self.VideoTitle.setScaledContents(False)
        self.VideoTitle.setWordWrap(False)
        self.VideoTitle.setObjectName("VideoTitle")

        self.VideoDetails = QtWidgets.QLabel(self.centralwidget)
        self.VideoDetails.setGeometry(QtCore.QRect(80, 340, 1011, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(131, 131, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(131, 131, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.VideoDetails.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.VideoDetails.setFont(font)
        self.VideoDetails.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.VideoDetails.setObjectName("VideoDetails")

        self.TypeSelect = QtWidgets.QComboBox(self.centralwidget)
        self.TypeSelect.setGeometry(QtCore.QRect(80, 390, 121, 31))
        self.TypeSelect.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.TypeSelect.setFont(font)
        self.TypeSelect.setObjectName("TypeSelect")
        self.TypeSelect.addItem("")
        self.TypeSelect.addItem("")
        self.TypeSelect.addItem("")

        self.Resolution = QtWidgets.QComboBox(self.centralwidget)
        self.Resolution.setGeometry(QtCore.QRect(240, 390, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Resolution.setFont(font)
        self.Resolution.setObjectName("Resolution")
        self.Resolution.addItem("")
        self.Resolution.addItem("")
        self.Resolution.addItem("")
        self.Resolution.addItem("")
        self.Resolution.addItem("")
        self.Resolution.addItem("")

        self.DownloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadButton.setGeometry(QtCore.QRect(420, 530, 200, 49))
        self.DownloadButton.setAutoFillBackground(False)
        self.DownloadButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images\download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DownloadButton.setIcon(icon)
        self.DownloadButton.setIconSize(QtCore.QSize(200, 49))
        self.DownloadButton.setCheckable(False)
        self.DownloadButton.setAutoDefault(False)
        self.DownloadButton.setDefault(False)
        self.DownloadButton.setFlat(True)
        self.DownloadButton.setObjectName("DownloadButton")
        self.DownloadButton.clicked.connect(self.start_download)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 870, 941, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")

        self.Queue = QtWidgets.QLabel(self.centralwidget)
        self.Queue.setGeometry(QtCore.QRect(110, 820, 781, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.Queue.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Queue.setFont(font)
        self.Queue.setObjectName("Queue")

        self.lDownloadSpeed = QtWidgets.QLabel(self.centralwidget)
        self.lDownloadSpeed.setGeometry(QtCore.QRect(1060, 870, 85, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lDownloadSpeed.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lDownloadSpeed.setFont(font)
        self.lDownloadSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.lDownloadSpeed.setObjectName("lDownloadSpeed")

        self.Remaining = QtWidgets.QLabel(self.centralwidget)
        self.Remaining.setGeometry(QtCore.QRect(1160, 870, 180, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(216, 216, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.Remaining.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Remaining.setFont(font)
        self.Remaining.setAlignment(QtCore.Qt.AlignCenter)
        self.Remaining.setObjectName("Remaining")

        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setGeometry(QtCore.QRect(1350, 865, 71, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Pause.setFont(font)
        self.Pause.setObjectName("Pause")
        self.Pause.clicked.connect(self.toggle_download)

        self.Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel.setGeometry(QtCore.QRect(1430, 865, 71, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Cancel.setFont(font)
        self.Cancel.setObjectName("Cancel")
        self.Cancel.clicked.connect(self.cancel_download)

        self.Icon = QtWidgets.QLabel(self.centralwidget)
        self.Icon.setGeometry(QtCore.QRect(1136, 258, 640, 360))
        self.Icon.setText("")
        self.Icon.setScaledContents(True)
        self.Icon.setObjectName("Icon")

        self.DownloadLocation = QtWidgets.QLabel(self.centralwidget)
        self.DownloadLocation.setGeometry(QtCore.QRect(120, 450, 431, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.DownloadLocation.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.DownloadLocation.setFont(font)
        self.DownloadLocation.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DownloadLocation.setObjectName("DownloadLocation")

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(80, 450, 27, 22))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.browse)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.VideoTitle.setText(_translate("MainWindow", "Video Title"))
        self.VideoDetails.setText(_translate("MainWindow", "Video Details"))
        self.TypeSelect.setItemText(0, _translate("MainWindow", "Video"))
        self.TypeSelect.setItemText(1, _translate("MainWindow", "Audio Only"))
        self.TypeSelect.setItemText(2, _translate("MainWindow", "Video Only"))
        self.Resolution.setItemText(0, _translate("MainWindow", "144p"))
        self.Resolution.setItemText(1, _translate("MainWindow", "240p"))
        self.Resolution.setItemText(2, _translate("MainWindow", "360p"))
        self.Resolution.setItemText(3, _translate("MainWindow", "480p"))
        self.Resolution.setItemText(4, _translate("MainWindow", "720p"))
        self.Resolution.setItemText(5, _translate("MainWindow", "1080p"))
        self.Queue.setText(_translate("MainWindow", " "))
        self.lDownloadSpeed.setText(_translate("MainWindow", "-- mB/s"))
        self.Remaining.setText(_translate("MainWindow", "-/-"))
        self.Pause.setText(_translate("MainWindow", "Pause"))
        self.Cancel.setText(_translate("MainWindow", "Cancel"))
        self.DownloadLocation.setText(_translate("MainWindow", "C:\\"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

    def sd(self):
        url = self.url.text()
        yt = YouTube(url)
        image = QtGui.QImage()
        image.loadFromData(requests.get(yt.thumbnail_url).content)
        self.VideoTitle.setText(yt.title)
        self.VideoDetails.setText(yt.author)
        self.Icon.setPixmap(QtGui.QPixmap(image))
        self.Icon.show()

    def data(self):
        threading.Thread(target=self.sd, daemon=True).start()

    def toggle_download(self):
        global is_paused
        if is_paused:
            self.Pause.setText("Pause")
        else:
            self.Pause.setText("Resume")
        is_paused = not is_paused

    def cancel_download(self):
        global is_cancelled
        is_cancelled = True

    def download_video(self, url, i):
        global is_paused, is_cancelled, loc, downloaded, filesize, pr
        yt = YouTube(url)
        stream = yt.streams.get_by_itag(self.getitag())
        if stream == []:
            stream = yt.streams.filter(progressive=True).get_highest_resolution()
        filesize = stream.filesize
        with open(loc + "/" + yt.title + ".mp4", "wb") as f:
            is_paused = is_cancelled = False
            stream = request.stream(stream.url)
            downloaded = 0
            while True:
                if is_cancelled:
                    self.progressBar.setProperty("value", 0)
                    break
                if is_paused:
                    continue
                chunk = next(stream, None)
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                pr = (int)((downloaded*100)/filesize)
                if pr == 100:
                    url_list.pop(0)
                    i_list.pop(0)
                    self.Queue.setText("Download Completed")
                    break
            f.close()
            if url_list and pr == 100:
                self.Queue.setText(YouTube(url_list[0]).title)
                threading.Thread(target=self.download_video, args=(url_list[0], i_list[0]), daemon=True).start()

    def start_download(self):
        global url_list, i_list, first
        url_list.append(self.url.text())
        i_list.append(0)
        if len(url_list) == 1:
            self.Queue.setText(YouTube(url_list[0]).title)
            threading.Thread(target=self.download_video, args=(url_list[0], i_list[0]), daemon=True).start()
            threading.Thread(target=self.setprogress, daemon=True).start()

    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    def setprogress(self):
        global downloaded, filesize, pr
        while True:
            spd = downloaded
            time.sleep(1)
            spd = downloaded - spd
            speed = self.convert_size(spd) + "/s"
            self.lDownloadSpeed.setText(speed)
            self.progressBar.setProperty("value", pr)
            rem = self.convert_size(downloaded) + "/" + self.convert_size(filesize)
            self.Remaining.setText(rem)

    def browse(self):
        global loc
        loc = QtWidgets.QFileDialog().getExistingDirectory(None, "Select Folder")
        self.DownloadLocation.setText(loc)

    def getitag(self):
        return db[self.TypeSelect.currentIndex()][self.Resolution.currentIndex()]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon('Icon.ico'))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
