# Less edgy
# Let's now try to spot just the outer shape of the grapefruits, the circles. You can do this by applying a more intense Gaussian filter to first make the image smoother. This can be achieved by specifying a bigger sigma in the canny function.

# In this exercise, you'll experiment with sigma values of the canny() function.

# Grapefruits
# Image preloaded as grapefruit.
# The show_image has already been preloaded.

# Instructions 1/3
# 35 XP
# Apply the canny edge detector to the grapefruit image with a sigma of 1.8.

# Instructions 2/3
# Apply the canny edge detector to the grapefruit image with a sigma of 2.2.

# Instructions 3/3
# Show the resulting images.


# # Apply canny edge detector with a sigma of 1.8 (Instruction 1)
# canny_edges = canny(grapefruit, sigma=1.8)


# Apply canny edge detector with a sigma of 1.8 (Instruction 2)
edges_1_8 = canny(grapefruit, sigma=1.8)

# Apply canny edge detector with a sigma of 2.2
edges_2_2 = canny(grapefruit, sigma=2.2)

# Show resulting images (Instruction 3)
show_image(edges_1_8, "Sigma of 1.8")
show_image(edges_2_2, "Sigma of 2.2")
