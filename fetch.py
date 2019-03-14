#!/usr/bin/env python
import html
import requests
import re

line_len = 7 #The maximum nomber of words in one line
text_color = ''
type_of_quote = '“”' # '«»'
quote_color = '1;33'
file_name = 'quote.txt'

url = 'http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1'

try:
	raw_file = requests.get(url).json()
except:
	print('Connection Error')
	exit()

content = re.sub(r'<.*?>', '',raw_file[0]['content'])
while '\n' in content:
	content = content.replace('\n','')

content = html.unescape(content)
author = raw_file[0]['title']

words = content.split(' ')
lines = []

while words != []:
	line = ' '.join(words[:line_len])
	words = words[line_len:]
	if words == []:
		lines.append(line)
	else:
		lines.append(line+'\n')

file = open(file_name,'w')

file.write(f'\033[{quote_color}m{type_of_quote[0]} \033[{text_color}m')
for line in lines:
	file.write(line)
file.write(f'\033[{quote_color}m{type_of_quote[1]}\033[{text_color}m {author}\n')

file.close()


