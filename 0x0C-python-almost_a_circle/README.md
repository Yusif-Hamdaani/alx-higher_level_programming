This is about 0C. Python - Almost a circle

Learning Objectives
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function


0x0C-python-almost_a_circle
models/
base.py
This file contains a class Base. It is the 'base' of all other classes in this project. Main goal is to manage id attribute to avoid code duplication.

rectangle.py
Contains the rectangle class that implements the base class.

square.py
This file contains the a class Square that implements the class Rectangle.

init.py
This makes the folder a python module.

tests/
This folder contains the test files and folders of this project.

test_models/
Test folder contains unittests for the model folder.

test_base.py
Test case for base.py.

test_rectangle.py
Test case for rectangle.py.

test_square.py
Test case for square.py.

Resources
args/kwargs
JSON encoder and decoder
unittest module
Python test cheatsheet
