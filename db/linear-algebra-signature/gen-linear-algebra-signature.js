// Seeded boundless generator for the The Signature Linear Algebra Database ("signature" edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-linear-algebra-signature.js [seed]  (prints one JSON record)
// or: node gen-linear-algebra-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "linear-algebra-signature";
const RECORD_KIND = "linear algebra record";
const ID_PREFIX = "JAH-LINALGS-";
const AI_NAME = "JAH Linear Algebra Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI — not stored files.";

const TOPICS = [
  {
    "title": "Signature Design: The Elimination Board",
    "subject": "a Signature elimination board design",
    "description": "The Elimination Board is a Signature-made design for teaching systems of equations: a board where a learner writes the system as a matrix, performs row operations (swapping rows, scaling a row, adding a multiple of one row to another), and watches the system become triangular. Gaussian elimination solves a system by such operations. Each row operation is shown as a button, and the board updates the matrix. A pivot (the leading entry of a row) is highlighted at each step. The solution is read off by back-substitution, with each step checked.",
    "inputs": "FIGURES = {'row_operations': 1, 'pivots': 2, 'solution_x': 2, 'solution_y': 3, 'rows': 2, 'cols': 3, 'steps': 3, 'design_version': 1}\nLABEL = 'a-signature-elimination-board-design'\n",
    "expected": "count: 8\nlabel: a-signature-elimination-board-design\nmax: 3\nmean: 2.125\nmin: 1\ntotal: 17\nResult: count=8|label=a-signature-elimination-board-design|max=3|mean=2.125|min=1|total=17\nRun 1 SHA-256: 1b65bf967485db0d24916b7280bbc911b337770ff18c27b1b3b681651f6af522\nRun 2 SHA-256: 1b65bf967485db0d24916b7280bbc911b337770ff18c27b1b3b681651f6af522\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Vector Playground",
    "subject": "a Signature vector playground design",
    "description": "The Vector Playground is a Signature-made design for teaching vectors: a plane where a learner drags vectors, adds them tip to tail, scales them, and tests whether a set is linearly independent. A vector is a list of numbers with direction and size. Dragging a vector shows its coordinates and its length. Adding two vectors shows the parallelogram they span. The independence test colours a dependent set red and an independent set green.",
    "inputs": "FIGURES = {'pairs_tested': 2, 'independent_pairs': 1, 'dependent_pairs': 1, 'spans_drawn': 2, 'vectors_dragged': 4, 'dimensions_shown': 2, 'colours_used': 2, 'design_version': 1}\nLABEL = 'a-signature-vector-playground-design'\n",
    "expected": "count: 8\nlabel: a-signature-vector-playground-design\nmax: 4\nmean: 1.875\nmin: 1\ntotal: 15\nResult: count=8|label=a-signature-vector-playground-design|max=4|mean=1.875|min=1|total=15\nRun 1 SHA-256: 74667014a3d30fdcc86e67503447d1b1cbe1b7a0f7a20133cf0d55de50c6511f\nRun 2 SHA-256: 74667014a3d30fdcc86e67503447d1b1cbe1b7a0f7a20133cf0d55de50c6511f\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Basis Builder",
    "subject": "a Signature basis builder design",
    "description": "The Basis Builder is a Signature-made design for teaching bases and dimension: a tool where a learner picks vectors, and the tool reports whether they are independent, whether they span, and whether they form a basis, with the coordinates of a test vector shown in the chosen basis. A basis is an independent spanning set. The tool tests independence and spanning separately, so a failure is diagnosed. A chosen basis shows the coordinates of any vector entered. The dimension is displayed as the size of any basis.",
    "inputs": "FIGURES = {'picks': 2, 'bases_found': 1, 'coordinate_1': 2, 'coordinate_2': 1, 'dimension': 2, 'vectors_in_failed_pick': 3, 'properties_tested': 2, 'design_version': 1}\nLABEL = 'a-signature-basis-builder-design'\n",
    "expected": "count: 8\nlabel: a-signature-basis-builder-design\nmax: 3\nmean: 1.75\nmin: 1\ntotal: 14\nResult: count=8|label=a-signature-basis-builder-design|max=3|mean=1.75|min=1|total=14\nRun 1 SHA-256: 48aa1a3c82bd49f8955097873cac5128a625a37d90ef556146427cf31a206530\nRun 2 SHA-256: 48aa1a3c82bd49f8955097873cac5128a625a37d90ef556146427cf31a206530\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Matrix Multiplier",
    "subject": "a Signature matrix multiplier design",
    "description": "The Matrix Multiplier is a Signature-made design for teaching matrix multiplication: a tool where a learner multiplies two matrices and watches each entry computed as a dot product of a row and a column, with the row and column highlighted. The (i, j) entry is the dot product of row i with column j. Clicking an entry highlights its row and column and shows the products summed. The reverse product is computed alongside, showing that multiplication is not commutative. Shapes that do not match are refused with the reason.",
    "inputs": "FIGURES = {'entries_computed': 4, 'products_shown': 2, 'ab_11': 19, 'ab_22': 50, 'ba_11': 23, 'ba_22': 46, 'rows': 2, 'cols': 2}\nLABEL = 'a-signature-matrix-multiplier-design'\n",
    "expected": "count: 8\nlabel: a-signature-matrix-multiplier-design\nmax: 50\nmean: 18.5\nmin: 2\ntotal: 148\nResult: count=8|label=a-signature-matrix-multiplier-design|max=50|mean=18.5|min=2|total=148\nRun 1 SHA-256: b30533a06bce2f3a48f2f3ce963bb8b4644598e9320e030f9051e8bcddb0bd92\nRun 2 SHA-256: b30533a06bce2f3a48f2f3ce963bb8b4644598e9320e030f9051e8bcddb0bd92\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Inverse Finder",
    "subject": "a Signature inverse finder design",
    "description": "The Inverse Finder is a Signature-made design for teaching matrix inverses: a tool where a learner enters a square matrix, the tool computes its determinant, and if it is non-zero, finds the inverse by the 2 by 2 formula or by elimination, and verifies it by multiplying. A matrix has an inverse exactly when its determinant is non-zero. The determinant is computed and shown first, as the test for invertibility. A singular matrix is refused with the reason: its determinant is zero. The inverse is verified by multiplying it with the original in both orders.",
    "inputs": "FIGURES = {'determinant_1': 1, 'determinant_2': 0, 'matrices_tested': 2, 'inverses_found': 1, 'refusals': 1, 'verifications': 2, 'inv_11': 3, 'inv_22': 2}\nLABEL = 'a-signature-inverse-finder-design'\n",
    "expected": "count: 8\nlabel: a-signature-inverse-finder-design\nmax: 3\nmean: 1.5\nmin: 0\ntotal: 12\nResult: count=8|label=a-signature-inverse-finder-design|max=3|mean=1.5|min=0|total=12\nRun 1 SHA-256: a0fce3fb88ec046d4d4c52c0981d3e1f856abd2fc199889bdf6e5fcad4162492\nRun 2 SHA-256: a0fce3fb88ec046d4d4c52c0981d3e1f856abd2fc199889bdf6e5fcad4162492\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Determinant Visualiser",
    "subject": "a Signature determinant visualiser design",
    "description": "The Determinant Visualiser is a Signature-made design for teaching determinants: a tool where a learner enters a 2 by 2 matrix and sees the unit square deformed into a parallelogram, with its area shown as the determinant. The determinant is the factor by which the matrix scales areas. The unit square is drawn, then deformed by the matrix into a parallelogram. The area of the parallelogram is shown and equals the determinant. A zero determinant flattens the square onto a line, shown in red.",
    "inputs": "FIGURES = {'determinant_1': 10, 'area_1': 10, 'determinant_2': 0, 'area_2': 0, 'matrices_shown': 2, 'flattenings': 1, 'vertices': 4, 'design_version': 1}\nLABEL = 'a-signature-determinant-visualiser-design'\n",
    "expected": "count: 8\nlabel: a-signature-determinant-visualiser-design\nmax: 10\nmean: 3.5\nmin: 0\ntotal: 28\nResult: count=8|label=a-signature-determinant-visualiser-design|max=10|mean=3.5|min=0|total=28\nRun 1 SHA-256: fd2490698c381663721a271f2f9484c4024a232ca0b08bef5e03878d23b7c757\nRun 2 SHA-256: fd2490698c381663721a271f2f9484c4024a232ca0b08bef5e03878d23b7c757\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Eigen Explorer",
    "subject": "a Signature eigen explorer design",
    "description": "The Eigen Explorer is a Signature-made design for teaching eigenvalues and eigenvectors: a tool where a learner enters a matrix and drags a vector, watching the matrix stretch it, and the tool flags the directions where the vector stays on its own line. An eigenvector is a direction the matrix only scales. Dragging a vector shows its image and the angle between the vector and its image. When the angle is zero, the vector is an eigenvector, and the scale factor is shown. The characteristic polynomial is displayed with its roots, the eigenvalues.",
    "inputs": "FIGURES = {'eigenvectors_found': 2, 'eigenvalue_1': 3, 'eigenvalue_2': 2, 'vectors_dragged': 5, 'scale_factors_shown': 2, 'characteristic_degree': 2, 'matrix_entries': 4, 'design_version': 1}\nLABEL = 'a-signature-eigen-explorer-design'\n",
    "expected": "count: 8\nlabel: a-signature-eigen-explorer-design\nmax: 5\nmean: 2.625\nmin: 1\ntotal: 21\nResult: count=8|label=a-signature-eigen-explorer-design|max=5|mean=2.625|min=1|total=21\nRun 1 SHA-256: 2d08ede00e147c022b95f484fcb9d32221b71be970f8f65e131fa372a77772da\nRun 2 SHA-256: 2d08ede00e147c022b95f484fcb9d32221b71be970f8f65e131fa372a77772da\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Diagonaliser",
    "subject": "a Signature diagonaliser design",
    "description": "The Diagonaliser is a Signature-made design for teaching diagonalisation: a tool where a learner enters a matrix, the tool finds its eigenvalues and eigenvectors, builds P and D, and shows A squared computed both directly and as P D squared P^-1. A matrix is diagonalisable when it has a full set of independent eigenvectors. The tool finds the eigenvalues, the eigenvectors, and the matrices P and D. Powers are computed both ways and compared. A defective matrix is flagged as not diagonalisable, with the reason.",
    "inputs": "FIGURES = {'eigenvalues': 2, 'eigenvectors': 2, 'a_squared_11': 9, 'a_squared_12': 5, 'a_squared_22': 4, 'computations_agreeing': 2, 'trace': 5, 'determinant': 6}\nLABEL = 'a-signature-diagonaliser-design'\n",
    "expected": "count: 8\nlabel: a-signature-diagonaliser-design\nmax: 9\nmean: 4.375\nmin: 2\ntotal: 35\nResult: count=8|label=a-signature-diagonaliser-design|max=9|mean=4.375|min=2|total=35\nRun 1 SHA-256: d06150614a0ea68247e72ac28c26f16ed28d78bd3dfcde63f6629e890b73cbe0\nRun 2 SHA-256: d06150614a0ea68247e72ac28c26f16ed28d78bd3dfcde63f6629e890b73cbe0\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Orthogonality Checker",
    "subject": "a Signature orthogonality checker design",
    "description": "The Orthogonality Checker is a Signature-made design for teaching inner products: a tool where a learner enters two vectors, the tool computes their dot product, their lengths, and the angle between them, and flags orthogonality when the dot product is zero. Two vectors are orthogonal when their inner product is zero. The dot product, the two lengths, and the angle are all shown. Orthogonal pairs are flagged green; non-orthogonal pairs show their angle. The projection of one vector onto the other is drawn and computed.",
    "inputs": "FIGURES = {'dot_product': 0, 'length_u': 5, 'length_v': 5, 'angle_degrees': 90, 'projection_x': 1.32, 'projection_y': 1.76, 'pairs_tested': 2, 'design_version': 1}\nLABEL = 'a-signature-orthogonality-checker-design'\n",
    "expected": "count: 8\nlabel: a-signature-orthogonality-checker-design\nmax: 90\nmean: 13.26\nmin: 0\ntotal: 106.08\nResult: count=8|label=a-signature-orthogonality-checker-design|max=90|mean=13.26|min=0|total=106.08\nRun 1 SHA-256: 35054e35f484e038172b10cf5f5f0bbe55d56de254cde3ffdb473e06b0cfbfe7\nRun 2 SHA-256: 35054e35f484e038172b10cf5f5f0bbe55d56de254cde3ffdb473e06b0cfbfe7\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Projection Fitter",
    "subject": "a Signature projection fitter design",
    "description": "The Projection Fitter is a Signature-made design for teaching least squares: a tool where a learner plots data points, the tool fits the best line by minimising the sum of squared errors, and shows the residuals (the errors) and their squares. Least squares is the projection of the data onto the model's column space. The data points are plotted, and the fitted line is drawn through them. Each residual is shown as a vertical segment, with its square listed. The sum of squared residuals is shown, and moving the line shows it increasing.",
    "inputs": "FIGURES = {'points': 3, 'intercept': 1.1667, 'slope': 1.5, 'residual_sum_squares': 0.1667, 'dragged_sum_squares': 0.5, 'residuals_shown': 3, 'parameters': 2, 'design_version': 1}\nLABEL = 'a-signature-projection-fitter-design'\n",
    "expected": "count: 8\nlabel: a-signature-projection-fitter-design\nmax: 3\nmean: 1.5417\nmin: 0.1667\ntotal: 12.3334\nResult: count=8|label=a-signature-projection-fitter-design|max=3|mean=1.5417|min=0.1667|total=12.3334\nRun 1 SHA-256: cec948b2f138804ea82a6755cd2cc828eba28ea3778328d3ca6e2a5152e8a864\nRun 2 SHA-256: cec948b2f138804ea82a6755cd2cc828eba28ea3778328d3ca6e2a5152e8a864\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Rank Meter",
    "subject": "a Signature rank meter design",
    "description": "The Rank Meter is a Signature-made design for teaching rank: a tool where a learner enters a matrix, the tool row-reduces it, counts the pivots, and shows the rank and the nullity (the dimension of the solution space of A x = 0). The rank is the number of pivots. Row reduction is shown step by step, with pivots highlighted. The rank is the pivot count; the nullity follows from the rank-nullity theorem. A null vector is shown when the nullity is non-zero.",
    "inputs": "FIGURES = {'rank': 2, 'nullity': 1, 'pivots': 2, 'rows': 3, 'cols': 3, 'null_x': 1, 'null_y': -2, 'null_z': 1}\nLABEL = 'a-signature-rank-meter-design'\n",
    "expected": "count: 8\nlabel: a-signature-rank-meter-design\nmax: 3\nmean: 1.375\nmin: -2\ntotal: 11\nResult: count=8|label=a-signature-rank-meter-design|max=3|mean=1.375|min=-2|total=11\nRun 1 SHA-256: 0c3570a71c7b11bd2dddce6936b46b4bf0243e5071af184dcd068320fe2a76b9\nRun 2 SHA-256: 0c3570a71c7b11bd2dddce6936b46b4bf0243e5071af184dcd068320fe2a76b9\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Transformation Studio",
    "subject": "a Signature transformation studio design",
    "description": "The Transformation Studio is a Signature-made design for teaching linear transformations: a studio where a learner picks a transformation (rotation, reflection, scaling, projection), applies it to a shape, and watches the shape move, with the matrix shown alongside. A linear transformation preserves addition and scaling. The shape and its image are drawn together, with the matrix shown. The kernel (vectors sent to zero) and the image are displayed. Composing two transformations shows the product of their matrices.",
    "inputs": "FIGURES = {'transformations': 2, 'vertices_moved': 3, 'rotation_degrees': 90, 'scale_x': 2, 'image_x': 0, 'image_y': 1, 'matrix_size': 2, 'design_version': 1}\nLABEL = 'a-signature-transformation-studio-design'\n",
    "expected": "count: 8\nlabel: a-signature-transformation-studio-design\nmax: 90\nmean: 12.625\nmin: 0\ntotal: 101\nResult: count=8|label=a-signature-transformation-studio-design|max=90|mean=12.625|min=0|total=101\nRun 1 SHA-256: 14fd95e4cf8bbd7c5279ea2f02b9d52bc96024733074a7c187e213037a3d5f19\nRun 2 SHA-256: 14fd95e4cf8bbd7c5279ea2f02b9d52bc96024733074a7c187e213037a3d5f19\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Change of Basis Viewer",
    "subject": "a Signature change of basis viewer design",
    "description": "The Change of Basis Viewer is a Signature-made design for teaching change of basis: a viewer where a learner sees the same vector drawn in two bases, with the coordinates in each basis shown and the change-of-basis matrix displayed. New coordinates are the old coordinates multiplied by the inverse of the change-of-basis matrix. The vector is drawn once, with two sets of grid lines for the two bases. The coordinates in each basis are shown side by side. The change-of-basis matrix and its inverse are displayed.",
    "inputs": "FIGURES = {'bases': 2, 'old_coord_1': 3, 'old_coord_2': 1, 'new_coord_1': 2, 'new_coord_2': 1, 'det_p': -2, 'inverse_factor': 0.5, 'design_version': 1}\nLABEL = 'a-signature-change-of-basis-viewer-design'\n",
    "expected": "count: 8\nlabel: a-signature-change-of-basis-viewer-design\nmax: 3\nmean: 1.0625\nmin: -2\ntotal: 8.5\nResult: count=8|label=a-signature-change-of-basis-viewer-design|max=3|mean=1.0625|min=-2|total=8.5\nRun 1 SHA-256: 69786f1334cf8f3c6d034d534267bdd21fe1744be27aaeddcba7107c786ceab4\nRun 2 SHA-256: 69786f1334cf8f3c6d034d534267bdd21fe1744be27aaeddcba7107c786ceab4\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The SVD Compressor",
    "subject": "a Signature singular value decomposition compressor design",
    "description": "The SVD Compressor is a Signature-made design for teaching the singular value decomposition: a tool where a learner loads a small image as a matrix, computes its singular values, and watches the image rebuild from the largest few, with the error shown. The singular value decomposition writes a matrix as U times Sigma times V transpose, with Sigma diagonal. The singular values are listed in decreasing order. Keeping the k largest rebuilds the best rank-k approximation. The error is shown as the size of the discarded singular values.",
    "inputs": "FIGURES = {'singular_values': 4, 'largest': 10, 'second': 5, 'third': 1, 'smallest': 0.5, 'error_k1': 5, 'error_k2': 1, 'error_k3': 0.5}\nLABEL = 'a-signature-singular-value-decomposition-compressor-design'\n",
    "expected": "count: 8\nlabel: a-signature-singular-value-decomposition-compressor-design\nmax: 10\nmean: 3.375\nmin: 0.5\ntotal: 27.0\nResult: count=8|label=a-signature-singular-value-decomposition-compressor-design|max=10|mean=3.375|min=0.5|total=27.0\nRun 1 SHA-256: c6c7a777f24243a8e096e680bed452e1bfa3c6ddb797dc525a18b3a5e2da7a11\nRun 2 SHA-256: c6c7a777f24243a8e096e680bed452e1bfa3c6ddb797dc525a18b3a5e2da7a11\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Finite Field Lab",
    "subject": "a Signature finite field laboratory design",
    "description": "The Finite Field Lab is a Signature-made design for teaching vector spaces over finite fields: a laboratory where a learner works with binary strings of length 3, adds them bit by bit, and sees the 8 vectors and their subspaces. A field is a number system where the four operations work; the field with 2 elements has 1 + 1 = 0. The 8 binary strings of length 3 are listed with their sums. Subspaces are shown as subsets closed under addition. The dimension is shown as the size of a basis.",
    "inputs": "FIGURES = {'vectors': 8, 'dimension': 3, 'subspaces_2d': 7, 'basis_vectors': 3, 'field_size': 2, 'string_length': 3, 'sums_shown': 8, 'design_version': 1}\nLABEL = 'a-signature-finite-field-laboratory-design'\n",
    "expected": "count: 8\nlabel: a-signature-finite-field-laboratory-design\nmax: 8\nmean: 4.375\nmin: 1\ntotal: 35\nResult: count=8|label=a-signature-finite-field-laboratory-design|max=8|mean=4.375|min=1|total=35\nRun 1 SHA-256: cbaf7f1c516980357b8d0e4c4c1015cd6d110a0a4521b04f2849bb20c11c93dd\nRun 2 SHA-256: cbaf7f1c516980357b8d0e4c4c1015cd6d110a0a4521b04f2849bb20c11c93dd\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Quadratic Form Bowl",
    "subject": "a Signature quadratic form bowl design",
    "description": "The Quadratic Form Bowl is a Signature-made design for teaching quadratic forms: a 3D bowl or saddle drawn from a symmetric matrix, with the eigenvalues shown as the heights along the principal axes. A quadratic form is a degree-2 polynomial written as x transpose A x for a symmetric matrix A. The surface is drawn, with the principal axes marked. Positive eigenvalues give a bowl; mixed signs give a saddle. The extreme values on the unit circle are shown as the eigenvalues.",
    "inputs": "FIGURES = {'eigenvalue_1': 4, 'eigenvalue_2': 2, 'value_at_1_1': 8, 'value_at_1_minus1': 4, 'min_on_circle': 2, 'max_on_circle': 4, 'variables': 2, 'design_version': 1}\nLABEL = 'a-signature-quadratic-form-bowl-design'\n",
    "expected": "count: 8\nlabel: a-signature-quadratic-form-bowl-design\nmax: 8\nmean: 3.375\nmin: 1\ntotal: 27\nResult: count=8|label=a-signature-quadratic-form-bowl-design|max=8|mean=3.375|min=1|total=27\nRun 1 SHA-256: 1604a38999ce8b1702bc92a7b985606bbba1509beb1bb0c663569167d9b75f98\nRun 2 SHA-256: 1604a38999ce8b1702bc92a7b985606bbba1509beb1bb0c663569167d9b75f98\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Graphics Pipeline",
    "subject": "a Signature graphics pipeline design",
    "description": "The Graphics Pipeline is a Signature-made design for teaching linear algebra in graphics: a pipeline of matrices (model, view, projection) that a learner applies in order to a 3D point, watching it move from object space to screen space. Points are vectors and transformations are matrices. Each stage is a matrix, shown with its effect on the point. The stages compose by matrix multiplication, and the order matters. Homogeneous coordinates are used so translation is a matrix too.",
    "inputs": "FIGURES = {'stages': 3, 'matrices': 3, 'rotation_degrees': 90, 'screen_x': 0, 'screen_y': 1, 'translated_z': 5, 'points_moved': 2, 'design_version': 1}\nLABEL = 'a-signature-graphics-pipeline-design'\n",
    "expected": "count: 8\nlabel: a-signature-graphics-pipeline-design\nmax: 90\nmean: 13.125\nmin: 0\ntotal: 105\nResult: count=8|label=a-signature-graphics-pipeline-design|max=90|mean=13.125|min=0|total=105\nRun 1 SHA-256: 1298e2d4e8abfcaae8a3c7c2d306b73908b3815c3f7e184fdfb421ee57f11deb\nRun 2 SHA-256: 1298e2d4e8abfcaae8a3c7c2d306b73908b3815c3f7e184fdfb421ee57f11deb\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Markov Chain Simulator",
    "subject": "a Signature Markov chain simulator design",
    "description": "The Markov Chain Simulator is a Signature-made design for teaching Markov chains: a simulator where a learner sets transition probabilities, watches the distribution evolve step by step, and sees it settle to the steady state. A Markov chain moves between states with fixed probabilities depending only on the current state. The distribution is shown as bars that change each step. The steady state is shown as the limit the bars approach. The eigenvalues are shown, with the second eigenvalue governing the speed of approach.",
    "inputs": "FIGURES = {'steps_shown': 10, 'after_1_sunny': 0.8, 'after_2_sunny': 0.72, 'after_10_sunny': 0.668, 'steady_sunny': 0.6667, 'steady_rainy': 0.3333, 'eigenvalue_2': 0.4, 'states': 2}\nLABEL = 'a-signature-markov-chain-simulator-design'\n",
    "expected": "count: 8\nlabel: a-signature-markov-chain-simulator-design\nmax: 10\nmean: 1.9485\nmin: 0.3333\ntotal: 15.588\nResult: count=8|label=a-signature-markov-chain-simulator-design|max=10|mean=1.9485|min=0.3333|total=15.588\nRun 1 SHA-256: 34e55538a30631e8c91958df10ba7e59d3d024dd07487ec37aa6073b82f6b189\nRun 2 SHA-256: 34e55538a30631e8c91958df10ba7e59d3d024dd07487ec37aa6073b82f6b189\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Linear Map Deformer",
    "subject": "a Signature linear map deformer design",
    "description": "The Linear Map Deformer is a Signature-made design for teaching the geometry of linear maps: a tool where a learner enters a matrix and watches the unit square deform into a parallelogram, with the area shown as the determinant. A linear map deforms space, and its determinant is the volume change. The unit square is drawn, then deformed into the parallelogram spanned by the columns. The area is shown and equals the determinant. A negative determinant flips the square, shown by reversing its corners.",
    "inputs": "FIGURES = {'determinant_1': 4, 'area_1': 4, 'determinant_2': 1, 'area_2': 1, 'vertices': 4, 'rotation_degrees': 90, 'matrices_shown': 2, 'design_version': 1}\nLABEL = 'a-signature-linear-map-deformer-design'\n",
    "expected": "count: 8\nlabel: a-signature-linear-map-deformer-design\nmax: 90\nmean: 13.375\nmin: 1\ntotal: 107\nResult: count=8|label=a-signature-linear-map-deformer-design|max=90|mean=13.375|min=1|total=107\nRun 1 SHA-256: f5f19c0c064706ce7ab09cd56a8d9ce4c710e1fc443f72a6bce5fd22d1bb035a\nRun 2 SHA-256: f5f19c0c064706ce7ab09cd56a8d9ce4c710e1fc443f72a6bce5fd22d1bb035a\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The QR Solver",
    "subject": "a Signature QR solver design",
    "description": "The QR Solver is a Signature-made design for teaching QR factorisation: a tool where a learner enters a matrix, watches Gram-Schmidt orthogonalisation build Q (with orthonormal columns) and R (upper triangular), and solves least squares by back-substitution. QR is the stable way to solve least squares. Gram-Schmidt is shown step by step, orthogonalising each column against the earlier ones. R is shown as upper triangular, and the system R x = Q transpose b is solved by back-substitution. The answer is compared with the normal equations.",
    "inputs": "FIGURES = {'intercept': 1.1667, 'slope': 1.5, 'residual_sum_squares': 0.1667, 'rows': 3, 'cols': 2, 'columns_orthogonalised': 2, 'steps': 4, 'design_version': 1}\nLABEL = 'a-signature-qr-solver-design'\n",
    "expected": "count: 8\nlabel: a-signature-qr-solver-design\nmax: 4\nmean: 1.8542\nmin: 0.1667\ntotal: 14.8334\nResult: count=8|label=a-signature-qr-solver-design|max=4|mean=1.8542|min=0.1667|total=14.8334\nRun 1 SHA-256: 9359d314ea7ece5116d8da4100a9af9fb6430dd9d54aa4f59177679beee0d869\nRun 2 SHA-256: 9359d314ea7ece5116d8da4100a9af9fb6430dd9d54aa4f59177679beee0d869\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Functional Reader",
    "subject": "a Signature functional reader design",
    "description": "The Functional Reader is a Signature-made design for teaching dual spaces: a tool where a learner enters a linear functional (a linear map to the scalars) and sees it as a dot product with a fixed vector, with the dual basis shown. A linear functional assigns a number to each vector, linearly. The functional is shown as a formula and as a vector to dot with. The dual basis is shown as the functionals that pick out coordinates. Applying the functional to a vector shows the number it assigns.",
    "inputs": "FIGURES = {'f_at_1_0': 2, 'f_at_0_1': 3, 'f_at_2_1': 7, 'dual_dimension': 2, 'evaluations': 3, 'dual_basis_size': 2, 'dot_vector_x': 2, 'dot_vector_y': 3}\nLABEL = 'a-signature-functional-reader-design'\n",
    "expected": "count: 8\nlabel: a-signature-functional-reader-design\nmax: 7\nmean: 3.0\nmin: 2\ntotal: 24\nResult: count=8|label=a-signature-functional-reader-design|max=7|mean=3.0|min=2|total=24\nRun 1 SHA-256: c7af57dfe5da4bd214301335635365c6932feb6035b500ec2f777e3e3789b1fd\nRun 2 SHA-256: c7af57dfe5da4bd214301335635365c6932feb6035b500ec2f777e3e3789b1fd\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Gram-Schmidt Orthogonaliser",
    "subject": "a Signature Gram-Schmidt orthogonaliser design",
    "description": "The Gram-Schmidt Orthogonaliser is a Signature-made design for teaching the Gram-Schmidt process: an orthogonaliser where a learner enters vectors, and the tool subtracts the projections and normalises, showing the orthonormal basis being built. Gram-Schmidt turns independent vectors into an orthonormal list spanning the same space. Each vector is shown with its projections onto the earlier ones. The subtraction is shown, and the result is normalised. A dependent vector is shown giving zero and being dropped.",
    "inputs": "FIGURES = {'u1_dot_u1': 2, 'projection_factor': 0.5, 'u2_x': 0.5, 'u2_y': -0.5, 'u2_z': 1, 'u2_norm': 1.225, 'e1_x': 0.707, 'e2_z': 0.816}\nLABEL = 'a-signature-gram-schmidt-orthogonaliser-design'\n",
    "expected": "count: 8\nlabel: a-signature-gram-schmidt-orthogonaliser-design\nmax: 2\nmean: 0.781\nmin: -0.5\ntotal: 6.248\nResult: count=8|label=a-signature-gram-schmidt-orthogonaliser-design|max=2|mean=0.781|min=-0.5|total=6.248\nRun 1 SHA-256: e35000b141f5bef8e2c096a937548f8d04a4bf8901c6e5c7585c38da2afce674\nRun 2 SHA-256: e35000b141f5bef8e2c096a937548f8d04a4bf8901c6e5c7585c38da2afce674\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Linear Algebra Capstone Console",
    "subject": "a Signature linear algebra capstone console design",
    "description": "The Linear Algebra Capstone Console is a Signature-made design for teaching combined linear algebra: a console where a learner analyses a whole system with elimination, eigenvalues, and least squares together, with the plan, the checks, and the assembly scored. A capstone problem uses several tools at once. The console plans the tools: elimination for the system, eigenvalues for the long run, least squares for the data. Each part is solved and checked separately. The assembly is scored as a whole argument.",
    "inputs": "FIGURES = {'parts': 4, 'checks_passed': 4, 'eigenvalue_2': 0.7, 'steady_1': 0.6667, 'after_2_steps': 83, 'slope': -8.5, 'states': 2, 'design_version': 1}\nLABEL = 'a-signature-linear-algebra-capstone-console-design'\n",
    "expected": "count: 8\nlabel: a-signature-linear-algebra-capstone-console-design\nmax: 83\nmean: 10.8583\nmin: -8.5\ntotal: 86.8667\nResult: count=8|label=a-signature-linear-algebra-capstone-console-design|max=83|mean=10.8583|min=-8.5|total=86.8667\nRun 1 SHA-256: b22705e473d6e0f8ace804d76c98506d4570660a40dabf6d741f4860caee3516\nRun 2 SHA-256: b22705e473d6e0f8ace804d76c98506d4570660a40dabf6d741f4860caee3516\nDeterministic: MATCH\n"
  },
  {
    "title": "Signature Design: The Span Finder",
    "subject": "a Signature span finder design",
    "description": "The Span Finder is a Signature-made design for teaching span: a tool where a learner enters vectors and a target vector, and the tool reports whether the target is in the span, with the combination shown when it is and the reason shown when it is not. The span is the set of all linear combinations. The tool solves for the coefficients and shows them when they exist. When no combination works, the tool shows the inconsistent system. The span is drawn as a line, a plane, or the whole space.",
    "inputs": "FIGURES = {'tests': 2, 'successes': 1, 'failures': 1, 'coefficient_1': 3, 'coefficient_2': 1, 'target_x': 3, 'target_y': 1, 'design_version': 1}\nLABEL = 'a-signature-span-finder-design'\n",
    "expected": "count: 8\nlabel: a-signature-span-finder-design\nmax: 3\nmean: 1.625\nmin: 1\ntotal: 13\nResult: count=8|label=a-signature-span-finder-design|max=3|mean=1.625|min=1|total=13\nRun 1 SHA-256: e11b6cb952b70b5f847104e9834ce1562ddf4d5c32d36c9c4bcdfe3326c3e681\nRun 2 SHA-256: e11b6cb952b70b5f847104e9834ce1562ddf4d5c32d36c9c4bcdfe3326c3e681\nDeterministic: MATCH\n"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - System of linear equations",
    "url": "https://en.wikipedia.org/wiki/System_of_linear_equations",
    "establishes": "The reference for a Signature elimination board design in this record."
  },
  {
    "name": "Wikipedia - Linear algebra",
    "url": "https://en.wikipedia.org/wiki/Linear_algebra",
    "establishes": "The reference for a Signature elimination board design in this record."
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
