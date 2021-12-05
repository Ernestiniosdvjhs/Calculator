import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_zn = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_zn)
        self.vbox.addLayout(self.hbox_result)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_0 = QPushButton("0", self)
        self.hbox_first.addWidget(self.b_0)

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_4 = QPushButton("4", self)
        self.hbox_first.addWidget(self.b_4)

        self.b_dt = QPushButton(".", self)
        self.hbox_first.addWidget(self.b_dt)

        self.b_plus = QPushButton("+", self)
        self.hbox_zn.addWidget(self.b_plus)

        self.b_minus = QPushButton("-", self)
        self.hbox_zn.addWidget(self.b_minus)

        self.b_um = QPushButton("*", self)
        self.hbox_zn.addWidget(self.b_um)

        self.b_del = QPushButton("/", self)
        self.hbox_zn.addWidget(self.b_del)

        self.b_o = QPushButton("C", self)
        self.hbox_result.addWidget(self.b_o)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_um.clicked.connect(lambda: self._operation("*"))
        self.b_del.clicked.connect(lambda: self._operation("/"))
        self.b_o.clicked.connect(lambda: self._operation("C"))
        self.b_result.clicked.connect(self._result)

        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_dt.clicked.connect(lambda: self._button("."))

    def _button(self, param):
        line = self.input.text()
        if param == ".":
            if line:
                self.input.setText(line + param)
            else:
                self.input.setText("")
        else:
            self.input.setText(line + param)
        if param == "*" or param == "+" or param == "/":
            self.input.setText("")

    def _operation(self, op):
        if self.input.text():
            self.num_1 = float(self.input.text())
            self.op = op
            self.input.setText("")

    def _result(self):
        if self.input.text() and self.op:
            self.num_2 = float(self.input.text())
            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))
            elif self.op == "-":
                self.input.setText(str(self.num_1 - self.num_2))
            elif self.op == "/":
                if self.num_2 != 0:
                    self.input.setText(str(self.num_1 / self.num_2))
                else:
                    self.input.setText("Can't divide by 0")
            if self.op == "*":
                self.input.setText(str(self.num_1 * self.num_2))


app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_())
