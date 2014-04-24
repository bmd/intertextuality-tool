import re

regex_lit = r'(^|\b)([a-zA-Z]{1,3})(\b|$)'
exp = re.compile(regex_lit)

text = "A cat jumped on the wall to the left of me"

overspaced = re.sub(exp, "", text)
overspaced = re.sub(re.compile(r'\s+')," ", overspaced).strip()

print '\n------------------'
print 'REGEX TESTING DEMO'
print '------------------'

print 'Original     : {}'.format(text)
print 'Compiled with: {}'.format(regex_lit)
print 'Final version: {}\n'.format(overspaced)