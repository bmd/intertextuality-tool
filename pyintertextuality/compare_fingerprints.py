# yikes - this is awful! Needs major re-work if this is determined
# to be the correct way to actually use the document fingerprints

def compare_fingerprints(fp1, fp2, threshold = 5):
    fp1_hashes = [f[2] for f in fp1]
    fp2_hashes = [f[2] for f in fp2]
    match_results = []
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

                    match_results.append((fp1[i][0][0], fp1[min(i+lenhit, len(fp1)-1)][0][-1], 
                                      fp2[j][0][0], fp2[min(j+lenhit, len(fp2)-1)][0][-1]))
        else:
            burnoff -= 1
    return match_results
