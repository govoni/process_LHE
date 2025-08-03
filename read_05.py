import sys
import pylhe
import vector
import numpy as np
import pickle


def main () :

    if len (sys.argv) < 2 :
        print ('usage: ' + sys.argv[0] + 'input.pkl')
    
    with open(sys.argv[1], 'rb') as f :
        sample = pickle.load (f)

    print (sample['events'].shape)   
    print (sample['names']) 
    

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 


if __name__ == '__main__' :
    
    main ()
