# create a dictionary called numbers_of_the_students
numbers_of_the_students={'Comedy':73,'Action':42,'Romance':38,'Fantasy':28,'Science-fiction':22,'Horror':19,'Crime':18,'Documentary':12,'History':8,'War':7}
colors={'Red','Orange','Yellow','Green','yellowgreen','Blue','lightskyblue','Purple','grey','Pink'}
import matplotlib.pyplot as plt
# Store the key and value in numbers_of_the_students in the two variables labels and sizes, respectively.
sizes = list(numbers_of_the_students.values())
labels = list(numbers_of_the_students.keys())

# Create a pie chart where the size of each sector is specified by the sizes array, the label of each sector is specified by the labels array, the colors of each sector is specified at the dictionary above and the percentage of each sector is specified by the autopct parameter.
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
# Equal can ensure the pie is drawn as a circal
plt.axis('equal')
# Title the chart as Favourite movie genres among Chinese university students
plt.title('Favourite movie genres among Chinese university students')
# Show the pie chart
plt.show()

# Choose a movie genre
movie_genre='Comedy'
# Print the number that how many students like this genre
print(numbers_of_the_students[movie_genre])#73
