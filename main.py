import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib import colors


def random_initial_state(n_cells=100, n_generations=100):
    first_row = np.random.random_integers(1, 2, size=(1, n_cells))
    spacetime = np.zeros(shape=(n_generations, n_cells))
    spacetime[0] = first_row

    return spacetime


def initialize(n_cells=0, n_generations=100):
        initial_state = random_initial_state(n_cells, n_generations)

        cmap = colors.ListedColormap(['gray', 'white', 'black'])
        bounds = [0, 1, 2, 2]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        fig = plt.figure()

        frame = plt.gca()
        frame.axes.get_xaxis().set_visible(False)
        frame.axes.get_yaxis().set_visible(False)

        grid = plt.imshow(initial_state, interpolation='nearest', cmap=cmap,
                          norm=norm)

        ani = animation.FuncAnimation(fig, next_generation,
                                      fargs=(grid, initial_state),
                                      frames=n_generations - 1,
                                      interval=50,
                                      blit=False)

        plt.show()


def next_generation(i, grid, initial_state):
    current_generation = initial_state[i]
    new_state = initial_state.copy()

    new_generation = process(current_generation)

    new_state[i + 1] = new_generation

    grid.set_data(new_state)
    initial_state[:] = new_state[:]

    return grid,


def process(generation):
    new_generation = []

    for i, cell in enumerate(generation):
        neighbours = []
        if i == 0:
            neighbours = [generation[len(generation) - 1], cell, generation[1]]
        elif i == len(generation) - 1:
            neighbours = [generation[len(generation) - 2], cell, generation[0]]
        else:
            neighbours = [generation[i - 1], cell, generation[i + 1]]

        new_generation.append(cell_in_next_generation(tuple(neighbours)))

    return new_generation


def cell_in_next_generation(neighbours):
    # Rule 18
    rule = {
        (2, 2, 2): 1,
        (2, 2, 1): 1,
        (2, 1, 2): 1,
        (2, 1, 1): 2,
        (1, 2, 2): 1,
        (1, 2, 1): 1,
        (1, 1, 2): 2,
        (1, 1, 1): 1
    }

    return rule[neighbours]


def main():
    n_cells = int(input("Number of cells: "))
    n_generations = int(input("Number of generations: "))
    initial_state = initialize(n_cells, n_generations)

if __name__ == '__main__':
    main()
