import pylhe
import numpy as np
from math import ceil


def read_LHE_file (LHE_file_name) : 

    lhe_events = pylhe.read_lhe_with_attributes (LHE_file_name)

    events = []
    for event_id, event in enumerate (lhe_events):
        particles = []
        for i, particle in enumerate (event.particles):
            particles.append ({
                "Ei": event_id,          # event ID  
                "in": i,                 # particle index
                "id": particle.id,       # particle ID  
                "st": particle.status,   # particle status    
                "m1": particle.mother1,  # particle mother 1
                "m2": particle.mother2,  # particle mother 2
                "c1": particle.color1,   # particle color 1
                "c2": particle.color2,   # particle color 2
                "px": particle.px,       # particle px
                "py": particle.py,       # particle py
                "pz": particle.pz,       # particle pz
                "E" : particle.e,        # particle energy
                "m" : particle.m,        # particle mass
                "ta": particle.lifetime, # particle lifetime
                "s" : particle.spin,     # particle spin
            })
        events.append (particles)    
    return events


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 


def sturges (N_events) :
    return ceil (1 + 3.322 * np.log (N_events))
    

