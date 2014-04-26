# stdlib imports
from __future__ import division
import os, sys
import pyintertextuality as itx
import multiprocessing
import glob

def compare_texts(winnow1, winnow2, threshold=10, optimize=True, CYTHON=True):
    compare_result = itx.compare_fingerprints(winnow1, winnow2, threshold=10, optimize=True, CYTHON=True)

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

if __name__ == '__main__':
    print '-----------------------------'
    print 'FINGERPRINTING ALGORITHM DEMO'
    print '-----------------------------'
    print 'Importing Text 1: "S. Praeiecti"'
    speech1 = itx.read_source_file('S. Praeiecti Text.txt').replace('\n','')

    print 'Importing Text 2: "Vita Columbani"'
    speech2 = itx.read_source_file('V. Columbani Text.txt').replace('\n','')

    print 'Importing Text 3: "Vita S. Germani"'
    speech3 = itx.read_source_file('germani.txt').replace('\n','')

    print 'Winnowing texts...',
    winnow1 = itx.algorithms.winnow(speech1, k=8, w=4)
    winnow2 = itx.algorithms.winnow(speech2, k=8, w=4)
    winnow3 = itx.algorithms.winnow(speech3, k=8, w=4)
    print 'DONE'

    print 'Running Comparisons'
    p = multiprocessing.Process(
        target=compare_texts, 
        args=(winnow1, winnow2)
        )
    q = multiprocessing.Process(
        target=compare_texts, 
        args=(winnow1, winnow3)
        )

    p.start()
    q.start()

