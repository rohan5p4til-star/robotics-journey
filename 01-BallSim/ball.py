import matplotlib.pyplot as plt
#need to build a sim of a ball falling from a height and bouncing 

#physical constraints
g = -9.81
dt = 0.01

#initally
y = 10.0
v = 0
t = 0
t_end = 10.0
nsteps= int(t_end/dt)

#store
times = [t]
heights = [y]
for step in range(1,nsteps+1):
    v = v + (g*dt)
    y = y + v * dt
    t= step * dt
    print(t, v, y)
    times.append(t)
    heights.append(y)

#plotting
plt.plot(times, heights)
plt.xlabel("time (s)")
plt.ylabel("height (m)")
plt.title("Bouncing ball — Euler integration")
plt.show()