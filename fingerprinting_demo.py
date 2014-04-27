from __future__ import division
# stdlib imports
import os
import sys
import glob
# external packages
from fuzzywuzzy import fuzz
# intertextuality package import
import pyintertextuality as itx


def compare_texts(speech1, speech2, winnow1, winnow2, cmptext, threshold=10, optimize=True, CYTHON=True):
    #compare_result = itx.compare_fingerprints(winnow1, winnow2, threshold, optimize=True, CYTHON=True)

    F = itx.FingerprintMatcher(winnow1, winnow2, threshold, progress=False)
    compare_result = F.match()
    if len(compare_result) > 0:
        print '\n--------------------'
        print 'RESULTS: {}'.format(cmptext.upper())
        print '--------------------'
        #for idx, (t1st, t1end, t2st, t2end) in enumerate(itx.remove_duplicate_matches(speech1, speech2, compare_result)):
        for idx, (t1st, t1end, t2st, t2end) in enumerate(compare_result):
            print '({}) {}[{}]{}\n    {}[{}]{}\n'.format(idx+1,
                                               speech1[t1st-50:t1st], 
                                               speech1[t1st:t1end+1], 
                                               speech1[t1end+1:t1end+51],
                                               speech2[t2st-50:t2st],
                                               speech2[t2st:t2end+1],
                                               speech2[t2end+1:t2end+51]
                                               )


if __name__ == '__main__':
    print '-----------------------------'
    print 'FINGERPRINTING ALGORITHM DEMO'
    print '-----------------------------'
    print 'Importing Text 1: "S. Praeiecti"...'
    speech1 = itx.read_source_file(os.path.join('Vitae', 'S. Praeiecti Text.txt'))
    print 'Winnowing text 1...'
    winnow1 = itx.algorithms.winnow(speech1, k=6, w=4)
    
    for fname in glob.glob(os.path.join('clemtext', '*.lat')):
        root_name = fname.split('/')[1].replace('.lat','')
        #print 'Importing Comparison Text: "{}"'.format(root_name)
        speech2 = itx.read_source_file(fname)
        #print 'Winnowing {}'.format(root_name)
        winnow2 = itx.algorithms.winnow(speech2, k=6, w=4)
        #print 'Searching texts for matches'
        compare_texts(speech1, speech2, winnow1, winnow2, root_name, threshold=5, optimize=True, CYTHON=True)

