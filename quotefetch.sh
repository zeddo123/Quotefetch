#!/bin/bash
python fetch.py
quote=$(<quote.txt)
cat<< END

	$quote

END