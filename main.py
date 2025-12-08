from pyinputplus import inputInt, inputStr

from orderbook import Orderbook
from task import Task


class OrderbookApplication:
    def __init__(self) -> None:
        self.__running: bool = False
        self.__orderbook: Orderbook = Orderbook()

    def add_order(self) -> None:
        description: str = inputStr("description: ")
        programmer: str = inputStr("programmer: ")
        workload: int = inputInt("workload estimate: ", greaterThan=0)

        self.__orderbook.add_order(description, programmer, workload)

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

        self.__orderbook.mark_order_finished(order_id)

        print("marked as finished")

    def print_programmers(self) -> None:
        for programmer in self.__orderbook.programmers:
            print(programmer)

    def status_of_programmer(self):
        programmer: str = inputStr("programmer: ")

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

    def run(self) -> None:
        self.__running = True

        self.__help()

        while self.__running:
            print()

            command = input("command: ")

            if command == "0":
                self.__exit()
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.print_finished_tasks()
            elif command == "3":
                self.print_unfinished_tasks()
            elif command == "4":
                self.mark_order_finished()
            elif command == "5":
                self.print_programmers()
            elif command == "6":
                self.status_of_programmer()
            else:
                self.__help()

    def __exit(self) -> None:
        self.__running = False

    def __help(self) -> None:
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def __print_orders(self, orders: list[Task]) -> None:
        for task in orders:
            print(task)


def main():
    orderbook_app = OrderbookApplication()

    orderbook_app.run()


if __name__ == "__main__":
    main()
