import sys
from functools import reduce

def parse_file_info(filename):
	with open(filename,'r') as f:
		return map(lambda line: line.replace('\n','').split(" "), f.readlines())

def main(input):
	for case in parse_file_info(input):
		print(reduce(lambda x,y: x if len(x)>=len(y) else y, case))
			
if __name__ == '__main__':
	main(sys.argv[1])