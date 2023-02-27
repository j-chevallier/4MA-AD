def diffPlot(classif1, classif2):
    n = classif1.shape[0]
    K = np.max(classif1)+1
    
    clusters = classif1.copy()
    idx = (classif1 != classif2)
    clusters[idx] = K+1
    
    nb_diff = np.sum(idx)
    print("Ratio of differently classified points:", nb_diff/n)   
    print("Nb of pixels differently classified:", nb_diff)

    # make a color map, with points differently classiffied in black
    cmap = plt.get_cmap('Set3',K)
    bk = np.array([0,0,0,1]).reshape(1,-1)
    cmap = colors.ListedColormap( np.concatenate((cmap.colors, bk)) )

    mars_image = clusters.reshape((n_pixel_x, n_pixel_y))
    plt.figure(figsize = (10,10))
    plt.imshow(mars_image, interpolation="nearest", aspect="auto", cmap=cmap)
    plt.show()