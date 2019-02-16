try:
    import Tkinter as tk # Python 2
except:
    import tkinter as tk # Python 3

import math

def draw_new_circle(canvas, x, y, size=10, offset = 0):
    return canvas.create_oval(x+offset,y+offset,x+size+offset,y+size+offset,outline="white",fill="blue")
    

def generate_path(radius=100):
    NUM_STEPS = 200
    rads_per_step = 2*math.pi/NUM_STEPS
    freq = 1
    paths = [[0,0] for _ in xrange(NUM_STEPS)]
    print(paths)

    for j in xrange(NUM_STEPS):
        cur_radian = 1.*j*rads_per_step
        paths[j][0] = radius*math.sin(freq * cur_radian)
        paths[j][1] = radius*math.cos(freq * cur_radian)

    return paths

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()
    x, y = None,None
    t = 0

    test_path = generate_path()
    print(test_path)

    def redraw(paths,t, x, y):
        if x and y:
            draw_new_circle(canvas, x, y, offset = 200)
        t += 1
        x = paths[t][0]
        y = paths[t][1]
        print('{},{}'.format(x,y))

        canvas.after(10, redraw, paths, t, x, y)

    canvas.after(100,redraw, test_path, t, x, y)
    root.mainloop()

