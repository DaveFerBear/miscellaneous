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


def generate_fourier_path(freqs, radii):
    NUM_STEPS = 360
    rads_per_step = 2*math.pi/NUM_STEPS
    path = [[0,0] for _ in xrange(NUM_STEPS)]
    
    for j in xrange(NUM_STEPS):
        cur_radian = 1.*j*rads_per_step
        for k in xrange(len(freqs)):
            path[j][0] += radii[k] * math.sin(freqs[k] * cur_radian)
            path[j][1] += radii[k] * math.cos(freqs[k] * cur_radian)

    return path