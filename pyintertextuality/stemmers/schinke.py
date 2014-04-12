"""
Schinke R, Greengrass M, Robertson AM and Willett P (1996) A stemming algorithm for Latin text databases. Journal of Documentation, 52: 172-187.
"""
class SchinkeStemmer:
    def __init__(self, text):
        self.src = text
        self.QUE_PRESERVE = ['atque', 'quoque', 'neque', 'itaque', 'absque', 'apsque', 
            'abusque', 'adaeque', 'adusque', 'denique', 'deque', 'susque', 
            'oblique', 'peraeque', 'plenisque', 'quandoque', 'quisque', 
            'quaeque', 'cuiusque', 'cuique', 'quemque', 'quamque', 'quaque', 
            'quique', 'quorumque', 'quarumque', 'quibusque', 'quosque', 
            'quasque', 'quotusquisque', 'quousque', 'ubique', 'undique', 
            'usque', 'uterque', 'utique', 'utroque', 'utribique', 'torque', 
            'coque', 'concoque', 'contorque', 'detorque', 'decoque', 'excoque', 
            'extorque', 'obtorque', 'optorque', 'retorque', 'recoque', 
            'attorque', 'incoque', 'intorque', 'praetorque']

    def _longer(self, n, v):
        if len(v) > len(n):
            return v
        else:
            return n

    def _remove_noun_suffix(self, tk):
        NOUN_SUFFIXES = ['ibus', 'ius', 'ae', 'am', 'as', 'em', 'es', 'ia',
        'is', 'nt', 'os', 'ud', 'um', 'us', 'a', 'e', 'i', 'o', 'u']

        for suff in NOUN_SUFFIXES:
            if tk.endswith(suff):
                # don't use replace unless you implement rreplace
                return tk[:-len(suff)]
        else:
            return tk
   
    def _noun_stem(self, token):
        ntoken = token[:]
        original = token[:]

        # return if either too short, or a protected word
        if (len(ntoken) <= 4 or 
            ntoken.lower() in self.QUE_PRESERVE):
            return ntoken

        # strip que
        if len(ntoken) > 3 and ntoken[-4:] == 'que':
            ntoken = ntoken.replace('que','')

        ntoken = self._remove_noun_suffix(ntoken)

        if len(ntoken) >= 2:
            return ntoken
        else:
            return original

    def _remove_verb_suffix(self, tk):
        VERB_SUFFIXES = ['iuntur', 'beris', 'erunt', 'untur', 'iunt', 'mini', 
        'ntur', 'stis', 'bor', 'ero', 'mur', 'mus', 'ris', 'sti', 'tis', 'tur',
        'unt',  'bo', 'ns', 'nt', 'ri', 'm', 'r', 's', 't']

        i_replace = ['iuntur','erunt','untur','iunt','unt']
        bi_replace = ['beris','bor','bo']

        for suff in VERB_SUFFIXES:
            if tk.endswith(suff):
                if suff in i_replace:
                    return tk[:-len(suff)] + 'i'
                elif suff in bi_replace:
                    return tk[:-len(suff)] + 'bi'
                elif suff == 'ero':
                    return tk[:-len(suff)] + 'eri'
                else:
                    return tk[:-len(suff)]
        else:
            return tk

    def _verb_stem(self, token):

        vtoken = token[:]
        original = vtoken[:]

        # return if either too short, or a protected word
        if (len(original) <= 4 or 
            original.lower() in self.QUE_PRESERVE):
            return vtoken

        # stripi que
        if len(vtoken) > 3 and vtoken.endswith('que'):
            vtoken = vtoken.replace('que','')

        # handle verb suffixes 
        vtoken = self._remove_verb_suffix(vtoken)

        # now return it
        if len(vtoken) >= 2:
            return vtoken
        else:
            return original

    def stem(self):
        """Convert all occurrences of the letters 'j' or 'v' 
        # to 'i' or 'u', respectively."""
        stemmed = [token.replace('j','i').replace('v','u') for token in self.src]

        for idx, word in enumerate(stemmed):
            #stemmed[idx] = self._longer(self._noun_stem(word), self._verb_stem(word))
            stemmed[idx] = self._longer(self._noun_stem(word), self._verb_stem(word))
        return stemmed