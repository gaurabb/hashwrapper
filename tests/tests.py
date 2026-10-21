"""Regression tests for the legacy salted hashing API."""

import hashlib
import unittest
from unittest.mock import patch
import uuid

from hashwrapper.hashwrapper import HashWrapper


class TestHashWrapper(unittest.TestCase):
    def setUp(self):
        self.wrapper = HashWrapper()

    def test_configured_defaults(self):
        self.assertEqual(self.wrapper.getDefaultHashAlgorithm(), "sha256")
        self.assertEqual(self.wrapper.getDefaultSaltGenerator(), "uuid.uuid4()")

    def test_fixed_length_algorithms(self):
        for algorithm in sorted(hashlib.algorithms_guaranteed):
            if hashlib.new(algorithm).digest_size == 0:
                continue
            with self.subTest(algorithm=algorithm):
                result = self.wrapper.generateHash("TestString", algorithm)
                expected = hashlib.new(
                    algorithm, ("TestString" + result["salt"]).encode("utf-8")
                ).hexdigest()
                self.assertEqual(result["hash"], expected)
                self.assertEqual(uuid.UUID(result["salt"]).version, 4)

    def test_unicode_and_empty_strings(self):
        for value in ("", "hello 🌏", "café"):
            with self.subTest(value=value), patch.object(
                self.wrapper, "getSalt", return_value="fixed-salt"
            ):
                result = self.wrapper.generateHash(value, "sha256")
                self.assertEqual(
                    result["hash"],
                    hashlib.sha256((value + "fixed-salt").encode("utf-8")).hexdigest(),
                )

    def test_each_call_gets_a_new_salt(self):
        first = self.wrapper.generateHash("hello", "sha256")
        second = self.wrapper.generateHash("hello", "sha256")
        self.assertNotEqual(first["salt"], second["salt"])
        self.assertNotEqual(first["hash"], second["hash"])

    def test_unknown_algorithm_uses_configured_default(self):
        for algorithm in ("", "unknown"):
            with self.subTest(algorithm=algorithm), patch.object(
                self.wrapper, "getSalt", return_value="fixed-salt"
            ):
                self.assertEqual(
                    self.wrapper.generateHash("hello", algorithm),
                    self.wrapper.generateHash("hello", "sha256"),
                )

    def test_get_hash_rejects_unknown_algorithm(self):
        with self.assertRaisesRegex(ValueError, "Unsupported hash algorithm"):
            self.wrapper.getHash("hello", "unknown")

    def test_shake_requires_an_explicit_length(self):
        for algorithm in ("shake_128", "shake_256"):
            with self.subTest(algorithm=algorithm):
                with self.assertRaisesRegex(ValueError, "digest length"):
                    self.wrapper.generateHash("hello", algorithm)


if __name__ == "__main__":
    unittest.main()
