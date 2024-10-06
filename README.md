The SparseMatrix class represents a sparse matrix and includes methods for various matrix operations. Key functionalities and file organization are as follows:

Key Functionalities:
Initialization:

The constructor (__init__) can initialize a SparseMatrix either from a file path or by specifying the number of rows and columns directly.
Loading from File:

The load_from_file method reads the matrix from a file, extracting the number of rows and columns from the first two lines and the matrix entries (in the format (row, column, value)) from subsequent lines.
Handles and ignores any whitespaces in the file.
Raises a ValueError for incorrect file formats (e.g., wrong parentheses, floating-point values).
Element Access and Modification:

get_element: Returns the value at a specified matrix position, defaulting to 0 if the position is not explicitly set.
set_element: Sets the value at a specified position. Removes the entry if the value is 0 to maintain sparsity.
Matrix Operations:

add: Adds two sparse matrices.
subtract: Subtracts one sparse matrix from another.
multiply: Multiplies two sparse matrices.
These methods compute the result by iterating over non-zero elements of the matrices involved.
File Organization:
The main Python script sparse_matrix.py is located in /dsa/sparse_matrix/code/src/.
Sample input files and result files are stored in /dsa/sparse_matrix/sample_inputs/.
