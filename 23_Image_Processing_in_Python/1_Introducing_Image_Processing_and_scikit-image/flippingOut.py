# Flipping out
# As a prank, someone has turned an image from a photo album of a trip to Seville upside-down and back-to-front! Now, we need to straighten the image, by flipping it.

# City of Seville upside-down
# Image loaded as flipped_seville.
# Using the NumPy methods learned in the course, flip the image horizontally and vertically. Then display the corrected image using the show_image() function.
# NumPy is already imported as np.

# Instructions 1/3
# 35 XP
# Flip the image vertically.

# Instructions 2/3
# 35 XP
# Now, flip the vertically-flipped image horizontally.

# Instructions 3/3
# 30 XP
# Show the, now fixed, image.


# Flip the image vertically
seville_vertical_flip = np.flipud(flipped_seville)

# Flip the image horizontally
seville_horizontal_flip = np.fliplr(seville_vertical_flip)

# Show the resulting image
show_image(seville_horizontal_flip, 'Seville')
