import sys
#the location of FreeCadLibs
#For Linux Debian, locaiton is stable like "/usr/lib/freecad/lib".
sys.path.append('<FreeCadLib location')

import FreeCAD
import Mesh
import Part

stl_file = "<.stl_file_location>"

mesh = Mesh.Mesh(stl_file)

shape = Part.Shape()
# you can change the error prop. of bottom code.
shape.makeShapeFromMesh(mesh.Topology, 0.1)  
solid = Part.Solid(shape)

inertia = solid.MatrixOfInertia
volume = solid.Volume
center_of_mass = solid.CenterOfMass

print(f"Inertia:\n{inertia}")
print(f"Volume: {volume}")
print(f"Center of Mass: {center_of_mass}")