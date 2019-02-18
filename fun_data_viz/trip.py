import Tkinter as tk # Python 2
import path_generator as pg

def draw_new_circle(canvas, x, y, size=10, offset = 0):
    return canvas.create_oval(x+offset, y+offset, x+size+offset, y+size+offset,outline='orange', fill='blue')

def draw_path(canvas, path):
    p = pg.Path(canvas)
    x, y = None, None
    t = 0

    def redraw(paths,t, x, y):
        if x and y:
            circle = draw_new_circle(canvas, x, y, offset = 350)
            p.add_object(circle)
        
        if (t < len(paths)-1):
            t += 1
            x = paths[t][0]
            y = paths[t][1]
            canvas.after(1, redraw, paths, t, x, y)
        else:
            return

    canvas.after(100,redraw, test_path, t, x, y)
    return p

if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()

    freqs = [1, 5, 13, 21]
    radii = [100, 50, 15, 15]
    test_path = pg.generate_fourier_path(freqs, radii)

    p = draw_path(canvas, test_path)
    del p

    root.mainloop()

