from queue import PriorityQueue

def heuristic(a, b):
    return abs(a - b)

def a_star(graph, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while not open_list.empty():
        current = open_list.get()[1]

        if current == goal:
            break

        for neighbor in graph[current]:
            new_cost = cost_so_far[current] + graph[current][neighbor]
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                open_list.put((priority, neighbor))
                came_from[neighbor] = current

    return came_from, cost_so_far

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(a_star(graph, 'A', 'D'))  # Salida: {'B': 'A', 'C': 'B', 'D': 'C'}, {'A': 0, 'B': 1, 'C': 3, 'D': 4}
