# 5. Acquire Regions on Board

# On a playing board which is represented by a 2D binary(containing 1 and 0) matrix M of size m x n,
# acquire all the regions surrounded by ‘1’.

# A region is captured by flipping all ‘0’s into ‘1’s in that surrounded region.

# 1 <= m, n <= 10

# NOTE: Surrounded region refer to only 4 directions - Top, Right, Bottom, Left.
# (Diagonals are not to be considered - TopRight, TopLeft, BottomRight, BottomLeft)

# Example Input

# Input 1:

# 4
# 4
# 1 1 1 1
# 1 0 1 1
# 1 1 0 1
# 1 0 1 1

# Example Output

# Output 1:

# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 0 1 1

# Explanation 1:

# 0 in (4, 2) is not surrounded by 1 from below, while 0 in (2, 2), (3, 3) are surrounded by 1 in all four directions
l = [[1, 0, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1]]
for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j], end=" ")
    print()
print('result::')
for i in range(1, len(l)-1):
    for j in range(1, len(l)-1):
        if l[i][j] == 0 and l[i-1][j] == 1 and l[i+1][j] == 1 and l[i][j-1] == 1 and l[i][j+1] == 1:
            l[i][j] = 1
for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j], end=" ")
    print()
