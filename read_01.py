import sys
import pylhe
import pandas as pd

from utils import read_LHE_file

def main () :

    if len (sys.argv) < 2 :
        print ('usage: ' + sys.argv[0] + 'input.lhe')
    
    lhe_events = pylhe.read_lhe_with_attributes (sys.argv[0])
    
    return 0


if __name__ == '__main__' :
    main ()
