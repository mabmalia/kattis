class Grid:
    # Constructor method
    def __init__(self, header):
        self.numberOfRows = int(header[0])
        self.numberOfCols = int(header[1])
        self.hasLand = False
        self.grid = []

    # Function to extract the input
    def getGrid(self):
        # Loop through the rows and columns to create a grid
        # check if the grid contains land
        for row in range(self.numberOfRows):
            self.grid.append(input())
            if self.hasLand == False:
                if self.grid[row].find("L") > -1:
                    self.hasLand = True

    # Implement depth first search algorithm (modified)
    # to find islands in the 4 adjacent nodes (horizontal and vertical)
    def findIslands(self, row, col):
        if row < 0 or row >= self.numberOfRows or col < 0 or col >= self.numberOfCols or self.grid[row][col] not in ["L","C"]:
            return
 
        # mark the node as visited
        self.grid[row] = self.grid[row][:col] + "V" + self.grid[row][col + 1:]
 
        # check neighbours
        self.findIslands(row - 1, col)
        self.findIslands(row, col - 1)
        self.findIslands(row, col + 1)
        self.findIslands(row + 1, col)

    # Function to count the number of islands	
    def countIslands(self):
        # Initialize count as 0 
        # and if there is land
        # then check all the cells of the matrix
        count = 0
        if self.hasLand != False:
            for row in range(self.numberOfRows):
                for col in range(self.numberOfCols):
                    # If a cell with value L is not visited yet,
                    # then new island found
                    if self.grid[row][col] == 'L':
                        # Visit all cells in this island
                        # and increment island count
                        self.findIslands(row, col)
                        count += 1
            
        return count

def main():
    grid = Grid(input().split())
    grid.getGrid()
    print(grid.countIslands())
	
if __name__ == "__main__":
	main()