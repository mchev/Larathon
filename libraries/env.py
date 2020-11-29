# Env function will parse the .env file and return the value asked
def env(label):
	filepath = '.env'
	env = {}
	with open(filepath) as fp:
		line = fp.readline()
		while line:
			splitted = line.split('=')
			if splitted[0] == label :
				return splitted[1].replace('\n', '').replace('\r', '')
			else :
				line = fp.readline()