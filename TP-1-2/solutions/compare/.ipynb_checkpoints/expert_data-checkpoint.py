n_pixel_x = 300
n_pixel_y = 128

clusters_expert = pd.read_csv("data_MARS/mask.csv").to_numpy()
clusters_expert = clusters_expert.reshape(n_pixel_x * n_pixel_y)