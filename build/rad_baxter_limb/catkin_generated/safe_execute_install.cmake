execute_process(COMMAND "/home/chad_samuelson/ME537-Project/build/rad_baxter_limb/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/chad_samuelson/ME537-Project/build/rad_baxter_limb/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
