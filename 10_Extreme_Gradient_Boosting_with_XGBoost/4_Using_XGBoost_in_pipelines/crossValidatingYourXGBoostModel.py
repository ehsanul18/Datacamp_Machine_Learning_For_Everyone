# Cross-validating your XGBoost model
# In this exercise, you'll go one step further by using the pipeline you've created to preprocess and cross-validate your model.

# Instructions
# 100 XP
# Create a pipeline called xgb_pipeline using steps.
# Perform 10-fold cross-validation using cross_val_score(). You'll have to pass in the pipeline, X (as a dictionary, using .to_dict("records")), y, the number of folds you want to use, and scoring ("neg_mean_squared_error").
# Print the 10-fold RMSE.


# Import necessary modules
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

# Fill LotFrontage missing values with 0
X.LotFrontage = X.LotFrontage.fillna(0)

# Setup the pipeline steps: steps
steps = [("ohe_onestep", DictVectorizer(sparse=False)),
         ("xgb_model", xgb.XGBRegressor(max_depth=2, objective="reg:linear"))]

# Create the pipeline: xgb_pipeline
xgb_pipeline = Pipeline(steps)

# Cross-validate the model
cross_val_scores = cross_val_score(xgb_pipeline, X.to_dict("records"), y, scoring="neg_mean_squared_error", cv=10)

# Print the 10-fold RMSE
print("10-fold RMSE: ", np.mean(np.sqrt(np.abs(cross_val_scores))))
