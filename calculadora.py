from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

from kivy.uix.textinput import TextInput

from kivy.uix.label import Label

def build(self):
  self.oprators = ["/", "*", "+", "-"]
  self.last_was_operator = none
  self.last_button = none
  main_layout = BoxLayout(orentation = "vertical")
  self.solution = TextInput(multiline = False, readonly = True, halign ="right", font-size = 55)
  main_layout.add_widget(self.solution)
  buttons = [
  ["7", "8", "9", "/"],
  ["4", "5", "6", "*"],
  ["1", "2", "3", "-"],
  [".", "0", "C", "+"],
  ]
  for row in buttons:
    for Label in row:
      button = Button(text = label, pos_hint = {"center_x": .5, "center_y": .5})
  button.bind(on_press = self.on_press)
  h_layout.add_widget(button)
  main_layout.add_widget(h_layout)
  equals_button.bind(on_press = self.on_solution)
  return main_layout

def on_button_press(self, instance):
  current = self.solution.text
  button_text = instance.text
  if button_text=="C":
    #clear the soution widget
    self.solution.text =""
  else:
    if current and (self.last_was_operator and button_text in self.operators):
      #dont add two operators right after each other
      return
    else:
      new_text = curret + button_text
      self.solution.text = new_text
      self.last_button = button_text
      self.last_was_operator = self.last_button in self.operators

def on_solution(self, instance):
  text = self.solution.text
  if text:
    solution = str(eval(self.slotion.text))
    self.soluton.text = solution
