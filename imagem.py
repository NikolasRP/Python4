from kivy.app import App

from kivy.uix.label import Image, AsyncImage

class MainApp(App):
  def build(self):
    img = AsyncImage(source="https://img.icons8.com/?size=100&id=NTLCh-Y0kOp9&format=png&color=000000", size_hint = (1, .5),pos_hint = {"center_x": 5, "center_y": .5})
    return img
    if __name == "__main__":
      app = MainApp(App)
      app.run()
