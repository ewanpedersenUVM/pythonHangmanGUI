import tkinter as tk
import pip

try:
    import tinytag as tt
except ImportError:
    pip.main(['install', 'tinytag'])
    import tinytag as tt

def my_function():
    print("Hello World")
    pass

