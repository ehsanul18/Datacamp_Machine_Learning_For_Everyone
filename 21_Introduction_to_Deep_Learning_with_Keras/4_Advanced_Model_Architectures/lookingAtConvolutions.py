# Looking at convolutions
# Inspecting the activations of a convolutional layer is a cool thing. You have to do it at least once in your lifetime!

# To do so, you will build a new model with the Keras Model object, which takes in a list of inputs and a list of outputs. The output you will provide to this new model is the first convolutional layer outputs when given an MNIST digit as input image.

# The convolutional model you built in the previous exercise has already been trained for you. It can now correctly classify MNIST handwritten images. You can check it with model.summary() in the console.

# Let's look at the convolutional masks that were learned in the first convolutional layer of this model!

# Instructions
# 100 XP
# Obtain a reference to the outputs of the first convolutional layer in the model.
# Build a new model using the model's first layer input and the first_layer_output as outputs.
# Use this first_layer_model to predict on X_test.
# Plot the activations of the first digit of X_test for the 15th and the 18th neuron filter.


# Obtain a reference to the outputs of the first layer
first_layer_output = model.layers[0].output

# Build a model using the model's input and the first layer output
first_layer_model = Model(inputs = model.layers[0].input, outputs = first_layer_output)

# Use this model to predict on X_test
activations = first_layer_model.predict(X_test)

# Plot the activations of first digit of X_test for the 15th filter
axs[0].matshow(activations[0,:,:,14], cmap = 'viridis')

# Do the same but for the 18th filter now
axs[1].matshow(activations[0,:,:,17], cmap = 'viridis')
plt.show()
