# Tuning max_depth
# In this exercise, your job is to tune max_depth, which is the parameter that dictates the maximum depth that each tree in a boosting round can grow to. Smaller values will lead to shallower trees, and larger values to deeper trees.

# Instructions
# 100 XP
# Create a list called max_depths to store the following "max_depth" values: 2, 5, 10, and 20.
# Iterate over your max_depths list using a for loop.
# Systematically vary "max_depth" in each iteration of the for loop and perform 2-fold cross-validation with early stopping (5 rounds), 10 boosting rounds, a metric of "rmse", and a seed of 123. Ensure the output is a DataFrame.


# Create your housing DMatrix
housing_dmatrix = xgb.DMatrix(data=X,label=y)

# Create the parameter dictionary
params = {"objective":"reg:linear"}

# Create list of max_depth values
max_depths = [2, 5, 10, 20]
best_rmse = []

# Systematically vary the max_depth
for curr_val in max_depths:

    params["max_depth"] = curr_val
    
    # Perform cross-validation
    cv_results = pd.DataFrame(xgb.cv(dtrain=housing_dmatrix, params=params, metrics="rmse", early_stopping_rounds=5, num_boost_round=10, seed=123, nfold=2, as_pandas=True))
    
    # Append the final round rmse to best_rmse
    best_rmse.append(cv_results["test-rmse-mean"].tail().values[-1])

# Print the resultant DataFrame
print(pd.DataFrame(list(zip(max_depths, best_rmse)),columns=["max_depth","best_rmse"]))
