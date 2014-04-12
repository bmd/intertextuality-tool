# stdlib imports
from __future__ import division
import os, sys

# custom imports - all nltk imports behind the curtain
import pyintertextuality as itx

if __name__ == '__main__':
	print '\n'
	speech1 = itx.read_source_file('beaches.txt')
	speech2 = itx.read_source_file('finest_hour.txt')
	"""
	#descr = 'WORD TOKENIZER'
	#header = '-' * ((50-len(descr))//2) + ' ' + descr + ' ' + '-' * ((50-len(descr))//2)
	#print header
	wt = itx.WordTokenizer()

	#descr = 'SENTENCE TOKENIZER'
	#header = '-' * ((50-len(descr))//2) + ' ' + descr + ' ' + '-' * ((50-len(descr))//2)
	#print header
	st = itx.SentenceTokenizer()

	#descr = 'COMBINED TOKENIZER'
	#header = '-' * ((50-len(descr))//2) + ' ' + descr + ' ' + '-' * ((50-len(descr))//2)
	#print header
	all_tokens = [wt.make_word_tokens(sent) for sent in st.make_sentence_tokens(vita)]
	correct_tokens = [item for sublist in all_tokens for item in sublist]

	descr = 'SCHINKE STEMMER'
	header = '-' * ((50-len(descr))//2) + ' ' + descr + ' ' + '-' * ((50-len(descr))//2)
	print header
	stemmer = itx.SchinkeStemmer(correct_tokens)
	stems = stemmer.stem()
	d = itx.TextDescriptor(stems)
	print 'Got {} unique stems'.format(len(set(stems)))
	print 'Lexical Richness: {:.3f}'.format(d.lexical_richness())

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
	#descr = 'DESCRIPTOR'
	#header = '-' * ((50-len(descr))//2) + ' ' + descr + ' ' + '-' * ((50-len(descr))//2)
	#print header
	#d = itx.TextDescriptor(correct_tokens)
	#print 'Lexical Richness: {}'.format(d.lexical_richness())
	#print d.frequencies()
	#print d.hapaxes()"""
	"""
	