import Tkinter as tk # Python 2
import path_generator as pg
import random

def get_rand_color():
    colors = ['red', 'blue', 'orange', 'green', 'yellow']
    i = int(random.random()*len(colors))
    return colors[i]

def draw_new_circle(canvas, x, y, size=10, outline = 'blue', fill = 'orange', offset = 0):
    return canvas.create_oval(x+offset, y+offset, x+size+offset, y+size+offset, outline=outline, fill=fill)

def draw_path(canvas, path, fill='orange', outline='blue'):
    p = pg.Path(canvas)
    x, y = None, None
    t = 0

    def redraw(path,t, x, y):
        if x and y:
            circle = draw_new_circle(canvas, x, y, fill=fill, outline=outline, offset = 350)
            p.add_object(circle)

        if (t < len(path)-1):
            t += 1
            x = path[t][0]
            y = path[t][1]
            canvas.after(1, redraw, path, t, x, y)
        else:
            return

    canvas.after(100,redraw, path, t, x, y)
    return p

if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()

    freqs, radii, paths = [], [], []

    # Path One
    freqs.append([1, 5, 13, 21])
    radii.append([100, 50, 15, 15])

    # Path Two
    freqs.append([21, 5, 13])
    radii.append([10, 50, 15])

    # Path Three
    freqs.append([20, 24])
    radii.append([200, 100])

    for i,f in enumerate(freqs):
        paths.append(pg.generate_fourier_path(freqs[i], radii[i]))

    for p in paths:
        draw_path(canvas, p, fill=get_rand_color())

    # del p TODO: fix this deletion code.
    root.mainloop()

