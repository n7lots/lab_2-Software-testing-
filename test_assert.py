import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from microPaint import DrawingArea

app = QApplication(sys.argv)

widget = DrawingArea()

# Assert тест 1 (чорний колір)
widget.set_color(Qt.black)
assert widget.pen_color == QColor(Qt.black)

# Assert тест 2 (малюнок лінією)
widget.set_drawing_mode("line")
assert widget.drawing_mode == "line"

print("All of assert tests - passed")