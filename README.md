DARMC Intertextuality Analysis Library
====================

DEMO:

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

prints the following output with brackets denoting the core of the match:

```
-----------------------------
FINGERPRINTING ALGORITHM DEMO
-----------------------------
Importing Text 1: "We will fight on the beaches" - Winston Churchill (June 6, 1940)
Importing Text 2: "This was their finest hour" - Winston Churchill (June 18, 1940)
Winnowing texts... DONE
Searching for similarities between texts... DONE

-------
RESULTS
-------
(1)  nation. T[he British Empire and] the Frenc
    tion and t[he British Empire and tha]t, once we

(2)  nation. T[he British Empire and the F]rench Repu
    cracies, t[he British Empire and the] United St

(3) tion. The [British Empire and the F]rench Repu
    cies, the [British Empire and the] United St

```
