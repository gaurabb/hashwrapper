import hashlib
import ConfigParser

class HashWrapper:
	def generateHash(self,stringToHash):
		## Set the encoding for the input string
		toHash = stringToHash.encode('utf-8')
		# Calculate the MD5 hash
		varMD5 = hashlib.md5(toHash).hexdigest()
		return varMD5

	def getDefaultHashAlgorithm(self):
		objConfigParser = ConfigParser.ConfigParser()
		objConfigParser.readfp(open(r'hashwrapper.config'))
		return objConfigParser.get('Default Settings','selected_hash_Algorithm')		

