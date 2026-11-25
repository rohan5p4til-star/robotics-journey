import numpy as np
import matplotlib.pyplot as plt

#need to build a sim of a ball falling from a height and bouncing moving right with vectors

#physical constraints
g = np.array([0.0, -9.81])
dt = 0.01

#to start
#y = 10 
pos = np.array([0.0,10.0])
vel = np.array([2.0,0.0])
#vy=0
#x = 0
#vx = 2
t = 0
t_end = 10.0
nsteps= round(t_end/dt)
energy_loss = 0.8

#motion
times = [t]
position = [pos.copy()]
#heights = [y]
#distance = [x]
for step in range(1,nsteps+1):
    #vy = vy + (g*dt)
    vel = vel + (g*dt)
    #y = y + vy * dt
    #x = x + vx * dt
    pos = pos + vel * dt
    if pos[1] < 0:
        pos[1] = 0
        vel[1] = (abs(vel[1])*energy_loss)
    t = step * dt
    print(t, vel, pos)
    times.append(t)
    position.append(pos.copy())
positions = np.array(position)
print(positions.shape)
#plotting
xs = positions[: , 0]   # all rows, column 0
ys = positions[: ,1 ]   # all rows, column 1
plt.plot(xs, ys)
plt.xlabel("distance (m)")
plt.ylabel("height (m)")
plt.title("Bouncing ball — Euler integration")
plt.show()