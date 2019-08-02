pYadiv Readme file 


1) Introduction
This is "python" Yet Another Dicom Image Viewer (pYadiv). It is a lightweight DICOM image viewer that will allow you to view most Radiology and Oncology image formats. It is not a medical image viewer and is intended for quality assurance purposes only. Image data is presented as pixel value and not Hounsfield or other units. 

Multiple images can be opened at once. Scroll through the images using the mouse wheel. Left click on the image and drag left-right to change the window width. Left click and drag up-down to change the window centre. Drag and drop of multiple images is supported.

2) Licence
Please read the file Licence.txt. This means that if as a result of using this program you fry your patients, trash your linac, nuke the cat, blow the city power in a ten block radius and generally cause global thermonuclear meltdown! Sorry, you were warned!

3) System Requirements
Currently running on Fedora 28/KDE 5.13/QT 5.11
Windows users will need to install a python stack (such as anaconda) and Pyside2/QT5.
Note: If you use anaconda you must install Pyside2 with conda and not Pip otherwise the paths will be incorrect.

4) Dependencies
* PySide2
* pydicom
* NumPy

5) Installation
Copy the files into a directory

6) Use
Open a console window, change to the above directory and run
python3 pYadiv.pyw

Open a DICOM file either from the menu or toolbar. Drag and drop from your
favourite file manager is also supported.

7) History
15/07/2019 version 0.1 released
2/8/2019   fix 3D dose matrix load

