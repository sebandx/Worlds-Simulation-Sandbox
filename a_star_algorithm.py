import heapq

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def find_path(grid, start, end):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    queue = [(0, start)]
    cost_map = {start: 0}
    parent_map = {start: None}

    while queue:
        cost, current = heapq.heappop(queue)

        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = parent_map[current]
            return path[::-1]  # Reverse the path

        for dx, dy in directions:
            next_x, next_y = current[0] + dx, current[1] + dy
            next_node = (next_x, next_y)

            if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid) and grid[next_y][next_x]:
                new_cost = cost_map[current] + 1
                if next_node not in cost_map or new_cost < cost_map[next_node]:
                    cost_map[next_node] = new_cost
                    priority = new_cost + heuristic(end, next_node)
                    heapq.heappush(queue, (priority, next_node))
                    parent_map[next_node] = current

    return []  # Return empty list if no path exists
