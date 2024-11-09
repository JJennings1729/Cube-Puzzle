# Solution to wooden block 17 puzzle from kubiyagames.com.

from PuzzleAlgorithm import CubePuzzle
import py5
import time

Puzzle = CubePuzzle()
BlockSize = 40
NumIter = 0
Begin = time.time()
print("Puzzle Solving...")

while not Puzzle.Solved:
    Puzzle.AssembleCube()
    print("Iteration " + str(NumIter))
    NumIter += 1

ElapsedTime = int(time.time()-Begin)
print("Puzzle solved in " + str(int(ElapsedTime/60)) + " min " + \
      str(ElapsedTime%60) + " sec with " + str(NumIter) + " iterations")

def setup():
    py5.size(900, 700, py5.P3D)
    py5.stroke_weight(4)


def draw():
    py5.translate(400,450,0)
    py5.background(255)
    py5.rotate_x(-py5.mouse_y/100)
    py5.rotate_y(py5.mouse_x/100)
    DrawPuzzle()

def DrawPuzzle():
    for F in Puzzle.Formation:
        Dimen = [A*BlockSize for A in Puzzle.BlockTypes[F[0]]]
        Orig = [A*BlockSize+D/2 for A,D in zip(F[1][0],Dimen)]
        py5.push_matrix()
        py5.translate(Orig[0],-Orig[1],Orig[2])
        py5.box(Dimen[0],Dimen[1],Dimen[2])
        py5.pop_matrix()

py5.run_sketch()