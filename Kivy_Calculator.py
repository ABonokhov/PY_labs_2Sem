"""
Доработать калькулятор:
1) сделать историю вычислений
2) сделать проверку первого ноля (чтобы не было вроде 02 числа)
3) сделать невозможность деления на 0
4) после очисткив поле ввода остается 0, но после начала ввода он исчезает
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import re

class MainApp(App):
    clear = "C"
    dot = "."
    operators = ["/", "*", "+", "-"]

    def build(self):
        self.current_text = ""

        main_layout = BoxLayout(orientation="vertical")
        self.history = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.history)
        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        main_layout.add_widget(self.solution)
        self.print_to_text_bar(self.solution, "")

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [MainApp.dot, "0", MainApp.clear, "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                if label in [str(i) for i in range(10)]:
                    button.bind(on_press=self.on_number_button_press)
                elif label == MainApp.dot:
                    button.bind(on_press=self.on_dot_button_press)
                elif label == MainApp.clear:
                    button.bind(on_press=self.on_clear_button_press)
                elif label in MainApp.operators:
                    button.bind(on_press=self.on_operator_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_operator_button_press(self, instance):
        button_text = instance.text
        last_button = self.get_last_button()
        last_was_operator = self.is_last_operator()

        if last_was_operator:
            return
        elif self.current_text == "":
            return
        elif self.current_text == "." and button_text == ".":
            return
        elif last_button == MainApp.dot:
            return

        self.add_to_text_bar(self.solution, button_text)

    def on_number_button_press(self, instance):
        button_text = instance.text

        if self.get_current_number() == "0":
            return

        self.add_to_text_bar(self.solution, button_text)

    def on_dot_button_press(self, instance):
        button_text = instance.text

        if self.is_has_dot():
            return
        if self.get_current_number() == "":
            return

        self.add_to_text_bar(self.solution, button_text)

    def on_clear_button_press(self, instance):
        self.print_to_text_bar(self.solution, "")

    def print_to_text_bar(self, text_bar, text):
        self.current_text = text

        if text:
            text_bar.text = text
        else:
            text_bar.text = "0"

    def get_current_number(self):
        search = re.search(r'[\d\.]+$', str(self.current_text))
        if search:
            return search.group()
        else:
            return ""

    def add_to_text_bar(self, text_bar, text):
        self.current_text += text
        self.print_to_text_bar(self.solution, self.current_text)

    def get_last_button(self):
        if len(str(self.current_text)) == 0:
            return ""
        return str(self.current_text)[-1]

    def is_last_operator(self):
        return self.get_last_button() in MainApp.operators

    def is_has_dot(self):
        return MainApp.dot in self.get_current_number()

    def on_solution(self, instance):
        try:
            last_was_operator = self.is_last_operator()

            if last_was_operator:
                return
            text = self.solution.text
            if text == "0":
                solution = 0
                self.history.text = self.solution.text
                self.print_to_text_bar(self.solution, solution)
            elif text:
                solution = str(eval(self.current_text))
                self.history.text = self.solution.text
                self.print_to_text_bar(self.solution, solution)
        except ZeroDivisionError:                               # Исключение, возникающее при попытке деления на нуль
            self.print_to_text_bar(self.solution, "Error")



if __name__ == "__main__":
    app = MainApp()
    app.run()