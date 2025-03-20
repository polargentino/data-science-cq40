NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n <= 0:
        return
        # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
        
        # move the nth disk from source to target
    target.append(source.pop())
        
        # display our progress
    print(A, B, C, '\n')
        
        # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)

# Salidas: 
# [5, 4, 3, 2] [] [1] 

# [5, 4, 3] [2] [1] 

# [5, 4, 3] [2, 1] [] 

# [5, 4] [2, 1] [3] 

# [5, 4, 1] [2] [3] 

# [5, 4, 1] [] [3, 2] 

# [5, 4] [] [3, 2, 1] 

# [5] [4] [3, 2, 1] 

# [5] [4, 1] [3, 2] 

# [5, 2] [4, 1] [3] 

# [5, 2, 1] [4] [3] 

# [5, 2, 1] [4, 3] [] 

# [5, 2] [4, 3] [1] 

# [5] [4, 3, 2] [1] 

# [5] [4, 3, 2, 1] [] 

# [] [4, 3, 2, 1] [5] 

# [1] [4, 3, 2] [5] 

# [1] [4, 3] [5, 2] 

# [] [4, 3] [5, 2, 1] 

# [3] [4] [5, 2, 1] 

# [3] [4, 1] [5, 2] 

# [3, 2] [4, 1] [5] 

# [3, 2, 1] [4] [5] 

# [3, 2, 1] [] [5, 4] 

# [3, 2] [] [5, 4, 1] 

# [3] [2] [5, 4, 1] 

# [3] [2, 1] [5, 4] 

# [] [2, 1] [5, 4, 3] 

# [1] [2] [5, 4, 3] 

# [1] [] [5, 4, 3, 2] 

# [] [] [5, 4, 3, 2, 1] 