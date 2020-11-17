# Replacing missing values with constants
# While removing missing data entirely maybe a correct approach in many situations, this may result in a lot of information being omitted from your models.

# You may find categorical columns where the missing value is a valid piece of information in itself, such as someone refusing to answer a question in a survey. In these cases, you can fill all missing values with a new category entirely, for example 'No response given'.

# Instructions 1/2
# 50 XP
# Print the count of occurrences of each category in so_survey_df's Gender column.

# Instructions 2/2
# 50 XP
# Replace all missing values in the Gender column with the string 'Not Given'. Make changes to the original DataFrame.


# # Print the count of occurrences (Instruction 1)
# print(so_survey_df['Gender'].value_counts())


# Replace missing values (Instruction 2)
so_survey_df['Gender'].fillna(value='Not Given', inplace=True)

# Print the count of each value
print(so_survey_df['Gender'].value_counts())
