import sys
from enum import nonmember

from PyQt6.QtWidgets import QLabel, QLineEdit, QMessageBox, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, \
 QWidget, QMainWindow

from database import Database
from PyQt6 import Qt
FROM PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QHearderView,
    QMainWindow,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget)

class MainWindow(QMainWindow):
  def __init__(self):
   super().__init__()
   self.db = Database()
   self.selected_id = none
   self.setWindowTitle("CRUD")
   self.resize(650,500)
   self.init_ui()

  def init_ui(self):
   central_widget = QWidget()
   self.setCentralWidget(central_widget)


