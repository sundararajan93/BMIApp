import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file("BMI_design.kv")

class MyGridLayout(Widget):
    
    def calculate(self):
        bmi_weight = self.ids.bmi_weight.text
        h = self.ids.h.text

        try:
            BMI_VALUE = (int(bmi_weight) / (int(h)/100.0)**2)
            ANSWER = (round(BMI_VALUE,2))

            self.ids.bmi_weight.text = ""
            self.ids.h.text = ""
            self.ids.bmi.text = str(ANSWER)

            if ANSWER <= 18.4:
                self.ids.bmi.text = str(f"Underweight - {ANSWER}")
            elif ANSWER >= 18.5 and ANSWER <= 24.9:
                self.ids.bmi.text = str(f"Normal - {ANSWER}")
            elif ANSWER >= 25.0 and ANSWER <= 39.9:
                self.ids.bmi.text = str(f"Overweight - {ANSWER}")
            elif ANSWER >= 40.0:
                self.ids.bmi.text = str(f"Obese - {ANSWER}")
            else:
                self.ids.bmi.text = str(f"Something went wrong - {ANSWER}")
        except:
            if self.ids.bmi_weight.text == "" or self.ids.h.text == "":
                self.ids.bmi.text = str(f"All the fields are mandatory")
            else:
                self.ids.bmi.text = str(f"Something went wrong")

class BMIApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    bmi_app = BMIApp()
    bmi_app.run()