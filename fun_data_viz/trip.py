try:
    import Tkinter as tk # Python 2
except:
    import tkinter as tk # Python 3

import path_generator as pg

def draw_new_circle(canvas, x, y, size=10, offset = 0):
    return canvas.create_oval(x+offset,y+offset,x+size+offset,y+size+offset,outline="orange",fill="blue")

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    x, y = None,None
    t = 0
    
    freqs = [1, 5, 13, 21]
    radii = [100, 50, 15, 15]

    test_path = pg.generate_fourier_path(freqs, radii)

    def redraw(paths,t, x, y):
        if x and y:
            draw_new_circle(canvas, x, y, offset = 350)
        
        if (t < len(paths)-1):
            t += 1
            x = paths[t][0]
            y = paths[t][1]
            canvas.after(1, redraw, paths, t, x, y)

    canvas.after(100,redraw, test_path, t, x, y)
    root.mainloop()

