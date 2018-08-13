from planet import Planet
from universe import Universe
from arena import Arena

if __name__ == '__main__':
	p1 = Planet(pos=[120,140], name='p1', size=40)
	p1.print_location()
	p2 = Planet(pos=[200,160], name='p2', size=20)
	p2.print_location()
	planet_map = {'p1': p1, 'p2': p2}
	u = Universe(planets=planet_map)
	# u.run_sim()

	arena = Arena(u)
	arena.setup_universe()
	for t in xrange(100):
		u.run_sim(num_steps=1)
		arena.update_planets()
