#Peter Mastropaolo (pjm8331)

#Only adds lines that include ICMP and Echo in them to the new NodeX_filtered.txt file

def filter(filename):


	f = open(filename, 'r')
	line = f.readline().strip()

	newfn = filename.strip(".txt")  + "_filtered.txt" 

	fw = open(newfn, 'w')

	for line in f.readlines():
		if "ICMP" in line:
			fw.write(line)

	f.close()
	fw.close()