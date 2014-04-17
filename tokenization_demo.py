# stdlib imports
from __future__ import division
import os, sys

# custom imports - all nltk imports behind the curtain
import pyintertextuality as itx

if __name__ == '__main__':
	vita_st_germani_excerpt = itx.read_source_file('germani.txt')[0:1000]

	print '--------------'
	print 'TOKENIZER DEMO'
	print '--------------'

	print 'WORD TOKENIZER'
	wt = itx.WordTokenizer()
	print wt.make_word_tokens(vita_st_germani_excerpt)
	print '\n'

	print 'SENTENCE TOKENIZER'
	st = itx.SentenceTokenizer()
	print st.make_sentence_tokens(vita_st_germani_excerpt)
	print '\n'

	print 'COMBINATION TOKENIZER'
	all_tokens = [wt.make_word_tokens(sent) for sent in st.make_sentence_tokens(vita_st_germani_excerpt)]
	print [item for sublist in all_tokens for item in sublist]
	print '\n'
	