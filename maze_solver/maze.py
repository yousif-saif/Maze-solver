from collections import deque

maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', ' ', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

def find_shortest_path(start, end, maze):
    paths = []
    visited = set()
    rows = len(maze)
    cols = len(maze[0])


    def bfs(start, end):
        queue = deque()
        visited.add(start)
        queue.append((start, [start]))

        while queue:
            curr, path = queue.popleft()
            visited.add(curr)

            if curr == end:
                paths.append(path)

            else:
                i, j = curr[0], curr[1]

                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dx, dy in directions:
                    new_i, new_j = i + dx, j + dy

                    if new_i in range(rows) and new_j in range(cols) and (new_i, new_j) not in visited and maze[new_i][new_j] == " ":
                        queue.append(((new_i, new_j), path + [(new_i, new_j)]))
                        visited.add((new_i, new_j))
        
    
    bfs(start, end)
    min_path_index = 0

    for i in range(len(paths)):
        if len(paths[i]) < len(paths[min_path_index]):
            min_path_index = i

    for i in paths[min_path_index]:
        maze[i[0]][i[1]] = "X"
    
find_shortest_path((1, 1), (9, 8), maze)
for row in maze:
    print(' '.join(row))