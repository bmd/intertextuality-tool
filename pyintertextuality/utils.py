# utilities for file handling, etc. that don't obviously belong in any other module
import os, sys

def read_source_file(infile):
	if not os.path.isfile(infile):
		sys.exit('>> Source file not found: \'{}\''.format(infile))
	with open(infile,'rU') as inf:
		return inf.read()