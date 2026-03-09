import sys
import unittest
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from microPaint import DrawingArea


class TestDrawingArea(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
        self.widget = DrawingArea()

    # Тест 1: перевірка зміни кольору на червоний
    def test_set_color(self):
        self.widget.set_color(Qt.red) #очікуване
        self.assertEqual(self.widget.pen_color, Qt.red)

    # Тест 2: перевірка зміни режиму малювання
    def test_set_drawing(self):
        self.widget.set_drawing_mode("rect") #очікуване
        self.assertEqual(self.widget.drawing_mode, "rect")


if __name__ == "__main__":
    unittest.main()