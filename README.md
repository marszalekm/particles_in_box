# Particles in box.

Script generates system of moving particles (points) confined in a box of a chosen size. 
When points reach (defined) vicinity of other ones, they form aggregates and continue moving together.
Results are stored in xyz file. For visualization I recommend VMD or PyMOL.

General workflow:
1. Points of origin are generated and added to the file.
2. Loop starts and algorithm checks distances between all points.
3. Random vectors are generated.
4. Particles that are in given vicinity, from now will move with the same vector.
5. Conditions of periodic boundary conditions are checks i.e. so the points won't cross given box size.
6. Step with coordinates is saved to the file.

