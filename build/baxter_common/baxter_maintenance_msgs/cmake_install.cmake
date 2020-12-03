# Install script for directory: /home/aaron/repos/ME537-Project/src/baxter_common/baxter_maintenance_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/aaron/repos/ME537-Project/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_maintenance_msgs/msg" TYPE FILE FILES
    "/home/aaron/repos/ME537-Project/src/baxter_common/baxter_maintenance_msgs/msg/CalibrateArmData.msg"
    "/home/aaron/repos/ME537-Project/src/baxter_common/baxter_maintenance_msgs/msg/CalibrateArmEnable.msg"
    "/home/aaron/repos/ME537-Project/src/baxter_common/baxter_maintenance_msgs/msg/TareData.msg"
    "/home/aaron/repos/ME537-Project/src/baxter_common/baxter_maintenance_msgs/msg/TareEnable.msg"
    "/home/aaron/repos/ME537-Project/src/baxter_common/baxter_maintenance_msgs/msg/UpdateSource.msg"
    "/home/aaron/repos/ME537-Project/src/baxter_common/baxter_maintenance_msgs/msg/UpdateSources.msg"
    "/home/aaron/repos/ME537-Project/src/baxter_common/baxter_maintenance_msgs/msg/UpdateStatus.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_maintenance_msgs/cmake" TYPE FILE FILES "/home/aaron/repos/ME537-Project/build/baxter_common/baxter_maintenance_msgs/catkin_generated/installspace/baxter_maintenance_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/aaron/repos/ME537-Project/devel/include/baxter_maintenance_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/aaron/repos/ME537-Project/devel/share/roseus/ros/baxter_maintenance_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/aaron/repos/ME537-Project/devel/share/common-lisp/ros/baxter_maintenance_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/aaron/repos/ME537-Project/devel/share/gennodejs/ros/baxter_maintenance_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/aaron/repos/ME537-Project/devel/lib/python3/dist-packages/baxter_maintenance_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/aaron/repos/ME537-Project/devel/lib/python3/dist-packages/baxter_maintenance_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/aaron/repos/ME537-Project/build/baxter_common/baxter_maintenance_msgs/catkin_generated/installspace/baxter_maintenance_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_maintenance_msgs/cmake" TYPE FILE FILES "/home/aaron/repos/ME537-Project/build/baxter_common/baxter_maintenance_msgs/catkin_generated/installspace/baxter_maintenance_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_maintenance_msgs/cmake" TYPE FILE FILES
    "/home/aaron/repos/ME537-Project/build/baxter_common/baxter_maintenance_msgs/catkin_generated/installspace/baxter_maintenance_msgsConfig.cmake"
    "/home/aaron/repos/ME537-Project/build/baxter_common/baxter_maintenance_msgs/catkin_generated/installspace/baxter_maintenance_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/baxter_maintenance_msgs" TYPE FILE FILES "/home/aaron/repos/ME537-Project/src/baxter_common/baxter_maintenance_msgs/package.xml")
endif()
