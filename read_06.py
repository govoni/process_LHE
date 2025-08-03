import sys
import pylhe
import vector
import numpy as np
import pickle
import matplotlib.pyplot as plt
import numpy as np

from utils import sturges


def main () :

    if len (sys.argv) < 2 :
        print ('usage: ' + sys.argv[0] + 'input.pkl')
    
    with open(sys.argv[1], 'rb') as f :
        sample = pickle.load (f)

    print (sample['events'].shape)   
    print (sample['names']) 
    
    sam = sample['events']
    nam = sample['names']

    col_index = nam.index ('z_M')

    x_min = 0.
    x_max = 200.
    # x_min = np.min (sam[:, col_index])
    # x_max = np.max (sam[:, col_index])

    N_bins = 4 * sturges (len (sam))
    bin_edges = np.linspace (x_min, x_max, N_bins)
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (sam[:,col_index],
             bins = bin_edges,
             # histtype = 'step', # transparent
             histtype = 'stepfilled', 
             color = 'skyblue',
             edgecolor = 'skyblue'
            )
    ax.set_title ('dimuon pair mass', size=14)
    ax.set_xlabel ('mass (GeV)')
    ax.set_ylabel ('event counts per bin')
    ax.set_yscale ('log')

    plt.savefig ('read_06.png')


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 


if __name__ == '__main__' :
    
    main ()
