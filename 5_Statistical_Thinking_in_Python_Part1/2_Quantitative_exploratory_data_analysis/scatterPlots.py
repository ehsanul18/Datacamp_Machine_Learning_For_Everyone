# Scatter plots
# When you made bee swarm plots, box plots, and ECDF plots in previous exercises, you compared the petal lengths of different species of iris. But what if you want to compare two properties of a single species? This is exactly what we will do in this exercise. We will make a scatter plot of the petal length and width measurements of Anderson's Iris versicolor flowers. If the flower scales (that is, it preserves its proportion as it grows), we would expect the length and width to be correlated.

# For your reference, the code used to produce the scatter plot in the video is provided below:

# _ = plt.plot(total_votes/1000, dem_share, marker='.', linestyle='none')

# _ = plt.xlabel('total votes (thousands)')

# _ = plt.ylabel('percent of vote for Obama')

# Instructions
# 100 XP
# Use plt.plot() with the appropriate keyword arguments to make a scatter plot of versicolor petal length (x-axis) versus petal width (y-axis). The variables versicolor_petal_length and versicolor_petal_width are already in your namespace. Do not forget to use the marker='.' and linestyle='none' keyword arguments.
# Label the axes.
# Display the plot.


# Make a scatter plot
_ = plt.plot(versicolor_petal_length, versicolor_petal_width, marker='.', linestyle='none')


# Label the axes
_ = plt.xlabel('petal length')
_ = plt.ylabel('petal width')


# Show the result
plt.show()
