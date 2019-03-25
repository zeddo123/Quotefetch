from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import re

def format_str(l):
	max_line = max([len(i) for i in l])

	for i in range(len(l)):
		while len(l[i]) < max_line:
			l[i] = ' ' + l[i] + ' ' # Format the lines to be equale

def get_content(url):
	try:
		with closing(get(url, stream=True)) as resp:
			if is_good_response(resp):
				return resp.content
			else:
				return None
	except RequestException as e:
		print('Error during requests')
		return None# Get the quote from the web site

def is_good_response(resp):
	content_type = resp.headers['Content-Type'].lower()
	return(resp.status_code == 200 
			and content_type is not None 
			and content_type.find('html') > -1)

def remove_web(raw):
	quote = re.findall(r'document.write\(\'(.*)\'\);', raw)

	quote[1] = re.sub(r'<.*?>','',quote[1])
	quote[0] = re.sub(r'<.*?>','',quote[0])

	quote[1] = quote[1][16:]

	return quote

def create_lines(words, line_len):
	lines = []
	while words != []:
		line = ' '.join(words[:line_len])
		words = words[line_len:]
		lines.append(line)

	return lines
