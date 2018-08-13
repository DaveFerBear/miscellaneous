try:
	import Tkinter as tk # Python 2
except:
	import tkinter as tk # Python 3
import utils

'''
An arena handles all GUI logic, rendering the output of the universe.
They can be run on seperate threads, in real time or on saved data.

A design decision was made to allow this class to have dependencies on the universe.
I may live to regret it.
'''
class Arena():
	def __init__(self, universe, width=400, height=400):
		self.root = tk.Tk()
		self.universe = universe
		self.canvas = tk.Canvas(self.root,width=width,height=height)
		self.canvas.pack()

	def setup_universe(self):
		self.planet_map = {}
		for name,planet in self.universe.planets.iteritems():
			self.planet_map[name] = self.canvas.create_oval(
					planet.x, planet.y,
					planet.x+planet.size,
					planet.y+planet.size,
					outline="white", fill=utils.random_tkinter_color())
		self.root.mainloop()

	def update_planets(self):
		for name,circle in self.planet_map.iteritems():
			p = self.universe.planets[name]
			p_coords = self.canvas.coords(circle)
			self.canvas.move(self.circle, p.x-p_coords[0], p.y-p_coords[1])
		self.root.mainloop()


	# This can be used to verify the GUI will output what is expected.
	def test_gui(self):
		circle = self.canvas.create_oval(50,50,20,80,outline="white",fill="blue")
		def redraw():
		   self.canvas.after(100,redraw)
		   self.canvas.move(circle,2,2)
		self.canvas.after(100,redraw)
		self.root.mainloop()
