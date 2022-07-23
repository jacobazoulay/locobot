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

echo_and_run cd "/home/ubuntu/interbotix_ws/src/interbotix_ros_rovers/interbotix_ros_xslocobots/examples/interbotix_xslocobot_landmark_nav"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/ubuntu/interbotix_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/ubuntu/interbotix_ws/install/lib/python3/dist-packages:/home/ubuntu/interbotix_ws/build/interbotix_xslocobot_landmark_nav/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/ubuntu/interbotix_ws/build/interbotix_xslocobot_landmark_nav" \
    "/bin/python3" \
    "/home/ubuntu/interbotix_ws/src/interbotix_ros_rovers/interbotix_ros_xslocobots/examples/interbotix_xslocobot_landmark_nav/setup.py" \
     \
    build --build-base "/home/ubuntu/interbotix_ws/build/interbotix_xslocobot_landmark_nav" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/ubuntu/interbotix_ws/install" --install-scripts="/home/ubuntu/interbotix_ws/install/bin"
