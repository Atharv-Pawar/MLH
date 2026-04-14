import pybullet as p # type: ignore
import time
import pybullet_data # type: ignore
import math 

class defineSimulation(): # class

    def __init__(self): # constructor
        # load physics server 
        self.physics_client = p.connect(p.GUI)
        # use data to call other objects like robots 
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # set the gravity
        p.setGravity(0, 0, -9,81)
        self.start_pos = ([0, 0, 1]) # starting position 
        self.start_orientation = p.getQuaternionFromEuler([0, 0, 0]) # get starting orientation
        self.plain_id = p.loadURDF("plain.urdf") # load the plane

    def spawn_robot(self, urdf):
        """
        Function that spwns URDF robots when callled
        """
        # load the robot as a box
        self.box_id = p.loadURDF(urdf, self.start_pos, self.start_orientation)

    def run_simulation(self):
        """
        Function that run the simulation
        """

        # our failsafe 
        for _ in range(100000):
            # do the step of the physics server 
            p.stepSimulation()
            # reduce the 240hz
            time.sleep(1./240.)
        
        # disconnect the server
        p.disconnect()

if __name__ == "__main__": # initialization 
    # create sim object
    simulator = defineSimulation()
    # spawn a robot
    simulator.spawn_robot("r2d2.urdf")
    # run the simulator
    simulator.run_simulation()
