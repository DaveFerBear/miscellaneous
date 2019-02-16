try:
    import Tkinter as tk # Python 2
except:
    import tkinter as tk # Python 3

import math

def draw_new_circle(canvas, x, y, size=10, offset = 0):
    return canvas.create_oval(x+offset,y+offset,x+size+offset,y+size+offset,outline="orange",fill="blue")
    

def generate_path():
    NUM_STEPS = 800
    rads_per_step = 2*math.pi/NUM_STEPS
    freqs = [1, 10, 24, 50, 12]
    radii = [100, 50, 10, 3, 8]
    paths = [[0,0] for _ in xrange(NUM_STEPS)]
    
    for j in xrange(NUM_STEPS):
        cur_radian = 1.*j*rads_per_step
        for k in xrange(len(freqs)):
            paths[j][0] += radii[k] * math.sin(freqs[k] * cur_radian)
            paths[j][1] += radii[k] * math.cos(freqs[k] * cur_radian)

    return paths

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    x, y = None,None
    t = 0

    test_path = generate_path()
    print(test_path)

    def redraw(paths,t, x, y):
        if x and y:
            draw_new_circle(canvas, x, y, offset = 350)
        t += 1
        x = paths[t][0]
        y = paths[t][1]
        print('{},{}'.format(x,y))

        canvas.after(1, redraw, paths, t, x, y)

    canvas.after(100,redraw, test_path, t, x, y)
    root.mainloop()

