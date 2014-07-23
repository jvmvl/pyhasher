#!/usr/bin/env python

import sys
import hashlib
import os

def newHash(hash,str):
	h = hashlib.new(hash)
	h.update(str)
	return h.hexdigest()
	
y=1
while y:
		_str=input("input :  ").encode('utf-8')
		print ('MD5       : ' + newHash('md5',_str))
		print ('SHA1      : ' + newHash('sha1',_str))
		print ('SHA256    : ' + newHash('sha256',_str))
		print ('SHA512    : ' + newHash('sha512',_str))
		print ('RipeMD160 : ' + newHash('ripemd160',_str))
		print ('Whirlpool : ' + newHash('whirlpool',_str))
		y=input("\n Again? (press enter to exit/Any key to continue) ")

os.system('exit')
