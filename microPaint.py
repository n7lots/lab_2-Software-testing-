import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QMenu, QToolBar)
from PySide6.QtGui import QMouseEvent, QPaintEvent, QPainter, QPen, QColor, QAction, QPixmap, QResizeEvent
from PySide6.QtCore import Qt, QPoint


class DrawingArea(QWidget):
    def __init__(self, parent: None = None):
        super().__init__(parent=parent)
        self.setMinimumSize(600, 400)
        self.pixmap = QPixmap(self.size())
        self.pixmap.fill(Qt.black) #тут був білий

        self.last_point = QPoint()
        self.start_point = QPoint()
        self.pen_color = QColor(Qt.black)
        self.pen_width = 4 #було три
        self.drawing_mode = 'line' # line - від руки
        self.is_drawing = False

    def resizeEvent(self, event: QResizeEvent) -> None:
        if self.width() > self.pixmap.width() or self.height() > self.pixmap.height():
            new_pixmap = QPixmap(self.size())
            new_pixmap.fill(Qt.black) #тут також мав бути білий
            painter = QPainter(new_pixmap)
            painter.drawPixmap(0, 0, self.pixmap)
            painter.end()
            self.pixmap = new_pixmap
        super().resizeEvent(event)

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap)

        if self.is_drawing and self.drawing_mode == 'rect':
            painter.setPen(QPen(self.pen_color, self.pen_width, Qt.SolidLine))
            painter.drawRect(self.start_point.x(), self.start_point.y(), self.last_point.x() - self.start_point.x(), self.last_point.y() - self.start_point.y())

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.LeftButton:
            self.is_drawing = True
            self.start_point = event.position().toPoint()
            self.last_point = self.start_point

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if event.buttons() & Qt.LeftButton and self.is_drawing and self.drawing_mode != 'rect':
            painter = QPainter(self.pixmap)
            painter.setPen(QPen(self.pen_color, self.pen_width, Qt.SolidLine))
            painter.drawLine(self.last_point, event.position().toPoint())
            painter.end()

        self.last_point = event.position().toPoint()
        self.update()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton and self.is_drawing and self.drawing_mode == 'rect':
            painter = QPainter(self.pixmap)
            painter.setPen(QPen(self.pen_color, self.pen_width, Qt.SolidLine))
            painter.drawRect(self.start_point.x(), self.start_point.y(), self.last_point.x() - self.start_point.x(), self.last_point.y() - self.start_point.y())
            painter.end()

            self.is_drawing = False
            self.update()


    def set_color(self, color):
        self.pen_color = QColor(color)

    def clear(self):
        self.update() #тут не вистачає строчки коду

    def set_drawing_mode(self, mode):
        self.drawing_mode = mode


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Drawing App')
        self.resize(800, 600)

        self.drawing_area = DrawingArea()
        self.setCentralWidget(self.drawing_area)

        toolbar = QToolBar('Drawing tools')
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        black_action = QAction('Чорний', self)
        black_action.triggered.connect(lambda: self.drawing_area.set_color(Qt.black))
        toolbar.addAction(black_action)

        red_action = QAction('Червоний', self)
        red_action.triggered.connect(lambda: self.drawing_area.set_color(Qt.green)) #тут має бути червоний
        toolbar.addAction(red_action)

        blue_action = QAction('Синій', self)
        blue_action.triggered.connect(lambda: self.drawing_area.set_color(Qt.blue))
        toolbar.addAction(blue_action)

        rect_action = QAction('Прямокутник', self)
        rect_action.triggered.connect(lambda: self.drawing_area.set_drawing_mode("rect"))
        toolbar.addAction(rect_action)

        line_action = QAction('Лінія (від руки)', self)
        line_action.triggered.connect(lambda: self.drawing_area.set_drawing_mode("rect"))  #тут так як і в 101, а має бути не rect
        toolbar.addAction(line_action)

        clear_action = QAction('Очистити', self)
        clear_action.triggered.connect(self.drawing_area.clear)
        toolbar.addAction(clear_action)

        toolbar.setStyleSheet("""
        QToolButton[text="Чорний"] { color: red; }
        QToolButton[text="Синій"] { color: orange; }
        QToolButton[text="Червоний"] { color: blue; }
        """) #тут треба змінити кольори відповідно назвам

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())