"""Assignment 01: Project box to xy-plane
"""
from compas.geometry import Box
from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Frame
from compas.geometry import Plane
from compas.geometry import Projection
from compas.artists import Artist
from compas.datastructures import Mesh


# Define a Frame, which is not in the origin and a bit tilted to the world frame
my_frame = Frame(Point(1, 1, 5), Vector(0.35, -0.2, 0.3), Vector(1, 0.3, 0))

# Create a Box with that frame
width, length, height = 1, 1, 1
box = Box(my_frame, width, length, height)

# Create a Projection (can be orthogonal, parallel or perspective)
# P = Projection.from_...
point = [0, 0, 0]
normal = [0, 0, 1]
m_plane = Plane(point, normal)
P = Projection.from_plane(m_plane)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Apply the Projection onto the mesh
mesh_projected = mesh.transformed(P)

# Create artists
artist1 = Artist(box)
artist2 = Artist(mesh_projected)

# Draw
artist1.draw()
artist2.draw_edges(color="#00ff00")
