import math

def generate_fourier_path(freqs, radii):
    NUM_STEPS = 1000
    rads_per_step = 2*math.pi/NUM_STEPS
    paths = [[0,0] for _ in xrange(NUM_STEPS)]
    
    for j in xrange(NUM_STEPS):
        cur_radian = 1.*j*rads_per_step
        for k in xrange(len(freqs)):
            paths[j][0] += radii[k] * math.sin(freqs[k] * cur_radian)
            paths[j][1] += radii[k] * math.cos(freqs[k] * cur_radian)

    return paths