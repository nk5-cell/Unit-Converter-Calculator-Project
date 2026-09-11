import tkinter as tk
import tkinter.ttk as ttk

from AboutApp import AboutApp
from GramsToOuncesApp import GramsToOuncesApp
from OuncesToGramsApp import OuncesToGramsApp

class MainApp:
    def __init__(self, master):

        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)

        # build ui
        self.__main_notebook = ttk.Notebook(master)
        self.__main_notebook.grid(column='0', row='0', sticky='nsew')
        self.__main_notebook.rowconfigure('0', weight='1')
        self.__main_notebook.columnconfigure('0', weight='1')

        # Main widget
        self.__mainwindow = self.__main_notebook

        # Add About... tab
        about_app = AboutApp(self.__mainwindow)
        self.__main_notebook.add(about_app.get_top_frame(), text="About...")

        # Add first calculator
        grams_to_ounces_app = GramsToOuncesApp(self.__mainwindow)
        self.__main_notebook.add(grams_to_ounces_app.get_top_frame(), text="Grams to Ounces")

        ounces_to_grams_app = OuncesToGramsApp(self.__mainwindow)
        self.__main_notebook.add(ounces_to_grams_app.get_top_frame(), text="Ounces to Grams")

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Nidhi's Calculator Project")
    root.geometry("400x400")
    app = MainApp(root)
    app.run()
