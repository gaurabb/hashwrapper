import hashlib
import configparser
import uuid

class HashWrapper:
	def getDefaultHashAlgorithm(self):
		objConfigParser = configparser.ConfigParser()
		objConfigParser.readfp(open(r'hashwrapper.config'))
		return objConfigParser.get('Default Settings','default_hash_Algorithm')	

	def setDefaultHashAlgorithm(self, hashAlgToUse):	
		## hashlib.algorithms_guaranteed= {'sha1', 'sha224', 'sha384', 'sha256', 'sha512', 'md5'}
		if hashAlgToUse in hashlib.algorithms_guaranteed:
			return True
		return False

	def getDefaultSaltGenerator(self):
		objConfigParser = configparser.ConfigParser()
		objConfigParser.readfp(open(r'hashwrapper.config'))
		return objConfigParser.get('Default Settings','default_salt_generator')

	def getHash(self, toHash, hashName):
		## Get Salt
		cur_Salt = self.getSalt()
		
		if hashName == 'sha1':
			## Generate the hash
			varHash = hashlib.sha1(toHash).hexdigest()
		elif hashName == 'sha224':
			## Generate the hash
			varHash = hashlib.sha224(toHash).hexdigest()
		elif hashName == 'sha384':
			## Generate the hash
			varHash = hashlib.sha384(toHash).hexdigest()
		elif hashName == 'sha256':
			## Generate the hash
			varHash = hashlib.sha256(toHash).hexdigest()
		elif hashName == 'md5':
			## Generate the hash
			varHash = hashlib.md5(toHash).hexdigest()
		else:
			varHash = "Error Generating the hash value"
		## Build the dictionary to return
		resDict = {'hash': varHash, 'salt': cur_Salt}
		return resDict 

	def generateHash(self,stringToHash, hashAlg):
		## Define a Dict to hold the return value
		hashAndSaltDict = dict
		## Validations for stringToHash
		if stringToHash is not None:
			## Set the encoding for the input string
			toHash = stringToHash.encode('utf-8')
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

