from __future__ import division
import pyprind
import sys
import hashlib
from time import time
from collections import OrderedDict

def _assemble_hash_dict(fp, threshold):
    hash_dict = OrderedDict()
    #print text[1]
    for x in range(len(fp)-threshold):
        chars = ''.join([str(v[2]) for v in fp[x:x+threshold]])
        hs = hashlib.sha1(chars.encode('utf-8'))
        hs = hs.hexdigest()
        candidate_val = int(hs, 16)
        #print candidate_val
        if candidate_val not in hash_dict:
            hash_dict[candidate_val] = [(fp[x][0][0], fp[x+threshold][0][-1])]
        else:
            hash_dict[candidate_val].append((fp[x][0][0], fp[x+threshold][0][-1]))
    return hash_dict

def fast_matching(fp1, fp2, threshold):
    # assemble hash dict
    ngram_hash_dict_1 = _assemble_hash_dict(fp1, threshold)
    ngram_hash_dict_2 = _assemble_hash_dict(fp2, threshold)

    results_list = []
    burnoff = 0
    for hash_key, location_list in ngram_hash_dict_1.items():
        # if that 5-gram appears in the other text
        if hash_key in ngram_hash_dict_2:
            for item in location_list:
                for match in ngram_hash_dict_2[hash_key]:
                    results_list.append((
                        item[0] , item[1], match[0],match[1]))

    return results_list

def do_matching(fp1, fp2, fp1_hashes, fp2_hashes, threshold):
    match_results = []

    # burn n-1 chars after a successful hit of n chars
    prbar = pyprind.ProgBar(len(fp1_hashes), stream=sys.stdout)
    burnoff = 0
    len2 = len(fp2_hashes)

    for i in xrange(len(fp1_hashes)):
        if burnoff == 0:
            for j in xrange(len2):
                if fp2_hashes[j:j+threshold] == fp1_hashes[i:i+threshold]:
                    still_matching = True
                    addtl_chars = 1
                    while still_matching:
                        if fp2_hashes[j:j+threshold+addtl_chars] == fp1_hashes[i:i+threshold+addtl_chars]:
                            addtl_chars += 1
                        else:
                            still_matching = False

                    lenhit = threshold + addtl_chars
                    burnoff = lenhit

                    match_results.append((fp1[i][0][0], fp1[min(i+lenhit, len(fp1)-1)][0][-1], 
                                      fp2[j][0][0], fp2[min(j+lenhit, len(fp2)-1)][0][-1]))
        
        else:
            burnoff -= 1
        prbar.update()

    return match_results

def remove_unmatched_hash_values(fp1, fp2):
    print 'OPTIMIZATION:\n  Removing kgram hashes not shared between both texts...'

    fp2_hashes = set([f[2] for f in fp2])
    fp1_start_len = len(fp1)
    for idx, item in enumerate(fp1):
        if item[2] not in fp2_hashes:
            fp1.pop(idx)
    removed = (fp1_start_len - len(fp1)) / fp1_start_len
    print '  Reduced text 1 from {} fingerprint values to {} ({:.2%})'.format(fp1_start_len, len(fp1), removed)

    fp1_hashes = set([f[2] for f in fp1])
    fp2_start_len = len(fp2)
    for idx, item in enumerate(fp2):
        if item[2] not in fp1_hashes:
            fp2.pop(idx)

    removed = (fp2_start_len - len(fp2)) / fp2_start_len
    print '  Reduced text 2 from {} fingerprint values to {} ({:.2%})'.format(fp2_start_len, len(fp2), removed)

    print '  Decreased total complexity from {:.2e} to {:.2e} iterations ({:.2%})'.format(fp1_start_len * fp2_start_len, len(fp1)*len(fp2), (len(fp1)*len(fp2))/(fp1_start_len * fp2_start_len))
    return fp1, fp2


def compare_fingerprints(fp1, fp2, threshold = 5, optimize=False, CYTHON=False):
    #if optimize:
    #    fp1, fp2 = remove_unmatched_hash_values(fp1, fp2)
    
    #fp1_hashes = [f[2] for f in fp1]
    #fp2_hashes = [f[2] for f in fp2]
    start = time()

    result = fast_matching(fp1, fp2, threshold)
    print 'Matched in {:.5f} seconds'.format(time()-start)

    return result
    #if CYTHON:
    #    try:
    #        import pyximport; pyximport.install()
    #        from cython_fingerprints import cython_match
    #    except ImportError:
    #        sys.exit('Cython does not appear to be properly configured on your system. Try comparing fingerprints using CYTHON=False')        
    #
    #    match_results = cython_match(fp1, fp2, fp1_hashes, fp2_hashes, threshold)
    #else:
    #    match_results = do_matching(fp1, fp2, fp1_hashes, fp2_hashes, threshold)

    #return match_results
