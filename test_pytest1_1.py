import sys
import pytest
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from microPaint import DrawingArea

@pytest.fixture(scope="session")
def app():
    return QApplication(sys.argv)


@pytest.fixture
def widget(app):
    return DrawingArea()


#Тест 1: параметризована перевірка кольорів
@pytest.mark.parametrize("color", [
    Qt.black,
    Qt.blue,
    Qt.red,
])
def test_set_color_parametrize(widget, color):
    widget.set_color(color)
    assert widget.pen_color == QColor(color)

# тест 2: перевірка режиму малювання лінією
def test_drawing_mode(widget):
    widget.set_drawing_mode("line")
    assert widget.drawing_mode == "line"