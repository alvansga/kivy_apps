from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock

class GameWidget(Widget):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		
		self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
		self._keyboard.bind(on_key_down = self._on_key_down)
		self._keyboard.bind(on_key_up = self._on_key_up)
		
		with self.canvas:
			self.player = Rectangle(source="player2.png",pos=(0,0),size=(100,100))
			
		self.keysPressed = set()
		
		Clock.schedule_interval(self.move_step,0)
		
	def _on_keyboard_closed(self):
		self._keyboard.unbind(on_key_down = self._on_key_down)
		self._keyboard.unbind(on_key_up = self._on_key_up)
		self._keyboard = None
		
	def _on_key_down(self, keyboard, keycode, text, modifiers):
		# print("key down:",text)
		self.keysPressed.add(text)
		
	def _on_key_up(self,keyboard,keycode):
		text = keycode[1]
		if text in self.keysPressed:
			self.keysPressed.remove(text)
			
	def move_step(self,dt):
		
		cur_x = self.player.pos[0]
		cur_y = self.player.pos[1]
		
		step_size = 500 * dt
		
		if "w" in self.keysPressed:
			cur_y += step_size
		if "s" in self.keysPressed:
			cur_y -= step_size
			
		if "a" in self.keysPressed:
			cur_x -= step_size
		if "d" in self.keysPressed:
			cur_x += step_size
			
		new_x = cur_x
		new_y = cur_y
		self.player.pos = (new_x,new_y)
		
		
class MyApp(App):
	def build(self):
		return GameWidget()
			
if __name__ == "__main__":
	app = MyApp()
	app.run()
