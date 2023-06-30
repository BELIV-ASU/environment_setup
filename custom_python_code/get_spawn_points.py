"""
Python code to get valid spawn points around the map.
"""
import glob
import sys
import carla

try:
    sys.path.append(glob.glob("../carla/dist/carla-0.9.13-py3.8-linux-x86_64.egg"))
except IndexError:
    pass

def spawn_point():
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(5.0)
        world = client.get_world()
        spawn_points = world.get_map().get_spawn_points()
        for spawn_point in spawn_points:
            print(spawn_point)

    except Exception as exception:
        print(exception)

if __name__ == '__main__':
    spawn_point()
