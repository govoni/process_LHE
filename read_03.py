import sys
import pylhe
import pandas as pd
import vector

from utils import read_LHE_file

def main () :

    if len (sys.argv) < 2 :
        print ('usage: ' + sys.argv[0] + 'input.lhe')
    
    events = read_LHE_file (sys.argv[1])

    print ('read ', len (events), 'events')

    # analysis of a single event


    # get particles present in the event
    v_input = []
    v_muons = []
    v_jets = []
    for p in events[0] :
        vec = vector.obj (px=p['px'], py=p['py'], pz=p['pz'], E=p['E'])
        if p['st'] == -1         : v_input.append (vec)
        elif p['st'] == 2        : continue
        elif abs (p['id']) == 13 : v_muons.append (vec)
        elif abs (p['id']) < 7 \
             or p['id'] == 21 \
             or p['id'] == 9     : v_jets.append (vec)
        else                     : continue

    assert len (v_input) == 2
    assert len (v_muons) == 2
    assert len (v_jets) == 2

    # test of kinematics
    for j in v_input : print (j.px, j.py, j.pz, j.eta)    
    for j in v_muons : print (j.px, j.py, j.pz, j.eta)    
    for j in v_jets : print (j.px, j.py, j.pz, j.eta)
    v_Z = v_muons[0] + v_muons[1]
    print (v_Z.M)  

    return 0


if __name__ == '__main__' :
    
    main ()
