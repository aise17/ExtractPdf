from .web_info import WebInfo
from .web_info_target import WebInfoTarget


from .alexa_rank import AlexaRank
from .platform_analyzer import Analyzer
from .search_contact import SearchContact
from .search_language import SearchLanguage
from .status import Status
from .manager import Manager


def main(ruta_entrada):
	salida = list()
	manager = Manager(ruta_entrada='exampleURL.csv')
	manager.imports()
	count = 1
	if count >= 5:
		manager.open_book_writer()
	else:
		manager.open_book_append()
	
	for urls in manager.urls_list:
		for url in urls:
			print (count)
			count += 1
			manager.resultados = {'url': '','alexa': '', 'status': '', 'platform': '', 'language': '', 'mail': ['']}


		#ALEXA RANK
			alexa_rank = AlexaRank(url)
			print (alexa_rank.url_alexa)
			print (alexa_rank.result_alexa)
			manager.resultados['alexa'] = alexa_rank.result_alexa

			print (manager.resultados)

		
		#STATUS
			try:
				status = Status(url)
				print (status.resource_url)
				print (status.result_status)
				manager.resultados['url'] = status.resource_url
				manager.resultados['status'] = status.result_status
		
				print (manager.resultados)

				if status.result_status == 200:

		#PLATFORM ANALYZER
					analizer = Analyzer(status.response)
					print (analizer.result_platform)
					manager.resultados['platform'] = analizer.result_platform

					print (manager.resultados)


			#SEARCH LANGUAGE USE IN THE WEB
					search_lang = SearchLanguage(status.response)
					print (search_lang.result_lang)
					try:
						manager.resultados['language'] = search_lang.result_lang
					except:	
						try:
							manager.resultados['language'] = search_lang.result_lang['lang'] 
						except KeyError:
							try:
								manager.resultados['language'] = search_lang.result_lang['xml:lang'] 
							except:
								manager.resultados['language'] = search_lang.result_lang
				
					print (manager.resultados)


			# SEARCH ITEMS OF CONTACT
					search_contact = SearchContact(status.response)
					print (search_contact.mail_result)
					for mail in search_contact.mail_result:
						if mail not in manager.resultados['mail']:
							manager.resultados['mail'].append(mail)
					join = ','
					manager.resultados['mail'] = join.join(manager.resultados['mail'])
					print (manager.resultados)
			except: 
				print ('Connection timed out #################################################')

			manager.export()
			manager.resultados
			salida.append((manager.resultados))
	return salida



if __name__ == '__main__':
	main()