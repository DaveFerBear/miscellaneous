m1 = .002384
m2 = .001287
wd = 6.25

def get_k(wn):
	return m1*m2*(wn**2)/(m1+m2)

def get_wn(zeta):
	return wd/(1-zeta**2)**0.5

wn = get_wn(.05)

print get_k(wn)
