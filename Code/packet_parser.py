#Peter Mastropaolo (pjm8331)
#Teo Luciani (ttl5052)
#Returns a list of lists
#Each line of the filtered file is split into a list by the delimiter (' ') and added to the master list

def parse(filename):
	
	packetlist = []

	f = open(filename, 'r')

	for line in f.readlines():
		listline = line.split()
		packetlist.append(listline)

	f.close()
	return packetlist

