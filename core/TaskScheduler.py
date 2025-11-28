class TaskScheduler:
    def __init__(self, interval: int, name: str, active: bool):
        self.interval = interval
        self.name = name
        self.active = active
        self._tasks = []

    def add_task(self, func) -> None:
        if not self.active:
            return
        if callable(func):
            self._tasks.append(func)

    def run_all(self) -> int:
        count = 0
        for task in self._tasks:
            try:
                task()
                count += 1
            except Exception:
                continue
        return count
