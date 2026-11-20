import matplotlib.pyplot as plt
#need to build a sim of a ball falling from a height and bouncing moving right

#physical constraints
g = -9.81
dt = 0.01

#to start
y = 10 
vy=0
x = 0
vx = 2
t=0
t_end = 10.0
nsteps= round(t_end/dt)
energy_loss = 0.8

#motion
times = [t]
heights = [y]
distance = [x]
for step in range(1,nsteps+1):
    vy = vy + (g*dt)
    y = y + vy * dt
    x = x + vx * dt
    if y < 0:
        y = 0
        vy = (abs(vy)*energy_loss)
    t= step * dt
    print(t, vy, y, vx, x)
    times.append(t)
    heights.append(y)
    distance.append(x)

#plotting
plt.plot(distance, heights)
plt.xlabel("distance (m)")
plt.ylabel("height (m)")
plt.title("Bouncing ball — Euler integration")
plt.show()