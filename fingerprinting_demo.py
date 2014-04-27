# stdlib imports
from __future__ import division
import os, sys
import pyintertextuality as itx
import multiprocessing
import glob
from fuzzywuzzy import fuzz



def compare_texts(speech1, speech2, winnow1, winnow2, threshold=10, optimize=True, CYTHON=True):
    #compare_result = itx.compare_fingerprints(winnow1, winnow2, threshold, optimize=True, CYTHON=True)

    F = itx.FingerprintMatcher(winnow1, winnow2, threshold)
    compare_result = F.match()

    print '\n-------'
    print 'RESULTS'
    print '-------'
    for idx, (t1st, t1end, t2st, t2end) in enumerate(itx.remove_duplicate_matches(speech1, speech2, compare_result)):
        print '({}) {}[{}]{}\n    {}[{}]{}\n'.format(idx+1,
                                           speech1[t1st-25:t1st], 
                                           speech1[t1st:t1end+1], 
                                           speech1[t1end+1:t1end+26],
                                           speech2[t2st-25:t2st],
                                           speech2[t2st:t2end+1],
                                           speech2[t2end+1:t2end+26]
                                           )


if __name__ == '__main__':
    print '-----------------------------'
    print 'FINGERPRINTING ALGORITHM DEMO'
    print '-----------------------------'
    print 'Importing Text 1: "S. Praeiecti"...'
    speech1 = itx.read_source_file('S. Praeiecti Text.txt')

    print 'Importing Text 2: "Complete Vulgate"...'
    speech2 = itx.read_source_file('Vulgate/vul_complete.txt')

    print 'Winnowing text 1...'
    winnow1 = itx.algorithms.winnow(speech1, k=6, w=4)
    print 'Winnowing text 2...'
    winnow2 = itx.algorithms.winnow(speech2, k=6, w=4)

    print 'Searching texts for matches'
    compare_texts(speech1, speech2, winnow1, winnow2, threshold=5, optimize=True, CYTHON=True)

