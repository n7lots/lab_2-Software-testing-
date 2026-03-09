import sys
import pytest
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from microPaint import DrawingArea

app = QApplication.instance()
if app is None:
    app = QApplication(sys.argv)

widget = DrawingArea()



#  тест (буде пропущено)
@pytest.mark.skip(reason="Тест пропущено")
def test_skip():
    widget.set_color(Qt.red)
    assert widget.pen_color == QColor(Qt.red)


# очікується провал
@pytest.mark.xfail(reason="Очікується помилка демонстрації")
def test_xfail():
    widget.set_drawing_mode("rect")
    assert widget.drawing_mode == "line"