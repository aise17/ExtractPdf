from bs4 import BeautifulSoup
import requests
from .web_info_target import WebInfoTarget

class Status(WebInfoTarget):
	''' information of web status  '''
	def __init__(self, site_url ):
		super(Status,self).__init__()
		self.site_url = site_url
		self.resource_url = self.get_resource_url().strip(' ')

		self.response = requests.get(
			self.resource_url,
			allow_redirects=True,
			timeout=10,
			verify=True,
			stream=True
		)
		self.result_status = self.get_result()

	def get_resource_url(self):
		'''
		in  this fuction, become the url without protocol in a url with protocol 

		Args :
			site_url(string): pure url without protocol
			resource_url(string) is a build url with ethernet protocol  
		'''
		if (self.site_url[:7]) == 'http://':

			print('URL corecta')    
			return self.site_url                    # comprobamos que las primeras letras de la url del 0 - 7 sea igual a " 'http:// "

		else:
			print (' URL corregida')
			self.resource_url = ('http://'+ self.site_url)

			return self.resource_url


	def get_result(self):
		'''
		this fuction , show to status code of the get web 

		Args:
			status(int): this variable stores the state of the web
		'''
		return self.response.status_code









'''

status = Status('google.es')
print status.resource_url

print status.result_status

'''