# process_LHE

## content

- **read_01.py**: ```pylhe``` unit test
- **read_02.py**: ```read_LHE_file``` unit test
- **read_03.py**: read a single LHE event
- **read_04.py**: read a full sample and store it in a pickle file
- **read_05.py**: pickle file reading unit test
- **read_06.py**: pickle file reading and histogram drawing
- **utils.py**: useful functions

## TODO

- variable plots
- save outside the repository in a output folder


## NOTES

### stacked histos in matplotlib (to be tested)
```
import numpy as np
import matplotlib.pyplot as plt

# Sample data for three groups
data1 = np.random.normal(loc=0, scale=1, size=500)
data2 = np.random.normal(loc=2, scale=1.5, size=500)
data3 = np.random.normal(loc=4, scale=1, size=500)

plt.hist([data1, data2, data3], bins=30, stacked=True,
         color=['red', 'green', 'blue'], edgecolor='black', alpha=0.7)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Stacked Histogram Example')
plt.show()
```