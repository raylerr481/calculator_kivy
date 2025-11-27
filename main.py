from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Calculator(BoxLayout):
    def calculate(self, expression):
        try:
            self.ids.result.text = str(eval(expression))
        except:
            self.ids.result.text = "Error"

class CalcApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalcApp().run()
