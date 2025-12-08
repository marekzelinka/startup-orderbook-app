from task import Task


class Orderbook:
    def __init__(self) -> None:
        self.__tasks: dict[int, Task] = {}

    def add_order(self, description: str, programmer: str, workload: int) -> None:
        new_id = len(self.__tasks) + 1
        task = Task(new_id, description, programmer, workload)

        self.__tasks[task.id] = task

    @property
    def orders(self) -> list[Task]:
        return list(self.__tasks.values())

    @property
    def programmers(self) -> list[str]:
        return list(set(task.programmer for task in self.__tasks.values()))

    def mark_order_finished(self, order_id: int) -> None:
        task = self.__tasks.get(order_id)

        if not task:
            raise ValueError(f"Task with id of {order_id} not found")

        task.mark_finished()

    @property
    def finished_orders(self) -> list[Task]:
        return [task for task in self.__tasks.values() if task.finished]

    @property
    def unfinished_orders(self) -> list[Task]:
        return [task for task in self.__tasks.values() if not task.finished]

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
