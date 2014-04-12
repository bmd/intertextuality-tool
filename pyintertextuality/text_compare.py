def find_strict_ngram_matches(text1, text2, ngram=5):
	"""
	Find all n-gram matches of length ngram or greater
	between tokenized texts text1 and text2.

	Text1 and text2 may either be raw texts or stemmed.
	"""
	good_matches = []
	burnoff = 0
	for idx1, token1 in enumerate(text1):
		if burnoff == 0:
			match_block = []
			for idx2, token2 in enumerate(text2):
				if token1 == token2:
					keep_matching = True
					while keep_matching:
						

