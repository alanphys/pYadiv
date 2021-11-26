"""
========================================
Show a dicom image or sequence of images
========================================

Show a dicom image or sequence of images using Pyside and QT5.
Usage: python3 DivPy.pyw dicom_filename
Or drag and drop from your file manager.

"""

# author : AC Chamberlain <alanphys@yahoo.co.uk>
# copyright: AC Chamberlain (c) 2019
# based on the scripts from Caduceus by Daniel Coelho

import sys
import os
from platform import system
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PySide2.QtGui import QPixmap, QImage, QMouseEvent
from PySide2.QtCore import SIGNAL, QObject, Qt
from pYadivForm import Ui_pYadivForm
from aboutpackage import About
from Imager import Imager
import pydicom

class pYadivForm(QMainWindow):
    def __init__(self, parent=None):
        super(pYadivForm, self).__init__()
        self.imager = None
        self.mouse_button_down = False
        self.mouse_last_pos = None
        self.ui = Ui_pYadivForm()
        self.ui.setupUi(self)
        self.ui.statusbar.showMessage('Open DICOM file or drag and drop')
        QObject.connect(self.ui.actionOpen, SIGNAL('triggered()'), self.openfile)
        QObject.connect(self.ui.actionAbout, SIGNAL('triggered()'), self.showabout)
        QObject.connect(self.ui.actionInvert, SIGNAL('triggered()'), self.invert)
        QObject.connect(self.ui.actionAuto_Window, SIGNAL('triggered()'), self.auto_window)

    def open_image(self, filenames):
        num_total = len(filenames)
        num_bad = 0

        # Clear non-dicom files
        datasets = []
        for file in filenames:
            try:
                ds = pydicom.dcmread(file,force=True)
                if 'TransferSyntaxUID' not in ds.file_meta:
                    ds.file_meta.TransferSyntaxUID = pydicom.uid.ImplicitVRLittleEndian
                datasets.append(ds)
            except pydicom.errors.InvalidDicomError:
                num_bad += 1
                filenames.remove(file)
        num_ok = num_total - num_bad

        # Try to sort based on instance number then SOPInstanceUID
        sorted_method = "filenames"
        try:
            datasets.sort(key=lambda x: x.InstanceNumber)
            sorted_method = "instance number"
        except AttributeError:
            try:
                datasets.sort(key=lambda x: x.SOPInstanceUID)
                sorted_method = "SOP instance UID"
            except AttributeError:
                pass

        self.imager = Imager(datasets)

        self.ui.statusbar.showMessage("Opened %d DICOM file(s) sorted on %s. Rejected %d bad files" % (num_ok, sorted_method, num_bad))

        self.show_image(self.imager.get_current_image())

    def openfile(self):
        if len(sys.argv) > 1:
            filenames = sys.argv[1]
        else:
            filenames = os.path.realpath(__file__)
        dirpath = os.path.dirname(os.path.realpath(filenames))
        ostype = system()
        if ostype == 'Linux':
            filenames = \
            QFileDialog.getOpenFileNames(self, 'Open DICOM file', dirpath, 'DICOM files (*.dcm);;All files (*)')[0]
        elif ostype == 'Windows':
            filenames = \
            QFileDialog.getOpenFileNames(self, 'Open DICOM file', dirpath, 'DICOM files (*.dcm);;All files (*.*)')[0]
        else:
            filenames = \
            QFileDialog.getOpenFileNames(self, 'Open DICOM file', dirpath, 'DICOM files (*.dcm);;All files (*)')[0]
        if filenames!= []:
            self.open_image(filenames)

    def show_image(self, numpy_array):
        if numpy_array is None:
            return

        #create a QImage from Numpy array and display it in a label
        qpImage = QImage(numpy_array, numpy_array.shape[1], numpy_array.shape[0], QImage.Format_ARGB32)
        self.ui.qlImage.setPixmap(QPixmap.fromImage(qpImage).scaled(self.ui.qlImage.width(),self.ui.qlImage.height(),Qt.KeepAspectRatio))
        self.ui.qlImage.show()

    def showabout(self):
        about = About()
        about.exec()

    def auto_window(self):
        self.imager.auto_window()
        self.show_image(self.imager.get_current_image())
        self.ui.statusbar.showMessage(
            "Window center %d, Window width %d" % (self.imager.window_center, self.imager.window_width))

    def wheelEvent(self, e):
        self.imager.index += int(e.delta()/120)
        self.show_image(self.imager.get_current_image())
        self.ui.statusbar.showMessage("Current slice %d" % (self.imager.index))

    def mousePressEvent(self, event:QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.mouse_last_pos = event.globalPos()
            self.mouse_button_down = True

    def mouseReleaseEvent(self, event:QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.mouse_last_pos = None
            self.mouse_button_down = False

    def mouseMoveEvent(self, event:QMouseEvent):
        if self.mouse_button_down:
            delta = (event.globalPos() - self.mouse_last_pos) * (self.imager.window_width/1000)
            self.mouse_last_pos = event.globalPos()

            self.imager.window_width += delta.x()
            self.imager.window_center += delta.y()

            self.show_image(self.imager.get_current_image())
            self.ui.statusbar.showMessage("Window center %d, Window width %d" % (self.imager.window_center, self.imager.window_width))

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasText():
            urls = event.mimeData().text().split("\n")
            filenames = []
            for url in urls:
                if url != "":
                    filename = url.split('/',2)[2]
                if filename != "":
                    filenames.append(filename)
            if filenames != []:
                self.open_image(filenames)

    def resizeEvent(self, event):
        if self.imager is not None:
            self.show_image(self.imager.get_current_image())

    def invert(self):
        if self.imager.invflag:
            self.imager.invflag = False
        else:
            self.imager.invflag = True
        self.show_image(self.imager.get_current_image())

def main():
    app = QApplication(sys.argv)
    window = pYadivForm()
    window.show()
    if len(sys.argv) > 1:
        filenames = sys.argv[1:]
        if filenames != []:
            window.open_image(filenames)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
