from Extract_refactor.settings import IMAGENES_PATH
from .web_info import WebInfo

import unicodecsv as csv

class Manager(WebInfo):

	def __init__(self, ruta_entrada):
		#self.resultados = {'status': 200, 'alexa': u'\n\n4,484,464              ', 'language': u'es-es', 'url': 'http://todosaintseiya.com', 'platform': ['prestashop'], 'mail': u'.todosaintseiya@hotmail.com.TODOSAINTSEIYA@HOTMAIL.COM'}
		self.urls_list = []
		self.writer = ''
		self.ruta_entrada = ruta_entrada
	def open_book_writer(self):	
		f = open('salida/' + self.ruta_entrada, 'wb')
		self.writer = csv.writer(f, lineterminator='\n', encoding='utf-8')
		self.writer.writerow(('url','alexa', 'status', 'platform', 'language', 'mail'))


	def open_book_append(self):
		f = open('salida/' + self.ruta_entrada, 'ab')
		self.writer = csv.writer(f, lineterminator='\n', encoding='utf-8')		
	

	def export(self):
			
		self.writer.writerow((self.resultados['url'], self.resultados['alexa'], self.resultados['status'], self.resultados['platform'], self.resultados['language'], self.resultados['mail']))
			
	  


	def imports(self):

		with open('media/' + self.ruta_entrada, 'rb') as f:
			reader = csv.reader(f, encoding='utf-8')
			for row in reader:
				
				self.urls_list.append(row)
			print (self.urls_list)

			
			
#manager = Manager()
#manager.imports()

