import pybullet as p # type: ignore
import time
import pybullet_data # type: ignore

# load the physics server
physics_client = p.connect(p.GUI)

# use additional robots + planes
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# set the gravity
p.setGravity(0, 0, -9.81) # x=0, y=0, z=-9.81

# load a world
pane_id = p.loadURDF("plane.urdf")

# give starting position to the robot
start_pos = [0, 0, 1]

# start orientation from euler to quaternions
start_orientation = p.getQuaternionFromEuler([0, 0, 0])

# load the urdf of the robot
box_id = p.loadURDF("r2d2.urdf", start_pos, start_orientation)

# use loops to control system
for _ in range(10000):
    # have the physics sim step
    p.stepSimulation()
    # make the time 
    time.sleep(1./240.)

p.disconnect()