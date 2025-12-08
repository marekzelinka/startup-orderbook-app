from orderbook import OrderBook


class OrderBookApp:
    def __init__(self) -> None:
        self.__running: bool = False
        self.__orderbook: OrderBook = OrderBook()

    def add_order(self, inputs: tuple[str, str, int]) -> None:
        self.__orderbook.add_order(*inputs)

        print("added!")

    def list_finished_tasks(self) -> None:
        finished_tasks = self.__orderbook.finished_orders()

        if not finished_tasks:
            print("no finished tasks")

        self.__print_orders(finished_tasks)

    def list_unfinished_tasks(self) -> None:
        unfinished_tasks = self.__orderbook.unfinished_orders()

        if not unfinished_tasks:
            print("no unfinished tasks")

        self.__print_orders(unfinished_tasks)

    def mark_finished(self, inputs: tuple[int]) -> None:
        self.__orderbook.mark_finished(*inputs)

        print("marked as finished")

    def list_programmers(self) -> None:
        programmers = self.__orderbook.list_programmers()

        for programmer in programmers:
            print(programmer)

    def status_of_programmer(self, inputs: tuple[str]):
        (
            finished_tasks_count,
            unfinished_tasks_count,
            sum_of_finished_workloads,
            sum_of_unfinished_workloads,
        ) = self.__orderbook.status_of_programmer(*inputs)

        print(
            f"tasks: finished {finished_tasks_count} not finished {unfinished_tasks_count}, "
            f"hours: done {sum_of_finished_workloads} scheduled {sum_of_unfinished_workloads}"
        )

    def exit(self) -> None:
        self.__running = False

    def execute(self) -> None:
        self.__running = True

        self.__help()

        while self.__running:
            print()

            command = input("command: ")

            if command == "0":
                self.exit()
            elif command == "1":
                try:
                    self.add_order(self.__add_order_inputs())
                except ValueError:
                    print("erroneous input")
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                try:
                    self.mark_finished(self.__mark_finished_inputs())
                except ValueError:
                    print("erroneous input")
            elif command == "5":
                self.list_programmers()
            elif command == "6":
                try:
                    self.status_of_programmer(self.__status_of_programmer_inputs())
                except ValueError:
                    print("erroneous input")
            else:
                self.__help()

    def __add_order_inputs(self) -> tuple[str, str, int]:
        description = input("description: ")
        programmer, workload = input("programmer and workload estimate: ").split(" ")

        return description, programmer, int(workload)

    def __mark_finished_inputs(self) -> tuple[int]:
        id = input("id: ")

        return (int(id),)

    def __status_of_programmer_inputs(self) -> tuple[str]:
        programmer = input("programmer: ")

        return (programmer,)

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
    orderbook_app = OrderBookApp()

    orderbook_app.execute()


if __name__ == "__main__":
    main()
