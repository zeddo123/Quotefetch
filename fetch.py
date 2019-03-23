#!/usr/bin/env python3
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

line_len = 8 #The maximum number of words in one line
text_color = '' # The Color of the quote (Default : White)
type_of_quote = '“”' # '«»'
quote_color = '1;33' # The color of the quote " ' "
file_name = 'quote.txt'

url = 'https://www.quotedb.com/quote/quote.php?action=random_quote'

try:
	raw = get_content(url).decode()
except:
	print('Connection Error')
	exit()

quote = re.findall(r'document.write\(\'(.*)\'\);', raw)

quote[1] = re.sub(r'<.*?>','',quote[1])
quote[0] = re.sub(r'<.*?>','',quote[0])

quote[1] = quote[1][16:]


content = quote[0]
author = quote[1]

words = content.split(' ')
lines = []

while words != []:
	line = ' '.join(words[:line_len])
	words = words[line_len:]
	lines.append(line)


format_str(lines)

lines = [i + '\n' for i in lines]
file = open(file_name,'w')

file.write(f'\033[{quote_color}m{type_of_quote[0]} \033[{text_color}m')
for line in lines:
	file.write(line)
file.write(f'{(len(max(lines))-len(author))* " "} \033[{quote_color}m{type_of_quote[1]}\033[{text_color}m {author}\n')

file.close()


