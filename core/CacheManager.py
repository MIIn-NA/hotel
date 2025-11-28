class CacheManager:
    def __init__(self, size_limit: int, eviction_policy: str, enabled: bool):
        self.size_limit = size_limit
        self.eviction_policy = eviction_policy
        self.enabled = enabled
        self._cache = {}

    def add_item(self, key: str, value: str) -> None:
        if not self.enabled:
            return
        if len(self._cache) >= self.size_limit:
            first_key = next(iter(self._cache))
            del self._cache[first_key]
        self._cache[key] = value

    def get_item(self, key: str) -> str | None:
        if not self.enabled:
            return None
        value = self._cache.get(key)
        if value:
            return value.strip()
        return None
