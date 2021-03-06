# Batch normalization effects
# Batch normalization tends to increase the learning speed of our models and make their learning curves more stable. Let's see how two identical models with and without batch normalization compare.

# The model you just built batchnorm_model is loaded for you to use. An exact copy of it without batch normalization: standard_model, is available as well. You can check their summary() in the console. X_train, y_train, X_test, and y_test are also loaded so that you can train both models.

# You will compare the accuracy learning curves for both models plotting them with compare_histories_acc().

# You can check the function pasting show_code(compare_histories_acc) in the console.

# Instructions
# 100 XP
# Train the standard_model for 10 epochs passing in train and validation data, storing its history in h1_callback.
# Train your batchnorm_model for 10 epochs passing in train and validation data, storing its history in h2_callback.
# Call compare_histories_acc passing in h1_callback and h2_callback.


# Train your standard model, storing its history callback
h1_callback = standard_model.fit(X_train, y_train, validation_data=(X_test,y_test), epochs=10, verbose=0)

# Train the batch normalized model you recently built, store its history callback
h2_callback = batchnorm_model.fit(X_train, y_train, validation_data=(X_test,y_test), epochs=10, verbose=0)

# Call compare_histories_acc passing in both model histories
compare_histories_acc(h1_callback, h2_callback)
