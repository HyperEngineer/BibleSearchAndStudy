
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Learning Python with Tkinter')
root.iconbitmap('C:/Users/Hyper/Documents/Images/KrisIcon.ico')
root.geometry('400x200')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('Hi,', name)
    print('Hi, %s' %name)

    import PopulateIt as populate
    pop_it = populate.PopulateIt()

    msg = pop_it.populate_versions()
    print(msg)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
