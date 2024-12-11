from kivy.app import App

from kivy.uix.button import Button

class MainApp(App):
  def build(self):
button = Button(text = "Fala garela!", size_hint = (.5, 5), pos_hint = {"center_X": .5, "center_y": .5})
button.bind(on_press = self.on_press_button)
return button

def on_press_button(self, instance):
print("você apertou o botão!")

if __name__ == "__main__":
  app = MainApp(App)
  app.run()
