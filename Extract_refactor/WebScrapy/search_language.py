from .web_info_target import WebInfoTarget
from bs4 import BeautifulSoup


class SearchLanguage(WebInfoTarget):
	def __init__(self, response):
		super(SearchLanguage,self).__init__()
		self.result_lang = self.get_result(response)


	def get_result(self, response):
		'''
		scraping a web for extraction a lang
		Args:
			soup(string): this variable contains the organized mark language
		'''
		
		soup = BeautifulSoup(response.text, "html.parser")
		for lang in soup.findAll('html'):
			result_lang = lang.attrs
			return result_lang['lang']
'''
search = SearchLanguage('comprarseguridad.es')

res = search.get_result()

print res'''