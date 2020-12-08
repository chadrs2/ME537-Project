#!/usr/bin/env python
from numpy.core.defchararray import join
from genpy.message import DeserializationError
import rospy
import tf
import numpy as np
from rad_baxter_limb import RadBaxterLimb
import baxter_interface
import baxter_left_kinematics as blk
import baxter_right_kinematics as brk
import matplotlib.pyplot as plt
import matplotlib
import sys
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

matplotlib.rcParams['backend'] = 'Qt5Agg'
# print(plt.matplotlib.rcParams['figure.dpi'])
if plt.get_backend() == 'Qt5Agg':
    from matplotlib.backends.qt_compat import QtWidgets
    qApp = QtWidgets.QApplication(sys.argv)
    # print(qApp.desktop().physicalDpiX())
    plt.matplotlib.rcParams['figure.dpi'] = qApp.desktop().physicalDpiX()


def main():
    np_load_old = np.load
    np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
    
    # X_list = np.load('baxter_position_data_w_object.npy')
    # X_real = np.load('baxter_fk_position_data_w_object.npy')
    # X_physical = np.load('baxter_real_fk_position_data_w_object.npy')
    X_list = np.load('baxter_position_data_no_object.npy')
    X_real = np.load('baxter_fk_position_data_no_object.npy')
    X_physical = np.load('baxter_real_fk_position_data_no_object.npy')
    
    for i in range(len(X_list)):
        if (X_list[i] == 'pause'):
            row_2_del = i 
    X_list = np.delete(X_list, row_2_del, 0)
    
    X = np.zeros((len(X_list),3))
    for i in range(len(X_list)):
        X[i,:] = np.array(X_list[i])

    x = X[:,0]
    y = X[:,1]
    z = X[:,2]
    x_real = X_real[:,0]
    y_real = X_real[:,1]
    z_real = X_real[:,2]
    x_phys = X_physical[:,0]
    y_phys = X_physical[:,1]
    z_phys = X_physical[:,2]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #ax.set_aspect('equal')

    ax.scatter(x, y, z, marker='*', color='black')
    ax.scatter(x_real, y_real, z_real, marker='*', color='blue')
    ax.scatter(x_phys, y_phys, z_phys, marker='o', color='red')
    ax.scatter(1.0, -0.7, 0.3, marker='^')
    ax.scatter(1.1, 0.0, 0.3, marker='^')
    ax.scatter(1.1,0.2,-0.3, marker='^')
    ax.scatter(1.1,0.15,0.4, marker='^')
    ax.scatter(1.1,0.15,0.6, marker='^')
    ax.scatter(1.0,-0.5,0.6, marker='^')
    ax.scatter(0.8,-0.8,0.3, marker='^')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('Position Path Determined from Obstacle Avoidance Algorithm')

    ax.text(x[0], y[0], z[0], 'Starting Position', color='black')
    ax.text(x[-1], y[-1], z[-1], 'Ending Position', color='black')
    ax.text(1.0, -0.7, 0.3, 'Commanded Position: 0')
    ax.text(1.1, 0, 0.3, 'Commanded Position: 1')
    ax.text(1.1,0.2,-.30, 'Commanded Position: 2')
    ax.text(1.1,0.15,0.4, 'Commanded Position: 3')
    ax.text(1.1,0.15,0.6, 'Commanded Position: 4')
    ax.text(1.0, -.5, .6, 'Commanded Position: 5')
    ax.text(.8,-.8,.3, 'Commanded Position: 6')

    # Plot object
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    rad = 0.3
    safety = 0.3 * rad
    obst_loc = [1.1, -.5, .05]
    x = rad * np.outer(np.cos(u), np.sin(v)) + obst_loc[0]
    y = rad * np.outer(np.sin(u), np.sin(v)) + obst_loc[1]
    z = rad * np.outer(np.ones(np.size(u)), np.cos(v)) + obst_loc[2]
    ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='k', linewidth=0, alpha=0.5)

    x_saf = (rad + safety) * np.outer(np.cos(u), np.sin(v)) + obst_loc[0]
    y_saf = (rad + safety) * np.outer(np.sin(u), np.sin(v)) + obst_loc[1]
    z_saf = (rad + safety) * np.outer(np.ones(np.size(u)), np.cos(v)) + obst_loc[2]
    #ax.plot_surface(x_saf, y_saf, z_saf,  rstride=4, cstride=4, color='b', linewidth=0, alpha=0.5)

    plt.show()



if __name__ == "__main__":
    main()
