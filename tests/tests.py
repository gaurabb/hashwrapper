## Default Python modules
import unittest
import sys
import hashlib

## Required Modules
from nose.tools import *

## Current project modules
from hashwrapper.hashwrapper import hashwrapper

class TestHashWrapper(unittest.TestCase):
	## Test that the generateHash function accept an input string and returns a string value containing the hash
	def test_hash_wrapper(self):
		##Section to set up the test
		objGetHash = hashwrapper.HashWrapper()
		
		## Check >: Get the default hash algorithm currently set in config file
		default_hash_alg_in_config = 'sha256' # Hadcoded for the development settings
		self.assertEqual(objGetHash.getDefaultHashAlgorithm(), default_hash_alg_in_config)

					
		## Check >: Get the default random salt generator for the hash algorithm currently set in config file
		default_salt_generator_used = 'uuid.uuid4()' # Hadcoded for the development settings
		self.assertEqual(objGetHash.getDefaultSaltGenerator(), default_salt_generator_used)

		## Check >: Check that a dictionary is returned
		resultHash = objGetHash.generateHash("TestString", "")
		print(resultHash)
		self.assertEqual(type(resultHash), dict)

		## Note> If the change needs to be reflected 
		## in the config file, the value currently needs to be updated manually in the hashwrapper.config file.
		## Check that hash and salt us returned for each algorithm in hashlib.algorithms_guaranteed
		hash_alg_to_use_for_current_cycle = 'sha512' # Hadcoded for the development settings; should be supplied runtime
		for hash_alg_to_use_for_current_cycle in hashlib.algorithms_guaranteed:
			print(hash_alg_to_use_for_current_cycle)
			resultHash = objGetHash.generateHash("TestString", hash_alg_to_use_for_current_cycle)
			print(resultHash)
			self.assertEqual(type(resultHash), dict)

		## Fail Intentionally for now. So we get some message back when everything else passes
		self.fail('Finish everything!') 	

