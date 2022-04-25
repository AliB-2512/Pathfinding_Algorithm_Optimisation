import a_star
import dijkstra
import pygame
import algorithms
import weighted_a_star

# pyGame Display Output
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
ROWS = 50

# Density Percentages
tenper = int(((ROWS * ROWS) // 100) * 10)
twentyper = int(((ROWS * ROWS) // 100) * 20)
thrityper = int(((ROWS * ROWS) // 100) * 30)
fourtyper = int(((ROWS * ROWS) // 100) * 40)
fiftyper = int(((ROWS * ROWS) // 100) * 50)
sixtyper = int(((ROWS * ROWS) // 100) * 60)
seventyper = int(((ROWS * ROWS) // 100) * 70)
eightyper = int(((ROWS * ROWS) // 100) * 80)
ninetyper = int(((ROWS * ROWS) // 100) * 90)

# Node Differences
small = ROWS // 5
medium = ROWS // 2
large = ROWS

# Number of Tests
TESTS = 20


def algorithm_run(density, path_distance, rows, tests):
    a_star_path_list = []
    a_star_total_path = 0

    a_star_searched_list = []
    a_star_total_searched = 0

    dijkstra_path_list = []
    dijkstra_total_path = 0

    dijkstra_searched_list = []
    dijkstra_total_searched = 0

    w_a_star_path_list = []
    w_a_star_total_path = 0

    w_a_star_searched_list = []
    w_a_star_total_searched = 0

    for x in range(tests):
        algorithms.main(WIN, WIDTH, density, path_distance, rows)

        a_star_path_list.append(a_star.path_count)
        a_star_searched_list.append(a_star.searched_count)

        dijkstra_path_list.append(dijkstra.path_count)
        dijkstra_searched_list.append(dijkstra.searched_count)

        w_a_star_path_list.append(weighted_a_star.path_count)
        w_a_star_searched_list.append(weighted_a_star.searched_count)

    for i in range(len(a_star_path_list)):
        a_star_total_path = a_star_total_path + a_star_path_list[i]
        a_star_total_searched = a_star_total_searched + a_star_searched_list[i]

    for j in range(len(dijkstra_path_list)):
        dijkstra_total_path = dijkstra_total_path + dijkstra_path_list[j]
        dijkstra_total_searched = dijkstra_total_searched + dijkstra_searched_list[j]

    for k in range(len(w_a_star_path_list)):
        w_a_star_total_path = w_a_star_total_path + w_a_star_path_list[k]
        w_a_star_total_searched = w_a_star_total_searched + w_a_star_searched_list[k]

    a_star_average_path = a_star_total_path / (len(a_star_path_list))
    a_star_average_searched = a_star_total_searched / (len(a_star_searched_list))

    dijkstra_average_path = dijkstra_total_path / (len(dijkstra_path_list))
    dijkstra_average_searched = dijkstra_total_searched / (len(dijkstra_searched_list))

    w_a_star_average_path = w_a_star_total_path / (len(w_a_star_path_list))
    w_a_star_average_searched = w_a_star_total_searched / (len(w_a_star_searched_list))

    print(f"""
A* Algorithm:
{a_star_path_list}
The average path length is: {a_star_average_path}
{a_star_searched_list}
the average number of searched nodes is: {a_star_average_searched}
""")

    print(f"""
Dijkstra's Algorithm:
{dijkstra_path_list}
The average path length is: {dijkstra_average_path}
{dijkstra_searched_list}
the average number of searched nodes is: {dijkstra_average_searched}
""")

    print(f"""
A*(Weighted) Algorithm:
{w_a_star_path_list}
The average path length is: {w_a_star_average_path}
{w_a_star_searched_list}
the average number of searched nodes is: {w_a_star_average_searched}
""")


def main():
    algorithm_run(fourtyper, large, ROWS, TESTS)


if __name__ == "__main__":
    main()
