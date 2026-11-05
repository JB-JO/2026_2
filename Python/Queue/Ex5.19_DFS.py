import queue

map = [ [ '1', '1', '1', '1', '1', '1'],
        [ 'e', '0', '0', '0', '0', '1' ],
        [ '1', '0', '1', '0', '1', '1' ],
        [ '1', '1', '1', '0', '0', 'x' ],
        [ '1', '1', '1', '0', '1', '1' ],
        [ '1', '1', '1', '1', '1', '1' ],]

MAZE_SIZE = 6

def is_valid_pos(x, y):
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE :
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

def dfs():
    print('DFS: ')
    stack = queue.LifoQueue(maxsize=0)
    stack.put((0,1))

    while not stack.empty():
        here = stack.get()
        print(here, end='->')
        (x,y) = here

        if(map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if is_valid_pos(x,y - 1): stack.put((x,y - 1))
            if is_valid_pos(x,y + 1): stack.put((x,y + 1))
            if is_valid_pos(x - 1,y): stack.put((x - 1,y))
            if is_valid_pos(x + 1,y): stack.put((x + 1,y))
        print('현재 스택: ', stack.queue)

    return False
result = dfs()
if result: print(' --> 미로탐색 성공')
else: print(' --> 미로탐색 실패')