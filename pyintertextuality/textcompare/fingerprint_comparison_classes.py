from __future__ import division
import sys
import hashlib
from time import time
from collections import OrderedDict

class FingerprintMatcher:
    def __init__(self, fingerprint1, fingerprint2, threshold=5):
        if len(fingerprint1) == 0 or len(fingerprint2) == 0:
            sys.exit('FAILED: Attempted to recieve 0-length fingerprint.')
        self.fp1 = fingerprint1
        self.fp2 = fingerprint2
        self.threshold = threshold

    def __repr__(self):
        return "\n-- FINGERPRINT MATCHER -- \
                \nText 1 fingerprinted length: {} \
                \nText 2 fingerprinted length: {} \
                \nFingerprint match threshold: {}".format(len(self.fp1), len(self.fp2), self.threshold) 

    def _hash(self, chunk):
        hs = hashlib.sha1(chunk.encode('utf-8')).hexdigest()
        return int(hs, 16)

    def _assemble_hash_dict(self, fp):
        """
        Given a fingerprinted text 'fp',  return an ordered dict of hash values
        based on the combined hash values of each fingerprint set [x:x+threshold] 
        within 'fp'.

        TODO: Explain this better - probably needs to be a diagram somewhere of this
            data structure.
        """
        composite_hashes = OrderedDict()

        for x in xrange(len(fp)-self.threshold):
            cphash = self._hash(''.join([str(v[2]) for v in fp[x:x+self.threshold]]))
            
            if cphash not in composite_hashes:
                composite_hashes[cphash] = [(fp[x][0][0], fp[x+self.threshold][0][-1])]
            else:
                composite_hashes[cphash].append((fp[x][0][0], fp[x+self.threshold][0][-1]))

        return composite_hashes

    def match(self):
        start_time = time()
        ngram_hash_dict_1 = self._assemble_hash_dict(self.fp1)
        ngram_hash_dict_2 = self._assemble_hash_dict(self.fp2)

        results_list = []
        for hash_key, location_list in ngram_hash_dict_1.items():
            # if that 5-gram appears in the other text
            if hash_key in ngram_hash_dict_2:
                results_list += [
                    (item[0], item[1], match[0], match[1]) 
                        for match in ngram_hash_dict_2[hash_key] 
                            for item in location_list                   
                    ]

        print 'Total matching time: {:.3f}s'.format(time()- start_time)
        return results_list
