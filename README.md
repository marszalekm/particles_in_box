# Particles in box

Script generates system of moving particles (points) confined in a box of a chosen size. 
When points reach (defined) vicinity of other ones, they form aggregates and continue moving together.
Results are stored in xyz file. For visualization I recommend VMD or PyMOL.

General workflow:
* Points of origin are generated and added to the file.
* Loop starts and algorithm checks distances between all points.
* Random vectors are generated.
* Particles that are in given vicinity from now will move with the same vector.
* Conditions of periodic boundary conditions are checks i.e. so the points won't cross given box size.
* Step with coordinates is saved to the file.

