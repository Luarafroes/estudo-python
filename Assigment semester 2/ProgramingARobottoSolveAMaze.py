# maze_robot.py
from collections import deque
import heapq
from typing import List, Tuple, Dict, Optional

Coord = Tuple[int, int]          # (row, col)

# ──────────────────────────
# 1. Maze representation
# ──────────────────────────
class Maze:
    """2‑D grid maze.
       • 'S'  : start
       • 'G'  : goal
       • ' '  : free cell
       • '#'  : wall
    """
    def __init__(self, grid: List[str]) -> None:
        assert all(len(row) == len(grid[0]) for row in grid), "Rows must be equal length"
        self.grid = grid
        self.h, self.w = len(grid), len(grid[0])
        self.start, self.goal = self._find_special_cells()

    def _find_special_cells(self) -> Tuple[Coord, Coord]:
        start = goal = None
        for r, row in enumerate(self.grid):
            for c, ch in enumerate(row):
                if ch == 'S':
                    start = (r, c)
                elif ch == 'G':
                    goal = (r, c)
        if start is None or goal is None:
            raise ValueError("Maze must contain exactly one S and one G")
        return start, goal

    def in_bounds(self, rc: Coord) -> bool:
        r, c = rc
        return 0 <= r < self.h and 0 <= c < self.w

    def is_free(self, rc: Coord) -> bool:
        r, c = rc
        return self.in_bounds(rc) and self.grid[r][c] != '#'

    def neighbours(self, rc: Coord) -> List[Coord]:
        """4‑connected grid (N, E, S, W)."""
        r, c = rc
        deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        return [(r + dr, c + dc) for dr, dc in deltas if self.is_free((r + dr, c + dc))]

# ──────────────────────────
# 2. Utility: reconstruct path
# ──────────────────────────
def backtrace(parent: Dict[Coord, Coord], end: Coord) -> List[Coord]:
    path = [end]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    path.reverse()
    return path

# ──────────────────────────
# 3A. Right‑hand wall follower
# ──────────────────────────
turn_right = {(-1, 0):(0, 1), (0, 1):(1, 0), (1, 0):(0, -1), (0, -1):(-1, 0)}
turn_left  = {v:k for k, v in turn_right.items()}

def wall_follower(maze: Maze) -> List[Coord]:
    """Right‑hand rule. Assumes simply‑connected maze."""
    dir_vec = (0, 1)             # start facing East → →
    pos = maze.start
    parent = {pos: None}
    visited = set([pos])

    while pos != maze.goal:
        # Attempt to turn right, else go straight, else left, else back
        for turn in (turn_right, lambda d: d, turn_left, lambda d: turn_left[turn_left[d]]):
            new_dir = turn(dir_vec) if callable(turn) else turn[dir_vec]
            next_pos = (pos[0] + new_dir[0], pos[1] + new_dir[1])
            if maze.is_free(next_pos):
                dir_vec = new_dir
                pos = next_pos
                if pos not in parent:          # record first arrival
                    parent[pos] = parent[pos] if pos in parent else parent
                parent[pos] = list(parent.keys())[-1]  # previous position
                visited.add(pos)
                break
    return backtrace(parent, maze.goal)

# ──────────────────────────
# 3B. Depth‑First Search
# ──────────────────────────
def dfs(maze: Maze) -> List[Coord]:
    stack = [maze.start]
    parent = {maze.start: None}

    while stack:
        current = stack.pop()
        if current == maze.goal:
            return backtrace(parent, current)
        for nxt in maze.neighbours(current):
            if nxt not in parent:
                parent[nxt] = current
                stack.append(nxt)
    return []

# ──────────────────────────
# 3C. Breadth‑First Search
# ──────────────────────────
def bfs(maze: Maze) -> List[Coord]:
    q = deque([maze.start])
    parent = {maze.start: None}

    while q:
        current = q.popleft()
        if current == maze.goal:
            return backtrace(parent, current)
        for nxt in maze.neighbours(current):
            if nxt not in parent:
                parent[nxt] = current
                q.append(nxt)
    return []

# ──────────────────────────
# 3D. A★ Search (Manhattan heuristic)
# ──────────────────────────
def manhattan(a: Coord, b: Coord) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze: Maze) -> List[Coord]:
    open_heap = [(0 + manhattan(maze.start, maze.goal), 0, maze.start)]
    parent = {maze.start: None}
    gscore = {maze.start: 0}

    while open_heap:
        _, g, current = heapq.heappop(open_heap)
        if current == maze.goal:
            return backtrace(parent, current)

        for nxt in maze.neighbours(current):
            tentative_g = g + 1
            if tentative_g < gscore.get(nxt, float('inf')):
                gscore[nxt] = tentative_g
                f = tentative_g + manhattan(nxt, maze.goal)
                heapq.heappush(open_heap, (f, tentative_g, nxt))
                parent[nxt] = current
    return []

# ──────────────────────────
# 4. Pretty‑print utilities
# ──────────────────────────
def draw_path(maze: Maze, path: List[Coord]) -> None:
    grid = [list(row) for row in maze.grid]
    for r, c in path:
        if grid[r][c] in ' SG':
            grid[r][c] = '.'
    grid[maze.start[0]][maze.start[1]] = 'S'
    grid[maze.goal[0]][maze.goal[1]]  = 'G'
    print('\n'.join(''.join(row) for row in grid))

# ──────────────────────────
# 5. Demo
# ──────────────────────────
if __name__ == "__main__":
    raw_maze = [
        "#########################",
        "#S     #       #       G#",
        "# ### ### ### ### ##### #",
        "# #   #   # #   #   #   #",
        "# # ### ### ### ### ### #",
        "# # #   #   #   #   #   #",
        "# ### ### ### ### ### ###",
        "#     #   #   #     #   #",
        "#########################"
    ]
    maze = Maze(raw_maze)

    algorithms = [
        ("Wall Follower", wall_follower),
        ("Depth‑First Search", dfs),
        ("Breadth‑First Search", bfs),
        ("A★ Search", astar),
    ]

    for name, solver in algorithms:
        print(f"\n=== {name} ===")
        path = solver(maze)
        print(f"Path length: {len(path)} steps")
        draw_path(maze, path)
