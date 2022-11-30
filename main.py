#!/usr/bin/python3

import hashlib
import os
import sys
import uuid
import binascii
import struct
from pathlib import Path
from datetime import datetime

class bchoc:
	def init(self, previous_block_hash, timestamp, caseID, evidenceID_list, state, length, data):
		self.previous_block_hash = previous_block_hash
		self.timestamp = timestamp
		self.caseID = caseID
		self.evidenceID_list = evidenceID_list
		self.state = state
		self.length = length
		self.data = data
		
		self.block_data = struct.pack('32s d 16s I 12s I', previous_block_hash.encode('utf-8'), timestamp, caseID.encode('utf-8'), evidenceID_list, state.encode('utf-8'), length)
		self.block_hash = hashlib.sha256(self.block_data).hexdigest()
		

t0 = ""


if (sys.argv[1]=='init' and len(sys.argv)<3):
	t0 = Path(os.environ.get('BCHOC_FILE_PATH', 'test.txt'))
	if t0.is_file():
		t1 = os.path.getsize(t0)
		if t1>70:
			k = open(t0, 'rb')
			content = k.read()
			print('the content of text file is ', content)
			print('Blockchain file found with INITIAL block.')
		else:
			sys.exit(1)
	else:
		print('Blockchain file not found. Created INITIAL block.')
		data = 'Initial block\0'
		state = 'INITIAL'
		statepaded = state.ljust(12, '\0')
		initial_block = bchoc('', datetime.now().timestamp(), '', 0, statepaded, len(data), data)
		f = open(os.environ.get('BCHOC_FILE_PATH', 'test.txt'), 'w+b')
		print(len(data))
		print(binascii.hexlify(initial_block.block_data))
		f.close()
elif sys.argv[1] == 'add':
	k = open(os.environ.get('BCHOC_FILE_PATH'), 'rb')
	content = k.read()
	data = ''
else:
	sys.exit(1)
			
			
