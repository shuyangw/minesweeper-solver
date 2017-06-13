# minesweeper-solver

## Changelog
### 6/13/17
Completed first working build. Can sometimes solve beginner boards with no usage of probabilistic methods, i.e. no guessing.

### 6/10/17
Fixed issue where creating a screenshot will throw unwanted exceptions.

### 6/8/17
Started work on the solving mechanism. Cleaned up some stuff.

### 6/7/17
Added auxiliary images to parse and finished the screen reading portion of the program.

### 6/4/17
Added class to draw lines, points and crosses.

### 6/2/17
Conformed to Python naming conventions. Added additional functionality to search.py so that it determines the number of tiles in the Minesweeper board

### 5/30/17
Added usages of numpy, scipy and Pillow libraries. Commit specifically added ways to take a screenshot of the main display and save it to a directory and converting an image to a numpy matrix with each node representing a pixel in a RGB 3-tuple. Also realized that the initial commit is basically useless.

### 4/28/17 - 4/29/17
Started project. Created some starting files and implemented a file input system for testing and a way to parse an input graph into an adjacency matrix.
