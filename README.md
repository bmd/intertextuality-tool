DARMC Intertextuality Analysis Library
====================
Fingerprinting Algorithms Demo:
```python
import pyintertextuality as itx

# read in files to compare
speech1 = itx.read_source_file('beaches.txt')
speech2 = itx.read_source_file('finest_hour.txt')

# hash using winnowing algorithm
winnow1 = itx.algorithms.winnow(speech1)
winnow2 = itx.algorithms.winnow(speech2)

# look for matches of at least 'threshold' hashes
compare_result = itx.compare_fingerprints(winnow1, winnow2, threshold=8)
```

Prints the following output with brackets denoting the core of the match:

```
-----------------------------
FINGERPRINTING ALGORITHM DEMO
-----------------------------
Importing Text 1: "We will fight on the beaches" - Winston Churchill (June 6, 1940)
Importing Text 2: "This was their finest hour" - Winston Churchill (June 18, 1940)
Winnowing texts... DONE
Searching for similarities between texts...
0%                                              100%
[##################################################]
Total time elapsed: 29.872 sec

-------
RESULTS
-------
(1) ower, the power of their [far more numerous Air Fo]rce, was thrown into the 
    The enemy is, of course, [far more numerous than w]e are. But our new produc

(2) . That is the resolve of [His Majesty's Government-every] man of them. That is the
    erned, but for our part, [His Majesty's Government ar]e entirely willing to acc

(3) liament and the nation. T[he British Empire and the F]rench Republic, linked to
     the British nation and t[he British Empire and that, on]ce we get properly equipp

(4) liament and the nation. T[he British Empire and] the French Republic, lin
     The British nation and t[he British Empire findi]ng themselves alone, stoo

(5) liament and the nation. T[he British Empire and] the French Republic, lin
    o because the fact that t[he British Empire stands] invincible, and that Naz

(6) liament and the nation. T[he British Empire and] the French Republic, lin
    ight have advanced with t[he British Empire to the re]scue of the independence 

(7) liament and the nation. T[he British Empire and] the French Republic, lin
    he United States and of t[he British Empire both re]quired that the United St

(8) liament and the nation. T[he British Empire and the Frenc]h Republic, linked togeth
    h-speaking democracies, t[he British Empire and the Un]ited States, will have to

```
