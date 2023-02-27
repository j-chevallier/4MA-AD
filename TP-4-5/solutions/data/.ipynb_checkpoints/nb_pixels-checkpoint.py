mars_data = mars.to_numpy()

# Dimensions de l'image
n_pixel_x = 300
n_pixel_y = 128

n_pixel = mars.shape[0]
dim_spectral = mars.shape[1]

print("Image size: n_x.n_y:", n_pixel_x*n_pixel_y)
print("Number of pixels   :", n_pixel)
print("Number of channels :", dim_spectral)