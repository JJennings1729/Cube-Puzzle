# Solution to wooden block 17 puzzle from kubiyagames.com.

class CubePuzzle():

    def __init__ (self):

        self.Cube = [[x,y,z] for x in range(5) for y in range(5) for z in range(5)]
        self.BlockTypes = [[2,2,3],[2,3,2],[3,2,2],[1,2,4],[1,4,2],[2,1,4],[2,4,1],[4,2,1],[4,1,2],[1,1,1]]
        self.NumBlocks = [[0,0,0,1,1,1,1,1,1,2],[6,6,5]]
        self.Formation = []
        self.Solved = False

    def BuildBlock (self, Corner, BlockType):  # Input Corner (3-ele list) and Blocktype (int index)
        Type = self.BlockTypes[BlockType]
        Cubies = [[x,y,z] for x in range(Type[0]) for y in range(Type[1]) for z in range(Type[2])]
        return [[A+B for A,B in zip(Corner,Cubie)] for Cubie in Cubies]

    def IsCorner (self, Cubie):  # Input Cubie (3-ele list)
        Neighbors = [[Cubie[C]-int(C==N) for C in range(3)] for N in range(3)]
        return not any([N in self.Cube for N in Neighbors]) and Cubie in self.Cube
    
    def PlaceBlock (self, Corner, StartType):  # Place a block by adding to formation array.

        if not self.Formation:
            if StartType == 1:
                StartType = 3
            if StartType == 4:
                StartType = 9

        for Type in range(StartType, 11):      # Try placing blocks at Corner starting with StartType.
            if Type == 10:                     # If nothing fits we end up returning True.
                return True
            if self.NumBlocks[1][self.NumBlocks[0][Type]] == 0:
                continue
            NewBlock = self.BuildBlock(Corner, Type)
            if any(N not in self.Cube for N in NewBlock):
                continue                             
            self.Formation.append([Type, NewBlock])
            self.NumBlocks[1][self.NumBlocks[0][Type]] -= 1
            self.Cube = [C for C in self.Cube if C not in NewBlock]
            break

    def RemoveBlock (self):   # Remove the last block in the Formation array.

        if not self.Formation:
            print("No solution found!")
            return None
        
        BlockType = self.Formation[-1][0]
        self.Cube.extend(self.Formation[-1][1])
        self.NumBlocks[1][self.NumBlocks[0][BlockType]] += 1
        self.Formation = self.Formation[:-1]

    def AssembleCube (self):
        for Cubie in self.Cube:
            if self.IsCorner(Cubie):
                if self.PlaceBlock(Cubie, 0): 
                    BackTrack = True
                    while BackTrack:
                        LastType = self.Formation[-1][0]
                        LastPlace = self.Formation[-1][1][0]
                        self.RemoveBlock()
                        if not self.PlaceBlock(LastPlace, LastType+1):
                            BackTrack = False
                elif not self.Cube:
                    print("Solution found!")
                    print(self.Formation) 
                    self.Solved = True