import a_star
import dijkstra
import pygame
import algorithms

# pyGame Display Output
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
ROWS = 50

# Density Percentages
tenper = int(((ROWS * ROWS) / 100) * 10)
twentyper = int(((ROWS * ROWS) / 100) * 20)
thrityper = int(((ROWS * ROWS)/ 100) * 30)
fourtyper = int(((ROWS * ROWS) / 100) * 40)
fiftyper = int(((ROWS * ROWS) / 100) * 50)
sixtyper = int(((ROWS * ROWS)/ 100) * 60)
seventyper = int(((ROWS * ROWS) / 100) * 70)
eightyper = int(((ROWS * ROWS) / 100) * 80)
ninetyper = int(((ROWS * ROWS) / 100) * 90)

# Path Lengths
small = 10
medium = 25
large = 50


def algorithm_run(algorithm_type, density, path_distance, rows):
    path_list = []
    total_path = 0

    expanded_list = []
    total_expanded = 0

    for x in range(5):
        if algorithm_type == 1:
            algorithms.main(WIN, WIDTH, density, 1, path_distance, rows)
            path_list.append(a_star.path_count)
            expanded_list.append(a_star.expanded_count)
        elif algorithm_type == 2:
            algorithms.main(WIN, WIDTH, density, 2, path_distance, rows)
            path_list.append(dijkstra.path_count)
            expanded_list.append(dijkstra.expanded_count)

    for i in range(len(path_list)):
        total_path = total_path + path_list[i]
        total_expanded = total_expanded + expanded_list[i]

    average_path = total_path / (len(path_list))
    average_expanded = total_expanded / (len(expanded_list))

    print(path_list)
    if algorithm_type == 1:
        print(f"Average length of path is: {average_path} for A* Algorithm")
    elif algorithm_type == 2:
        print(f"Average length of path is: {average_path} for Dijkstra's Algorithm")
    print(expanded_list)
    if algorithm_type == 1:
        print(
            f"Average number of searched grids is: {average_expanded} for A* Algorithm for path length {path_distance} with obstacle density {density}")
    elif algorithm_type == 2:
        print(
            f"Average number of searched grids is: {average_expanded} for Dijkstra's Algorithm for path length of {path_distance} with obstacle density {density}")


def main():
    algorithm_run(1, fourtyper, large, ROWS)
    algorithm_run(2, fourtyper, small, ROWS)


if __name__ == "__main__":
    main()
