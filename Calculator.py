import tkinter as tk
from StandardDeviation import standard_deviation
from ExponentialFunction import exponential_function
from Arccos import arccos
from Log import log
from GammaFunction import gamma
from HyperSineFunction import exponential_function2
from HelperFunctions import truncate_value

LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
SMALL_FONT_STYLE = ("Arial", 10)
LARGE_FONT_STYLE = ("Arial", 18, "bold")
DIGIT_FONT_STYLE = ("Arial", 20, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)
SPECIAL_FUNCTION_FONT_STYLE = ("Arial", 17)
OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"

FORMAT_ERROR_MESSAGE = "Wrong format entered"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("316x450")
        self.window.resizable(0, 0)
        self.window.title("ETERNITY Calculator")

        self.total_expression = ""  # small display
        self.current_expression = ""  # big display
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.digits = {
            7: (2, 1), 8: (2, 2), 9: (2, 3),
            4: (3, 1), 5: (3, 2), 6: (3, 3),
            1: (4, 1), 2: (4, 2), 3: (4, 3),
            ".": (5, 1), 0: (5, 2)
        }

        self.operations = {
            "/": (4, 4), "*": (4, 5), "+": (5, 5)
        }

        self.buttons_frame = self.create_buttons_frame()
        self.create_buttons()

    def create_buttons(self):
        self.create_digit_buttons()
        self.create_operators_buttons()
        self.create_clear_button()
        self.create_delete_button()
        self.create_equals_button()
        self.create_comma_button()
        self.create_open_parenthesis()
        self.create_close_parenthesis()
        self.create_minus()
        self.create_standard_deviation_button()
        self.create_arccos_button()
        self.create_ab_power_x_button()
        self.create_x_power_y_button()
        self.create_log_button()
        self.create_gamma_button()
        self.create_hyperbolic_sine_button()

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

    # =========================== DIGITS ===========================
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR,
                               font=DIGIT_FONT_STYLE, borderwidth=0, command=lambda x=digit: self.add_to_expression(x),
                               width=3)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    # =========================== OPERATORS ===========================
    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operators_buttons(self):
        for operator, grid_value in self.operations.items():
            button = tk.Button(self.buttons_frame, text=str(operator), bg=OFF_WHITE, fg=LABEL_COLOR,
                               font=DEFAULT_FONT_STYLE, borderwidth=0,
                               command=lambda x=operator: self.append_operator(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def open_parenthesis(self):
        self.current_expression += "("
        self.update_label()

    def create_open_parenthesis(self):
        button = tk.Button(self.buttons_frame, text="(", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0,
                           command=self.open_parenthesis)
        button.grid(row=3, column=4, sticky=tk.NSEW)

    def close_parenthesis(self):
        self.current_expression += ")"
        self.update_label()

    def create_close_parenthesis(self):
        button = tk.Button(self.buttons_frame, text=")", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0,
                           command=self.close_parenthesis)
        button.grid(row=3, column=5, sticky=tk.NSEW)

    def minus(self):
        self.current_expression += "-"
        self.update_label()

    def create_minus(self):
        button = tk.Button(self.buttons_frame, text="-", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0,
                           command=self.minus)
        button.grid(row=5, column=4, sticky=tk.NSEW)

    # =========================== FUNCTIONS ===========================

    def ab_power_x_button_click(self):
        try:
            chunks = self.current_expression.split(",")
            a = float(chunks[0])
            b = float(chunks[1])
            x = float(chunks[2])
            total = exponential_function(b, x)
            final_total = truncate_value(a * total)
            self.current_expression = str(final_total)
        except Exception as e:
            self.current_expression = FORMAT_ERROR_MESSAGE
        finally:
            self.update_label()

    def x_power_y_button_click(self):
        try:
            chunks = self.current_expression.split(",")

            base = float(chunks[0])
            exponent = float(chunks[1])

            computed_value = exponential_function(base, exponent)

            self.current_expression = str(computed_value)
        except Exception as e:
            self.current_expression = FORMAT_ERROR_MESSAGE
        finally:
            self.update_label()

    def log_button_click(self):
        try:
            chunks = self.current_expression.split(",")

            x = float(chunks[0])
            base = float(chunks[1])

            computed_value = log(x, base)

            self.current_expression = str(computed_value)
        except Exception as e:
            self.current_expression = FORMAT_ERROR_MESSAGE
        finally:
            self.update_label()

    def standard_deviation_button_click(self):
        try:
            chunks = self.current_expression.split(",")
            final_total = standard_deviation(chunks, True)
            self.current_expression = str(final_total)
        except Exception as e:
            self.current_expression = FORMAT_ERROR_MESSAGE
        finally:
            self.update_label()

    def arc_cossine_button_click(self):
        try:
            result = float(self.current_expression)
            computed_value = arccos(result)
            self.current_expression = str(computed_value)
        except Exception as e:
            self.current_expression = FORMAT_ERROR_MESSAGE
        finally:
            self.update_label()

    def gamma_button_click(self):
        try:
            computed_value = gamma(float(self.current_expression))

            self.current_expression = str(computed_value)
        except Exception as e:
            self.current_expression = FORMAT_ERROR_MESSAGE
        finally:
            self.update_label()

    def hyperbolic_sine_button_click(self):
        try:
            x = float(self.current_expression)
            e_approx = 2.7182818284590452353602874713527
            numerator = exponential_function2(e_approx, x) - exponential_function2(e_approx, -x)
            denominator = 2
            final_total = truncate_value(numerator / denominator)
            self.current_expression = str(final_total)
        except Exception as e:
            self.current_expression = FORMAT_ERROR_MESSAGE
        finally:
            self.update_label()

    def create_arccos_button(self):
        button = tk.Button(self.buttons_frame, text="cos\u207B\u00B9", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=SPECIAL_FUNCTION_FONT_STYLE, borderwidth=0, command=self.arc_cossine_button_click)
        button.grid(row=2, column=5, sticky=tk.NSEW)

    def create_x_power_y_button(self):
        button = tk.Button(self.buttons_frame, text="x\u02b8", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=SPECIAL_FUNCTION_FONT_STYLE, borderwidth=0, command=self.x_power_y_button_click)
        button.grid(row=1, column=2, sticky=tk.NSEW)

    def create_log_button(self):
        button = tk.Button(self.buttons_frame, text="logb", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=SPECIAL_FUNCTION_FONT_STYLE, borderwidth=0, command=self.log_button_click)
        button.grid(row=1, column=5, sticky=tk.NSEW)

    def create_gamma_button(self):
        button = tk.Button(self.buttons_frame, text="Γ", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=SPECIAL_FUNCTION_FONT_STYLE, borderwidth=0, command=self.gamma_button_click)
        button.grid(row=1, column=3, sticky=tk.NSEW)

    def create_hyperbolic_sine_button(self):
        button = tk.Button(self.buttons_frame, text="sinh", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=SPECIAL_FUNCTION_FONT_STYLE, borderwidth=0, command=self.hyperbolic_sine_button_click)
        button.grid(row=1, column=4, sticky=tk.NSEW)

    def create_standard_deviation_button(self):
        button = tk.Button(self.buttons_frame, text="\u03C3", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=SPECIAL_FUNCTION_FONT_STYLE,
                           borderwidth=0, command=self.standard_deviation_button_click)
        button.grid(row=2, column=4, sticky=tk.NSEW)

    def create_ab_power_x_button(self):
        button = tk.Button(self.buttons_frame, text="ab\u02e3", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=SPECIAL_FUNCTION_FONT_STYLE, borderwidth=0, command=self.ab_power_x_button_click)
        button.grid(row=1, column=1, sticky=tk.NSEW)

    # =========================== CLEAR ===========================
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="clr", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.clear)
        button.grid(row=1, column=6, rowspan=2, sticky=tk.NSEW)

    # =========================== COMMA ===========================
    def comma(self):
        self.current_expression += ","
        self.update_label()

    def create_comma_button(self):
        button = tk.Button(self.buttons_frame, text=",", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.comma)
        button.grid(row=3, column=6, rowspan=1, sticky=tk.NSEW)

    # =========================== DELETE ===========================
    def delete(self):
        self.current_expression = self.current_expression[:-1]
        self.update_label()

    def create_delete_button(self):
        button = tk.Button(self.buttons_frame, text="del", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.delete)
        button.grid(row=4, column=6, rowspan=2, sticky=tk.NSEW)

    # =========================== EQUALS ===========================
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()

        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
            self.update_label()

        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=OFF_WHITE, fg=LABEL_COLOR,
                           font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.evaluate)
        button.grid(row=5, column=3, sticky=tk.NSEW)

    # ================================================================

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        for i in range(5):
            frame.rowconfigure(i, weight=1)
        for j in range(6):
            frame.columnconfigure(j, weight=1)  # set column width to be the same
        return frame

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
