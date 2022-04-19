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
tenper = int(((ROWS * ROWS) / 100) * 10)
twentyper = int(((ROWS * ROWS) / 100) * 20)
thrityper = int(((ROWS * ROWS) / 100) * 30)
fourtyper = int(((ROWS * ROWS) / 100) * 40)
fiftyper = int(((ROWS * ROWS) / 100) * 50)
sixtyper = int(((ROWS * ROWS) / 100) * 60)
seventyper = int(((ROWS * ROWS) / 100) * 70)
eightyper = int(((ROWS * ROWS) / 100) * 80)
ninetyper = int(((ROWS * ROWS) / 100) * 90)

# Path Lengths
small = 10
medium = 25
large = 50


# noinspection PyStatementEffect
def algorithm_run(density, path_distance, rows):
    a_star_path_list = []
    a_star_total_path = 0

    a_star_expanded_list = []
    a_star_total_expanded = 0

    dijkstra_path_list = []
    dijkstra_total_path = 0

    dijkstra_expanded_list = []
    dijkstra_total_expanded = 0

    for x in range(5):
        algorithms.main(WIN, WIDTH, density, path_distance, rows)

        a_star_path_list.append(a_star.path_count)
        a_star_expanded_list.append(a_star.expanded_count)

        dijkstra_path_list.append(dijkstra.path_count)
        dijkstra_expanded_list.append(dijkstra.expanded_count)

    for i in range(len(a_star_path_list)):
        a_star_total_path = a_star_total_path + a_star_path_list[i]
        a_star_total_expanded = a_star_total_expanded + a_star_expanded_list[i]

    for j in range(len(dijkstra_path_list)):
        dijkstra_total_path = dijkstra_total_path + dijkstra_path_list[j]
        dijkstra_total_expanded = dijkstra_total_expanded + dijkstra_expanded_list[j]

    a_star_average_path = a_star_total_path / (len(a_star_path_list))
    a_star_average_expanded = a_star_total_expanded / (len(a_star_expanded_list))

    dijkstra_average_path = dijkstra_total_path / (len(dijkstra_path_list))
    dijkstra_average_expanded = dijkstra_total_expanded / (len(dijkstra_expanded_list))

    print(f"""
A* Algorithm:
{a_star_path_list}
The average path length is: {a_star_average_path}
{a_star_expanded_list}
the average number of searched nodes is: {a_star_average_expanded}
""")

    print(f"""
Dijkstra's Algorithm:
{dijkstra_path_list}
The average path length is: {dijkstra_average_path}
{dijkstra_expanded_list}
the average number of searched nodes is: {dijkstra_average_expanded}
""")


def main():
    algorithm_run(fourtyper, large, ROWS)


if __name__ == "__main__":
    main()
