from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from .web_info import WebInfo
import requests

class AlexaRank(WebInfo):
	''' information of number of alexa ranck  '''
	def __init__(self, site_url):
		super(AlexaRank,self).__init__()
		self.site_url = site_url
		self.url_alexa = self.get_resource_url()
		self.result_alexa = self.get_result()
	def get_resource_url(self):
		'''
		allow build a url whit alexa rank search uri
		Args:
			baseUrl(string): contains alexa perfix for search 
			finalUrl(string): contains alexa suffix for search 
		'''
		baseUrl = 'http://www.alexa.com/siteinfo/'
		finalUrl = '#linksin'

		self.url_alexa = baseUrl + self.site_url + finalUrl
		return self.url_alexa

	def get_result(self):
		'''
		scraping a web for extraction a number of alexa rank
		Args:
			soup(string): this variable contains the organized mark language
			result_AlexaRank(int): in the alexaranking number
		'''
		response = requests.get(
			self.url_alexa,
			allow_redirects=True,
			timeout=10,
			verify=True,
			stream=True
		)
		soup = BeautifulSoup(response.text, "html.parser")

		for span in soup.find_all('div',{'class':'rankmini-global'}):  
			for strong in span.find_all('div', {'class': 'rankmini-rank'}):  

				result_AlexaRank = strong.text
				result_AlexaRank = result_AlexaRank.strip(' ')
				result_AlexaRank = result_AlexaRank.strip('\n')
				result_AlexaRank = result_AlexaRank.strip('\t')
				result_AlexaRank = result_AlexaRank.strip('#')
				return result_AlexaRank    





'''
alexa_rank = AlexaRank('analyzer.tk')

print(alexa_rank.url_alexa)

print(alexa_rank.result_alexa)

'''