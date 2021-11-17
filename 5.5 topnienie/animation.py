import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

file = open("./output/topnienie_xyz_100.dat", "r")

config = file.readline().strip("\n").split(' ')
frames = int(config[0])
N = int(config[1])
tau = float(config[2])

p = np.zeros((frames, N, 3))

for f in range(frames):
    for i in range(N + 2):
        line = file.readline()
        if line == "":
            print(f"EMPTY LINE f:{f} i:{i}")
            exit(-1)
        if line != "\n":
            p[f][i] = [float(x) for x in line.split(' ')[:3]]

file.close()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# sphere
u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)

L = 2.3

def update(i):
    xs = [p_i[0] for p_i in p[i]]
    ys = [p_i[1] for p_i in p[i]]
    zs = [p_i[2] for p_i in p[i]]
    ax.clear()
    ax.scatter(xs, ys, zs)
    ax.set_title(f"time {'{:.6f}'.format(i * 10 * tau)} ps")
    ax.set_xlim3d(-L, L)
    ax.set_ylim3d(-L, L)
    ax.set_zlim3d(-L, L)
    ax.plot_wireframe(x * L, y * L, z * L, color="k", alpha=0.3, linewidth=1)


a = anim.FuncAnimation(fig, update, frames=frames)
# a.save(f'tau_{tau}_20fps.mp4', fps=20, dpi=600)
plt.show()
