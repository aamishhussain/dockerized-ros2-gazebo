# Dockerized ROS2 Package Development Startpoint

This repository provides a Dockerized implementation of a starter codebase for rapid ROS2 package development. I created this for myself for quick development with gazebo. Just paste your ROS2 package code inside the ws_ros2_gazebo and build the Docker Image to start testing and developing.


## Aimed for (but can be easily changed):

- ROS2 development in WSL2
- python based ROS2 packeges
- Gazebo Simulation

## QuickStart:

### Clone the Repository

```bash
git clone https://github.com/aamishhussain/dockerized-ros2-gazebo.git
cd dockerized-ros2-gazebo
```

### Paste Your Executable ROS2 Code

Copy your ROS2 executable code files into the `ws_ros2_gazebo/src` directory:

```bash
cp /path/to/your/code/* ws_ros2_gazebo/src/
```

### Update `setup.py` and `package.xml`

Edit `setup.py` and `package.xml` in the `ws_ros2_gazebo/src` directory to reflect your package details and dependencies.

### Build the Docker Image

Run the following command inside the `environment` folder to build the Docker image:

```bash
docker compose build --no-cache
```

### Run the Docker Container

Start the Docker container using:

```bash
docker compose up -d
```

### Inside the Container

To get into the container:
```bash
docker exec -it <containerID> /bin/bash
```
Once inside:

```bash
source entrypont.sh
```

### Ready for testing!!!



## Acknowledgements

- [ROS2](https://docs.ros.org/en/) for the framework.
- [Docker](https://www.docker.com/) for containerized development.


