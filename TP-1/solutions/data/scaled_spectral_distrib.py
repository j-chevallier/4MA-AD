print("Visualization of different wave length distributions after standard scaling \n")

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.hist(mars_scaled[:, plotIndex[i]], bins = 100, color="mediumorchid")
    plt.xlabel("V%i" % (plotIndex[i]+1))
    plt.ylabel("Frequency")
    
plt.tight_layout()
plt.show()