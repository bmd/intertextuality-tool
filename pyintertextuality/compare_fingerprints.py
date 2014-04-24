import pyprind
#import pyximport; pyximport.install()

USE_CYTHON = False

def do_matching(fp1, fp2, fp1_hashes, fp2_hashes, threshold):
    match_results = []
    # burn n-1 chars after a successful hit of n chars
    burnoff = 0
    prbar = pyprind.ProgBar(len(fp1_hashes))
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


def compare_fingerprints(fp1, fp2, threshold = 5):
    fp1_hashes = [f[2] for f in fp1]
    fp2_hashes = [f[2] for f in fp2]
    match_results = do_matching(fp1, fp2, fp1_hashes, fp2_hashes, threshold)

    return match_results
