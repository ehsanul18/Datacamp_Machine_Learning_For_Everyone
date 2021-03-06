# Two samples
# After building several classification models based on thetic_tac_toe dataset, you realize that some models do not generalize as well as others. You have created training and testing splits just as you have been taught, so you are curious why your validation process is not working.

# After trying a different training, test split, you noticed differing accuracies for your machine learning model. Before getting too frustrated with the varying results, you have decided to see what else could be going on.

# Instructions 1/3
# 35 XP
# Create samples sample1 and sample2 with 200 observations that could act as possible testing datasets.

# Instructions 2/3
# 35 XP
# Use the list comprehension statement to find out how many observations these samples have in common.

# Instructions 3/3
# 30 XP
# Use the Series.value_counts() method to print the values in both samples for column Class.


# Create two different samples of 200 observations (Instruction 1)
sample1 = tic_tac_toe.sample(200, random_state=1111)
sample2 = tic_tac_toe.sample(200, random_state=1171)

# Print the number of common observations (Instruction 2)
print(len([index for index in sample1.index if index in sample2.index]))

# Print the number of observations in the Class column for both samples (Instruction 3) 
print(sample1['Class'].value_counts())
print(sample2['Class'].value_counts())
