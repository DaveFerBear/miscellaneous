try:
	import Tkinter as tk # Python 2
except:
	import tkinter as tk # Python 3
import utils
import random

'''
An arena handles all GUI logic, rendering the output of the universe.
They can be run on seperate threads, in real time or on saved data.

A design decision was made to allow this class to have dependencies on the universe.
I may live to regret it.
'''
class Arena():
	def __init__(self, universe, width=400, height=400, name='Planet Sim'):
		self.root = tk.Tk()
		self.root.title(name)
		self.universe = universe
		self.canvas = tk.Canvas(self.root, width=width, height=height)
		self.canvas.pack()

	def setup_universe(self):
		self.planet_map = {}
		for name,planet in self.universe.planets.iteritems():
			self.planet_map[name] = self.canvas.create_oval(
					planet.x, planet.y,
					planet.x+planet.size,
					planet.y+planet.size,
					outline="white", fill=utils.random_tkinter_color())

	# Animates planet position history. How cool is this function name?
	def animate_universe_history(self):
		# Sanity check - the planets must have the same length history.
		planet_histories = set([len(v.pos_history) for k,v in self.universe.planets.iteritems()])
		if len(planet_histories) is not 1:
			raise ValueError('Non-uniform planet histories.')
		if 0 in planet_histories:
			raise ValueError('This universe has no history.  Try runnnig a simulation first?')

		self.time_left = list(planet_histories)[0]
		print('Simulation History Length: {t}'.format(t=self.time_left))

		def redraw():
			if self.time_left > 0:
				self.canvas.after(400, redraw)
				self.time_left = self.time_left-1
				for name,circle in self.planet_map.iteritems():
					p = self.universe.planets[name]
					self.canvas.move(circle, p.pos_history[self.time_left][0], p.pos_history[self.time_left][1])
		self.canvas.after(400, redraw)
		self.root.mainloop()


	# TODO: There are some issues with this realtime implementation.
	# The best solution is probably threaded with both universe and arena
	# writing to some shared and protected data structure.
	def update_planets_realtime(self):
		for name,circle in self.planet_map.iteritems():
			p = self.universe.planets[name]
			p_coords = self.canvas.coords(circle)
			self.canvas.move(circle, p.x-p_coords[0], p.y-p_coords[1])
		self.root.mainloop()

	# This can be used to verify the GUI will output what is expected.
	def test_gui(self, num_steps=50):
		self.steps_left = num_steps
		circle = self.canvas.create_oval(180, 180, 200, 200, outline="white", fill="blue")
		def redraw():
			if self.steps_left > 0:
				self.canvas.after(100, redraw)
				self.steps_left = self.steps_left-1
				self.canvas.move(circle, random.random()*6-3., random.random()*6.-3)
		self.canvas.after(100, redraw)
		self.root.mainloop()
