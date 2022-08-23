## In this code , we use the A* algorithm which approximates the shortest distance between two points 
## https://github.com/melkir/A-Star-Python/blob/master/Algorithms.py
### http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
## https://www.youtube.com/watch?v=sAoBeujec74
##https://www.youtube.com/watch?v=eTx6HQ9Veas -- BEST WAY TO KNOW WHAT A* ALGORITHM IS ---
import math   # importing the library
import heapq
## a way to use priority queues this pops the smallest heap elements(https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/)
def shortest_path(M, start, goal): ## the main function
    def heuristic_distance(node1, node2):# Function for finding distance between nodes
        h_dist =  math.sqrt(((node1[0] - node2[0]) ** 2) + ((node1[1] - node2[1]) ** 2))
        ## the shortet distance is found using h_dist , using the mathamatical formula
        return h_dist

    def bestpath(parent, start, goal):## this gives us the best path we can use
        current = goal
        way = [current] ## a list is created where we store values of every place we go 
        
        while current != start: ## this is done till current is not start
            
            current = parent[current][1]
            
            way.append(current) ## this adds the current value into the end of the list, way
        way.reverse() ## this reverses the items in the list , so we go from start to goal
        return way
    
    ## NEXT , we have to create two lists , an open list and a closed list
    
    open_list = []
    ## open list is basically everywhere we can go to , all the possible nodes
    heapq.heapify(open_list) ## Converting this to a heap
    heapq.heappush(open_list, (0,start))## Putting the very first value in it. 
    
    ## heapify "heapifies" the open list and heappush "pops' the open list and puts a value in it 
   
    origin = {start: None} ## we create a dictionary to show where we came from 
    ## it is NONE as we want to don't want to start from anywhere , i.e , we want to originate from nowhere to the start position
    gscore = {start: 0}  

    while  open_list: ## runs till open_list doesn't return boolean false
        current= heapq.heappop(open_list)# assiging the value with minimum value and popping the open list

        if current[1] == goal: ## if current value is goal 
            bestpath(origin, start, goal)
            return bestpath(origin, start, goal)
        for i in M.roads[current[1]]:
            # for every node from our current node calculate its provisional gscore value.
            gscore_a = gscore[current[1]] + heuristic_distance(M.intersections[current[1]], M.intersections[i])
            ##we don't know the gscore so we calc a temporary one 
            ##
            
            if i not in gscore: # if this value is already not in gscore then calculate its heuristic value and put it in openlist.
                gscore[i] = gscore_a
                fscore = gscore_a + heuristic_distance(M.intersections[goal], M.intersections[i])
                heapq.heappush(open_list,(fscore,i))
                ##. heappush(heap, ele) :- This function is used to insert the element mentioned in its arguments into heap. The order is                   adjusted, so as heap structure is maintained.
                origin[i] = current 
                 
            if  gscore_a < gscore[i]:# if the calculated gscore is less than every gscore then proceed . 
                gscore[i] = gscore_a
                fscore = gscore_a + heuristic_distance(M.intersections[goal], M.intersections[i])
                            ##https://www.geeksforgeeks.org/a-search-algorithm/ ---> explanation 
                ## basically , f = g + h and we want minimum value of f to proced to the next cell
                heapq.heappush(open_list,(fscore,i))
                origin[i]= current
                

    return bestpath(origin, start, goal)# Return the path we traveled on.

   

