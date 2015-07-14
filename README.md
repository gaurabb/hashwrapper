# hashwrapper
Provides a wrapper around hashing methods [hashlib](https://docs.python.org/3.4/library/hashlib.html)

## External packages used
For Tests: [nose](https://nose.readthedocs.org/en/latest/)

# Installation


# Usage

#### Import
To use the hashing function, import the module:
```python
from hashwrapper.hashwrapper import hashwrapper
:::::::
objGetHash = hashwrapper.HashWrapper()
::::::
```
#### Generate a hash
To get a hash and the salt value:
```python
:::::
resultHash = objGetHash.generateHash(string_to_hash, hash_alg_to_use_for_current_cycle)
:::::
```
#### Default hash algorithm
To check the default hash function setting in the configuration:
```python
:::::
default_hash_in_config = objGetHash.getDefaultHashAlgorithm()
:::::
```
#### Default salt|IV generator
To check the default salt generation function setting in the configuration:
```python
:::::
default_salt_in_config = objGetHash.getDefaultSaltGenerator()
:::::
```



