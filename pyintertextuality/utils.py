import os
import sys

def read_source_file(infile):
    if not os.path.isfile(infile):
        sys.exit('Source file not found: \'{}\''.format(infile))
    
    with open(infile,'rU') as inf:
        # always clear line breaks
        return inf.read().replace('\r\n','').replace('\n','')