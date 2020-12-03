#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/aaron/repos/ME537-Project/src/baxter_interface"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/aaron/repos/ME537-Project/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/aaron/repos/ME537-Project/install/lib/python3/dist-packages:/home/aaron/repos/ME537-Project/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/aaron/repos/ME537-Project/build" \
    "/usr/bin/python3" \
    "/home/aaron/repos/ME537-Project/src/baxter_interface/setup.py" \
     \
    build --build-base "/home/aaron/repos/ME537-Project/build/baxter_interface" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/aaron/repos/ME537-Project/install" --install-scripts="/home/aaron/repos/ME537-Project/install/bin"
