import sys

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: line.replace('\n','').split(" "), f.readlines())

def main(input):
	for case in parse_file_info(input):
		print(' '.join(map(lambda x: x[-1]+x[1:-1]+x[0],case)))

if __name__ == '__main__':
	main(sys.argv[1])