#bf.py

'''
A brainfuck interpreter

WRHM
31 Jul 2015

Last edit: 27 Apr 2016

SYNTAX
>	increment the data pointer.
<	decrement the data pointer.
+	increment the byte at the data pointer.
-	decrement the byte at the data pointer.
.	output the byte at the data pointer.
,	accept one byte of input, and store at the data pointer.
[	begin loop, if current byte is not zero.
]	end loop.
'''

import sys

NUMCELLS = 20
BITSPERCELL = 16#8
CELLMINVAL = -(2**(BITSPERCELL-1))
CELLMAXVAL = (2**(BITSPERCELL-1))-1

memory = [0]*NUMCELLS

VERBOSE = False
# print sys.argv
# exit()
try:
	f = open(sys.argv[1],'r')
	program = ''.join([x for x in ''.join(f.readlines()) if x in '><+-.,[]'])
	f.close()
	if len(sys.argv)>2:
		VERBOSE = 't' in sys.argv[2] or 'T' in sys.argv[2]
except Exception, e:
	print 'Error: please use filename as argument.'
	exit()

programLength = len(program)
programPos = 0
cellPos = 0

EXIT = False

# resultString = ""

def dispMemPos():
	print memory
	s = str(memory)
	i = 0
	if cellPos == NUMCELLS-1:
		i = s.index(']')
	else:
		for j in xrange(cellPos+1):
			i += 1
			while s[i] != ',':
				i += 1
	print '%s^ (%d)'%(' '*(i-1),cellPos)

if VERBOSE:
	dispMemPos()
while programPos < programLength:
	# raw_input()
	instruction = program[programPos]
	
	if VERBOSE:
		print '\n%sv\n%s'%(' '*programPos,program)

	if instruction == '>':
		programPos += 1
		cellPos += 1
		if cellPos >= NUMCELLS:
			print 'Error: out of bounds (HIGH)'
			EXIT = True
			break
	elif instruction == '<':
		programPos += 1
		cellPos -= 1
		if cellPos < 0:
			print 'Error: out of bounds (LOW)'
			EXIT = True
			break
	elif instruction == '+':
		programPos += 1
		memory[cellPos] += 1
		if memory[cellPos] > CELLMAXVAL:
			memory[cellPos] = CELLMINVAL
	elif instruction == '-':
		programPos += 1
		memory[cellPos] -= 1
		if memory[cellPos] < CELLMINVAL:
			memory[cellPos] = CELLMAXVAL
	elif instruction == '.':
		programPos += 1
		print 'OUTPUT CHAR: %s'%chr(memory[cellPos])
		# resultString += chr(memory[cellPos])
	elif instruction == ',':
		programPos += 1
		memory[cellPos] = ord(raw_input('INPUT CHAR: ')[0])
	elif instruction == '[':
		if memory[cellPos] == 0:
			c = 1
			while c>0:
				programPos += 1
				if program[programPos] == ']':
					c -= 1
				elif program[programPos] == '[':
					c += 1 
		
		programPos += 1
	else:
		c = 1
		while c>0:
			programPos -= 1
			if program[programPos] == ']':
				c += 1
			elif program[programPos] == '[':
				c -= 1
	
	if VERBOSE:
		dispMemPos()
	
	if EXIT:
		break

# print 'RESULT_STRING:\n%s'%resultString
# dispMemPos()