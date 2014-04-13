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
(1) rceness, and their main power, the power of their [far more numerous Air Fo]rce, was thrown into the battle or else concentrat
    n quantity and quality.  The enemy is, of course, [far more numerous than w]e are. But our new production already, as I am adv

(2) we are going to try to do. That is the resolve of [His Majesty's Government-every] man of them. That is the will of Parliament and t
    the various Colonies concerned, but for our part, [His Majesty's Government ar]e entirely willing to accord defence facilities to

(3) . That is the will of Parliament and the nation. T[he British Empire and the F]rench Republic, linked together in their cause and
    nius and the resources of the British nation and t[he British Empire and that, on]ce we get properly equipped and properly started, 

(4) . That is the will of Parliament and the nation. T[he British Empire and] the French Republic, linked together in their cau
    other side of the scales. The British nation and t[he British Empire findi]ng themselves alone, stood undismayed against disa

(5) . That is the will of Parliament and the nation. T[he British Empire and] the French Republic, linked together in their cau
     for years." I say it also because the fact that t[he British Empire stands] invincible, and that Nazidom is still being resis

(6) . That is the will of Parliament and the nation. T[he British Empire and] the French Republic, linked together in their cau
    , and the French Empire might have advanced with t[he British Empire to the re]scue of the independence and integrity of the Fren

(7) . That is the will of Parliament and the nation. T[he British Empire and] the French Republic, linked together in their cau
    n that the interests of the United States and of t[he British Empire both re]quired that the United States should have faciliti

(8) . That is the will of Parliament and the nation. T[he British Empire and the Frenc]h Republic, linked together in their cause and in 
    ganisations of the English-speaking democracies, t[he British Empire and the Un]ited States, will have to be somewhat mixed up tog

```
