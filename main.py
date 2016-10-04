import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib import colors


def random_initial_state(n_cells=100, n_generations=100):
    first_row = np.random.random_integers(1, 2, size=(1, n_cells))
    spacetime = np.zeros(shape=(n_generations, n_cells))
    spacetime[0] = first_row

    return spacetime


def initialize(n_cells=0, n_generations=100, rule={}):
        initial_state = random_initial_state(n_cells, n_generations)

        cmap = colors.ListedColormap(['white', 'blue', 'grey'])
        bounds = [0, 1, 2, 2]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        fig = plt.figure()

        frame = plt.gca()
        frame.axes.get_xaxis().set_visible(False)
        frame.axes.get_yaxis().set_visible(False)

        grid = plt.imshow(initial_state, interpolation='nearest', cmap=cmap,
                          norm=norm)

        ani = animation.FuncAnimation(fig, next_generation,
                                      fargs=(grid, initial_state, rule),
                                      frames=n_generations - 1,
                                      interval=50,
                                      blit=False)

        plt.show()


def next_generation(i, grid, initial_state, rule):
    current_generation = initial_state[i]
    new_state = initial_state.copy()

    new_generation = process(current_generation, rule)

    new_state[i + 1] = new_generation

    grid.set_data(new_state)
    initial_state[:] = new_state[:]

    return grid,


def process(generation, rule):
    new_generation = []

    for i, cell in enumerate(generation):
        neighbours = []
        if i == 0:
            neighbours = [generation[len(generation) - 1], cell, generation[1]]
        elif i == len(generation) - 1:
            neighbours = [generation[len(generation) - 2], cell, generation[0]]
        else:
            neighbours = [generation[i - 1], cell, generation[i + 1]]

        new_generation.append(rule[tuple(neighbours)])

    return new_generation


def generate_rule(rule):
    rule_str = format(rule, '#010b')[2:]

    rule = {
        (2, 2, 2): int(rule_str[0]) + 1,
        (2, 2, 1): int(rule_str[1]) + 1,
        (2, 1, 2): int(rule_str[2]) + 1,
        (2, 1, 1): int(rule_str[3]) + 1,
        (1, 2, 2): int(rule_str[4]) + 1,
        (1, 2, 1): int(rule_str[5]) + 1,
        (1, 1, 2): int(rule_str[6]) + 1,
        (1, 1, 1): int(rule_str[7]) + 1
    }

    return rule


def main():
    n_cells = int(input("Number of cells: "))
    n_generations = int(input("Number of generations: "))
    rule = int(input("Rule number: "))
    rule = generate_rule(rule)
    initial_state = initialize(n_cells, n_generations, rule)

if __name__ == '__main__':
    main()
