import hashlib
import configparser
import uuid

class HashWrapper:
	def getDefaultHashAlgorithm(self):
		''' Function to get the default hashing algorithm from the config file '''
		objConfigParser = configparser.ConfigParser()
		with open('hashwrapper.config') as config_file:
			objConfigParser.read_file(config_file)
		return objConfigParser.get('Default Settings','default_hash_Algorithm')	

	def getDefaultSaltGenerator(self):
		''' Function to get the default salt generator from the config file '''
		objConfigParser = configparser.ConfigParser()
		with open('hashwrapper.config') as config_file:
			objConfigParser.read_file(config_file)
		return objConfigParser.get('Default Settings','default_salt_generator')

	def getHash(self, stringToHash, hashName):
		''' Function to generate the hash value for the given string using the specified hashing algorithm
			Parameters:
				stringToHash: The plain text string for which the hash value needs to be generated
				hashName: The hashing algorithm to be used for generating the hash value
			Returns:
				Dictionary with the hash value and the salt used for generating the hash value'''
		## Set the encoding for the input string
		toHash = stringToHash.encode('utf-8')			
		## Get Salt
		cur_Salt = self.getSalt().encode('utf-8')
		## Generate the hash after concatenating the plaint text string with the salt string
		if hashName not in hashlib.algorithms_guaranteed:
			raise ValueError(f"Unsupported hash algorithm: '{hashName}'. Must be one of: {hashlib.algorithms_guaranteed}")
		hasher = hashlib.new(hashName, toHash + cur_Salt)
		if hasher.digest_size == 0:
			raise ValueError("Hash algorithm requires an explicit digest length: " + hashName)
		varHash = hasher.hexdigest()
		## Build the dictionary to return
		resDict = {'hash': varHash, 'salt': cur_Salt.decode("utf-8")}
		return resDict 

	def generateHash(self,toHash, hashAlg):
		''' Function to generate the hash value for the given string using the specified hashing algorithm
			Parameters:
				toHash: The plain text string for which the hash value needs to be generated
				hashAlg: The hashing algorithm to be used for generating the hash value
			Returns:
				Dictionary with the hash value and the salt used for generating the hash value'''
		## Define a Dict to hold the return value
		hashAndSaltDict = dict
		## Validations for stringToHash
		if toHash is not None:
			## Validations for hashAlg
			if hashAlg is not None:
				if hashAlg in hashlib.algorithms_guaranteed:
					## Use the user provided algorithm for generating the hash for the current pass
					hashAndSaltDict = self.getHash(toHash,hashAlg)
				else:
					## Use the default algorithm for generating the hash for the current pass
					hashAndSaltDict = self.getHash(toHash,self.getDefaultHashAlgorithm())
		return hashAndSaltDict	
						
	def getSalt(self):
		return str(uuid.uuid4())

