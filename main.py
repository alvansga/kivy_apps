from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window

class GameWidget(Widget):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
		self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
		self._keyboard.bind(on_key_down = self._on_key_down)
		
		with self.canvas:
			self.player = Rectangle(source="player2.png",pos=(0,0),size=(100,100))
			
	def _on_keyboard_closed(self):
		self._keyboard.unbind(on_key_down = self._on_key_down)
		self._keyboard = None
		
	def _on_key_down(self, keyboard, keycode, text, modifiers):
		print("key down:",text)
		
		cur_x = self.player.pos[0]
		cur_y = self.player.pos[1]
		
		if text == "w":
			cur_y += 5
		if text == "s":
			cur_y -= 5
			
		if text == "a":
			cur_x -= 5
		if text == "d":
			cur_x += 5
			
		new_x = cur_x
		new_y = cur_y
		self.player.pos = (new_x,new_y)
		
class MyApp(App):
	def build(self):
		return GameWidget()
			
if __name__ == "__main__":
	app = MyApp()
	app.run()
