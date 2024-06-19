# Helper code for transparent transformation matrices

import numpy as np
from numpy import cos, sin

def frame_transformation(translation_vector, rotation_axis: int, rotation_angle: float):

    ''' return an alias transformation matrix in homogenous coordinates which applies a translation followed
     by a rotation, both relative to the parent coordinate frame. Because of frame transformation convention
     rotation and translation get inverted along the way.'''
    
    ra: float = -rotation_angle

    translation = np.identity(4) 
    
    translation[0][3] = -translation_vector[0] 
    translation[1][3] = -translation_vector[1]
    translation[2][3] = -translation_vector[2]
    
    if rotation_axis == 0: # X

        rotation = np.array([[1,        0      ,  0       ],
                             [0,        cos(ra), -sin(ra) ],
                             [0,        sin(ra),  cos(ra) ]])

    elif rotation_axis == 1: # Y

        rotation = np.array([[ cos(ra), 0      , sin(ra) ],
                             [ 0      , 1.     ,       0 ],
                             [-sin(ra), 0      , cos(ra) ]])
        
    elif rotation_axis == 2: # Z

        rotation = np.array([[ cos(ra), -sin(ra),       0 ],
                             [ sin(ra), cos(ra) ,       0 ],
                             [ 0      , 0       ,       1 ]])

    else:
        raise ValueError
    
    # add row/colum 4 for homogoenous coordinate convention

    rotation = np.append(rotation, [[0,0,0]],0)
    rotation = np.append(rotation, [[0],[0],[0],[1]],1)

    return rotation @ translation   

def reflection_matrix(surface_normal):

    # convert array to vector and normalize in case the surface normal is not yet a unit vector
    surface_normal = surface_normal.reshape(-1, 1)/np.linalg.norm(surface_normal)

    # assemble and return the full reflection matrix
    return np.identity(3) - 2*(surface_normal @ surface_normal.T)