import pytest
from core.CacheManager import CacheManager


class TestCacheManager:
    def test_init(self):
        cache = CacheManager(10, "LRU", True)
        assert cache.size_limit == 10
        assert cache.eviction_policy == "LRU"
        assert cache.enabled is True
        assert cache._cache == {}

    def test_add_item_when_enabled(self):
        cache = CacheManager(10, "LRU", True)
        cache.add_item("key1", "value1")
        assert cache._cache["key1"] == "value1"

    def test_add_item_when_disabled(self):
        cache = CacheManager(10, "LRU", False)
        cache.add_item("key1", "value1")
        assert cache._cache == {}

    def test_add_item_eviction(self):
        cache = CacheManager(2, "LRU", True)
        cache.add_item("key1", "value1")
        cache.add_item("key2", "value2")
        cache.add_item("key3", "value3")
        assert "key1" not in cache._cache
        assert "key2" in cache._cache
        assert "key3" in cache._cache

    def test_get_item_existing(self):
        cache = CacheManager(10, "LRU", True)
        cache.add_item("key1", "value1")
        result = cache.get_item("key1")
        assert result == "value1"

    def test_get_item_with_whitespace(self):
        cache = CacheManager(10, "LRU", True)
        cache.add_item("key1", "  value1  ")
        result = cache.get_item("key1")
        assert result == "value1"

    def test_get_item_nonexistent(self):
        cache = CacheManager(10, "LRU", True)
        result = cache.get_item("nonexistent")
        assert result is None

    def test_get_item_when_disabled(self):
        cache = CacheManager(10, "LRU", False)
        cache._cache["key1"] = "value1"
        result = cache.get_item("key1")
        assert result is None

    def test_multiple_items(self):
        cache = CacheManager(5, "LRU", True)
        for i in range(5):
            cache.add_item(f"key{i}", f"value{i}")
        assert len(cache._cache) == 5

    def test_size_limit_enforcement(self):
        cache = CacheManager(3, "LRU", True)
        for i in range(5):
            cache.add_item(f"key{i}", f"value{i}")
        assert len(cache._cache) <= 3
