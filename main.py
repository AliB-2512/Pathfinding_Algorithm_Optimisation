import a_star
import dijkstra
import pygame
import algorithms

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
tenper = 250
twentyper = 500
thrityper = 750
fourtyper = 1000
fiftyper = 1250
sixtyper = 1500
seventyper = 1750
eightyper = 2000
ninetyper = 2250


def algorithm_run(algorithm_type):
    path_list = []
    total_path = 0

    expanded_list = []
    total_expanded = 0

    for x in range(5):
        if algorithm_type == 1:
            algorithms.main(WIN, WIDTH, fourtyper, 1)
            path_list.append(a_star.path_count)
            expanded_list.append(a_star.expanded_count)
        elif algorithm_type == 2:
            algorithms.main(WIN, WIDTH, fourtyper, 2)
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
        print(f"Average number of searched grids is: {average_expanded} for A* Algorithm")
    elif algorithm_type == 2:
        print(f"Average number of searched grids is: {average_expanded} for Dijkstra's Algorithm")


def main():
    algorithm_run(1)
    algorithm_run(2)


if __name__ == "__main__":
    main()
