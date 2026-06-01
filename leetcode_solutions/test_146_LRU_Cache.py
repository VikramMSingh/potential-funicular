"""
Unit tests for 146_LRU_Cache.py using unittest. The test file loads the module
by file path because the filename starts with a digit (not a valid Python
identifier for importlib.import_module).
"""
import unittest
import importlib.util
from pathlib import Path

# Load the LRUCache module by path
HERE = Path(__file__).resolve().parent
MOD_PATH = HERE / "146_LRU_Cache.py"
spec = importlib.util.spec_from_file_location("lru_module", str(MOD_PATH))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
LRUCache = mod.LRUCache


class TestLRUCache(unittest.TestCase):
    def test_put_get_basic(self):
        c = LRUCache(2)
        c.put(1, 1)
        c.put(2, 2)
        self.assertEqual(c.get(1), 1)  # 1 is MRU now
        self.assertEqual(c.get(2), 2)

    def test_eviction_order(self):
        c = LRUCache(2)
        c.put(1, 1)
        c.put(2, 2)
        c.get(1)        # access 1 -> 2 is LRU
        c.put(3, 3)     # should evict key 2
        self.assertEqual(c.get(2), -1)
        self.assertEqual(c.get(1), 1)
        self.assertEqual(c.get(3), 3)

    def test_update_existing(self):
        c = LRUCache(2)
        c.put(1, 1)
        c.put(2, 2)
        c.put(1, 10)    # update value for existing key 1
        self.assertEqual(c.get(1), 10)
        c.put(3, 3)     # should evict key 2
        self.assertEqual(c.get(2), -1)

    def test_get_missing(self):
        c = LRUCache(1)
        self.assertEqual(c.get(42), -1)


if __name__ == "__main__":
    unittest.main()
