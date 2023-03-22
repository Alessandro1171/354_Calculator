from tkinter import *
import tkinter as tk

LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
SMALL_FONT_STYLE = ("Arial", 10)
LARGE_FONT_STYLE = ("Arial", 30, "bold")
DIGIT_FONT_STYLE = ("Arial", 20, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)
OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x650")
        self.window.resizable(0, 0)
        self.window.title("ETERNITY Calculator")

        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.digits = {
            7: (2, 1), 8: (2, 2), 9: (2, 3),
            4: (3, 1), 5: (3, 2), 6: (3, 3),
            1: (4, 1), 2: (4, 2), 3: (4, 3),
            ".": (5, 1), 0: (5, 2)
        }

        self.operations = {
            "\u00F7": (3, 4), "\u00D7": (3, 5),  # /, *
            "-": (4, 4), "+": (4, 5)
        }
        self.functions = {
            "F1": (1, 1), "F2": (1, 2), "F3": (1, 3), "F4": (1, 4), "F5": (1, 5),
            "F6": (2, 4), "F7": (2, 5), "=": (5, 3), "clr": (5, 4), "del": (5, 5)
        }
        self.buttons_frame = self.create_buttons_frame()
        self.create_digit_buttons()
        self.create_operators_buttons()
        self.create_functions_buttons()
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
                               bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                         bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=220, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR,
                               font=DIGIT_FONT_STYLE, borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operators_buttons(self):
        for operator, grid_value in self.operations.items():
            button = tk.Button(self.buttons_frame, text=str(operator), bg=OFF_WHITE, fg=LABEL_COLOR,
                               font=DEFAULT_FONT_STYLE, borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_functions_buttons(self):
        for function, grid_value in self.functions.items():
            button = tk.Button(self.buttons_frame, text=str(function), bg=OFF_WHITE, fg=LABEL_COLOR,
                               font=DEFAULT_FONT_STYLE, borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
#
# root = Tk()  # creates main window
# root.title("ETERNITY CALCULATOR")
#
# entry = Entry(root, width=50, borderwidth=5, relief=FLAT, fg="Black", bg="White")
# entry.grid(row=0, column=0, columnspan=5, padx=10, pady=15)  # pushes into window
#
#
# def click(new_value):
#     old_value = entry.get()  # take everything in entry bar
#     entry.delete(0, END)  # clears everything in entry bar
#     entry.insert(0, old_value + new_value)  # new value appended to old value
#     return
#
#
# def clear():
#     entry.delete(0, END)
#     return
#
#
# def backspace():
#     current = entry.get()
#     length = len(current) - 1
#     entry.delete(length, END)
#
#
# def evaluate():
#     total = entry.get()
#     answer = eval(total) # check what eval actually does
#     entry.delete(0, END)  # maybe move this value to history?
#     entry.insert(0, answer)
#
#
# function1 = Button(root, text="f1", padx=25, pady=10, relief=FLAT, bg="White")
# function1.bind('<Button-1>')
# function1.grid(row=1, column=0)
#
# function2 = Button(root, text="f2", padx=25, pady=10, relief=FLAT, bg="#d5d5d5")
# function2.grid(row=1, column=1)
#
# function3 = Button(root, text="f3", padx=25, pady=10, relief=FLAT, bg="White")
# function3.grid(row=1, column=2)
#
# function4 = Button(root, text="f4", padx=25, pady=10, relief=FLAT, bg="#e9e9e9")
# function4.grid(row=1, column=3)
#
# function5 = Button(root, text="f5", padx=25, pady=10, relief=FLAT, bg="White")
# function5.grid(row=1, column=4)
#
# root.resizable(False, False)  # cannot resize window
# root.mainloop()  # runs window continuously unless u exit
