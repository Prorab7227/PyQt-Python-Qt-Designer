# -*- coding: utf-8 -*-

MULT = 2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700*MULT, 500*MULT)
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        MainWindow.setFont(font)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"background-color: rgb(241, 238, 213);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.vert_prop = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vert_prop.sizePolicy().hasHeightForWidth())
        self.vert_prop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        self.vert_prop.setFont(font)
        self.vert_prop.setStyleSheet("QWidget {\n"
"color: black;\n"
"font-family: Minecraft;\n"
f"font-size: {8*MULT}px;\n"
"border: 2px outset rgb(34, 34, 34);\n"
"background-color: rgb(81, 95, 70);\n"
"}\n"
"\n"
"QLabel {\n"
"border: None;\n"
"background-color: rgb(169, 179, 136);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"border: 2px solid rgb(185, 148, 112);\n"
"} ")
        self.vert_prop.setObjectName("vert_prop")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.vert_prop)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.one = QtWidgets.QHBoxLayout()
        self.one.setContentsMargins(5, 5, 5, 5)
        self.one.setSpacing(5)
        self.one.setObjectName("one")
        self.object_id_label = QtWidgets.QLabel(self.vert_prop)
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        self.object_id_label.setFont(font)
        self.object_id_label.setAlignment(QtCore.Qt.AlignCenter)
        self.object_id_label.setObjectName("object_id_label")
        self.one.addWidget(self.object_id_label)
        self.object_id_input = QtWidgets.QLineEdit(self.vert_prop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object_id_input.sizePolicy().hasHeightForWidth())
        self.object_id_input.setSizePolicy(sizePolicy)
        self.object_id_input.setMinimumSize(QtCore.QSize(225*MULT, 0))
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        self.object_id_input.setFont(font)
        self.object_id_input.setAlignment(QtCore.Qt.AlignCenter)
        self.object_id_input.setObjectName("object_id_input")
        self.one.addWidget(self.object_id_input)
        self.verticalLayout.addLayout(self.one)
        self.two = QtWidgets.QHBoxLayout()
        self.two.setContentsMargins(5, 5, 5, 5)
        self.two.setSpacing(5)
        self.two.setObjectName("two")
        self.nam_label = QtWidgets.QLabel(self.vert_prop)
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        self.nam_label.setFont(font)
        self.nam_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nam_label.setObjectName("nam_label")
        self.two.addWidget(self.nam_label)
        self.name_input = QtWidgets.QLineEdit(self.vert_prop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_input.sizePolicy().hasHeightForWidth())
        self.name_input.setSizePolicy(sizePolicy)
        self.name_input.setMinimumSize(QtCore.QSize(225*MULT, 0))
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        self.name_input.setFont(font)
        self.name_input.setAlignment(QtCore.Qt.AlignCenter)
        self.name_input.setObjectName("name_input")
        self.two.addWidget(self.name_input)
        self.verticalLayout.addLayout(self.two)
        self.three = QtWidgets.QHBoxLayout()
        self.three.setContentsMargins(5, 5, 5, 5)
        self.three.setSpacing(5)
        self.three.setObjectName("three")
        self.stackable_label = QtWidgets.QLabel(self.vert_prop)
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        self.stackable_label.setFont(font)
        self.stackable_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stackable_label.setObjectName("stackable_label")
        self.three.addWidget(self.stackable_label)
        self.stackable_input = QtWidgets.QLineEdit(self.vert_prop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackable_input.sizePolicy().hasHeightForWidth())
        self.stackable_input.setSizePolicy(sizePolicy)
        self.stackable_input.setMinimumSize(QtCore.QSize(225*MULT, 0))
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        self.stackable_input.setFont(font)
        self.stackable_input.setAlignment(QtCore.Qt.AlignCenter)
        self.stackable_input.setObjectName("stackable_input")
        self.three.addWidget(self.stackable_input)
        self.verticalLayout.addLayout(self.three)
        self.four = QtWidgets.QHBoxLayout()
        self.four.setContentsMargins(5, 5, 5, 5)
        self.four.setSpacing(5)
        self.four.setObjectName("four")
        self.tool_label = QtWidgets.QLabel(self.vert_prop)
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        self.tool_label.setFont(font)
        self.tool_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tool_label.setObjectName("tool_label")
        self.four.addWidget(self.tool_label)
        self.tool_input = QtWidgets.QLineEdit(self.vert_prop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_input.sizePolicy().hasHeightForWidth())
        self.tool_input.setSizePolicy(sizePolicy)
        self.tool_input.setMinimumSize(QtCore.QSize(225*MULT, 0))
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        self.tool_input.setFont(font)
        self.tool_input.setAlignment(QtCore.Qt.AlignCenter)
        self.tool_input.setObjectName("tool_input")
        self.four.addWidget(self.tool_input)
        self.verticalLayout.addLayout(self.four)
        self.five = QtWidgets.QHBoxLayout()
        self.five.setContentsMargins(5, 5, 5, 5)
        self.five.setSpacing(5)
        self.five.setObjectName("five")
        self.blast_resistance_label = QtWidgets.QLabel(self.vert_prop)
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        self.blast_resistance_label.setFont(font)
        self.blast_resistance_label.setAlignment(QtCore.Qt.AlignCenter)
        self.blast_resistance_label.setObjectName("blast_resistance_label")
        self.five.addWidget(self.blast_resistance_label)
        self.blast_resistance_input = QtWidgets.QLineEdit(self.vert_prop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blast_resistance_input.sizePolicy().hasHeightForWidth())
        self.blast_resistance_input.setSizePolicy(sizePolicy)
        self.blast_resistance_input.setMinimumSize(QtCore.QSize(225*MULT, 0))
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        self.blast_resistance_input.setFont(font)
        self.blast_resistance_input.setAlignment(QtCore.Qt.AlignCenter)
        self.blast_resistance_input.setObjectName("blast_resistance_input")
        self.five.addWidget(self.blast_resistance_input)
        self.verticalLayout.addLayout(self.five)
        self.six = QtWidgets.QHBoxLayout()
        self.six.setContentsMargins(5, 5, 5, 5)
        self.six.setSpacing(5)
        self.six.setObjectName("six")
        self.flammable_label = QtWidgets.QLabel(self.vert_prop)
        self.flammable_label.setAlignment(QtCore.Qt.AlignCenter)
        self.flammable_label.setObjectName("flammable_label")
        self.six.addWidget(self.flammable_label)
        self.flammable_input = QtWidgets.QLineEdit(self.vert_prop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flammable_input.sizePolicy().hasHeightForWidth())
        self.flammable_input.setSizePolicy(sizePolicy)
        self.flammable_input.setMinimumSize(QtCore.QSize(225*MULT, 0))
        self.flammable_input.setAlignment(QtCore.Qt.AlignCenter)
        self.flammable_input.setObjectName("flammable_input")
        self.six.addWidget(self.flammable_input)
        self.verticalLayout.addLayout(self.six)
        self.seven = QtWidgets.QHBoxLayout()
        self.seven.setContentsMargins(5, 5, 5, 5)
        self.seven.setSpacing(5)
        self.seven.setObjectName("seven")
        self.rarity_label = QtWidgets.QLabel(self.vert_prop)
        self.rarity_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rarity_label.setObjectName("rarity_label")
        self.seven.addWidget(self.rarity_label)
        self.rarity_input = QtWidgets.QLineEdit(self.vert_prop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rarity_input.sizePolicy().hasHeightForWidth())
        self.rarity_input.setSizePolicy(sizePolicy)
        self.rarity_input.setMinimumSize(QtCore.QSize(225*MULT, 0))
        self.rarity_input.setAlignment(QtCore.Qt.AlignCenter)
        self.rarity_input.setObjectName("rarity_input")
        self.seven.addWidget(self.rarity_input)
        self.verticalLayout.addLayout(self.seven)
        self.eight = QtWidgets.QHBoxLayout()
        self.eight.setContentsMargins(5, 5, 5, 5)
        self.eight.setSpacing(5)
        self.eight.setObjectName("eight")
        self.restore_label = QtWidgets.QLabel(self.vert_prop)
        self.restore_label.setAlignment(QtCore.Qt.AlignCenter)
        self.restore_label.setObjectName("restore_label")
        self.eight.addWidget(self.restore_label)
        self.restore_input = QtWidgets.QLineEdit(self.vert_prop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restore_input.sizePolicy().hasHeightForWidth())
        self.restore_input.setSizePolicy(sizePolicy)
        self.restore_input.setMinimumSize(QtCore.QSize(225*MULT, 0))
        self.restore_input.setAlignment(QtCore.Qt.AlignCenter)
        self.restore_input.setObjectName("restore_input")
        self.eight.addWidget(self.restore_input)
        self.verticalLayout.addLayout(self.eight)
        self.nine = QtWidgets.QHBoxLayout()
        self.nine.setContentsMargins(5, 5, 5, 5)
        self.nine.setSpacing(5)
        self.nine.setObjectName("nine")
        self.durability_label = QtWidgets.QLabel(self.vert_prop)
        self.durability_label.setAlignment(QtCore.Qt.AlignCenter)
        self.durability_label.setObjectName("durability_label")
        self.nine.addWidget(self.durability_label)
        self.durability_input = QtWidgets.QLineEdit(self.vert_prop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.durability_input.sizePolicy().hasHeightForWidth())
        self.durability_input.setSizePolicy(sizePolicy)
        self.durability_input.setMinimumSize(QtCore.QSize(225*MULT, 0))
        self.durability_input.setAlignment(QtCore.Qt.AlignCenter)
        self.durability_input.setObjectName("durability_input")
        self.nine.addWidget(self.durability_input)
        self.verticalLayout.addLayout(self.nine)
        self.ten = QtWidgets.QHBoxLayout()
        self.ten.setContentsMargins(5, 5, 5, 5)
        self.ten.setSpacing(5)
        self.ten.setObjectName("ten")
        self.damage_label = QtWidgets.QLabel(self.vert_prop)
        self.damage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.damage_label.setObjectName("damage_label")
        self.ten.addWidget(self.damage_label)
        self.damage_input = QtWidgets.QLineEdit(self.vert_prop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.damage_input.sizePolicy().hasHeightForWidth())
        self.damage_input.setSizePolicy(sizePolicy)
        self.damage_input.setMinimumSize(QtCore.QSize(225*MULT, 0))
        self.damage_input.setAlignment(QtCore.Qt.AlignCenter)
        self.damage_input.setObjectName("damage_input")
        self.ten.addWidget(self.damage_input)
        self.verticalLayout.addLayout(self.ten)
        self.eleven = QtWidgets.QHBoxLayout()
        self.eleven.setContentsMargins(5, 5, 5, 5)
        self.eleven.setSpacing(5)
        self.eleven.setObjectName("eleven")
        self.effect_label = QtWidgets.QLabel(self.vert_prop)
        self.effect_label.setAlignment(QtCore.Qt.AlignCenter)
        self.effect_label.setObjectName("effect_label")
        self.eleven.addWidget(self.effect_label)
        self.effect_input = QtWidgets.QLineEdit(self.vert_prop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.effect_input.sizePolicy().hasHeightForWidth())
        self.effect_input.setSizePolicy(sizePolicy)
        self.effect_input.setMinimumSize(QtCore.QSize(225*MULT, 0))
        self.effect_input.setAlignment(QtCore.Qt.AlignCenter)
        self.effect_input.setObjectName("effect_input")
        self.eleven.addWidget(self.effect_input)
        self.verticalLayout.addLayout(self.eleven)
        self.twelve = QtWidgets.QHBoxLayout()
        self.twelve.setContentsMargins(5, 5, 5, 5)
        self.twelve.setSpacing(5)
        self.twelve.setObjectName("twelve")
        self.renewable_label = QtWidgets.QLabel(self.vert_prop)
        self.renewable_label.setAlignment(QtCore.Qt.AlignCenter)
        self.renewable_label.setObjectName("renewable_label")
        self.twelve.addWidget(self.renewable_label)
        self.renewable_input = QtWidgets.QLineEdit(self.vert_prop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.renewable_input.sizePolicy().hasHeightForWidth())
        self.renewable_input.setSizePolicy(sizePolicy)
        self.renewable_input.setMinimumSize(QtCore.QSize(225*MULT, 0))
        self.renewable_input.setAlignment(QtCore.Qt.AlignCenter)
        self.renewable_input.setObjectName("renewable_input")
        self.twelve.addWidget(self.renewable_input)
        self.verticalLayout.addLayout(self.twelve)
        self.gridLayout.addWidget(self.vert_prop, 1, 0, 1, 1)
        self.act_buttons = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(11)
        self.act_buttons.setFont(font)
        self.act_buttons.setStyleSheet("QWidget{\n"
"font-family: Minecraft;\n"
"}\n"
"\n"
"QPushButton {\n"
f"font-size: {11*MULT}px;\n"
"border: 2px rgb(86, 86, 86);\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"background-color: rgb(185, 148, 112);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(144, 114, 87);\n"
"}")
        self.act_buttons.setObjectName("act_buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.act_buttons)
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_button = QtWidgets.QPushButton(self.act_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        self.add_button.setMinimumSize(QtCore.QSize(110*MULT, 30*MULT))
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("color: rgb(82, 120, 83);")
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.delete_button = QtWidgets.QPushButton(self.act_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        self.delete_button.setMinimumSize(QtCore.QSize(110*MULT, 30*MULT))
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet("color: rgb(223, 46, 56);")
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        self.clear_button = QtWidgets.QPushButton(self.act_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        self.clear_button.setMinimumSize(QtCore.QSize(90*MULT, 25*MULT))
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        self.clear_button.setFont(font)
        self.clear_button.setAutoDefault(False)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout.addWidget(self.clear_button)
        self.gridLayout.addWidget(self.act_buttons, 0, 0, 1, 1)
        self.main_list = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(12)
        self.main_list.setFont(font)
        self.main_list.setStyleSheet("QListWidget {\n"
f"font-size: {9*MULT}px;\n"
"font-family: Minecraft;\n"
"border: 2px dotted rgb(34, 34, 34);\n"
"}")
        self.main_list.setObjectName("main_list")
        self.gridLayout.addWidget(self.main_list, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Minecraft")
        font.setPointSize(-1)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"font-family: Minecraft;\n"
f"font-size: {25*MULT}px;\n"
"text-decoration: underline;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.my_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minecraft Objects"))
        self.object_id_label.setText(_translate("MainWindow", "Object id"))
        self.object_id_input.setPlaceholderText(_translate("MainWindow", "int"))
        self.nam_label.setText(_translate("MainWindow", "Name"))
        self.name_input.setPlaceholderText(_translate("MainWindow", "str"))
        self.stackable_label.setText(_translate("MainWindow", "Stackable"))
        self.stackable_input.setPlaceholderText(_translate("MainWindow", "int"))
        self.tool_label.setText(_translate("MainWindow", "Tool"))
        self.tool_input.setPlaceholderText(_translate("MainWindow", "str"))
        self.blast_resistance_label.setText(_translate("MainWindow", "Blast resistance"))
        self.blast_resistance_input.setPlaceholderText(_translate("MainWindow", "int or float"))
        self.flammable_label.setText(_translate("MainWindow", "Flammable"))
        self.flammable_input.setPlaceholderText(_translate("MainWindow", "true or false"))
        self.rarity_label.setText(_translate("MainWindow", "Rarity"))
        self.rarity_input.setPlaceholderText(_translate("MainWindow", "str"))
        self.restore_label.setText(_translate("MainWindow", "Restores"))
        self.restore_input.setPlaceholderText(_translate("MainWindow", "int or float"))
        self.durability_label.setText(_translate("MainWindow", "Durability"))
        self.durability_input.setPlaceholderText(_translate("MainWindow", "int"))
        self.damage_label.setText(_translate("MainWindow", "Damage"))
        self.damage_input.setPlaceholderText(_translate("MainWindow", "int or float"))
        self.effect_label.setText(_translate("MainWindow", "Effect"))
        self.effect_input.setPlaceholderText(_translate("MainWindow", "true or false"))
        self.renewable_label.setText(_translate("MainWindow", "Renewable"))
        self.renewable_input.setPlaceholderText(_translate("MainWindow", "true or false"))
        self.add_button.setText(_translate("MainWindow", "Add Object"))
        self.delete_button.setText(_translate("MainWindow", "Delete Object"))
        self.clear_button.setText(_translate("MainWindow", "Clear Data"))
        self.label.setText(_translate("MainWindow", "Minecraft Objects"))

    def my_functions(self):
        self.add_button.clicked.connect(lambda:self.add_item_list())
        self.delete_button.clicked.connect(lambda:self.delete_item_list())
        self.clear_button.clicked.connect(lambda:self.clear_lineedit())

    def add_item_list(self):
        entered_res = self.read_props()
        start_obj_prop = [entered_res['object_id'], entered_res['name'], entered_res['stackable']]
        array_of_exception = {
            'Mine_Object':['blast_resistance', 'damage', 'durability', 'effect', 'flammable', 'rarity', 'renewable', 'restore', 'tool'],
            'Armor':['blast_resistance', 'damage', 'effect', 'flammable', 'renewable', 'restore', 'tool'],
            'Block':['damage', 'durability', 'effect', 'rarity', 'renewable', 'restore'],
            'Food':['blast_resistance', 'damage', 'durability', 'effect', 'flammable', 'rarity', 'tool'],
            'Potion':['blast_resistance', 'damage', 'durability', 'flammable', 'renewable', 'restore', 'tool'],
            'Tool':['blast_resistance', 'effect', 'flammable', 'renewable', 'restore', 'tool'],
            'All_prop':['blast_resistance', 'damage', 'durability', 'effect', 'flammable', 'name', 'object_id', 'rarity', 'renewable', 'restore', 'stackable', 'tool']
        }

        if all(entered_res[key] for key in ['object_id', 'name', 'stackable']) and all(entered_res[key] == None for key in array_of_exception['Mine_Object']):
            temp = Mine_Object(*start_obj_prop)

        elif all(entered_res[key] for key in ['durability', 'rarity']) and all(entered_res[key] == None for key in array_of_exception['Armor']):
            temp = Armor(*start_obj_prop, entered_res['rarity'], entered_res['durability'])

        elif all(entered_res[key] for key in ['blast_resistance', 'flammable', 'tool']) and all(entered_res[key] == None for key in array_of_exception['Block']):
            temp = Block(*start_obj_prop,  entered_res['tool'], entered_res['blast_resistance'], entered_res['flammable'])

        elif all(entered_res[key] for key in ['renewable', 'restore']) and all(entered_res[key] == None for key in array_of_exception['Food']):
            temp = Food(*start_obj_prop, entered_res['renewable'], entered_res['restore'])

        elif all(entered_res[key] for key in ['effect', 'rarity']) and all(entered_res[key] == None for key in array_of_exception['Potion']):
            temp = Potion(*start_obj_prop, entered_res['rarity'], entered_res['effect'])

        elif all(entered_res[key] for key in ['damage', 'durability', 'rarity']) and all(entered_res[key] == None for key in array_of_exception['Tool']):
            temp = Tool(*start_obj_prop, entered_res['rarity'], entered_res['durability'], entered_res['damage'])

        else:
            temp = All_Props(**entered_res)
        
        icon = temp.path_to_icon
        self.main_list.setIconSize(QtCore.QSize(60,60))
        item = QtWidgets.QListWidgetItem(QtGui.QIcon(icon),str(temp))
        self.main_list.addItem(item)

    def delete_item_list(self):
        selected = self.main_list.selectedItems()
        for item in selected:
            row = self.main_list.row(item)
            self.main_list.takeItem(row)

    def clear_lineedit(self):
        for widget in self.__dict__.values():
            if isinstance(widget, QtWidgets.QLineEdit):
                widget.clear()

    def read_props(self) -> dict:
        entered_res = {}
        entered_res['object_id'] = int(self.object_id_input.text()) if self.object_id_input.text() else None
        entered_res['name'] = str(self.name_input.text()) if self.name_input.text() else None
        entered_res['stackable'] = int(self.stackable_input.text()) if self.stackable_input.text() else None
        entered_res['tool'] = str(self.tool_input.text()) if self.tool_input.text() else None
        entered_res['blast_resistance'] = float(self.blast_resistance_input.text()) if self.blast_resistance_input.text() else None
        entered_res['flammable'] = self.supply_read_props(self.flammable_input.text())
        entered_res['rarity'] = str(self.rarity_input.text()) if self.rarity_input.text() else None
        entered_res['restore'] = float(self.restore_input.text()) if self.restore_input.text() else None
        entered_res['durability'] = int(self.durability_input.text()) if self.durability_input.text() else None
        entered_res['damage'] = float(self.damage_input.text()) if self.damage_input.text() else None
        entered_res['effect'] = self.supply_read_props(self.effect_input.text())
        entered_res['renewable'] = self.supply_read_props(self.renewable_input.text())
        return entered_res
    
    def supply_read_props(self, line_dif:str):
        line_dif = line_dif.lower().strip()
        if line_dif == '':
            return None
        elif line_dif in ['0','false']:
            return 'False'
        else:
            return 'True'

if __name__ == "__main__":
    import sys
    from Types_Obj import Mine_Object,Armor,Block,Food,Potion,Tool,All_Props
    from PyQt5 import QtCore, QtWidgets, QtGui
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())