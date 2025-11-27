from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CalculatorLayout(BoxLayout):
    def calculate(self, operation):
        try:
            num1 = float(self.ids.num1.text)
            num2 = float(self.ids.num2.text)

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    self.ids.result.text = "ERROR"
                    return
                result = num1 / num2
            else:
                result = "ERROR"

            self.ids.result.text = str(result)

        except Exception:
            self.ids.result.text = "ERROR"


class CalculatorApp(App):
    pass


if __name__ == "__main__":
    CalculatorApp().run()
