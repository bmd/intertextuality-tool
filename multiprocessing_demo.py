# stdlib imports
from __future__ import division
import os, sys
import pyintertextuality as itx
import multiprocessing
import glob

def compare_texts(speech1, speech2, winnow1, winnow2, threshold=10, optimize=True, CYTHON=True):
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
    print '-----------------------------------'
    print 'MULTIPROCESSING IMPLEMENTATION DEMO'
    print '-----------------------------------'
    print 'Importing Source Text: "S. Praeiecti"'
    main_text = itx.read_source_file('S. Praeiecti Text.txt').replace('\n','')

    print 'Importing Comparison Texts...',
    vulgate_pieces = glob.glob(os.path.join('Vulgate','Vul*.txt'))
    print '{} pieces found'.format(len(vulgate_pieces))

    vulgate_texts = []
    for infile in vulgate_pieces:
        vulgate_texts.append(itx.read_source_file(infile))

    print 'Winnowing texts...',
    winnowed_vulgate = []
    for text in vulgate_texts:
        winnowed_vulgate.append(itx.algorithms.winnow(text, k=8, w=4))
    winnowed_src = itx.algorithms.winnow(main_text, k=8, w=4)
    print 'DONE'

    print 'Running Comparisons'
    processes = []
    for i, winnowed_chunk in enumerate(winnowed_vulgate):
        p = multiprocessing.Process(
            target=compare_texts, 
            args=(main_text, vulgate_texts[i], winnowed_src, winnowed_chunk)
            )
        processes.append(p)
        p.start()
