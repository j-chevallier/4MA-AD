print("Comparison of the wave length distributions, before and after standard scaling \n")

for i in range(6):
    plt.subplot(6, 2, 2*i+1)
    plt.hist(mars_data[:, plotIndex[i]], bins = 100)
    plt.xlabel("V%i" % (plotIndex[i]+1))
    plt.subplot(6, 2, 2*(i+1))
    plt.hist(mars_scaled[:, plotIndex[i]], bins = 100, color="mediumorchid")
    plt.xlabel("V%i" % (plotIndex[i]+1))
    # plt.ylabel("Frequency")
    # plt.tight_layout()
plt.show()