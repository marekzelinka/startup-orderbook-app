import csv
from typing import Protocol

from task import Task


class OrderbookStorageService(Protocol):
    def __init__(self, filename: str) -> None: ...

    def load_file(self) -> dict[int, Task]: ...

    def save_file(self, orderbook: dict[int, Task]) -> None: ...


class OrderbookCSVStorage(OrderbookStorageService):
    def __init__(self, filename: str) -> None:
        self.__filename: str = filename

    def load_file(self) -> dict[int, Task]:
        orderbook: dict[int, Task] = {}

        with open(self.__filename, newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                task_id = int(row["id"])
                description = row["description"]
                programmer = row["programmer"]
                workload = int(row["workload"])
                finished = row["finished"] == "True"

                orderbook[task_id] = Task(
                    task_id, description, programmer, workload, finished
                )

        return orderbook

    def save_file(self, orderbook: dict[int, Task]) -> None:
        with open(self.__filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=["id", "description", "programmer", "workload", "finished"],
            )

            writer.writeheader()

            for task in orderbook.values():
                writer.writerow(
                    {
                        "id": task.id,
                        "description": task.description,
                        "programmer": task.programmer,
                        "workload": task.workload,
                        "finished": task.finished,
                    }
                )
