#!/usr/bin/env python3
from utils import *

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

quote = remove_web(raw)

content = quote[0]
author = quote[1]

words = content.split(' ')

lines = create_lines(words,line_len)
format_str(lines)

lines = [i + '\n' for i in lines] #adding return charcater to every line


with open(file_name,'w') as file:
	file.write(f'\033[{quote_color}m{type_of_quote[0]} \033[{text_color}m')
	
	for line in lines:
		file.write(line)
	
	file.write(f'{(len(max(lines))-len(author))* " "} \033[{quote_color}m{type_of_quote[1]}\033[{text_color}m {author}\n')



