import utils

'''
This API should be used to control all planetary motion.
Planets are purely data containers, and should not contain any logic.
'''
class Universe():
	def __init__(self, planets=None, G=1.):
		if type(planets) is not type({}):
			raise ValueError('Planets provided to universe are not in dict.')
		print('You have created a new universe!')
		self.planets = planets or {} # Key by planet name for faster deletion.
		self.G = G

	def add_planet(self, p):
		if p.name is None:
			print('Could not add planet (no name).')
			return
		self.planets[p.name] = p

	def run_sim(self, num_steps=100000, update_frequency=1000, save_history=True):
		# Create a map of update weights in memory.  This way we can update all planets at once
		# for a much more accurate simulation.
		force_map = {}
		for k in self.planets:
			force_map[k] = 0

		# TODO: This can be threaded for better performance.
		for n in xrange(num_steps):
			# How often the user should be updated (GUI or print).
			should_update = False
			if n%update_frequency == 0:
				should_update = True
				print('Current simulation: {0}%'.format(n*100./num_steps))

			# TODO: use combinations lib to find pairs (force is calculated 2x per pair).
			for k1,v1 in self.planets.iteritems():
				for k2,v2 in self.planets.iteritems():
					if k1 is not k2:
						dist_sq = utils.euclidean_distance_squared(v1.x, v1.y, v2.x, v2.y)
						if dist_sq == 0:
							force_map [k1] = (0., 0.)
						else:
							# Prevents 'result too large' errors.
							# TODO: Formalize max accleration/forces possible in universe.
							force_magnitude = min(self.G*v1.size*v2.size/dist_sq, 1e20) * .0000001
							fx = force_magnitude*(v2.x - v1.x)/dist_sq
							fy = force_magnitude*(v2.y - v1.y)/dist_sq
							force_map[k1] = (fx, fy)

			for planet_name,force_components in force_map.iteritems():
				# Update planet.
				p = self.planets[planet_name]
				p.ax = 0#force_components[0]*p.size
				p.ay = 0#force_components[1]*p.size
				p.vx += p.ax
				p.vy += p.ay
				p.x += p.vx
				p.y += p.vy

				if save_history: 
					p.pos_history.append((p.x, p.y))

				if should_update:
					v1.print_location()
		print('Simulation 100% complete.')


