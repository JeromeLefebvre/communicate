
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from redis import Redis

class Form(BoxLayout):
	name = StringProperty()
	update = ObjectProperty()
	refresh = ObjectProperty()


class FormApp(App):

	def build(self):
		self.redis = Redis.from_url( "redis://redistogo:e53d9c9eee21af1cb977ac1c75e493e2@angelfish.redistogo.com:9536/")
		name = self.redis.get('name')
		self.form = Form(name=name, update=self.update, refresh=self.refresh)
		return self.form

	def refresh(self):
		name = self.redis.get('name')
		self.form.ids.textinput.text = name

	def update(self):
		name = self.form.ids.textinput.text
		self.form.name = name
		self.redis.set('name', name)

FormApp().run()