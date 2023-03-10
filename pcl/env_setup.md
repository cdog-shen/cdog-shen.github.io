# Point cloud lib environment setup

- install dependence

    ```sh
    sudo apt-get update  
    sudo apt-get install git build-essential linux-libc-dev -y
    sudo apt-get install cmake cmake-gui -y
    sudo apt-get install libusb-1.0-0-dev libusb-dev libudev-dev -y
    sudo apt-get install mpi-default-dev openmpi-bin openmpi-common  -y
    sudo apt-get install libflann1.9 libflann-dev -y
    sudo apt-get install libeigen3-dev  -y
    sudo apt-get install libboost-all-dev -y
    sudo apt-get install libvtk7.1-qt -y
    sudo apt-get install libvtk7.1  -y
    sudo apt-get install libvtk7-jni libvtk7-java libvtk7-dev libvtk7-qt-dev -y
    sudo apt-get install libqhull* libgtest-dev -y
    sudo apt-get install freeglut3-dev pkg-config -y
    sudo apt-get install libxmu-dev libxi-dev -y
    sudo apt-get install mono-complete -y
    sudo apt-get install openjdk-8-jdk openjdk-8-jre -y
    ```

- clone pcl source code

    ```sh
    git clone https://github.com/PointCloudLibrary/pcl.git 
    ```

- build executable file

    ```sh
    cd pcl 
    mkdir release 
    cd release
    cmake -DCMAKE_BUILD_TYPE=None -DCMAKE_INSTALL_PREFIX=/usr \ -DBUILD_GPU=ON-DBUILD_apps=ON -DBUILD_examples=ON \ -DCMAKE_INSTALL_PREFIX=/usr .. 
    make  
    ```

- make install

    ```sh
    sudo make install
    ```


