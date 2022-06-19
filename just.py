from kivymd.app import MDApp
from kivy.lang import Builder
import sqlite3
import requests 
from covid import *
import re

#"""""""""""""""""covid files""""""""""""""""""""""""""
covid = Covid()
sty = str(covid)
cleaned  = re.findall(r'\d+', sty) 
print(cleaned)


#""""""""""""""""""""""""""""""""""""""""""
#data base files ''''''''''''''''
con = sqlite3.connect('cat.db')
c = con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS shirt
	(theme text)''')
c.execute('''INSERT INTO shirt VALUES ('Dark')''')	
#''''''''''''''''''''''''''''''''''''''''''''''''''''''

class java(MDApp):
	try:
		requests.get('https://google.com',timeout=2)
		image = 'tr.png'
		test = ''
		cases = 'Ethiopian cases'
		total = 'Total ethiopian cases'
	except:
		image = 'no.png'
		test = ''	
		

	covid = Covid()
	man = covid.get_status_by_country_name('Ethiopia')
	var = str(man)
	kalk = var.replace("{'id': '60',",'')
	tat = kalk.replace(", 'latitude': 9.145, 'longitude': 40.4897",'')
	lolo = tat.replace("'recovered': None, 'last_update': 1633429279000}",'')
	easy = lolo.replace("'country': 'Ethiopia', ",'')
	sos = easy.replace(", 'active': None, 'deaths': 5765,",'')
	last = sos.replace("'confirmed': ",'')

	comon = Covid()
	man = comon.get_status_by_country_name('Ethiopia')
	sata = str(man)
	kalk = sata.replace("{'id': '60', 'country': 'Ethiopia', 'confirmed': 349231, 'active': None, '",'')
	tata = kalk.replace(", 'recovered': None, 'latitude': 9.145, 'longitude': 40.4897, 'last_update': 1633429279000}",'')
	vava = tata.replace("deaths': ",'')
	print(man)











	def mango(self,instace):
		icon = instace.icon
		if icon == 'brightness-7':
			self.theme_cls.theme_style = "Light"
			mode = 'light'
			c.execute('UPDATE shirt SET theme ="Light" ')
			con.commit()
		if icon == 'brightness-4':
			self.theme_cls.theme_style = "Dark"
			mode = 'Dark'
			c.execute('UPDATE shirt SET theme ="Dark" ')
			con.commit()			
	

	def build(self):
		self.root.ids.var.source = ''
		c.execute('SELECT theme FROM shirt')
		man = c.fetchone()
		sawo = str(man)
		fi = sawo.replace('(','')
		tw = fi.replace(')','')
		self.theme_cls.primary_palette = 'Teal'
		thr = tw.replace(',','')
		quote = thr.replace("'","")

		self.theme_cls.theme_style = quote
		return Builder.load_file('java.kv')
		con.commit()
		
java().run()


