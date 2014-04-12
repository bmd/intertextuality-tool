#from algorithms.winnower import winnow

def compare_fingerprints(fp1, fp2, threshold = 5):
    fp1_hashes = [f[2] for f in fp1]
    fp2_hashes = [f[2] for f in fp2]
    match_idxs = []
    # burn n-1 chars after a successful hit of n chars
    for i, hs in enumerate(fp1_hashes):
        burnoff = 0
        if burnoff == 0:
            for j, hs2 in enumerate(fp2_hashes):
                if fp2_hashes[j:j+threshold] == fp1_hashes[i:i+threshold]:
                    still_matching = True
                    addtl_chars = 1
                    while still_matching:
                        if fp2_hashes[j:j+threshold+addtl_chars] == fp1_hashes[i:i+threshold+addtl_chars]:
                            addtl_chars += 1
                            #print 'Matched {} chars'.format(threshold+addtl_chars)
                        else:
                            still_matching = False

                    lenhit = threshold + addtl_chars - 1
                    #burnoff = lenhit
                    #print 'Burning {} chars'.format(burnoff)

                    match_idxs.append((fp1[i][0][0], fp1[min(i+lenhit, len(fp1)-1)][0][-1], 
                                      fp2[j][0][0], fp2[min(j+lenhit, len(fp2)-1)][0][-1]))
        else:
            burnoff -= 1
    return match_idxs
"""
if __name__ == '__main__':
    with open('beaches.txt', 'rU') as inf:
        text1 = inf.read()
    with open('finest_hour.txt', 'rU') as inf:
        text2 = inf.read()
    fp1 = winnow(text1)
    fp2 = winnow(text2)
    
    cmpare = compare_fingerprints(fp1, fp2, threshold=6)
    print len(cmpare)
    #for (t1st, t1end, t2st, t2end) in compare_fingerprints(fp1, fp2, threshold=6):
    #    print '{} | {}'.format(text1[t1st:t1end+1], text2[t2st:t2end+1])"""