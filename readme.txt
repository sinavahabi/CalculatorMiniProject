Calculator Application

Features: OOP, PyQt, Error handling

Languages: Python, CSS

Note: Program can be run from either "main.py" of "app.py" module.

"main.py" module is just a simple calculator program which uses eval() method for performing mathematical operations. This program is also very exact, specific and continuous. user can keep up performing mathematical operations and entering invalid input such as strings won't crash the program because of regex.

"app.py" module however, is an actual application. This program has been written by using PyQt5 library after qt installation in system. Application stylesheet is written by style.css file. This app includes a quit message that program will ask the user when they want to quit the program.
Also program input only accepts numbers (float or integer), and user can't enter anything but numbers on keyboard or buttons on main app window. Even if user tries to square root a negative number in calculator, program won't crash, and it only shows an invalid input message.
After that, previous results of app will be removed and user can keep going on performing mathematical operations.

Note: Codes documentation and description is more obvious in comments among the codes on each file.