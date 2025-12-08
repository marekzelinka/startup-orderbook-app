from task import Task


class Orderbook:
    def __init__(self) -> None:
        self.__tasks: dict[int, Task] = {}

    @property
    def orders(self) -> dict[int, Task]:
        return self.__tasks

    @property
    def programmers(self) -> list[str]:
        return list(set(task.programmer for task in self.__tasks.values()))

    @property
    def finished_orders(self) -> list[Task]:
        return [task for task in self.__tasks.values() if task.finished]

    @property
    def unfinished_orders(self) -> list[Task]:
        return [task for task in self.__tasks.values() if not task.finished]

    def add_order(
        self,
        id: int,
        description: str,
        programmer: str,
        workload: int,
        finished: bool = False,
    ) -> None:
        task = Task(id, description, programmer, workload, finished)

        self.__tasks[id] = task

    def mark_order_finished(self, order_id: int) -> None:
        task = self.__tasks.get(order_id)

        if not task:
            raise ValueError(f"Task with id of {order_id} not found")

        task.mark_finished()

    def status_of_programmer(self, programmer: str) -> tuple[int, int, int, int]:
        assignet_tasks = [
            task for task in self.__tasks.values() if task.programmer == programmer
        ]

        if not assignet_tasks:
            raise ValueError("No programmer with given name")

        finished_tasks = [task for task in assignet_tasks if task.finished]
        unfinished_tasks = [task for task in assignet_tasks if not task.finished]

        finished_tasks_count = len(finished_tasks)
        unfinished_tasks_count = len(assignet_tasks) - finished_tasks_count
        sum_of_finished_workloads = sum(task.workload for task in finished_tasks)
        sum_of_unfinished_workloads = sum(task.workload for task in unfinished_tasks)

        return (
            finished_tasks_count,
            unfinished_tasks_count,
            sum_of_finished_workloads,
            sum_of_unfinished_workloads,
        )
