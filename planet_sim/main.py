from planet import Planet
from universe import Universe
from arena import Arena

if __name__ == '__main__':
	p1 = Planet(pos=[60,70], name='p1', size=40)
	p1.print_location()
	p2 = Planet(pos=[150,296], name='p2', size=20)
	p2.print_location()
	planet_map = {'p1': p1, 'p2': p2}
	u = Universe(planets=planet_map)
	u.run_sim(
			save_history=True,
			num_steps=1000)

	arena = Arena(u)
	arena.setup_universe()
	arena.animate_universe_history(frame_delay_ms=1)
