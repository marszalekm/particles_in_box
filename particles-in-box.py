#!/usr/bin/env python3

import numpy as np
from itertools import combinations

class particles_in_box():

    def __init__(self, n_mol = 10, n_step = 1000, boundaries = (0.0, 30.0), rad = 2):
        self.n_mol = n_mol  # Number of molecules
        self.n_step = n_step  # Number of steps
        self.boundaries = boundaries  # Box range
        self.rad = rad  # Radius of interactions (not recommended to use value lower than 1.75)

    def create_origin(self):
        """
        Creates points of origin and adds them to the file.
        """

        origin = np.around(np.random.uniform(self.boundaries[0], self.boundaries[1], size=(self.n_mol, 3)), 2)
        originlist = origin.tolist()

        xyz = open('coordinates.xyz', 'a+')
        xyz.write("%d \nOrigin\n" % self.n_mol)
        for n in range(self.n_mol):
            xyz.write("H%d %.2f %.2f %.2f\n" % (n + 1, originlist[n][0], originlist[n][1], originlist[n][2]))

        return origin, xyz

    def interactions(self, path, origin):
        """
        Function simulates interactions between points in given vicinity
        """
        dictionary = {}  # dictionary consisting of positions and coordinates

        for x, y in combinations(path, 2):

            if np.linalg.norm(x - y) <= self.rad:

                pair = [np.argwhere(origin == x)[0][0], np.argwhere(origin == y)[0][0]]

                for i in pair:
                    if i not in dictionary:
                        vector = np.around(np.random.uniform(-0.5, 0.5, size=(1, 3)), 2)
                        dictionary.update({pair[0]: vector})
                        dictionary.update({pair[1]: vector})

                    else:
                        dictionary.update({pair[0]: dictionary[i]})
                        dictionary.update({pair[1]: dictionary[i]})

        return dictionary

    def generate_step(self, dictionary, path, step):
        """
        Addition points to dictionary and setting setting final form of particular step (coordinates)
        """
        for i in range(self.n_mol):
            if i not in dictionary:
                addpoint = np.around(np.random.uniform(-0.5, 0.5, size=(1, 3)), 2)
                dictionary.update({i: addpoint})

        for key, value in sorted(dictionary.items()):
            step = np.append(step, np.array(value), axis=0)
        path += step
        return path

    def boundaries_conditions(self, path):
        """
        Management of points close to boundaries of box.
        """

        for cord in np.nditer(path, op_flags=['readwrite']):
            if cord > self.boundaries[1]:
                cord[...] = cord - 0.5
            if cord < self.boundaries[0]:
                cord[...] = cord + 0.5

        return path


    def step_to_file(self, pstep, path, xyz):
        """
        Saves current step to file.
        """
        pathlist = path.tolist()
        xyz.write("%d \nStep number %d\n" % (self.n_mol, pstep + 1))
        for n in range(self.n_mol):
            xyz.write("H%d %.2f %.2f %.2f\n" % (n + 1, pathlist[n][0], pathlist[n][1], pathlist[n][2]))

    @staticmethod
    def print_step(pstep):
        """
        Prints currents step (progress) on screen.
        """
        if pstep % 100 == 0:
            print('Current step:', pstep)

    def run_simulation(self):
        """
        Main loop of simulation.
        """
        origin, xyz = self.create_origin()
        path = origin
        pstep = 0 #Present step
        while pstep < self.n_step - 1:
            pstep += 1
            step = np.empty(shape=(0, 3), dtype=float)
            dictionary = self.interactions(path, origin)
            path = self.generate_step(dictionary, path, step)
            path = self.boundaries_conditions(path)
            self.step_to_file(pstep, path, xyz)
            self.print_step(pstep)
        xyz.close()

simulation = particles_in_box()
simulation.run_simulation()
