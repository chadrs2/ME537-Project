import numpy as np

def offset_and_reshape(pose, x_offset, y_offset, z_offset):
    pose_arr = np.array(pose).reshape(4,4)
    pose_offset = np.array([[1, 0, 0, x_offset],
                            [0, 1, 0, y_offset],
                            [0, 0, 1, z_offset],
                            [0, 0, 0, 1]])
    pose_arr[0,3] += .111
    pose_arr[1,3] -= .113
    pose_arr[2,3] += .000
    return np.dot(pose_offset,pose_arr)
