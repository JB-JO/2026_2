import queue

MAZE_SIZE = 6

map = [ ['1', '1', '1', '1', '1', '1'],
        ['e', '0', '1', '0', '0', '1'],
        ['1', '0', '0', '0', '1', '1'],
        ['1', '0', '1', '0', '1', '1'],
        ['1', '0', '1', '0', '0', 'x'],
        ['1', '1', '1', '1', '1', '1'],]

def is_valid_pos(x, y):
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE :
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

def bfs():
    que = queue.Queue(maxsize=0)
    que.put((0,1))
    print('BFS: ')

    while not que.empty():
        here = que.get()
        print(here, end='->')
        (x,y) = here
        if(map[y][x] == 'x'): return True
        else:
            map[y][x] = '.'
            if is_valid_pos(x, y - 1): que.put((x, y - 1))
            if is_valid_pos(x, y + 1): que.put((x, y + 1))
            if is_valid_pos(x - 1, y): que.put((x - 1, y))
            if is_valid_pos(x + 1, y): que.put((x + 1, y))
    return False

result = bfs()
if result: print(' --> 미로탐색 성공')
else: print(' --> 미로탐색 실패')