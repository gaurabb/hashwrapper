#!usr/bin/python
#Generate a random Salt value
#Get hash values in hexadecimal for supplied input
#Returns a dictionary with the hash and the salt
import hashlib
import uuid

def main():
	varToHash = raw_input("Enter the string to be hashed: ")
	varHashAlgo = raw_input("Enter: 1 for MD5 \n 2 for SHA1 \n 3 for SHA256 \n 4 for SHA384 \n 5 for SHA512 \n")
	saltValue = getSalt()
	#print ("SALT: " + saltValue)
	if 1 == int(varHashAlgo):
		dictRetValues={'hash':getMD5(varToHash + saltValue)}
	elif 2 == int(varHashAlgo):
		dictRetValues={'hash':getSHA1(varToHash + saltValue)}
	elif 3 == int(varHashAlgo):
		dictRetValues={'hash':getSHA256(varToHash + saltValue)}
	elif 4 == int(varHashAlgo):
		dictRetValues={'hash':getSHA384(varToHash + str(getSalt()))}
	elif 5 == int(varHashAlgo):
		dictRetValues={'hash':getSHA512(varToHash + saltValue)}
	else:
		print ("You entered: " + varHashAlgo + " but this is not an acceptable option. Run Again. Bye Bye.")
		dictRetValues={'Error':'1'}
		return  dictRetValues
	dictRetValues['salt']=saltValue
	print dictRetValues
	return dictRetValues
	
	
		
def getMD5(toHash):
	varMD5 = hashlib.md5(toHash).hexdigest()
	return varMD5

def getSHA1(toHash):
	varSHA1 = hashlib.sha1(toHash).hexdigest()
	return varSHA1
	
def getSHA256(toHash):
	varSHA256 = hashlib.sha256(toHash).hexdigest()
	return varSHA256
	
def getSHA384(toHash):
	varSHA384 = hashlib.sha384(toHash).hexdigest()
	return varSHA384
	
def getSHA512(toHash):
	varSHA512 = hashlib.sha512(toHash).hexdigest()
	return varSHA512
	
def getSalt():
	return str(uuid.uuid4())
	
if __name__ == '__main__':
	main()