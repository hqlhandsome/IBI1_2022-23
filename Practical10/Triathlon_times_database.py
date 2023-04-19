class triathlon:
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time):
        self.first_name=first_name
        self.last_name=last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = swim_time + cycle_time + run_time

    def print_details(self):
        print(f"{self.first_name} {self.last_name} competed in {self.location} and finished with a swim time of {self.swim_time}s, a cycle time of {self.cycle_time}s, a run time of {self.run_time}s, and a total time of {self.total_time}s.")
a = triathlon(input('first_name:'), input('last_name:'), input('location:'), int(input('swim time(s):')), int(input('cycle time(s):')), int(input('run time(s):')))
a.print_details()
# an example
b = triathlon('Paul', 'George', 'OKC', 1000, 1000, 1000)
b.print_details()
