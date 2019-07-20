import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2, 2)
cm = ['RdBu_r', 'viridis']
for col in range(2):
    for row in range(2):
        ax = axs[row, col]
        pcm = ax.pcolormesh(np.random.random((20, 20)) * (col + 1),
                            cmap=cm[col])
        fig.colorbar(pcm, ax=ax)
plt.show()

