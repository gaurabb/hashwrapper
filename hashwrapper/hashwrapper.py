import hashlib
import configparser

class HashWrapper:
	def generateHash(self,stringToHash):
		## Set the encoding for the input string
		toHash = stringToHash.encode('utf-8')
		# Calculate the MD5 hash
		varMD5 = hashlib.md5(toHash).hexdigest()
		return varMD5

	def getDefaultHashAlgorithm(self):
		objConfigParser = configparser.ConfigParser()
		objConfigParser.readfp(open(r'hashwrapper.config'))
		return objConfigParser.get('Default Settings','default_hash_Algorithm')	

	def setDefaultHashAlgorithm(self, hashAlgToUse):	
		algorithms_guaranteed= {'sha1', 'sha224', 'sha384', 'sha256', 'sha512', 'md5'}
		if hashAlgToUse in algorithms_guaranteed :
			return True
		return False

	def getDefaultSaltGenerator(self):
		objConfigParser = configparser.ConfigParser()
		objConfigParser.readfp(open(r'hashwrapper.config'))
		return objConfigParser.get('Default Settings','default_salt_generator')

