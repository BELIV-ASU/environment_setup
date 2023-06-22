#! bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt-get install aria2 -y
sudo apt install ninja-build -y
sudo apt install clang-8 -y
sudo apt install python-is-python3 -y
sudo apt install pip -y
sudo apt install clang

# ROS2 Galactic Installation
sudo apt install software-properties-common -y 
sudo add-apt-repository universe -y 
sudo apt update && sudo apt install curl gnupg lsb-release -y 
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg -y
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update # update your apt repo caches -y 
sudo apt install ros-galactic-desktop -y 
source /opt/ros/galactic/setup.bash
echo "source /opt/ros/galactic/setup.bash" >> ~/.bashrc
source ~/.bashrc

# UnrealEngine 4 setup
cd ~/
git clone https://github.com/VishalNadig/BELIV.git
cd ~/
git clone https://github.com/CarlaUnreal/UnrealEngine
cd UnrealEngine
./Setup.sh && ./GenerateProjectFiles.sh && make
mv ~/UnrealEngine ~/UnrealEngine-4.26

echo "export UE4_ROOT=~/UnrealEngine-4.26" >> ~/.bashrc

# Install and Build CARLA

pip install --user pygame numpy && pip3 install --user pygame numpy
pip install --user setuptools && pip3 install --user -Iv setuptools==67.8.0 && pip install --user distro && pip3 install --user distro && pip install --user wheel && pip3 install --user wheel auditwheel
cd ~/
git clone https://github.com/carla-simulator/carla.git
cd ~/carla
git checkout 0.9.13
./Update.sh

sed -i 's+XERCESC_REPO=https://ftp.cixug.es/apache//xerces/c/3/sources/xerces-c-${XERCESC_VERSION}.tar.gz+XERCESC_REPO=https://archive.apache.org/dist/xerces/c/3/sources/xerces-c-${XERCESC_VERSION}.tar.gz+g' ~/carla/Util/BuildTools/Setup.sh

make PythonAPI 
cp ~/BELIV/carla-0.9.13-py3.7-linux-x86_64.egg ~/carla/PythonAPI/ 
echo "export PYTHONPATH=$PYTHONPATH:~/carla/PythonAPI/carla-0.9.13-py3.7-linux-x86_64.egg" >> ~/.bashrc
make launch
