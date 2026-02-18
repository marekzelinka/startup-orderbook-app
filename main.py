from pyinputplus import inputInt, inputMenu, inputStr

from orderbook import Orderbook
from orderbook_storage import OrderbookCSVStorageService, OrderbookStorageService
from task import Task


class OrderbookApplication:
    def __init__(self, storage_service: OrderbookStorageService) -> None:
        self.__running: bool = False
        self.__orderbook: Orderbook = Orderbook()
        self.__storage_service: OrderbookStorageService = storage_service

        for id, task in self.__storage_service.load_file().items():
            self.__orderbook.add_order(
                id, task.description, task.programmer, task.workload, task.finished
            )

    def add_order(self) -> None:
        task_id = len(self.__orderbook.orders) + 1
        description: str = inputStr("description: ")
        programmer: str = inputStr("programmer: ")
        workload: int = inputInt("workload estimate: ", greaterThan=0)

        self.__orderbook.add_order(task_id, description, programmer, workload)

        print("task added!")

    def print_finished_tasks(self) -> None:
        if not self.__orderbook.finished_orders:
            print("no finished tasks")

        self.__print_orders(self.__orderbook.finished_orders)

    def print_unfinished_tasks(self) -> None:
        if not self.__orderbook.unfinished_orders:
            print("no unfinished tasks")

        self.__print_orders(self.__orderbook.unfinished_orders)

    def mark_order_finished(self) -> None:
        order_id: int = inputInt("id: ", greaterThan=0)

        try:
            self.__orderbook.mark_order_finished(order_id)

            print("marked as finished")
        except ValueError as e:
            print(e)

    def print_programmers(self) -> None:
        for programmer in self.__orderbook.programmers:
            print(programmer)

    def status_of_programmer(self):
        programmer: str = inputStr("programmer: ")

        try:
            (
                finished_tasks_count,
                unfinished_tasks_count,
                sum_of_finished_workloads,
                sum_of_unfinished_workloads,
            ) = self.__orderbook.status_of_programmer(programmer)

            print(
                f"tasks: finished {finished_tasks_count} - unfinished {unfinished_tasks_count}, "
                f"hours: done {sum_of_finished_workloads} - scheduled {sum_of_unfinished_workloads}"
            )
        except ValueError as e:
            print(e)

    def run(self) -> None:
        self.__running = True

        print("Welcome back to your OrderBook!")
        print()

        while self.__running:
            COMMANDS = {
                "exit": self.__exit,
                "add order": self.add_order,
                "list finished tasks": self.print_finished_tasks,
                "list unfinished tasks": self.print_unfinished_tasks,
                "mark task as finished": self.mark_order_finished,
                "programmers": self.print_programmers,
                "status of programmer": self.status_of_programmer,
            }

            command: int = inputMenu(
                list(COMMANDS.keys()),
                numbered=True,
            )

            COMMANDS[command]()

    def __exit(self) -> None:
        self.__running = False

        self.__storage_service.save_file(self.__orderbook.orders)

        print("\nExiting...")

    def __print_orders(self, orders: list[Task]) -> None:
        for task in orders:
            print(task)


def main():
    csv_storage_service = OrderbookCSVStorageService("orders.csv")
    orderbook_app = OrderbookApplication(storage_service=csv_storage_service)

    orderbook_app.run()


if __name__ == "__main__":
    main()
