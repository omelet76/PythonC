import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers,)
    plt.show()

    keep_running = input('make another walk?(y/n):')
    if keep_running == 'n':
        break
