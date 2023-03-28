"""
    Program: Calculator Application
    Author: sina vahabi
    Copyright: 2023/03
"""

# Installing essential libraries and packages which can be run in your terminal, virtual env, etc.:
# Commands:
# pip install PyQt5

import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QDoubleValidator, QFont, QIcon


'''
    Instantiating 'Button' class set initial buttons, user input and 'text' variable in order to
    make them work with 'handle_input()' method.
'''


class Button:
    def __init__(self, text, results):
        self.push_button = QPushButton(str(text))
        self.text = text
        self.results = results
        self.push_button.clicked.connect(lambda: self.handle_input(self.text))
        self.input_error = ''

    '''
        Defining this method helps us to avoid program crashes if user wanted to perform square root 
        on negative numbers by showing and error message. After error happens, user can click on Ok button 
        and then every results before will be deleted like a normal calculator will do. 
    '''

    def invalid_input(self):
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setText('Invalid Input\n')
        message.setWindowTitle('Error')
        message.setWindowIcon(QIcon('Icons/Error.png'))
        message.setFont(QFont('Sitka Text', 10))
        message.setStandardButtons(QMessageBox.Ok)
        self.input_error = message.exec_()
        return self.input_error

    '''
    By defining this method we handle if-else statements for '=', 'AC', 'DEL' and '√' buttons.
    These buttons have different functionality, and we can't perform mathematical operations on them.
    so we use different blocks of codes for each one.
    '''
    def handle_input(self, value):
        if value == '=':
            eval_result = eval(self.results.text())
            self.results.setText(str(eval_result))

        elif value == 'AC':
            self.results.setText('')

        elif value == 'DEL':
            current_value = self.results.text()
            self.results.setText(current_value[:-1])

        elif value == '√':
            result_value = float(self.results.text())
            # Using 'invalid_input()' method for negative numbers which user want to perform square root on them.
            if result_value < 0:
                self.invalid_input()
                if self.input_error == QMessageBox.Ok:
                    self.results.setText('')
            else:
                self.results.setText(str(math.sqrt(result_value)))

        else:
            current_value = self.results.text()
            next_value = current_value + str(value)
            self.results.setText(next_value)
            '''
            So if none of above conditions were True we simply perform mathematical operations with other buttons
            with previous result, and we can continuously keep up operating mathematical calculations.
            '''


# Instantiating main window 'Application()' class by inheritance from 'QWidget' and setting primary values.
class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('Icons/Calculator.png'))
        self.setFixedSize(370, 185)
        self.create_app()

    def create_app(self):
        grid = QGridLayout()
        grid.setSpacing(0)
        grid.setContentsMargins(0, 0, 0, 0)
        results = QLineEdit()
        '''
        By using 'QDoubleValidator()' we make sure that user can only enter float numbers and program won't stop
        if user tries entering anything else such as characters, strings and etc.
        '''
        results.setValidator(QDoubleValidator())
        results.setFont(QFont('Lucida Console', 14))

        # Filling up main window space with buttons and user input via using for loop.
        buttons = [
            'AC', 'DEL', '√', '/',
            7, 8, 9, '*',
            4, 5, 6, '-',
            1, 2, 3, '+',
            0, '.', '='
                   ]
        '''
        Setting row = 1 and column = 0 for user input position. With this we can make sure that, when we are setting up
        the other buttons by using for loop, other buttons won't be set in user input position.
        '''
        row, col = 1, 0
        # Setting user input position in first row,first col, 1 row height, 4 col width.
        grid.addWidget(results, 0, 0, 1, 4)

        for button in buttons:
            if col > 3:
                col = 0
                row += 1

            button_object = Button(button, results)
            # In order to keep every thing precise and fit, we use the codes below for 0 button to take 2 columns width.
            if button == 0:
                grid.addWidget(button_object.push_button, row, col, 1, 2)
                col += 1
            else:
                grid.addWidget(button_object.push_button, row, col, 1, 1)

            col += 1

        self.setLayout(grid)
        self.show()

    '''
        Defining this method helps us to ask a question from user when they click on close button of the main window.
        By using 'QMessageBox()' we will give two options to user. They can either click on 'Yes' or 'No' button.
        If they click on 'Yes' button they will quit from the program and if they click on 'No' button,
        they can stay on program.
    '''

    def closeEvent(self, event):
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setText('Are you sure you want to quit?')
        message.setWindowTitle('Quit')
        message.setWindowIcon(QIcon('Icons/Quit.png'))
        message.setFont(QFont('Sitka Text', 10))
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return_value = message.exec_()
        if return_value == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()

    with open('style.css', 'r') as style:
        app.setStyleSheet(style.read())

    sys.exit(app.exec_())
