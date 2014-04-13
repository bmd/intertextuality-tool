# stdlib imports
from __future__ import division
import os, sys
import pyintertextuality as itx

if __name__ == '__main__':
    print '-----------------------------'
    print 'FINGERPRINTING ALGORITHM DEMO'
    print '-----------------------------'
    print 'Importing Text 1: "We will fight on the beaches" - Winston Churchill (June 6, 1940)'
    speech1 = itx.read_source_file('beaches.txt')

    print 'Importing Text 2: "This was their finest hour" - Winston Churchill (June 18, 1940)'
    speech2 = itx.read_source_file('finest_hour.txt')

    print 'Winnowing texts...',
    winnow1 = itx.algorithms.winnow(speech1)
    winnow2 = itx.algorithms.winnow(speech2)
    print 'DONE'

    print 'Searching for similarities between texts...'
    compare_result = itx.compare_fingerprints(winnow1, winnow2, threshold=7)

    print '\n-------'
    print 'RESULTS'
    print '-------'
    for idx, (t1st, t1end, t2st, t2end) in enumerate(compare_result):
        print '({}) {}[{}]{}\n    {}[{}]{}\n'.format(idx+1,
                                           speech1[t1st-25:t1st], 
                                           speech1[t1st:t1end+1], 
                                           speech1[t1end+1:t1end+26],
                                           speech2[t2st-25:t2st],
                                           speech2[t2st:t2end+1],
                                           speech2[t2end+1:t2end+26]
                                           )