# 100 PhD-Level Resources — Wave 1 Glossary (merged)

Plain-words definitions of every technical and network term the Wave 1 records use. No term is assumed known. The three group glossaries are reproduced verbatim below (group-a, group-b, group-c); terms may repeat across groups with compatible definitions.


## From group-a

# Glossary — PhD-Level Resources Wave 1, Group A

Every technical and network term used in this group's records, defined in
plain words. A term is defined in plain words on first use in each record;
this glossary is the single reference for all of them.

## Mathematics terms

- **Theorem** — a mathematical statement that has been proved, meaning shown
  to follow by logical steps from accepted starting points.
- **Proof** — a finite sequence of logical steps, each following from earlier
  steps and from axioms, that ends with the claimed statement.
- **Conjecture** — a precise mathematical guess that has been stated exactly
  but not yet proved or disproved.
- **Axiom** — a starting assumption accepted without proof, from which
  theorems are derived.
- **Lemma** — a small proved statement used as a step inside a larger proof.
- **Counterexample** — a single example that shows a general claim false.
- **Prime number (prime)** — a whole number greater than 1 whose only
  divisors are 1 and itself, such as 2, 3, 5, 7, 11.
- **Whole number** — a counting number such as 1, 2, 3, or 0.
- **Rational point** — a point whose coordinates are fractions (ratios of
  whole numbers).
- **Genus** — for a curve, the number of holes in it: a line has genus 0, an
  elliptic curve genus 1, more complicated curves higher genus.
- **Elliptic curve** — a smooth curve of genus one with a chosen point,
  defined by an equation of the form y squared equals x cubed plus a times x
  plus b.
- **Zeta function** — a function that encodes information about the prime
  numbers; the Riemann zeta function is the central example.
- **L-function** — a generalisation of the zeta function built from a
  mathematical object such as an elliptic curve.
- **Rank** — for an elliptic curve, the number of independent rational points
  of infinite order.
- **Divisor** — a formal list of points with whole-number weights, recording
  where a function is allowed poles (places where it blows up) and zeros.
- **Manifold** — a space that looks flat up close: every point has a small
  region around it that looks like ordinary flat space.
- **Tangent space** — the flat space of directions through a point of a
  manifold.
- **Chart** — a map from a small region of a manifold to flat space.
- **Atlas** — a collection of charts covering a whole manifold.
- **Metric** — a rule that assigns to each tangent space a way of measuring
  lengths of vectors and angles between them.
- **Riemannian manifold** — a manifold equipped with a metric.
- **Curvature** — a measure of how a shape bends. Gaussian curvature is the
  bending of a surface at a point; sectional curvature generalises it to
  higher dimensions by looking at two-dimensional slices; Ricci curvature
  averages sectional curvatures over directions containing a given vector.
- **Geodesic** — the straightest possible path on a curved space; a curve
  whose direction does not turn as it moves.
- **Connection** — a rule for comparing directions at different points of a
  manifold.
- **Parallel transport** — carrying a vector along a curve using a connection,
  keeping it as constant as the connection allows.
- **Holonomy** — the transformation a vector undergoes when parallel
  transported around a closed loop; it measures curvature.
- **Differential form** — an object that can be integrated over a manifold; a
  zero-form is a function, a one-form integrates along a curve, a two-form
  over a surface.
- **Exterior derivative** — an operation taking a k-form to a (k+1)-form,
  generalising gradient, curl, and divergence; it satisfies d squared = 0.
- **Cohomology** — a sequence of groups measuring the holes and twists of a
  shape, and the obstruction to patching locally defined data into global
  data.
- **Sheaf** — a tool for tracking data defined locally, on small pieces of a
  space.
- **Variety** — a geometric shape defined as the set of points satisfying a
  system of polynomial equations.
- **Polynomial** — an expression built from variables and their powers, such
  as x squared plus y squared minus one.
- **Scheme** — Grothendieck's generalisation of a variety: a space built by
  gluing affine schemes, each the spectrum (set of prime ideals) of a ring.
- **Spectrum** — for a ring, the set of its prime ideals made into a space.
- **Moduli space** — a geometric space whose points are themselves geometric
  objects, such as curves of a given genus.
- **Hodge structure** — a decomposition of a cohomology group into parts of
  type (p, q), recording holomorphic and anti-holomorphic directions.
- **Etale map** — a map that is locally an isomorphism, like a covering map.
- **Etale cohomology** — a cohomology theory for varieties that works over
  any field, including finite fields.
- **Topos** — a category behaving like the category of sheaves on a space; a
  generalisation of topology introduced by Grothendieck.
- **Toric variety** — a variety containing a torus as a dense open part,
  determined by a fan (a collection of cones).
- **Fan** — a collection of cones (wedge-shaped regions in a lattice) that
  determines a toric variety.
- **Abelian variety** — a higher-dimensional analogue of an elliptic curve:
  a complete algebraic variety that is also a group.
- **Jacobian variety** — the abelian variety built from a curve, whose
  dimension equals the curve's genus.
- **Lie group** — a smooth manifold that is also a group, with smooth group
  operations.
- **Lie algebra** — the tangent space at the identity of a Lie group,
  equipped with a bracket operation recording non-commutativity.
- **Laplace-Beltrami operator** — the generalisation of the Laplacian (sum
  of second derivatives) to a Riemannian manifold.
- **Eigenvalue** — a special number for which an equation involving an
  operator has a non-zero solution.
- **Minimal surface** — a surface that minimises area locally, like a soap
  film; it has zero mean curvature at every point.
- **Mean curvature** — the average of a surface's two principal bendings.
- **Symplectic manifold** — a manifold with a symplectic form, a closed
  nondegenerate two-form; the geometry of phase space in mechanics.
- **Finsler metric** — a rule assigning a length to each tangent vector that
  need not come from an inner product, so length may depend on direction.
- **Fibre bundle** — a space that locally looks like a product, with a fibre
  (a copy of a fixed space) over each point of a base space.
- **Vector bundle** — a fibre bundle whose fibres are vector spaces.
- **Submanifold** — a manifold sitting inside another manifold.
- **Second fundamental form** — a measurement of how a submanifold bends
  inside the space containing it.
- **Lorentzian manifold** — a manifold whose metric distinguishes time-like
  from space-like directions; the setting of general relativity.
- **Blow-up** — a surgery that replaces a point by the set of directions
  through it, used to resolve singularities.
- **Singular point** — a point where a shape is not smooth, like the tip of
  a cone.
- **Isometry** — a map that preserves distances.
- **Isospectral** — having the same spectrum (list of eigenvalues) while
  having a different shape.
- **Morse function** — a smooth function whose critical points (where its
  derivative vanishes) are all non-degenerate.
- **Handle** — a piece attached to a manifold at a critical point in a Morse
  decomposition.

## Research and evidence terms

- **Peer review** — checking of a paper by independent experts before
  publication.
- **Referee** — an independent expert who checks a paper before publication.
- **Preprint** — a paper shared publicly before peer review.
- **arXiv** — the open-access archive of scholarly articles.
- **Reproducibility** — the property that a result can be checked again by
  another researcher from the same starting points, reaching the same
  conclusion.
- **Evidence status** — one of seven values from the program's ladder:
  Proposed, Derived, Simulated, Experimentally tested, Independently
  reproduced, Formally verified, Peer reviewed.
- **Proposed** — a stated conjecture or design, put forward but not yet
  demonstrated.
- **Derived** — a result following by derivation from established results.
- **Simulated** — a result produced by computation or simulation, not by a
  closed proof or physical experiment.
- **Experimentally tested** — a result checked by experiment.
- **Independently reproduced** — a result reproduced by independent workers.
- **Formally verified** — a result checked by a fully rigorous proof, in
  some cases machine-checked.
- **Peer reviewed** — a result that has passed peer review.

## Network and database terms

- **Public edition** — the public version of a database, built from public
  records and public research.
- **Signature edition** — the Signature version of a database, containing
  Signature-made material.
- **Design-study** — a Signature-made design, labelled as a design, never
  presented as a real system or established fact.
- **public-harvest** — the source value marking a record built from public
  records.
- **signature-generated** — the source value marking a Signature-made record.
- **Record kind** — the type label of every record in a pair, for example
  "algebraic geometry research record".
- **JCC** — the condensed-by-code key: `jcc_code` is `JAHDB/<slug>#<id>` and
  `jcc_key` is `k=` plus the first 8 hex characters of the SHA-256 hash of
  the canonical record JSON without the two JCC fields.
- **SHA-256** — a standard 256-bit hash function; its digest identifies a
  record and proves the computation is deterministic when two runs match.
- **Deterministic** — giving the same output every time for the same input;
  the demos print `Deterministic: MATCH` when two runs agree.
- **Boundless generator** — a seeded program that generates further records
  on demand, up to a hard stop of 1,000,000,000 scales per file; outputs are
  generated, not stored files.
- **Hard stop** — the generator's absolute limit: 1,000,000,000.
- **Throttle per call** — the generator's per-call limit: 100 outputs.
- **Seed** — the integer input to a seeded generator; the same seed always
  emits the same record.
- **AI Librarian** — the named AI for a pair, for example "JAH Algebraic
  Geometry Librarian", which answers questions about the pair's records.
- **Adjacent pair** — a neighbouring live database linked from a record's
  network links, for example `fundamental-differential-geometry`.
- **Sibling edition** — the other edition of the same pair (public vs
  Signature).
- **Teaching ladder** — the principle that a database teaches from simple to
  compounded to most complex.
- **HTTP 200** — the web response code meaning a page was fetched
  successfully.


## From group-b

# Glossary — Wave 1 Group B (PhD-Level Resources)

Every technical term and network term used in this group's records, defined
in plain words. A term is defined in plain words on first use in each record
too; this glossary is the single reference for the whole group.

## General and network terms

- **Database** — a named, organized collection of records on one subject, stored as files.
- **Record** — one entry in a database: a complete file of information about one topic, with its own identifier, text, demo, program, and sources.
- **Public edition** — the version of a database that records established, published research.
- **Signature edition** — the version of a database that holds Signature-made designs: new proposals created for this network, labeled design-study, never presented as established fact.
- **Design study** — a worked-out proposal for something that could be built and tested. It is a plan, not a result.
- **Record kind** — the type label of every record in a database, for example "topology research record".
- **Slug** — the short web address name of a database, for example `topology-research`.
- **Identifier (id)** — the unique code of one record, for example `JAH-TOPR-000001`. The prefix shows which database it belongs to.
- **Id prefix** — the fixed start of every identifier in one database, for example `JAH-TOPR-`.
- **AI name / Librarian** — the named AI assistant attached to a database, for example "JAH Topology Research Librarian". It explains the database and runs its demos.
- **Source (src)** — where a record's material comes from: `public-harvest` for established public research, `signature-generated` for Signature-made designs.
- **Evidence status** — one of seven labels saying how well a result is established: Proposed, Derived, Simulated, Experimentally tested, Independently reproduced, Formally verified, Peer reviewed.
- **Evidence record** — the four stored facts behind an evidence status: assumptions, methods, test outputs, limitations.
- **Peer reviewed** — checked by other researchers before publication.
- **OPEN** — the label on a problem nobody has yet solved. An OPEN problem has no claimed solution in the record.
- **Ladder rank** — the number 1 to 7 for an evidence status, 1 for Proposed up to 7 for Peer reviewed.
- **JCC code / JCC key** — the condensed code of a record. The code looks like `JAHDB/<slug>#<id>`; the key is `k=` plus the first 8 characters of the SHA-256 fingerprint of the record. Recomputing the key from the record must reproduce the stored key.
- **SHA-256** — a standard fingerprint method: it turns any text into a fixed-length string of characters, and changing one character of the text changes the fingerprint.
- **Deterministic** — giving the same result every time it runs. A demo is deterministic when two runs print identical output.
- **Demo** — a small program in a record that recomputes the record's checkable numbers and prints them.
- **Expected output** — the exact text a demo must print. The validator runs the demo and compares its printed output character for character.
- **Program** — a working class in a record with a `run()` method that recomputes the same result as the demo.
- **Generator** — a seeded program that produces new records on demand. Seeded means the same seed number always produces the same record.
- **Hard stop** — the maximum number of outputs a generator may produce per file: 1,000,000,000.
- **Ceiling note** — the sentence in every record stating the 1,000,000,000 ceiling and that outputs are generated, not stored.
- **Scales (A1, A2, A3)** — three views of a topic: one example, the whole topic, and the topic against the whole field.
- **Body** — the record's text in web-page form, in fourteen titled sections in fixed order: History, Description, The Problem, The Worked Solution, The Answer, When It Applies, Limits, Math Proof, Science Proof, Demo, Program, Generator, AI, Sources.
- **Network links** — links inside a record to its sibling edition and to adjacent live databases.
- **Sibling edition** — the other edition of the same database: the public record links to its Signature twin and back.
- **Adjacent database** — a live database on a neighboring subject, linked for the reader.
- **Manifest** — the master list of all live databases in the network, used to check that new slugs and id prefixes are free.
- **Package-only** — built and checked locally, not pushed anywhere, not live, not merged.

## Topology terms

- **Topology** — the branch of mathematics that studies shape by studying nearness without measuring distance.
- **Topological space** — a set together with a collection of subsets called open sets, satisfying the open-set axioms.
- **Open set** — a member of the collection that defines a topology; the basic "neighborhood" of topology.
- **Closed set** — a set whose complement is open.
- **Continuity / continuous function** — a function is continuous when the preimage of every open set is open. The preimage of a set is the set of points that map into it.
- **Homeomorphism** — a continuous bijection with a continuous inverse: the strict notion of "same shape" in topology.
- **Homotopy** — a deformation of one map into another through a continuous family of intermediate maps.
- **Homotopy equivalence** — two spaces have the same shape in the loose sense when maps back and forth compose to maps deformable to the identity.
- **Metric space** — a set with a distance function (a metric) satisfying four rules, including the triangle inequality.
- **Metric** — a distance function: it assigns a non-negative number to each pair of points.
- **Triangle inequality** — the rule that the direct distance never exceeds the distance through a third point.
- **Cauchy sequence** — a sequence whose terms get arbitrarily close to each other.
- **Complete** — a metric space is complete when every Cauchy sequence converges to a point inside the space.
- **Compact** — a space is compact when every open cover has a finite subcover. An open cover is a collection of open sets whose union is the whole space; a finite subcover is finitely many of them that already cover the space.
- **Connected** — a space is connected when it cannot be split into two disjoint non-empty open sets.
- **Path connected** — any two points can be joined by a continuous path.
- **Hausdorff space** — a space where any two distinct points have disjoint neighborhoods (open sets around each point that do not overlap).
- **Separation axioms (T0–T4)** — a ladder of properties saying how strongly points and closed sets can be separated by open sets.
- **Normal space** — a space where disjoint closed sets can be separated by disjoint open sets.
- **Base (basis)** — a collection of open sets such that every open set is a union of members of the base.
- **Subbase** — a smaller collection whose finite intersections form a base.
- **Product topology** — the topology on a product of spaces, the coarsest one making all projection maps continuous. A projection map sends a tuple to one of its coordinates.
- **Quotient topology** — the topology on a space formed by gluing points together, the finest one making the gluing map continuous.
- **Manifold** — a space that looks locally like ordinary Euclidean space.
- **Chart / atlas** — a chart is a coordinate map from a patch of a manifold to Euclidean space; an atlas is the collection of charts.
- **Surface** — a two-dimensional manifold.
- **Genus** — the number of handles on a surface.
- **Orientable** — having two distinct sides.
- **Fundamental group** — the group of homotopy classes of loops based at a point; it measures the holes in a space.
- **Loop** — a path that starts and ends at the same point.
- **Winding number** — the number of times a loop winds around a circle.
- **Homology** — the algebraic measurement of holes in a space in every dimension, computed from a chain complex.
- **Chain complex** — a sequence of groups linked by boundary maps, used to compute homology.
- **Cycle / boundary** — a cycle is a chain with zero boundary; a boundary is a chain that is the boundary of something one dimension higher. Homology is cycles modulo boundaries.
- **Betti number** — the rank (size) of a homology group; the zeroth counts pieces, the first counts loops, the second counts voids.
- **Euler characteristic** — vertices minus edges plus faces for a polyhedron; a number that survives stretching and bending.
- **Knot** — a closed loop embedded in three-dimensional space.
- **Knot invariant** — a quantity that is the same for equivalent knots, for example the Jones polynomial.
- **Jones polynomial** — a polynomial in one variable assigned to a knot, discovered by Vaughan Jones in 1984.
- **Reidemeister moves** — the three local moves on a knot diagram that generate all equivalences.
- **Covering space** — a space mapping onto another so that every point has a neighborhood whose preimage is a disjoint union of copies (sheets).
- **Universal cover** — the simply connected covering space (the one with no holes).
- **Simply connected** — having no holes: every loop can be shrunk to a point.
- **Fixed point** — a point a map leaves exactly where it is.
- **Retraction** — a continuous map from a space onto a subspace that fixes the subspace pointwise.
- **Compactification** — a compact space containing the original as a dense subset (every point is a limit of points of the original).
- **Antipodal points** — points exactly opposite each other on a sphere.
- **Simplicial complex** — a family of simplices (points, edges, triangles, tetrahedra, and higher analogues) glued along faces.
- **Triangulation** — a simplicial complex whose geometric realization is a given space.
- **Lie group** — a topological group that is also a smooth manifold with smooth group operations.
- **Topological group** — a group that is also a topological space, with continuous group operations.
- **Lie algebra** — a vector space with a bracket operation capturing the infinitesimal symmetry of a Lie group.

## Measure theory terms

- **Measure** — a rule assigning a size (a non-negative number, possibly infinite) to sets, adding over countable disjoint unions.
- **Sigma-algebra** — a collection of subsets containing the empty set and closed under complements and countable unions; the sets a measure is allowed to measure.
- **Measurable set** — a member of a sigma-algebra.
- **Borel sigma-algebra / Borel set** — the smallest sigma-algebra containing all open sets; its members are Borel sets.
- **Borel measure** — a measure defined on the Borel sigma-algebra.
- **Lebesgue measure** — the measure on the real line extending the length of intervals; countably additive and translation invariant.
- **Null set** — a set of measure zero.
- **Almost everywhere** — holding except on a null set.
- **Outer measure** — a size assigned to every subset, monotone and countably subadditive; the starting point for building measures.
- **Countably additive** — the measure of a countable disjoint union equals the sum of the measures.
- **Translation invariant** — shifting a set does not change its measure.
- **Regular (measure)** — every measurable set can be approximated from inside by compact sets and from outside by open sets.
- **Radon measure** — a Borel measure on a locally compact Hausdorff space, finite on compact sets and regular.
- **Signed measure** — a countably additive set function that can take negative values.
- **Hahn decomposition** — the split of a space into a positive set and a negative set for a signed measure.
- **Jordan decomposition** — writing a signed measure as the difference of two ordinary measures (positive and negative variation).
- **Total variation** — the sum of the positive and negative variations of a signed measure.
- **Absolutely continuous** — one measure is absolutely continuous with respect to another when every null set of the second is a null set of the first.
- **Singular (measure)** — a measure living on a null set of another measure.
- **Radon-Nikodym derivative (density)** — the density function that writes one measure as an integral against another.
- **Measurable function** — a function whose preimages of Borel sets are measurable.
- **Simple function** — a function taking finitely many values.
- **Lebesgue integral** — the integral built by slicing a function's range into horizontal levels and measuring the level sets.
- **Riemann integral** — the older integral built by slicing a function's domain into vertical strips.
- **Monotone convergence theorem** — the integral of an increasing sequence of non-negative functions is the limit of the integrals.
- **Fatou's lemma** — the integral of the limit inferior is at most the limit inferior of the integrals.
- **Limit inferior** — the smallest limit point of a sequence at each point.
- **Dominated convergence theorem** — pointwise convergence plus domination by one integrable function implies convergence of the integrals.
- **Product measure** — the measure on a product of spaces giving rectangles the product of their measures.
- **Fubini's theorem** — the integral over a product equals the iterated integrals in either order, for integrable functions.
- **Tonelli's theorem** — the companion for non-negative functions: the iterated integrals agree, possibly infinite.
- **Sigma-finite** — a space that is a countable union of finite-measure sets.
- **Probability measure** — a measure of total mass one.
- **Probability space** — a set with a sigma-algebra of events and a probability measure.
- **Random variable** — a measurable function on a probability space.
- **Expectation** — the Lebesgue integral of a random variable.
- **Conditional expectation** — the best prediction of a random variable given partial information (a smaller sigma-algebra).
- **Martingale** — a sequence of successive fair predictions: each term is the conditional expectation of the next.
- **Filtration** — an increasing sequence of sigma-algebras representing growing information.
- **Lp space** — the space of measurable functions whose p-th power is integrable, with the norm given by the p-th root of the integral of the p-th power.
- **Norm** — a function assigning a non-negative size to a vector (or function), satisfying three rules.
- **Hausdorff measure / Hausdorff dimension** — the measure defined by coverings, and the critical dimension where it jumps from infinity to zero; the dimension of a fractal.
- **Fractal** — a set with non-integer dimension, such as the Cantor set.
- **Ergodic** — a measure-preserving system that cannot be split into two non-trivial invariant pieces.
- **Invariant measure** — a measure a transformation preserves.
- **Jacobian determinant** — the factor by which a map stretches volumes locally.
- **Diffeomorphism** — a smooth invertible map with a smooth inverse.
- **Caratheodory criterion** — a set is measurable when it splits every test set additively under the outer measure.
- **Pre-measure** — a countably additive set function on an algebra (a collection closed under finite unions and complements), extended to a measure by the Caratheodory extension theorem.

## Functional analysis terms

- **Vector space** — a set where vectors can be added and scaled.
- **Normed vector space** — a vector space with a norm.
- **Banach space** — a normed vector space that is complete.
- **Hilbert space** — a vector space with an inner product that is complete with respect to the norm the inner product defines.
- **Inner product** — a rule assigning a number to each pair of vectors that measures their alignment.
- **Orthogonal / orthogonality** — perpendicular: two vectors are orthogonal when their inner product is zero.
- **Orthonormal basis** — a set of mutually perpendicular unit vectors that spans the space.
- **Linear operator** — a map between vector spaces preserving addition and scalar multiplication.
- **Bounded operator** — a linear operator whose outputs are bounded by a constant times the inputs; its smallest such constant is the operator norm.
- **Operator norm** — the size of a bounded linear operator.
- **Continuous linear functional** — a continuous linear map from a space to the scalars (ordinary numbers).
- **Dual space** — the space of all continuous linear functionals on a space, with the operator norm.
- **Weak topology** — the coarsest topology making all dual functionals continuous.
- **Weak-star topology** — the topology on a dual space defined by evaluation at points of the original space.
- **Reflexive** — a space that equals its double dual (its dual's dual) through the canonical embedding.
- **Compact operator** — a bounded linear operator sending the unit ball to a set with compact closure.
- **Finite-rank operator** — an operator whose range is finite-dimensional.
- **Self-adjoint operator** — an operator equal to its own adjoint (its mirror across the inner product).
- **Adjoint** — the operator that mirrors a given operator across the inner product.
- **Spectrum** — the set of scalars where an operator minus that scalar fails to be invertible.
- **Eigenvalue / eigenvector** — a scalar and a non-zero vector such that the operator sends the vector to the scalar times the vector.
- **Spectral theorem** — the diagonalization of self-adjoint operators, in finite and infinite dimensions.
- **Functional calculus** — the rule for applying functions to operators through the spectral theorem.
- **Fredholm alternative** — for a compact operator, either an equation is solvable for every right-hand side or the homogeneous equation has a non-trivial solution.
- **Fredholm index** — the dimension of the kernel minus the dimension of the cokernel (the kernel is the set sent to zero; the cokernel measures the failure of surjectivity).
- **Distribution (generalized function)** — a continuous linear functional on test functions; a generalized function defined by how it acts, not by values at points.
- **Test function** — a smooth function with compact support (zero outside a bounded set).
- **Dirac delta** — the distribution that evaluates a test function at zero.
- **Fourier transform** — the operation decomposing a function into its frequency components.
- **Plancherel's theorem** — the Fourier transform is a unitary operator on L2 (it preserves norms and inner products).
- **Unitary operator** — a distance- and inner-product-preserving bijection.
- **Convolution** — the smoothing operation blending two functions; the Fourier transform turns it into pointwise multiplication.
- **Sobolev space** — a space of functions whose distributional (weak) derivatives up to a given order are in Lp.
- **Weak derivative** — a derivative defined by integration by parts against test functions.
- **Weak solution** — a function in a Sobolev space satisfying an equation in integral form rather than pointwise.
- **Bilinear form** — a function of two vectors, linear in each separately.
- **Coercive** — a bilinear form bounded below by the norm: it controls the size of vectors.
- **Lax-Milgram theorem** — a bounded coercive bilinear form on a Hilbert space gives a unique solution to its variational equation.
- **Unbounded operator** — a linear operator defined only on a dense subspace (its domain), not bounded there.
- **Domain** — the set where an unbounded operator is defined.
- **Dense** — a subset is dense when every point of the space is a limit of points of the subset.
- **Closed operator** — an operator whose graph (the set of input-output pairs) is closed.
- **Semigroup (C0-semigroup)** — a family of bounded operators indexed by non-negative time, evolving a state forward, with the semigroup property.
- **Generator (of a semigroup)** — the operator whose time derivative at zero defines the semigroup.
- **Resolvent** — the inverse of an operator minus a scalar.
- **Hille-Yosida theorem** — the characterization of generators of contraction semigroups by a resolvent estimate.
- **Convex set** — a set containing the whole segment between any two of its points.
- **Extreme point** — a point of a convex set that cannot be written as a non-trivial convex combination (weighted average) of two other points of the set.
- **Convex hull** — the smallest convex set containing a given set.
- **Krein-Milman theorem** — a compact convex set is the closed convex hull of its extreme points.
- **Contraction** — a map shrinking distances by a fixed factor less than one.
- **Fixed-point theorem** — a theorem guaranteeing a point a map leaves unchanged.
- **Banach algebra** — a complete normed algebra (a vector space with a compatible multiplication).
- **C-star algebra** — a Banach algebra with an involution satisfying the C-star identity.
- **Character** — a non-zero homomorphism from an algebra to the scalars.
- **Maximal ideal** — a largest proper ideal (a subset closed under addition and under multiplication by algebra elements).
- **Gelfand transform** — the map sending an element of an algebra to the function of its values at characters.
- **Stone-Weierstrass theorem** — a point-separating subalgebra of continuous functions containing the constants is uniformly dense.
- **Dense (approximation)** — a set of functions is dense when every continuous function can be approximated uniformly by its members.
- **Baire category theorem** — a complete metric space cannot be a countable union of nowhere-dense sets (sets whose closure has empty interior).
- **Zorn's lemma** — the maximality principle that every chain has an upper bound; used for non-constructive extensions.
- **Sublinear function** — a function that is subadditive and positively homogeneous; the domination in the Hahn-Banach theorem.


## From group-c

# GLOSSARY — Wave 1 Group C (PhD-Level Resources)

Every technical and network term used in the Group C records, defined in
plain words. A term is defined here once, and also in plain words on first
use inside each record that uses it.

## Mathematical logic

- **Axiom** — a starting statement accepted without proof, used as a base for proving other statements.
- **Axiom system** — a chosen set of axioms plus the rules for proving things from them.
- **Completeness (of a logic)** — the property that every statement that is true in all models can be proved from the axioms.
- **Compactness** — the property that if every finite part of a set of statements can be satisfied, the whole set can be satisfied.
- **Consistency** — a system is consistent when it cannot prove both a statement and its opposite.
- **Decidable** — a question is decidable when a mechanical procedure always gives the right yes-or-no answer in finite time.
- **Undecidable** — a question is undecidable when no mechanical procedure can always answer it correctly.
- **First-order logic** — logic in which one can quantify (say "for all" or "there exists") over individual things, but not over sets of things or properties.
- **Second-order logic** — logic in which one can also quantify over sets of things and properties.
- **Formal system** — a precisely specified language, axioms, and proof rules, so that checking a proof is mechanical.
- **Forcing** — a method for building new models of set theory, used to show that some statements can neither be proved nor disproved from the usual axioms.
- **Model** — a mathematical structure in which the statements of a theory are interpreted as true or false.
- **Model theory** — the study of the relationship between formal theories and the structures (models) that satisfy them.
- **Proof theory** — the study of proofs themselves as mathematical objects.
- **Incompleteness** — Godel's discovery that any consistent system strong enough for arithmetic leaves some true statements unprovable inside it.
- **Soundness** — the property that everything provable in a system is true in its models.
- **ZFC** — Zermelo-Fraenkel set theory with the axiom of choice; the standard axiom system for mathematics.
- **Continuum hypothesis** — the claim that there is no size of infinity strictly between the counting numbers and the real numbers; independent of ZFC.
- **Axiom of choice** — the axiom saying that from any collection of non-empty sets one can pick one element from each; independent of the other ZFC axioms.
- **Lambda calculus** — a minimal system for computing with functions, where functions can take functions as inputs and produce functions as outputs.
- **Type theory** — a system in which every expression has a type (a kind), and only well-typed combinations are allowed; used as a foundation for mathematics and programming.
- **Modal logic** — logic with operators for "necessarily" and "possibly", used to reason about what must be true or could be true.
- **Intuitionistic logic** — logic that rejects proof by contradiction as a general rule: to prove something exists, one must construct it.
- **Presburger arithmetic** — arithmetic with addition only (no multiplication), which is decidable.
- **Nonstandard analysis** — a rigorous way to work with infinitesimals (infinitely small numbers) using models that extend the real numbers.
- **Lowenheim-Skolem theorem** — the result that a countable first-order theory with an infinite model also has models of every infinite size.
- **Lob's theorem** — the result that if a system can prove "if this statement is provable then it is true", then the system can prove the statement itself.
- **Ordinal** — a number that measures order and size beyond the finite numbers, used to measure the strength of proof systems.
- **Diagonal argument** — a method of constructing a new object that differs from every object in a given list, used to prove unprovability and uncountability.
- **Self-reference** — a statement or construction that talks about itself.
- **Quantifier** — a word like "for all" or "there exists" that says how many things a statement applies to.
- **Predicate** — a property or relation that can be true or false of things, such as "is even" or "is greater than".
- **Formula** — a precisely built statement in a formal language.
- **Sentence** — a formula with no free variables, which is either true or false in a model.
- **Theory** — a set of sentences closed under proof: everything provable from them is in the theory.
- **Derivation (proof)** — a step-by-step chain from axioms to a conclusion, following the proof rules.
- **Cut-elimination** — Gentzen's result that proofs can be transformed to avoid an intermediate rule, making proofs more direct.
- **Reflection** — a statement in which a system talks about its own provability.
- **Fixed point** — a statement that says of itself exactly what a given property says of it.

## Category theory

- **Category** — a collection of objects and arrows (morphisms) between them, with a rule for composing arrows and an identity arrow for each object.
- **Object** — one of the things in a category, such as a set, a group, or a space.
- **Morphism (arrow)** — a structure-preserving map from one object to another inside a category.
- **Functor** — a map between categories that sends objects to objects and arrows to arrows, preserving composition and identities.
- **Natural transformation** — a systematic way of turning one functor into another, one arrow per object, fitting together consistently.
- **Yoneda lemma** — the result that an object is completely determined by all the arrows into (or out of) it.
- **Adjoint functors** — a pair of functors going in opposite directions, related by a natural correspondence between arrows; the left one is the free construction, the right one the forgetful one.
- **Unit and counit** — the two canonical maps that come with an adjunction, going into and out of the round trip.
- **Limit** — the universal construction that captures "the most general object mapping into a diagram", such as a product.
- **Colimit** — the dual of a limit: the universal construction that captures "the most general object a diagram maps into", such as a disjoint union.
- **Universal property** — a description of an object by the arrows into or out of it, rather than by its internal parts; it pins the object down up to isomorphism.
- **Monad** — a functor with a unit and a multiplication satisfying coherence laws; used to model effects such as state, exceptions, or non-determinism.
- **Cartesian closed category** — a category with products and exponential objects, in which functions between objects are themselves objects.
- **Exponential object** — the object that stands for "all functions from A to B" inside a category.
- **Topos** — a category that behaves like the category of sets, with a logic of its own; a universe of sets.
- **Abelian category** — a category in which one can add morphisms, take kernels and cokernels, and do homological algebra, as with modules over a ring.
- **Monoidal category** — a category with a tensor product operation combining objects, plus a unit object, satisfying coherence laws.
- **Tensor product** — a way of combining two objects into one, generalizing multiplication of vector spaces.
- **Enriched category** — a category whose arrows between two objects form an object of some other category, rather than a plain set.
- **Kan extension** — the best way to extend a functor along another functor, in a universal sense.
- **Sheaf** — data attached to the open parts of a space that agrees where parts overlap, so local data glues into global data.
- **Grothendieck topology** — a notion of "covering" that generalizes open covers of a space, letting sheaf theory work in abstract settings.
- **Site** — a category equipped with a Grothendieck topology.
- **Derived category** — a category built from chain complexes by treating quasi-isomorphisms (maps inducing isomorphisms on homology) as isomorphisms.
- **Higher category theory** — category theory in which there are arrows between arrows, and arrows between those, and so on.
- **Equivalence of categories** — a pair of functors going back and forth that are inverse up to natural isomorphism; the categories have the same structure.
- **Free category** — the category generated from a directed graph, whose arrows are the paths in the graph.
- **Forgetful functor** — a functor that drops some structure, such as sending a group to its underlying set.
- **Isomorphism** — an arrow with a two-sided inverse; it says two objects are the same for the purposes of the category.
- **Commutative diagram** — a picture of objects and arrows in which any two routes between the same objects give the same composite arrow.
- **Composition** — combining two arrows end to end to get a new arrow.
- **Identity morphism** — the arrow that does nothing to an object; composing with it changes nothing.
- **Dual (opposite)** — the same category with all arrows reversed.

## Theoretical computer science

- **Turing machine** — the standard mathematical model of a computer: a tape, a read-write head, and a finite set of states.
- **Polynomial time** — time that grows at most like a power of the input size; the usual meaning of "efficient".
- **P** — the class of problems solvable in polynomial time by a deterministic computer.
- **NP** — the class of problems whose solutions can be checked in polynomial time.
- **NP-complete** — among the hardest problems in NP: every NP problem reduces to it.
- **Reduction** — a translation from one problem to another, showing the second is at least as hard as the first.
- **Satisfiability (SAT)** — the question of whether a Boolean formula has an assignment of true/false to its variables making it true.
- **Boolean formula** — a combination of variables with and, or, and not.
- **Cook-Levin theorem** — the theorem that SAT is NP-complete, the first NP-completeness result.
- **Time hierarchy theorem** — the result that more time allows strictly more problems to be solved.
- **Space hierarchy theorem** — the result that more memory allows strictly more problems to be solved.
- **Savitch's theorem** — the result that nondeterministic space can be simulated in deterministic space with only a squared increase.
- **PCP theorem** — the result that proofs can be rewritten so that checking a few random spots is enough to catch errors with high probability.
- **Ladner's theorem** — the result that if P differs from NP, then there are NP problems that are neither in P nor NP-complete.
- **Rice's theorem** — the result that every non-trivial property of what a program computes is undecidable.
- **Circuit complexity** — the study of how large or deep a Boolean circuit must be to compute a function.
- **Probabilistic Turing machine** — a Turing machine that can flip coins; its decisions may depend on random choices.
- **BPP** — the class of problems solvable by a probabilistic machine in polynomial time with error at most one third.
- **Interactive proof** — a conversation in which a prover convinces a verifier of a claim by answering challenges.
- **IP** — the class of problems with an interactive proof; IP equals PSPACE.
- **PSPACE** — the class of problems solvable using polynomial memory.
- **Zero-knowledge proof** — a proof that convinces the verifier without revealing why the claim is true.
- **Simulator** — a program that fakes an interaction without the secret, showing that nothing was leaked.
- **Shor's algorithm** — a quantum algorithm that factors integers in polynomial time by finding periods.
- **BQP** — the class of problems solvable by a quantum computer in polynomial time with bounded error.
- **Quantum computing** — computing with qubits, using superposition and entanglement.
- **Qubit** — a quantum bit, which can be in a superposition of 0 and 1.
- **Superposition** — a combination of 0 and 1 at once, with amplitudes that can interfere.
- **Entanglement** — a correlation between qubits with no classical analogue.
- **Quantum Fourier transform** — a quantum operation that finds periodicities in a function.
- **Communication complexity** — the study of how many bits two parties must exchange to compute a function of their combined inputs.
- **Alice and Bob** — the two parties in a communication protocol, each holding half the input.
- **Parameterized complexity** — the study of hard problems that become easy when some parameter of the input is small.
- **Fixed-parameter tractable** — solvable in time that depends on the parameter times a polynomial in the input size.
- **Kernel** — a small equivalent instance produced by preprocessing, whose size depends only on the parameter.
- **W-hierarchy** — a ladder of parameterized complexity classes, used to classify how hard a parameterized problem is.
- **Approximation algorithm** — an algorithm that finds a near-optimal solution quickly for a hard optimization problem.
- **Approximation ratio** — the worst-case factor by which an approximation algorithm's answer can differ from the optimum.
- **FLP impossibility result** — the theorem that deterministic asynchronous consensus is impossible with even one crash.
- **Consensus** — the problem of getting distributed processes to agree on one value.
- **Bivalent configuration** — a state of a distributed system from which both outcomes (0 and 1) remain reachable.
- **Asynchronous** — a system in which messages can be delayed arbitrarily, with no bound on delivery time.
- **One-way function** — a function that is easy to compute but hard to reverse; its existence is OPEN.
- **Derandomization** — removing randomness from algorithms, replacing coin flips with deterministic choices.
- **Pseudorandom generator** — a function that stretches a short random seed into a long sequence that looks random to given tests.
- **Complexity class** — a set of problems solvable within given resource bounds.
- **Inclusion** — the statement that every problem in one class is also in another.
- **Separation** — the statement that two complexity classes differ.
- **Open problem** — a question that is not known to be answered either way; marked OPEN in these records.

## Network and database terms

- **Database** — a collection of records on one subject, with an AI, a generator, and full files for each record.
- **Record** — one full file in a database: the complete entry for one topic, with all its data.
- **Public edition** — the edition of a database holding established public research, sourced from public records.
- **Signature edition** — the edition holding Signature-made designs, labeled design-study, never presented as established fact.
- **Design study** — a blueprint or design for something that could be built, not a claim that it exists or works.
- **Evidence status** — one of seven ladder values (Proposed, Derived, Simulated, Experimentally tested, Independently reproduced, Formally verified, Peer reviewed) saying how strongly a result is supported.
- **Evidence record** — the four-part record (assumptions, methods, test outputs, limitations) backing an evidence status.
- **Ladder** — the seven-step evidence scale, from Proposed (weakest) to Peer reviewed (strongest).
- **JCC** — the condensed code for a record: `JAHDB/<slug>#<id>` plus a short key derived from the record's content, so a record can be cited by code.
- **Generator** — a program that produces new records on demand from a seed; outputs are generated, not stored.
- **Boundless generator** — a generator that can produce up to 1,000,000,000 scales per file (the hard stop).
- **Hard stop** — the absolute limit on a generator: 1,000,000,000 scales per file.
- **Ceiling** — the note stating the generator's hard stop and that outputs are generated, not stored.
- **Scales** — the three levels A1 (one instance), A2 (the whole system), A3 (the system against the whole network).
- **Demo** — the working code in a record that recomputes the record's checkable figures and prints them twice with SHA-256 digests.
- **Program** — the working class in a record with a run() method that recomputes the same result as the demo.
- **AI librarian** — the named AI for a database, which answers questions about its records.
- **Network links** — the links in a record to its sibling edition and to adjacent databases.
- **Sibling edition** — the other edition of the same database (public for Signature, Signature for public).
- **Adjacent** — a nearby database linked from a record, live in the manifest or package-only.
- **Manifest** — the master list of all live databases in the network, with slugs and id prefixes.
- **Merge** — the step that adds a package-only database to the live manifest; nothing in this group has been merged.
- **Package-only** — built and verified as a package, but not pushed, not live, not merged.
- **Record kind** — the type label of a record, such as "mathematical logic research record".
- **Slug** — the short URL-style name of a database, such as `mathematical-logic`.
- **Id prefix** — the code at the start of every record id in a database, such as `JAH-MLOG-`.
- **SHA-256** — a standard fingerprint function: the same input always gives the same 64-character digest, and different inputs give different digests.
- **Deterministic** — always giving the same output for the same input.
- **Seed** — the starting number for a seeded generator; the same seed always emits the same record.
- **Throttle** — the limit on how many outputs a generator produces in one call (100 per call here).
- **OPEN** — the mark on a problem whose answer is not known; an open problem is never presented as solved.
