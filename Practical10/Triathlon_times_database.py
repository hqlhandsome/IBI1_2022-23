# Define a class called triathlon
class triathlon:
    # Define the constructor method that takes seven parameters: first name, last name, location, swim time, cycle time, run time, and total time
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time):
        # Assign the parameters to the instance attributes
        self.first_name=first_name
        self.last_name=last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        # Calculate the total time by adding the swim time, cycle time, and run time
        self.total_time = swim_time + cycle_time + run_time

    # Define a method that prints the details of the triathlon instance
    def print_details(self):
         # Use string formatting to print the first name, last name, location, swim time, cycle time, run time, and total time of the instance
        print(f"{self.first_name} {self.last_name} competed in {self.location} and finished with a swim time of {self.swim_time}s, a cycle time of {self.cycle_time}s, a run time of {self.run_time}s, and a total time of {self.total_time}s.")

# Create an instance of the triathlon class by using the input function to get the user's input for each parameter
a = triathlon(input('first_name:'), input('last_name:'), input('location:'), int(input('swim time(s):')), int(input('cycle time(s):')), int(input('run time(s):')))
# Call the print_details method on the instance to print its details
a.print_details()
# an example
b = triathlon('Paul', 'George', 'OKC', 1000, 1000, 1000)
b.print_details()
