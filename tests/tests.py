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
		##Set up the test
		objGetHash = hashwrapper.HashWrapper()
		
		## Check that an hash Hex string is returned
		resultHash = objGetHash.generateHash("TestString")
		self.assertEqual(type(resultHash), str)

		## Fail Intentionally for now. So we get some message back when everything else passes
		self.fail('Finish everything!') 	

