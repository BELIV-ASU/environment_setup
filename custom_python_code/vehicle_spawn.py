"""Code to generate and spawn vehicles at specific points on the map in CARLA using PythonAPI
"""
import glob
import os
import numpy
import cv2
import queue
import sys
import math
import carla
from carla import Location, Rotation

try:
    sys.path.append(glob.glob("../carla/dist/carla-0.9.13-py3.8-linux-x86_64.egg"))
except IndexError:
    pass


def main() -> None:
    """Connect the client to the server running in localhost and generate and spawn the vehicles on the map in CARLA using the PythonAPI.
    """
    actor_list = []
    print("Starting connection...")
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(5.0)
        world = client.get_world()
        map = world.get_map()
        blueprint_library = world.get_blueprint_library()
        vehicle_bp = blueprint_library.filter('mustang_mache')[0]
        spawn_point = carla.Transform(Location(x=106.513153, y=-21.554596, z=0), Rotation(pitch=0.000000, yaw=-91.519577, roll=0.000000))
        print(f"Spawning vehicle {vehicle_bp} at {spawn_point}")
        vehicle = world.spawn_actor(vehicle_bp, spawn_point)

        actor_list.append(vehicle)


    finally:
        pass
        # client.apply_batch([carla.command.DestroyActor(x) for x in actor_list])


if __name__ == '__main__':
    main()
    
