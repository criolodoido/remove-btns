#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
from kivy.app import App
from kivy.app import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.core.window import Window;

#terminar isso aqui
class PrimeiroScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'um'
		super(Screen,self).__init__(**kwargs)
	
	def add(self,i):
		screen2 = self.manager.get_screen('dois')		
		screen2.btn = Button(text= "Btn",size_hint=(1,None))
		screen2.btn.bind(on_press=self.remova)
		screen2.ids.grade3.add_widget(screen2.btn)
		
		
	def remova(self,i):
		screen2 = self.manager.get_screen('dois')
		screen2.ids.grade3.remove_widget(i)#ta funcionando poorra
				
class SegundoScreen(Screen):
	def __init__(self, **kwargs):
		self.name = 'dois'
		super(Screen,self).__init__(**kwargs)
	
	
class RootScreen(ScreenManager):
    pass
    
class btnApp(App):
	title = 'Gerador de btns!'
	def on_pause(self):
		return True
		
	def on_resume(self):
	   
	   pass
      
	def build(self):
		return RootScreen()
if __name__ == '__main__':
    appVar = btnApp()
    btnApp().run()
