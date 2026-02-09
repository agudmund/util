import sys
from PySide6.QtWidgets import (
    QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem,
    QGraphicsEllipseItem, QGraphicsPathItem, QMainWindow,
    QGraphicsSimpleTextItem, QGraphicsDropShadowEffect
)
from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import (
    QPen, QBrush, QPainterPath, QPainter, QColor, QLinearGradient, QPalette
)

class Port(QGraphicsEllipseItem):
    def __init__(self, parent_node, is_output=False):
        super().__init__(-10, -10, 20, 20, parent_node)
        
        # Muted pastels: soft peach for input, pale mint for output
        base_color = QColor(180, 140, 120) if not is_output else QColor(140, 190, 160)  # peach / mint
        self.setBrush(QBrush(base_color.lighter(115)))  # soft, desaturated
        self.setPen(QPen(QColor(60, 60, 80, 100), 1))
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable, False)
        self.edge = None

        # Gentle muted glow
        glow = QGraphicsDropShadowEffect()
        glow.setBlurRadius(12)
        glow.setColor(base_color.darker(140))
        glow.setOffset(0, 0)
        self.setGraphicsEffect(glow)

class Node(QGraphicsRectItem):
    def __init__(self, x, y, label="Node"):
        super().__init__(0, 0, 160, 100)
        self.setPos(x, y)
        self.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemSendsGeometryChanges)

        # Soft muted pastel glass: very translucent lavender/mint tint
        self.setBrush(QColor(220, 210, 235, 65))  # light lavender with alpha
        self.setPen(QPen(QColor(160, 150, 180, 90), 1.5, Qt.PenStyle.SolidLine))

        self.round_radius = 18  # softer, larger rounding

        # Label – soft off-white
        self.text = QGraphicsSimpleTextItem(label, self)
        self.text.setBrush(QBrush(QColor(240, 240, 245)))
        font = self.text.font()
        font.setPointSize(12)
        font.setBold(True)
        self.text.setFont(font)
        self.text.setPos(16, 12)

        # Ports
        self.output_port = Port(self, is_output=True)
        self.output_port.setPos(160, 50)

        self.input_port = Port(self, is_output=False)
        self.input_port.setPos(0, 50)

        # Subtle floating shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(24)
        shadow.setColor(QColor(0, 0, 0, 140))
        shadow.setOffset(0, 6)
        self.setGraphicsEffect(shadow)

    def paint(self, painter: QPainter, option, widget=None):
        # Inner subtle highlight for glass depth
        painter.setBrush(Qt.NoBrush)
        highlight_pen = QPen(QColor(255, 255, 255, 40), 1.2)
        painter.setPen(highlight_pen)
        painter.drawRoundedRect(self.rect().adjusted(1, 1, -1, -1), self.round_radius, self.round_radius)

        # Main glass shape
        painter.setPen(self.pen())
        painter.setBrush(self.brush())
        painter.drawRoundedRect(self.rect(), self.round_radius, self.round_radius)

        super().paint(painter, option, widget)

    def itemChange(self, change, value):
        if change == QGraphicsRectItem.GraphicsItemChange.ItemPositionHasChanged:
            if hasattr(self, 'output_port') and self.output_port.edge:
                self.output_port.edge.update_path()
        return super().itemChange(change, value)

class Edge(QGraphicsPathItem):
    def __init__(self, source_port, target_port=None):
        super().__init__()
        self.source = source_port
        self.target = target_port
        
        # Soft muted pastel line (lavender-gray with slight warmth)
        self.setPen(QPen(QColor(190, 180, 210, 160), 3.5, Qt.PenStyle.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        self.update_path()

        # Very gentle glow
        glow = QGraphicsDropShadowEffect()
        glow.setBlurRadius(10)
        glow.setColor(QColor(180, 170, 200, 100))
        glow.setOffset(0, 0)
        self.setGraphicsEffect(glow)

    def update_path(self):
        path = QPainterPath()
        src_pos = self.source.scenePos()
        tgt_pos = self.target.scenePos() if self.target else src_pos

        ctrl1 = QPointF(src_pos.x() + 80, src_pos.y())
        ctrl2 = QPointF(tgt_pos.x() - 80, tgt_pos.y())
        path.moveTo(src_pos)
        path.cubicTo(ctrl1, ctrl2, tgt_pos)
        self.setPath(path)

class NodePlayground(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tiny Playground")
        self.resize(1000, 700)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.view.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        self.setCentralWidget(self.view)

        # Darkish muted pastel background gradient
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(45, 40, 65))
        gradient.setColorAt(1, QColor(30, 25, 50))
        self.scene.setBackgroundBrush(QBrush(gradient))

        # Example nodes
        node1 = Node(140, 180, "Input")
        node2 = Node(480, 240, "Output")
        self.scene.addItem(node1)
        self.scene.addItem(node2)

        self.temp_edge = Edge(node1.output_port)
        self.scene.addItem(self.temp_edge)

        self.edge = Edge(node1.output_port, node2.input_port)
        self.scene.addItem(self.edge)
        node1.output_port.edge = self.edge
        self.temp_edge.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Soft dark palette
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(35, 30, 55))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(230, 230, 240))
    palette.setColor(QPalette.ColorRole.Base, QColor(45, 40, 65))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(50, 45, 70))
    palette.setColor(QPalette.ColorRole.Text, QColor(230, 230, 240))
    palette.setColor(QPalette.ColorRole.Button, QColor(50, 45, 70))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(230, 230, 240))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(160, 140, 200, 180))
    palette.setColor(QPalette.ColorRole.HighlightedText, Qt.black)
    app.setPalette(palette)

    window = NodePlayground()
    window.show()
    sys.exit(app.exec())