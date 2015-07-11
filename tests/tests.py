## Default Python modules
import unittest
import sys

## Required Modules
from nose.tools import *

## Current project modules
from hashwrapper.hashwrapper import hashwrapper

class TestHashWrapper(unittest.TestCase):
	## Test that the generateHash function accept an input string and returns a string value containing the hash
	def test_can_create_hash(self):
		##Section to set up the test
		objGetHash = hashwrapper.HashWrapper()
		
		## Check >: Get the default hash algorithm currently set in config file
		default_hash_alg_in_config = 'sha256' # Hadcoded for the development settings
		self.assertEqual(objGetHash.getDefaultHashAlgorithm(), default_hash_alg_in_config)

		## Check >: Set the hash algorithm to use for the current cycle. If the change needs to be reflected 
		## in the config file, the value currently needs to be updated manually in the hashwrapper.config file.
		
		

		## Check >: Check that an hash Hex string is returned
		resultHash = objGetHash.generateHash("TestString")
		self.assertEqual(type(resultHash), str)

		## Fail Intentionally for now. So we get some message back when everything else passes
		self.fail('Finish everything!') 	

