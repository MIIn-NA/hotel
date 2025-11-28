import pytest
from core.TaskScheduler import TaskScheduler


class TestTaskScheduler:
    def test_init(self):
        scheduler = TaskScheduler(60, "DailyTasks", True)
        assert scheduler.interval == 60
        assert scheduler.name == "DailyTasks"
        assert scheduler.active is True
        assert scheduler._tasks == []

    def test_add_task_when_active(self):
        scheduler = TaskScheduler(60, "DailyTasks", True)

        def sample_task():
            return "done"

        scheduler.add_task(sample_task)
        assert len(scheduler._tasks) == 1

    def test_add_task_when_inactive(self):
        scheduler = TaskScheduler(60, "DailyTasks", False)

        def sample_task():
            return "done"

        scheduler.add_task(sample_task)
        assert len(scheduler._tasks) == 0

    def test_add_task_not_callable(self):
        scheduler = TaskScheduler(60, "DailyTasks", True)
        scheduler.add_task("not a function")
        assert len(scheduler._tasks) == 0

    def test_add_multiple_tasks(self):
        scheduler = TaskScheduler(60, "DailyTasks", True)

        def task1():
            pass

        def task2():
            pass

        scheduler.add_task(task1)
        scheduler.add_task(task2)
        assert len(scheduler._tasks) == 2

    def test_run_all_success(self):
        scheduler = TaskScheduler(60, "DailyTasks", True)

        def task1():
            return "done1"

        def task2():
            return "done2"

        scheduler.add_task(task1)
        scheduler.add_task(task2)
        count = scheduler.run_all()
        assert count == 2

    def test_run_all_with_exception(self):
        scheduler = TaskScheduler(60, "DailyTasks", True)

        def task1():
            raise Exception("Error")

        def task2():
            return "done"

        scheduler.add_task(task1)
        scheduler.add_task(task2)
        count = scheduler.run_all()
        assert count == 1

    def test_run_all_empty(self):
        scheduler = TaskScheduler(60, "DailyTasks", True)
        count = scheduler.run_all()
        assert count == 0

    def test_run_all_all_fail(self):
        scheduler = TaskScheduler(60, "DailyTasks", True)

        def task1():
            raise ValueError("Error 1")

        def task2():
            raise RuntimeError("Error 2")

        scheduler.add_task(task1)
        scheduler.add_task(task2)
        count = scheduler.run_all()
        assert count == 0
