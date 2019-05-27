from six import iteritems
from bs4 import BeautifulSoup
import re
import requests
from .web_info_target import WebInfoTarget

USER_AGENT = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
APPS_DATA = {
	"magento": {
		"script": "/(js/mage|skin/frontend/(default|enterprise))/",
		"headers": {
			"set-cookie": "^(magento=[0-9a-f]+|frontend=[0-9a-z]+)"
		},
		"html": (
			"new VarienForm",
			"new Varien.searchForm"
		)
	},
	"oscommerce": {
		"headers": {"set-cookie": "cookie_test=please_accept_for_session;"},
		"html": (
			"<a[^>]*oscsid",
			"<a[^>]href=\"http://www.oscommerce.com[^>]+>OsCommerce"
		)
	},
	"prestashop": {
		"meta": {
			"generator": "prestashop",
			"keywords": "prestashop"
		},
		"html": (
			"powered by <a href=\\\"[^>]+prestashop",
			"themes/prestashop",
			"modules/blockcart/ajax-cart.js",
			"modules/blocksearch/blocksearch.css",
			"id=\"search_query_block\" name=\"search_query\""
		)
	},
	"shopify": {
		"html": "//cdn.shopify.com",
	},
	"shopware": {
		"meta": {
			"application-name": "shopware"
		},
		"html": (
			"<script[^>]src=\"/engine/Shopware/",
			"/web/cache/[\d]{10}_[\w]{32}.(js|css)"
		),
	},
	"woocommerce": {
		"meta": {"generator": "^woocommerce"},
		"html": (
			"<[^>]+(href|src)=[\"'][^>]*/wp-content/plugins/"
			"woocommerce[^>]*>",
			"var wc_add_to_cart_params = {"
		),
	},
	"opencart": {
		"html": "(Powered By <a href=\\\"[^>]+OpenCart|route = getURLVar\\(\\\"route)"
	}
}

def precompile_regex(apps):
	for app_name, app_data in iteritems(apps):
		new_app_data = {}
		for k, v in iteritems(app_data):
			if isinstance(v, dict):
				new_app_data[k + '_regex'] = {}
				for n, r in iteritems(v):
					new_app_data[k + '_regex'][n] = re.compile(r, re.I)
			else:
				new_app_data[k + '_regex'] = []
				if isinstance(v, str) or isinstance(v, str):
					v = [v]
				for r in v:
					new_app_data[k + '_regex'].append(re.compile(r, re.I))
		apps[app_name] = new_app_data
	return apps

APPS_DATA_COMPILED = precompile_regex(apps=APPS_DATA)


class Analyzer(WebInfoTarget):
	class InvalidContent(Exception):
		pass

	def __init__(self, response):
		self.apps = APPS_DATA_COMPILED.copy()
		super(Analyzer, self).__init__()
		self.result_platform = self.get_result(response)

	



	def get_result(self, response):
		detected_apps = []


		

		response.raise_for_status()

		content_type = response.headers['content-type'].lower()
		if 'text/html' not in content_type:
			response.close()
			raise Analyzer.InvalidContent(content_type)

		script_tags, meta_tags = self.parse_tags(response.text)

		for app_name, app_data in iteritems(self.apps):
			html_regex = app_data.get('html_regex')
			script_regex = app_data.get('script_regex')
			meta_regex = app_data.get('meta_regex')
			headers = app_data.get('headers')
			if html_regex and self.find_html(response.text, html_regex):
				detected_apps.append(app_name)
				break
			if script_regex and self.find_script(script_tags, script_regex):
				detected_apps.append(app_name)
				break
			if meta_regex and self.find_meta(meta_tags, meta_regex):
				detected_apps.append(app_name)
				break
			if headers and self.find_headers(response.headers, headers):
				detected_apps.append(app_name)
				break

		if detected_apps:
			return detected_apps[0]
		else:
			""

	@staticmethod
	def parse_tags(html):
		script_tags = []
		meta_tags = []

		soup = BeautifulSoup(html, "html.parser")

		for s in soup.findAll('script'):
			script_tags.append(s)

		for m in soup.findAll('meta'):
			meta_tags.append(m)

		return script_tags, meta_tags

	@staticmethod
	def find_script(script_tags, regex_collection):
		for s in script_tags:
			for regex in regex_collection:
				if regex.search(s.get('src', '')):
					return True
		return False

	@staticmethod
	def find_meta(meta_tags, regex_collection):
		for meta, regex in iteritems(regex_collection):
			for m in meta_tags:
				if m.get('name', '').strip() == meta:
					if regex.search(m.get('content', '')):
						return True
		return False

	@staticmethod
	def find_headers(headers, regex_collection):
		for k, v in iteritems(regex_collection):
			if k in headers and re.search(v, headers[k]) is not None:
				return True
		return False

	@staticmethod
	def find_html(html, regex_collection):
		for regex in regex_collection:
			if regex.search(html):
				return True
		return False



'''
p = Analyzer('comprarseguridad.es')
result = p.analyze()
print result
'''