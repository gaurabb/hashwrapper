# hashwrapper

A small Python wrapper around `hashlib` that generates a salted hash of a string.
This repository is being modernized; the current API retains its legacy behavior.

## Usage

Run from the repository root so `hashwrapper.config` is available:

```python
from hashwrapper.hashwrapper import HashWrapper

wrapper = HashWrapper()
result = wrapper.generateHash("hello", "sha256")
print(result["hash"])
print(result["salt"])

print(wrapper.getDefaultHashAlgorithm())  # sha256
print(wrapper.getDefaultSaltGenerator())  # uuid.uuid4()
```

The input and a newly generated UUID4 salt are encoded as UTF-8. The returned
hex digest hashes `input + salt`; the result is a dictionary with `hash` and
`salt` strings. Repeated calls generate different salts and therefore different
hashes.

`generateHash` accepts fixed-length algorithms in `hashlib.algorithms_guaranteed`.
An empty or unknown algorithm name falls back to the configured default.
SHAKE algorithms require an output length and are not supported by this API.
`getHash` rejects unknown algorithm names directly.

## Current limitations

- Configuration is read from `hashwrapper.config` in the working directory.
- Salt generation always uses UUID4; the salt-generator setting is informational.
- Callers must supply a string and an algorithm name. Legacy `None` handling
  returns the `dict` type instead of a result and should not be relied upon.
- There is no password verification, file hashing, or command-line interface yet.
- Salted general-purpose hashes are not a dedicated password-storage scheme.

## Development

The baseline tests use only Python's standard library. From the repository root:

```sh
python3 -m unittest discover -s tests -v
```

Tests cover fixed-length algorithms, UTF-8 and empty inputs, random salts,
legacy algorithm fallback, and explicit errors for unsupported algorithms.

Packaging and CI modernization, a deterministic hashing API, file verification,
and a command-line interface are planned for subsequent phases.
