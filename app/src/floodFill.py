from collections import deque 
DIRS=['N','E','S','W']
DIR_VECS = {'N': (-1, 0),'E': (0, 1),'S': (1, 0),'W': (0, -1)}


def floodFill(maze,start,end):
   
    rows = maze.rows
    cols = maze.cols
    cost=[[float('inf') for _ in range(cols)] for _ in range(rows)] #distance from each cell to the end coordinate
    end_row,end_col = end
    cost[end_row][end_col] = 0 #distance from end to itself is 0
    queue = deque([end])
    while queue:
        current_row,current_column = queue.popleft()
        for dir in DIRS:
            #checks if theres a wall in each direction
            if not maze.wall(current_row,current_column,dir):
                delta_row,delta_column = DIR_VECS[dir]
                neighbor_row,neighbor_column = current_row+delta_row,current_column+delta_column
                if maze.in_bounds(neighbor_row,neighbor_column):
                    #checks if the neighbor has a cost/been visited 
                    if cost[neighbor_row][neighbor_column] == float('inf'):
                        #sets the cost to the current cell + 1
                        cost[neighbor_row][neighbor_column] = cost[current_row][current_column] + 1
                        queue.append((neighbor_row,neighbor_column))
    
    
    path = [start] #path to be returned, itll be a list of coordinates
    current_row,current_column = start
    #this part actually moves along the best path
    while(current_row,current_column) != end:
        best_next=None
        lowest_cost = cost[current_row][current_column]
        #checks all the neighbors to find the lowest corst option
        for dir in DIRS:
            if not maze.wall(current_row,current_column,dir):
                delta_row,delta_column = DIR_VECS[dir]
                neighbor_row = current_row+delta_row
                neighbor_column = current_column+delta_column
                if maze.in_bounds(neighbor_row,neighbor_column) and cost[neighbor_row][neighbor_column] < lowest_cost:
                    best_next = (neighbor_row,neighbor_column)
                    lowest_cost = cost[neighbor_row][neighbor_column]
        if best_next:
            #moves to next cell if its better
            path.append(best_next)
            current_row,current_column = best_next
        else:
            #if it cant move anymore it breaks the loop
            break
    return path