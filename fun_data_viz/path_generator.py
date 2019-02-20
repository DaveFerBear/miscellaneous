import math

'''
Container object for facilitating creation/deletion of paths.
'''
class Path(object):
    def __init__(self, canvas):
        self.canvas = canvas # Need a reference to canvas for objection deletion.
        self.objects = []
    
    def add_object(self, obj):
        self.objects.append(obj)
    
    def __del__(self):
        print('Attemping deletion of path.')
        for o in self.objects:
            self.canvas.delete(o)


def generate_fourier_pathc(freqs, radii):
    NUM_STEPS = 1000
    rads_per_step = 2*math.pi/NUM_STEPS
    paths = [[0,0] for _ in xrange(NUM_STEPS)]
    
    for j in xrange(NUM_STEPS):
        cur_radian = 1.*j*rads_per_step
        for k in xrange(len(freqs)):
            paths[j][0] += radii[k] * math.sin(freqs[k] * cur_radian)
            paths[j][1] += radii[k] * math.cos(freqs[k] * cur_radian)

    return paths