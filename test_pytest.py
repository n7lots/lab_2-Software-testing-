import sys
import pytest
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from microPaint import DrawingArea

app = QApplication(sys.argv)

widget = DrawingArea()


def test_assert_color_black():
    widget.set_color(Qt.black)
    assert widget.pen_color == QColor(Qt.black)


def test_assert_drawing_line():
    widget.set_drawing_mode("line")
    assert widget.drawing_mode == "line"