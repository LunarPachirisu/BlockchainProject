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
parser.add_argument('-c') # caseID
parser.add_argument('-i') # itemID
parser.add_argument('-r', '--reverse')
parser.add_argument('-n') # num_entries
parser.add_argument('-y', '--why') # reason
parser.add_argument('-o') # owner
args = parser.parse_args()

class bchoc:
	def __init__(self, previous_block_hash, timestamp, caseID, evidenceID, state, length, data):
		self.previous_block_hash = previous_block_hash
		self.timestamp = timestamp
		self.caseID = caseID
		self.evidenceID = evidenceID
		self.state = state
		self.length = length
		self.data = data
		
		self.block_data = struct.pack('32s d 16s I 12s I', previous_block_hash.encode('utf-8'), timestamp, caseID.encode('utf-8'), evidenceID, state.encode('utf-8'), length)
		self.block_hash = sha256(self.block_data).hexdigest()
		
	def test(self):
		print(sha256(self))




# creates an initial block
def create():
	data = 'Initial block\0'
	state = 'INITIAL'
	#datetime.utcnow().isoformat()
	initial_block = bchoc('', datetime.utcnow().timestamp(), '', 0, state, len(bytes(data, 'utf-8')), data)
	f = open(os.environ.get('BCHOC_FILE_PATH', 'test.txt'), 'w+b')
	f.close()

#if args.param == 'add':
#elif args.param == 'checkout':
#elif args.param == 'checkin':
#elif args.param == 'log':
#elif args.param == 'remove':
if args.param == 'init':
	t0 = Path(os.environ.get('BCHOC_FILE_PATH', 'test.txt'))
	if t0.is_file():
		if os.path.getsize(t0) >= 70:
			print('Blockchain file found with INITIAL block.')
		else:
			sys.exit('invalid file')
	else:
		print('Blockchain file not found. Created INITIAL block.')
		create()
#elif args.param == 'verify':
else:
	exit(1)

			
