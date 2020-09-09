#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from particles_in_box import ParticlesInBox

simulation = ParticlesInBox()
n_step = simulation.n_step
n_mol = simulation.n_mol
boundaries = simulation.boundaries
xyz = simulation.xyz

x, y, z = np.loadtxt(xyz, comments='#').T
fig = plt.figure()
ax = fig.gca(projection='3d')
for i in range(n_step):
    plt.cla()
    x_graph = x[i * n_mol: i * n_mol + n_mol]
    y_graph = y[i * n_mol: i * n_mol + n_mol]
    z_graph = z[i * n_mol: i * n_mol + n_mol]
    ax.scatter(x_graph, y_graph, z_graph, c='k', s=200, marker='.')
    ax.set_axis_off()
    ax.set_xlim(boundaries)
    ax.set_ylim(boundaries)
    ax.set_zlim(boundaries)
    plt.pause(0.001)
    simulation.print_step(i)
plt.show()
