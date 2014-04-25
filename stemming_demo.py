# stdlib imports
from __future__ import division
import os, sys
from time import time()

# custom imports - all nltk imports behind the curtain
import pyintertextuality as itx

if __name__ == '__main__':
	vita_st_germani = itx.read_source_file('germani.txt')
	st = itx.SentenceTokenizer()
	wt = itx.WordTokenizer()
	all_tokens = [wt.make_word_tokens(sent) for sent in st.make_sentence_tokens(vita_st_germani)]
	correct_tokens = [item for sublist in all_tokens for item in sublist]

	descr = 'SCHINKE STEMMER'
	header = '-' * ((50-len(descr))//2) + ' ' + descr + ' ' + '-' * ((50-len(descr))//2)
	print header
	start = time()
	stemmer = itx.SchinkeStemmer(correct_tokens)
	stems = stemmer.stem()
	total_time = time() - start
	d = itx.TextDescriptor(stems)
	print 'Got {} unique stems'.format(len(set(stems)))
	print 'Lexical Richness: {:.3f}'.format(d.lexical_richness())
	print 'Test ran in {:.3f} seconds'.format(total_time)

	print '\n'
	descr = 'NAIVE STEMMER'
	header = '-' * ((50-len(descr))//2) + ' ' + descr + ' ' + '-' * ((50-len(descr))//2)
	print header
	naive_stemmer = itx.NaiveStemmer(correct_tokens)
	other_stems = naive_stemmer.stem()
	d2 = itx.TextDescriptor(other_stems)
	print 'Got {} unique stems'.format(len(set(other_stems)))
	print 'Lexical Richness: {:.3f}'.format(d2.lexical_richness())
	print '\n'
	