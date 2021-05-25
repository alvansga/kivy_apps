import kivy 
kivy.require('2.0.0')

from kivmob import KivMob, TestIds

from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput 

class LoginScreen(GridLayout):
    def __init__(self,**kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols = 2
        # self.add_widget(Label(text="username"))
        # self.username = TextInput(multiline=False)
        # self.add_widget(self.username)
        # self.add_widget(Label(text="password"))
        # self.password = TextInput(password=True, multiline=False)
        # self.add_widget(self.password)


class LoginApp(App):
    def build(self):
        # self.ads = KivMob(TestIds.APP)
        # self.ads.new_banner(TestIds.BANNER, top_pos=True)
        # self.ads.request_banner()
        # self.ads.show_banner()

        return LoginScreen()
        # return Label(text='Banner Ad Demo')

if __name__ == '__main__':
    LoginApp().run()