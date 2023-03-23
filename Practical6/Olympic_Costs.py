#Create a dictionary contain The cost of hosting the Summer Olympic Games has increased rapidly over time Olympic Games and Cost (in $ billions)
costs = {'Los Angeles 1984': 1, 'Seoul 1988': 8, 'Barcelona 1992': 15, 'Atlanta 1996': 7, 'Sydney 2000': 5, 'Athens 2003': 14, 'Beijing 2008': 43, 'London 2012': 40}
import matplotlib.pyplot as plt

# Sort the dictionary by value and create a list
sorted_costs = sorted(costs.items(), key=lambda x: x[1])

# Print the sorted costs list
print("Sorted Costs:") #uses the print function to output the string Sorted Costs:, which is the title of the sorted list output.
for item in sorted_costs:#uses a for loop to iterate through each element in the sorted_costs list, with item representing an element in the sorted_costs list.
    print(f"{item[0]}: {item[1]}")#uses the print function to output a formatted string labeled with item[0] and size item[1]. item[0] and item[1] represent the first and second values of the element in the sorted_costs list, which are the label and size, respectively.

# Extract the sorted labels and sizes from the sorted costs list
#defines a new list called labels, which uses the form of a list inference to extract the first value of all elements (labels) from the sorted_costs and form them into a new list.
labels = [item[0] for item in sorted_costs]
#defines a new list called sizes, which also uses the form of a list inference to extract the second value (size) of all elements from the sorted_costs and form a new list.
sizes = [item[1] for item in sorted_costs]

# Plot the sorted costs as a bar chart
plt.bar(labels, sizes)
# Title the chart as Olympic Costs by Host City (Sorted)
plt.title('Olympic Costs by Host City (Sorted)')
# Name the x of the chart as Host City
plt.xlabel('Host City')
# Name the y of the chart as Cost in Billions
plt.ylabel('Cost in Billions')
# Show the bar chart
plt.show()
