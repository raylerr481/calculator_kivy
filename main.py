from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CalcLayout(BoxLayout):
    def press_button(self, label):
        if label == "C":
            self.ids.input.text = ""
            return
        
        if label == "=":
            try:
                expr = self.ids.input.text
                result = eval(expr)
                self.ids.input.text = str(result)
            except:
                self.ids.input.text = "Error"
            return

        self.ids.input.text += label

class CalculatorApp(App):
    def build(self):
        return CalcLayout()

if __name__ == "__main__":
    CalculatorApp().run()
