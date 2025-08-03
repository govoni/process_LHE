import sys
import pylhe
import pandas as pd
import vector
import numpy as np
import pickle

from utils import read_LHE_file

def main () :

    if len (sys.argv) < 3 :
        print ('usage: ' + sys.argv[0] + 'input.lhe ouptut.pkl')
    
    events = read_LHE_file (sys.argv[1])

    print ('read', len (events), 'events')

    sample = []

    # loop over events
    for event in events:

        # get particles present in the event
        v_input = []
        v_muons = []
        v_jets = []

        # loop over particles
        for p in event :
            vec = vector.obj (px=p['px'], py=p['py'], pz=p['pz'], E=p['E'])
            if p['st'] == -1         : v_input.append (vec)
            elif p['st'] == 2        : continue
            elif abs (p['id']) == 13 : v_muons.append (vec)
            elif abs (p['id']) < 7 \
                 or p['id'] == 21 \
                 or p['id'] == 9     : v_jets.append (vec)
            else                     : continue
        # end loop over particles
    
        assert len (v_input) == 2
        assert len (v_muons) == 2
        assert len (v_jets) == 2

        # prepare the info to be saved for data analysis

        v_muons.sort (key = lambda p : p.pt, reverse=True)
        v_jets.sort (key = lambda p : p.pt, reverse=True)

        vars = []
        vars.append (v_jets[0].pt)
        vars.append (v_jets[0].eta)
        vars.append (v_jets[0].phi)
        vars.append (v_jets[1].pt)
        vars.append (v_jets[1].eta)
        vars.append (v_jets[1].phi)
        vars.append (v_muons[0].pt)
        vars.append (v_muons[0].eta)
        vars.append (v_muons[0].phi)
        vars.append (v_muons[1].pt)
        vars.append (v_muons[1].eta)
        vars.append (v_muons[1].phi)

        v_Z = v_muons[0] + v_muons[1]
        vars.append (v_Z.M)
        vars.append (v_Z.eta)
        vars.append (v_Z.phi)
        vars.append (v_Z.pt)

        v_dijet = v_jets[0] + v_jets[1]
        vars.append (v_dijet.M)
        vars.append (v_dijet.pt)
        vars.append (v_dijet.eta)
        vars.append (v_dijet.phi)

        vars.append (abs (v_jets[0].eta - v_jets[1].eta))
        vars.append (v_jets[0].deltaphi(v_jets[1]))

        sample.append (vars)

    # end loop over events

    print ('processed', len (sample), 'events')

    print (sample[0])
    np_sample = np.array (sample)
    print (np_sample.shape)

    variables = ['j0_pt', 'j0.eta', 'j0_phi', 
                 'j1_pt', 'j1.eta', 'j1_phi',
                 'm0_pt', 'm0.eta', 'm0_phi',
                 'm1_pt', 'm1.eta', 'm1_phi', 
                 'z_M', 'z_pt', 'z.eta', 'z_phi',
                 'jj_M', 'jj_pt', 'jj.eta', 'jj_phi','jj_dEta', 'jj_dPhi', 
                ] 

    file_content = {'names': variables, 'events': np_sample}


    with open (sys.argv[2], 'wb') as f :
        pickle.dump (file_content, f)

    return 0


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 


if __name__ == '__main__' :
    
    main ()
