
def sanitize(text):
    import re
    tuples = zip(xrange(len(text)), text)
    v = re.compile(r'[^a-zA-Z0-9]')
    return [(t[0], t[1].lower()) for t in tuples if v.match(t[1]) == None]

def kgram_gen(sanitized_text, k=5):
    for x in xrange(len(sanitized_text)-k+1):
        yield sanitized_text[x:x+k]

def hash(text):
    import hashlib
    
    hs = hashlib.sha1(text.encode('utf-8'))
    hs = hs.hexdigest()[-4:]
    hs = int(hs, 16)

    return hs

def compute_kgram_hashes(sanitized):
    final = []
    for k in kgram_gen(sanitized):
        unpacked = zip(*k)
        #print ''.join(unpacked[1])
        final.append([unpacked[0], unpacked[1], hash(''.join(unpacked[1]))])
    return final

def winnow_kgrams(hashed_kgrams, window=4):
    fingerprints = []
    for k in xrange(len(hashed_kgrams)-window+1):
        min_hash = min(hashed_kgrams[k:k+window], key=lambda x: x[2])
        try:
            if fingerprints[-1] != min_hash:
                fingerprints.append(min_hash)
        except IndexError:
            fingerprints.append(min_hash)

    return fingerprints

def winnow(text):
    sanitized = sanitize(text)
    kgram_hashes = compute_kgram_hashes(sanitized)
    return winnow_kgrams(kgram_hashes)

if __name__ == '__main__':
    text = "Even though large tracts of Europe and many old and famous States have fallen or may fall into the grip of the Gestapo and all the odious apparatus of Nazi rule, we shall not flag or fail. We shall go on to the end. We shall fight in France, we shall fight on the seas and oceans, we shall fight with growing confidence and growing strength in the air, we shall defend our island, whatever the cost may be. We shall fight on the beaches, we shall fight on the landing grounds, we shall fight in the fields and in the streets, we shall fight in the hills; we shall never surrender, and if, which I do not for a moment believe, this island or a large part of it were subjugated and starving, then our Empire beyond the seas, armed and guarded by the British Fleet, would carry on the struggle, until, in God's good time, the New World, with all its power and might, steps forth to the rescue and the liberation of the old."
    print winnow(text)


    