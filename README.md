intertextuality-tool
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
nation. T[he British Empire and] the Frenc
tion and t[he British Empire and tha]t, once we

nation. T[he British Empire and the F]rench Repu
cracies, t[he British Empire and the] United St

tion. The [British Empire and the F]rench Repu
cies, the [British Empire and the] United St
```
