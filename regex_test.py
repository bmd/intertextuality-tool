import re

words = ['in', 'on', 'I','to','forever']
exp = re.compile(r'(^|\b)([a-zA-Z]{1,3})(\b|$)')

for word in words:
	print word, re.match(exp, word)

text = "A cat jumped on the wall the the left of me"

overspaced = re.sub(exp, "", text)
print re.sub(re.compile(r'\s+')," ", overspaced).strip()