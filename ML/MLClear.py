import numpy as np
sludge = [0, 0, 5, 1]
grease = [0, 0, 5, 1]
time = [0, 0.25, 0.5, 0.75, 1]
sludgeandgrease = np.zeros((len(sludge), len(grease)))
for i in range(len(sludge)):
	for j in range(len(grease)):
		sludgeandgrease[i, j] = max(sludge[i], grease[j])
sludgeandgeease = sludgeandgrease.reshape(9, 1)

