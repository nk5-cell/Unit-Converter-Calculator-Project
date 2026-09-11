import os
import pygubu
import tkinter as tk
import tkinter.messagebox as mb

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "ounces_to_grams.ui")

class OuncesToGramsApp:
    GRAMS_PER_OUNCE = 28.3495

    def __init__(self, master):

        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)

        self.__mainwindow = builder.get_object('ounces_to_grams_top_frame', master)
        self.__ounces_entry = builder.get_object('ounces_entry', master)
        self.__grams_entry_variable = builder.get_variable('grams_entry_variable')

        builder.connect_callbacks(self)

    def calculate(self):

        try:
            ounces = float(self.__ounces_entry.get())
            grams = ounces * self.GRAMS_PER_OUNCE
            self.__grams_entry_variable.set("{:.2f} grams".format(grams))
        except ValueError:
            mb.showerror(title="Input Error", message="Please enter a valid number for ounces.")

    def get_top_frame(self):
        return self.__mainwindow

    def run(self):
        self.__mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Test Ounces to Grams")
    app = OuncesToGramsApp(root)
    app.run()

