#!/bin/sh
#startup script
currentPath=$(pwd)

echo ""
echo "----------------------------------------------------------------"
echo "Noceur 1.0"
echo "Copyright (C) 2021 OWL Software"
echo "All Rights Reserved."
echo "----------------------------------------------------------------"

# Chcking if ROOTPATH var is set
if test "X$ROOTPATH" = "X" 
    then
        cd ..
        ROOTPATH=$(pwd)
fi
echo ""
echo Root Path home directory: $ROOTPATH

# Checking if python3 is installed

pythonVersion=$(python3 --version)

checkPython=$(grep "Python 3" <<<$pythonVersion >/dev/null && echo "Found" || echo "Not found")

if test "$checkPython" = "Not found"
    then

    echo "You do not have Python 3 in your system, please contact your system administrator"
    exit
fi

# Checking if python virtual environment exist

mainApp="$ROOTPATH/apps/main"

if [ -d "$mainApp" ];
then
   source ./apps/main/bin/activate
   checkVPythonVersion=$(python --version)
else 
    echo "Installing the Main App"
    Python3 -m venv ./apps/main
    source ./apps/main/bin/activate
    checkVPythonVersion=$(python --version)
    pip3 install -r $ROOTPATH/conf/dependencies.dat
fi

if test "$checkVPythonVersion" = "$pythonVersion"
then
echo ""
echo "-----------------------------------------------"
echo "App will start with $pythonVersion         "
echo "-----------------------------------------------"
echo ""
echo "Starting $checkVPythonVersion and Main App"
echo ""
Python $ROOTPATH/lib/engine.py 
fi