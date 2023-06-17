Installation
----

ROS2 Galactic Installation
""""

To use the software, first install ROS2 Galactic on your Ubuntu 20.04 desktop environment.

.. code-block:: console

   sudo apt install software-properties-common
   sudo add-apt-repository universe
   sudo apt update && sudo apt install curl gnupg lsb-release
   sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
   sudo apt update # update your apt repo caches
   sudo apt install ros-galactic-desktop

Then source the setup of ROS2 on bash by running the following commands:

.. code-block:: console

   source /opt/ros/galactic/setup.bash
   echo "source /opt/ros/galactic/setup.bash" >> ~/.bashrc
   source ~/.bashrc


Run Some Examples
""""
To verify that ROS2 Galactic has been installed properly run the following commands:

.. code-block:: console

   ros2 run demo_nodes_cpp talker

The output should confirm that the talker is successfully publishing messages:

.. code-block:: console

   [INFO] [1652382860.246687611] [talker]: Publishing: 'Hello World: 1'
   [INFO] [1652382861.250208871] [talker]: Publishing: 'Hello World: 2'
   [INFO] [1652382862.246508551] [talker]: Publishing: 'Hello World: 3'
   ...

In another terminal window, run the example Python listener

.. code-block:: console

   ros2 run demo_nodes_py listener
   
The output should confirm that the listener is hearing the published messages:

.. code-block:: console

   [INFO] [1652382936.495044030] [listener]: I heard: [Hello World: 1]
   [INFO] [1652382937.478216343] [listener]: I heard: [Hello World: 2]
   [INFO] [1652382938.487370309] [listener]: I heard: [Hello World: 3]
   ...

If all the above steps worked and the listener node is printing messages to your console in sync with the talker node publishing them, ROS2 has been successfully installed.


.. note:: 
   
   Clone this repository before proceeding with next steps:

   .. code-block:: console

      cd ~/
      git clone https://github.com/VishalNadig/BELIV.git


UnrealEngine Setup
""""

1) Please visit: `Unreal Engine <https://www.unrealengine.com/en-US/ue-on-github>`_ for steps to get access to the UnrealEngine repository.
2) Clone the `Unreal Engine For CARLA GitHub <https://github.com/CarlaUnreal/UnrealEngine>`_ and check if you can see the UnrealEngine Repository.

.. code-block:: console
   
   cd ~/
   git clone https://github.com/CarlaUnreal/UnrealEngine
   cd ~/UnrealEngine

3) Then setup the UnrealEngine using the following commands:

.. code-block:: console

   ./Setup.sh && ./GenerateProjectFiles.sh && make
   mv ~/UnrealEngine ~/UnrealEngine-4.26

The installation takes over an hour or two to finish. Might be slower if your laptop has lower end specs.

4) Add UnrealEngine to environment variables

.. code-block:: console

   gedit ~/.bashrc

5) In the last line of the .bashrc file, write

.. code-block:: console

   export UE4_ROOT=~/UnrealEngine-4.26

Install and Build CARLA
""""

1) Downloading aria2 will speed up the following commands.

.. code-block:: console

   sudo apt-get install aria2

2) Install Ninja tool and clang-8 required to build the PythonAPI and the important python libraries using:

.. code-block:: console

   sudo apt install ninja-build
   sudo apt install clang-8
   pip install --user setuptools && pip3 install --user -Iv setuptools==67.8.0 && pip install --user distro && pip3 install --user distro && pip install --user wheel && pip3 install --user wheel auditwheel
   sudo apt install clang

3) Clone the CARLA repository found here: `CARLA GitHub <https://github.com/carla-simulator/carla.git>`_ into your home directory.
Then go into the carla repository that was just cloned and get the latest assets.

.. code-block:: console
   
   cd ~/
   git clone https://github.com/carla-simulator/carla.git
   cd ~/carla
   git checkout 0.9.13
   ./Update.sh

4) Compile the Python API client:

The Python API client grants control over the simulation. Compilation of the Python API client is required the first time you build CARLA and again after you perform any updates. After the client is compiled, you will be able to run scripts to interact with the simulation.

The following command compiles the Python API client:

.. code-block:: console

    make PythonAPI

While the above make command is running if you encounter a 404 not found error while downloading xerces-c3.2.3 then do the following, if not then skip this and go to step 5.
If xerces-c3.2.3 cannot be downloaded because of a 404 not found error then comment the following line found in line 432 in ~/carla/Util/BuildTools/Setup.sh

.. code-block:: console

   "XERCESC_REPO=https://ftp.cixug.es/apache//xerces/c/3/sources/xerces-c-${XERCESC_VERSION}.tar.gz"

and add the following line below it and run "make PythonAPI" from above command again

.. code-block:: console

   "XERCESC_REPO=https://archive.apache.org/dist/xerces/c/3/sources/xerces-c-${XERCESC_VERSION}.tar.gz"


5) Copy the carla-0.9.13-py3.7-linux-x86_64.egg file from BELIV/ to carla/PythonAPI/ folder.

.. code-block:: console

   cp ~/BELIV/carla-0.9.13-py3.7-linux-x86_64.egg ~/carla/PythonAPI/

6) Edit the .bashrc file to export the above .egg file to the PYTHONPATH variable:

.. code-block:: console

    echo "export PYTHONPATH=$PYTHONPATH:~/carla/PythonAPI/carla-0.9.13-py3.7-linux-x86_64.egg" >> ~/.bashrc

7) Compile the server:

The following command compiles and launches Unreal Engine. Run this command each time you want to launch the server or use the Unreal Engine editor:

.. code-block:: console

    make launch
    
The project may ask to build other instances such as UE4Editor-Carla.dll the first time. Agree in order to open the project. During the first launch, the editor may show warnings regarding shaders and mesh distance fields. These take some time to be loaded and the map will not show properly until then.

8) Go to the Edit>Editor Preferences option on the top left of the UnrealEngine Editor and go to Performance option on the left hand side of the screen. Uncheck "Use Less CPU when in background" option and close the Editor Preferences window. Now hit the Play button on the top of the UnrealEngine editor and wait for the simulation to start.

9) Open a new terminal by pressing Ctrl+Alt+T on the keyboard and navigate to the PythonAPI examples directory and run python examples:

.. code-block:: console

   cd ~/carla/PythonAPI/examples
   python3 dynamic_weather.py

This should change the weather in the simulation running in the UnrealEngine Editor. Weather effects such as cloudy and rain as well as change of day will occur.

10) Open a new terminal by pressing Ctrl+Alt+T on the keyboard and navigate to the PythonAPI examples directory and run python examples:

.. code-block:: console

   cd ~/carla/PythonAPI/examples
   python3 manual_control.py

The above command will open a seperate pygame window that will let you drive a car around the simulation. The pygame window represents a small portion of the simulation running in the UnrealEngine editor. Press ESC on the terminal on which the python3 manual_control.py was run to close the pygame window.

Troubleshooting
""""

If the simulation is bluish and and the colors are washed out or have a bright white hue to them and you have an Nvidia Graphic card then run the following
Verify that you have a Nvidia Graphic Card

.. code-block:: console

   lspci | grep -i nvidia

If you can see the words "Nvidia Controller" and the word Nvidia highlighted in red then you have an Nvidia graphic card. 

Download the drivers for Nvidia graphic card by running the following commands.

.. code-block:: console
   
   wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
   sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
   wget https://developer.download.nvidia.com/compute/cuda/12.1.1/local_installers/cuda-repo-ubuntu2004-12-1-local_12.1.1-530.30.02-1_amd64.deb
   sudo dpkg -i cuda-repo-ubuntu2004-12-1-local_12.1.1-530.30.02-1_amd64.deb
   sudo cp /var/cuda-repo-ubuntu2004-12-1-local/cuda-*-keyring.gpg /usr/share/keyrings/
   sudo apt-get update
   sudo apt-get -y install cuda

After the above steps restart your computer and the run the below command to verify that the drivers were updated successfully

.. code-block:: console
   
   nvidia-smi

CARLA in Docker
""""

To install CARLA in docker environment you will need two things:
   1) Docker
   2) Nvdia-Container-Toolkit

Docker Installation
''''

.. code-block:: console

   sudo apt-get remove docker docker-engine docker.io
   sudo apt-get update
   sudo apt install docker.io -y
   sudo snap install docker

Verify that docker was successfully installed on your system by running:

.. code-block:: console

   docker --version

Add docker to sudo group to avoid using sudo everytime to run docker commands:

.. code-block:: console

   sudo groupadd docker
   sudo usermod -aG docker $USER

Nvidia-Container-Toolkit Installation
''''
Nvidia Container Toolkit to give access to Linux Containers to the GPUs.

Add the nvidia-container-toolkit to apt list

.. code-block:: console

   distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
   && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
         sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
         sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

Update the sources list of apt to include the installation of nvidia-container-toolkit

.. code-block:: console

      sudo apt update

Install nvidia-container-toolkit

.. code-block:: console

      sudo apt install -y nvidia-container-toolkit







