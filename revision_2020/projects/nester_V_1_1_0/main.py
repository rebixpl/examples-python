import nester
cast = ['Palin', 'Cleese', ['Idle',['Gilliam', 'Chapman'], 'Jones'], 'Gilliam', 'Chapman']
nester.print_lol(cast, True, 0)
# nester.print_lol(cast, 2) # it works 
# nester.print_lol(cast) # it works too, because of default 0 argument

""" OUTPUT:
Palin
Cleese
	Idle
		Gilliam
		Chapman
	Jones
Gilliam
Chapman
"""