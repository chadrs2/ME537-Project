## *********************************************************
##
## File autogenerated for the baxter_interface package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'goal_time', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'Amount of time (s) controller is permitted to be late achieving goal', 'min': 0.0, 'max': 120.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'stopped_velocity_tolerance', 'type': 'double', 'default': 0.25, 'level': 0, 'description': 'Maximum velocity (m/s) at end of trajectory to be considered stopped', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_s0_goal', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'left_s0 - maximum final error', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_s1_goal', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'left_s1 - maximum final error', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_e0_goal', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'left_e0 - maximum final error', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_e1_goal', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'left_e1 - maximum final error', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_w0_goal', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'left_w0 - maximum final error', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_w1_goal', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'left_w1 - maximum final error', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_w2_goal', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'left_w2 - maximum final error', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_s0_goal', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'right_s0 - maximum final error', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_s1_goal', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'right_s1 - maximum final error', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_e0_goal', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'right_e0 - maximum final error', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_e1_goal', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'right_e1 - maximum final error', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_w0_goal', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'right_w0 - maximum final error', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_w1_goal', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'right_w1 - maximum final error', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_w2_goal', 'type': 'double', 'default': -1.0, 'level': 0, 'description': 'right_w2 - maximum final error', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_s0_trajectory', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'left_s0 - maximum error during trajectory execution', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_s1_trajectory', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'left_s1 - maximum error during trajectory execution', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_e0_trajectory', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'left_e0 - maximum error during trajectory execution', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_e1_trajectory', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'left_e1 - maximum error during trajectory execution', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_w0_trajectory', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'left_w0 - maximum error during trajectory execution', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_w1_trajectory', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'left_w1 - maximum error during trajectory execution', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_w2_trajectory', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'left_w2 - maximum error during trajectory execution', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_s0_trajectory', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'right_s0 - maximum error during trajectory execution', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_s1_trajectory', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'right_s1 - maximum error during trajectory execution', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_e0_trajectory', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'right_e0 - maximum error during trajectory execution', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_e1_trajectory', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'right_e1 - maximum error during trajectory execution', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_w0_trajectory', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'right_w0 - maximum error during trajectory execution', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_w1_trajectory', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'right_w1 - maximum error during trajectory execution', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_w2_trajectory', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'right_w2 - maximum error during trajectory execution', 'min': -1.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

