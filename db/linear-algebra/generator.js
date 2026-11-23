// Seeded boundless generator for the Linear Algebra Database ("public" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-linear-algebra.js [seed]  (prints one JSON record)
// or: node gen-linear-algebra.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "linear-algebra";
const RECORD_KIND = "linear algebra record";
const ID_PREFIX = "JAH-LINALG-";
const AI_NAME = "JAH Linear Algebra Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Linear Algebra: Systems of Linear Equations",
    "subject": "systems of linear equations",
    "description": "A system of linear equations is a set of equations in which each equation is linear: each term is a constant times a single variable, with no products or powers of variables. The solution set is the set of assignments to the variables that satisfy every equation at once. A system has no solution, exactly one solution, or infinitely many. Gaussian elimination solves a system by adding multiples of equations to each other until the system is triangular. A system is inconsistent when elimination produces an equation such as 0 = 1. A free variable is one that can take any value, giving infinitely many solutions.",
    "inputs": "FIGURES = {'solution_x': 2, 'solution_y': 3, 'equations': 2, 'unknowns': 2, 'systems_shown': 3, 'free_variables': 1, 'sum_check': 5, 'difference_check': 1}\nLABEL = 'systems-of-linear-equations'\n",
    "expected": "count: 8\nlabel: systems-of-linear-equations\nmax: 5\nmean: 2.375\nmin: 1\ntotal: 19\nResult: count=8|label=systems-of-linear-equations|max=5|mean=2.375|min=1|total=19\nRun 1 SHA-256: 10b72aad420d079b56e2fde1226824b4850146cf9bf5b889ce1382c6856b743d\nRun 2 SHA-256: 10b72aad420d079b56e2fde1226824b4850146cf9bf5b889ce1382c6856b743d\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Vectors, Span, and Linear Independence",
    "subject": "vectors, span, and linear independence",
    "description": "A vector is a list of numbers, added entry by entry and scaled by multiplying every entry by the same number. The span of a set of vectors is the set of all their linear combinations (sums of scaled copies). A set of vectors is linearly independent when the only combination that gives the zero vector is the one with all coefficients zero. A vector is in the span of others when it can be written as a combination of them. A set containing the zero vector is always linearly dependent. In n-dimensional space, any set of more than n vectors is linearly dependent.",
    "inputs": "FIGURES = {'vectors_tested': 2, 'independent_pair': 2, 'dependent_pair': 2, 'span_dimension': 2, 'coefficients_zero': 2, 'plane_points': 2, 'line_dimension': 1, 'checks': 2}\nLABEL = 'vectors-span-and-linear-independence'\n",
    "expected": "count: 8\nlabel: vectors-span-and-linear-independence\nmax: 2\nmean: 1.875\nmin: 1\ntotal: 15\nResult: count=8|label=vectors-span-and-linear-independence|max=2|mean=1.875|min=1|total=15\nRun 1 SHA-256: 2e13b1bf720dae13bb8595d4829bc172fbadd0a8c8984db501e70158471a1515\nRun 2 SHA-256: 2e13b1bf720dae13bb8595d4829bc172fbadd0a8c8984db501e70158471a1515\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Bases and Dimension",
    "subject": "bases and dimension",
    "description": "A basis of a vector space is a linearly independent set that spans the whole space. The dimension of the space is the number of vectors in any basis: every basis of the same space has the same number of vectors. Coordinates are the coefficients of a vector in a given basis. Every vector in the space has exactly one expression as a combination of basis vectors. The standard basis of n-dimensional space is the vectors with a 1 in one place and 0 elsewhere. A basis can be extended: any independent set can be enlarged to a basis.",
    "inputs": "FIGURES = {'dimension_plane': 2, 'coordinates_x': 2, 'coordinates_y': 1, 'vector_x': 3, 'vector_y': 1, 'poly_dimension': 3, 'basis_vectors': 2, 'checks': 1}\nLABEL = 'bases-and-dimension'\n",
    "expected": "count: 8\nlabel: bases-and-dimension\nmax: 3\nmean: 1.875\nmin: 1\ntotal: 15\nResult: count=8|label=bases-and-dimension|max=3|mean=1.875|min=1|total=15\nRun 1 SHA-256: 04fa5b2c0b8fa7f89d142380608624020ab212e9b13cf34bc41cbb7de295b10e\nRun 2 SHA-256: 04fa5b2c0b8fa7f89d142380608624020ab212e9b13cf34bc41cbb7de295b10e\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Matrix Arithmetic",
    "subject": "matrix arithmetic",
    "description": "A matrix is a rectangular array of numbers, with rows and columns. Matrices are added entry by entry and multiplied by a number entry by entry. Matrix multiplication is defined when the number of columns of the first equals the number of rows of the second: the (i, j) entry of the product is the dot product (sum of pairwise products) of row i of the first with column j of the second. Matrix multiplication is associative but not commutative: AB is usually different from BA. The identity matrix has 1s on its diagonal and 0s elsewhere, and leaves any matrix unchanged on multiplying. The transpose of a matrix flips it across its diagonal, swapping rows and columns.",
    "inputs": "FIGURES = {'ab_11': 19, 'ab_12': 22, 'ab_21': 43, 'ab_22': 50, 'ba_11': 23, 'ba_22': 46, 'sum_11': 6, 'sum_22': 12}\nLABEL = 'matrix-arithmetic'\n",
    "expected": "count: 8\nlabel: matrix-arithmetic\nmax: 50\nmean: 27.625\nmin: 6\ntotal: 221\nResult: count=8|label=matrix-arithmetic|max=50|mean=27.625|min=6|total=221\nRun 1 SHA-256: e3876b55693b87188db13741099361117ac03e32f2533ead633de8146873c96d\nRun 2 SHA-256: e3876b55693b87188db13741099361117ac03e32f2533ead633de8146873c96d\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Matrix Inverses",
    "subject": "matrix inverses",
    "description": "The inverse of a square matrix A is a matrix A^-1 such that A times A^-1 and A^-1 times A both equal the identity matrix. A matrix has an inverse exactly when its determinant (a single number computed from its entries) is non-zero. The inverse solves the system A x = b as x = A^-1 b. A 2 by 2 matrix [[a, b], [c, d]] has inverse (1/(ad - bc)) times [[d, -b], [-c, a]], when ad - bc is not zero. The inverse of a product is the product of the inverses in reverse order. A singular matrix (determinant zero) has no inverse, and the system A x = b may have no solution or infinitely many.",
    "inputs": "FIGURES = {'determinant': 1, 'inv_11': 3, 'inv_12': -1, 'inv_21': -5, 'inv_22': 2, 'solution_x': 1, 'solution_y': 2, 'check_b1': 4}\nLABEL = 'matrix-inverses'\n",
    "expected": "count: 8\nlabel: matrix-inverses\nmax: 4\nmean: 0.875\nmin: -5\ntotal: 7\nResult: count=8|label=matrix-inverses|max=4|mean=0.875|min=-5|total=7\nRun 1 SHA-256: 72c33f3b71367cc81c32373b00cad5d1baac9c095d905bbdcd2e332c624bddb6\nRun 2 SHA-256: 72c33f3b71367cc81c32373b00cad5d1baac9c095d905bbdcd2e332c624bddb6\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Determinants",
    "subject": "determinants",
    "description": "The determinant is a single number assigned to a square matrix. For a 2 by 2 matrix [[a, b], [c, d]] it is ad - bc. Geometrically it is the factor by which the matrix scales areas (in two dimensions) or volumes (in three): a determinant of 2 doubles areas, a determinant of 0 collapses the plane onto a line or a point, and a negative determinant also flips orientation. A matrix is invertible exactly when its determinant is non-zero. The determinant of a product is the product of the determinants. The determinant of a triangular matrix is the product of its diagonal entries.",
    "inputs": "FIGURES = {'det_1': 10, 'det_singular': 0, 'det_identity': 1, 'det_2i': 8, 'scale_factor': 10, 'matrix_size': 2, 'rows': 2, 'cols': 2}\nLABEL = 'determinants'\n",
    "expected": "count: 8\nlabel: determinants\nmax: 10\nmean: 4.375\nmin: 0\ntotal: 35\nResult: count=8|label=determinants|max=10|mean=4.375|min=0|total=35\nRun 1 SHA-256: 2741ff4227087f9e348b27550401c8962c51d7ba6a833297de2920f5408d76d3\nRun 2 SHA-256: 2741ff4227087f9e348b27550401c8962c51d7ba6a833297de2920f5408d76d3\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Eigenvalues and Eigenvectors",
    "subject": "eigenvalues and eigenvectors",
    "description": "An eigenvector of a square matrix A is a non-zero vector v that A only scales: A v = lambda v, where the number lambda is the eigenvalue. Eigenvectors are the directions a transformation leaves unchanged in direction, and eigenvalues are the factors by which it stretches them. The eigenvalues are the roots of the characteristic polynomial, det(A - lambda I) = 0. A 2 by 2 matrix has at most 2 eigenvalues, counting multiplicity. Eigenvectors for distinct eigenvalues are linearly independent.",
    "inputs": "FIGURES = {'eigenvalue_1': 3, 'eigenvalue_2': 2, 'eigenvector_1_x': 1, 'eigenvector_1_y': 0, 'eigenvector_2_x': 1, 'eigenvector_2_y': -1, 'matrix_trace': 5, 'matrix_det': 6}\nLABEL = 'eigenvalues-and-eigenvectors'\n",
    "expected": "count: 8\nlabel: eigenvalues-and-eigenvectors\nmax: 6\nmean: 2.125\nmin: -1\ntotal: 17\nResult: count=8|label=eigenvalues-and-eigenvectors|max=6|mean=2.125|min=-1|total=17\nRun 1 SHA-256: d3b08119c2508d5e29c49f28a9a65c652dd5fb1eca0932c7616e1009330a7b7a\nRun 2 SHA-256: d3b08119c2508d5e29c49f28a9a65c652dd5fb1eca0932c7616e1009330a7b7a\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Diagonalisation",
    "subject": "diagonalisation of matrices",
    "description": "A square matrix A is diagonalisable when it can be written as P D P^-1, where D is a diagonal matrix (non-zero entries only on the diagonal) and P is the matrix whose columns are the eigenvectors. Then powers of A are easy: A to the power k equals P D^k P^-1, and D^k just raises the diagonal entries to the power k. A matrix is diagonalisable exactly when it has a full set of linearly independent eigenvectors. A matrix with n distinct eigenvalues is always diagonalisable. Symmetric matrices are always diagonalisable, with orthogonal eigenvectors.",
    "inputs": "FIGURES = {'eigenvalue_1': 3, 'eigenvalue_2': 2, 'a_squared_11': 9, 'a_squared_12': 5, 'a_squared_22': 4, 'trace': 5, 'determinant': 6, 'd_squared_11': 9}\nLABEL = 'diagonalisation-of-matrices'\n",
    "expected": "count: 8\nlabel: diagonalisation-of-matrices\nmax: 9\nmean: 5.375\nmin: 2\ntotal: 43\nResult: count=8|label=diagonalisation-of-matrices|max=9|mean=5.375|min=2|total=43\nRun 1 SHA-256: 9caca7f910ca6862cfe897496f71cc3208d5aacbd72b3d64e126fe462438531e\nRun 2 SHA-256: 9caca7f910ca6862cfe897496f71cc3208d5aacbd72b3d64e126fe462438531e\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Inner Products and Orthogonality",
    "subject": "inner products and orthogonality",
    "description": "An inner product is a way of multiplying two vectors to get a number, generalising the dot product: the dot product of (x1, x2) and (y1, y2) is x1 y1 + x2 y2. Two vectors are orthogonal (perpendicular) when their inner product is zero. The length of a vector is the square root of its inner product with itself. The Cauchy-Schwarz inequality says the absolute value of the inner product is at most the product of the lengths. An orthonormal set is a set of mutually orthogonal vectors, each of length 1. The projection of one vector onto another is the closest point on the other's line.",
    "inputs": "FIGURES = {'dot_product': 0, 'length_u': 5, 'length_v': 5, 'projection_x': 1.32, 'projection_y': 1.76, 'w_dot_u': 11, 'u_dot_u': 25, 'vectors_checked': 3}\nLABEL = 'inner-products-and-orthogonality'\n",
    "expected": "count: 8\nlabel: inner-products-and-orthogonality\nmax: 25\nmean: 6.51\nmin: 0\ntotal: 52.08\nResult: count=8|label=inner-products-and-orthogonality|max=25|mean=6.51|min=0|total=52.08\nRun 1 SHA-256: 8e3a621a5dc95dcc8181ec698caea8a0460d1bb7e1f182d62d61787003474939\nRun 2 SHA-256: 8e3a621a5dc95dcc8181ec698caea8a0460d1bb7e1f182d62d61787003474939\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Orthogonal Projections and Least Squares",
    "subject": "orthogonal projections and least squares",
    "description": "The orthogonal projection of a vector onto a subspace is the closest point in the subspace to the vector. Least squares fits a line (or another model) to data by minimising the sum of the squares of the errors (the differences between the observed and predicted values); the solution is the projection of the data vector onto the column space of the design matrix. The projection is the unique point in the subspace whose difference from the vector is orthogonal to the subspace. The normal equations A^T A x = A^T b give the least-squares solution. The residual (the difference between the data and the fit) is orthogonal to every column of A.",
    "inputs": "FIGURES = {'intercept': 1.1667, 'slope': 1.5, 'residual_sum_squares': 0.1667, 'residual_1': -0.1667, 'residual_2': 0.3333, 'residual_3': -0.1667, 'points_fitted': 3, 'parameters': 2}\nLABEL = 'orthogonal-projections-and-least-squares'\n",
    "expected": "count: 8\nlabel: orthogonal-projections-and-least-squares\nmax: 3\nmean: 0.9792\nmin: -0.1667\ntotal: 7.8333\nResult: count=8|label=orthogonal-projections-and-least-squares|max=3|mean=0.9792|min=-0.1667|total=7.8333\nRun 1 SHA-256: 17103fa3fbe3a72976c5b046d274fbec60e42013a7eba6f6a9c455a5e63a5ed0\nRun 2 SHA-256: 17103fa3fbe3a72976c5b046d274fbec60e42013a7eba6f6a9c455a5e63a5ed0\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: The Rank of a Matrix",
    "subject": "rank of a matrix",
    "description": "The rank of a matrix is the dimension of its column space (the span of its columns), which equals the dimension of its row space. It counts the number of independent directions the matrix preserves. A square matrix is invertible exactly when its rank equals its size. The rank is the number of pivots (leading entries) in the row-echelon form. The rank-nullity theorem says rank plus nullity (the dimension of the solution space of A x = 0) equals the number of columns. The rank of a product is at most the smaller of the ranks of the factors.",
    "inputs": "FIGURES = {'rank': 2, 'rows': 3, 'cols': 3, 'nullity': 1, 'pivots': 2, 'null_vector_x': 1, 'null_vector_y': -2, 'null_vector_z': 1}\nLABEL = 'rank-of-a-matrix'\n",
    "expected": "count: 8\nlabel: rank-of-a-matrix\nmax: 3\nmean: 1.375\nmin: -2\ntotal: 11\nResult: count=8|label=rank-of-a-matrix|max=3|mean=1.375|min=-2|total=11\nRun 1 SHA-256: 727862885331b4ed10efa8bbf5ac8de9989a306889488691aa95df23a8be3372\nRun 2 SHA-256: 727862885331b4ed10efa8bbf5ac8de9989a306889488691aa95df23a8be3372\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Linear Transformations",
    "subject": "linear transformations",
    "description": "A linear transformation is a function between vector spaces that preserves addition and scaling: T(u + v) = T(u) + T(v) and T(c u) = c T(u). Every linear transformation between finite-dimensional spaces is given by a matrix, and the matrix's columns are the images of the basis vectors. Rotation, reflection, scaling, and projection are all linear transformations. The kernel of a transformation is the set of vectors it sends to zero; the image is the set of outputs. A transformation is one-to-one exactly when its kernel contains only the zero vector.",
    "inputs": "FIGURES = {'rotation_degrees': 90, 'image_x': -4, 'image_y': 3, 'length_before': 5, 'length_after': 5, 'dot_product': 0, 'matrix_entries': 4, 'basis_images': 2}\nLABEL = 'linear-transformations'\n",
    "expected": "count: 8\nlabel: linear-transformations\nmax: 90\nmean: 13.125\nmin: -4\ntotal: 105\nResult: count=8|label=linear-transformations|max=90|mean=13.125|min=-4|total=105\nRun 1 SHA-256: 0b07d88f90839bc3978516ae9868e7d764a75282572d973793132704237147a0\nRun 2 SHA-256: 0b07d88f90839bc3978516ae9868e7d764a75282572d973793132704237147a0\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Change of Basis",
    "subject": "change of basis",
    "description": "A change of basis rewrites the coordinates of a vector, or the matrix of a transformation, in a new basis. If P is the matrix whose columns are the new basis vectors written in the old basis, then the new coordinates are P^-1 times the old coordinates, and the new matrix of a transformation is P^-1 A P. The change-of-basis matrix P has the new basis vectors as its columns. Similar matrices (related by P^-1 A P) have the same eigenvalues, trace, and determinant. Choosing a good basis can diagonalise a matrix, making it easy to work with.",
    "inputs": "FIGURES = {'new_coord_1': 2, 'new_coord_2': 1, 'old_coord_1': 3, 'old_coord_2': 1, 'det_p': -2, 'basis_vectors': 2, 'inverse_factor': 0.5, 'checks': 1}\nLABEL = 'change-of-basis'\n",
    "expected": "count: 8\nlabel: change-of-basis\nmax: 3\nmean: 1.0625\nmin: -2\ntotal: 8.5\nResult: count=8|label=change-of-basis|max=3|mean=1.0625|min=-2|total=8.5\nRun 1 SHA-256: df112d418075999471abd9cddbc934fa16b4481455a99c85816be8793902b88f\nRun 2 SHA-256: df112d418075999471abd9cddbc934fa16b4481455a99c85816be8793902b88f\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: The Singular Value Decomposition",
    "subject": "the singular value decomposition",
    "description": "The singular value decomposition (SVD) writes any matrix A as U times Sigma times V^T, where U and V are orthogonal matrices (their columns are orthonormal) and Sigma is diagonal with non-negative entries, the singular values, in decreasing order. It is the generalisation of diagonalisation to non-square matrices. The singular values are the square roots of the eigenvalues of A^T A. The best rank-k approximation to A is obtained by keeping the k largest singular values. The SVD gives the least-squares solution, the pseudoinverse, and the principal components of data.",
    "inputs": "FIGURES = {'singular_1': 3, 'singular_2': 2, 'rank1_error': 2, 'singular_2nd_example_1': 2, 'singular_2nd_example_2': 0, 'rank_of_example': 1, 'matrices_factored': 3, 'values_kept': 1}\nLABEL = 'the-singular-value-decomposition'\n",
    "expected": "count: 8\nlabel: the-singular-value-decomposition\nmax: 3\nmean: 1.75\nmin: 0\ntotal: 14\nResult: count=8|label=the-singular-value-decomposition|max=3|mean=1.75|min=0|total=14\nRun 1 SHA-256: e1212a7f9ca6265a0c2181295b6e6419a2b86ded362ff640dd620e1bfaab9b06\nRun 2 SHA-256: e1212a7f9ca6265a0c2181295b6e6419a2b86ded362ff640dd620e1bfaab9b06\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Vector Spaces over General Fields",
    "subject": "vector spaces over general fields",
    "description": "A vector space is defined over a field (a number system where addition, subtraction, multiplication, and division by non-zero elements work, such as the rationals, reals, or complex numbers). The same axioms (rules) apply: the field supplies the scalars (the numbers that scale vectors), and the vectors satisfy the eight vector-space axioms. The real numbers, the rational numbers, and the complex numbers are all fields. The integers are not a field, because division by a non-zero integer need not give an integer. Finite fields, with finitely many elements, are used in coding theory and cryptography.",
    "inputs": "FIGURES = {'field_size': 2, 'vector_count': 8, 'dimension': 3, 'subspaces_2d': 7, 'basis_vectors': 3, 'sum_example': 6, 'string_length': 3, 'axioms': 8}\nLABEL = 'vector-spaces-over-general-fields'\n",
    "expected": "count: 8\nlabel: vector-spaces-over-general-fields\nmax: 8\nmean: 5.0\nmin: 2\ntotal: 40\nResult: count=8|label=vector-spaces-over-general-fields|max=8|mean=5.0|min=2|total=40\nRun 1 SHA-256: 1fe89f170d71a4710cc0aeb7b5abfb71ebc473fc4202e1d61c42ac3369a995ec\nRun 2 SHA-256: 1fe89f170d71a4710cc0aeb7b5abfb71ebc473fc4202e1d61c42ac3369a995ec\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Quadratic Forms",
    "subject": "quadratic forms",
    "description": "A quadratic form is a homogeneous polynomial of degree 2 in several variables, such as 3x squared + 2xy + 3y squared. It is written as x^T A x for a symmetric matrix A, and its shape is read from the eigenvalues of A: all positive means a bowl, mixed signs means a saddle. A symmetric matrix is diagonalisable by an orthogonal change of basis. A quadratic form is positive definite when it is positive for every non-zero vector. The principal axes of the form are the eigenvectors of its matrix.",
    "inputs": "FIGURES = {'eigenvalue_1': 4, 'eigenvalue_2': 2, 'value_at_1_1': 8, 'value_at_1_minus1': 4, 'min_on_circle': 2, 'max_on_circle': 4, 'matrix_entries': 4, 'variables': 2}\nLABEL = 'quadratic-forms'\n",
    "expected": "count: 8\nlabel: quadratic-forms\nmax: 8\nmean: 3.75\nmin: 2\ntotal: 30\nResult: count=8|label=quadratic-forms|max=8|mean=3.75|min=2|total=30\nRun 1 SHA-256: 7aa95eaabab0accb04edad961dc3f5c418005139d38053a47fb459708e587a46\nRun 2 SHA-256: 7aa95eaabab0accb04edad961dc3f5c418005139d38053a47fb459708e587a46\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Linear Algebra in Computer Graphics",
    "subject": "linear algebra in computer graphics",
    "description": "Computer graphics is linear algebra made visible: points are vectors, rotations and scalings are matrices, and the picture on the screen is the result of multiplying the scene's vectors by a chain of matrices (model, view, and projection). Homogeneous coordinates add a fourth coordinate so that translations can also be written as matrices. A rotation matrix turns a shape; a scaling matrix stretches it; a translation matrix moves it. Homogeneous coordinates use 4 numbers for a 3D point, so translation becomes a matrix multiplication. The projection matrix turns 3D coordinates into 2D screen coordinates.",
    "inputs": "FIGURES = {'rotation_result_x': 0, 'rotation_result_y': 1, 'scale_result_x': 2, 'scale_result_y': 3, 'composed_result_x': 0, 'composed_result_y': 3, 'matrix_size': 4, 'coordinates_used': 4}\nLABEL = 'linear-algebra-in-computer-graphics'\n",
    "expected": "count: 8\nlabel: linear-algebra-in-computer-graphics\nmax: 4\nmean: 2.125\nmin: 0\ntotal: 17\nResult: count=8|label=linear-algebra-in-computer-graphics|max=4|mean=2.125|min=0|total=17\nRun 1 SHA-256: e195a9e9e4acc4982259fa809ba6d6a4a2d84ed4716d1195d9a4ea894af09c9f\nRun 2 SHA-256: e195a9e9e4acc4982259fa809ba6d6a4a2d84ed4716d1195d9a4ea894af09c9f\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Markov Chains",
    "subject": "Markov chains",
    "description": "A Markov chain is a system that moves between states with fixed probabilities, where the next state depends only on the current state. Its transition matrix has columns (or rows) that sum to 1, and the long-run behaviour is given by the steady-state vector, an eigenvector with eigenvalue 1. The transition matrix is stochastic: its entries are probabilities that sum to 1 in each column. The steady-state vector satisfies P v = v and its entries sum to 1. A regular chain converges to its steady state regardless of the starting distribution.",
    "inputs": "FIGURES = {'sunny_prob': 0.8, 'rainy_prob': 0.6, 'steady_sunny': 0.6667, 'steady_rainy': 0.3333, 'states': 2, 'eigenvalue_1': 1, 'eigenvalue_2': 0.4, 'days_modelled': 2}\nLABEL = 'markov-chains'\n",
    "expected": "count: 8\nlabel: markov-chains\nmax: 2\nmean: 0.975\nmin: 0.3333\ntotal: 7.8\nResult: count=8|label=markov-chains|max=2|mean=0.975|min=0.3333|total=7.8\nRun 1 SHA-256: b2bb7ee78ea56c5921a9eddc72607d70dced910b5fb7880bf1fb5c0664d4485c\nRun 2 SHA-256: b2bb7ee78ea56c5921a9eddc72607d70dced910b5fb7880bf1fb5c0664d4485c\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: The Geometry of Linear Maps",
    "subject": "the geometry of linear maps",
    "description": "A linear map in the plane is understood by its action on the unit square: the image is a parallelogram, and the determinant is the signed area of that parallelogram. A map with determinant 2 doubles areas; with determinant 0 it flattens the square onto a line; with a negative determinant it flips the square over. The image of the unit square under a matrix is the parallelogram spanned by the matrix's columns. The determinant is the signed area of that parallelogram. An orthogonal matrix preserves lengths and angles: it is a rotation or a reflection.",
    "inputs": "FIGURES = {'determinant': 4, 'area': 4, 'vertices': 4, 'image_x_1': 2, 'image_y_1': 0, 'image_x_2': 1, 'image_y_2': 2, 'columns': 2}\nLABEL = 'the-geometry-of-linear-maps'\n",
    "expected": "count: 8\nlabel: the-geometry-of-linear-maps\nmax: 4\nmean: 2.375\nmin: 0\ntotal: 19\nResult: count=8|label=the-geometry-of-linear-maps|max=4|mean=2.375|min=0|total=19\nRun 1 SHA-256: 35ab675871fd771de8350f6a4a6eb3fda599166f9da9bbf81b2afdb7493a1540\nRun 2 SHA-256: 35ab675871fd771de8350f6a4a6eb3fda599166f9da9bbf81b2afdb7493a1540\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Solving Least Squares by QR",
    "subject": "solving least squares by QR factorisation",
    "description": "The QR factorisation writes a matrix A as Q times R, where Q has orthonormal columns and R is upper triangular (non-zero entries only on and above the diagonal). Least squares is then solved by a triangular system, which is fast and numerically stable. It is the preferred method in practice over the normal equations. The columns of Q are obtained by Gram-Schmidt orthogonalisation of the columns of A. R is upper triangular, so R x = Q^T b is solved by back-substitution. QR avoids forming A^T A, whose condition number (a measure of sensitivity to error) is the square of A's.",
    "inputs": "FIGURES = {'intercept': 1.1667, 'slope': 1.5, 'first_col_length': 1.732, 'rows': 3, 'cols': 2, 'residual_sum_squares': 0.1667, 'q_columns': 2, 'r_size': 2}\nLABEL = 'solving-least-squares-by-qr-factorisation'\n",
    "expected": "count: 8\nlabel: solving-least-squares-by-qr-factorisation\nmax: 3\nmean: 1.6957\nmin: 0.1667\ntotal: 13.5654\nResult: count=8|label=solving-least-squares-by-qr-factorisation|max=3|mean=1.6957|min=0.1667|total=13.5654\nRun 1 SHA-256: 5494ff66118338d8f966429b98605942b4a0afde7aeb01fb57dca05f5a480791\nRun 2 SHA-256: 5494ff66118338d8f966429b98605942b4a0afde7aeb01fb57dca05f5a480791\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Dual Spaces and Linear Functionals",
    "subject": "dual spaces and linear functionals",
    "description": "A linear functional is a linear map from a vector space to its field of scalars: it assigns a number to each vector, linearly. The dual space is the space of all linear functionals on a given space. In finite dimensions, the dual space has the same dimension as the original, and every functional is given by a dot product with a fixed vector. A linear functional satisfies f(u + v) = f(u) + f(v) and f(c u) = c f(u). The dual basis is the set of functionals that pick out the coordinates in a given basis. The double dual (the dual of the dual) is naturally the original space.",
    "inputs": "FIGURES = {'f_at_1_0': 2, 'f_at_0_1': 3, 'f_at_2_1': 7, 'dual_dimension': 2, 'functionals_in_dual_basis': 2, 'coordinates_picked': 2, 'linearity_checks': 2, 'dot_vector_x': 2}\nLABEL = 'dual-spaces-and-linear-functionals'\n",
    "expected": "count: 8\nlabel: dual-spaces-and-linear-functionals\nmax: 7\nmean: 2.75\nmin: 2\ntotal: 22\nResult: count=8|label=dual-spaces-and-linear-functionals|max=7|mean=2.75|min=2|total=22\nRun 1 SHA-256: 26add28ae48b3b8b42eeb871d943d20b32741011c462dc1715a1729bf7d81a28\nRun 2 SHA-256: 26add28ae48b3b8b42eeb871d943d20b32741011c462dc1715a1729bf7d81a28\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: The Gram-Schmidt Process",
    "subject": "the Gram-Schmidt process",
    "description": "The Gram-Schmidt process turns a list of independent vectors into an orthonormal list (vectors of length 1, pairwise perpendicular) spanning the same space, by subtracting the projections onto the vectors already built. It is the algorithm behind QR factorisation and the construction of orthonormal bases. Each new vector has its projections onto the earlier ones subtracted. The result is normalised to length 1. The process keeps the span: the new list spans the same space as the old.",
    "inputs": "FIGURES = {'u1_dot_u1': 2, 'projection_factor': 0.5, 'u2_x': 0.5, 'u2_y': -0.5, 'u2_z': 1, 'u2_norm': 1.225, 'e1_x': 0.707, 'e2_z': 0.816}\nLABEL = 'the-gram-schmidt-process'\n",
    "expected": "count: 8\nlabel: the-gram-schmidt-process\nmax: 2\nmean: 0.781\nmin: -0.5\ntotal: 6.248\nResult: count=8|label=the-gram-schmidt-process|max=2|mean=0.781|min=-0.5|total=6.248\nRun 1 SHA-256: b40c90a293395f656332a87c207673bc4176b8dd179a2456ed2b0423f1017fcf\nRun 2 SHA-256: b40c90a293395f656332a87c207673bc4176b8dd179a2456ed2b0423f1017fcf\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Orthogonal Matrices and Rotations",
    "subject": "orthogonal matrices and rotations",
    "description": "An orthogonal matrix is a square matrix whose columns (and rows) are orthonormal: Q^T Q = I. Orthogonal matrices preserve lengths and angles, and their determinant is +1 or -1. Rotations and reflections are the orthogonal matrices; a rotation has determinant +1. Q^T Q = I: the columns are orthonormal. Orthogonal matrices preserve lengths: |Qx| = |x|. Rotations have determinant +1; reflections have determinant -1.",
    "inputs": "FIGURES = {'cos30': 0.866, 'sin30': 0.5, 'det': 1, 'column_length': 1, 'dot_product': 0, 'rotated_x': 0.866, 'rotated_y': 0.5, 'angle_deg': 30}\nLABEL = 'orthogonal-matrices-and-rotations'\n",
    "expected": "count: 8\nlabel: orthogonal-matrices-and-rotations\nmax: 30\nmean: 4.3415\nmin: 0\ntotal: 34.732\nResult: count=8|label=orthogonal-matrices-and-rotations|max=30|mean=4.3415|min=0|total=34.732\nRun 1 SHA-256: 84162122d6a97a32dccc0bcf2e64ec9f95d0c5f3c832c3da129f87b3657c9f8e\nRun 2 SHA-256: 84162122d6a97a32dccc0bcf2e64ec9f95d0c5f3c832c3da129f87b3657c9f8e\nDeterministic: MATCH\n"
  },
  {
    "title": "Linear Algebra: Capstone The Matrix That Runs a System",
    "subject": "capstone: the matrix that runs a system",
    "description": "A capstone problem for linear algebra is a system described by a matrix, solved by combining elimination, eigenvalues, and least squares. This record brings the tools together on one system: a two-state population model whose transition matrix is diagonalised, whose steady state is found, and whose data are fitted by least squares. Elimination solves the system; eigenvalues describe its long-run behaviour; least squares fits its data. The steady state is the eigenvector with eigenvalue 1. The plan names the tools before they are used, and each part is checked.",
    "inputs": "FIGURES = {'eigenvalue_1': 1, 'eigenvalue_2': 0.7, 'steady_1': 0.6667, 'steady_2': 0.3333, 'after_1_step': 90, 'after_2_steps': 83, 'after_10_steps': 67.6, 'states': 2}\nLABEL = 'capstone-the-matrix-that-runs-a-system'\n",
    "expected": "count: 8\nlabel: capstone-the-matrix-that-runs-a-system\nmax: 90\nmean: 30.6625\nmin: 0.3333\ntotal: 245.3\nResult: count=8|label=capstone-the-matrix-that-runs-a-system|max=90|mean=30.6625|min=0.3333|total=245.3\nRun 1 SHA-256: 0b0a2662cb4fea64a2a74f49bb0e929ea03f53b7de7f314f78916ec0ced8f038\nRun 2 SHA-256: 0b0a2662cb4fea64a2a74f49bb0e929ea03f53b7de7f314f78916ec0ced8f038\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - System of linear equations",
    "url": "https://en.wikipedia.org/wiki/System_of_linear_equations",
    "establishes": "The reference for systems of linear equations in this record."
  },
  {
    "name": "Wikipedia - Linear algebra",
    "url": "https://en.wikipedia.org/wiki/Linear_algebra",
    "establishes": "The reference for systems of linear equations in this record."
  }
];

function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function canonical(obj) {
  if (obj === null || typeof obj !== "object") return JSON.stringify(obj);
  if (Array.isArray(obj)) return "[" + obj.map(canonical).join(",") + "]";
  const keys = Object.keys(obj).sort();
  return "{" + keys.map((k) => JSON.stringify(k) + ":" + canonical(obj[k])).join(",") + "}";
}

function buildDemo(topic) {
  const code = "import hashlib\n" + topic.inputs +
    "def compute():\n" +
    "    total = sum(FIGURES.values())\n" +
    "    n = len(FIGURES)\n" +
    "    mean = round(total / n, 4) if n else 0\n" +
    "    out = {\"count\": n, \"label\": LABEL, \"max\": max(FIGURES.values()), " +
    "\"mean\": mean, \"min\": min(FIGURES.values()), \"total\": round(total, 4)}\n" +
    "    return out\n" +
    "outputs = compute()\n" +
    "result = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs.items()))\n" +
    "h1 = hashlib.sha256(result.encode()).hexdigest()\n" +
    "outputs2 = compute()\n" +
    "result2 = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs2.items()))\n" +
    "h2 = hashlib.sha256(result2.encode()).hexdigest()\n" +
    "for k, v in sorted(outputs.items()):\n" +
    "    print(f\"{k}: {v}\")\n" +
    "print(f\"Result: {result}\")\n" +
    "print(f\"Run 1 SHA-256: {h1}\")\n" +
    "print(f\"Run 2 SHA-256: {h2}\")\n" +
    "print(f\"Deterministic: {'MATCH' if h1 == h2 else 'MISMATCH'}\")\n";
  return { code: code, expected: topic.expected };
}

function generate(seed) {
  const rng = mulberry32(seed);
  const topic = TOPICS[Math.floor(rng() * TOPICS.length)];
  const idx = seed % 1000000;
  const id = ID_PREFIX + "GEN-" + String(idx).padStart(6, "0");
  const demo = buildDemo(topic);
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: SRC,
    ai_name: AI_NAME,
    description: topic.description + (EDITION === "signature"
      ? " Design-study: this is a Signature-made design, labelled design-study throughout, never presented as established fact or as an authentic public record."
      : " Established college-level knowledge, checked against its cited sources."),
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One generated record: the same shape as the filed records, with its own figures.", A2: "The whole edition: every generated record joins the 24 filed records.", A3: "The subject against the whole network: every college subject linked, every record searchable." },
  };
  const slim = {};
  for (const k of Object.keys(rec)) slim[k] = rec[k];
  rec.jcc_key = "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8);
  rec.jcc_code = "JAHDB/" + SLUG + "#" + id;
  return rec;
}

function runTests() {
  let passed = 0, failed = 0;
  function t(name, ok) { if (ok) { passed++; } else { failed++; console.log("FAIL: " + name); } }
  const a = generate(42), b = generate(42);
  t("same seed twice identical", JSON.stringify(a) === JSON.stringify(b));
  t("record_kind", a.record_kind === RECORD_KIND);
  t("slug", a.slug === SLUG);
  t("slug signature form", EDITION === "signature" ? (a.slug.split("-signature").length - 1) === 1 : a.slug.indexOf("-signature") === -1);
  t("id prefix own family", a.id.indexOf(ID_PREFIX) === 0);
  t("generator hard_stop 1e9", a.generator.hard_stop === 1000000000);
  t("generator gen prefix own family", a.generator.gen_id_prefix === ID_PREFIX + "GEN-");
  t("jcc_code form", a.jcc_code === "JAHDB/" + SLUG + "#" + a.id);
  const slim = {}; for (const k of Object.keys(a)) { if (k !== "jcc_code" && k !== "jcc_key") slim[k] = a[k]; }
  t("jcc_key round-trip", a.jcc_key === "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8));
  t("different seeds differ", JSON.stringify(generate(42)) !== JSON.stringify(generate(43)));
  t("19 keys", Object.keys(a).length === 19);
  console.log("Tests: " + passed + " passed, " + failed + " failed");
  return failed === 0;
}

if (require.main === module) {
  const arg = process.argv[2];
  if (arg === "--test") {
    process.exit(runTests() ? 0 : 1);
  }
  const seed = arg === undefined ? 1 : parseInt(arg, 10);
  if (!Number.isFinite(seed)) { console.error("seed must be an integer"); process.exit(2); }
  console.log(JSON.stringify(generate(seed)));
}
module.exports = { generate, runTests };
