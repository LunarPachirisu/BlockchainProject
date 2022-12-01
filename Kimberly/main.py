#!/usr/bin/python3

from hashlib import sha256
import os
import sys
import uuid
import binascii
import struct
from pathlib import Path
from datetime import datetime, timezone
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('param') # add, checkout, checkin, log, remove, init, verify
parser.add_argument('-c', type=str) # caseID
parser.add_argument('-i', type=int, action = 'append') # itemID
parser.add_argument('-r', '--reverse')
parser.add_argument('-n', type=int) # num_entries
parser.add_argument('-y', '--why') # reason
parser.add_argument('-o') # owner
args = parser.parse_args()



path = os.environ.get('BCHOC_FILE_PATH')
if path == None:
	path = os.environ.get('BCHOC_FILE_PATH', 'test.bin')

k = open(path, 'wb+')




class bchoc:
	def __init__(self, previous_block_hash, timestamp, caseID, evidenceID, state, size=0, data=''):
		self.__previous_block_hash = previous_block_hash
		self.__timestamp = timestamp
		self.__caseID = caseID
		self.__evidenceID = evidenceID
		self.__state = state
		self.__size = size
		self.__data = data
		
		
	def bin(self):
		return struct.pack("32s d 16s I 12s I"+str(self.__size)+"s", self.__previous_block_hash.encode('utf-8'), self.__timestamp, self.__caseID.encode('utf-8'), self.__evidenceID, self.__state.encode('utf-8'), self.__size, self.__data.encode('utf-8'))

		



# creates an initial block
def create():
	data = 'Initial block'
	state = 'INITIAL'
	ts = datetime.utcnow().timestamp()
	#datetime.utcnow().isoformat()
	initial_block = bchoc('', ts, '', 0, state, 14, data)
	bi = k.write(initial_block.bin())
	print(bi)




if args.param == 'add':
	if (args.c == None or args.i == None):
		exit('incorrect args')
	caseID = args.c
	itemIDs = args.i
	
	ids = []
	for val in itemIDs:
		ids.append(str(val))
	if (len(ids) != len(set(ids))):
		exit(1)
	
	content = k.read()
	l = len(content)
	if l == 0:
		create()
	
	index = 76
	print(l)
	while index < l:
		print('ya')
		heada = content[index:index+76]
		print(heada)
		h, t, ci, ii, s, l = struct.unpack("32s d 16s I 12s I", heada)
		print(ii.encode('ascii'))
		ids.append(int(heada[56:59].encode('ascii')))
		if len(ids) != len(set(ids)):
			exit(1)
		index = index + 76
		print(index)
	
	
	

	for val in itemIDs:
		time = datetime.utcnow()
	
		print('Case: ' + caseID)
		print('Added item: ' + str(val))
		print('\tStatus: CHECKEDIN')
		print('\tTime of action: ' + time.isoformat())
		
		block = bchoc('', time.timestamp(), caseID, val, 'CHECKEDIN')
		k.write(block.bin())
		
		index = index + 76
elif args.param == 'log':
	rev = False if args.reverse == None else True
	num = 0 if args.n == None else args.n
	caseID = '' if args.c == None else args.c
	itemID = 0 if args.i == None else args.i
elif args.param == 'init':
	data = k.read()
	if len(data) == 0:
		create()
		print('Blockchain file not found. Created INITIAL block.')
	else:
		if data[60:67] == 'INITIAL'.encode('utf-8'):
			print('Blockchain file found with INITIAL block.')
		else:
			exit(1)
elif args.param == 'verify':
	data = k.read()
	i = 0
	size = 1
	if data[60:67] != 'INITIAL'.encode('utf-8'):
		exit(1)
	if (size ==1 and data[60:67] != 'INITIAL'.encode('utf-8')):
		exit(1)
	while i < len(data):
		if data[60:67] == 'INITIAL'.encode('utf-8') or data[60:69] == 'CHECKEDIN'.encode('utf-8') or data[60:70] == 'CHECKEDOUT'.encode('utf-8') or data[60:68] == 'RELEASED'.encode('utf-8'):
			pass
		else:
			exit(1)
else:
	exit(1)
'''
elif args.param == 'checkout':
	if args.i == None:
		exit('incorrect args')
	itemID = args.i
'''
'''
elif args.param == 'checkin':
	if args.i == None:
		exit('incorrect args')
	itemID = args.i
'''
'''
elif args.param == 'log':
	rev = False if args.r == None else True
	num = 0 if args.n == None else args.n
	caseID = '' if args.c == None else args.c
	itemID = 0 if args.i == None else args.i
	
	
	vals = []
	
	vals.append('Case: ' + caseID + '\nItem: ' + str(itemIDs[index]) + '\nAction: CHECKEDIN\nTime: ' + time)
'''
'''
elif args.param == 'remove':
	if (args.c == None or args.y == None):
		exit('incorrect args')
	itemID = args.i
	reason = args.y
	owner = '' if args.o == None else args.o
'''

#elif args.param == 'verify':


	


y = '''
t0 = ""

commands = 
	add
	checkout
	checkin
	log
	remove
		init
	verify
	-c case_id
	-i item_id
	-r, --reverse
	-n num_entries
	-y reason, --why reason
	-o owner
	

# calculates sha256
#def hash(self):


# creates an initial block
def create():
	data = 'Initial block\0'
	state = 'INITIAL'
	#datetime.utcnow().isoformat()
	initial_block = bchoc('', datetime.utcnow().timestamp(), '', 0, state, len(bytes(data, 'utf-8')), data)
	f = open(os.environ.get('BCHOC_FILE_PATH', 'test.txt'), 'w+b')
	f.close()
	

if len(sys.argv) == 2:
	if sys.argv[1] == 'init':
		t0 = Path(os.environ.get('BCHOC_FILE_PATH', 'test.txt'))
		if t0.is_file():
			if os.path.getsize(t0) >= 70:
				print('Blockchain file found with INITIAL block.')
			else:
				sys.exit('invalid file')
		else:
			print('Blockchain file not found. Created INITIAL block.')
			create()
			
	#elif sys.argv[1] == 'verify':
	
else:
	check = 1
	if sys.argv[check] == 'add':
		check = 2
		if Path(os.environ.get('BCHOC_FILE_PATH', 'test.txt')).is_file() == False:
			create()
		if sys.argv[check] != '-c':
			sys.exit('didn\'t include -c')
		if len(sys.argv) < 6:
			sys.exit('not long enough for add')
		print(os.environ.get('BCHOC_FILE_PATH'))
		check = 3
		caseID = sys.argv[check]
		check = 4
		if sys.argv[check] != '-i':
			sys.exit('didn\'t include -i')
		
		k = open(os.environ.get('BCHOC_FILE_PATH'), 'rb')
		content = k.read()
		print(content)
		#data = 
	
	
	else: sys.exit(1)
	'''



k.close()
			
