from planet import Planet
from universe import Universe
from arena import Arena

if __name__ == '__main__':
	p1 = Planet(pos=[20,40], name='p1', size=10)
	p1.print_location()
	p2 = Planet(pos=[1,3], name='p2', size=40)
	p2.print_location()
	planet_map = {'p1': p1, 'p2': p2}
	u = Universe(planets=planet_map)
	# u.run_sim()

	arena = Arena(u)
	#arena.test_gui()
	arena.setup_universe_gui()