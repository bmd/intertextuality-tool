# stdlib imports
from __future__ import division
import os, sys

# custom imports - all nltk imports behind the curtain
import pyintertextuality as itx

if __name__ == '__main__':
    print '\n'
    speech1 = itx.read_source_file('beaches.txt')
    speech2 = itx.read_source_file('finest_hour.txt')

    winnow1 = itx.algorithms.winnow(speech1)
    winnow2 = itx.algorithms.winnow(speech2)

    compare_result = itx.compare_fingerprints(winnow1, winnow2, threshold=8)

    for (t1st, t1end, t2st, t2end) in compare_result:
        print '{}[{}]{}\n{}[{}]{}\n'.format(speech1[t1st-10:t1st], 
                                           speech1[t1st:t1end+1], 
                                           speech1[t1end+1:t1end+11],
                                           speech2[t2st-10:t2st],
                                           speech2[t2st:t2end+1],
                                           speech2[t2end+1:t2end+11]
                                           )