from .web_info_target import WebInfoTarget
import re
from bs4 import BeautifulSoup
import requests

class SearchContact(WebInfoTarget):
	
	def __init__(self, response):
		super(SearchContact, self).__init__()
		self.mail_result = []
		self.result_contact = self.get_result(response)
	
	'''
	def get_result(self):
		self.get_mail()
		self.iter_site_web()
	'''	

	def iter_site_web(self):
		
		resource_url =  self.resource_url + '/content/'
		for i in range(10) :
			self.resource_url =  resource_url + '%d-' % (i)
			self.get_mail()
			print (self.resource_url)


	def get_result(self, response):
		
		
		query = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
		regex = re.compile(query)


		soup = BeautifulSoup(response.text, "html.parser")
		for s in soup.find_all('span'):
			s = s.text
			
			match = regex.search(s)
			if match: 
				return self.mail_result.append(match.group())
			
			
	def get_Phone(self):
		query = r"" 
		regex = re.compile(query, re.I)							
		phone = re.search(query, self.span)

		return phone


'''
search = SearchContact('disfraces.tienda')
search.get_result()

print search.resource_url
print search.mail_result'''