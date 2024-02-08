List = list


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        numOfIsland = int(0)

        # convert to list of int
        realMap = [[int(num) for num in row] for row in grid]

        xLength = len(realMap[0])  # -1
        yLength = len(realMap)  # -1

        # Returns the area of the land
        def landDetector(x: int, y: int) -> int:
            if x < 0 or x > xLength - 1:
                return 0
            if y < 0 or y > yLength - 1:
                return 0

            if flagMap[y][x]:  # FlagMap(x,y) == 1
                return 0
            elif not (flagMap[y][x]) and not (realMap[y][x]):  # 0 0
                flagMap[y][x] = 1
                return 0
            else:  # not flagged and realmap = 1
                flagMap[y][x] = 1
                return (
                    1
                    + landDetector(x+1,y)
                    + landDetector(x-1,y)
                    + landDetector(x,y+1)
                    + landDetector(x,y-1)
                )
            pass

        flagMap = [[0 for x in range(xLength)] for row in range(yLength)]

        for y, row in enumerate(realMap):
            for x, block in enumerate(row):
                if not (flagMap[y][x]) and realMap[y][x]:  # 0 1
                    # use the recursive function
                    landDetector(x, y)
                    numOfIsland += 1

        return numOfIsland