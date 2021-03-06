import random

'''
This class is purely a data container.
'''
class Planet():
	def __init__(self, pos=[None,None], vel=[None,None], name=None, size=None):
		if len(pos) != 2:
			raise ValueError('Only 2D space currently supported.')

		# Miscellaneous member variables.
		self.name = name or 'Unknown Planet'
		self.size = size or random.random()

		# Real time position related variables.
		self.x = pos[0] or random.random()
		self.y = pos[1] or random.random()
		self.vx = vel[0] or 0. # By default planets start at rest.
		self.vy = vel[1] or 0.
		self.ax = 0.
		self.ay = 0.

		# Motion history.
		# TODO: Write to file, no need to store this is memory.
		self.pos_history = []

	def print_location(self):
		print('{n} position: ({x},{y})'.format(n=self.name, x=self.x, y=self.y))