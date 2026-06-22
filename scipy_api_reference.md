<!-- Source: https://docs.scipy.org/doc/scipy/reference/ -->
* SciPy API
# SciPy API[#](#scipy-api "Link to this heading")
## Importing from SciPy[#](#importing-from-scipy "Link to this heading")
In Python, the distinction between what is the public API of a library and what
are private implementation details is not always clear. Unlike in other
languages like Java, it is possible in Python to access âprivateâ functions or
objects. Occasionally this may be convenient, but be aware that if you do so
your code may break without warning in future releases. Some widely understood
rules for what is and isnât public in Python are:
* Methods / functions / classes and module attributes whose names begin with a
  leading underscore are private.
* If a class name begins with a leading underscore, none of its members are
  public, whether or not they begin with a leading underscore.
* If a module name in a package begins with a leading underscore none of
  its members are public, whether or not they begin with a leading underscore.
* If a module or package defines `__all__`, that authoritatively defines the
  public interface.
* If a module or package doesnât define `__all__`, then all names that donât
  start with a leading underscore are public.
Note
Reading the above guidelines one could draw the conclusion that every
private module or object starts with an underscore. This is not the
case; the presence of underscores do mark something as private, but
the absence of underscores do not mark something as public.
In SciPy there are modules whose names donât start with an underscore, but that
should be considered private. To clarify which modules these are, we define
below what the public API is for SciPy, and give some recommendations for how
to import modules/functions/objects from SciPy.
## Guidelines for importing functions from SciPy[#](#guidelines-for-importing-functions-from-scipy "Link to this heading")
Everything in the namespaces of SciPy submodules is public. In general in
Python, it is recommended to make use of namespaces. For example, the
function `curve_fit` (defined in `scipy/optimize/_minpack_py.py`) should be
imported like this:
```
import scipy
result = scipy.optimize.curve_fit(...)
```
Or alternatively one could use the submodule as a namespace like so:
```
from scipy import optimize
result = optimize.curve_fit(...)
```
Note
For `scipy.io` prefer the use of `import scipy`
because `io` is also the name of a module in the Python
stdlib.
In some cases, the public API is one level deeper. For example, the
`scipy.sparse.linalg` module is public, and the functions it contains are not
available in the `scipy.sparse` namespace. Sometimes it may result in more
easily understandable code if functions are imported from one level deeper.
For example, in the following it is immediately clear that `lomax` is a
distribution if the second form is chosen:
```
# first form
from scipy import stats
stats.lomax(...)
# second form
from scipy.stats import distributions
distributions.lomax(...)
```
In that case, the second form can be chosen **if** it is documented in the next
section that the submodule in question is public. Of course you can still use:
```
import scipy
scipy.stats.lomax(...)
# or
scipy.stats.distributions.lomax(...)
```
Note
SciPy is using a lazy loading mechanism which means that modules
are only loaded in memory when you first try to access them.
## API definition[#](#api-definition "Link to this heading")
Every submodule listed below is public. That means that these submodules are
unlikely to be renamed or changed in an incompatible way, and if that is
necessary, a deprecation warning will be raised for one SciPy release before the
change is made.
* [`scipy`](../index.html#module-scipy "scipy")
* [`scipy.cluster`](cluster.html#module-scipy.cluster "scipy.cluster")
  + [`scipy.cluster.vq`](cluster.vq.html#module-scipy.cluster.vq "scipy.cluster.vq")
  + [`scipy.cluster.hierarchy`](cluster.hierarchy.html#module-scipy.cluster.hierarchy "scipy.cluster.hierarchy")
* [`scipy.constants`](constants.html#module-scipy.constants "scipy.constants")
* [`scipy.datasets`](datasets.html#module-scipy.datasets "scipy.datasets")
* [`scipy.differentiate`](differentiate.html#module-scipy.differentiate "scipy.differentiate")
* [`scipy.fft`](fft.html#module-scipy.fft "scipy.fft")
* [`scipy.fftpack`](fftpack.html#module-scipy.fftpack "scipy.fftpack")
* [`scipy.integrate`](integrate.html#module-scipy.integrate "scipy.integrate")
* [`scipy.interpolate`](interpolate.html#module-scipy.interpolate "scipy.interpolate")
* [`scipy.io`](io.html#module-scipy.io "scipy.io")
  + [`scipy.io.arff`](io.html#module-scipy.io.arff "scipy.io.arff")
  + [`scipy.io.matlab`](io.matlab.html#module-scipy.io.matlab "scipy.io.matlab")
  + [`scipy.io.wavfile`](io.html#module-scipy.io.wavfile "scipy.io.wavfile")
* [`scipy.linalg`](linalg.html#module-scipy.linalg "scipy.linalg")
  + [`scipy.linalg.blas`](linalg.blas.html#module-scipy.linalg.blas "scipy.linalg.blas")
  + [`scipy.linalg.cython_blas`](linalg.cython_blas.html#module-scipy.linalg.cython_blas "scipy.linalg.cython_blas")
  + [`scipy.linalg.lapack`](linalg.lapack.html#module-scipy.linalg.lapack "scipy.linalg.lapack")
  + [`scipy.linalg.cython_lapack`](linalg.cython_lapack.html#module-scipy.linalg.cython_lapack "scipy.linalg.cython_lapack")
  + [`scipy.linalg.interpolative`](linalg.interpolative.html#module-scipy.linalg.interpolative "scipy.linalg.interpolative")
* [`scipy.ndimage`](ndimage.html#module-scipy.ndimage "scipy.ndimage")
* [`scipy.odr`](odr.html#module-scipy.odr "scipy.odr")
* [`scipy.optimize`](optimize.html#module-scipy.optimize "scipy.optimize")
  + [`scipy.optimize.cython_optimize`](optimize.cython_optimize.html#module-scipy.optimize.cython_optimize "scipy.optimize.cython_optimize")
  + [`scipy.optimize.elementwise`](optimize.elementwise.html#module-scipy.optimize.elementwise "scipy.optimize.elementwise")
* [`scipy.signal`](signal.html#module-scipy.signal "scipy.signal")
  + [`scipy.signal.windows`](signal.windows.html#module-scipy.signal.windows "scipy.signal.windows")
* [`scipy.sparse`](sparse.html#module-scipy.sparse "scipy.sparse")
  + [`scipy.sparse.linalg`](sparse.linalg.html#module-scipy.sparse.linalg "scipy.sparse.linalg")
  + [`scipy.sparse.csgraph`](sparse.csgraph.html#module-scipy.sparse.csgraph "scipy.sparse.csgraph")
* [`scipy.spatial`](spatial.html#module-scipy.spatial "scipy.spatial")
  + [`scipy.spatial.distance`](spatial.distance.html#module-scipy.spatial.distance "scipy.spatial.distance")
  + [`scipy.spatial.transform`](spatial.transform.html#module-scipy.spatial.transform "scipy.spatial.transform")
* [`scipy.special`](special.html#module-scipy.special "scipy.special")
* [`scipy.stats`](stats.html#module-scipy.stats "scipy.stats")
  + [`scipy.stats.contingency`](stats.contingency.html#module-scipy.stats.contingency "scipy.stats.contingency")
  + [`scipy.stats.mstats`](stats.mstats.html#module-scipy.stats.mstats "scipy.stats.mstats")
  + [`scipy.stats.qmc`](stats.qmc.html#module-scipy.stats.qmc "scipy.stats.qmc")
  + [`scipy.stats.sampling`](stats.sampling.html#module-scipy.stats.sampling "scipy.stats.sampling")
## SciPy structure[#](#scipy-structure "Link to this heading")
All SciPy modules should follow the following conventions. In the
following, a *SciPy module* is defined as a Python package, say
`yyy`, that is located in the scipy/ directory.
* Ideally, each SciPy module should be as self-contained as possible.
  That is, it should have minimal dependencies on other packages or
  modules. Even dependencies on other SciPy modules should be kept to
  a minimum. A dependency on NumPy is of course assumed.
* Directory `yyy/` contains:
  + A file `meson.build` with build configuration for the submodule.
  + A directory `tests/` that contains files `test_<name>.py`
    corresponding to modules `yyy/<name>{.py,.so,/}`.
* Private modules should be prefixed with an underscore `_`,
  for instance `yyy/_somemodule.py`.
* User-visible functions should have good documentation following
  the [NumPy documentation style](https://numpydoc.readthedocs.io/en/latest/format.html).
* The `__init__.py` of the module should contain the main reference
  documentation in its docstring. This is connected to the Sphinx
  documentation under `doc/` via Sphinxâs automodule directive.
  The reference documentation should first give a categorized list of
  the contents of the module using `autosummary::` directives, and
  after that explain points essential for understanding the use of the
  module.
  Tutorial-style documentation with extensive examples should be
  separate and put under `doc/source/tutorial/`.
See the existing SciPy submodules for guidance.
[previous
Thread Safety in SciPy](../tutorial/thread_safety.html "previous page")
[next
The main SciPy namespace](main_namespace.html "next page")
On this page
* [Importing from SciPy](#importing-from-scipy)
* [Guidelines for importing functions from SciPy](#guidelines-for-importing-functions-from-scipy)
* [API definition](#api-definition)
* [SciPy structure](#scipy-structure)
---
<!-- Source: https://docs.scipy.org/doc/scipy/index.html -->
# SciPy documentation[#](#scipy-documentation "Link to this heading")
**Date**: June 19, 2026 **Version**: 1.18.0
**Download documentation**: <https://docs.scipy.org/doc/>
**Useful links**:
[Install](https://scipy.org/install/) |
[Source Repository](https://github.com/scipy/scipy) |
[Issues & Ideas](https://github.com/scipy/scipy/issues) |
[Q&A Support](https://stackoverflow.com/questions/tagged/scipy) |
[Forum](https://discuss.scientific-python.org/c/contributor/scipy)
**SciPy** (pronounced âSigh Pieâ) is an open-source software for mathematics,
science, and engineering.
![](_images/index_user_guide.svg)
**User guide**
The user guide provides in-depth information on the
key concepts of SciPy with useful background information and explanation.
[To the user guide](tutorial/index.html#user-guide)
![](_images/index_api.svg)
**API reference**
The reference guide contains a detailed description of
the SciPy API. The reference describes how the methods work and which parameters can
be used. It assumes that you have an understanding of the key concepts.
[To the reference guide](reference/index.html#scipy-api)
![](_images/index_getting_started.svg)
**Building from source**
Want to build from source rather than use a Python distribution or
pre-built SciPy binary? This guide will describe how to set up your
build environment, and how to build *SciPy* itself, including the many
options for customizing that build.
[To the build guide](building/index.html#building-from-source)
![](_images/index_contribute.svg)
**Developer guide**
Saw a typo in the documentation? Want to improve
existing functionalities? The contributing guidelines will guide
you through the process of improving SciPy.
[To the development guide](dev/index.html#scipy-development)
[next
SciPy User Guide](tutorial/index.html "next page")
---
<!-- Source: https://docs.scipy.org/doc/scipy/index.html#module-scipy -->
# SciPy documentation[#](#scipy-documentation "Link to this heading")
**Date**: June 19, 2026 **Version**: 1.18.0
**Download documentation**: <https://docs.scipy.org/doc/>
**Useful links**:
[Install](https://scipy.org/install/) |
[Source Repository](https://github.com/scipy/scipy) |
[Issues & Ideas](https://github.com/scipy/scipy/issues) |
[Q&A Support](https://stackoverflow.com/questions/tagged/scipy) |
[Forum](https://discuss.scientific-python.org/c/contributor/scipy)
**SciPy** (pronounced âSigh Pieâ) is an open-source software for mathematics,
science, and engineering.
![](_images/index_user_guide.svg)
**User guide**
The user guide provides in-depth information on the
key concepts of SciPy with useful background information and explanation.
[To the user guide](tutorial/index.html#user-guide)
![](_images/index_api.svg)
**API reference**
The reference guide contains a detailed description of
the SciPy API. The reference describes how the methods work and which parameters can
be used. It assumes that you have an understanding of the key concepts.
[To the reference guide](reference/index.html#scipy-api)
![](_images/index_getting_started.svg)
**Building from source**
Want to build from source rather than use a Python distribution or
pre-built SciPy binary? This guide will describe how to set up your
build environment, and how to build *SciPy* itself, including the many
options for customizing that build.
[To the build guide](building/index.html#building-from-source)
![](_images/index_contribute.svg)
**Developer guide**
Saw a typo in the documentation? Want to improve
existing functionalities? The contributing guidelines will guide
you through the process of improving SciPy.
[To the development guide](dev/index.html#scipy-development)
[next
SciPy User Guide](tutorial/index.html "next page")
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/cluster.html#module-scipy.cluster -->
* [SciPy API](index.html)
* Clustering package (`scipy.cluster`)
# Clustering package ([`scipy.cluster`](#module-scipy.cluster "scipy.cluster"))[#](#clustering-package-scipy-cluster "Link to this heading")
Clustering algorithms are useful in information theory, target detection,
communications, compression, and other areas. The [`vq`](cluster.vq.html#module-scipy.cluster.vq "scipy.cluster.vq") module only
supports vector quantization and the k-means algorithms.
The [`hierarchy`](cluster.hierarchy.html#module-scipy.cluster.hierarchy "scipy.cluster.hierarchy") module provides functions for hierarchical and
agglomerative clustering. Its features include generating hierarchical
clusters from distance matrices,
calculating statistics on clusters, cutting linkages
to generate flat clusters, and visualizing clusters with dendrograms.
* [K-means clustering and vector quantization (`scipy.cluster.vq`)](cluster.vq.html)
* [Hierarchical clustering (`scipy.cluster.hierarchy`)](cluster.hierarchy.html)
[previous
scipy.test](generated/scipy.test.html "previous page")
[next
K-means clustering and vector quantization (`scipy.cluster.vq`)](cluster.vq.html "next page")
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/cluster.vq.html#module-scipy.cluster.vq -->
* [SciPy API](index.html)
* [Clustering package (`scipy.cluster`)](cluster.html)
* K-means clustering and vector quantization (`scipy.cluster.vq`)
# K-means clustering and vector quantization ([`scipy.cluster.vq`](#module-scipy.cluster.vq "scipy.cluster.vq"))[#](#k-means-clustering-and-vector-quantization-scipy-cluster-vq "Link to this heading")
Provides routines for k-means clustering, generating code books
from k-means models and quantizing vectors by comparing them with
centroids in a code book.
|  |  |
| --- | --- |
| [`whiten`](generated/scipy.cluster.vq.whiten.html#scipy.cluster.vq.whiten "scipy.cluster.vq.whiten")(obs[,Â check\_finite]) | Normalize a group of observations on a per feature basis. |
| [`vq`](generated/scipy.cluster.vq.vq.html#scipy.cluster.vq.vq "scipy.cluster.vq.vq")(obs,Â code\_book[,Â check\_finite]) | Assign codes from a code book to observations. |
| [`kmeans`](generated/scipy.cluster.vq.kmeans.html#scipy.cluster.vq.kmeans "scipy.cluster.vq.kmeans")(obs,Â k\_or\_guess[,Â iter,Â thresh,Â ...]) | Performs k-means on a set of observation vectors forming k clusters. |
| [`kmeans2`](generated/scipy.cluster.vq.kmeans2.html#scipy.cluster.vq.kmeans2 "scipy.cluster.vq.kmeans2")(data,Â k[,Â iter,Â thresh,Â minit,Â ...]) | Classify a set of observations into k clusters using the k-means algorithm. |
Exceptions:
|  |  |
| --- | --- |
| [`ClusterError`](generated/scipy.cluster.vq.ClusterError.html#scipy.cluster.vq.ClusterError "scipy.cluster.vq.ClusterError") | An `Exception` raised during clustering. |
## Background information[#](#background-information "Link to this heading")
The k-means algorithm takes as input the number of clusters to
generate, k, and a set of observation vectors to cluster. It
returns a set of centroids, one for each of the k clusters. An
observation vector is classified with the cluster number or
centroid index of the centroid closest to it.
A vector v belongs to cluster i if it is closer to centroid i than
any other centroid. If v belongs to i, we say centroid i is the
dominating centroid of v. The k-means algorithm tries to
minimize distortion, which is defined as the sum of the squared distances
between each observation vector and its dominating centroid.
The minimization is achieved by iteratively reclassifying
the observations into clusters and recalculating the centroids until
a configuration is reached in which the centroids are stable. One can
also define a maximum number of iterations.
Since vector quantization is a natural application for k-means,
information theory terminology is often used. The centroid index
or cluster index is also referred to as a âcodeâ and the table
mapping codes to centroids and, vice versa, is often referred to as a
âcode bookâ. The result of k-means, a set of centroids, can be
used to quantize vectors. Quantization aims to find an encoding of
vectors that reduces the expected distortion.
All routines expect obs to be an M by N array, where the rows are
the observation vectors. The codebook is a k by N array, where the
ith row is the centroid of code word i. The observation vectors
and centroids have the same feature dimension.
As an example, suppose we wish to compress a 24-bit color image
(each pixel is represented by one byte for red, one for blue, and
one for green) before sending it over the web. By using a smaller
8-bit encoding, we can reduce the amount of data by two
thirds. Ideally, the colors for each of the 256 possible 8-bit
encoding values should be chosen to minimize distortion of the
color. Running k-means with k=256 generates a code book of 256
codes, which fills up all possible 8-bit sequences. Instead of
sending a 3-byte value for each pixel, the 8-bit centroid index
(or code word) of the dominating centroid is transmitted. The code
book is also sent over the wire so each 8-bit code can be
translated back to a 24-bit pixel value representation. If the
image of interest was of an ocean, we would expect many 24-bit
blues to be represented by 8-bit codes. If it was an image of a
human face, more flesh-tone colors would be represented in the
code book.
[previous
Clustering package (`scipy.cluster`)](cluster.html "previous page")
[next
whiten](generated/scipy.cluster.vq.whiten.html "next page")
On this page
* [Background information](#background-information)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html#module-scipy.cluster.hierarchy -->
* [SciPy API](index.html)
* [Clustering package (`scipy.cluster`)](cluster.html)
* Hierarchical clustering (`scipy.cluster.hierarchy`)
# Hierarchical clustering ([`scipy.cluster.hierarchy`](#module-scipy.cluster.hierarchy "scipy.cluster.hierarchy"))[#](#hierarchical-clustering-scipy-cluster-hierarchy "Link to this heading")
These functions cut hierarchical clusterings into flat clusterings
or find the roots of the forest formed by a cut by providing the flat
cluster ids of each observation.
|  |  |
| --- | --- |
| [`fcluster`](generated/scipy.cluster.hierarchy.fcluster.html#scipy.cluster.hierarchy.fcluster "scipy.cluster.hierarchy.fcluster")(Z,Â t[,Â criterion,Â depth,Â R,Â monocrit]) | Form flat clusters from the hierarchical clustering defined by the given linkage matrix. |
| [`fclusterdata`](generated/scipy.cluster.hierarchy.fclusterdata.html#scipy.cluster.hierarchy.fclusterdata "scipy.cluster.hierarchy.fclusterdata")(X,Â t[,Â criterion,Â metric,Â ...]) | Cluster observation data using a given metric. |
| [`leaders`](generated/scipy.cluster.hierarchy.leaders.html#scipy.cluster.hierarchy.leaders "scipy.cluster.hierarchy.leaders")(Z,Â T) | Return the root nodes in a hierarchical clustering. |
These are routines for agglomerative clustering.
|  |  |
| --- | --- |
| [`linkage`](generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage "scipy.cluster.hierarchy.linkage")(y[,Â method,Â metric,Â optimal\_ordering]) | Perform hierarchical/agglomerative clustering. |
| [`single`](generated/scipy.cluster.hierarchy.single.html#scipy.cluster.hierarchy.single "scipy.cluster.hierarchy.single")(y) | Perform single/min/nearest linkage on the condensed distance matrix `y`. |
| [`complete`](generated/scipy.cluster.hierarchy.complete.html#scipy.cluster.hierarchy.complete "scipy.cluster.hierarchy.complete")(y) | Perform complete/max/farthest point linkage on a condensed distance matrix. |
| [`average`](generated/scipy.cluster.hierarchy.average.html#scipy.cluster.hierarchy.average "scipy.cluster.hierarchy.average")(y) | Perform average/UPGMA linkage on a condensed distance matrix. |
| [`weighted`](generated/scipy.cluster.hierarchy.weighted.html#scipy.cluster.hierarchy.weighted "scipy.cluster.hierarchy.weighted")(y) | Perform weighted/WPGMA linkage on the condensed distance matrix. |
| [`centroid`](generated/scipy.cluster.hierarchy.centroid.html#scipy.cluster.hierarchy.centroid "scipy.cluster.hierarchy.centroid")(y) | Perform centroid/UPGMC linkage. |
| [`median`](generated/scipy.cluster.hierarchy.median.html#scipy.cluster.hierarchy.median "scipy.cluster.hierarchy.median")(y) | Perform median/WPGMC linkage. |
| [`ward`](generated/scipy.cluster.hierarchy.ward.html#scipy.cluster.hierarchy.ward "scipy.cluster.hierarchy.ward")(y) | Perform Ward's linkage on a condensed distance matrix. |
These routines compute statistics on hierarchies.
|  |  |
| --- | --- |
| [`cophenet`](generated/scipy.cluster.hierarchy.cophenet.html#scipy.cluster.hierarchy.cophenet "scipy.cluster.hierarchy.cophenet")(Z[,Â Y]) | Calculate the cophenetic distances between each observation in the hierarchical clustering defined by the linkage `Z`. |
| [`from_mlab_linkage`](generated/scipy.cluster.hierarchy.from_mlab_linkage.html#scipy.cluster.hierarchy.from_mlab_linkage "scipy.cluster.hierarchy.from_mlab_linkage")(Z) | Convert a linkage matrix generated by MATLAB(TM) to a new linkage matrix compatible with this module. |
| [`inconsistent`](generated/scipy.cluster.hierarchy.inconsistent.html#scipy.cluster.hierarchy.inconsistent "scipy.cluster.hierarchy.inconsistent")(Z[,Â d]) | Calculate inconsistency statistics on a linkage matrix. |
| [`maxinconsts`](generated/scipy.cluster.hierarchy.maxinconsts.html#scipy.cluster.hierarchy.maxinconsts "scipy.cluster.hierarchy.maxinconsts")(Z,Â R) | Return the maximum inconsistency coefficient for each non-singleton cluster and its children. |
| [`maxdists`](generated/scipy.cluster.hierarchy.maxdists.html#scipy.cluster.hierarchy.maxdists "scipy.cluster.hierarchy.maxdists")(Z) | Return the maximum distance between any non-singleton cluster. |
| [`maxRstat`](generated/scipy.cluster.hierarchy.maxRstat.html#scipy.cluster.hierarchy.maxRstat "scipy.cluster.hierarchy.maxRstat")(Z,Â R,Â i) | Return the maximum statistic for each non-singleton cluster and its children. |
| [`to_mlab_linkage`](generated/scipy.cluster.hierarchy.to_mlab_linkage.html#scipy.cluster.hierarchy.to_mlab_linkage "scipy.cluster.hierarchy.to_mlab_linkage")(Z) | Convert a linkage matrix to a MATLAB(TM) compatible one. |
Routines for visualizing flat clusters.
|  |  |
| --- | --- |
| [`dendrogram`](generated/scipy.cluster.hierarchy.dendrogram.html#scipy.cluster.hierarchy.dendrogram "scipy.cluster.hierarchy.dendrogram")(Z[,Â p,Â truncate\_mode,Â ...]) | Plot the hierarchical clustering as a dendrogram. |
These are data structures and routines for representing hierarchies as
tree objects.
|  |  |
| --- | --- |
| [`ClusterNode`](generated/scipy.cluster.hierarchy.ClusterNode.html#scipy.cluster.hierarchy.ClusterNode "scipy.cluster.hierarchy.ClusterNode")(id[,Â left,Â right,Â dist,Â count]) | A tree node class for representing a cluster. |
| [`leaves_list`](generated/scipy.cluster.hierarchy.leaves_list.html#scipy.cluster.hierarchy.leaves_list "scipy.cluster.hierarchy.leaves_list")(Z) | Return a list of leaf node ids. |
| [`to_tree`](generated/scipy.cluster.hierarchy.to_tree.html#scipy.cluster.hierarchy.to_tree "scipy.cluster.hierarchy.to_tree")(Z[,Â rd]) | Convert a linkage matrix into an easy-to-use tree object. |
| [`cut_tree`](generated/scipy.cluster.hierarchy.cut_tree.html#scipy.cluster.hierarchy.cut_tree "scipy.cluster.hierarchy.cut_tree")(Z[,Â n\_clusters,Â height]) | Given a linkage matrix Z, return the cut tree. |
| [`optimal_leaf_ordering`](generated/scipy.cluster.hierarchy.optimal_leaf_ordering.html#scipy.cluster.hierarchy.optimal_leaf_ordering "scipy.cluster.hierarchy.optimal_leaf_ordering")(Z,Â y[,Â metric]) | Given a linkage matrix Z and distance, reorder the cut tree. |
These are predicates for checking the validity of linkage and
inconsistency matrices as well as for checking isomorphism of two
flat cluster assignments.
|  |  |
| --- | --- |
| [`is_valid_im`](generated/scipy.cluster.hierarchy.is_valid_im.html#scipy.cluster.hierarchy.is_valid_im "scipy.cluster.hierarchy.is_valid_im")(R[,Â warning,Â throw,Â name]) | Return True if the inconsistency matrix passed is valid. |
| [`is_valid_linkage`](generated/scipy.cluster.hierarchy.is_valid_linkage.html#scipy.cluster.hierarchy.is_valid_linkage "scipy.cluster.hierarchy.is_valid_linkage")(Z[,Â warning,Â throw,Â name]) | Check the validity of a linkage matrix. |
| [`is_isomorphic`](generated/scipy.cluster.hierarchy.is_isomorphic.html#scipy.cluster.hierarchy.is_isomorphic "scipy.cluster.hierarchy.is_isomorphic")(T1,Â T2) | Determine if two different cluster assignments are equivalent. |
| [`is_monotonic`](generated/scipy.cluster.hierarchy.is_monotonic.html#scipy.cluster.hierarchy.is_monotonic "scipy.cluster.hierarchy.is_monotonic")(Z) | Return True if the linkage passed is monotonic. |
| [`correspond`](generated/scipy.cluster.hierarchy.correspond.html#scipy.cluster.hierarchy.correspond "scipy.cluster.hierarchy.correspond")(Z,Â Y) | Check for correspondence between linkage and condensed distance matrices. |
| [`num_obs_linkage`](generated/scipy.cluster.hierarchy.num_obs_linkage.html#scipy.cluster.hierarchy.num_obs_linkage "scipy.cluster.hierarchy.num_obs_linkage")(Z) | Return the number of original observations of the linkage matrix passed. |
Utility routines for plotting:
|  |  |
| --- | --- |
| [`set_link_color_palette`](generated/scipy.cluster.hierarchy.set_link_color_palette.html#scipy.cluster.hierarchy.set_link_color_palette "scipy.cluster.hierarchy.set_link_color_palette")(palette) | Set list of matplotlib color codes for use by dendrogram. |
Utility classes:
|  |  |
| --- | --- |
| [`DisjointSet`](generated/scipy.cluster.hierarchy.DisjointSet.html#scipy.cluster.hierarchy.DisjointSet "scipy.cluster.hierarchy.DisjointSet")([elements]) | Disjoint set data structure for incremental connectivity queries. |
Warnings:
|  |  |
| --- | --- |
| [`ClusterWarning`](generated/scipy.cluster.hierarchy.ClusterWarning.html#scipy.cluster.hierarchy.ClusterWarning "scipy.cluster.hierarchy.ClusterWarning") | A `UserWarning` raised during clustering. |
[previous
scipy.cluster.vq.ClusterError](generated/scipy.cluster.vq.ClusterError.html "previous page")
[next
fcluster](generated/scipy.cluster.hierarchy.fcluster.html "next page")
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/constants.html#module-scipy.constants -->
* [SciPy API](index.html)
* Constants (`scipy.constants`)
# Constants ([`scipy.constants`](#module-scipy.constants "scipy.constants"))[#](#constants-scipy-constants "Link to this heading")
Physical and mathematical constants and units.
## Mathematical constants[#](#mathematical-constants "Link to this heading")
|  |  |
| --- | --- |
| `pi` | Pi |
| `golden` | Golden ratio |
| `golden_ratio` | Golden ratio |
## Physical constants[#](#physical-constants "Link to this heading")
The following physical constants are available as attributes of [`scipy.constants`](#module-scipy.constants "scipy.constants").
All units are [SI](https://en.wikipedia.org/wiki/International_System_of_Units).
| Attribute | Quantity | Units |
| --- | --- | --- |
| `c` | speed of light in vacuum | m s^-1 |
| `speed_of_light` | speed of light in vacuum | m s^-1 |
| `mu_0` | the magnetic constant \(\mu\_0\) | N A^-2 |
| `epsilon_0` | the electric constant (vacuum permittivity), \(\epsilon\_0\) | F m^-1 |
| `h` | the Planck constant \(h\) | J Hz^-1 |
| `Planck` | the Planck constant \(h\) | J Hz^-1 |
| `hbar` | the reduced Planck constant, \(\hbar = h/(2\pi)\) | J s |
| `G` | Newtonian constant of gravitation | m^3 kg^-1 s^-2 |
| `gravitational_constant` | Newtonian constant of gravitation | m^3 kg^-1 s^-2 |
| `g` | standard acceleration of gravity | m s^-2 |
| `e` | elementary charge | C |
| `elementary_charge` | elementary charge | C |
| `R` | molar gas constant | J mol^-1 K^-1 |
| `gas_constant` | molar gas constant | J mol^-1 K^-1 |
| `alpha` | fine-structure constant | (unitless) |
| `fine_structure` | fine-structure constant | (unitless) |
| `N_A` | Avogadro constant | mol^-1 |
| `Avogadro` | Avogadro constant | mol^-1 |
| `k` | Boltzmann constant | J K^-1 |
| `Boltzmann` | Boltzmann constant | J K^-1 |
| `sigma` | Stefan-Boltzmann constant \(\sigma\) | W m^-2 K^-4 |
| `Stefan_Boltzmann` | Stefan-Boltzmann constant \(\sigma\) | W m^-2 K^-4 |
| `Wien` | Wien wavelength displacement law constant | m K |
| `Rydberg` | Rydberg constant | m^-1 |
| `m_e` | electron mass | kg |
| `electron_mass` | electron mass | kg |
| `m_p` | proton mass | kg |
| `proton_mass` | proton mass | kg |
| `m_n` | neutron mass | kg |
| `neutron_mass` | neutron mass | kg |
### Constants database[#](#constants-database "Link to this heading")
In addition to the above variables, [`scipy.constants`](#module-scipy.constants "scipy.constants") also contains the
2022 CODATA recommended values [[CODATA2022]](#rc437f0a4090e-codata2022) database containing more physical
constants.
|  |  |
| --- | --- |
| [`value`](generated/scipy.constants.value.html#scipy.constants.value "scipy.constants.value")(key) | Value in physical\_constants indexed by key. |
| [`unit`](generated/scipy.constants.unit.html#scipy.constants.unit "scipy.constants.unit")(key) | Unit in physical\_constants indexed by key. |
| [`precision`](generated/scipy.constants.precision.html#scipy.constants.precision "scipy.constants.precision")(key) | Relative precision in physical\_constants indexed by key. |
| [`find`](generated/scipy.constants.find.html#scipy.constants.find "scipy.constants.find")([sub,Â disp]) | Return list of physical\_constant keys containing a given string. |
| [`ConstantWarning`](generated/scipy.constants.ConstantWarning.html#scipy.constants.ConstantWarning "scipy.constants.ConstantWarning") | Accessing a constant no longer in current CODATA data set. |
scipy.constants.physical\_constants[#](#scipy.constants.physical_constants "Link to this definition")
:   Dictionary of physical constants, of the format
    `physical_constants[name] = (value, unit, uncertainty)`.
    The CODATA database uses ellipses to indicate that a value is defined
    (exactly) in terms of others but cannot be represented exactly with the
    allocated number of digits. In these cases, SciPy calculates the derived
    value and reports it to the full precision of a Python `float`. Although
    `physical_constants` lists the uncertainty as `0.0` to indicate that
    the CODATA value is exact, the value in `physical_constants` is still
    subject to the truncation error inherent in double-precision representation.
Available constants:
|  |  |
| --- | --- |
| `alpha particle mass` | 6.644657345e-27 kg |
| `alpha particle mass energy equivalent` | 5.9719201997e-10 J |
| `alpha particle mass energy equivalent in MeV` | 3727.3794118 MeV |
| `alpha particle mass in u` | 4.001506179129 u |
| `alpha particle molar mass` | 0.0040015061833 kg mol^-1 |
| `alpha particle relative atomic mass` | 4.001506179129 |
| `alpha particle rms charge radius` | 1.6785e-15 m |
| `alpha particle-electron mass ratio` | 7294.29954171 |
| `alpha particle-proton mass ratio` | 3.972599690252 |
| `Angstrom star` | 1.00001495e-10 m |
| `atomic mass constant` | 1.66053906892e-27 kg |
| `atomic mass constant energy equivalent` | 1.49241808768e-10 J |
| `atomic mass constant energy equivalent in MeV` | 931.49410372 MeV |
| `atomic mass unit-electron volt relationship` | 931494103.72 eV |
| `atomic mass unit-hartree relationship` | 34231776.922 E\_h |
| `atomic mass unit-hertz relationship` | 2.25234272185e+23 Hz |
| `atomic mass unit-inverse meter relationship` | 751300662090000.0 m^-1 |
| `atomic mass unit-joule relationship` | 1.49241808768e-10 J |
| `atomic mass unit-kelvin relationship` | 10809540206700.0 K |
| `atomic mass unit-kilogram relationship` | 1.66053906892e-27 kg |
| `atomic unit of 1st hyperpolarizability` | 3.2063612996e-53 C^3 m^3 J^-2 |
| `atomic unit of 2nd hyperpolarizability` | 6.2353799735e-65 C^4 m^4 J^-3 |
| `atomic unit of action` | 1.0545718176461565e-34 J s |
| `atomic unit of charge` | 1.602176634e-19 C |
| `atomic unit of charge density` | 1081202386770.0 C m^-3 |
| `atomic unit of current` | 0.0066236182375082 A |
| `atomic unit of electric dipole mom.` | 8.4783536198e-30 C m |
| `atomic unit of electric field` | 514220675112.0 V m^-1 |
| `atomic unit of electric field gradient` | 9.7173624424e+21 V m^-2 |
| `atomic unit of electric polarizability` | 1.64877727212e-41 C^2 m^2 J^-1 |
| `atomic unit of electric potential` | 27.211386245981 V |
| `atomic unit of electric quadrupole mom.` | 4.4865515185e-40 C m^2 |
| `atomic unit of energy` | 4.359744722206e-18 J |
| `atomic unit of force` | 8.2387235038e-08 N |
| `atomic unit of length` | 5.29177210544e-11 m |
| `atomic unit of mag. dipole mom.` | 1.85480201315e-23 J T^-1 |
| `atomic unit of mag. flux density` | 235051.757077 T |
| `atomic unit of magnetizability` | 7.8910365794e-29 J T^-2 |
| `atomic unit of mass` | 9.1093837139e-31 kg |
| `atomic unit of momentum` | 1.99285191545e-24 kg m s^-1 |
| `atomic unit of permittivity` | 1.1126500562e-10 F m^-1 |
| `atomic unit of time` | 2.4188843265864e-17 s |
| `atomic unit of velocity` | 2187691.26216 m s^-1 |
| `Avogadro constant` | 6.02214076e+23 mol^-1 |
| `Bohr magneton` | 9.2740100657e-24 J T^-1 |
| `Bohr magneton in eV/T` | 5.7883817982e-05 eV T^-1 |
| `Bohr magneton in Hz/T` | 13996244917.1 Hz T^-1 |
| `Bohr magneton in inverse meter per tesla` | 46.686447719 m^-1 T^-1 |
| `Bohr magneton in K/T` | 0.67171381472 K T^-1 |
| `Bohr radius` | 5.29177210544e-11 m |
| `Boltzmann constant` | 1.380649e-23 J K^-1 |
| `Boltzmann constant in eV/K` | 8.617333262145179e-05 eV K^-1 |
| `Boltzmann constant in Hz/K` | 20836619123.327576 Hz K^-1 |
| `Boltzmann constant in inverse meter per kelvin` | 69.50348004861274 m^-1 K^-1 |
| `characteristic impedance of vacuum` | 376.730313412 ohm |
| `classical electron radius` | 2.8179403205e-15 m |
| `Compton wavelength` | 2.42631023538e-12 m |
| `conductance quantum` | 7.748091729863649e-05 S |
| `conventional value of ampere-90` | 1.0000000888714378 A |
| `conventional value of coulomb-90` | 1.0000000888714378 C |
| `conventional value of farad-90` | 0.9999999822063325 F |
| `conventional value of henry-90` | 1.0000000177936679 H |
| `conventional value of Josephson constant` | 483597900000000.0 Hz V^-1 |
| `conventional value of ohm-90` | 1.0000000177936679 ohm |
| `conventional value of volt-90` | 1.0000001066651072 V |
| `conventional value of von Klitzing constant` | 25812.807 ohm |
| `conventional value of watt-90` | 1.0000001955365543 W |
| `Copper x unit` | 1.00207697e-13 m |
| `deuteron g factor` | 0.8574382335 |
| `deuteron mag. mom.` | 4.330735087e-27 J T^-1 |
| `deuteron mag. mom. to Bohr magneton ratio` | 0.0004669754568 |
| `deuteron mag. mom. to nuclear magneton ratio` | 0.8574382335 |
| `deuteron mass` | 3.3435837768e-27 kg |
| `deuteron mass energy equivalent` | 3.00506323491e-10 J |
| `deuteron mass energy equivalent in MeV` | 1875.612945 MeV |
| `deuteron mass in u` | 2.013553212544 u |
| `deuteron molar mass` | 0.00201355321466 kg mol^-1 |
| `deuteron relative atomic mass` | 2.013553212544 |
| `deuteron rms charge radius` | 2.12778e-15 m |
| `deuteron-electron mag. mom. ratio` | -0.000466434555 |
| `deuteron-electron mass ratio` | 3670.482967655 |
| `deuteron-neutron mag. mom. ratio` | -0.44820652 |
| `deuteron-proton mag. mom. ratio` | 0.3070122093 |
| `deuteron-proton mass ratio` | 1.9990075012699 |
| `electron charge to mass quotient` | -175882000838.0 C kg^-1 |
| `electron g factor` | -2.00231930436092 |
| `electron gyromag. ratio` | 176085962784.0 s^-1 T^-1 |
| `electron gyromag. ratio in MHz/T` | 28024.9513861 MHz T^-1 |
| `electron mag. mom.` | -9.2847646917e-24 J T^-1 |
| `electron mag. mom. anomaly` | 0.00115965218046 |
| `electron mag. mom. to Bohr magneton ratio` | -1.00115965218046 |
| `electron mag. mom. to nuclear magneton ratio` | -1838.281971877 |
| `electron mass` | 9.1093837139e-31 kg |
| `electron mass energy equivalent` | 8.187105788e-14 J |
| `electron mass energy equivalent in MeV` | 0.51099895069 MeV |
| `electron mass in u` | 0.0005485799090441 u |
| `electron molar mass` | 5.4857990962e-07 kg mol^-1 |
| `electron relative atomic mass` | 0.0005485799090441 |
| `electron to alpha particle mass ratio` | 0.0001370933554733 |
| `electron to shielded helion mag. mom. ratio` | 864.05823986 |
| `electron to shielded proton mag. mom. ratio` | -658.2275856 |
| `electron volt` | 1.602176634e-19 J |
| `electron volt-atomic mass unit relationship` | 1.07354410083e-09 u |
| `electron volt-hartree relationship` | 0.036749322175665 E\_h |
| `electron volt-hertz relationship` | 241798924208491.8 Hz |
| `electron volt-inverse meter relationship` | 806554.3937349211 m^-1 |
| `electron volt-joule relationship` | 1.602176634e-19 J |
| `electron volt-kelvin relationship` | 11604.518121550082 K |
| `electron volt-kilogram relationship` | 1.7826619216278975e-36 kg |
| `electron-deuteron mag. mom. ratio` | -2143.9234921 |
| `electron-deuteron mass ratio` | 0.0002724437107629 |
| `electron-helion mass ratio` | 0.0001819543074649 |
| `electron-muon mag. mom. ratio` | 206.7669881 |
| `electron-muon mass ratio` | 0.0048363317 |
| `electron-neutron mag. mom. ratio` | 960.92048 |
| `electron-neutron mass ratio` | 0.00054386734416 |
| `electron-proton mag. mom. ratio` | -658.21068789 |
| `electron-proton mass ratio` | 0.0005446170214889 |
| `electron-tau mass ratio` | 0.000287585 |
| `electron-triton mass ratio` | 0.0001819200062327 |
| `elementary charge` | 1.602176634e-19 C |
| `elementary charge over h-bar` | 1519267447878626.0 A J^-1 |
| `Faraday constant` | 96485.33212331001 C mol^-1 |
| `Fermi coupling constant` | 1.1663787e-05 GeV^-2 |
| `fine-structure constant` | 0.0072973525643 |
| `first radiation constant` | 3.7417718521927573e-16 W m^2 |
| `first radiation constant for spectral radiance` | 1.1910429723971884e-16 W m^2 sr^-1 |
| `Hartree energy` | 4.359744722206e-18 J |
| `Hartree energy in eV` | 27.211386245981 eV |
| `hartree-atomic mass unit relationship` | 2.92126231797e-08 u |
| `hartree-electron volt relationship` | 27.211386245981 eV |
| `hartree-hertz relationship` | 6579683920499900.0 Hz |
| `hartree-inverse meter relationship` | 21947463.136314 m^-1 |
| `hartree-joule relationship` | 4.359744722206e-18 J |
| `hartree-kelvin relationship` | 315775.02480398 K |
| `hartree-kilogram relationship` | 4.8508702095419e-35 kg |
| `helion g factor` | -4.2552506995 |
| `helion mag. mom.` | -1.07461755198e-26 J T^-1 |
| `helion mag. mom. to Bohr magneton ratio` | -0.00115874098083 |
| `helion mag. mom. to nuclear magneton ratio` | -2.1276253498 |
| `helion mass` | 5.0064127862e-27 kg |
| `helion mass energy equivalent` | 4.4995394185e-10 J |
| `helion mass energy equivalent in MeV` | 2808.39161112 MeV |
| `helion mass in u` | 3.014932246932 u |
| `helion molar mass` | 0.0030149322501 kg mol^-1 |
| `helion relative atomic mass` | 3.014932246932 |
| `helion shielding shift` | 5.9967029e-05 |
| `helion-electron mass ratio` | 5495.88527984 |
| `helion-proton mass ratio` | 2.993152671552 |
| `hertz-atomic mass unit relationship` | 4.439821659e-24 u |
| `hertz-electron volt relationship` | 4.135667696923859e-15 eV |
| `hertz-hartree relationship` | 1.5198298460574e-16 E\_h |
| `hertz-inverse meter relationship` | 3.3356409519815204e-09 m^-1 |
| `hertz-joule relationship` | 6.62607015e-34 J |
| `hertz-kelvin relationship` | 4.799243073366221e-11 K |
| `hertz-kilogram relationship` | 7.372497323812708e-51 kg |
| `hyperfine transition frequency of Cs-133` | 9192631770.0 Hz |
| `inverse fine-structure constant` | 137.035999177 |
| `inverse meter-atomic mass unit relationship` | 1.33102504824e-15 u |
| `inverse meter-electron volt relationship` | 1.2398419843320026e-06 eV |
| `inverse meter-hartree relationship` | 4.5563352529132e-08 E\_h |
| `inverse meter-hertz relationship` | 299792458.0 Hz |
| `inverse meter-joule relationship` | 1.9864458571489286e-25 J |
| `inverse meter-kelvin relationship` | 0.014387768775039337 K |
| `inverse meter-kilogram relationship` | 2.2102190943042335e-42 kg |
| `inverse of conductance quantum` | 12906.403729652257 ohm |
| `Josephson constant` | 483597848416983.6 Hz V^-1 |
| `joule-atomic mass unit relationship` | 6700535247.1 u |
| `joule-electron volt relationship` | 6.241509074460763e+18 eV |
| `joule-hartree relationship` | 2.2937122783969e+17 E\_h |
| `joule-hertz relationship` | 1.5091901796421518e+33 Hz |
| `joule-inverse meter relationship` | 5.03411656754271e+24 m^-1 |
| `joule-kelvin relationship` | 7.24297051603992e+22 K |
| `joule-kilogram relationship` | 1.1126500560536185e-17 kg |
| `kelvin-atomic mass unit relationship` | 9.2510872884e-14 u |
| `kelvin-electron volt relationship` | 8.617333262145179e-05 eV |
| `kelvin-hartree relationship` | 3.1668115634564e-06 E\_h |
| `kelvin-hertz relationship` | 20836619123.327576 Hz |
| `kelvin-inverse meter relationship` | 69.50348004861274 m^-1 |
| `kelvin-joule relationship` | 1.380649e-23 J |
| `kelvin-kilogram relationship` | 1.5361791872403723e-40 kg |
| `kilogram-atomic mass unit relationship` | 6.0221407537e+26 u |
| `kilogram-electron volt relationship` | 5.609588603804452e+35 eV |
| `kilogram-hartree relationship` | 2.0614857887415e+34 E\_h |
| `kilogram-hertz relationship` | 1.3563924896521321e+50 Hz |
| `kilogram-inverse meter relationship` | 4.524438335443823e+41 m^-1 |
| `kilogram-joule relationship` | 8.987551787368176e+16 J |
| `kilogram-kelvin relationship` | 6.509657260728958e+39 K |
| `lattice parameter of silicon` | 5.431020511e-10 m |
| `lattice spacing of ideal Si (220)` | 1.920155716e-10 m |
| `Loschmidt constant (273.15 K, 100 kPa)` | 2.6516458048837345e+25 m^-3 |
| `Loschmidt constant (273.15 K, 101.325 kPa)` | 2.686780111798444e+25 m^-3 |
| `luminous efficacy` | 683.0 lm W^-1 |
| `mag. flux quantum` | 2.0678338484619295e-15 Wb |
| `molar gas constant` | 8.31446261815324 J mol^-1 K^-1 |
| `molar mass constant` | 0.00100000000105 kg mol^-1 |
| `molar mass of carbon-12` | 0.0120000000126 kg mol^-1 |
| `molar Planck constant` | 3.990312712893431e-10 J Hz^-1 mol^-1 |
| `molar volume of ideal gas (273.15 K, 100 kPa)` | 0.02271095464148557 m^3 mol^-1 |
| `molar volume of ideal gas (273.15 K, 101.325 kPa)` | 0.022413969545014137 m^3 mol^-1 |
| `molar volume of silicon` | 1.205883199e-05 m^3 mol^-1 |
| `Molybdenum x unit` | 1.00209952e-13 m |
| `muon Compton wavelength` | 1.17344411e-14 m |
| `muon g factor` | -2.00233184123 |
| `muon mag. mom.` | -4.4904483e-26 J T^-1 |
| `muon mag. mom. anomaly` | 0.00116592062 |
| `muon mag. mom. to Bohr magneton ratio` | -0.00484197048 |
| `muon mag. mom. to nuclear magneton ratio` | -8.89059704 |
| `muon mass` | 1.883531627e-28 kg |
| `muon mass energy equivalent` | 1.692833804e-11 J |
| `muon mass energy equivalent in MeV` | 105.6583755 MeV |
| `muon mass in u` | 0.1134289257 u |
| `muon molar mass` | 0.0001134289258 kg mol^-1 |
| `muon-electron mass ratio` | 206.7682827 |
| `muon-neutron mass ratio` | 0.1124545168 |
| `muon-proton mag. mom. ratio` | -3.183345146 |
| `muon-proton mass ratio` | 0.1126095262 |
| `muon-tau mass ratio` | 0.0594635 |
| `natural unit of action` | 1.0545718176461565e-34 J s |
| `natural unit of action in eV s` | 6.582119569509067e-16 eV s |
| `natural unit of energy` | 8.187105788e-14 J |
| `natural unit of energy in MeV` | 0.51099895069 MeV |
| `natural unit of length` | 3.8615926744e-13 m |
| `natural unit of mass` | 9.1093837139e-31 kg |
| `natural unit of momentum` | 2.730924488e-22 kg m s^-1 |
| `natural unit of momentum in MeV/c` | 0.5109989461 MeV/c |
| `natural unit of time` | 1.28808866644e-21 s |
| `natural unit of velocity` | 299792458.0 m s^-1 |
| `neutron Compton wavelength` | 1.31959090382e-15 m |
| `neutron g factor` | -3.82608552 |
| `neutron gyromag. ratio` | 183247174.0 s^-1 T^-1 |
| `neutron gyromag. ratio in MHz/T` | 29.1646935 MHz T^-1 |
| `neutron mag. mom.` | -9.6623653e-27 J T^-1 |
| `neutron mag. mom. to Bohr magneton ratio` | -0.00104187565 |
| `neutron mag. mom. to nuclear magneton ratio` | -1.91304276 |
| `neutron mass` | 1.67492750056e-27 kg |
| `neutron mass energy equivalent` | 1.50534976514e-10 J |
| `neutron mass energy equivalent in MeV` | 939.56542194 MeV |
| `neutron mass in u` | 1.00866491606 u |
| `neutron molar mass` | 0.00100866491712 kg mol^-1 |
| `neutron relative atomic mass` | 1.00866491606 |
| `neutron to shielded proton mag. mom. ratio` | -0.68499694 |
| `neutron-electron mag. mom. ratio` | 0.00104066884 |
| `neutron-electron mass ratio` | 1838.683662 |
| `neutron-muon mass ratio` | 8.89248408 |
| `neutron-proton mag. mom. ratio` | -0.68497935 |
| `neutron-proton mass difference` | 2.30557461e-30 kg |
| `neutron-proton mass difference energy equivalent` | 2.07214712e-13 J |
| `neutron-proton mass difference energy equivalent in MeV` | 1.29333251 MeV |
| `neutron-proton mass difference in u` | 0.00138844948 u |
| `neutron-proton mass ratio` | 1.00137841946 |
| `neutron-tau mass ratio` | 0.528779 |
| `Newtonian constant of gravitation` | 6.6743e-11 m^3 kg^-1 s^-2 |
| `Newtonian constant of gravitation over h-bar c` | 6.70883e-39 (GeV/c^2)^-2 |
| `nuclear magneton` | 5.0507837393e-27 J T^-1 |
| `nuclear magneton in eV/T` | 3.15245125417e-08 eV T^-1 |
| `nuclear magneton in inverse meter per tesla` | 0.0254262341009 m^-1 T^-1 |
| `nuclear magneton in K/T` | 0.00036582677706 K T^-1 |
| `nuclear magneton in MHz/T` | 7.6225932188 MHz T^-1 |
| `Planck constant` | 6.62607015e-34 J Hz^-1 |
| `Planck constant in eV/Hz` | 4.135667696923859e-15 eV Hz^-1 |
| `Planck length` | 1.616255e-35 m |
| `Planck mass` | 2.176434e-08 kg |
| `Planck mass energy equivalent in GeV` | 1.22089e+19 GeV |
| `Planck temperature` | 1.416784e+32 K |
| `Planck time` | 5.391247e-44 s |
| `proton charge to mass quotient` | 95788331.43 C kg^-1 |
| `proton Compton wavelength` | 1.3214098536e-15 m |
| `proton g factor` | 5.5856946893 |
| `proton gyromag. ratio` | 267522187.08 s^-1 T^-1 |
| `proton gyromag. ratio in MHz/T` | 42.577478461 MHz T^-1 |
| `proton mag. mom.` | 1.41060679545e-26 J T^-1 |
| `proton mag. mom. to Bohr magneton ratio` | 0.0015210322023 |
| `proton mag. mom. to nuclear magneton ratio` | 2.79284734463 |
| `proton mag. shielding correction` | 2.56715e-05 |
| `proton mass` | 1.67262192595e-27 kg |
| `proton mass energy equivalent` | 1.50327761802e-10 J |
| `proton mass energy equivalent in MeV` | 938.27208943 MeV |
| `proton mass in u` | 1.0072764665789 u |
| `proton molar mass` | 0.00100727646764 kg mol^-1 |
| `proton relative atomic mass` | 1.0072764665789 |
| `proton rms charge radius` | 8.4075e-16 m |
| `proton-electron mass ratio` | 1836.152673426 |
| `proton-muon mass ratio` | 8.88024338 |
| `proton-neutron mag. mom. ratio` | -1.45989802 |
| `proton-neutron mass ratio` | 0.99862347797 |
| `proton-tau mass ratio` | 0.528051 |
| `quantum of circulation` | 0.00036369475467 m^2 s^-1 |
| `quantum of circulation times 2` | 0.00072738950934 m^2 s^-1 |
| `reduced Compton wavelength` | 3.8615926744e-13 m |
| `reduced muon Compton wavelength` | 1.867594306e-15 m |
| `reduced neutron Compton wavelength` | 2.100194152e-16 m |
| `reduced Planck constant` | 1.0545718176461565e-34 J s |
| `reduced Planck constant in eV s` | 6.582119569509067e-16 eV s |
| `reduced Planck constant times c in MeV fm` | 197.3269804593025 MeV fm |
| `reduced proton Compton wavelength` | 2.10308910051e-16 m |
| `reduced tau Compton wavelength` | 1.110538e-16 m |
| `Rydberg constant` | 10973731.568157 m^-1 |
| `Rydberg constant times c in Hz` | 3289841960250000.0 Hz |
| `Rydberg constant times hc in eV` | 13.60569312299 eV |
| `Rydberg constant times hc in J` | 2.179872361103e-18 J |
| `Sackur-Tetrode constant (1 K, 100 kPa)` | -1.15170753496 |
| `Sackur-Tetrode constant (1 K, 101.325 kPa)` | -1.16487052149 |
| `second radiation constant` | 0.014387768775039337 m K |
| `shielded helion gyromag. ratio` | 203789460.78 s^-1 T^-1 |
| `shielded helion gyromag. ratio in MHz/T` | 32.434100033 MHz T^-1 |
| `shielded helion mag. mom.` | -1.07455311035e-26 J T^-1 |
| `shielded helion mag. mom. to Bohr magneton ratio` | -0.00115867149457 |
| `shielded helion mag. mom. to nuclear magneton ratio` | -2.1274977624 |
| `shielded helion to proton mag. mom. ratio` | -0.76176657721 |
| `shielded helion to shielded proton mag. mom. ratio` | -0.7617861334 |
| `shielded proton gyromag. ratio` | 267515319.4 s^-1 T^-1 |
| `shielded proton gyromag. ratio in MHz/T` | 42.57638543 MHz T^-1 |
| `shielded proton mag. mom.` | 1.410570583e-26 J T^-1 |
| `shielded proton mag. mom. to Bohr magneton ratio` | 0.0015209931551 |
| `shielded proton mag. mom. to nuclear magneton ratio` | 2.792775648 |
| `shielding difference of d and p in HD` | 1.9877e-08 |
| `shielding difference of t and p in HT` | 2.3945e-08 |
| `speed of light in vacuum` | 299792458.0 m s^-1 |
| `standard acceleration of gravity` | 9.80665 m s^-2 |
| `standard atmosphere` | 101325.0 Pa |
| `standard-state pressure` | 100000.0 Pa |
| `Stefan-Boltzmann constant` | 5.6703744191844314e-08 W m^-2 K^-4 |
| `tau Compton wavelength` | 6.97771e-16 m |
| `tau energy equivalent` | 1776.86 MeV |
| `tau mass` | 3.16754e-27 kg |
| `tau mass energy equivalent` | 2.84684e-10 J |
| `tau mass in u` | 1.90754 u |
| `tau molar mass` | 0.00190754 kg mol^-1 |
| `tau-electron mass ratio` | 3477.23 |
| `tau-muon mass ratio` | 16.817 |
| `tau-neutron mass ratio` | 1.89115 |
| `tau-proton mass ratio` | 1.89376 |
| `Thomson cross section` | 6.6524587051e-29 m^2 |
| `triton g factor` | 5.95792493 |
| `triton mag. mom.` | 1.5046095178e-26 J T^-1 |
| `triton mag. mom. to Bohr magneton ratio` | 0.0016223936648 |
| `triton mag. mom. to nuclear magneton ratio` | 2.978962465 |
| `triton mass` | 5.0073567512e-27 kg |
| `triton mass energy equivalent` | 4.5003878119e-10 J |
| `triton mass energy equivalent in MeV` | 2808.92113668 MeV |
| `triton mass in u` | 3.01550071597 u |
| `triton molar mass` | 0.00301550071913 kg mol^-1 |
| `triton relative atomic mass` | 3.01550071597 |
| `triton to proton mag. mom. ratio` | 1.0666399189 |
| `triton-electron mass ratio` | 5496.92153551 |
| `triton-proton mass ratio` | 2.99371703403 |
| `unified atomic mass unit` | 1.66053906892e-27 kg |
| `vacuum electric permittivity` | 8.8541878188e-12 F m^-1 |
| `vacuum mag. permeability` | 1.25663706127e-06 N A^-2 |
| `von Klitzing constant` | 25812.807459304513 ohm |
| `W to Z mass ratio` | 0.88145 |
| `weak mixing angle` | 0.22305 |
| `Wien frequency displacement law constant` | 58789257576.468254 Hz K^-1 |
| `Wien wavelength displacement law constant` | 0.0028977719551851727 m K |
## Units[#](#units "Link to this heading")
### SI prefixes[#](#si-prefixes "Link to this heading")
|  |  |
| --- | --- |
| `quetta` | \(10^{30}\) |
| `ronna` | \(10^{27}\) |
| `yotta` | \(10^{24}\) |
| `zetta` | \(10^{21}\) |
| `exa` | \(10^{18}\) |
| `peta` | \(10^{15}\) |
| `tera` | \(10^{12}\) |
| `giga` | \(10^{9}\) |
| `mega` | \(10^{6}\) |
| `kilo` | \(10^{3}\) |
| `hecto` | \(10^{2}\) |
| `deka` | \(10^{1}\) |
| `deci` | \(10^{-1}\) |
| `centi` | \(10^{-2}\) |
| `milli` | \(10^{-3}\) |
| `micro` | \(10^{-6}\) |
| `nano` | \(10^{-9}\) |
| `pico` | \(10^{-12}\) |
| `femto` | \(10^{-15}\) |
| `atto` | \(10^{-18}\) |
| `zepto` | \(10^{-21}\) |
| `yocto` | \(10^{-24}\) |
| `ronto` | \(10^{-27}\) |
| `quecto` | \(10^{-30}\) |
### Binary prefixes[#](#binary-prefixes "Link to this heading")
|  |  |
| --- | --- |
| `kibi` | \(2^{10}\) |
| `mebi` | \(2^{20}\) |
| `gibi` | \(2^{30}\) |
| `tebi` | \(2^{40}\) |
| `pebi` | \(2^{50}\) |
| `exbi` | \(2^{60}\) |
| `zebi` | \(2^{70}\) |
| `yobi` | \(2^{80}\) |
### Mass[#](#mass "Link to this heading")
|  |  |
| --- | --- |
| `gram` | \(10^{-3}\) kg |
| `metric_ton` | \(10^{3}\) kg |
| `grain` | one grain in kg |
| `lb` | one pound (avoirdupous) in kg |
| `pound` | one pound (avoirdupous) in kg |
| `blob` | one inch version of a slug in kg (added in 1.0.0) |
| `slinch` | one inch version of a slug in kg (added in 1.0.0) |
| `slug` | one slug in kg (added in 1.0.0) |
| `oz` | one ounce in kg |
| `ounce` | one ounce in kg |
| `stone` | one stone in kg |
| `long_ton` | one long ton in kg |
| `short_ton` | one short ton in kg |
| `troy_ounce` | one Troy ounce in kg |
| `troy_pound` | one Troy pound in kg |
| `carat` | one carat in kg |
| `m_u` | atomic mass constant (in kg) |
| `u` | atomic mass constant (in kg) |
| `atomic_mass` | atomic mass constant (in kg) |
### Angle[#](#angle "Link to this heading")
|  |  |
| --- | --- |
| `degree` | degree in radians |
| `arcmin` | arc minute in radians |
| `arcminute` | arc minute in radians |
| `arcsec` | arc second in radians |
| `arcsecond` | arc second in radians |
### Time[#](#time "Link to this heading")
|  |  |
| --- | --- |
| `minute` | one minute in seconds |
| `hour` | one hour in seconds |
| `day` | one day in seconds |
| `week` | one week in seconds |
| `year` | one year (365 days) in seconds |
| `Julian_year` | one Julian year (365.25 days) in seconds |
### Length[#](#length "Link to this heading")
|  |  |
| --- | --- |
| `inch` | one inch in meters |
| `foot` | one foot in meters |
| `yard` | one yard in meters |
| `mile` | one mile in meters |
| `mil` | one mil in meters |
| `pt` | one point in meters |
| `point` | one point in meters |
| `survey_foot` | one survey foot in meters |
| `survey_mile` | one survey mile in meters |
| `nautical_mile` | one nautical mile in meters |
| `fermi` | one Fermi in meters |
| `angstrom` | one Angstrom in meters |
| `micron` | one micron in meters |
| `au` | one astronomical unit in meters |
| `astronomical_unit` | one astronomical unit in meters |
| `light_year` | one light year in meters |
| `parsec` | one parsec in meters |
### Pressure[#](#pressure "Link to this heading")
|  |  |
| --- | --- |
| `atm` | standard atmosphere in pascals |
| `atmosphere` | standard atmosphere in pascals |
| `bar` | one bar in pascals |
| `torr` | one torr (mmHg) in pascals |
| `mmHg` | one torr (mmHg) in pascals |
| `psi` | one psi in pascals |
### Area[#](#area "Link to this heading")
|  |  |
| --- | --- |
| `hectare` | one hectare in square meters |
| `acre` | one acre in square meters |
### Volume[#](#volume "Link to this heading")
|  |  |
| --- | --- |
| `liter` | one liter in cubic meters |
| `litre` | one liter in cubic meters |
| `gallon` | one gallon (US) in cubic meters |
| `gallon_US` | one gallon (US) in cubic meters |
| `gallon_imp` | one gallon (UK) in cubic meters |
| `fluid_ounce` | one fluid ounce (US) in cubic meters |
| `fluid_ounce_US` | one fluid ounce (US) in cubic meters |
| `fluid_ounce_imp` | one fluid ounce (UK) in cubic meters |
| `bbl` | one barrel in cubic meters |
| `barrel` | one barrel in cubic meters |
### Speed[#](#speed "Link to this heading")
|  |  |
| --- | --- |
| `kmh` | kilometers per hour in meters per second |
| `mph` | miles per hour in meters per second |
| `mach` | one Mach (approx., at 15 C, 1 atm) in meters per second |
| `speed_of_sound` | one Mach (approx., at 15 C, 1 atm) in meters per second |
| `knot` | one knot in meters per second |
### Temperature[#](#temperature "Link to this heading")
|  |  |
| --- | --- |
| `zero_Celsius` | zero of Celsius scale in Kelvin |
| `degree_Fahrenheit` | one Fahrenheit (only differences) in Kelvins |
|  |  |
| --- | --- |
| [`convert_temperature`](generated/scipy.constants.convert_temperature.html#scipy.constants.convert_temperature "scipy.constants.convert_temperature")(val,Â old\_scale,Â new\_scale) | Convert from a temperature scale to another one among Celsius, Kelvin, Fahrenheit, and Rankine scales. |
### Energy[#](#energy "Link to this heading")
|  |  |
| --- | --- |
| `eV` | one electron volt in Joules |
| `electron_volt` | one electron volt in Joules |
| `calorie` | one calorie (thermochemical) in Joules |
| `calorie_th` | one calorie (thermochemical) in Joules |
| `calorie_IT` | one calorie (International Steam Table calorie, 1956) in Joules |
| `erg` | one erg in Joules |
| `Btu` | one British thermal unit (International Steam Table) in Joules |
| `Btu_IT` | one British thermal unit (International Steam Table) in Joules |
| `Btu_th` | one British thermal unit (thermochemical) in Joules |
| `ton_TNT` | one ton of TNT in Joules |
### Power[#](#power "Link to this heading")
|  |  |
| --- | --- |
| `hp` | one horsepower in watts |
| `horsepower` | one horsepower in watts |
### Force[#](#force "Link to this heading")
|  |  |
| --- | --- |
| `dyn` | one dyne in newtons |
| `dyne` | one dyne in newtons |
| `lbf` | one pound force in newtons |
| `pound_force` | one pound force in newtons |
| `kgf` | one kilogram force in newtons |
| `kilogram_force` | one kilogram force in newtons |
### Optics[#](#optics "Link to this heading")
|  |  |
| --- | --- |
| [`lambda2nu`](generated/scipy.constants.lambda2nu.html#scipy.constants.lambda2nu "scipy.constants.lambda2nu")(lambda\_) | Convert wavelength to optical frequency. |
| [`nu2lambda`](generated/scipy.constants.nu2lambda.html#scipy.constants.nu2lambda "scipy.constants.nu2lambda")(nu) | Convert optical frequency to wavelength. |
## References[#](#references "Link to this heading")
[[CODATA2022](#id1)]
CODATA Recommended Values of the Fundamental
Physical Constants 2022.
<https://physics.nist.gov/cuu/Constants/>
[previous
scipy.cluster.hierarchy.ClusterWarning](generated/scipy.cluster.hierarchy.ClusterWarning.html "previous page")
[next
value](generated/scipy.constants.value.html "next page")
On this page
* [Mathematical constants](#mathematical-constants)
* [Physical constants](#physical-constants)
  + [Constants database](#constants-database)
    - [`physical_constants`](#scipy.constants.physical_constants)
* [Units](#units)
  + [SI prefixes](#si-prefixes)
  + [Binary prefixes](#binary-prefixes)
  + [Mass](#mass)
  + [Angle](#angle)
  + [Time](#time)
  + [Length](#length)
  + [Pressure](#pressure)
  + [Area](#area)
  + [Volume](#volume)
  + [Speed](#speed)
  + [Temperature](#temperature)
  + [Energy](#energy)
  + [Power](#power)
  + [Force](#force)
  + [Optics](#optics)
* [References](#references)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/datasets.html#module-scipy.datasets -->
* [SciPy API](index.html)
* Datasets (`scipy.datasets`)
# Datasets ([`scipy.datasets`](#module-scipy.datasets "scipy.datasets"))[#](#datasets-scipy-datasets "Link to this heading")
## Dataset Methods[#](#dataset-methods "Link to this heading")
|  |  |
| --- | --- |
| [`ascent`](generated/scipy.datasets.ascent.html#scipy.datasets.ascent "scipy.datasets.ascent")() | Get an 8-bit grayscale bit-depth, 512 x 512 derived image for easy use in demos. |
| [`face`](generated/scipy.datasets.face.html#scipy.datasets.face "scipy.datasets.face")([gray]) | Get a 1024 x 768, color image of a raccoon face. |
| [`electrocardiogram`](generated/scipy.datasets.electrocardiogram.html#scipy.datasets.electrocardiogram "scipy.datasets.electrocardiogram")() | Load an electrocardiogram as an example for a 1-D signal. |
## Utility Methods[#](#utility-methods "Link to this heading")
|  |  |
| --- | --- |
| [`download_all`](generated/scipy.datasets.download_all.html#scipy.datasets.download_all "scipy.datasets.download_all")([path]) | Utility method to download all the dataset files for [`scipy.datasets`](#module-scipy.datasets "scipy.datasets") module. |
| [`clear_cache`](generated/scipy.datasets.clear_cache.html#scipy.datasets.clear_cache "scipy.datasets.clear_cache")([datasets]) | Cleans the SciPy datasets cache directory. |
## Usage of Datasets[#](#usage-of-datasets "Link to this heading")
SciPy dataset methods can be simply called as follows: `'<dataset-name>()'`
This downloads the dataset files over the network once, and saves the cache,
before returning a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)") object representing the dataset.
Note that the return data structure and data type might be different for
different dataset methods. For a more detailed example on usage, please look
into the particular dataset method documentation above.
## How dataset retrieval and storage works[#](#how-dataset-retrieval-and-storage-works "Link to this heading")
SciPy dataset files are stored within individual GitHub repositories under the
SciPy GitHub organization, following a naming convention as
`'dataset-<name>'`, for example [`scipy.datasets.face`](generated/scipy.datasets.face.html#scipy.datasets.face "scipy.datasets.face") files live at
[scipy/dataset-face](https://github.com/scipy/dataset-face). The [`scipy.datasets`](#module-scipy.datasets "scipy.datasets") submodule utilizes
and depends on [Pooch](https://www.fatiando.org/pooch/latest/), a Python
package built to simplify fetching data files. Pooch uses these repos to
retrieve the respective dataset files when calling the dataset function.
A registry of all the datasets, essentially a mapping of filenames with their
SHA256 hash and repo urls are maintained, which Pooch uses to handle and verify
the downloads on function call. After downloading the dataset once, the files
are saved in the system cache directory under `'scipy-data'`.
Dataset cache locations may vary on different platforms.
For macOS:
```
'~/Library/Caches/scipy-data'
```
For Linux and other Unix-like platforms:
```
'~/.cache/scipy-data'  # or the value of the XDG_CACHE_HOME env var, if defined
```
For Windows:
```
'C:\Users\<user>\AppData\Local\<AppAuthor>\scipy-data\Cache'
```
In environments with constrained network connectivity for various security
reasons or on systems without continuous internet connections, one may manually
load the cache of the datasets by placing the contents of the dataset repo in
the above mentioned cache directory to avoid fetching dataset errors without
the internet connectivity.
[previous
nu2lambda](generated/scipy.constants.nu2lambda.html "previous page")
[next
ascent](generated/scipy.datasets.ascent.html "next page")
On this page
* [Dataset Methods](#dataset-methods)
* [Utility Methods](#utility-methods)
* [Usage of Datasets](#usage-of-datasets)
* [How dataset retrieval and storage works](#how-dataset-retrieval-and-storage-works)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/differentiate.html#module-scipy.differentiate -->
* [SciPy API](index.html)
* Finite Difference Differentiation (`scipy.differentiate`)
# Finite Difference Differentiation ([`scipy.differentiate`](#module-scipy.differentiate "scipy.differentiate"))[#](#finite-difference-differentiation-scipy-differentiate "Link to this heading")
SciPy `differentiate` provides functions for performing finite difference
numerical differentiation of black-box functions.
|  |  |
| --- | --- |
| [`derivative`](generated/scipy.differentiate.derivative.html#scipy.differentiate.derivative "scipy.differentiate.derivative")(f,Â x,Â \*[,Â args,Â kwargs,Â ...]) | Evaluate the derivative of an elementwise, real scalar function numerically. |
| [`jacobian`](generated/scipy.differentiate.jacobian.html#scipy.differentiate.jacobian "scipy.differentiate.jacobian")(f,Â x,Â \*[,Â tolerances,Â maxiter,Â ...]) | Evaluate the Jacobian of a function numerically. |
| [`hessian`](generated/scipy.differentiate.hessian.html#scipy.differentiate.hessian "scipy.differentiate.hessian")(f,Â x,Â \*[,Â tolerances,Â maxiter,Â ...]) | Evaluate the Hessian of a function numerically. |
[previous
clear\_cache](generated/scipy.datasets.clear_cache.html "previous page")
[next
derivative](generated/scipy.differentiate.derivative.html "next page")
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/fft.html#module-scipy.fft -->
* [SciPy API](index.html)
* Discrete Fourier transforms (`scipy.fft`)
# Discrete Fourier transforms ([`scipy.fft`](#module-scipy.fft "scipy.fft"))[#](#discrete-fourier-transforms-scipy-fft "Link to this heading")
## Fast Fourier Transforms (FFTs)[#](#fast-fourier-transforms-ffts "Link to this heading")
|  |  |
| --- | --- |
| [`fft`](generated/scipy.fft.fft.html#scipy.fft.fft "scipy.fft.fft")(x[,Â n,Â axis,Â norm,Â overwrite\_x,Â ...]) | Compute the 1-D discrete Fourier Transform. |
| [`ifft`](generated/scipy.fft.ifft.html#scipy.fft.ifft "scipy.fft.ifft")(x[,Â n,Â axis,Â norm,Â overwrite\_x,Â ...]) | Compute the 1-D inverse discrete Fourier Transform. |
| [`fft2`](generated/scipy.fft.fft2.html#scipy.fft.fft2 "scipy.fft.fft2")(x[,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Compute the 2-D discrete Fourier Transform. |
| [`ifft2`](generated/scipy.fft.ifft2.html#scipy.fft.ifft2 "scipy.fft.ifft2")(x[,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Compute the 2-D inverse discrete Fourier Transform. |
| [`fftn`](generated/scipy.fft.fftn.html#scipy.fft.fftn "scipy.fft.fftn")(x[,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Compute the N-D discrete Fourier Transform. |
| [`ifftn`](generated/scipy.fft.ifftn.html#scipy.fft.ifftn "scipy.fft.ifftn")(x[,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Compute the N-D inverse discrete Fourier Transform. |
| [`rfft`](generated/scipy.fft.rfft.html#scipy.fft.rfft "scipy.fft.rfft")(x[,Â n,Â axis,Â norm,Â overwrite\_x,Â ...]) | Compute the 1-D discrete Fourier Transform for real input. |
| [`irfft`](generated/scipy.fft.irfft.html#scipy.fft.irfft "scipy.fft.irfft")(x[,Â n,Â axis,Â norm,Â overwrite\_x,Â ...]) | Computes the inverse of [`rfft`](generated/scipy.fft.rfft.html#scipy.fft.rfft "scipy.fft.rfft"). |
| [`rfft2`](generated/scipy.fft.rfft2.html#scipy.fft.rfft2 "scipy.fft.rfft2")(x[,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Compute the 2-D FFT of a real array. |
| [`irfft2`](generated/scipy.fft.irfft2.html#scipy.fft.irfft2 "scipy.fft.irfft2")(x[,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Computes the inverse of [`rfft2`](generated/scipy.fft.rfft2.html#scipy.fft.rfft2 "scipy.fft.rfft2"). |
| [`rfftn`](generated/scipy.fft.rfftn.html#scipy.fft.rfftn "scipy.fft.rfftn")(x[,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Compute the N-D discrete Fourier Transform for real input. |
| [`irfftn`](generated/scipy.fft.irfftn.html#scipy.fft.irfftn "scipy.fft.irfftn")(x[,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Computes the inverse of [`rfftn`](generated/scipy.fft.rfftn.html#scipy.fft.rfftn "scipy.fft.rfftn"). |
| [`hfft`](generated/scipy.fft.hfft.html#scipy.fft.hfft "scipy.fft.hfft")(x[,Â n,Â axis,Â norm,Â overwrite\_x,Â ...]) | Compute the FFT of a signal that has Hermitian symmetry, i.e., a real spectrum. |
| [`ihfft`](generated/scipy.fft.ihfft.html#scipy.fft.ihfft "scipy.fft.ihfft")(x[,Â n,Â axis,Â norm,Â overwrite\_x,Â ...]) | Compute the inverse FFT of a signal that has Hermitian symmetry. |
| [`hfft2`](generated/scipy.fft.hfft2.html#scipy.fft.hfft2 "scipy.fft.hfft2")(x[,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Compute the 2-D FFT of a Hermitian complex array. |
| [`ihfft2`](generated/scipy.fft.ihfft2.html#scipy.fft.ihfft2 "scipy.fft.ihfft2")(x[,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Compute the 2-D inverse FFT of a real spectrum. |
| [`hfftn`](generated/scipy.fft.hfftn.html#scipy.fft.hfftn "scipy.fft.hfftn")(x[,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Compute the N-D FFT of Hermitian symmetric complex input, i.e., a signal with a real spectrum. |
| [`ihfftn`](generated/scipy.fft.ihfftn.html#scipy.fft.ihfftn "scipy.fft.ihfftn")(x[,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Compute the N-D inverse discrete Fourier Transform for a real spectrum. |
## Discrete Sin and Cosine Transforms (DST and DCT)[#](#discrete-sin-and-cosine-transforms-dst-and-dct "Link to this heading")
|  |  |
| --- | --- |
| [`dct`](generated/scipy.fft.dct.html#scipy.fft.dct "scipy.fft.dct")(x[,Â type,Â n,Â axis,Â norm,Â overwrite\_x,Â ...]) | Return the Discrete Cosine Transform of arbitrary type sequence x. |
| [`idct`](generated/scipy.fft.idct.html#scipy.fft.idct "scipy.fft.idct")(x[,Â type,Â n,Â axis,Â norm,Â overwrite\_x,Â ...]) | Return the Inverse Discrete Cosine Transform of an arbitrary type sequence. |
| [`dctn`](generated/scipy.fft.dctn.html#scipy.fft.dctn "scipy.fft.dctn")(x[,Â type,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Return multidimensional Discrete Cosine Transform along the specified axes. |
| [`idctn`](generated/scipy.fft.idctn.html#scipy.fft.idctn "scipy.fft.idctn")(x[,Â type,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Return multidimensional Inverse Discrete Cosine Transform along the specified axes. |
| [`dst`](generated/scipy.fft.dst.html#scipy.fft.dst "scipy.fft.dst")(x[,Â type,Â n,Â axis,Â norm,Â overwrite\_x,Â ...]) | Return the Discrete Sine Transform of arbitrary type sequence x. |
| [`idst`](generated/scipy.fft.idst.html#scipy.fft.idst "scipy.fft.idst")(x[,Â type,Â n,Â axis,Â norm,Â overwrite\_x,Â ...]) | Return the Inverse Discrete Sine Transform of an arbitrary type sequence. |
| [`dstn`](generated/scipy.fft.dstn.html#scipy.fft.dstn "scipy.fft.dstn")(x[,Â type,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Return multidimensional Discrete Sine Transform along the specified axes. |
| [`idstn`](generated/scipy.fft.idstn.html#scipy.fft.idstn "scipy.fft.idstn")(x[,Â type,Â s,Â axes,Â norm,Â overwrite\_x,Â ...]) | Return multidimensional Inverse Discrete Sine Transform along the specified axes. |
## Fast Hankel Transforms[#](#fast-hankel-transforms "Link to this heading")
|  |  |
| --- | --- |
| [`fht`](generated/scipy.fft.fht.html#scipy.fft.fht "scipy.fft.fht")(a,Â dln,Â mu[,Â offset,Â bias]) | Compute the fast Hankel transform. |
| [`ifht`](generated/scipy.fft.ifht.html#scipy.fft.ifht "scipy.fft.ifht")(A,Â dln,Â mu[,Â offset,Â bias]) | Compute the inverse fast Hankel transform. |
## Helper functions[#](#helper-functions "Link to this heading")
|  |  |
| --- | --- |
| [`fftshift`](generated/scipy.fft.fftshift.html#scipy.fft.fftshift "scipy.fft.fftshift")(x[,Â axes]) | Shift the zero-frequency component to the center of the spectrum. |
| [`ifftshift`](generated/scipy.fft.ifftshift.html#scipy.fft.ifftshift "scipy.fft.ifftshift")(x[,Â axes]) | The inverse of [`fftshift`](generated/scipy.fft.fftshift.html#scipy.fft.fftshift "scipy.fft.fftshift"). |
| [`fftfreq`](generated/scipy.fft.fftfreq.html#scipy.fft.fftfreq "scipy.fft.fftfreq")(n[,Â d,Â xp,Â device]) | Return the Discrete Fourier Transform sample frequencies. |
| [`rfftfreq`](generated/scipy.fft.rfftfreq.html#scipy.fft.rfftfreq "scipy.fft.rfftfreq")(n[,Â d,Â xp,Â device]) | Return the Discrete Fourier Transform sample frequencies (for usage with rfft, irfft). |
| [`fhtoffset`](generated/scipy.fft.fhtoffset.html#scipy.fft.fhtoffset "scipy.fft.fhtoffset")(dln,Â mu[,Â initial,Â bias]) | Return optimal offset for a fast Hankel transform. |
| [`next_fast_len`](generated/scipy.fft.next_fast_len.html#scipy.fft.next_fast_len "scipy.fft.next_fast_len")(target[,Â real]) | Find the next fast size of input data to `fft`, for zero-padding, etc. |
| [`prev_fast_len`](generated/scipy.fft.prev_fast_len.html#scipy.fft.prev_fast_len "scipy.fft.prev_fast_len")(target[,Â real]) | Find the previous fast size of input data to `fft`. |
| [`set_workers`](generated/scipy.fft.set_workers.html#scipy.fft.set_workers "scipy.fft.set_workers")(workers) | Context manager for the default number of workers used in [`scipy.fft`](#module-scipy.fft "scipy.fft"). |
| [`get_workers`](generated/scipy.fft.get_workers.html#scipy.fft.get_workers "scipy.fft.get_workers")() | Returns the default number of workers within the current context. |
## Backend control[#](#backend-control "Link to this heading")
|  |  |
| --- | --- |
| [`set_backend`](generated/scipy.fft.set_backend.html#scipy.fft.set_backend "scipy.fft.set_backend")(backend[,Â coerce,Â only]) | Context manager to set the backend within a fixed scope. |
| [`skip_backend`](generated/scipy.fft.skip_backend.html#scipy.fft.skip_backend "scipy.fft.skip_backend")(backend) | Context manager to skip a backend within a fixed scope. |
| [`set_global_backend`](generated/scipy.fft.set_global_backend.html#scipy.fft.set_global_backend "scipy.fft.set_global_backend")(backend[,Â coerce,Â only,Â ...]) | Sets the global fft backend. |
| [`register_backend`](generated/scipy.fft.register_backend.html#scipy.fft.register_backend "scipy.fft.register_backend")(backend) | Register a backend for permanent use. |
[previous
hessian](generated/scipy.differentiate.hessian.html "previous page")
[next
fft](generated/scipy.fft.fft.html "next page")
On this page
* [Fast Fourier Transforms (FFTs)](#fast-fourier-transforms-ffts)
* [Discrete Sin and Cosine Transforms (DST and DCT)](#discrete-sin-and-cosine-transforms-dst-and-dct)
* [Fast Hankel Transforms](#fast-hankel-transforms)
* [Helper functions](#helper-functions)
* [Backend control](#backend-control)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/fftpack.html#module-scipy.fftpack -->
* [SciPy API](index.html)
* Legacy discrete Fourier transforms (`scipy.fftpack`)
# Legacy discrete Fourier transforms ([`scipy.fftpack`](#module-scipy.fftpack "scipy.fftpack"))[#](#legacy-discrete-fourier-transforms-scipy-fftpack "Link to this heading")
Legacy
This submodule is considered legacy and will no longer receive updates. While we currently have no plans to remove it, we recommend that new code uses more modern alternatives instead. New code should use [`scipy.fft`](fft.html#module-scipy.fft "scipy.fft").
## Fast Fourier Transforms (FFTs)[#](#fast-fourier-transforms-ffts "Link to this heading")
|  |  |
| --- | --- |
| [`fft`](generated/scipy.fftpack.fft.html#scipy.fftpack.fft "scipy.fftpack.fft")(x[,Â n,Â axis,Â overwrite\_x]) | Return discrete Fourier transform of real or complex sequence. |
| [`ifft`](generated/scipy.fftpack.ifft.html#scipy.fftpack.ifft "scipy.fftpack.ifft")(x[,Â n,Â axis,Â overwrite\_x]) | Return discrete inverse Fourier transform of real or complex sequence. |
| [`fft2`](generated/scipy.fftpack.fft2.html#scipy.fftpack.fft2 "scipy.fftpack.fft2")(x[,Â shape,Â axes,Â overwrite\_x]) | 2-D discrete Fourier transform. |
| [`ifft2`](generated/scipy.fftpack.ifft2.html#scipy.fftpack.ifft2 "scipy.fftpack.ifft2")(x[,Â shape,Â axes,Â overwrite\_x]) | 2-D discrete inverse Fourier transform of real or complex sequence. |
| [`fftn`](generated/scipy.fftpack.fftn.html#scipy.fftpack.fftn "scipy.fftpack.fftn")(x[,Â shape,Â axes,Â overwrite\_x]) | Return multidimensional discrete Fourier transform. |
| [`ifftn`](generated/scipy.fftpack.ifftn.html#scipy.fftpack.ifftn "scipy.fftpack.ifftn")(x[,Â shape,Â axes,Â overwrite\_x]) | Return inverse multidimensional discrete Fourier transform. |
| [`rfft`](generated/scipy.fftpack.rfft.html#scipy.fftpack.rfft "scipy.fftpack.rfft")(x[,Â n,Â axis,Â overwrite\_x]) | Discrete Fourier transform of a real sequence. |
| [`irfft`](generated/scipy.fftpack.irfft.html#scipy.fftpack.irfft "scipy.fftpack.irfft")(x[,Â n,Â axis,Â overwrite\_x]) | Return inverse discrete Fourier transform of real sequence x. |
| [`dct`](generated/scipy.fftpack.dct.html#scipy.fftpack.dct "scipy.fftpack.dct")(x[,Â type,Â n,Â axis,Â norm,Â overwrite\_x]) | Return the Discrete Cosine Transform of arbitrary type sequence x. |
| [`idct`](generated/scipy.fftpack.idct.html#scipy.fftpack.idct "scipy.fftpack.idct")(x[,Â type,Â n,Â axis,Â norm,Â overwrite\_x]) | Return the Inverse Discrete Cosine Transform of an arbitrary type sequence. |
| [`dctn`](generated/scipy.fftpack.dctn.html#scipy.fftpack.dctn "scipy.fftpack.dctn")(x[,Â type,Â shape,Â axes,Â norm,Â overwrite\_x]) | Return multidimensional Discrete Cosine Transform along the specified axes. |
| [`idctn`](generated/scipy.fftpack.idctn.html#scipy.fftpack.idctn "scipy.fftpack.idctn")(x[,Â type,Â shape,Â axes,Â norm,Â overwrite\_x]) | Return multidimensional Discrete Cosine Transform along the specified axes. |
| [`dst`](generated/scipy.fftpack.dst.html#scipy.fftpack.dst "scipy.fftpack.dst")(x[,Â type,Â n,Â axis,Â norm,Â overwrite\_x]) | Return the Discrete Sine Transform of arbitrary type sequence x. |
| [`idst`](generated/scipy.fftpack.idst.html#scipy.fftpack.idst "scipy.fftpack.idst")(x[,Â type,Â n,Â axis,Â norm,Â overwrite\_x]) | Return the Inverse Discrete Sine Transform of an arbitrary type sequence. |
| [`dstn`](generated/scipy.fftpack.dstn.html#scipy.fftpack.dstn "scipy.fftpack.dstn")(x[,Â type,Â shape,Â axes,Â norm,Â overwrite\_x]) | Return multidimensional Discrete Sine Transform along the specified axes. |
| [`idstn`](generated/scipy.fftpack.idstn.html#scipy.fftpack.idstn "scipy.fftpack.idstn")(x[,Â type,Â shape,Â axes,Â norm,Â overwrite\_x]) | Return multidimensional Discrete Sine Transform along the specified axes. |
## Differential and pseudo-differential operators[#](#differential-and-pseudo-differential-operators "Link to this heading")
|  |  |
| --- | --- |
| [`diff`](generated/scipy.fftpack.diff.html#scipy.fftpack.diff "scipy.fftpack.diff")(x[,Â order,Â period,Â \_cache]) | Return kth derivative (or integral) of a periodic sequence x. |
| [`tilbert`](generated/scipy.fftpack.tilbert.html#scipy.fftpack.tilbert "scipy.fftpack.tilbert")(x,Â h[,Â period,Â \_cache]) | Return h-Tilbert transform of a periodic sequence x. |
| [`itilbert`](generated/scipy.fftpack.itilbert.html#scipy.fftpack.itilbert "scipy.fftpack.itilbert")(x,Â h[,Â period,Â \_cache]) | Return inverse h-Tilbert transform of a periodic sequence x. |
| [`hilbert`](generated/scipy.fftpack.hilbert.html#scipy.fftpack.hilbert "scipy.fftpack.hilbert")(x[,Â \_cache]) | Return Hilbert transform of a periodic sequence x. |
| [`ihilbert`](generated/scipy.fftpack.ihilbert.html#scipy.fftpack.ihilbert "scipy.fftpack.ihilbert")(x[,Â \_cache]) | Return inverse Hilbert transform of a periodic sequence x. |
| [`cs_diff`](generated/scipy.fftpack.cs_diff.html#scipy.fftpack.cs_diff "scipy.fftpack.cs_diff")(x,Â a,Â b[,Â period,Â \_cache]) | Return (a,b)-cosh/sinh pseudo-derivative of a periodic sequence. |
| [`sc_diff`](generated/scipy.fftpack.sc_diff.html#scipy.fftpack.sc_diff "scipy.fftpack.sc_diff")(x,Â a,Â b[,Â period,Â \_cache]) | Return (a,b)-sinh/cosh pseudo-derivative of a periodic sequence x. |
| [`ss_diff`](generated/scipy.fftpack.ss_diff.html#scipy.fftpack.ss_diff "scipy.fftpack.ss_diff")(x,Â a,Â b[,Â period,Â \_cache]) | Return (a,b)-sinh/sinh pseudo-derivative of a periodic sequence x. |
| [`cc_diff`](generated/scipy.fftpack.cc_diff.html#scipy.fftpack.cc_diff "scipy.fftpack.cc_diff")(x,Â a,Â b[,Â period,Â \_cache]) | Return (a,b)-cosh/cosh pseudo-derivative of a periodic sequence. |
| [`shift`](generated/scipy.fftpack.shift.html#scipy.fftpack.shift "scipy.fftpack.shift")(x,Â a[,Â period,Â \_cache]) | Shift periodic sequence x by a: y(u) = x(u+a). |
## Helper functions[#](#helper-functions "Link to this heading")
|  |  |
| --- | --- |
| [`fftshift`](generated/scipy.fftpack.fftshift.html#scipy.fftpack.fftshift "scipy.fftpack.fftshift")(x[,Â axes]) | Shift the zero-frequency component to the center of the spectrum. |
| [`ifftshift`](generated/scipy.fftpack.ifftshift.html#scipy.fftpack.ifftshift "scipy.fftpack.ifftshift")(x[,Â axes]) | The inverse of [`fftshift`](generated/scipy.fftpack.fftshift.html#scipy.fftpack.fftshift "scipy.fftpack.fftshift"). |
| [`fftfreq`](generated/scipy.fftpack.fftfreq.html#scipy.fftpack.fftfreq "scipy.fftpack.fftfreq")(n[,Â d,Â device]) | Return the Discrete Fourier Transform sample frequencies. |
| [`rfftfreq`](generated/scipy.fftpack.rfftfreq.html#scipy.fftpack.rfftfreq "scipy.fftpack.rfftfreq")(n[,Â d]) | DFT sample frequencies (for usage with rfft, irfft). |
| [`next_fast_len`](generated/scipy.fftpack.next_fast_len.html#scipy.fftpack.next_fast_len "scipy.fftpack.next_fast_len")(target) | Find the next fast size of input data to [`fft`](generated/scipy.fftpack.fft.html#scipy.fftpack.fft "scipy.fftpack.fft"), for zero-padding, etc. |
Note that `fftshift`, `ifftshift` and `fftfreq` are numpy functions
exposed by `fftpack`; importing them from `numpy` should be preferred.
## Convolutions ([`scipy.fftpack.convolve`](#module-scipy.fftpack.convolve "scipy.fftpack.convolve"))[#](#module-scipy.fftpack.convolve "Link to this heading")
|  |  |
| --- | --- |
| [`convolve`](generated/scipy.fftpack.convolve.convolve.html#scipy.fftpack.convolve.convolve "scipy.fftpack.convolve.convolve")(x,omega,[swap\_real\_imag,overwrite\_x]) | Wrapper for `convolve`. |
| [`convolve_z`](generated/scipy.fftpack.convolve.convolve_z.html#scipy.fftpack.convolve.convolve_z "scipy.fftpack.convolve.convolve_z")(x,omega\_real,omega\_imag,[overwrite\_x]) | Wrapper for `convolve_z`. |
| [`init_convolution_kernel`](generated/scipy.fftpack.convolve.init_convolution_kernel.html#scipy.fftpack.convolve.init_convolution_kernel "scipy.fftpack.convolve.init_convolution_kernel")(...) | Wrapper for `init_convolution_kernel`. |
| [`destroy_convolve_cache`](generated/scipy.fftpack.convolve.destroy_convolve_cache.html#scipy.fftpack.convolve.destroy_convolve_cache "scipy.fftpack.convolve.destroy_convolve_cache")() |  |
[previous
register\_backend](generated/scipy.fft.register_backend.html "previous page")
[next
fft](generated/scipy.fftpack.fft.html "next page")
On this page
* [Fast Fourier Transforms (FFTs)](#fast-fourier-transforms-ffts)
* [Differential and pseudo-differential operators](#differential-and-pseudo-differential-operators)
* [Helper functions](#helper-functions)
* [Convolutions (`scipy.fftpack.convolve`)](#module-scipy.fftpack.convolve)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/integrate.html#module-scipy.integrate -->
* [SciPy API](index.html)
* Integration and ODEs (`scipy.integrate`)
# Integration and ODEs ([`scipy.integrate`](#module-scipy.integrate "scipy.integrate"))[#](#integration-and-odes-scipy-integrate "Link to this heading")
## Integrating functions, given function object[#](#integrating-functions-given-function-object "Link to this heading")
|  |  |
| --- | --- |
| [`quad`](generated/scipy.integrate.quad.html#scipy.integrate.quad "scipy.integrate.quad")(func,Â a,Â b[,Â args,Â full\_output,Â ...]) | Compute a definite integral. |
| [`quad_vec`](generated/scipy.integrate.quad_vec.html#scipy.integrate.quad_vec "scipy.integrate.quad_vec")(f,Â a,Â b[,Â epsabs,Â epsrel,Â norm,Â ...]) | Adaptive integration of a vector-valued function. |
| [`cubature`](generated/scipy.integrate.cubature.html#scipy.integrate.cubature "scipy.integrate.cubature")(f,Â a,Â b,Â \*[,Â rule,Â rtol,Â atol,Â ...]) | Adaptive cubature of multidimensional array-valued function. |
| [`dblquad`](generated/scipy.integrate.dblquad.html#scipy.integrate.dblquad "scipy.integrate.dblquad")(func,Â a,Â b,Â gfun,Â hfun[,Â args,Â ...]) | Compute a double integral. |
| [`tplquad`](generated/scipy.integrate.tplquad.html#scipy.integrate.tplquad "scipy.integrate.tplquad")(func,Â a,Â b,Â gfun,Â hfun,Â qfun,Â rfun) | Compute a triple (definite) integral. |
| [`nquad`](generated/scipy.integrate.nquad.html#scipy.integrate.nquad "scipy.integrate.nquad")(func,Â ranges[,Â args,Â opts,Â full\_output]) | Integration over multiple variables. |
| [`tanhsinh`](generated/scipy.integrate.tanhsinh.html#scipy.integrate.tanhsinh "scipy.integrate.tanhsinh")(f,Â a,Â b,Â \*[,Â args,Â kwargs,Â log,Â ...]) | Evaluate a convergent integral numerically using tanh-sinh quadrature. |
| [`fixed_quad`](generated/scipy.integrate.fixed_quad.html#scipy.integrate.fixed_quad "scipy.integrate.fixed_quad")(func,Â a,Â b[,Â args,Â n]) | Compute a definite integral using fixed-order Gaussian quadrature. |
| [`newton_cotes`](generated/scipy.integrate.newton_cotes.html#scipy.integrate.newton_cotes "scipy.integrate.newton_cotes")(rn[,Â equal]) | Return weights and error coefficient for Newton-Cotes integration. |
| [`lebedev_rule`](generated/scipy.integrate.lebedev_rule.html#scipy.integrate.lebedev_rule "scipy.integrate.lebedev_rule")(n) | Lebedev quadrature. |
| [`qmc_quad`](generated/scipy.integrate.qmc_quad.html#scipy.integrate.qmc_quad "scipy.integrate.qmc_quad")(func,Â a,Â b,Â \*[,Â n\_estimates,Â ...]) | Compute an integral in N-dimensions using Quasi-Monte Carlo quadrature. |
| [`IntegrationWarning`](generated/scipy.integrate.IntegrationWarning.html#scipy.integrate.IntegrationWarning "scipy.integrate.IntegrationWarning") | Warning on issues during integration. |
## Integrating functions, given fixed samples[#](#integrating-functions-given-fixed-samples "Link to this heading")
|  |  |
| --- | --- |
| [`trapezoid`](generated/scipy.integrate.trapezoid.html#scipy.integrate.trapezoid "scipy.integrate.trapezoid")(y[,Â x,Â dx,Â axis]) | Integrate along the given axis using the composite trapezoidal rule. |
| [`cumulative_trapezoid`](generated/scipy.integrate.cumulative_trapezoid.html#scipy.integrate.cumulative_trapezoid "scipy.integrate.cumulative_trapezoid")(y[,Â x,Â dx,Â axis,Â initial]) | Cumulatively integrate y(x) using the composite trapezoidal rule. |
| [`simpson`](generated/scipy.integrate.simpson.html#scipy.integrate.simpson "scipy.integrate.simpson")(y[,Â x,Â dx,Â axis]) | Integrate y(x) using samples along the given axis and the composite Simpson's rule. |
| [`cumulative_simpson`](generated/scipy.integrate.cumulative_simpson.html#scipy.integrate.cumulative_simpson "scipy.integrate.cumulative_simpson")(y,Â \*[,Â x,Â dx,Â axis,Â initial]) | Cumulatively integrate y(x) using the composite Simpson's 1/3 rule. |
| [`romb`](generated/scipy.integrate.romb.html#scipy.integrate.romb "scipy.integrate.romb")(y[,Â dx,Â axis,Â show]) | Romberg integration using samples of a function. |
See also
[`scipy.special`](special.html#module-scipy.special "scipy.special") for orthogonal polynomials (special) for Gaussian
quadrature roots and weights for other weighting factors and regions.
## Summation[#](#summation "Link to this heading")
|  |  |
| --- | --- |
| [`nsum`](generated/scipy.integrate.nsum.html#scipy.integrate.nsum "scipy.integrate.nsum")(f,Â a,Â b,Â \*[,Â step,Â args,Â kwargs,Â log,Â ...]) | Evaluate a convergent finite or infinite series. |
## Solving initial value problems for ODE systems[#](#solving-initial-value-problems-for-ode-systems "Link to this heading")
The solvers are implemented as individual classes, which can be used directly
(low-level usage) or through a convenience function.
|  |  |
| --- | --- |
| [`solve_ivp`](generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp "scipy.integrate.solve_ivp")(fun,Â t\_span,Â y0[,Â method,Â t\_eval,Â ...]) | Solve an initial value problem for a system of ODEs. |
| [`RK23`](generated/scipy.integrate.RK23.html#scipy.integrate.RK23 "scipy.integrate.RK23")(fun,Â t0,Â y0,Â t\_bound[,Â max\_step,Â rtol,Â ...]) | Explicit Runge-Kutta method of order 3(2). |
| [`RK45`](generated/scipy.integrate.RK45.html#scipy.integrate.RK45 "scipy.integrate.RK45")(fun,Â t0,Â y0,Â t\_bound[,Â max\_step,Â rtol,Â ...]) | Explicit Runge-Kutta method of order 5(4). |
| [`DOP853`](generated/scipy.integrate.DOP853.html#scipy.integrate.DOP853 "scipy.integrate.DOP853")(fun,Â t0,Â y0,Â t\_bound[,Â max\_step,Â ...]) | Explicit Runge-Kutta method of order 8. |
| [`Radau`](generated/scipy.integrate.Radau.html#scipy.integrate.Radau "scipy.integrate.Radau")(fun,Â t0,Â y0,Â t\_bound[,Â max\_step,Â ...]) | Implicit Runge-Kutta method of Radau IIA family of order 5. |
| [`BDF`](generated/scipy.integrate.BDF.html#scipy.integrate.BDF "scipy.integrate.BDF")(fun,Â t0,Â y0,Â t\_bound[,Â max\_step,Â rtol,Â ...]) | Implicit method based on backward-differentiation formulas. |
| [`LSODA`](generated/scipy.integrate.LSODA.html#scipy.integrate.LSODA "scipy.integrate.LSODA")(fun,Â t0,Â y0,Â t\_bound[,Â first\_step,Â ...]) | Adams/BDF method with automatic stiffness detection and switching. |
| [`OdeSolver`](generated/scipy.integrate.OdeSolver.html#scipy.integrate.OdeSolver "scipy.integrate.OdeSolver")(fun,Â t0,Â y0,Â t\_bound,Â vectorized) | Base class for ODE solvers. |
| [`DenseOutput`](generated/scipy.integrate.DenseOutput.html#scipy.integrate.DenseOutput "scipy.integrate.DenseOutput")(t\_old,Â t) | Base class for local interpolant over step made by an ODE solver. |
| [`OdeSolution`](generated/scipy.integrate.OdeSolution.html#scipy.integrate.OdeSolution "scipy.integrate.OdeSolution")(ts,Â interpolants[,Â alt\_segment]) | Continuous ODE solution. |
### Old API[#](#old-api "Link to this heading")
These are the routines developed earlier for SciPy. They wrap older solvers
implemented in Fortran (mostly ODEPACK). While the interface to them is not
particularly convenient and certain features are missing compared to the new
API, the solvers themselves are of good quality and work fast as compiled
Fortran code. In some cases, it might be worth using this old API.
|  |  |
| --- | --- |
| [`odeint`](generated/scipy.integrate.odeint.html#scipy.integrate.odeint "scipy.integrate.odeint")(func,Â y0,Â t[,Â args,Â Dfun,Â col\_deriv,Â ...]) | Integrate a system of ordinary differential equations. |
| [`ode`](generated/scipy.integrate.ode.html#scipy.integrate.ode "scipy.integrate.ode")(f[,Â jac]) | A generic interface class to numeric integrators. |
| [`complex_ode`](generated/scipy.integrate.complex_ode.html#scipy.integrate.complex_ode "scipy.integrate.complex_ode")(f[,Â jac]) | A wrapper of ode for complex systems. |
| [`ODEintWarning`](generated/scipy.integrate.ODEintWarning.html#scipy.integrate.ODEintWarning "scipy.integrate.ODEintWarning") | Warning raised during the execution of [`odeint`](generated/scipy.integrate.odeint.html#scipy.integrate.odeint "scipy.integrate.odeint"). |
## Solving boundary value problems for ODE systems[#](#solving-boundary-value-problems-for-ode-systems "Link to this heading")
|  |  |
| --- | --- |
| [`solve_bvp`](generated/scipy.integrate.solve_bvp.html#scipy.integrate.solve_bvp "scipy.integrate.solve_bvp")(fun,Â bc,Â x,Â y[,Â p,Â S,Â fun\_jac,Â ...]) | Solve a boundary value problem for a system of ODEs. |
[previous
destroy\_convolve\_cache](generated/scipy.fftpack.convolve.destroy_convolve_cache.html "previous page")
[next
quad](generated/scipy.integrate.quad.html "next page")
On this page
* [Integrating functions, given function object](#integrating-functions-given-function-object)
* [Integrating functions, given fixed samples](#integrating-functions-given-fixed-samples)
* [Summation](#summation)
* [Solving initial value problems for ODE systems](#solving-initial-value-problems-for-ode-systems)
  + [Old API](#old-api)
* [Solving boundary value problems for ODE systems](#solving-boundary-value-problems-for-ode-systems)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/interpolate.html#module-scipy.interpolate -->
* [SciPy API](index.html)
* Interpolation (`scipy.interpolate`)
# Interpolation ([`scipy.interpolate`](#module-scipy.interpolate "scipy.interpolate"))[#](#interpolation-scipy-interpolate "Link to this heading")
Sub-package for functions and objects used in interpolation.
See the [user guide](../tutorial/interpolate.html#tutorial-interpolate) for recommendations on choosing a
routine, and other usage details.
## Univariate interpolation[#](#univariate-interpolation "Link to this heading")
|  |  |
| --- | --- |
| [`make_interp_spline`](generated/scipy.interpolate.make_interp_spline.html#scipy.interpolate.make_interp_spline "scipy.interpolate.make_interp_spline")(x,Â y[,Â k,Â t,Â bc\_type,Â ...]) | Create an interpolating B-spline with specified degree and boundary conditions. |
| [`CubicSpline`](generated/scipy.interpolate.CubicSpline.html#scipy.interpolate.CubicSpline "scipy.interpolate.CubicSpline")(x,Â y[,Â axis,Â bc\_type,Â extrapolate]) | Piecewise cubic interpolator to fit values (C2 smooth). |
| [`PchipInterpolator`](generated/scipy.interpolate.PchipInterpolator.html#scipy.interpolate.PchipInterpolator "scipy.interpolate.PchipInterpolator")(x,Â y[,Â axis,Â extrapolate]) | PCHIP shape-preserving interpolator (C1 smooth). |
| [`Akima1DInterpolator`](generated/scipy.interpolate.Akima1DInterpolator.html#scipy.interpolate.Akima1DInterpolator "scipy.interpolate.Akima1DInterpolator")(x,Â y[,Â axis,Â method,Â ...]) | Akima "visually pleasing" interpolator (C1 smooth). |
| [`FloaterHormannInterpolator`](generated/scipy.interpolate.FloaterHormannInterpolator.html#scipy.interpolate.FloaterHormannInterpolator "scipy.interpolate.FloaterHormannInterpolator")(points,Â values,Â \*) | Floater-Hormann barycentric rational interpolator (Câ smooth on real axis). |
| [`BarycentricInterpolator`](generated/scipy.interpolate.BarycentricInterpolator.html#scipy.interpolate.BarycentricInterpolator "scipy.interpolate.BarycentricInterpolator")(xi[,Â yi,Â axis,Â wi,Â ...]) | Barycentric (Lagrange with improved stability) interpolator (Câ smooth). |
| [`KroghInterpolator`](generated/scipy.interpolate.KroghInterpolator.html#scipy.interpolate.KroghInterpolator "scipy.interpolate.KroghInterpolator")(xi,Â yi[,Â axis]) | Krogh interpolator (Câ smooth). |
| [`CubicHermiteSpline`](generated/scipy.interpolate.CubicHermiteSpline.html#scipy.interpolate.CubicHermiteSpline "scipy.interpolate.CubicHermiteSpline")(x,Â y,Â dydx[,Â axis,Â ...]) | Piecewise cubic interpolator to fit values and first derivatives (C1 smooth). |
**Low-level data structures for univariate interpolation:**
|  |  |
| --- | --- |
| [`PPoly`](generated/scipy.interpolate.PPoly.html#scipy.interpolate.PPoly "scipy.interpolate.PPoly")(c,Â x[,Â extrapolate,Â axis]) | Piecewise polynomial in the power basis. |
| [`BPoly`](generated/scipy.interpolate.BPoly.html#scipy.interpolate.BPoly "scipy.interpolate.BPoly")(c,Â x[,Â extrapolate,Â axis]) | Piecewise polynomial in the Bernstein basis. |
| [`BSpline`](generated/scipy.interpolate.BSpline.html#scipy.interpolate.BSpline "scipy.interpolate.BSpline")(t,Â c,Â k[,Â extrapolate,Â axis]) | Univariate spline in the B-spline basis. |
## Multivariate interpolation[#](#multivariate-interpolation "Link to this heading")
**Unstructured data**
|  |  |
| --- | --- |
| [`LinearNDInterpolator`](generated/scipy.interpolate.LinearNDInterpolator.html#scipy.interpolate.LinearNDInterpolator "scipy.interpolate.LinearNDInterpolator")(points,Â values[,Â ...]) | Piecewise linear interpolator in N > 1 dimensions. |
| [`NearestNDInterpolator`](generated/scipy.interpolate.NearestNDInterpolator.html#scipy.interpolate.NearestNDInterpolator "scipy.interpolate.NearestNDInterpolator")(x,Â y[,Â rescale,Â ...]) | Nearest-neighbor interpolator in N > 1 dimensions. |
| [`CloughTocher2DInterpolator`](generated/scipy.interpolate.CloughTocher2DInterpolator.html#scipy.interpolate.CloughTocher2DInterpolator "scipy.interpolate.CloughTocher2DInterpolator")(points,Â values[,Â ...]) | Piecewise cubic, C1 smooth, curvature-minimizing interpolator in N=2 dimensions. |
| [`RBFInterpolator`](generated/scipy.interpolate.RBFInterpolator.html#scipy.interpolate.RBFInterpolator "scipy.interpolate.RBFInterpolator")(y,Â d[,Â neighbors,Â ...]) | Radial basis function interpolator in N â¥ 1 dimensions. |
**For data on a grid:**
|  |  |
| --- | --- |
| [`RegularGridInterpolator`](generated/scipy.interpolate.RegularGridInterpolator.html#scipy.interpolate.RegularGridInterpolator "scipy.interpolate.RegularGridInterpolator")(points,Â values[,Â ...]) | Interpolator of specified order on a rectilinear grid in N â¥ 1 dimensions. |
See also
[`scipy.ndimage.map_coordinates`](generated/scipy.ndimage.map_coordinates.html#scipy.ndimage.map_coordinates "scipy.ndimage.map_coordinates"),
[An example wrapper for map\_coordinates](../tutorial/interpolate/ND_regular_grid.html#tutorial-interpolate-cartesian-grids)
**Low-level data structures for tensor product polynomials and splines:**
|  |  |
| --- | --- |
| [`NdPPoly`](generated/scipy.interpolate.NdPPoly.html#scipy.interpolate.NdPPoly "scipy.interpolate.NdPPoly")(c,Â x[,Â extrapolate]) | Piecewise tensor product polynomial. |
| [`NdBSpline`](generated/scipy.interpolate.NdBSpline.html#scipy.interpolate.NdBSpline "scipy.interpolate.NdBSpline")(t,Â c,Â k,Â \*[,Â extrapolate]) | Tensor product spline object. |
## 1-D spline smoothing and approximation[#](#d-spline-smoothing-and-approximation "Link to this heading")
|  |  |
| --- | --- |
| [`make_lsq_spline`](generated/scipy.interpolate.make_lsq_spline.html#scipy.interpolate.make_lsq_spline "scipy.interpolate.make_lsq_spline")(x,Â y,Â t[,Â k,Â w,Â axis,Â ...]) | Create a smoothing B-spline satisfying the Least SQuares (LSQ) criterion. |
| [`make_smoothing_spline`](generated/scipy.interpolate.make_smoothing_spline.html#scipy.interpolate.make_smoothing_spline "scipy.interpolate.make_smoothing_spline")(x,Â y[,Â w,Â lam,Â axis]) | Create a smoothing B-spline satisfying the Generalized Cross Validation (GCV) criterion. |
| [`make_splrep`](generated/scipy.interpolate.make_splrep.html#scipy.interpolate.make_splrep "scipy.interpolate.make_splrep")(x,Â y,Â \*[,Â w,Â xb,Â xe,Â k,Â s,Â t,Â ...]) | Create a smoothing B-spline function with bounded error, minimizing derivative jumps. |
| [`make_splprep`](generated/scipy.interpolate.make_splprep.html#scipy.interpolate.make_splprep "scipy.interpolate.make_splprep")(x,Â \*[,Â w,Â u,Â ub,Â ue,Â k,Â s,Â t,Â ...]) | Create a smoothing parametric B-spline curve with bounded error, minimizing derivative jumps. |
| [`generate_knots`](generated/scipy.interpolate.generate_knots.html#scipy.interpolate.generate_knots "scipy.interpolate.generate_knots")(x,Â y,Â \*[,Â w,Â xb,Â xe,Â k,Â s,Â ...]) | Generate knot vectors until the Least SQuares (LSQ) criterion is satified. |
## Rational Approximation[#](#rational-approximation "Link to this heading")
|  |  |
| --- | --- |
| [`AAA`](generated/scipy.interpolate.AAA.html#scipy.interpolate.AAA "scipy.interpolate.AAA")(x,Â y,Â \*[,Â rtol,Â max\_terms,Â clean\_up,Â ...]) | AAA real or complex rational approximation. |
## Interfaces to FITPACK routines for 1D and 2D spline fitting[#](#interfaces-to-fitpack-routines-for-1d-and-2d-spline-fitting "Link to this heading")
This section lists wrappers for [FITPACK](http://www.netlib.org/dierckx/)
functionality for 1D and 2D smoothing splines. In most cases, users are better off
using higher-level routines listed in previous sections.
### 1D FITPACK splines[#](#d-fitpack-splines "Link to this heading")
This package provides two sets of functionally equivalent wrappers: object-oriented and
functional.
**Functional FITPACK interface:**
|  |  |
| --- | --- |
| [`splrep`](generated/scipy.interpolate.splrep.html#scipy.interpolate.splrep "scipy.interpolate.splrep")(x,Â y[,Â w,Â xb,Â xe,Â k,Â task,Â s,Â t,Â ...]) | Find the B-spline representation of a 1-D curve. |
| [`splprep`](generated/scipy.interpolate.splprep.html#scipy.interpolate.splprep "scipy.interpolate.splprep")(x[,Â w,Â u,Â ub,Â ue,Â k,Â task,Â s,Â t,Â ...]) | Find the B-spline representation of an N-D curve. |
| [`splev`](generated/scipy.interpolate.splev.html#scipy.interpolate.splev "scipy.interpolate.splev")(x,Â tck[,Â der,Â ext]) | Evaluate a B-spline or its derivatives. |
| [`splint`](generated/scipy.interpolate.splint.html#scipy.interpolate.splint "scipy.interpolate.splint")(a,Â b,Â tck[,Â full\_output]) | Evaluate the definite integral of a B-spline between two given points. |
| [`sproot`](generated/scipy.interpolate.sproot.html#scipy.interpolate.sproot "scipy.interpolate.sproot")(tck[,Â mest]) | Find the roots of a cubic B-spline. |
| [`spalde`](generated/scipy.interpolate.spalde.html#scipy.interpolate.spalde "scipy.interpolate.spalde")(x,Â tck) | Evaluate a B-spline and all its derivatives at one point (or set of points) up to order k (the degree of the spline), being 0 the spline itself. |
| [`splder`](generated/scipy.interpolate.splder.html#scipy.interpolate.splder "scipy.interpolate.splder")(tck[,Â n]) | Compute the spline representation of the derivative of a given spline. |
| [`splantider`](generated/scipy.interpolate.splantider.html#scipy.interpolate.splantider "scipy.interpolate.splantider")(tck[,Â n]) | Compute the spline for the antiderivative (integral) of a given spline. |
| [`insert`](generated/scipy.interpolate.insert.html#scipy.interpolate.insert "scipy.interpolate.insert")(x,Â tck[,Â m,Â per]) | Insert knots into a B-spline. |
**Object-oriented FITPACK interface:**
|  |  |
| --- | --- |
| [`UnivariateSpline`](generated/scipy.interpolate.UnivariateSpline.html#scipy.interpolate.UnivariateSpline "scipy.interpolate.UnivariateSpline")(x,Â y[,Â w,Â bbox,Â k,Â s,Â ext,Â ...]) | 1-D smoothing spline fit to a given set of data points. |
| [`InterpolatedUnivariateSpline`](generated/scipy.interpolate.InterpolatedUnivariateSpline.html#scipy.interpolate.InterpolatedUnivariateSpline "scipy.interpolate.InterpolatedUnivariateSpline")(x,Â y[,Â w,Â ...]) | 1-D interpolating spline for a given set of data points. |
| [`LSQUnivariateSpline`](generated/scipy.interpolate.LSQUnivariateSpline.html#scipy.interpolate.LSQUnivariateSpline "scipy.interpolate.LSQUnivariateSpline")(x,Â y,Â t[,Â w,Â bbox,Â k,Â ...]) | 1-D spline with explicit internal knots. |
### 2D FITPACK splines[#](#id1 "Link to this heading")
**For data on a grid:**
|  |  |
| --- | --- |
| [`RectBivariateSpline`](generated/scipy.interpolate.RectBivariateSpline.html#scipy.interpolate.RectBivariateSpline "scipy.interpolate.RectBivariateSpline")(x,Â y,Â z[,Â bbox,Â kx,Â ky,Â ...]) | Bivariate spline approximation over a rectangular mesh. |
| [`RectSphereBivariateSpline`](generated/scipy.interpolate.RectSphereBivariateSpline.html#scipy.interpolate.RectSphereBivariateSpline "scipy.interpolate.RectSphereBivariateSpline")(u,Â v,Â r[,Â s,Â ...]) | Bivariate spline approximation over a rectangular mesh on a sphere. |
**For unstructured data (OOP interface):**
|  |  |
| --- | --- |
| [`BivariateSpline`](generated/scipy.interpolate.BivariateSpline.html#scipy.interpolate.BivariateSpline "scipy.interpolate.BivariateSpline")() | Base class for bivariate splines. |
| [`SmoothBivariateSpline`](generated/scipy.interpolate.SmoothBivariateSpline.html#scipy.interpolate.SmoothBivariateSpline "scipy.interpolate.SmoothBivariateSpline")(x,Â y,Â z[,Â w,Â bbox,Â ...]) | Smooth bivariate spline approximation. |
| [`SmoothSphereBivariateSpline`](generated/scipy.interpolate.SmoothSphereBivariateSpline.html#scipy.interpolate.SmoothSphereBivariateSpline "scipy.interpolate.SmoothSphereBivariateSpline")(theta,Â phi,Â r[,Â ...]) | Smooth bivariate spline approximation in spherical coordinates. |
| [`LSQBivariateSpline`](generated/scipy.interpolate.LSQBivariateSpline.html#scipy.interpolate.LSQBivariateSpline "scipy.interpolate.LSQBivariateSpline")(x,Â y,Â z,Â tx,Â ty[,Â w,Â ...]) | Weighted least-squares bivariate spline approximation. |
| [`LSQSphereBivariateSpline`](generated/scipy.interpolate.LSQSphereBivariateSpline.html#scipy.interpolate.LSQSphereBivariateSpline "scipy.interpolate.LSQSphereBivariateSpline")(theta,Â phi,Â r,Â tt,Â tp) | Weighted least-squares bivariate spline approximation in spherical coordinates. |
**For unstructured data (functional interface):**
|  |  |
| --- | --- |
| [`bisplrep`](generated/scipy.interpolate.bisplrep.html#scipy.interpolate.bisplrep "scipy.interpolate.bisplrep")(x,Â y,Â z[,Â w,Â xb,Â xe,Â yb,Â ye,Â kx,Â ...]) | Find a bivariate B-spline representation of a surface. |
| [`bisplev`](generated/scipy.interpolate.bisplev.html#scipy.interpolate.bisplev "scipy.interpolate.bisplev")(x,Â y,Â tck[,Â dx,Â dy]) | Evaluate a bivariate B-spline and its derivatives. |
## Additional tools[#](#additional-tools "Link to this heading")
|  |  |
| --- | --- |
| [`lagrange`](generated/scipy.interpolate.lagrange.html#scipy.interpolate.lagrange "scipy.interpolate.lagrange")(x,Â w) | Return a Lagrange interpolating polynomial. |
| [`approximate_taylor_polynomial`](generated/scipy.interpolate.approximate_taylor_polynomial.html#scipy.interpolate.approximate_taylor_polynomial "scipy.interpolate.approximate_taylor_polynomial")(f,Â x,Â degree,Â ...) | Estimate the Taylor polynomial of f at x by polynomial fitting. |
| [`pade`](generated/scipy.interpolate.pade.html#scipy.interpolate.pade "scipy.interpolate.pade")(an,Â m[,Â n]) | Return Pade approximation to a polynomial as the ratio of two polynomials. |
| [`interpn`](generated/scipy.interpolate.interpn.html#scipy.interpolate.interpn "scipy.interpolate.interpn")(points,Â values,Â xi[,Â method,Â ...]) | Multidimensional interpolation on regular or rectilinear grids. |
| [`griddata`](generated/scipy.interpolate.griddata.html#scipy.interpolate.griddata "scipy.interpolate.griddata")(points,Â values,Â xi[,Â method,Â ...]) | Convenience function for interpolating unstructured data in multiple dimensions. |
| [`barycentric_interpolate`](generated/scipy.interpolate.barycentric_interpolate.html#scipy.interpolate.barycentric_interpolate "scipy.interpolate.barycentric_interpolate")(xi,Â yi,Â x[,Â axis,Â ...]) | Convenience function for barycentric interpolation. |
| [`krogh_interpolate`](generated/scipy.interpolate.krogh_interpolate.html#scipy.interpolate.krogh_interpolate "scipy.interpolate.krogh_interpolate")(xi,Â yi,Â x[,Â der,Â axis]) | Convenience function for Krogh interpolation. |
| [`pchip_interpolate`](generated/scipy.interpolate.pchip_interpolate.html#scipy.interpolate.pchip_interpolate "scipy.interpolate.pchip_interpolate")(xi,Â yi,Â x[,Â der,Â axis]) | Convenience function for pchip interpolation. |
| [`Rbf`](generated/scipy.interpolate.Rbf.html#scipy.interpolate.Rbf "scipy.interpolate.Rbf")(\\*args,Â \\*\\*kwargs) | Class for radial basis function interpolation of functions from N-D scattered data to an M-D domain (legacy). |
| [`interp1d`](generated/scipy.interpolate.interp1d.html#scipy.interpolate.interp1d "scipy.interpolate.interp1d")(x,Â y[,Â kind,Â axis,Â copy,Â ...]) | Interpolate a 1-D function (legacy). |
| [`interp2d`](generated/scipy.interpolate.interp2d.html#scipy.interpolate.interp2d "scipy.interpolate.interp2d")(x,Â y,Â z[,Â kind,Â copy,Â ...]) | Class for 2D interpolation (deprecated and removed). |
See also
[`scipy.ndimage.map_coordinates`](generated/scipy.ndimage.map_coordinates.html#scipy.ndimage.map_coordinates "scipy.ndimage.map_coordinates"),
[`scipy.ndimage.spline_filter`](generated/scipy.ndimage.spline_filter.html#scipy.ndimage.spline_filter "scipy.ndimage.spline_filter"),
[previous
solve\_bvp](generated/scipy.integrate.solve_bvp.html "previous page")
[next
make\_interp\_spline](generated/scipy.interpolate.make_interp_spline.html "next page")
On this page
* [Univariate interpolation](#univariate-interpolation)
* [Multivariate interpolation](#multivariate-interpolation)
* [1-D spline smoothing and approximation](#d-spline-smoothing-and-approximation)
* [Rational Approximation](#rational-approximation)
* [Interfaces to FITPACK routines for 1D and 2D spline fitting](#interfaces-to-fitpack-routines-for-1d-and-2d-spline-fitting)
  + [1D FITPACK splines](#d-fitpack-splines)
  + [2D FITPACK splines](#id1)
* [Additional tools](#additional-tools)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/io.html#module-scipy.io -->
* [SciPy API](index.html)
* Input and output (`scipy.io`)
# Input and output ([`scipy.io`](#module-scipy.io "scipy.io"))[#](#input-and-output-scipy-io "Link to this heading")
SciPy has many modules, classes, and functions available to read data
from and write data to a variety of file formats.
See also
[NumPy IO routines](https://www.numpy.org/devdocs/reference/routines.io.html)
## MATLABÂ® files[#](#matlab-files "Link to this heading")
|  |  |
| --- | --- |
| [`loadmat`](generated/scipy.io.loadmat.html#scipy.io.loadmat "scipy.io.loadmat")(file\_name[,Â mdict,Â appendmat,Â spmatrix]) | Load MATLAB file. |
| [`savemat`](generated/scipy.io.savemat.html#scipy.io.savemat "scipy.io.savemat")(file\_name,Â mdict[,Â appendmat,Â ...]) | Save a dictionary of names and arrays into a MATLAB-style .mat file. |
| [`whosmat`](generated/scipy.io.whosmat.html#scipy.io.whosmat "scipy.io.whosmat")(file\_name[,Â appendmat]) | List variables inside a MATLAB file. |
For low-level MATLAB reading and writing utilities, see [`scipy.io.matlab`](io.matlab.html#module-scipy.io.matlab "scipy.io.matlab").
## IDLÂ® files[#](#idl-files "Link to this heading")
|  |  |
| --- | --- |
| [`readsav`](generated/scipy.io.readsav.html#scipy.io.readsav "scipy.io.readsav")(file\_name[,Â idict,Â python\_dict,Â ...]) | Read an IDL .sav file. |
## Matrix Market files[#](#matrix-market-files "Link to this heading")
|  |  |
| --- | --- |
| [`mminfo`](generated/scipy.io.mminfo.html#scipy.io.mminfo "scipy.io.mminfo")(source) | Return size and storage parameters from Matrix Market file-like 'source'. |
| [`mmread`](generated/scipy.io.mmread.html#scipy.io.mmread "scipy.io.mmread")(source,Â \*[,Â spmatrix]) | Reads the contents of a Matrix Market file-like 'source' into a matrix. |
| [`mmwrite`](generated/scipy.io.mmwrite.html#scipy.io.mmwrite "scipy.io.mmwrite")(target,Â a[,Â comment,Â field,Â ...]) | Writes the sparse or dense array *a* to Matrix Market file-like *target*. |
## Unformatted Fortran files[#](#unformatted-fortran-files "Link to this heading")
|  |  |
| --- | --- |
| [`FortranFile`](generated/scipy.io.FortranFile.html#scipy.io.FortranFile "scipy.io.FortranFile")(filename[,Â mode,Â header\_dtype]) | A file object for unformatted sequential files from Fortran code. |
| [`FortranEOFError`](generated/scipy.io.FortranEOFError.html#scipy.io.FortranEOFError "scipy.io.FortranEOFError") | Indicates that the file ended properly. |
| [`FortranFormattingError`](generated/scipy.io.FortranFormattingError.html#scipy.io.FortranFormattingError "scipy.io.FortranFormattingError") | Indicates that the file ended mid-record. |
## Netcdf[#](#netcdf "Link to this heading")
|  |  |
| --- | --- |
| [`netcdf_file`](generated/scipy.io.netcdf_file.html#scipy.io.netcdf_file "scipy.io.netcdf_file")(filename[,Â mode,Â mmap,Â version,Â ...]) | A file object for NetCDF data. |
| [`netcdf_variable`](generated/scipy.io.netcdf_variable.html#scipy.io.netcdf_variable "scipy.io.netcdf_variable")(data,Â typecode,Â size,Â shape,Â ...) | A data object for netcdf files. |
## Harwell-Boeing files[#](#harwell-boeing-files "Link to this heading")
|  |  |
| --- | --- |
| [`hb_read`](generated/scipy.io.hb_read.html#scipy.io.hb_read "scipy.io.hb_read")(path\_or\_open\_file,Â \*[,Â spmatrix]) | Read HB-format file. |
| [`hb_write`](generated/scipy.io.hb_write.html#scipy.io.hb_write "scipy.io.hb_write")(path\_or\_open\_file,Â m[,Â hb\_info]) | Write HB-format file. |
## Wav sound files ([`scipy.io.wavfile`](#module-scipy.io.wavfile "scipy.io.wavfile"))[#](#module-scipy.io.wavfile "Link to this heading")
|  |  |
| --- | --- |
| [`read`](generated/scipy.io.wavfile.read.html#scipy.io.wavfile.read "scipy.io.wavfile.read")(filename[,Â mmap]) | Open a WAV file. |
| [`write`](generated/scipy.io.wavfile.write.html#scipy.io.wavfile.write "scipy.io.wavfile.write")(filename,Â rate,Â data) | Write a NumPy array as a WAV file. |
| [`WavFileWarning`](generated/scipy.io.wavfile.WavFileWarning.html#scipy.io.wavfile.WavFileWarning "scipy.io.wavfile.WavFileWarning") | Warning for WAV files with format issues that can still be read. |
## Arff files ([`scipy.io.arff`](#module-scipy.io.arff "scipy.io.arff"))[#](#module-scipy.io.arff "Link to this heading")
|  |  |
| --- | --- |
| [`loadarff`](generated/scipy.io.arff.loadarff.html#scipy.io.arff.loadarff "scipy.io.arff.loadarff")(f) | Read an arff file. |
| [`MetaData`](generated/scipy.io.arff.MetaData.html#scipy.io.arff.MetaData "scipy.io.arff.MetaData")(rel,Â attr) | Small container to keep useful information on an ARFF dataset. |
| [`ArffError`](generated/scipy.io.arff.ArffError.html#scipy.io.arff.ArffError "scipy.io.arff.ArffError") | Base exception for errors when reading ARFF files. |
| [`ParseArffError`](generated/scipy.io.arff.ParseArffError.html#scipy.io.arff.ParseArffError "scipy.io.arff.ParseArffError") | Exception for syntax and parsing errors in ARFF files. |
[previous
interp2d](generated/scipy.interpolate.interp2d.html "previous page")
[next
MATLABÂ® file utilities (`scipy.io.matlab`)](io.matlab.html "next page")
On this page
* [MATLABÂ® files](#matlab-files)
* [IDLÂ® files](#idl-files)
* [Matrix Market files](#matrix-market-files)
* [Unformatted Fortran files](#unformatted-fortran-files)
* [Netcdf](#netcdf)
* [Harwell-Boeing files](#harwell-boeing-files)
* [Wav sound files (`scipy.io.wavfile`)](#module-scipy.io.wavfile)
* [Arff files (`scipy.io.arff`)](#module-scipy.io.arff)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/io.html#module-scipy.io.arff -->
* [SciPy API](index.html)
* Input and output (`scipy.io`)
# Input and output ([`scipy.io`](#module-scipy.io "scipy.io"))[#](#input-and-output-scipy-io "Link to this heading")
SciPy has many modules, classes, and functions available to read data
from and write data to a variety of file formats.
See also
[NumPy IO routines](https://www.numpy.org/devdocs/reference/routines.io.html)
## MATLABÂ® files[#](#matlab-files "Link to this heading")
|  |  |
| --- | --- |
| [`loadmat`](generated/scipy.io.loadmat.html#scipy.io.loadmat "scipy.io.loadmat")(file\_name[,Â mdict,Â appendmat,Â spmatrix]) | Load MATLAB file. |
| [`savemat`](generated/scipy.io.savemat.html#scipy.io.savemat "scipy.io.savemat")(file\_name,Â mdict[,Â appendmat,Â ...]) | Save a dictionary of names and arrays into a MATLAB-style .mat file. |
| [`whosmat`](generated/scipy.io.whosmat.html#scipy.io.whosmat "scipy.io.whosmat")(file\_name[,Â appendmat]) | List variables inside a MATLAB file. |
For low-level MATLAB reading and writing utilities, see [`scipy.io.matlab`](io.matlab.html#module-scipy.io.matlab "scipy.io.matlab").
## IDLÂ® files[#](#idl-files "Link to this heading")
|  |  |
| --- | --- |
| [`readsav`](generated/scipy.io.readsav.html#scipy.io.readsav "scipy.io.readsav")(file\_name[,Â idict,Â python\_dict,Â ...]) | Read an IDL .sav file. |
## Matrix Market files[#](#matrix-market-files "Link to this heading")
|  |  |
| --- | --- |
| [`mminfo`](generated/scipy.io.mminfo.html#scipy.io.mminfo "scipy.io.mminfo")(source) | Return size and storage parameters from Matrix Market file-like 'source'. |
| [`mmread`](generated/scipy.io.mmread.html#scipy.io.mmread "scipy.io.mmread")(source,Â \*[,Â spmatrix]) | Reads the contents of a Matrix Market file-like 'source' into a matrix. |
| [`mmwrite`](generated/scipy.io.mmwrite.html#scipy.io.mmwrite "scipy.io.mmwrite")(target,Â a[,Â comment,Â field,Â ...]) | Writes the sparse or dense array *a* to Matrix Market file-like *target*. |
## Unformatted Fortran files[#](#unformatted-fortran-files "Link to this heading")
|  |  |
| --- | --- |
| [`FortranFile`](generated/scipy.io.FortranFile.html#scipy.io.FortranFile "scipy.io.FortranFile")(filename[,Â mode,Â header\_dtype]) | A file object for unformatted sequential files from Fortran code. |
| [`FortranEOFError`](generated/scipy.io.FortranEOFError.html#scipy.io.FortranEOFError "scipy.io.FortranEOFError") | Indicates that the file ended properly. |
| [`FortranFormattingError`](generated/scipy.io.FortranFormattingError.html#scipy.io.FortranFormattingError "scipy.io.FortranFormattingError") | Indicates that the file ended mid-record. |
## Netcdf[#](#netcdf "Link to this heading")
|  |  |
| --- | --- |
| [`netcdf_file`](generated/scipy.io.netcdf_file.html#scipy.io.netcdf_file "scipy.io.netcdf_file")(filename[,Â mode,Â mmap,Â version,Â ...]) | A file object for NetCDF data. |
| [`netcdf_variable`](generated/scipy.io.netcdf_variable.html#scipy.io.netcdf_variable "scipy.io.netcdf_variable")(data,Â typecode,Â size,Â shape,Â ...) | A data object for netcdf files. |
## Harwell-Boeing files[#](#harwell-boeing-files "Link to this heading")
|  |  |
| --- | --- |
| [`hb_read`](generated/scipy.io.hb_read.html#scipy.io.hb_read "scipy.io.hb_read")(path\_or\_open\_file,Â \*[,Â spmatrix]) | Read HB-format file. |
| [`hb_write`](generated/scipy.io.hb_write.html#scipy.io.hb_write "scipy.io.hb_write")(path\_or\_open\_file,Â m[,Â hb\_info]) | Write HB-format file. |
## Wav sound files ([`scipy.io.wavfile`](#module-scipy.io.wavfile "scipy.io.wavfile"))[#](#module-scipy.io.wavfile "Link to this heading")
|  |  |
| --- | --- |
| [`read`](generated/scipy.io.wavfile.read.html#scipy.io.wavfile.read "scipy.io.wavfile.read")(filename[,Â mmap]) | Open a WAV file. |
| [`write`](generated/scipy.io.wavfile.write.html#scipy.io.wavfile.write "scipy.io.wavfile.write")(filename,Â rate,Â data) | Write a NumPy array as a WAV file. |
| [`WavFileWarning`](generated/scipy.io.wavfile.WavFileWarning.html#scipy.io.wavfile.WavFileWarning "scipy.io.wavfile.WavFileWarning") | Warning for WAV files with format issues that can still be read. |
## Arff files ([`scipy.io.arff`](#module-scipy.io.arff "scipy.io.arff"))[#](#module-scipy.io.arff "Link to this heading")
|  |  |
| --- | --- |
| [`loadarff`](generated/scipy.io.arff.loadarff.html#scipy.io.arff.loadarff "scipy.io.arff.loadarff")(f) | Read an arff file. |
| [`MetaData`](generated/scipy.io.arff.MetaData.html#scipy.io.arff.MetaData "scipy.io.arff.MetaData")(rel,Â attr) | Small container to keep useful information on an ARFF dataset. |
| [`ArffError`](generated/scipy.io.arff.ArffError.html#scipy.io.arff.ArffError "scipy.io.arff.ArffError") | Base exception for errors when reading ARFF files. |
| [`ParseArffError`](generated/scipy.io.arff.ParseArffError.html#scipy.io.arff.ParseArffError "scipy.io.arff.ParseArffError") | Exception for syntax and parsing errors in ARFF files. |
[previous
interp2d](generated/scipy.interpolate.interp2d.html "previous page")
[next
MATLABÂ® file utilities (`scipy.io.matlab`)](io.matlab.html "next page")
On this page
* [MATLABÂ® files](#matlab-files)
* [IDLÂ® files](#idl-files)
* [Matrix Market files](#matrix-market-files)
* [Unformatted Fortran files](#unformatted-fortran-files)
* [Netcdf](#netcdf)
* [Harwell-Boeing files](#harwell-boeing-files)
* [Wav sound files (`scipy.io.wavfile`)](#module-scipy.io.wavfile)
* [Arff files (`scipy.io.arff`)](#module-scipy.io.arff)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/io.matlab.html#module-scipy.io.matlab -->
* [SciPy API](index.html)
* [Input and output (`scipy.io`)](io.html)
* MATLABÂ® file utilities (`scipy.io.matlab`)
# MATLABÂ® file utilities ([`scipy.io.matlab`](#module-scipy.io.matlab "scipy.io.matlab"))[#](#matlab-file-utilities-scipy-io-matlab "Link to this heading")
This submodule is meant to provide lower-level file utilities related to reading
and writing MATLAB files.
|  |  |
| --- | --- |
| [`matfile_version`](generated/scipy.io.matlab.matfile_version.html#scipy.io.matlab.matfile_version "scipy.io.matlab.matfile_version")(file\_name,Â \*[,Â appendmat]) | Return major, minor tuple depending on apparent mat file type. |
| [`MatReadError`](generated/scipy.io.matlab.MatReadError.html#scipy.io.matlab.MatReadError "scipy.io.matlab.MatReadError") | Exception indicating a read issue. |
| [`MatReadWarning`](generated/scipy.io.matlab.MatReadWarning.html#scipy.io.matlab.MatReadWarning "scipy.io.matlab.MatReadWarning") | Warning class for read issues. |
| [`MatWriteError`](generated/scipy.io.matlab.MatWriteError.html#scipy.io.matlab.MatWriteError "scipy.io.matlab.MatWriteError") | Exception indicating a write issue. |
| [`MatWriteWarning`](generated/scipy.io.matlab.MatWriteWarning.html#scipy.io.matlab.MatWriteWarning "scipy.io.matlab.MatWriteWarning") | Warning class for write issues. |
| [`mat_struct`](generated/scipy.io.matlab.mat_struct.html#scipy.io.matlab.mat_struct "scipy.io.matlab.mat_struct")() | Placeholder for holding read data from structs. |
| [`varmats_from_mat`](generated/scipy.io.matlab.varmats_from_mat.html#scipy.io.matlab.varmats_from_mat "scipy.io.matlab.varmats_from_mat")(file\_obj) | Pull variables out of mat 5 file as a sequence of mat file objects. |
|  |  |
| --- | --- |
| [`MatlabObject`](generated/scipy.io.matlab.MatlabObject.html#scipy.io.matlab.MatlabObject "scipy.io.matlab.MatlabObject") | Subclass of ndarray to signal this is a matlab object. |
| [`MatlabOpaque`](generated/scipy.io.matlab.MatlabOpaque.html#scipy.io.matlab.MatlabOpaque "scipy.io.matlab.MatlabOpaque") | Subclass for a MATLAB opaque matrix. |
| [`MatlabFunction`](generated/scipy.io.matlab.MatlabFunction.html#scipy.io.matlab.MatlabFunction "scipy.io.matlab.MatlabFunction") | Subclass for a MATLAB function. |
The following utilities that live in the [`scipy.io`](io.html#module-scipy.io "scipy.io")
namespace also exist in this namespace:
|  |  |
| --- | --- |
| [`loadmat`](generated/scipy.io.matlab.loadmat.html#scipy.io.matlab.loadmat "scipy.io.matlab.loadmat")(file\_name[,Â mdict,Â appendmat,Â spmatrix]) | Load MATLAB file. |
| [`savemat`](generated/scipy.io.matlab.savemat.html#scipy.io.matlab.savemat "scipy.io.matlab.savemat")(file\_name,Â mdict[,Â appendmat,Â ...]) | Save a dictionary of names and arrays into a MATLAB-style .mat file. |
| [`whosmat`](generated/scipy.io.matlab.whosmat.html#scipy.io.matlab.whosmat "scipy.io.matlab.whosmat")(file\_name[,Â appendmat]) | List variables inside a MATLAB file. |
## Notes[#](#notes "Link to this heading")
MATLABÂ® is a registered trademark of The MathWorks, Inc., 3 Apple Hill
Drive, Natick, MA 01760-2098, USA.
[previous
Input and output (`scipy.io`)](io.html "previous page")
[next
matfile\_version](generated/scipy.io.matlab.matfile_version.html "next page")
On this page
* [Notes](#notes)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/io.html#module-scipy.io.wavfile -->
* [SciPy API](index.html)
* Input and output (`scipy.io`)
# Input and output ([`scipy.io`](#module-scipy.io "scipy.io"))[#](#input-and-output-scipy-io "Link to this heading")
SciPy has many modules, classes, and functions available to read data
from and write data to a variety of file formats.
See also
[NumPy IO routines](https://www.numpy.org/devdocs/reference/routines.io.html)
## MATLABÂ® files[#](#matlab-files "Link to this heading")
|  |  |
| --- | --- |
| [`loadmat`](generated/scipy.io.loadmat.html#scipy.io.loadmat "scipy.io.loadmat")(file\_name[,Â mdict,Â appendmat,Â spmatrix]) | Load MATLAB file. |
| [`savemat`](generated/scipy.io.savemat.html#scipy.io.savemat "scipy.io.savemat")(file\_name,Â mdict[,Â appendmat,Â ...]) | Save a dictionary of names and arrays into a MATLAB-style .mat file. |
| [`whosmat`](generated/scipy.io.whosmat.html#scipy.io.whosmat "scipy.io.whosmat")(file\_name[,Â appendmat]) | List variables inside a MATLAB file. |
For low-level MATLAB reading and writing utilities, see [`scipy.io.matlab`](io.matlab.html#module-scipy.io.matlab "scipy.io.matlab").
## IDLÂ® files[#](#idl-files "Link to this heading")
|  |  |
| --- | --- |
| [`readsav`](generated/scipy.io.readsav.html#scipy.io.readsav "scipy.io.readsav")(file\_name[,Â idict,Â python\_dict,Â ...]) | Read an IDL .sav file. |
## Matrix Market files[#](#matrix-market-files "Link to this heading")
|  |  |
| --- | --- |
| [`mminfo`](generated/scipy.io.mminfo.html#scipy.io.mminfo "scipy.io.mminfo")(source) | Return size and storage parameters from Matrix Market file-like 'source'. |
| [`mmread`](generated/scipy.io.mmread.html#scipy.io.mmread "scipy.io.mmread")(source,Â \*[,Â spmatrix]) | Reads the contents of a Matrix Market file-like 'source' into a matrix. |
| [`mmwrite`](generated/scipy.io.mmwrite.html#scipy.io.mmwrite "scipy.io.mmwrite")(target,Â a[,Â comment,Â field,Â ...]) | Writes the sparse or dense array *a* to Matrix Market file-like *target*. |
## Unformatted Fortran files[#](#unformatted-fortran-files "Link to this heading")
|  |  |
| --- | --- |
| [`FortranFile`](generated/scipy.io.FortranFile.html#scipy.io.FortranFile "scipy.io.FortranFile")(filename[,Â mode,Â header\_dtype]) | A file object for unformatted sequential files from Fortran code. |
| [`FortranEOFError`](generated/scipy.io.FortranEOFError.html#scipy.io.FortranEOFError "scipy.io.FortranEOFError") | Indicates that the file ended properly. |
| [`FortranFormattingError`](generated/scipy.io.FortranFormattingError.html#scipy.io.FortranFormattingError "scipy.io.FortranFormattingError") | Indicates that the file ended mid-record. |
## Netcdf[#](#netcdf "Link to this heading")
|  |  |
| --- | --- |
| [`netcdf_file`](generated/scipy.io.netcdf_file.html#scipy.io.netcdf_file "scipy.io.netcdf_file")(filename[,Â mode,Â mmap,Â version,Â ...]) | A file object for NetCDF data. |
| [`netcdf_variable`](generated/scipy.io.netcdf_variable.html#scipy.io.netcdf_variable "scipy.io.netcdf_variable")(data,Â typecode,Â size,Â shape,Â ...) | A data object for netcdf files. |
## Harwell-Boeing files[#](#harwell-boeing-files "Link to this heading")
|  |  |
| --- | --- |
| [`hb_read`](generated/scipy.io.hb_read.html#scipy.io.hb_read "scipy.io.hb_read")(path\_or\_open\_file,Â \*[,Â spmatrix]) | Read HB-format file. |
| [`hb_write`](generated/scipy.io.hb_write.html#scipy.io.hb_write "scipy.io.hb_write")(path\_or\_open\_file,Â m[,Â hb\_info]) | Write HB-format file. |
## Wav sound files ([`scipy.io.wavfile`](#module-scipy.io.wavfile "scipy.io.wavfile"))[#](#module-scipy.io.wavfile "Link to this heading")
|  |  |
| --- | --- |
| [`read`](generated/scipy.io.wavfile.read.html#scipy.io.wavfile.read "scipy.io.wavfile.read")(filename[,Â mmap]) | Open a WAV file. |
| [`write`](generated/scipy.io.wavfile.write.html#scipy.io.wavfile.write "scipy.io.wavfile.write")(filename,Â rate,Â data) | Write a NumPy array as a WAV file. |
| [`WavFileWarning`](generated/scipy.io.wavfile.WavFileWarning.html#scipy.io.wavfile.WavFileWarning "scipy.io.wavfile.WavFileWarning") | Warning for WAV files with format issues that can still be read. |
## Arff files ([`scipy.io.arff`](#module-scipy.io.arff "scipy.io.arff"))[#](#module-scipy.io.arff "Link to this heading")
|  |  |
| --- | --- |
| [`loadarff`](generated/scipy.io.arff.loadarff.html#scipy.io.arff.loadarff "scipy.io.arff.loadarff")(f) | Read an arff file. |
| [`MetaData`](generated/scipy.io.arff.MetaData.html#scipy.io.arff.MetaData "scipy.io.arff.MetaData")(rel,Â attr) | Small container to keep useful information on an ARFF dataset. |
| [`ArffError`](generated/scipy.io.arff.ArffError.html#scipy.io.arff.ArffError "scipy.io.arff.ArffError") | Base exception for errors when reading ARFF files. |
| [`ParseArffError`](generated/scipy.io.arff.ParseArffError.html#scipy.io.arff.ParseArffError "scipy.io.arff.ParseArffError") | Exception for syntax and parsing errors in ARFF files. |
[previous
interp2d](generated/scipy.interpolate.interp2d.html "previous page")
[next
MATLABÂ® file utilities (`scipy.io.matlab`)](io.matlab.html "next page")
On this page
* [MATLABÂ® files](#matlab-files)
* [IDLÂ® files](#idl-files)
* [Matrix Market files](#matrix-market-files)
* [Unformatted Fortran files](#unformatted-fortran-files)
* [Netcdf](#netcdf)
* [Harwell-Boeing files](#harwell-boeing-files)
* [Wav sound files (`scipy.io.wavfile`)](#module-scipy.io.wavfile)
* [Arff files (`scipy.io.arff`)](#module-scipy.io.arff)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/linalg.html#module-scipy.linalg -->
* [SciPy API](index.html)
* Linear algebra (`scipy.linalg`)
# Linear algebra ([`scipy.linalg`](#module-scipy.linalg "scipy.linalg"))[#](#linear-algebra-scipy-linalg "Link to this heading")
Linear algebra functions.
See also
[numpy.linalg](https://www.numpy.org/devdocs/reference/routines.linalg.html)
for more linear algebra functions. Note that identically named
functions from [`scipy.linalg`](#module-scipy.linalg "scipy.linalg") may offer more or slightly differing
functionality.
## Basics[#](#basics "Link to this heading")
|  |  |
| --- | --- |
| [`inv`](generated/scipy.linalg.inv.html#scipy.linalg.inv "scipy.linalg.inv")(a[,Â overwrite\_a,Â check\_finite,Â ...]) | Compute the inverse of a matrix. |
| [`solve`](generated/scipy.linalg.solve.html#scipy.linalg.solve "scipy.linalg.solve")(a,Â b[,Â lower,Â overwrite\_a,Â ...]) | Solve the equation `a @ x = b` for `x`, where *a* is a square matrix. |
| [`solve_banded`](generated/scipy.linalg.solve_banded.html#scipy.linalg.solve_banded "scipy.linalg.solve_banded")(l\_and\_u,Â ab,Â b[,Â overwrite\_ab,Â ...]) | Solve the equation `a @ x = b` for `x`, where `a` is the banded matrix defined by *ab*. |
| [`solveh_banded`](generated/scipy.linalg.solveh_banded.html#scipy.linalg.solveh_banded "scipy.linalg.solveh_banded")(ab,Â b[,Â overwrite\_ab,Â ...]) | Solve the equation `a @ x = b` for `x`, where `a` is the Hermitian positive-definite banded matrix defined by *ab*. |
| [`solve_circulant`](generated/scipy.linalg.solve_circulant.html#scipy.linalg.solve_circulant "scipy.linalg.solve_circulant")(c,Â b[,Â singular,Â tol,Â ...]) | Solve the equation `C @ x = b` for `x`, where `C` is a circulant matrix defined by *c*. |
| [`solve_triangular`](generated/scipy.linalg.solve_triangular.html#scipy.linalg.solve_triangular "scipy.linalg.solve_triangular")(a,Â b[,Â trans,Â lower,Â ...]) | Solve the equation `a @ x = b` for `x`, where *a* is a triangular matrix. |
| [`solve_toeplitz`](generated/scipy.linalg.solve_toeplitz.html#scipy.linalg.solve_toeplitz "scipy.linalg.solve_toeplitz")(c\_or\_cr,Â b[,Â check\_finite]) | Solve the equation `T @ x = b` for `x`, where `T` is a Toeplitz matrix defined by *c\_or\_cr*. |
| [`matmul_toeplitz`](generated/scipy.linalg.matmul_toeplitz.html#scipy.linalg.matmul_toeplitz "scipy.linalg.matmul_toeplitz")(c\_or\_cr,Â x[,Â check\_finite,Â ...]) | Efficient Toeplitz Matrix-Matrix Multiplication using FFT. |
| [`det`](generated/scipy.linalg.det.html#scipy.linalg.det "scipy.linalg.det")(a[,Â overwrite\_a,Â check\_finite]) | Compute the determinant of a matrix. |
| [`norm`](generated/scipy.linalg.norm.html#scipy.linalg.norm "scipy.linalg.norm")(a[,Â ord,Â axis,Â keepdims,Â check\_finite]) | Matrix or vector norm. |
| [`lstsq`](generated/scipy.linalg.lstsq.html#scipy.linalg.lstsq "scipy.linalg.lstsq")(a,Â b[,Â cond,Â overwrite\_a,Â ...]) | Compute least-squares solution to the equation `a @ x = b`. |
| [`pinv`](generated/scipy.linalg.pinv.html#scipy.linalg.pinv "scipy.linalg.pinv")(a,Â \*[,Â atol,Â rtol,Â return\_rank,Â ...]) | Compute the (Moore-Penrose) pseudo-inverse of a matrix. |
| [`pinvh`](generated/scipy.linalg.pinvh.html#scipy.linalg.pinvh "scipy.linalg.pinvh")(a[,Â atol,Â rtol,Â lower,Â return\_rank,Â ...]) | Compute the (Moore-Penrose) pseudo-inverse of a Hermitian matrix. |
| [`khatri_rao`](generated/scipy.linalg.khatri_rao.html#scipy.linalg.khatri_rao "scipy.linalg.khatri_rao")(a,Â b) | Khatri-Rao product of two matrices. |
| [`orthogonal_procrustes`](generated/scipy.linalg.orthogonal_procrustes.html#scipy.linalg.orthogonal_procrustes "scipy.linalg.orthogonal_procrustes")(A,Â B[,Â check\_finite]) | Compute the matrix solution of the orthogonal (or unitary) Procrustes problem. |
| [`matrix_balance`](generated/scipy.linalg.matrix_balance.html#scipy.linalg.matrix_balance "scipy.linalg.matrix_balance")(A[,Â permute,Â scale,Â ...]) | Compute a diagonal similarity transformation for row/column balancing. |
| [`subspace_angles`](generated/scipy.linalg.subspace_angles.html#scipy.linalg.subspace_angles "scipy.linalg.subspace_angles")(A,Â B) | Compute the subspace angles between two matrices. |
| [`bandwidth`](generated/scipy.linalg.bandwidth.html#scipy.linalg.bandwidth "scipy.linalg.bandwidth")(a) | Return the lower and upper bandwidth of a numeric array. |
| [`issymmetric`](generated/scipy.linalg.issymmetric.html#scipy.linalg.issymmetric "scipy.linalg.issymmetric")(a[,Â atol,Â rtol]) | Check if a square 2D array is symmetric. |
| [`ishermitian`](generated/scipy.linalg.ishermitian.html#scipy.linalg.ishermitian "scipy.linalg.ishermitian")(a[,Â atol,Â rtol]) | Check if a square 2D array is Hermitian. |
| [`LinAlgError`](generated/scipy.linalg.LinAlgError.html#scipy.linalg.LinAlgError "scipy.linalg.LinAlgError") | Generic Python-exception-derived object raised by linalg functions. |
| [`LinAlgWarning`](generated/scipy.linalg.LinAlgWarning.html#scipy.linalg.LinAlgWarning "scipy.linalg.LinAlgWarning") | The warning emitted when a linear algebra related operation is close to fail conditions of the algorithm or loss of accuracy is expected. |
## Eigenvalue Problems[#](#eigenvalue-problems "Link to this heading")
|  |  |
| --- | --- |
| [`eig`](generated/scipy.linalg.eig.html#scipy.linalg.eig "scipy.linalg.eig")(a[,Â b,Â left,Â right,Â overwrite\_a,Â ...]) | Solve an ordinary or generalized eigenvalue problem of a square matrix. |
| [`eigvals`](generated/scipy.linalg.eigvals.html#scipy.linalg.eigvals "scipy.linalg.eigvals")(a[,Â b,Â overwrite\_a,Â overwrite\_b,Â ...]) | Compute eigenvalues from an ordinary or generalized eigenvalue problem. |
| [`eigh`](generated/scipy.linalg.eigh.html#scipy.linalg.eigh "scipy.linalg.eigh")(a[,Â b,Â lower,Â eigvals\_only,Â ...]) | Solve a standard or generalized eigenvalue problem for a complex Hermitian or real symmetric matrix. |
| [`eigvalsh`](generated/scipy.linalg.eigvalsh.html#scipy.linalg.eigvalsh "scipy.linalg.eigvalsh")(a[,Â b,Â lower,Â overwrite\_a,Â ...]) | Solves a standard or generalized eigenvalue problem for a complex Hermitian or real symmetric matrix. |
| [`eig_banded`](generated/scipy.linalg.eig_banded.html#scipy.linalg.eig_banded "scipy.linalg.eig_banded")(a\_band[,Â lower,Â eigvals\_only,Â ...]) | Solve real symmetric or complex Hermitian band matrix eigenvalue problem. |
| [`eigvals_banded`](generated/scipy.linalg.eigvals_banded.html#scipy.linalg.eigvals_banded "scipy.linalg.eigvals_banded")(a\_band[,Â lower,Â ...]) | Solve real symmetric or complex Hermitian band matrix eigenvalue problem. |
| [`eigh_tridiagonal`](generated/scipy.linalg.eigh_tridiagonal.html#scipy.linalg.eigh_tridiagonal "scipy.linalg.eigh_tridiagonal")(d,Â e[,Â eigvals\_only,Â ...]) | Solve eigenvalue problem for a real symmetric tridiagonal matrix. |
| [`eigvalsh_tridiagonal`](generated/scipy.linalg.eigvalsh_tridiagonal.html#scipy.linalg.eigvalsh_tridiagonal "scipy.linalg.eigvalsh_tridiagonal")(d,Â e[,Â select,Â ...]) | Solve eigenvalue problem for a real symmetric tridiagonal matrix. |
## Decompositions[#](#decompositions "Link to this heading")
|  |  |
| --- | --- |
| [`lu`](generated/scipy.linalg.lu.html#scipy.linalg.lu "scipy.linalg.lu")(a[,Â permute\_l,Â overwrite\_a,Â ...]) | Compute LU decomposition of a matrix with partial pivoting. |
| [`lu_factor`](generated/scipy.linalg.lu_factor.html#scipy.linalg.lu_factor "scipy.linalg.lu_factor")(a[,Â overwrite\_a,Â check\_finite]) | Compute pivoted LU decomposition of a matrix. |
| [`lu_solve`](generated/scipy.linalg.lu_solve.html#scipy.linalg.lu_solve "scipy.linalg.lu_solve")(lu\_and\_piv,Â b[,Â trans,Â ...]) | Solve an equation system, `a @ x = b`, given the LU factorization of a. |
| [`svd`](generated/scipy.linalg.svd.html#scipy.linalg.svd "scipy.linalg.svd")(a[,Â full\_matrices,Â compute\_uv,Â ...]) | Singular Value Decomposition. |
| [`svdvals`](generated/scipy.linalg.svdvals.html#scipy.linalg.svdvals "scipy.linalg.svdvals")(a[,Â overwrite\_a,Â check\_finite]) | Compute singular values of a matrix. |
| [`diagsvd`](generated/scipy.linalg.diagsvd.html#scipy.linalg.diagsvd "scipy.linalg.diagsvd")(s,Â M,Â N) | Construct the sigma matrix in SVD from singular values and size M, N. |
| [`orth`](generated/scipy.linalg.orth.html#scipy.linalg.orth "scipy.linalg.orth")(A[,Â rcond]) | Construct an orthonormal basis for the range of A using SVD. |
| [`null_space`](generated/scipy.linalg.null_space.html#scipy.linalg.null_space "scipy.linalg.null_space")(A[,Â rcond,Â overwrite\_a,Â ...]) | Construct an orthonormal basis for the null space of A using SVD. |
| [`ldl`](generated/scipy.linalg.ldl.html#scipy.linalg.ldl "scipy.linalg.ldl")(A[,Â lower,Â hermitian,Â overwrite\_a,Â ...]) | Computes the LDLt or Bunch-Kaufman factorization of a symmetric/ hermitian matrix. |
| [`cholesky`](generated/scipy.linalg.cholesky.html#scipy.linalg.cholesky "scipy.linalg.cholesky")(a[,Â lower,Â overwrite\_a,Â check\_finite]) | Compute the Cholesky decomposition of a matrix. |
| [`cholesky_banded`](generated/scipy.linalg.cholesky_banded.html#scipy.linalg.cholesky_banded "scipy.linalg.cholesky_banded")(ab[,Â overwrite\_ab,Â lower,Â ...]) | Cholesky decompose a banded Hermitian positive-definite matrix. |
| [`cho_factor`](generated/scipy.linalg.cho_factor.html#scipy.linalg.cho_factor "scipy.linalg.cho_factor")(a[,Â lower,Â overwrite\_a,Â check\_finite]) | Compute the Cholesky decomposition of a matrix, to use in cho\_solve. |
| [`cho_solve`](generated/scipy.linalg.cho_solve.html#scipy.linalg.cho_solve "scipy.linalg.cho_solve")(c\_and\_lower,Â b[,Â overwrite\_b,Â ...]) | Solve the linear equations A x = b, given the Cholesky factorization of A. |
| [`cho_solve_banded`](generated/scipy.linalg.cho_solve_banded.html#scipy.linalg.cho_solve_banded "scipy.linalg.cho_solve_banded")(cb\_and\_lower,Â b[,Â ...]) | Solve the linear equations `A x = b`, given the Cholesky factorization of the banded Hermitian `A`. |
| [`polar`](generated/scipy.linalg.polar.html#scipy.linalg.polar "scipy.linalg.polar")(a[,Â side]) | Compute the polar decomposition. |
| [`qr`](generated/scipy.linalg.qr.html#scipy.linalg.qr "scipy.linalg.qr")(a[,Â overwrite\_a,Â lwork,Â mode,Â pivoting,Â ...]) | Compute QR decomposition of a matrix. |
| [`qr_multiply`](generated/scipy.linalg.qr_multiply.html#scipy.linalg.qr_multiply "scipy.linalg.qr_multiply")(a,Â c[,Â mode,Â pivoting,Â ...]) | Calculate the QR decomposition and multiply Q with a matrix. |
| [`qr_update`](generated/scipy.linalg.qr_update.html#scipy.linalg.qr_update "scipy.linalg.qr_update")(Q,Â R,Â u,Â v[,Â overwrite\_qruv,Â ...]) | Rank-k QR update. |
| [`qr_delete`](generated/scipy.linalg.qr_delete.html#scipy.linalg.qr_delete "scipy.linalg.qr_delete")(Q,Â R,Â k,Â intÂ p=1[,Â which,Â ...]) | QR downdate on row or column deletions. |
| [`qr_insert`](generated/scipy.linalg.qr_insert.html#scipy.linalg.qr_insert "scipy.linalg.qr_insert")(Q,Â R,Â u,Â k[,Â which,Â rcond,Â ...]) | QR update on row or column insertions. |
| [`rq`](generated/scipy.linalg.rq.html#scipy.linalg.rq "scipy.linalg.rq")(a[,Â overwrite\_a,Â lwork,Â mode,Â check\_finite]) | Compute RQ decomposition of a matrix. |
| [`qz`](generated/scipy.linalg.qz.html#scipy.linalg.qz "scipy.linalg.qz")(A,Â B[,Â output,Â lwork,Â sort,Â overwrite\_a,Â ...]) | QZ decomposition for generalized eigenvalues of a pair of matrices. |
| [`ordqz`](generated/scipy.linalg.ordqz.html#scipy.linalg.ordqz "scipy.linalg.ordqz")(A,Â B[,Â sort,Â output,Â overwrite\_a,Â ...]) | QZ decomposition for a pair of matrices with reordering. |
| [`schur`](generated/scipy.linalg.schur.html#scipy.linalg.schur "scipy.linalg.schur")(a[,Â output,Â lwork,Â overwrite\_a,Â sort,Â ...]) | Compute Schur decomposition of a matrix. |
| [`rsf2csf`](generated/scipy.linalg.rsf2csf.html#scipy.linalg.rsf2csf "scipy.linalg.rsf2csf")(T,Â Z[,Â check\_finite]) | Convert real Schur form to complex Schur form. |
| [`hessenberg`](generated/scipy.linalg.hessenberg.html#scipy.linalg.hessenberg "scipy.linalg.hessenberg")(a[,Â calc\_q,Â overwrite\_a,Â ...]) | Compute Hessenberg form of a matrix. |
| [`cdf2rdf`](generated/scipy.linalg.cdf2rdf.html#scipy.linalg.cdf2rdf "scipy.linalg.cdf2rdf")(w,Â v) | Complex diagonal form to real diagonal block form. |
| [`cossin`](generated/scipy.linalg.cossin.html#scipy.linalg.cossin "scipy.linalg.cossin")(X[,Â p,Â q,Â separate,Â swap\_sign,Â ...]) | Compute the cosine-sine (CS) decomposition of an orthogonal/unitary matrix. |
See also
[`scipy.linalg.interpolative`](linalg.interpolative.html#module-scipy.linalg.interpolative "scipy.linalg.interpolative") â Interpolative matrix decompositions
## Matrix Functions[#](#matrix-functions "Link to this heading")
|  |  |
| --- | --- |
| [`expm`](generated/scipy.linalg.expm.html#scipy.linalg.expm "scipy.linalg.expm")(A) | Compute the matrix exponential of an array. |
| [`logm`](generated/scipy.linalg.logm.html#scipy.linalg.logm "scipy.linalg.logm")(A) | Compute matrix logarithm. |
| [`cosm`](generated/scipy.linalg.cosm.html#scipy.linalg.cosm "scipy.linalg.cosm")(A) | Compute the matrix cosine. |
| [`sinm`](generated/scipy.linalg.sinm.html#scipy.linalg.sinm "scipy.linalg.sinm")(A) | Compute the matrix sine. |
| [`tanm`](generated/scipy.linalg.tanm.html#scipy.linalg.tanm "scipy.linalg.tanm")(A) | Compute the matrix tangent. |
| [`coshm`](generated/scipy.linalg.coshm.html#scipy.linalg.coshm "scipy.linalg.coshm")(A) | Compute the hyperbolic matrix cosine. |
| [`sinhm`](generated/scipy.linalg.sinhm.html#scipy.linalg.sinhm "scipy.linalg.sinhm")(A) | Compute the hyperbolic matrix sine. |
| [`tanhm`](generated/scipy.linalg.tanhm.html#scipy.linalg.tanhm "scipy.linalg.tanhm")(A) | Compute the hyperbolic matrix tangent. |
| [`signm`](generated/scipy.linalg.signm.html#scipy.linalg.signm "scipy.linalg.signm")(A) | Matrix sign function. |
| [`sqrtm`](generated/scipy.linalg.sqrtm.html#scipy.linalg.sqrtm "scipy.linalg.sqrtm")(A) | Compute, if exists, the matrix square root. |
| [`funm`](generated/scipy.linalg.funm.html#scipy.linalg.funm "scipy.linalg.funm")(A,Â func[,Â disp]) | Evaluate a matrix function specified by a callable. |
| [`expm_frechet`](generated/scipy.linalg.expm_frechet.html#scipy.linalg.expm_frechet "scipy.linalg.expm_frechet")(A,Â E[,Â method,Â compute\_expm,Â ...]) | Frechet derivative of the matrix exponential of A in the direction E. |
| [`expm_cond`](generated/scipy.linalg.expm_cond.html#scipy.linalg.expm_cond "scipy.linalg.expm_cond")(A[,Â check\_finite]) | Relative condition number of the matrix exponential in the Frobenius norm. |
| [`fractional_matrix_power`](generated/scipy.linalg.fractional_matrix_power.html#scipy.linalg.fractional_matrix_power "scipy.linalg.fractional_matrix_power")(A,Â t) | Compute the fractional power of a matrix. |
## Matrix Equation Solvers[#](#matrix-equation-solvers "Link to this heading")
|  |  |
| --- | --- |
| [`solve_sylvester`](generated/scipy.linalg.solve_sylvester.html#scipy.linalg.solve_sylvester "scipy.linalg.solve_sylvester")(a,Â b,Â q) | Computes a solution (X) to the Sylvester equation \(AX + XB = Q\). |
| [`solve_continuous_are`](generated/scipy.linalg.solve_continuous_are.html#scipy.linalg.solve_continuous_are "scipy.linalg.solve_continuous_are")(a,Â b,Â q,Â r[,Â e,Â s,Â ...]) | Solves the continuous-time algebraic Riccati equation (CARE). |
| [`solve_discrete_are`](generated/scipy.linalg.solve_discrete_are.html#scipy.linalg.solve_discrete_are "scipy.linalg.solve_discrete_are")(a,Â b,Â q,Â r[,Â e,Â s,Â balanced]) | Solves the discrete-time algebraic Riccati equation (DARE). |
| [`solve_continuous_lyapunov`](generated/scipy.linalg.solve_continuous_lyapunov.html#scipy.linalg.solve_continuous_lyapunov "scipy.linalg.solve_continuous_lyapunov")(a,Â q) | Solves the continuous Lyapunov equation \(AX + XA^H = Q\). |
| [`solve_discrete_lyapunov`](generated/scipy.linalg.solve_discrete_lyapunov.html#scipy.linalg.solve_discrete_lyapunov "scipy.linalg.solve_discrete_lyapunov")(a,Â q[,Â method]) | Solves the discrete Lyapunov equation \(AXA^H - X + Q = 0\). |
## Sketches and Random Projections[#](#sketches-and-random-projections "Link to this heading")
|  |  |
| --- | --- |
| [`clarkson_woodruff_transform`](generated/scipy.linalg.clarkson_woodruff_transform.html#scipy.linalg.clarkson_woodruff_transform "scipy.linalg.clarkson_woodruff_transform")(input\_matrix,Â ...) | Applies a Clarkson-Woodruff Transform/sketch to the input matrix. |
## Special Matrices[#](#special-matrices "Link to this heading")
|  |  |
| --- | --- |
| [`block_diag`](generated/scipy.linalg.block_diag.html#scipy.linalg.block_diag "scipy.linalg.block_diag")(\*arrs) | Create a block diagonal array from provided arrays. |
| [`circulant`](generated/scipy.linalg.circulant.html#scipy.linalg.circulant "scipy.linalg.circulant")(c) | Construct a circulant matrix. |
| [`companion`](generated/scipy.linalg.companion.html#scipy.linalg.companion "scipy.linalg.companion")(a) | Create a companion matrix. |
| [`convolution_matrix`](generated/scipy.linalg.convolution_matrix.html#scipy.linalg.convolution_matrix "scipy.linalg.convolution_matrix")(a,Â n[,Â mode]) | Construct a convolution matrix. |
| [`dft`](generated/scipy.linalg.dft.html#scipy.linalg.dft "scipy.linalg.dft")(n[,Â scale]) | Discrete Fourier transform matrix. |
| [`fiedler`](generated/scipy.linalg.fiedler.html#scipy.linalg.fiedler "scipy.linalg.fiedler")(a) | Returns a symmetric Fiedler matrix. |
| [`fiedler_companion`](generated/scipy.linalg.fiedler_companion.html#scipy.linalg.fiedler_companion "scipy.linalg.fiedler_companion")(a) | Returns a Fiedler companion matrix. |
| [`hadamard`](generated/scipy.linalg.hadamard.html#scipy.linalg.hadamard "scipy.linalg.hadamard")(n[,Â dtype]) | Construct a Hadamard matrix. |
| [`hankel`](generated/scipy.linalg.hankel.html#scipy.linalg.hankel "scipy.linalg.hankel")(c[,Â r]) | Construct a Hankel matrix. |
| [`helmert`](generated/scipy.linalg.helmert.html#scipy.linalg.helmert "scipy.linalg.helmert")(n[,Â full]) | Create a Helmert matrix of order *n*. |
| [`hilbert`](generated/scipy.linalg.hilbert.html#scipy.linalg.hilbert "scipy.linalg.hilbert")(n) | Create a Hilbert matrix of order *n*. |
| [`invhilbert`](generated/scipy.linalg.invhilbert.html#scipy.linalg.invhilbert "scipy.linalg.invhilbert")(n[,Â exact]) | Compute the inverse of the Hilbert matrix of order *n*. |
| [`leslie`](generated/scipy.linalg.leslie.html#scipy.linalg.leslie "scipy.linalg.leslie")(f,Â s) | Create a Leslie matrix. |
| [`pascal`](generated/scipy.linalg.pascal.html#scipy.linalg.pascal "scipy.linalg.pascal")(n[,Â kind,Â exact]) | Returns the n x n Pascal matrix. |
| [`invpascal`](generated/scipy.linalg.invpascal.html#scipy.linalg.invpascal "scipy.linalg.invpascal")(n[,Â kind,Â exact]) | Returns the inverse of the n x n Pascal matrix. |
| [`toeplitz`](generated/scipy.linalg.toeplitz.html#scipy.linalg.toeplitz "scipy.linalg.toeplitz")(c[,Â r]) | Construct a Toeplitz matrix. |
## Low-level routines[#](#low-level-routines "Link to this heading")
|  |  |
| --- | --- |
| [`get_blas_funcs`](generated/scipy.linalg.get_blas_funcs.html#scipy.linalg.get_blas_funcs "scipy.linalg.get_blas_funcs")(names[,Â arrays,Â dtype,Â ilp64]) | Return available BLAS function objects from names. |
| [`get_lapack_funcs`](generated/scipy.linalg.get_lapack_funcs.html#scipy.linalg.get_lapack_funcs "scipy.linalg.get_lapack_funcs")(names[,Â arrays,Â dtype,Â ilp64]) | Return available LAPACK function objects from names. |
| [`find_best_blas_type`](generated/scipy.linalg.find_best_blas_type.html#scipy.linalg.find_best_blas_type "scipy.linalg.find_best_blas_type")([arrays,Â dtype]) | Find best-matching BLAS/LAPACK type. |
See also
[`scipy.linalg.blas`](linalg.blas.html#module-scipy.linalg.blas "scipy.linalg.blas") â Low-level BLAS functions
[`scipy.linalg.lapack`](linalg.lapack.html#module-scipy.linalg.lapack "scipy.linalg.lapack") â Low-level LAPACK functions
[`scipy.linalg.cython_blas`](linalg.cython_blas.html#module-scipy.linalg.cython_blas "scipy.linalg.cython_blas") â Low-level BLAS functions for Cython
[`scipy.linalg.cython_lapack`](linalg.cython_lapack.html#module-scipy.linalg.cython_lapack "scipy.linalg.cython_lapack") â Low-level LAPACK functions for Cython
[previous
scipy.io.arff.ParseArffError](generated/scipy.io.arff.ParseArffError.html "previous page")
[next
Low-level BLAS functions (`scipy.linalg.blas`)](linalg.blas.html "next page")
On this page
* [Basics](#basics)
* [Eigenvalue Problems](#eigenvalue-problems)
* [Decompositions](#decompositions)
* [Matrix Functions](#matrix-functions)
* [Matrix Equation Solvers](#matrix-equation-solvers)
* [Sketches and Random Projections](#sketches-and-random-projections)
* [Special Matrices](#special-matrices)
* [Low-level routines](#low-level-routines)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/linalg.blas.html#module-scipy.linalg.blas -->
* [SciPy API](index.html)
* [Linear algebra (`scipy.linalg`)](linalg.html)
* Low-level BLAS functions (`scipy.linalg.blas`)
# Low-level BLAS functions ([`scipy.linalg.blas`](#module-scipy.linalg.blas "scipy.linalg.blas"))[#](#low-level-blas-functions-scipy-linalg-blas "Link to this heading")
This module contains low-level functions from the BLAS library.
Added in version 0.12.0.
Note
The common `overwrite_<>` option in many routines, allows the
input arrays to be overwritten to avoid extra memory allocation.
However this requires the array to satisfy two conditions
which are memory order and the data type to match exactly the
order and the type expected by the routine.
As an example, if you pass a double precision float array to any
`S....` routine which expects single precision arguments, f2py
will create an intermediate array to match the argument types and
overwriting will be performed on that intermediate array.
Similarly, if a C-contiguous array is passed, f2py will pass a
FORTRAN-contiguous array internally. Please make sure that these
details are satisfied. More information can be found in the f2py
documentation.
Warning
These functions do little to no error checking.
It is possible to cause crashes by mis-using them,
so prefer using the higher-level routines in [`scipy.linalg`](linalg.html#module-scipy.linalg "scipy.linalg").
Note
Prefer using `get_blas_funcs` to importing the bare functions directly.
If you do, for example, `from scipy.linalg.blas import dgemm`, the `dgemm`
function may be either LP64 or ILP64, depending on how SciPy is built.
The following is more robust:
```
>>> from scipy.linalg.blas import get_blas_funcs
>>> dgemm = get_blas_funcs('gemm', dtype='float64', ilp64='preferred')
>>> dgemm.int_dtype
dtype('int32')    # may vary
```
## Finding functions[#](#finding-functions "Link to this heading")
|  |  |
| --- | --- |
| [`get_blas_funcs`](generated/scipy.linalg.blas.get_blas_funcs.html#scipy.linalg.blas.get_blas_funcs "scipy.linalg.blas.get_blas_funcs")(names[,Â arrays,Â dtype,Â ilp64]) | Return available BLAS function objects from names. |
| [`find_best_blas_type`](generated/scipy.linalg.blas.find_best_blas_type.html#scipy.linalg.blas.find_best_blas_type "scipy.linalg.blas.find_best_blas_type")([arrays,Â dtype]) | Find best-matching BLAS/LAPACK type. |
## BLAS Level 1 functions[#](#blas-level-1-functions "Link to this heading")
|  |  |
| --- | --- |
| [`sasum`](generated/scipy.linalg.blas.sasum.html#scipy.linalg.blas.sasum "scipy.linalg.blas.sasum")(x,[n,offx,incx]) | Wrapper for `sasum`. |
| [`saxpy`](generated/scipy.linalg.blas.saxpy.html#scipy.linalg.blas.saxpy "scipy.linalg.blas.saxpy")(x,y,[n,a,offx,incx,offy,incy]) | Wrapper for `saxpy`. |
| [`scasum`](generated/scipy.linalg.blas.scasum.html#scipy.linalg.blas.scasum "scipy.linalg.blas.scasum")(x,[n,offx,incx]) | Wrapper for `scasum`. |
| [`scnrm2`](generated/scipy.linalg.blas.scnrm2.html#scipy.linalg.blas.scnrm2 "scipy.linalg.blas.scnrm2")(x,[n,offx,incx]) | Wrapper for `scnrm2`. |
| [`scopy`](generated/scipy.linalg.blas.scopy.html#scipy.linalg.blas.scopy "scipy.linalg.blas.scopy")(x,y,[n,offx,incx,offy,incy]) | Wrapper for `scopy`. |
| [`sdot`](generated/scipy.linalg.blas.sdot.html#scipy.linalg.blas.sdot "scipy.linalg.blas.sdot")(x,y,[n,offx,incx,offy,incy]) | Wrapper for `sdot`. |
| [`snrm2`](generated/scipy.linalg.blas.snrm2.html#scipy.linalg.blas.snrm2 "scipy.linalg.blas.snrm2")(x,[n,offx,incx]) | Wrapper for `snrm2`. |
| [`srot`](generated/scipy.linalg.blas.srot.html#scipy.linalg.blas.srot "scipy.linalg.blas.srot")(...) | Wrapper for `srot`. |
| [`srotg`](generated/scipy.linalg.blas.srotg.html#scipy.linalg.blas.srotg "scipy.linalg.blas.srotg")(a,Â b) | Wrapper for `srotg`. |
| [`srotm`](generated/scipy.linalg.blas.srotm.html#scipy.linalg.blas.srotm "scipy.linalg.blas.srotm")(...) | Wrapper for `srotm`. |
| [`srotmg`](generated/scipy.linalg.blas.srotmg.html#scipy.linalg.blas.srotmg "scipy.linalg.blas.srotmg")(d1,Â d2,Â x1,Â y1) | Wrapper for `srotmg`. |
| [`sscal`](generated/scipy.linalg.blas.sscal.html#scipy.linalg.blas.sscal "scipy.linalg.blas.sscal")(a,x,[n,offx,incx]) | Wrapper for `sscal`. |
| [`sswap`](generated/scipy.linalg.blas.sswap.html#scipy.linalg.blas.sswap "scipy.linalg.blas.sswap")(x,y,[n,offx,incx,offy,incy]) | Wrapper for `sswap`. |
| [`dasum`](generated/scipy.linalg.blas.dasum.html#scipy.linalg.blas.dasum "scipy.linalg.blas.dasum")(x,[n,offx,incx]) | Wrapper for `dasum`. |
| [`daxpy`](generated/scipy.linalg.blas.daxpy.html#scipy.linalg.blas.daxpy "scipy.linalg.blas.daxpy")(x,y,[n,a,offx,incx,offy,incy]) | Wrapper for `daxpy`. |
| [`dcopy`](generated/scipy.linalg.blas.dcopy.html#scipy.linalg.blas.dcopy "scipy.linalg.blas.dcopy")(x,y,[n,offx,incx,offy,incy]) | Wrapper for `dcopy`. |
| [`ddot`](generated/scipy.linalg.blas.ddot.html#scipy.linalg.blas.ddot "scipy.linalg.blas.ddot")(x,y,[n,offx,incx,offy,incy]) | Wrapper for `ddot`. |
| [`dnrm2`](generated/scipy.linalg.blas.dnrm2.html#scipy.linalg.blas.dnrm2 "scipy.linalg.blas.dnrm2")(x,[n,offx,incx]) | Wrapper for `dnrm2`. |
| [`drot`](generated/scipy.linalg.blas.drot.html#scipy.linalg.blas.drot "scipy.linalg.blas.drot")(...) | Wrapper for `drot`. |
| [`drotg`](generated/scipy.linalg.blas.drotg.html#scipy.linalg.blas.drotg "scipy.linalg.blas.drotg")(a,Â b) | Wrapper for `drotg`. |
| [`drotm`](generated/scipy.linalg.blas.drotm.html#scipy.linalg.blas.drotm "scipy.linalg.blas.drotm")(...) | Wrapper for `drotm`. |
| [`drotmg`](generated/scipy.linalg.blas.drotmg.html#scipy.linalg.blas.drotmg "scipy.linalg.blas.drotmg")(d1,Â d2,Â x1,Â y1) | Wrapper for `drotmg`. |
| [`dscal`](generated/scipy.linalg.blas.dscal.html#scipy.linalg.blas.dscal "scipy.linalg.blas.dscal")(a,x,[n,offx,incx]) | Wrapper for `dscal`. |
| [`dswap`](generated/scipy.linalg.blas.dswap.html#scipy.linalg.blas.dswap "scipy.linalg.blas.dswap")(x,y,[n,offx,incx,offy,incy]) | Wrapper for `dswap`. |
| [`dzasum`](generated/scipy.linalg.blas.dzasum.html#scipy.linalg.blas.dzasum "scipy.linalg.blas.dzasum")(x,[n,offx,incx]) | Wrapper for `dzasum`. |
| [`dznrm2`](generated/scipy.linalg.blas.dznrm2.html#scipy.linalg.blas.dznrm2 "scipy.linalg.blas.dznrm2")(x,[n,offx,incx]) | Wrapper for `dznrm2`. |
| [`icamax`](generated/scipy.linalg.blas.icamax.html#scipy.linalg.blas.icamax "scipy.linalg.blas.icamax")(x,[n,offx,incx]) | Wrapper for `icamax`. |
| [`idamax`](generated/scipy.linalg.blas.idamax.html#scipy.linalg.blas.idamax "scipy.linalg.blas.idamax")(x,[n,offx,incx]) | Wrapper for `idamax`. |
| [`isamax`](generated/scipy.linalg.blas.isamax.html#scipy.linalg.blas.isamax "scipy.linalg.blas.isamax")(x,[n,offx,incx]) | Wrapper for `isamax`. |
| [`izamax`](generated/scipy.linalg.blas.izamax.html#scipy.linalg.blas.izamax "scipy.linalg.blas.izamax")(x,[n,offx,incx]) | Wrapper for `izamax`. |
| [`caxpy`](generated/scipy.linalg.blas.caxpy.html#scipy.linalg.blas.caxpy "scipy.linalg.blas.caxpy")(x,y,[n,a,offx,incx,offy,incy]) | Wrapper for `caxpy`. |
| [`ccopy`](generated/scipy.linalg.blas.ccopy.html#scipy.linalg.blas.ccopy "scipy.linalg.blas.ccopy")(x,y,[n,offx,incx,offy,incy]) | Wrapper for `ccopy`. |
| [`cdotc`](generated/scipy.linalg.blas.cdotc.html#scipy.linalg.blas.cdotc "scipy.linalg.blas.cdotc")(x,y,[n,offx,incx,offy,incy]) | Wrapper for `cdotc`. |
| [`cdotu`](generated/scipy.linalg.blas.cdotu.html#scipy.linalg.blas.cdotu "scipy.linalg.blas.cdotu")(x,y,[n,offx,incx,offy,incy]) | Wrapper for `cdotu`. |
| [`crotg`](generated/scipy.linalg.blas.crotg.html#scipy.linalg.blas.crotg "scipy.linalg.blas.crotg")(a,Â b) | Wrapper for `crotg`. |
| [`cscal`](generated/scipy.linalg.blas.cscal.html#scipy.linalg.blas.cscal "scipy.linalg.blas.cscal")(a,x,[n,offx,incx]) | Wrapper for `cscal`. |
| [`csrot`](generated/scipy.linalg.blas.csrot.html#scipy.linalg.blas.csrot "scipy.linalg.blas.csrot")(...) | Wrapper for `csrot`. |
| [`csscal`](generated/scipy.linalg.blas.csscal.html#scipy.linalg.blas.csscal "scipy.linalg.blas.csscal")(a,x,[n,offx,incx,overwrite\_x]) | Wrapper for `csscal`. |
| [`cswap`](generated/scipy.linalg.blas.cswap.html#scipy.linalg.blas.cswap "scipy.linalg.blas.cswap")(x,y,[n,offx,incx,offy,incy]) | Wrapper for `cswap`. |
| [`zaxpy`](generated/scipy.linalg.blas.zaxpy.html#scipy.linalg.blas.zaxpy "scipy.linalg.blas.zaxpy")(x,y,[n,a,offx,incx,offy,incy]) | Wrapper for `zaxpy`. |
| [`zcopy`](generated/scipy.linalg.blas.zcopy.html#scipy.linalg.blas.zcopy "scipy.linalg.blas.zcopy")(x,y,[n,offx,incx,offy,incy]) | Wrapper for `zcopy`. |
| [`zdotc`](generated/scipy.linalg.blas.zdotc.html#scipy.linalg.blas.zdotc "scipy.linalg.blas.zdotc")(x,y,[n,offx,incx,offy,incy]) | Wrapper for `zdotc`. |
| [`zdotu`](generated/scipy.linalg.blas.zdotu.html#scipy.linalg.blas.zdotu "scipy.linalg.blas.zdotu")(x,y,[n,offx,incx,offy,incy]) | Wrapper for `zdotu`. |
| [`zdrot`](generated/scipy.linalg.blas.zdrot.html#scipy.linalg.blas.zdrot "scipy.linalg.blas.zdrot")(...) | Wrapper for `zdrot`. |
| [`zdscal`](generated/scipy.linalg.blas.zdscal.html#scipy.linalg.blas.zdscal "scipy.linalg.blas.zdscal")(a,x,[n,offx,incx,overwrite\_x]) | Wrapper for `zdscal`. |
| [`zrotg`](generated/scipy.linalg.blas.zrotg.html#scipy.linalg.blas.zrotg "scipy.linalg.blas.zrotg")(a,Â b) | Wrapper for `zrotg`. |
| [`zscal`](generated/scipy.linalg.blas.zscal.html#scipy.linalg.blas.zscal "scipy.linalg.blas.zscal")(a,x,[n,offx,incx]) | Wrapper for `zscal`. |
| [`zswap`](generated/scipy.linalg.blas.zswap.html#scipy.linalg.blas.zswap "scipy.linalg.blas.zswap")(x,y,[n,offx,incx,offy,incy]) | Wrapper for `zswap`. |
## BLAS Level 2 functions[#](#blas-level-2-functions "Link to this heading")
|  |  |
| --- | --- |
| [`sgbmv`](generated/scipy.linalg.blas.sgbmv.html#scipy.linalg.blas.sgbmv "scipy.linalg.blas.sgbmv")(...) | Wrapper for `sgbmv`. |
| [`sgemv`](generated/scipy.linalg.blas.sgemv.html#scipy.linalg.blas.sgemv "scipy.linalg.blas.sgemv")(...) | Wrapper for `sgemv`. |
| [`sger`](generated/scipy.linalg.blas.sger.html#scipy.linalg.blas.sger "scipy.linalg.blas.sger")(...) | Wrapper for `sger`. |
| [`ssbmv`](generated/scipy.linalg.blas.ssbmv.html#scipy.linalg.blas.ssbmv "scipy.linalg.blas.ssbmv")(...) | Wrapper for `ssbmv`. |
| [`sspmv`](generated/scipy.linalg.blas.sspmv.html#scipy.linalg.blas.sspmv "scipy.linalg.blas.sspmv")(...) | Wrapper for `sspmv`. |
| [`sspr`](generated/scipy.linalg.blas.sspr.html#scipy.linalg.blas.sspr "scipy.linalg.blas.sspr")(n,alpha,x,ap,[incx,offx,lower,overwrite\_ap]) | Wrapper for `sspr`. |
| [`sspr2`](generated/scipy.linalg.blas.sspr2.html#scipy.linalg.blas.sspr2 "scipy.linalg.blas.sspr2")(...) | Wrapper for `sspr2`. |
| [`ssymv`](generated/scipy.linalg.blas.ssymv.html#scipy.linalg.blas.ssymv "scipy.linalg.blas.ssymv")(...) | Wrapper for `ssymv`. |
| [`ssyr`](generated/scipy.linalg.blas.ssyr.html#scipy.linalg.blas.ssyr "scipy.linalg.blas.ssyr")(alpha,x,[lower,incx,offx,n,a,overwrite\_a]) | Wrapper for `ssyr`. |
| [`ssyr2`](generated/scipy.linalg.blas.ssyr2.html#scipy.linalg.blas.ssyr2 "scipy.linalg.blas.ssyr2")(...) | Wrapper for `ssyr2`. |
| [`stbmv`](generated/scipy.linalg.blas.stbmv.html#scipy.linalg.blas.stbmv "scipy.linalg.blas.stbmv")(...) | Wrapper for `stbmv`. |
| [`stbsv`](generated/scipy.linalg.blas.stbsv.html#scipy.linalg.blas.stbsv "scipy.linalg.blas.stbsv")(...) | Wrapper for `stbsv`. |
| [`stpmv`](generated/scipy.linalg.blas.stpmv.html#scipy.linalg.blas.stpmv "scipy.linalg.blas.stpmv")(...) | Wrapper for `stpmv`. |
| [`stpsv`](generated/scipy.linalg.blas.stpsv.html#scipy.linalg.blas.stpsv "scipy.linalg.blas.stpsv")(...) | Wrapper for `stpsv`. |
| [`strmv`](generated/scipy.linalg.blas.strmv.html#scipy.linalg.blas.strmv "scipy.linalg.blas.strmv")(...) | Wrapper for `strmv`. |
| [`strsv`](generated/scipy.linalg.blas.strsv.html#scipy.linalg.blas.strsv "scipy.linalg.blas.strsv")(...) | Wrapper for `strsv`. |
| [`dgbmv`](generated/scipy.linalg.blas.dgbmv.html#scipy.linalg.blas.dgbmv "scipy.linalg.blas.dgbmv")(...) | Wrapper for `dgbmv`. |
| [`dgemv`](generated/scipy.linalg.blas.dgemv.html#scipy.linalg.blas.dgemv "scipy.linalg.blas.dgemv")(...) | Wrapper for `dgemv`. |
| [`dger`](generated/scipy.linalg.blas.dger.html#scipy.linalg.blas.dger "scipy.linalg.blas.dger")(...) | Wrapper for `dger`. |
| [`dsbmv`](generated/scipy.linalg.blas.dsbmv.html#scipy.linalg.blas.dsbmv "scipy.linalg.blas.dsbmv")(...) | Wrapper for `dsbmv`. |
| [`dspmv`](generated/scipy.linalg.blas.dspmv.html#scipy.linalg.blas.dspmv "scipy.linalg.blas.dspmv")(...) | Wrapper for `dspmv`. |
| [`dspr`](generated/scipy.linalg.blas.dspr.html#scipy.linalg.blas.dspr "scipy.linalg.blas.dspr")(n,alpha,x,ap,[incx,offx,lower,overwrite\_ap]) | Wrapper for `dspr`. |
| [`dspr2`](generated/scipy.linalg.blas.dspr2.html#scipy.linalg.blas.dspr2 "scipy.linalg.blas.dspr2")(...) | Wrapper for `dspr2`. |
| [`dsymv`](generated/scipy.linalg.blas.dsymv.html#scipy.linalg.blas.dsymv "scipy.linalg.blas.dsymv")(...) | Wrapper for `dsymv`. |
| [`dsyr`](generated/scipy.linalg.blas.dsyr.html#scipy.linalg.blas.dsyr "scipy.linalg.blas.dsyr")(alpha,x,[lower,incx,offx,n,a,overwrite\_a]) | Wrapper for `dsyr`. |
| [`dsyr2`](generated/scipy.linalg.blas.dsyr2.html#scipy.linalg.blas.dsyr2 "scipy.linalg.blas.dsyr2")(...) | Wrapper for `dsyr2`. |
| [`dtbmv`](generated/scipy.linalg.blas.dtbmv.html#scipy.linalg.blas.dtbmv "scipy.linalg.blas.dtbmv")(...) | Wrapper for `dtbmv`. |
| [`dtbsv`](generated/scipy.linalg.blas.dtbsv.html#scipy.linalg.blas.dtbsv "scipy.linalg.blas.dtbsv")(...) | Wrapper for `dtbsv`. |
| [`dtpmv`](generated/scipy.linalg.blas.dtpmv.html#scipy.linalg.blas.dtpmv "scipy.linalg.blas.dtpmv")(...) | Wrapper for `dtpmv`. |
| [`dtpsv`](generated/scipy.linalg.blas.dtpsv.html#scipy.linalg.blas.dtpsv "scipy.linalg.blas.dtpsv")(...) | Wrapper for `dtpsv`. |
| [`dtrmv`](generated/scipy.linalg.blas.dtrmv.html#scipy.linalg.blas.dtrmv "scipy.linalg.blas.dtrmv")(...) | Wrapper for `dtrmv`. |
| [`dtrsv`](generated/scipy.linalg.blas.dtrsv.html#scipy.linalg.blas.dtrsv "scipy.linalg.blas.dtrsv")(...) | Wrapper for `dtrsv`. |
| [`cgbmv`](generated/scipy.linalg.blas.cgbmv.html#scipy.linalg.blas.cgbmv "scipy.linalg.blas.cgbmv")(...) | Wrapper for `cgbmv`. |
| [`cgemv`](generated/scipy.linalg.blas.cgemv.html#scipy.linalg.blas.cgemv "scipy.linalg.blas.cgemv")(...) | Wrapper for `cgemv`. |
| [`cgerc`](generated/scipy.linalg.blas.cgerc.html#scipy.linalg.blas.cgerc "scipy.linalg.blas.cgerc")(...) | Wrapper for `cgerc`. |
| [`cgeru`](generated/scipy.linalg.blas.cgeru.html#scipy.linalg.blas.cgeru "scipy.linalg.blas.cgeru")(...) | Wrapper for `cgeru`. |
| [`chbmv`](generated/scipy.linalg.blas.chbmv.html#scipy.linalg.blas.chbmv "scipy.linalg.blas.chbmv")(...) | Wrapper for `chbmv`. |
| [`chemv`](generated/scipy.linalg.blas.chemv.html#scipy.linalg.blas.chemv "scipy.linalg.blas.chemv")(...) | Wrapper for `chemv`. |
| [`cher`](generated/scipy.linalg.blas.cher.html#scipy.linalg.blas.cher "scipy.linalg.blas.cher")(alpha,x,[lower,incx,offx,n,a,overwrite\_a]) | Wrapper for `cher`. |
| [`cher2`](generated/scipy.linalg.blas.cher2.html#scipy.linalg.blas.cher2 "scipy.linalg.blas.cher2")(...) | Wrapper for `cher2`. |
| [`chpmv`](generated/scipy.linalg.blas.chpmv.html#scipy.linalg.blas.chpmv "scipy.linalg.blas.chpmv")(...) | Wrapper for `chpmv`. |
| [`chpr`](generated/scipy.linalg.blas.chpr.html#scipy.linalg.blas.chpr "scipy.linalg.blas.chpr")(n,alpha,x,ap,[incx,offx,lower,overwrite\_ap]) | Wrapper for `chpr`. |
| [`chpr2`](generated/scipy.linalg.blas.chpr2.html#scipy.linalg.blas.chpr2 "scipy.linalg.blas.chpr2")(...) | Wrapper for `chpr2`. |
| [`cspmv`](generated/scipy.linalg.blas.cspmv.html#scipy.linalg.blas.cspmv "scipy.linalg.blas.cspmv")(...) | Wrapper for `cspmv`. |
| [`cspr`](generated/scipy.linalg.blas.cspr.html#scipy.linalg.blas.cspr "scipy.linalg.blas.cspr")(n,alpha,x,ap,[incx,offx,lower,overwrite\_ap]) | Wrapper for `cspr`. |
| [`csyr`](generated/scipy.linalg.blas.csyr.html#scipy.linalg.blas.csyr "scipy.linalg.blas.csyr")(alpha,x,[lower,incx,offx,n,a,overwrite\_a]) | Wrapper for `csyr`. |
| [`ctbmv`](generated/scipy.linalg.blas.ctbmv.html#scipy.linalg.blas.ctbmv "scipy.linalg.blas.ctbmv")(...) | Wrapper for `ctbmv`. |
| [`ctbsv`](generated/scipy.linalg.blas.ctbsv.html#scipy.linalg.blas.ctbsv "scipy.linalg.blas.ctbsv")(...) | Wrapper for `ctbsv`. |
| [`ctpmv`](generated/scipy.linalg.blas.ctpmv.html#scipy.linalg.blas.ctpmv "scipy.linalg.blas.ctpmv")(...) | Wrapper for `ctpmv`. |
| [`ctpsv`](generated/scipy.linalg.blas.ctpsv.html#scipy.linalg.blas.ctpsv "scipy.linalg.blas.ctpsv")(...) | Wrapper for `ctpsv`. |
| [`ctrmv`](generated/scipy.linalg.blas.ctrmv.html#scipy.linalg.blas.ctrmv "scipy.linalg.blas.ctrmv")(...) | Wrapper for `ctrmv`. |
| [`ctrsv`](generated/scipy.linalg.blas.ctrsv.html#scipy.linalg.blas.ctrsv "scipy.linalg.blas.ctrsv")(...) | Wrapper for `ctrsv`. |
| [`zgbmv`](generated/scipy.linalg.blas.zgbmv.html#scipy.linalg.blas.zgbmv "scipy.linalg.blas.zgbmv")(...) | Wrapper for `zgbmv`. |
| [`zgemv`](generated/scipy.linalg.blas.zgemv.html#scipy.linalg.blas.zgemv "scipy.linalg.blas.zgemv")(...) | Wrapper for `zgemv`. |
| [`zgerc`](generated/scipy.linalg.blas.zgerc.html#scipy.linalg.blas.zgerc "scipy.linalg.blas.zgerc")(...) | Wrapper for `zgerc`. |
| [`zgeru`](generated/scipy.linalg.blas.zgeru.html#scipy.linalg.blas.zgeru "scipy.linalg.blas.zgeru")(...) | Wrapper for `zgeru`. |
| [`zhbmv`](generated/scipy.linalg.blas.zhbmv.html#scipy.linalg.blas.zhbmv "scipy.linalg.blas.zhbmv")(...) | Wrapper for `zhbmv`. |
| [`zhemv`](generated/scipy.linalg.blas.zhemv.html#scipy.linalg.blas.zhemv "scipy.linalg.blas.zhemv")(...) | Wrapper for `zhemv`. |
| [`zher`](generated/scipy.linalg.blas.zher.html#scipy.linalg.blas.zher "scipy.linalg.blas.zher")(alpha,x,[lower,incx,offx,n,a,overwrite\_a]) | Wrapper for `zher`. |
| [`zher2`](generated/scipy.linalg.blas.zher2.html#scipy.linalg.blas.zher2 "scipy.linalg.blas.zher2")(...) | Wrapper for `zher2`. |
| [`zhpmv`](generated/scipy.linalg.blas.zhpmv.html#scipy.linalg.blas.zhpmv "scipy.linalg.blas.zhpmv")(...) | Wrapper for `zhpmv`. |
| [`zhpr`](generated/scipy.linalg.blas.zhpr.html#scipy.linalg.blas.zhpr "scipy.linalg.blas.zhpr")(n,alpha,x,ap,[incx,offx,lower,overwrite\_ap]) | Wrapper for `zhpr`. |
| [`zhpr2`](generated/scipy.linalg.blas.zhpr2.html#scipy.linalg.blas.zhpr2 "scipy.linalg.blas.zhpr2")(...) | Wrapper for `zhpr2`. |
| [`zspmv`](generated/scipy.linalg.blas.zspmv.html#scipy.linalg.blas.zspmv "scipy.linalg.blas.zspmv")(...) | Wrapper for `zspmv`. |
| [`zspr`](generated/scipy.linalg.blas.zspr.html#scipy.linalg.blas.zspr "scipy.linalg.blas.zspr")(n,alpha,x,ap,[incx,offx,lower,overwrite\_ap]) | Wrapper for `zspr`. |
| [`zsyr`](generated/scipy.linalg.blas.zsyr.html#scipy.linalg.blas.zsyr "scipy.linalg.blas.zsyr")(alpha,x,[lower,incx,offx,n,a,overwrite\_a]) | Wrapper for `zsyr`. |
| [`ztbmv`](generated/scipy.linalg.blas.ztbmv.html#scipy.linalg.blas.ztbmv "scipy.linalg.blas.ztbmv")(...) | Wrapper for `ztbmv`. |
| [`ztbsv`](generated/scipy.linalg.blas.ztbsv.html#scipy.linalg.blas.ztbsv "scipy.linalg.blas.ztbsv")(...) | Wrapper for `ztbsv`. |
| [`ztpmv`](generated/scipy.linalg.blas.ztpmv.html#scipy.linalg.blas.ztpmv "scipy.linalg.blas.ztpmv")(...) | Wrapper for `ztpmv`. |
| [`ztpsv`](generated/scipy.linalg.blas.ztpsv.html#scipy.linalg.blas.ztpsv "scipy.linalg.blas.ztpsv")(...) | Wrapper for `ztpsv`. |
| [`ztrmv`](generated/scipy.linalg.blas.ztrmv.html#scipy.linalg.blas.ztrmv "scipy.linalg.blas.ztrmv")(...) | Wrapper for `ztrmv`. |
| [`ztrsv`](generated/scipy.linalg.blas.ztrsv.html#scipy.linalg.blas.ztrsv "scipy.linalg.blas.ztrsv")(...) | Wrapper for `ztrsv`. |
## BLAS Level 3 functions[#](#blas-level-3-functions "Link to this heading")
|  |  |
| --- | --- |
| [`sgemm`](generated/scipy.linalg.blas.sgemm.html#scipy.linalg.blas.sgemm "scipy.linalg.blas.sgemm")(...) | Wrapper for `sgemm`. |
| [`ssymm`](generated/scipy.linalg.blas.ssymm.html#scipy.linalg.blas.ssymm "scipy.linalg.blas.ssymm")(alpha,a,b,[beta,c,side,lower,overwrite\_c]) | Wrapper for `ssymm`. |
| [`ssyr2k`](generated/scipy.linalg.blas.ssyr2k.html#scipy.linalg.blas.ssyr2k "scipy.linalg.blas.ssyr2k")(...) | Wrapper for `ssyr2k`. |
| [`ssyrk`](generated/scipy.linalg.blas.ssyrk.html#scipy.linalg.blas.ssyrk "scipy.linalg.blas.ssyrk")(alpha,a,[beta,c,trans,lower,overwrite\_c]) | Wrapper for `ssyrk`. |
| [`strmm`](generated/scipy.linalg.blas.strmm.html#scipy.linalg.blas.strmm "scipy.linalg.blas.strmm")(...) | Wrapper for `strmm`. |
| [`strsm`](generated/scipy.linalg.blas.strsm.html#scipy.linalg.blas.strsm "scipy.linalg.blas.strsm")(...) | Wrapper for `strsm`. |
| [`dgemm`](generated/scipy.linalg.blas.dgemm.html#scipy.linalg.blas.dgemm "scipy.linalg.blas.dgemm")(...) | Wrapper for `dgemm`. |
| [`dsymm`](generated/scipy.linalg.blas.dsymm.html#scipy.linalg.blas.dsymm "scipy.linalg.blas.dsymm")(alpha,a,b,[beta,c,side,lower,overwrite\_c]) | Wrapper for `dsymm`. |
| [`dsyr2k`](generated/scipy.linalg.blas.dsyr2k.html#scipy.linalg.blas.dsyr2k "scipy.linalg.blas.dsyr2k")(...) | Wrapper for `dsyr2k`. |
| [`dsyrk`](generated/scipy.linalg.blas.dsyrk.html#scipy.linalg.blas.dsyrk "scipy.linalg.blas.dsyrk")(alpha,a,[beta,c,trans,lower,overwrite\_c]) | Wrapper for `dsyrk`. |
| [`dtrmm`](generated/scipy.linalg.blas.dtrmm.html#scipy.linalg.blas.dtrmm "scipy.linalg.blas.dtrmm")(...) | Wrapper for `dtrmm`. |
| [`dtrsm`](generated/scipy.linalg.blas.dtrsm.html#scipy.linalg.blas.dtrsm "scipy.linalg.blas.dtrsm")(...) | Wrapper for `dtrsm`. |
| [`cgemm`](generated/scipy.linalg.blas.cgemm.html#scipy.linalg.blas.cgemm "scipy.linalg.blas.cgemm")(...) | Wrapper for `cgemm`. |
| [`chemm`](generated/scipy.linalg.blas.chemm.html#scipy.linalg.blas.chemm "scipy.linalg.blas.chemm")(alpha,a,b,[beta,c,side,lower,overwrite\_c]) | Wrapper for `chemm`. |
| [`cher2k`](generated/scipy.linalg.blas.cher2k.html#scipy.linalg.blas.cher2k "scipy.linalg.blas.cher2k")(...) | Wrapper for `cher2k`. |
| [`cherk`](generated/scipy.linalg.blas.cherk.html#scipy.linalg.blas.cherk "scipy.linalg.blas.cherk")(alpha,a,[beta,c,trans,lower,overwrite\_c]) | Wrapper for `cherk`. |
| [`csymm`](generated/scipy.linalg.blas.csymm.html#scipy.linalg.blas.csymm "scipy.linalg.blas.csymm")(alpha,a,b,[beta,c,side,lower,overwrite\_c]) | Wrapper for `csymm`. |
| [`csyr2k`](generated/scipy.linalg.blas.csyr2k.html#scipy.linalg.blas.csyr2k "scipy.linalg.blas.csyr2k")(...) | Wrapper for `csyr2k`. |
| [`csyrk`](generated/scipy.linalg.blas.csyrk.html#scipy.linalg.blas.csyrk "scipy.linalg.blas.csyrk")(alpha,a,[beta,c,trans,lower,overwrite\_c]) | Wrapper for `csyrk`. |
| [`ctrmm`](generated/scipy.linalg.blas.ctrmm.html#scipy.linalg.blas.ctrmm "scipy.linalg.blas.ctrmm")(...) | Wrapper for `ctrmm`. |
| [`ctrsm`](generated/scipy.linalg.blas.ctrsm.html#scipy.linalg.blas.ctrsm "scipy.linalg.blas.ctrsm")(...) | Wrapper for `ctrsm`. |
| [`zgemm`](generated/scipy.linalg.blas.zgemm.html#scipy.linalg.blas.zgemm "scipy.linalg.blas.zgemm")(...) | Wrapper for `zgemm`. |
| [`zhemm`](generated/scipy.linalg.blas.zhemm.html#scipy.linalg.blas.zhemm "scipy.linalg.blas.zhemm")(alpha,a,b,[beta,c,side,lower,overwrite\_c]) | Wrapper for `zhemm`. |
| [`zher2k`](generated/scipy.linalg.blas.zher2k.html#scipy.linalg.blas.zher2k "scipy.linalg.blas.zher2k")(...) | Wrapper for `zher2k`. |
| [`zherk`](generated/scipy.linalg.blas.zherk.html#scipy.linalg.blas.zherk "scipy.linalg.blas.zherk")(alpha,a,[beta,c,trans,lower,overwrite\_c]) | Wrapper for `zherk`. |
| [`zsymm`](generated/scipy.linalg.blas.zsymm.html#scipy.linalg.blas.zsymm "scipy.linalg.blas.zsymm")(alpha,a,b,[beta,c,side,lower,overwrite\_c]) | Wrapper for `zsymm`. |
| [`zsyr2k`](generated/scipy.linalg.blas.zsyr2k.html#scipy.linalg.blas.zsyr2k "scipy.linalg.blas.zsyr2k")(...) | Wrapper for `zsyr2k`. |
| [`zsyrk`](generated/scipy.linalg.blas.zsyrk.html#scipy.linalg.blas.zsyrk "scipy.linalg.blas.zsyrk")(alpha,a,[beta,c,trans,lower,overwrite\_c]) | Wrapper for `zsyrk`. |
| [`ztrmm`](generated/scipy.linalg.blas.ztrmm.html#scipy.linalg.blas.ztrmm "scipy.linalg.blas.ztrmm")(...) | Wrapper for `ztrmm`. |
| [`ztrsm`](generated/scipy.linalg.blas.ztrsm.html#scipy.linalg.blas.ztrsm "scipy.linalg.blas.ztrsm")(...) | Wrapper for `ztrsm`. |
[previous
Linear algebra (`scipy.linalg`)](linalg.html "previous page")
[next
get\_blas\_funcs](generated/scipy.linalg.blas.get_blas_funcs.html "next page")
On this page
* [Finding functions](#finding-functions)
* [BLAS Level 1 functions](#blas-level-1-functions)
* [BLAS Level 2 functions](#blas-level-2-functions)
* [BLAS Level 3 functions](#blas-level-3-functions)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/linalg.cython_blas.html#module-scipy.linalg.cython_blas -->
* [SciPy API](index.html)
* [Linear algebra (`scipy.linalg`)](linalg.html)
* BLAS Functions for Cython
# BLAS Functions for Cython[#](#blas-functions-for-cython "Link to this heading")
Usable from Cython via:
```
cimport scipy.linalg.cython_blas
```
These wrappers do not check for alignment of arrays.
Alignment should be checked before these wrappers are used.
If using `cdotu`, `cdotc`, `zdotu`, `zdotc`, `sladiv`, or `dladiv`,
the `CYTHON_CCOMPLEX` define must be set to 0 during compilation. For
example, in a `meson.build` file when using Meson:
```
py.extension_module('ext_module'
    'ext_module.pyx',
    c_args: ['-DCYTHON_CCOMPLEX=0'],
    ...
)
```
## ILP64 support[#](#ilp64-support "Link to this heading")
Integer parameters in the function signatures use `int` for LP64
builds (the default) and `int64_t` for ILP64 builds. A convenience
typedef `blas_int` (aliasing the appropriate concrete type) is also
exported so that downstream packages can write code that works with
both variants. The build configuration can be checked at runtime via
`scipy.show_config(mode='dicts')['Build Dependencies']['blas']['cython blas ilp64']`.
Boolean (Fortran `logical`) parameters in the function signatures use `bint` for
LP64 builds and `int64_t` for ILP64 builds. A convenience typedef `blas_bint` is
exported in a similar way to `blas_int`.
Downstream packages that want to support both LP64 and ILP64 builds of SciPy
should follow this pattern:
1. Use `blas_int` for all integer variables passed to BLAS functions. For boolean
   variables, use `blas_bint`.
2. For backwards compatibility with scipy <=1.17.0 (if desired), perform a
   **build-time check** for whether `blas_int` is available, and typedef
   it as `int` otherwise. Example for Meson:
```
# Check if scipy's cython_blas exports blas_int (ILP64 support).
_blas_int_conf = configuration_data()
if cython.compiles('from scipy.linalg.cython_blas cimport blas_int')
  _blas_int_conf.set('BLAS_INT_DEF', 'from scipy.linalg.cython_blas cimport blas_int')
  _blas_int_conf.set('BLAS_BINT_DEF', 'from scipy.linalg.cython_blas cimport blas_bint')
else
  _blas_int_conf.set('BLAS_INT_DEF', 'ctypedef int blas_int')
  _blas_int_conf.set('BLAS_BINT_DEF', 'ctypedef bint blas_bint')
endif
_blas_int_pxi = configure_file(
  input: '_blas_int.pxi.in',
  output: '_blas_int.pxi',
  configuration: _blas_int_conf,
)
```
With the file `_blas_int.pxi.in` containing two lines:
```
@BLAS_INT_DEF@
@BLAS_BINT_DEF@
```
## `cython_blas` API[#](#cython-blas-api "Link to this heading")
Integer types:
* blas\_int: convenience typedef for either `int` (LP64) or `int64_t` (ILP64)
* blas\_bint: convenience typedef for either `bint` (LP64) or `int64_t` (ILP64)
Raw function pointers (Fortran-style pointer arguments):
* caxpy
* ccopy
* cdotc
* cdotu
* cgbmv
* cgemm
* cgemv
* cgerc
* cgeru
* chbmv
* chemm
* chemv
* cher
* cher2
* cher2k
* cherk
* chpmv
* chpr
* chpr2
* crotg
* cscal
* csrot
* csscal
* cswap
* csymm
* csyr2k
* csyrk
* ctbmv
* ctbsv
* ctpmv
* ctpsv
* ctrmm
* ctrmv
* ctrsm
* ctrsv
* dasum
* daxpy
* dcabs1
* dcopy
* ddot
* dgbmv
* dgemm
* dgemv
* dger
* dnrm2
* drot
* drotg
* drotm
* drotmg
* dsbmv
* dscal
* dsdot
* dspmv
* dspr
* dspr2
* dswap
* dsymm
* dsymv
* dsyr
* dsyr2
* dsyr2k
* dsyrk
* dtbmv
* dtbsv
* dtpmv
* dtpsv
* dtrmm
* dtrmv
* dtrsm
* dtrsv
* dzasum
* dznrm2
* icamax
* idamax
* isamax
* izamax
* lsame
* sasum
* saxpy
* scasum
* scnrm2
* scopy
* sdot
* sdsdot
* sgbmv
* sgemm
* sgemv
* sger
* snrm2
* srot
* srotg
* srotm
* srotmg
* ssbmv
* sscal
* sspmv
* sspr
* sspr2
* sswap
* ssymm
* ssymv
* ssyr
* ssyr2
* ssyr2k
* ssyrk
* stbmv
* stbsv
* stpmv
* stpsv
* strmm
* strmv
* strsm
* strsv
* zaxpy
* zcopy
* zdotc
* zdotu
* zdrot
* zdscal
* zgbmv
* zgemm
* zgemv
* zgerc
* zgeru
* zhbmv
* zhemm
* zhemv
* zher
* zher2
* zher2k
* zherk
* zhpmv
* zhpr
* zhpr2
* zrotg
* zscal
* zswap
* zsymm
* zsyr2k
* zsyrk
* ztbmv
* ztbsv
* ztpmv
* ztpsv
* ztrmm
* ztrmv
* ztrsm
* ztrsv
[previous
scipy.linalg.blas.ztrsm](generated/scipy.linalg.blas.ztrsm.html "previous page")
[next
LAPACK functions for Cython](linalg.cython_lapack.html "next page")
On this page
* [ILP64 support](#ilp64-support)
* [`cython_blas` API](#cython-blas-api)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/linalg.lapack.html#module-scipy.linalg.lapack -->
* [SciPy API](index.html)
* [Linear algebra (`scipy.linalg`)](linalg.html)
* Low-level LAPACK functions (`scipy.linalg.lapack`)
# Low-level LAPACK functions ([`scipy.linalg.lapack`](#module-scipy.linalg.lapack "scipy.linalg.lapack"))[#](#low-level-lapack-functions-scipy-linalg-lapack "Link to this heading")
This module contains low-level functions from the LAPACK library.
Added in version 0.12.0.
Note
The common `overwrite_<>` option in many routines, allows the
input arrays to be overwritten to avoid extra memory allocation.
However this requires the array to satisfy two conditions
which are memory order and the data type to match exactly the
order and the type expected by the routine.
As an example, if you pass a double precision float array to any
`S....` routine which expects single precision arguments, f2py
will create an intermediate array to match the argument types and
overwriting will be performed on that intermediate array.
Similarly, if a C-contiguous array is passed, f2py will pass a
FORTRAN-contiguous array internally. Please make sure that these
details are satisfied. More information can be found in the f2py
documentation.
Warning
These functions do little to no error checking.
It is possible to cause crashes by mis-using them,
so prefer using the higher-level routines in [`scipy.linalg`](linalg.html#module-scipy.linalg "scipy.linalg").
Note
Prefer using `get_lapack_funcs` to importing the bare functions directly.
If you do, for example, `from scipy.linalg.lapack import dsysv`, the `dsysv`
function may be either LP64 or ILP64, depending on how SciPy is built.
The following is more robust:
```
>>> from scipy.linalg.lapack import get_lapack_funcs
>>> dsysv = get_lapack_funcs('sysv', dtype='float64', ilp64='preferred')
>>> dsysv.int_dtype
dtype('int32')    # may vary
```
## Finding functions[#](#finding-functions "Link to this heading")
|  |  |
| --- | --- |
| [`get_lapack_funcs`](generated/scipy.linalg.lapack.get_lapack_funcs.html#scipy.linalg.lapack.get_lapack_funcs "scipy.linalg.lapack.get_lapack_funcs")(names[,Â arrays,Â dtype,Â ilp64]) | Return available LAPACK function objects from names. |
## All functions[#](#all-functions "Link to this heading")
|  |  |
| --- | --- |
| [`sgbcon`](generated/scipy.linalg.lapack.sgbcon.html#scipy.linalg.lapack.sgbcon "scipy.linalg.lapack.sgbcon")(kl,ku,ab,ipiv,anorm,[norm,ldab]) | Wrapper for `sgbcon`. |
| [`dgbcon`](generated/scipy.linalg.lapack.dgbcon.html#scipy.linalg.lapack.dgbcon "scipy.linalg.lapack.dgbcon")(kl,ku,ab,ipiv,anorm,[norm,ldab]) | Wrapper for `dgbcon`. |
| [`cgbcon`](generated/scipy.linalg.lapack.cgbcon.html#scipy.linalg.lapack.cgbcon "scipy.linalg.lapack.cgbcon")(kl,ku,ab,ipiv,anorm,[norm,ldab]) | Wrapper for `cgbcon`. |
| [`zgbcon`](generated/scipy.linalg.lapack.zgbcon.html#scipy.linalg.lapack.zgbcon "scipy.linalg.lapack.zgbcon")(kl,ku,ab,ipiv,anorm,[norm,ldab]) | Wrapper for `zgbcon`. |
| [`sgbsv`](generated/scipy.linalg.lapack.sgbsv.html#scipy.linalg.lapack.sgbsv "scipy.linalg.lapack.sgbsv")(kl,ku,ab,b,[overwrite\_ab,overwrite\_b]) | Wrapper for `sgbsv`. |
| [`dgbsv`](generated/scipy.linalg.lapack.dgbsv.html#scipy.linalg.lapack.dgbsv "scipy.linalg.lapack.dgbsv")(kl,ku,ab,b,[overwrite\_ab,overwrite\_b]) | Wrapper for `dgbsv`. |
| [`cgbsv`](generated/scipy.linalg.lapack.cgbsv.html#scipy.linalg.lapack.cgbsv "scipy.linalg.lapack.cgbsv")(kl,ku,ab,b,[overwrite\_ab,overwrite\_b]) | Wrapper for `cgbsv`. |
| [`zgbsv`](generated/scipy.linalg.lapack.zgbsv.html#scipy.linalg.lapack.zgbsv "scipy.linalg.lapack.zgbsv")(kl,ku,ab,b,[overwrite\_ab,overwrite\_b]) | Wrapper for `zgbsv`. |
| [`sgbtrf`](generated/scipy.linalg.lapack.sgbtrf.html#scipy.linalg.lapack.sgbtrf "scipy.linalg.lapack.sgbtrf")(ab,kl,ku,[m,n,ldab,overwrite\_ab]) | Wrapper for `sgbtrf`. |
| [`dgbtrf`](generated/scipy.linalg.lapack.dgbtrf.html#scipy.linalg.lapack.dgbtrf "scipy.linalg.lapack.dgbtrf")(ab,kl,ku,[m,n,ldab,overwrite\_ab]) | Wrapper for `dgbtrf`. |
| [`cgbtrf`](generated/scipy.linalg.lapack.cgbtrf.html#scipy.linalg.lapack.cgbtrf "scipy.linalg.lapack.cgbtrf")(ab,kl,ku,[m,n,ldab,overwrite\_ab]) | Wrapper for `cgbtrf`. |
| [`zgbtrf`](generated/scipy.linalg.lapack.zgbtrf.html#scipy.linalg.lapack.zgbtrf "scipy.linalg.lapack.zgbtrf")(ab,kl,ku,[m,n,ldab,overwrite\_ab]) | Wrapper for `zgbtrf`. |
| [`sgbtrs`](generated/scipy.linalg.lapack.sgbtrs.html#scipy.linalg.lapack.sgbtrs "scipy.linalg.lapack.sgbtrs")(...) | Wrapper for `sgbtrs`. |
| [`dgbtrs`](generated/scipy.linalg.lapack.dgbtrs.html#scipy.linalg.lapack.dgbtrs "scipy.linalg.lapack.dgbtrs")(...) | Wrapper for `dgbtrs`. |
| [`cgbtrs`](generated/scipy.linalg.lapack.cgbtrs.html#scipy.linalg.lapack.cgbtrs "scipy.linalg.lapack.cgbtrs")(...) | Wrapper for `cgbtrs`. |
| [`zgbtrs`](generated/scipy.linalg.lapack.zgbtrs.html#scipy.linalg.lapack.zgbtrs "scipy.linalg.lapack.zgbtrs")(...) | Wrapper for `zgbtrs`. |
| [`sgebal`](generated/scipy.linalg.lapack.sgebal.html#scipy.linalg.lapack.sgebal "scipy.linalg.lapack.sgebal")(a,[scale,permute,overwrite\_a]) | Wrapper for `sgebal`. |
| [`dgebal`](generated/scipy.linalg.lapack.dgebal.html#scipy.linalg.lapack.dgebal "scipy.linalg.lapack.dgebal")(a,[scale,permute,overwrite\_a]) | Wrapper for `dgebal`. |
| [`cgebal`](generated/scipy.linalg.lapack.cgebal.html#scipy.linalg.lapack.cgebal "scipy.linalg.lapack.cgebal")(a,[scale,permute,overwrite\_a]) | Wrapper for `cgebal`. |
| [`zgebal`](generated/scipy.linalg.lapack.zgebal.html#scipy.linalg.lapack.zgebal "scipy.linalg.lapack.zgebal")(a,[scale,permute,overwrite\_a]) | Wrapper for `zgebal`. |
| [`sgecon`](generated/scipy.linalg.lapack.sgecon.html#scipy.linalg.lapack.sgecon "scipy.linalg.lapack.sgecon")(a,anorm,[norm]) | Wrapper for `sgecon`. |
| [`dgecon`](generated/scipy.linalg.lapack.dgecon.html#scipy.linalg.lapack.dgecon "scipy.linalg.lapack.dgecon")(a,anorm,[norm]) | Wrapper for `dgecon`. |
| [`cgecon`](generated/scipy.linalg.lapack.cgecon.html#scipy.linalg.lapack.cgecon "scipy.linalg.lapack.cgecon")(a,anorm,[norm]) | Wrapper for `cgecon`. |
| [`zgecon`](generated/scipy.linalg.lapack.zgecon.html#scipy.linalg.lapack.zgecon "scipy.linalg.lapack.zgecon")(a,anorm,[norm]) | Wrapper for `zgecon`. |
| [`sgeequ`](generated/scipy.linalg.lapack.sgeequ.html#scipy.linalg.lapack.sgeequ "scipy.linalg.lapack.sgeequ")(a) | Wrapper for `sgeequ`. |
| [`dgeequ`](generated/scipy.linalg.lapack.dgeequ.html#scipy.linalg.lapack.dgeequ "scipy.linalg.lapack.dgeequ")(a) | Wrapper for `dgeequ`. |
| [`cgeequ`](generated/scipy.linalg.lapack.cgeequ.html#scipy.linalg.lapack.cgeequ "scipy.linalg.lapack.cgeequ")(a) | Wrapper for `cgeequ`. |
| [`zgeequ`](generated/scipy.linalg.lapack.zgeequ.html#scipy.linalg.lapack.zgeequ "scipy.linalg.lapack.zgeequ")(a) | Wrapper for `zgeequ`. |
| [`sgeequb`](generated/scipy.linalg.lapack.sgeequb.html#scipy.linalg.lapack.sgeequb "scipy.linalg.lapack.sgeequb")(a) | Wrapper for `sgeequb`. |
| [`dgeequb`](generated/scipy.linalg.lapack.dgeequb.html#scipy.linalg.lapack.dgeequb "scipy.linalg.lapack.dgeequb")(a) | Wrapper for `dgeequb`. |
| [`cgeequb`](generated/scipy.linalg.lapack.cgeequb.html#scipy.linalg.lapack.cgeequb "scipy.linalg.lapack.cgeequb")(a) | Wrapper for `cgeequb`. |
| [`zgeequb`](generated/scipy.linalg.lapack.zgeequb.html#scipy.linalg.lapack.zgeequb "scipy.linalg.lapack.zgeequb")(a) | Wrapper for `zgeequb`. |
| [`sgees`](generated/scipy.linalg.lapack.sgees.html#scipy.linalg.lapack.sgees "scipy.linalg.lapack.sgees")(...) | Wrapper for `sgees`. |
| [`dgees`](generated/scipy.linalg.lapack.dgees.html#scipy.linalg.lapack.dgees "scipy.linalg.lapack.dgees")(...) | Wrapper for `dgees`. |
| [`cgees`](generated/scipy.linalg.lapack.cgees.html#scipy.linalg.lapack.cgees "scipy.linalg.lapack.cgees")(...) | Wrapper for `cgees`. |
| [`zgees`](generated/scipy.linalg.lapack.zgees.html#scipy.linalg.lapack.zgees "scipy.linalg.lapack.zgees")(...) | Wrapper for `zgees`. |
| [`sgeev`](generated/scipy.linalg.lapack.sgeev.html#scipy.linalg.lapack.sgeev "scipy.linalg.lapack.sgeev")(...) | Wrapper for `sgeev`. |
| [`dgeev`](generated/scipy.linalg.lapack.dgeev.html#scipy.linalg.lapack.dgeev "scipy.linalg.lapack.dgeev")(...) | Wrapper for `dgeev`. |
| [`cgeev`](generated/scipy.linalg.lapack.cgeev.html#scipy.linalg.lapack.cgeev "scipy.linalg.lapack.cgeev")(...) | Wrapper for `cgeev`. |
| [`zgeev`](generated/scipy.linalg.lapack.zgeev.html#scipy.linalg.lapack.zgeev "scipy.linalg.lapack.zgeev")(...) | Wrapper for `zgeev`. |
| [`sgeev_lwork`](generated/scipy.linalg.lapack.sgeev_lwork.html#scipy.linalg.lapack.sgeev_lwork "scipy.linalg.lapack.sgeev_lwork")(n,[compute\_vl,compute\_vr]) | Wrapper for `sgeev_lwork`. |
| [`dgeev_lwork`](generated/scipy.linalg.lapack.dgeev_lwork.html#scipy.linalg.lapack.dgeev_lwork "scipy.linalg.lapack.dgeev_lwork")(n,[compute\_vl,compute\_vr]) | Wrapper for `dgeev_lwork`. |
| [`cgeev_lwork`](generated/scipy.linalg.lapack.cgeev_lwork.html#scipy.linalg.lapack.cgeev_lwork "scipy.linalg.lapack.cgeev_lwork")(n,[compute\_vl,compute\_vr]) | Wrapper for `cgeev_lwork`. |
| [`zgeev_lwork`](generated/scipy.linalg.lapack.zgeev_lwork.html#scipy.linalg.lapack.zgeev_lwork "scipy.linalg.lapack.zgeev_lwork")(n,[compute\_vl,compute\_vr]) | Wrapper for `zgeev_lwork`. |
| [`sgehrd`](generated/scipy.linalg.lapack.sgehrd.html#scipy.linalg.lapack.sgehrd "scipy.linalg.lapack.sgehrd")(a,[lo,hi,lwork,overwrite\_a]) | Wrapper for `sgehrd`. |
| [`dgehrd`](generated/scipy.linalg.lapack.dgehrd.html#scipy.linalg.lapack.dgehrd "scipy.linalg.lapack.dgehrd")(a,[lo,hi,lwork,overwrite\_a]) | Wrapper for `dgehrd`. |
| [`cgehrd`](generated/scipy.linalg.lapack.cgehrd.html#scipy.linalg.lapack.cgehrd "scipy.linalg.lapack.cgehrd")(a,[lo,hi,lwork,overwrite\_a]) | Wrapper for `cgehrd`. |
| [`zgehrd`](generated/scipy.linalg.lapack.zgehrd.html#scipy.linalg.lapack.zgehrd "scipy.linalg.lapack.zgehrd")(a,[lo,hi,lwork,overwrite\_a]) | Wrapper for `zgehrd`. |
| [`sgehrd_lwork`](generated/scipy.linalg.lapack.sgehrd_lwork.html#scipy.linalg.lapack.sgehrd_lwork "scipy.linalg.lapack.sgehrd_lwork")(n,[lo,hi]) | Wrapper for `sgehrd_lwork`. |
| [`dgehrd_lwork`](generated/scipy.linalg.lapack.dgehrd_lwork.html#scipy.linalg.lapack.dgehrd_lwork "scipy.linalg.lapack.dgehrd_lwork")(n,[lo,hi]) | Wrapper for `dgehrd_lwork`. |
| [`cgehrd_lwork`](generated/scipy.linalg.lapack.cgehrd_lwork.html#scipy.linalg.lapack.cgehrd_lwork "scipy.linalg.lapack.cgehrd_lwork")(n,[lo,hi]) | Wrapper for `cgehrd_lwork`. |
| [`zgehrd_lwork`](generated/scipy.linalg.lapack.zgehrd_lwork.html#scipy.linalg.lapack.zgehrd_lwork "scipy.linalg.lapack.zgehrd_lwork")(n,[lo,hi]) | Wrapper for `zgehrd_lwork`. |
| [`sgejsv`](generated/scipy.linalg.lapack.sgejsv.html#scipy.linalg.lapack.sgejsv "scipy.linalg.lapack.sgejsv")(...) | Wrapper for `sgejsv`. |
| [`dgejsv`](generated/scipy.linalg.lapack.dgejsv.html#scipy.linalg.lapack.dgejsv "scipy.linalg.lapack.dgejsv")(...) | Wrapper for `dgejsv`. |
| [`sgels`](generated/scipy.linalg.lapack.sgels.html#scipy.linalg.lapack.sgels "scipy.linalg.lapack.sgels")(a,b,[trans,lwork,overwrite\_a,overwrite\_b]) | Wrapper for `sgels`. |
| [`dgels`](generated/scipy.linalg.lapack.dgels.html#scipy.linalg.lapack.dgels "scipy.linalg.lapack.dgels")(a,b,[trans,lwork,overwrite\_a,overwrite\_b]) | Wrapper for `dgels`. |
| [`cgels`](generated/scipy.linalg.lapack.cgels.html#scipy.linalg.lapack.cgels "scipy.linalg.lapack.cgels")(a,b,[trans,lwork,overwrite\_a,overwrite\_b]) | Wrapper for `cgels`. |
| [`zgels`](generated/scipy.linalg.lapack.zgels.html#scipy.linalg.lapack.zgels "scipy.linalg.lapack.zgels")(a,b,[trans,lwork,overwrite\_a,overwrite\_b]) | Wrapper for `zgels`. |
| [`sgels_lwork`](generated/scipy.linalg.lapack.sgels_lwork.html#scipy.linalg.lapack.sgels_lwork "scipy.linalg.lapack.sgels_lwork")(m,n,nrhs,[trans]) | Wrapper for `sgels_lwork`. |
| [`dgels_lwork`](generated/scipy.linalg.lapack.dgels_lwork.html#scipy.linalg.lapack.dgels_lwork "scipy.linalg.lapack.dgels_lwork")(m,n,nrhs,[trans]) | Wrapper for `dgels_lwork`. |
| [`cgels_lwork`](generated/scipy.linalg.lapack.cgels_lwork.html#scipy.linalg.lapack.cgels_lwork "scipy.linalg.lapack.cgels_lwork")(m,n,nrhs,[trans]) | Wrapper for `cgels_lwork`. |
| [`zgels_lwork`](generated/scipy.linalg.lapack.zgels_lwork.html#scipy.linalg.lapack.zgels_lwork "scipy.linalg.lapack.zgels_lwork")(m,n,nrhs,[trans]) | Wrapper for `zgels_lwork`. |
| [`sgelsd`](generated/scipy.linalg.lapack.sgelsd.html#scipy.linalg.lapack.sgelsd "scipy.linalg.lapack.sgelsd")(...) | Wrapper for `sgelsd`. |
| [`dgelsd`](generated/scipy.linalg.lapack.dgelsd.html#scipy.linalg.lapack.dgelsd "scipy.linalg.lapack.dgelsd")(...) | Wrapper for `dgelsd`. |
| [`cgelsd`](generated/scipy.linalg.lapack.cgelsd.html#scipy.linalg.lapack.cgelsd "scipy.linalg.lapack.cgelsd")(...) | Wrapper for `cgelsd`. |
| [`zgelsd`](generated/scipy.linalg.lapack.zgelsd.html#scipy.linalg.lapack.zgelsd "scipy.linalg.lapack.zgelsd")(...) | Wrapper for `zgelsd`. |
| [`sgelsd_lwork`](generated/scipy.linalg.lapack.sgelsd_lwork.html#scipy.linalg.lapack.sgelsd_lwork "scipy.linalg.lapack.sgelsd_lwork")(m,n,nrhs,[cond,lwork]) | Wrapper for `sgelsd_lwork`. |
| [`dgelsd_lwork`](generated/scipy.linalg.lapack.dgelsd_lwork.html#scipy.linalg.lapack.dgelsd_lwork "scipy.linalg.lapack.dgelsd_lwork")(m,n,nrhs,[cond,lwork]) | Wrapper for `dgelsd_lwork`. |
| [`cgelsd_lwork`](generated/scipy.linalg.lapack.cgelsd_lwork.html#scipy.linalg.lapack.cgelsd_lwork "scipy.linalg.lapack.cgelsd_lwork")(m,n,nrhs,[cond,lwork]) | Wrapper for `cgelsd_lwork`. |
| [`zgelsd_lwork`](generated/scipy.linalg.lapack.zgelsd_lwork.html#scipy.linalg.lapack.zgelsd_lwork "scipy.linalg.lapack.zgelsd_lwork")(m,n,nrhs,[cond,lwork]) | Wrapper for `zgelsd_lwork`. |
| [`sgelss`](generated/scipy.linalg.lapack.sgelss.html#scipy.linalg.lapack.sgelss "scipy.linalg.lapack.sgelss")(a,b,[cond,lwork,overwrite\_a,overwrite\_b]) | Wrapper for `sgelss`. |
| [`dgelss`](generated/scipy.linalg.lapack.dgelss.html#scipy.linalg.lapack.dgelss "scipy.linalg.lapack.dgelss")(a,b,[cond,lwork,overwrite\_a,overwrite\_b]) | Wrapper for `dgelss`. |
| [`cgelss`](generated/scipy.linalg.lapack.cgelss.html#scipy.linalg.lapack.cgelss "scipy.linalg.lapack.cgelss")(a,b,[cond,lwork,overwrite\_a,overwrite\_b]) | Wrapper for `cgelss`. |
| [`zgelss`](generated/scipy.linalg.lapack.zgelss.html#scipy.linalg.lapack.zgelss "scipy.linalg.lapack.zgelss")(a,b,[cond,lwork,overwrite\_a,overwrite\_b]) | Wrapper for `zgelss`. |
| [`sgelss_lwork`](generated/scipy.linalg.lapack.sgelss_lwork.html#scipy.linalg.lapack.sgelss_lwork "scipy.linalg.lapack.sgelss_lwork")(m,n,nrhs,[cond,lwork]) | Wrapper for `sgelss_lwork`. |
| [`dgelss_lwork`](generated/scipy.linalg.lapack.dgelss_lwork.html#scipy.linalg.lapack.dgelss_lwork "scipy.linalg.lapack.dgelss_lwork")(m,n,nrhs,[cond,lwork]) | Wrapper for `dgelss_lwork`. |
| [`cgelss_lwork`](generated/scipy.linalg.lapack.cgelss_lwork.html#scipy.linalg.lapack.cgelss_lwork "scipy.linalg.lapack.cgelss_lwork")(m,n,nrhs,[cond,lwork]) | Wrapper for `cgelss_lwork`. |
| [`zgelss_lwork`](generated/scipy.linalg.lapack.zgelss_lwork.html#scipy.linalg.lapack.zgelss_lwork "scipy.linalg.lapack.zgelss_lwork")(m,n,nrhs,[cond,lwork]) | Wrapper for `zgelss_lwork`. |
| [`sgelsy`](generated/scipy.linalg.lapack.sgelsy.html#scipy.linalg.lapack.sgelsy "scipy.linalg.lapack.sgelsy")(...) | Wrapper for `sgelsy`. |
| [`dgelsy`](generated/scipy.linalg.lapack.dgelsy.html#scipy.linalg.lapack.dgelsy "scipy.linalg.lapack.dgelsy")(...) | Wrapper for `dgelsy`. |
| [`cgelsy`](generated/scipy.linalg.lapack.cgelsy.html#scipy.linalg.lapack.cgelsy "scipy.linalg.lapack.cgelsy")(...) | Wrapper for `cgelsy`. |
| [`zgelsy`](generated/scipy.linalg.lapack.zgelsy.html#scipy.linalg.lapack.zgelsy "scipy.linalg.lapack.zgelsy")(...) | Wrapper for `zgelsy`. |
| [`sgelsy_lwork`](generated/scipy.linalg.lapack.sgelsy_lwork.html#scipy.linalg.lapack.sgelsy_lwork "scipy.linalg.lapack.sgelsy_lwork")(m,n,nrhs,cond,[lwork]) | Wrapper for `sgelsy_lwork`. |
| [`dgelsy_lwork`](generated/scipy.linalg.lapack.dgelsy_lwork.html#scipy.linalg.lapack.dgelsy_lwork "scipy.linalg.lapack.dgelsy_lwork")(m,n,nrhs,cond,[lwork]) | Wrapper for `dgelsy_lwork`. |
| [`cgelsy_lwork`](generated/scipy.linalg.lapack.cgelsy_lwork.html#scipy.linalg.lapack.cgelsy_lwork "scipy.linalg.lapack.cgelsy_lwork")(m,n,nrhs,cond,[lwork]) | Wrapper for `cgelsy_lwork`. |
| [`zgelsy_lwork`](generated/scipy.linalg.lapack.zgelsy_lwork.html#scipy.linalg.lapack.zgelsy_lwork "scipy.linalg.lapack.zgelsy_lwork")(m,n,nrhs,cond,[lwork]) | Wrapper for `zgelsy_lwork`. |
| [`sgeqp3`](generated/scipy.linalg.lapack.sgeqp3.html#scipy.linalg.lapack.sgeqp3 "scipy.linalg.lapack.sgeqp3")(a,[lwork,overwrite\_a]) | Wrapper for `sgeqp3`. |
| [`dgeqp3`](generated/scipy.linalg.lapack.dgeqp3.html#scipy.linalg.lapack.dgeqp3 "scipy.linalg.lapack.dgeqp3")(a,[lwork,overwrite\_a]) | Wrapper for `dgeqp3`. |
| [`cgeqp3`](generated/scipy.linalg.lapack.cgeqp3.html#scipy.linalg.lapack.cgeqp3 "scipy.linalg.lapack.cgeqp3")(a,[lwork,overwrite\_a]) | Wrapper for `cgeqp3`. |
| [`zgeqp3`](generated/scipy.linalg.lapack.zgeqp3.html#scipy.linalg.lapack.zgeqp3 "scipy.linalg.lapack.zgeqp3")(a,[lwork,overwrite\_a]) | Wrapper for `zgeqp3`. |
| [`sgeqrf`](generated/scipy.linalg.lapack.sgeqrf.html#scipy.linalg.lapack.sgeqrf "scipy.linalg.lapack.sgeqrf")(a,[lwork,overwrite\_a]) | Wrapper for `sgeqrf`. |
| [`dgeqrf`](generated/scipy.linalg.lapack.dgeqrf.html#scipy.linalg.lapack.dgeqrf "scipy.linalg.lapack.dgeqrf")(a,[lwork,overwrite\_a]) | Wrapper for `dgeqrf`. |
| [`cgeqrf`](generated/scipy.linalg.lapack.cgeqrf.html#scipy.linalg.lapack.cgeqrf "scipy.linalg.lapack.cgeqrf")(a,[lwork,overwrite\_a]) | Wrapper for `cgeqrf`. |
| [`zgeqrf`](generated/scipy.linalg.lapack.zgeqrf.html#scipy.linalg.lapack.zgeqrf "scipy.linalg.lapack.zgeqrf")(a,[lwork,overwrite\_a]) | Wrapper for `zgeqrf`. |
| [`sgeqrf_lwork`](generated/scipy.linalg.lapack.sgeqrf_lwork.html#scipy.linalg.lapack.sgeqrf_lwork "scipy.linalg.lapack.sgeqrf_lwork")(m,Â n) | Wrapper for `sgeqrf_lwork`. |
| [`dgeqrf_lwork`](generated/scipy.linalg.lapack.dgeqrf_lwork.html#scipy.linalg.lapack.dgeqrf_lwork "scipy.linalg.lapack.dgeqrf_lwork")(m,Â n) | Wrapper for `dgeqrf_lwork`. |
| [`cgeqrf_lwork`](generated/scipy.linalg.lapack.cgeqrf_lwork.html#scipy.linalg.lapack.cgeqrf_lwork "scipy.linalg.lapack.cgeqrf_lwork")(m,Â n) | Wrapper for `cgeqrf_lwork`. |
| [`zgeqrf_lwork`](generated/scipy.linalg.lapack.zgeqrf_lwork.html#scipy.linalg.lapack.zgeqrf_lwork "scipy.linalg.lapack.zgeqrf_lwork")(m,Â n) | Wrapper for `zgeqrf_lwork`. |
| [`sgeqrfp`](generated/scipy.linalg.lapack.sgeqrfp.html#scipy.linalg.lapack.sgeqrfp "scipy.linalg.lapack.sgeqrfp")(a,[lwork,overwrite\_a]) | Wrapper for `sgeqrfp`. |
| [`dgeqrfp`](generated/scipy.linalg.lapack.dgeqrfp.html#scipy.linalg.lapack.dgeqrfp "scipy.linalg.lapack.dgeqrfp")(a,[lwork,overwrite\_a]) | Wrapper for `dgeqrfp`. |
| [`cgeqrfp`](generated/scipy.linalg.lapack.cgeqrfp.html#scipy.linalg.lapack.cgeqrfp "scipy.linalg.lapack.cgeqrfp")(a,[lwork,overwrite\_a]) | Wrapper for `cgeqrfp`. |
| [`zgeqrfp`](generated/scipy.linalg.lapack.zgeqrfp.html#scipy.linalg.lapack.zgeqrfp "scipy.linalg.lapack.zgeqrfp")(a,[lwork,overwrite\_a]) | Wrapper for `zgeqrfp`. |
| [`sgeqrfp_lwork`](generated/scipy.linalg.lapack.sgeqrfp_lwork.html#scipy.linalg.lapack.sgeqrfp_lwork "scipy.linalg.lapack.sgeqrfp_lwork")(m,Â n) | Wrapper for `sgeqrfp_lwork`. |
| [`dgeqrfp_lwork`](generated/scipy.linalg.lapack.dgeqrfp_lwork.html#scipy.linalg.lapack.dgeqrfp_lwork "scipy.linalg.lapack.dgeqrfp_lwork")(m,Â n) | Wrapper for `dgeqrfp_lwork`. |
| [`cgeqrfp_lwork`](generated/scipy.linalg.lapack.cgeqrfp_lwork.html#scipy.linalg.lapack.cgeqrfp_lwork "scipy.linalg.lapack.cgeqrfp_lwork")(m,Â n) | Wrapper for `cgeqrfp_lwork`. |
| [`zgeqrfp_lwork`](generated/scipy.linalg.lapack.zgeqrfp_lwork.html#scipy.linalg.lapack.zgeqrfp_lwork "scipy.linalg.lapack.zgeqrfp_lwork")(m,Â n) | Wrapper for `zgeqrfp_lwork`. |
| [`sgerqf`](generated/scipy.linalg.lapack.sgerqf.html#scipy.linalg.lapack.sgerqf "scipy.linalg.lapack.sgerqf")(a,[lwork,overwrite\_a]) | Wrapper for `sgerqf`. |
| [`dgerqf`](generated/scipy.linalg.lapack.dgerqf.html#scipy.linalg.lapack.dgerqf "scipy.linalg.lapack.dgerqf")(a,[lwork,overwrite\_a]) | Wrapper for `dgerqf`. |
| [`cgerqf`](generated/scipy.linalg.lapack.cgerqf.html#scipy.linalg.lapack.cgerqf "scipy.linalg.lapack.cgerqf")(a,[lwork,overwrite\_a]) | Wrapper for `cgerqf`. |
| [`zgerqf`](generated/scipy.linalg.lapack.zgerqf.html#scipy.linalg.lapack.zgerqf "scipy.linalg.lapack.zgerqf")(a,[lwork,overwrite\_a]) | Wrapper for `zgerqf`. |
| [`sgesdd`](generated/scipy.linalg.lapack.sgesdd.html#scipy.linalg.lapack.sgesdd "scipy.linalg.lapack.sgesdd")(...) | Wrapper for `sgesdd`. |
| [`dgesdd`](generated/scipy.linalg.lapack.dgesdd.html#scipy.linalg.lapack.dgesdd "scipy.linalg.lapack.dgesdd")(...) | Wrapper for `dgesdd`. |
| [`cgesdd`](generated/scipy.linalg.lapack.cgesdd.html#scipy.linalg.lapack.cgesdd "scipy.linalg.lapack.cgesdd")(...) | Wrapper for `cgesdd`. |
| [`zgesdd`](generated/scipy.linalg.lapack.zgesdd.html#scipy.linalg.lapack.zgesdd "scipy.linalg.lapack.zgesdd")(...) | Wrapper for `zgesdd`. |
| [`sgesdd_lwork`](generated/scipy.linalg.lapack.sgesdd_lwork.html#scipy.linalg.lapack.sgesdd_lwork "scipy.linalg.lapack.sgesdd_lwork")(m,n,[compute\_uv,full\_matrices]) | Wrapper for `sgesdd_lwork`. |
| [`dgesdd_lwork`](generated/scipy.linalg.lapack.dgesdd_lwork.html#scipy.linalg.lapack.dgesdd_lwork "scipy.linalg.lapack.dgesdd_lwork")(m,n,[compute\_uv,full\_matrices]) | Wrapper for `dgesdd_lwork`. |
| [`cgesdd_lwork`](generated/scipy.linalg.lapack.cgesdd_lwork.html#scipy.linalg.lapack.cgesdd_lwork "scipy.linalg.lapack.cgesdd_lwork")(m,n,[compute\_uv,full\_matrices]) | Wrapper for `cgesdd_lwork`. |
| [`zgesdd_lwork`](generated/scipy.linalg.lapack.zgesdd_lwork.html#scipy.linalg.lapack.zgesdd_lwork "scipy.linalg.lapack.zgesdd_lwork")(m,n,[compute\_uv,full\_matrices]) | Wrapper for `zgesdd_lwork`. |
| [`sgesv`](generated/scipy.linalg.lapack.sgesv.html#scipy.linalg.lapack.sgesv "scipy.linalg.lapack.sgesv")(a,b,[overwrite\_a,overwrite\_b]) | Wrapper for `sgesv`. |
| [`dgesv`](generated/scipy.linalg.lapack.dgesv.html#scipy.linalg.lapack.dgesv "scipy.linalg.lapack.dgesv")(a,b,[overwrite\_a,overwrite\_b]) | Wrapper for `dgesv`. |
| [`cgesv`](generated/scipy.linalg.lapack.cgesv.html#scipy.linalg.lapack.cgesv "scipy.linalg.lapack.cgesv")(a,b,[overwrite\_a,overwrite\_b]) | Wrapper for `cgesv`. |
| [`zgesv`](generated/scipy.linalg.lapack.zgesv.html#scipy.linalg.lapack.zgesv "scipy.linalg.lapack.zgesv")(a,b,[overwrite\_a,overwrite\_b]) | Wrapper for `zgesv`. |
| [`sgesvd`](generated/scipy.linalg.lapack.sgesvd.html#scipy.linalg.lapack.sgesvd "scipy.linalg.lapack.sgesvd")(...) | Wrapper for `sgesvd`. |
| [`dgesvd`](generated/scipy.linalg.lapack.dgesvd.html#scipy.linalg.lapack.dgesvd "scipy.linalg.lapack.dgesvd")(...) | Wrapper for `dgesvd`. |
| [`cgesvd`](generated/scipy.linalg.lapack.cgesvd.html#scipy.linalg.lapack.cgesvd "scipy.linalg.lapack.cgesvd")(...) | Wrapper for `cgesvd`. |
| [`zgesvd`](generated/scipy.linalg.lapack.zgesvd.html#scipy.linalg.lapack.zgesvd "scipy.linalg.lapack.zgesvd")(...) | Wrapper for `zgesvd`. |
| [`sgesvd_lwork`](generated/scipy.linalg.lapack.sgesvd_lwork.html#scipy.linalg.lapack.sgesvd_lwork "scipy.linalg.lapack.sgesvd_lwork")(m,n,[compute\_uv,full\_matrices]) | Wrapper for `sgesvd_lwork`. |
| [`dgesvd_lwork`](generated/scipy.linalg.lapack.dgesvd_lwork.html#scipy.linalg.lapack.dgesvd_lwork "scipy.linalg.lapack.dgesvd_lwork")(m,n,[compute\_uv,full\_matrices]) | Wrapper for `dgesvd_lwork`. |
| [`cgesvd_lwork`](generated/scipy.linalg.lapack.cgesvd_lwork.html#scipy.linalg.lapack.cgesvd_lwork "scipy.linalg.lapack.cgesvd_lwork")(m,n,[compute\_uv,full\_matrices]) | Wrapper for `cgesvd_lwork`. |
| [`zgesvd_lwork`](generated/scipy.linalg.lapack.zgesvd_lwork.html#scipy.linalg.lapack.zgesvd_lwork "scipy.linalg.lapack.zgesvd_lwork")(m,n,[compute\_uv,full\_matrices]) | Wrapper for `zgesvd_lwork`. |
| [`sgesvx`](generated/scipy.linalg.lapack.sgesvx.html#scipy.linalg.lapack.sgesvx "scipy.linalg.lapack.sgesvx")(...) | Wrapper for `sgesvx`. |
| [`dgesvx`](generated/scipy.linalg.lapack.dgesvx.html#scipy.linalg.lapack.dgesvx "scipy.linalg.lapack.dgesvx")(...) | Wrapper for `dgesvx`. |
| [`cgesvx`](generated/scipy.linalg.lapack.cgesvx.html#scipy.linalg.lapack.cgesvx "scipy.linalg.lapack.cgesvx")(...) | Wrapper for `cgesvx`. |
| [`zgesvx`](generated/scipy.linalg.lapack.zgesvx.html#scipy.linalg.lapack.zgesvx "scipy.linalg.lapack.zgesvx")(...) | Wrapper for `zgesvx`. |
| [`sgetrf`](generated/scipy.linalg.lapack.sgetrf.html#scipy.linalg.lapack.sgetrf "scipy.linalg.lapack.sgetrf")(a,[overwrite\_a]) | Wrapper for `sgetrf`. |
| [`dgetrf`](generated/scipy.linalg.lapack.dgetrf.html#scipy.linalg.lapack.dgetrf "scipy.linalg.lapack.dgetrf")(a,[overwrite\_a]) | Wrapper for `dgetrf`. |
| [`cgetrf`](generated/scipy.linalg.lapack.cgetrf.html#scipy.linalg.lapack.cgetrf "scipy.linalg.lapack.cgetrf")(a,[overwrite\_a]) | Wrapper for `cgetrf`. |
| [`zgetrf`](generated/scipy.linalg.lapack.zgetrf.html#scipy.linalg.lapack.zgetrf "scipy.linalg.lapack.zgetrf")(a,[overwrite\_a]) | Wrapper for `zgetrf`. |
| [`sgetc2`](generated/scipy.linalg.lapack.sgetc2.html#scipy.linalg.lapack.sgetc2 "scipy.linalg.lapack.sgetc2")(a,[overwrite\_a]) | Wrapper for `sgetc2`. |
| [`dgetc2`](generated/scipy.linalg.lapack.dgetc2.html#scipy.linalg.lapack.dgetc2 "scipy.linalg.lapack.dgetc2")(a,[overwrite\_a]) | Wrapper for `dgetc2`. |
| [`cgetc2`](generated/scipy.linalg.lapack.cgetc2.html#scipy.linalg.lapack.cgetc2 "scipy.linalg.lapack.cgetc2")(a,[overwrite\_a]) | Wrapper for `cgetc2`. |
| [`zgetc2`](generated/scipy.linalg.lapack.zgetc2.html#scipy.linalg.lapack.zgetc2 "scipy.linalg.lapack.zgetc2")(a,[overwrite\_a]) | Wrapper for `zgetc2`. |
| [`sgetri`](generated/scipy.linalg.lapack.sgetri.html#scipy.linalg.lapack.sgetri "scipy.linalg.lapack.sgetri")(lu,piv,[lwork,overwrite\_lu]) | Wrapper for `sgetri`. |
| [`dgetri`](generated/scipy.linalg.lapack.dgetri.html#scipy.linalg.lapack.dgetri "scipy.linalg.lapack.dgetri")(lu,piv,[lwork,overwrite\_lu]) | Wrapper for `dgetri`. |
| [`cgetri`](generated/scipy.linalg.lapack.cgetri.html#scipy.linalg.lapack.cgetri "scipy.linalg.lapack.cgetri")(lu,piv,[lwork,overwrite\_lu]) | Wrapper for `cgetri`. |
| [`zgetri`](generated/scipy.linalg.lapack.zgetri.html#scipy.linalg.lapack.zgetri "scipy.linalg.lapack.zgetri")(lu,piv,[lwork,overwrite\_lu]) | Wrapper for `zgetri`. |
| [`sgetri_lwork`](generated/scipy.linalg.lapack.sgetri_lwork.html#scipy.linalg.lapack.sgetri_lwork "scipy.linalg.lapack.sgetri_lwork")(n) | Wrapper for `sgetri_lwork`. |
| [`dgetri_lwork`](generated/scipy.linalg.lapack.dgetri_lwork.html#scipy.linalg.lapack.dgetri_lwork "scipy.linalg.lapack.dgetri_lwork")(n) | Wrapper for `dgetri_lwork`. |
| [`cgetri_lwork`](generated/scipy.linalg.lapack.cgetri_lwork.html#scipy.linalg.lapack.cgetri_lwork "scipy.linalg.lapack.cgetri_lwork")(n) | Wrapper for `cgetri_lwork`. |
| [`zgetri_lwork`](generated/scipy.linalg.lapack.zgetri_lwork.html#scipy.linalg.lapack.zgetri_lwork "scipy.linalg.lapack.zgetri_lwork")(n) | Wrapper for `zgetri_lwork`. |
| [`sgetrs`](generated/scipy.linalg.lapack.sgetrs.html#scipy.linalg.lapack.sgetrs "scipy.linalg.lapack.sgetrs")(lu,piv,b,[trans,overwrite\_b]) | Wrapper for `sgetrs`. |
| [`dgetrs`](generated/scipy.linalg.lapack.dgetrs.html#scipy.linalg.lapack.dgetrs "scipy.linalg.lapack.dgetrs")(lu,piv,b,[trans,overwrite\_b]) | Wrapper for `dgetrs`. |
| [`cgetrs`](generated/scipy.linalg.lapack.cgetrs.html#scipy.linalg.lapack.cgetrs "scipy.linalg.lapack.cgetrs")(lu,piv,b,[trans,overwrite\_b]) | Wrapper for `cgetrs`. |
| [`zgetrs`](generated/scipy.linalg.lapack.zgetrs.html#scipy.linalg.lapack.zgetrs "scipy.linalg.lapack.zgetrs")(lu,piv,b,[trans,overwrite\_b]) | Wrapper for `zgetrs`. |
| [`sgesc2`](generated/scipy.linalg.lapack.sgesc2.html#scipy.linalg.lapack.sgesc2 "scipy.linalg.lapack.sgesc2")(lu,rhs,ipiv,jpiv,[overwrite\_rhs]) | Wrapper for `sgesc2`. |
| [`dgesc2`](generated/scipy.linalg.lapack.dgesc2.html#scipy.linalg.lapack.dgesc2 "scipy.linalg.lapack.dgesc2")(lu,rhs,ipiv,jpiv,[overwrite\_rhs]) | Wrapper for `dgesc2`. |
| [`cgesc2`](generated/scipy.linalg.lapack.cgesc2.html#scipy.linalg.lapack.cgesc2 "scipy.linalg.lapack.cgesc2")(lu,rhs,ipiv,jpiv,[overwrite\_rhs]) | Wrapper for `cgesc2`. |
| [`zgesc2`](generated/scipy.linalg.lapack.zgesc2.html#scipy.linalg.lapack.zgesc2 "scipy.linalg.lapack.zgesc2")(lu,rhs,ipiv,jpiv,[overwrite\_rhs]) | Wrapper for `zgesc2`. |
| [`sgges`](generated/scipy.linalg.lapack.sgges.html#scipy.linalg.lapack.sgges "scipy.linalg.lapack.sgges")(...) | Wrapper for `sgges`. |
| [`dgges`](generated/scipy.linalg.lapack.dgges.html#scipy.linalg.lapack.dgges "scipy.linalg.lapack.dgges")(...) | Wrapper for `dgges`. |
| [`cgges`](generated/scipy.linalg.lapack.cgges.html#scipy.linalg.lapack.cgges "scipy.linalg.lapack.cgges")(...) | Wrapper for `cgges`. |
| [`zgges`](generated/scipy.linalg.lapack.zgges.html#scipy.linalg.lapack.zgges "scipy.linalg.lapack.zgges")(...) | Wrapper for `zgges`. |
| [`sggev`](generated/scipy.linalg.lapack.sggev.html#scipy.linalg.lapack.sggev "scipy.linalg.lapack.sggev")(...) | Wrapper for `sggev`. |
| [`dggev`](generated/scipy.linalg.lapack.dggev.html#scipy.linalg.lapack.dggev "scipy.linalg.lapack.dggev")(...) | Wrapper for `dggev`. |
| [`cggev`](generated/scipy.linalg.lapack.cggev.html#scipy.linalg.lapack.cggev "scipy.linalg.lapack.cggev")(...) | Wrapper for `cggev`. |
| [`zggev`](generated/scipy.linalg.lapack.zggev.html#scipy.linalg.lapack.zggev "scipy.linalg.lapack.zggev")(...) | Wrapper for `zggev`. |
| [`sgglse`](generated/scipy.linalg.lapack.sgglse.html#scipy.linalg.lapack.sgglse "scipy.linalg.lapack.sgglse")(...) | Wrapper for `sgglse`. |
| [`dgglse`](generated/scipy.linalg.lapack.dgglse.html#scipy.linalg.lapack.dgglse "scipy.linalg.lapack.dgglse")(...) | Wrapper for `dgglse`. |
| [`cgglse`](generated/scipy.linalg.lapack.cgglse.html#scipy.linalg.lapack.cgglse "scipy.linalg.lapack.cgglse")(...) | Wrapper for `cgglse`. |
| [`zgglse`](generated/scipy.linalg.lapack.zgglse.html#scipy.linalg.lapack.zgglse "scipy.linalg.lapack.zgglse")(...) | Wrapper for `zgglse`. |
| [`sgglse_lwork`](generated/scipy.linalg.lapack.sgglse_lwork.html#scipy.linalg.lapack.sgglse_lwork "scipy.linalg.lapack.sgglse_lwork")(m,Â n,Â p) | Wrapper for `sgglse_lwork`. |
| [`dgglse_lwork`](generated/scipy.linalg.lapack.dgglse_lwork.html#scipy.linalg.lapack.dgglse_lwork "scipy.linalg.lapack.dgglse_lwork")(m,Â n,Â p) | Wrapper for `dgglse_lwork`. |
| [`cgglse_lwork`](generated/scipy.linalg.lapack.cgglse_lwork.html#scipy.linalg.lapack.cgglse_lwork "scipy.linalg.lapack.cgglse_lwork")(m,Â n,Â p) | Wrapper for `cgglse_lwork`. |
| [`zgglse_lwork`](generated/scipy.linalg.lapack.zgglse_lwork.html#scipy.linalg.lapack.zgglse_lwork "scipy.linalg.lapack.zgglse_lwork")(m,Â n,Â p) | Wrapper for `zgglse_lwork`. |
| [`sgtsv`](generated/scipy.linalg.lapack.sgtsv.html#scipy.linalg.lapack.sgtsv "scipy.linalg.lapack.sgtsv")(...) | Wrapper for `sgtsv`. |
| [`dgtsv`](generated/scipy.linalg.lapack.dgtsv.html#scipy.linalg.lapack.dgtsv "scipy.linalg.lapack.dgtsv")(...) | Wrapper for `dgtsv`. |
| [`cgtsv`](generated/scipy.linalg.lapack.cgtsv.html#scipy.linalg.lapack.cgtsv "scipy.linalg.lapack.cgtsv")(...) | Wrapper for `cgtsv`. |
| [`zgtsv`](generated/scipy.linalg.lapack.zgtsv.html#scipy.linalg.lapack.zgtsv "scipy.linalg.lapack.zgtsv")(...) | Wrapper for `zgtsv`. |
| [`sgtsvx`](generated/scipy.linalg.lapack.sgtsvx.html#scipy.linalg.lapack.sgtsvx "scipy.linalg.lapack.sgtsvx")(...) | Wrapper for `sgtsvx`. |
| [`dgtsvx`](generated/scipy.linalg.lapack.dgtsvx.html#scipy.linalg.lapack.dgtsvx "scipy.linalg.lapack.dgtsvx")(...) | Wrapper for `dgtsvx`. |
| [`cgtsvx`](generated/scipy.linalg.lapack.cgtsvx.html#scipy.linalg.lapack.cgtsvx "scipy.linalg.lapack.cgtsvx")(...) | Wrapper for `cgtsvx`. |
| [`zgtsvx`](generated/scipy.linalg.lapack.zgtsvx.html#scipy.linalg.lapack.zgtsvx "scipy.linalg.lapack.zgtsvx")(...) | Wrapper for `zgtsvx`. |
| [`chbevd`](generated/scipy.linalg.lapack.chbevd.html#scipy.linalg.lapack.chbevd "scipy.linalg.lapack.chbevd")(...) | Wrapper for `chbevd`. |
| [`zhbevd`](generated/scipy.linalg.lapack.zhbevd.html#scipy.linalg.lapack.zhbevd "scipy.linalg.lapack.zhbevd")(...) | Wrapper for `zhbevd`. |
| [`chbevx`](generated/scipy.linalg.lapack.chbevx.html#scipy.linalg.lapack.chbevx "scipy.linalg.lapack.chbevx")(...) | Wrapper for `chbevx`. |
| [`zhbevx`](generated/scipy.linalg.lapack.zhbevx.html#scipy.linalg.lapack.zhbevx "scipy.linalg.lapack.zhbevx")(...) | Wrapper for `zhbevx`. |
| [`checon`](generated/scipy.linalg.lapack.checon.html#scipy.linalg.lapack.checon "scipy.linalg.lapack.checon")(a,ipiv,anorm,[lower]) | Wrapper for `checon`. |
| [`zhecon`](generated/scipy.linalg.lapack.zhecon.html#scipy.linalg.lapack.zhecon "scipy.linalg.lapack.zhecon")(a,ipiv,anorm,[lower]) | Wrapper for `zhecon`. |
| [`cheequb`](generated/scipy.linalg.lapack.cheequb.html#scipy.linalg.lapack.cheequb "scipy.linalg.lapack.cheequb")(a,[lower]) | Wrapper for `cheequb`. |
| [`zheequb`](generated/scipy.linalg.lapack.zheequb.html#scipy.linalg.lapack.zheequb "scipy.linalg.lapack.zheequb")(a,[lower]) | Wrapper for `zheequb`. |
| [`cheev`](generated/scipy.linalg.lapack.cheev.html#scipy.linalg.lapack.cheev "scipy.linalg.lapack.cheev")(a,[compute\_v,lower,lwork,overwrite\_a]) | Wrapper for `cheev`. |
| [`zheev`](generated/scipy.linalg.lapack.zheev.html#scipy.linalg.lapack.zheev "scipy.linalg.lapack.zheev")(a,[compute\_v,lower,lwork,overwrite\_a]) | Wrapper for `zheev`. |
| [`cheev_lwork`](generated/scipy.linalg.lapack.cheev_lwork.html#scipy.linalg.lapack.cheev_lwork "scipy.linalg.lapack.cheev_lwork")(n,[lower]) | Wrapper for `cheev_lwork`. |
| [`zheev_lwork`](generated/scipy.linalg.lapack.zheev_lwork.html#scipy.linalg.lapack.zheev_lwork "scipy.linalg.lapack.zheev_lwork")(n,[lower]) | Wrapper for `zheev_lwork`. |
| [`cheevd`](generated/scipy.linalg.lapack.cheevd.html#scipy.linalg.lapack.cheevd "scipy.linalg.lapack.cheevd")(...) | Wrapper for `cheevd`. |
| [`zheevd`](generated/scipy.linalg.lapack.zheevd.html#scipy.linalg.lapack.zheevd "scipy.linalg.lapack.zheevd")(...) | Wrapper for `zheevd`. |
| [`cheevd_lwork`](generated/scipy.linalg.lapack.cheevd_lwork.html#scipy.linalg.lapack.cheevd_lwork "scipy.linalg.lapack.cheevd_lwork")(n,[compute\_v,lower]) | Wrapper for `cheevd_lwork`. |
| [`zheevd_lwork`](generated/scipy.linalg.lapack.zheevd_lwork.html#scipy.linalg.lapack.zheevd_lwork "scipy.linalg.lapack.zheevd_lwork")(n,[compute\_v,lower]) | Wrapper for `zheevd_lwork`. |
| [`cheevr`](generated/scipy.linalg.lapack.cheevr.html#scipy.linalg.lapack.cheevr "scipy.linalg.lapack.cheevr")(...) | Wrapper for `cheevr`. |
| [`zheevr`](generated/scipy.linalg.lapack.zheevr.html#scipy.linalg.lapack.zheevr "scipy.linalg.lapack.zheevr")(...) | Wrapper for `zheevr`. |
| [`cheevr_lwork`](generated/scipy.linalg.lapack.cheevr_lwork.html#scipy.linalg.lapack.cheevr_lwork "scipy.linalg.lapack.cheevr_lwork")(n,[lower]) | Wrapper for `cheevr_lwork`. |
| [`zheevr_lwork`](generated/scipy.linalg.lapack.zheevr_lwork.html#scipy.linalg.lapack.zheevr_lwork "scipy.linalg.lapack.zheevr_lwork")(n,[lower]) | Wrapper for `zheevr_lwork`. |
| [`cheevx`](generated/scipy.linalg.lapack.cheevx.html#scipy.linalg.lapack.cheevx "scipy.linalg.lapack.cheevx")(...) | Wrapper for `cheevx`. |
| [`zheevx`](generated/scipy.linalg.lapack.zheevx.html#scipy.linalg.lapack.zheevx "scipy.linalg.lapack.zheevx")(...) | Wrapper for `zheevx`. |
| [`cheevx_lwork`](generated/scipy.linalg.lapack.cheevx_lwork.html#scipy.linalg.lapack.cheevx_lwork "scipy.linalg.lapack.cheevx_lwork")(n,[lower]) | Wrapper for `cheevx_lwork`. |
| [`zheevx_lwork`](generated/scipy.linalg.lapack.zheevx_lwork.html#scipy.linalg.lapack.zheevx_lwork "scipy.linalg.lapack.zheevx_lwork")(n,[lower]) | Wrapper for `zheevx_lwork`. |
| [`chegst`](generated/scipy.linalg.lapack.chegst.html#scipy.linalg.lapack.chegst "scipy.linalg.lapack.chegst")(a,b,[itype,lower,overwrite\_a]) | Wrapper for `chegst`. |
| [`zhegst`](generated/scipy.linalg.lapack.zhegst.html#scipy.linalg.lapack.zhegst "scipy.linalg.lapack.zhegst")(a,b,[itype,lower,overwrite\_a]) | Wrapper for `zhegst`. |
| [`chegv`](generated/scipy.linalg.lapack.chegv.html#scipy.linalg.lapack.chegv "scipy.linalg.lapack.chegv")(...) | Wrapper for `chegv`. |
| [`zhegv`](generated/scipy.linalg.lapack.zhegv.html#scipy.linalg.lapack.zhegv "scipy.linalg.lapack.zhegv")(...) | Wrapper for `zhegv`. |
| [`chegv_lwork`](generated/scipy.linalg.lapack.chegv_lwork.html#scipy.linalg.lapack.chegv_lwork "scipy.linalg.lapack.chegv_lwork")(n,[uplo]) | Wrapper for `chegv_lwork`. |
| [`zhegv_lwork`](generated/scipy.linalg.lapack.zhegv_lwork.html#scipy.linalg.lapack.zhegv_lwork "scipy.linalg.lapack.zhegv_lwork")(n,[uplo]) | Wrapper for `zhegv_lwork`. |
| [`chegvd`](generated/scipy.linalg.lapack.chegvd.html#scipy.linalg.lapack.chegvd "scipy.linalg.lapack.chegvd")(...) | Wrapper for `chegvd`. |
| [`zhegvd`](generated/scipy.linalg.lapack.zhegvd.html#scipy.linalg.lapack.zhegvd "scipy.linalg.lapack.zhegvd")(...) | Wrapper for `zhegvd`. |
| [`chegvx`](generated/scipy.linalg.lapack.chegvx.html#scipy.linalg.lapack.chegvx "scipy.linalg.lapack.chegvx")(...) | Wrapper for `chegvx`. |
| [`zhegvx`](generated/scipy.linalg.lapack.zhegvx.html#scipy.linalg.lapack.zhegvx "scipy.linalg.lapack.zhegvx")(...) | Wrapper for `zhegvx`. |
| [`chegvx_lwork`](generated/scipy.linalg.lapack.chegvx_lwork.html#scipy.linalg.lapack.chegvx_lwork "scipy.linalg.lapack.chegvx_lwork")(n,[uplo]) | Wrapper for `chegvx_lwork`. |
| [`zhegvx_lwork`](generated/scipy.linalg.lapack.zhegvx_lwork.html#scipy.linalg.lapack.zhegvx_lwork "scipy.linalg.lapack.zhegvx_lwork")(n,[uplo]) | Wrapper for `zhegvx_lwork`. |
| [`chesv`](generated/scipy.linalg.lapack.chesv.html#scipy.linalg.lapack.chesv "scipy.linalg.lapack.chesv")(a,b,[lwork,lower,overwrite\_a,overwrite\_b]) | Wrapper for `chesv`. |
| [`zhesv`](generated/scipy.linalg.lapack.zhesv.html#scipy.linalg.lapack.zhesv "scipy.linalg.lapack.zhesv")(a,b,[lwork,lower,overwrite\_a,overwrite\_b]) | Wrapper for `zhesv`. |
| [`chesv_lwork`](generated/scipy.linalg.lapack.chesv_lwork.html#scipy.linalg.lapack.chesv_lwork "scipy.linalg.lapack.chesv_lwork")(n,[lower]) | Wrapper for `chesv_lwork`. |
| [`zhesv_lwork`](generated/scipy.linalg.lapack.zhesv_lwork.html#scipy.linalg.lapack.zhesv_lwork "scipy.linalg.lapack.zhesv_lwork")(n,[lower]) | Wrapper for `zhesv_lwork`. |
| [`chesvx`](generated/scipy.linalg.lapack.chesvx.html#scipy.linalg.lapack.chesvx "scipy.linalg.lapack.chesvx")(...) | Wrapper for `chesvx`. |
| [`zhesvx`](generated/scipy.linalg.lapack.zhesvx.html#scipy.linalg.lapack.zhesvx "scipy.linalg.lapack.zhesvx")(...) | Wrapper for `zhesvx`. |
| [`chesvx_lwork`](generated/scipy.linalg.lapack.chesvx_lwork.html#scipy.linalg.lapack.chesvx_lwork "scipy.linalg.lapack.chesvx_lwork")(n,[lower]) | Wrapper for `chesvx_lwork`. |
| [`zhesvx_lwork`](generated/scipy.linalg.lapack.zhesvx_lwork.html#scipy.linalg.lapack.zhesvx_lwork "scipy.linalg.lapack.zhesvx_lwork")(n,[lower]) | Wrapper for `zhesvx_lwork`. |
| [`chetrd`](generated/scipy.linalg.lapack.chetrd.html#scipy.linalg.lapack.chetrd "scipy.linalg.lapack.chetrd")(a,[lower,lwork,overwrite\_a]) | Wrapper for `chetrd`. |
| [`zhetrd`](generated/scipy.linalg.lapack.zhetrd.html#scipy.linalg.lapack.zhetrd "scipy.linalg.lapack.zhetrd")(a,[lower,lwork,overwrite\_a]) | Wrapper for `zhetrd`. |
| [`chetrd_lwork`](generated/scipy.linalg.lapack.chetrd_lwork.html#scipy.linalg.lapack.chetrd_lwork "scipy.linalg.lapack.chetrd_lwork")(n,[lower]) | Wrapper for `chetrd_lwork`. |
| [`zhetrd_lwork`](generated/scipy.linalg.lapack.zhetrd_lwork.html#scipy.linalg.lapack.zhetrd_lwork "scipy.linalg.lapack.zhetrd_lwork")(n,[lower]) | Wrapper for `zhetrd_lwork`. |
| [`chetrf`](generated/scipy.linalg.lapack.chetrf.html#scipy.linalg.lapack.chetrf "scipy.linalg.lapack.chetrf")(a,[lower,lwork,overwrite\_a]) | Wrapper for `chetrf`. |
| [`zhetrf`](generated/scipy.linalg.lapack.zhetrf.html#scipy.linalg.lapack.zhetrf "scipy.linalg.lapack.zhetrf")(a,[lower,lwork,overwrite\_a]) | Wrapper for `zhetrf`. |
| [`chetrf_lwork`](generated/scipy.linalg.lapack.chetrf_lwork.html#scipy.linalg.lapack.chetrf_lwork "scipy.linalg.lapack.chetrf_lwork")(n,[lower]) | Wrapper for `chetrf_lwork`. |
| [`zhetrf_lwork`](generated/scipy.linalg.lapack.zhetrf_lwork.html#scipy.linalg.lapack.zhetrf_lwork "scipy.linalg.lapack.zhetrf_lwork")(n,[lower]) | Wrapper for `zhetrf_lwork`. |
| [`chetri`](generated/scipy.linalg.lapack.chetri.html#scipy.linalg.lapack.chetri "scipy.linalg.lapack.chetri")(a,ipiv,[lower,overwrite\_a]) | Wrapper for `chetri`. |
| [`zhetri`](generated/scipy.linalg.lapack.zhetri.html#scipy.linalg.lapack.zhetri "scipy.linalg.lapack.zhetri")(a,ipiv,[lower,overwrite\_a]) | Wrapper for `zhetri`. |
| [`chetrs`](generated/scipy.linalg.lapack.chetrs.html#scipy.linalg.lapack.chetrs "scipy.linalg.lapack.chetrs")(a,ipiv,b,[lower,overwrite\_b]) | Wrapper for `chetrs`. |
| [`zhetrs`](generated/scipy.linalg.lapack.zhetrs.html#scipy.linalg.lapack.zhetrs "scipy.linalg.lapack.zhetrs")(a,ipiv,b,[lower,overwrite\_b]) | Wrapper for `zhetrs`. |
| [`chfrk`](generated/scipy.linalg.lapack.chfrk.html#scipy.linalg.lapack.chfrk "scipy.linalg.lapack.chfrk")(...) | Wrapper for `chfrk`. |
| [`zhfrk`](generated/scipy.linalg.lapack.zhfrk.html#scipy.linalg.lapack.zhfrk "scipy.linalg.lapack.zhfrk")(...) | Wrapper for `zhfrk`. |
| [`slamch`](generated/scipy.linalg.lapack.slamch.html#scipy.linalg.lapack.slamch "scipy.linalg.lapack.slamch")(cmach) | Wrapper for `slamch`. |
| [`dlamch`](generated/scipy.linalg.lapack.dlamch.html#scipy.linalg.lapack.dlamch "scipy.linalg.lapack.dlamch")(cmach) | Wrapper for `dlamch`. |
| [`slangb`](generated/scipy.linalg.lapack.slangb.html#scipy.linalg.lapack.slangb "scipy.linalg.lapack.slangb")(norm,kl,ku,ab,[ldab]) | Wrapper for `slangb`. |
| [`dlangb`](generated/scipy.linalg.lapack.dlangb.html#scipy.linalg.lapack.dlangb "scipy.linalg.lapack.dlangb")(norm,kl,ku,ab,[ldab]) | Wrapper for `dlangb`. |
| [`clangb`](generated/scipy.linalg.lapack.clangb.html#scipy.linalg.lapack.clangb "scipy.linalg.lapack.clangb")(norm,kl,ku,ab,[ldab]) | Wrapper for `clangb`. |
| [`zlangb`](generated/scipy.linalg.lapack.zlangb.html#scipy.linalg.lapack.zlangb "scipy.linalg.lapack.zlangb")(norm,kl,ku,ab,[ldab]) | Wrapper for `zlangb`. |
| [`slange`](generated/scipy.linalg.lapack.slange.html#scipy.linalg.lapack.slange "scipy.linalg.lapack.slange")(norm,Â a) | Wrapper for `slange`. |
| [`dlange`](generated/scipy.linalg.lapack.dlange.html#scipy.linalg.lapack.dlange "scipy.linalg.lapack.dlange")(norm,Â a) | Wrapper for `dlange`. |
| [`clange`](generated/scipy.linalg.lapack.clange.html#scipy.linalg.lapack.clange "scipy.linalg.lapack.clange")(norm,Â a) | Wrapper for `clange`. |
| [`zlange`](generated/scipy.linalg.lapack.zlange.html#scipy.linalg.lapack.zlange "scipy.linalg.lapack.zlange")(norm,Â a) | Wrapper for `zlange`. |
| [`slantr`](generated/scipy.linalg.lapack.slantr.html#scipy.linalg.lapack.slantr "scipy.linalg.lapack.slantr")(norm,a,[uplo,diag]) | Wrapper for `slantr`. |
| [`dlantr`](generated/scipy.linalg.lapack.dlantr.html#scipy.linalg.lapack.dlantr "scipy.linalg.lapack.dlantr")(norm,a,[uplo,diag]) | Wrapper for `dlantr`. |
| [`clantr`](generated/scipy.linalg.lapack.clantr.html#scipy.linalg.lapack.clantr "scipy.linalg.lapack.clantr")(norm,a,[uplo,diag]) | Wrapper for `clantr`. |
| [`zlantr`](generated/scipy.linalg.lapack.zlantr.html#scipy.linalg.lapack.zlantr "scipy.linalg.lapack.zlantr")(norm,a,[uplo,diag]) | Wrapper for `zlantr`. |
| [`slarf`](generated/scipy.linalg.lapack.slarf.html#scipy.linalg.lapack.slarf "scipy.linalg.lapack.slarf")(v,tau,c,work,[side,incv,overwrite\_c]) | Wrapper for `slarf`. |
| [`dlarf`](generated/scipy.linalg.lapack.dlarf.html#scipy.linalg.lapack.dlarf "scipy.linalg.lapack.dlarf")(v,tau,c,work,[side,incv,overwrite\_c]) | Wrapper for `dlarf`. |
| [`clarf`](generated/scipy.linalg.lapack.clarf.html#scipy.linalg.lapack.clarf "scipy.linalg.lapack.clarf")(v,tau,c,work,[side,incv,overwrite\_c]) | Wrapper for `clarf`. |
| [`zlarf`](generated/scipy.linalg.lapack.zlarf.html#scipy.linalg.lapack.zlarf "scipy.linalg.lapack.zlarf")(v,tau,c,work,[side,incv,overwrite\_c]) | Wrapper for `zlarf`. |
| [`slarfg`](generated/scipy.linalg.lapack.slarfg.html#scipy.linalg.lapack.slarfg "scipy.linalg.lapack.slarfg")(n,alpha,x,[incx,overwrite\_x]) | Wrapper for `slarfg`. |
| [`dlarfg`](generated/scipy.linalg.lapack.dlarfg.html#scipy.linalg.lapack.dlarfg "scipy.linalg.lapack.dlarfg")(n,alpha,x,[incx,overwrite\_x]) | Wrapper for `dlarfg`. |
| [`clarfg`](generated/scipy.linalg.lapack.clarfg.html#scipy.linalg.lapack.clarfg "scipy.linalg.lapack.clarfg")(n,alpha,x,[incx,overwrite\_x]) | Wrapper for `clarfg`. |
| [`zlarfg`](generated/scipy.linalg.lapack.zlarfg.html#scipy.linalg.lapack.zlarfg "scipy.linalg.lapack.zlarfg")(n,alpha,x,[incx,overwrite\_x]) | Wrapper for `zlarfg`. |
| [`slartg`](generated/scipy.linalg.lapack.slartg.html#scipy.linalg.lapack.slartg "scipy.linalg.lapack.slartg")(f,Â g) | Wrapper for `slartg`. |
| [`dlartg`](generated/scipy.linalg.lapack.dlartg.html#scipy.linalg.lapack.dlartg "scipy.linalg.lapack.dlartg")(f,Â g) | Wrapper for `dlartg`. |
| [`clartg`](generated/scipy.linalg.lapack.clartg.html#scipy.linalg.lapack.clartg "scipy.linalg.lapack.clartg")(f,Â g) | Wrapper for `clartg`. |
| [`zlartg`](generated/scipy.linalg.lapack.zlartg.html#scipy.linalg.lapack.zlartg "scipy.linalg.lapack.zlartg")(f,Â g) | Wrapper for `zlartg`. |
| [`slasd4`](generated/scipy.linalg.lapack.slasd4.html#scipy.linalg.lapack.slasd4 "scipy.linalg.lapack.slasd4")(i,d,z,[rho]) | Wrapper for `slasd4`. |
| [`dlasd4`](generated/scipy.linalg.lapack.dlasd4.html#scipy.linalg.lapack.dlasd4 "scipy.linalg.lapack.dlasd4")(i,d,z,[rho]) | Wrapper for `dlasd4`. |
| [`slaswp`](generated/scipy.linalg.lapack.slaswp.html#scipy.linalg.lapack.slaswp "scipy.linalg.lapack.slaswp")(a,piv,[k1,k2,off,inc,overwrite\_a]) | Wrapper for `slaswp`. |
| [`dlaswp`](generated/scipy.linalg.lapack.dlaswp.html#scipy.linalg.lapack.dlaswp "scipy.linalg.lapack.dlaswp")(a,piv,[k1,k2,off,inc,overwrite\_a]) | Wrapper for `dlaswp`. |
| [`claswp`](generated/scipy.linalg.lapack.claswp.html#scipy.linalg.lapack.claswp "scipy.linalg.lapack.claswp")(a,piv,[k1,k2,off,inc,overwrite\_a]) | Wrapper for `claswp`. |
| [`zlaswp`](generated/scipy.linalg.lapack.zlaswp.html#scipy.linalg.lapack.zlaswp "scipy.linalg.lapack.zlaswp")(a,piv,[k1,k2,off,inc,overwrite\_a]) | Wrapper for `zlaswp`. |
| [`slauum`](generated/scipy.linalg.lapack.slauum.html#scipy.linalg.lapack.slauum "scipy.linalg.lapack.slauum")(c,[lower,overwrite\_c]) | Wrapper for `slauum`. |
| [`dlauum`](generated/scipy.linalg.lapack.dlauum.html#scipy.linalg.lapack.dlauum "scipy.linalg.lapack.dlauum")(c,[lower,overwrite\_c]) | Wrapper for `dlauum`. |
| [`clauum`](generated/scipy.linalg.lapack.clauum.html#scipy.linalg.lapack.clauum "scipy.linalg.lapack.clauum")(c,[lower,overwrite\_c]) | Wrapper for `clauum`. |
| [`zlauum`](generated/scipy.linalg.lapack.zlauum.html#scipy.linalg.lapack.zlauum "scipy.linalg.lapack.zlauum")(c,[lower,overwrite\_c]) | Wrapper for `zlauum`. |
| [`sorcsd`](generated/scipy.linalg.lapack.sorcsd.html#scipy.linalg.lapack.sorcsd "scipy.linalg.lapack.sorcsd")(...) | Wrapper for `sorcsd`. |
| [`dorcsd`](generated/scipy.linalg.lapack.dorcsd.html#scipy.linalg.lapack.dorcsd "scipy.linalg.lapack.dorcsd")(...) | Wrapper for `dorcsd`. |
| [`sorcsd_lwork`](generated/scipy.linalg.lapack.sorcsd_lwork.html#scipy.linalg.lapack.sorcsd_lwork "scipy.linalg.lapack.sorcsd_lwork")(m,Â p,Â q) | Wrapper for `sorcsd_lwork`. |
| [`dorcsd_lwork`](generated/scipy.linalg.lapack.dorcsd_lwork.html#scipy.linalg.lapack.dorcsd_lwork "scipy.linalg.lapack.dorcsd_lwork")(m,Â p,Â q) | Wrapper for `dorcsd_lwork`. |
| [`sorghr`](generated/scipy.linalg.lapack.sorghr.html#scipy.linalg.lapack.sorghr "scipy.linalg.lapack.sorghr")(a,tau,[lo,hi,lwork,overwrite\_a]) | Wrapper for `sorghr`. |
| [`dorghr`](generated/scipy.linalg.lapack.dorghr.html#scipy.linalg.lapack.dorghr "scipy.linalg.lapack.dorghr")(a,tau,[lo,hi,lwork,overwrite\_a]) | Wrapper for `dorghr`. |
| [`sorghr_lwork`](generated/scipy.linalg.lapack.sorghr_lwork.html#scipy.linalg.lapack.sorghr_lwork "scipy.linalg.lapack.sorghr_lwork")(n,[lo,hi]) | Wrapper for `sorghr_lwork`. |
| [`dorghr_lwork`](generated/scipy.linalg.lapack.dorghr_lwork.html#scipy.linalg.lapack.dorghr_lwork "scipy.linalg.lapack.dorghr_lwork")(n,[lo,hi]) | Wrapper for `dorghr_lwork`. |
| [`sorgqr`](generated/scipy.linalg.lapack.sorgqr.html#scipy.linalg.lapack.sorgqr "scipy.linalg.lapack.sorgqr")(a,tau,[lwork,overwrite\_a]) | Wrapper for `sorgqr`. |
| [`dorgqr`](generated/scipy.linalg.lapack.dorgqr.html#scipy.linalg.lapack.dorgqr "scipy.linalg.lapack.dorgqr")(a,tau,[lwork,overwrite\_a]) | Wrapper for `dorgqr`. |
| [`sorgrq`](generated/scipy.linalg.lapack.sorgrq.html#scipy.linalg.lapack.sorgrq "scipy.linalg.lapack.sorgrq")(a,tau,[lwork,overwrite\_a]) | Wrapper for `sorgrq`. |
| [`dorgrq`](generated/scipy.linalg.lapack.dorgrq.html#scipy.linalg.lapack.dorgrq "scipy.linalg.lapack.dorgrq")(a,tau,[lwork,overwrite\_a]) | Wrapper for `dorgrq`. |
| [`sormqr`](generated/scipy.linalg.lapack.sormqr.html#scipy.linalg.lapack.sormqr "scipy.linalg.lapack.sormqr")(side,trans,a,tau,c,lwork,[overwrite\_c]) | Wrapper for `sormqr`. |
| [`dormqr`](generated/scipy.linalg.lapack.dormqr.html#scipy.linalg.lapack.dormqr "scipy.linalg.lapack.dormqr")(side,trans,a,tau,c,lwork,[overwrite\_c]) | Wrapper for `dormqr`. |
| [`sormrz`](generated/scipy.linalg.lapack.sormrz.html#scipy.linalg.lapack.sormrz "scipy.linalg.lapack.sormrz")(a,tau,c,[side,trans,lwork,overwrite\_c]) | Wrapper for `sormrz`. |
| [`dormrz`](generated/scipy.linalg.lapack.dormrz.html#scipy.linalg.lapack.dormrz "scipy.linalg.lapack.dormrz")(a,tau,c,[side,trans,lwork,overwrite\_c]) | Wrapper for `dormrz`. |
| [`sormrz_lwork`](generated/scipy.linalg.lapack.sormrz_lwork.html#scipy.linalg.lapack.sormrz_lwork "scipy.linalg.lapack.sormrz_lwork")(m,n,[side,trans]) | Wrapper for `sormrz_lwork`. |
| [`dormrz_lwork`](generated/scipy.linalg.lapack.dormrz_lwork.html#scipy.linalg.lapack.dormrz_lwork "scipy.linalg.lapack.dormrz_lwork")(m,n,[side,trans]) | Wrapper for `dormrz_lwork`. |
| [`spbsv`](generated/scipy.linalg.lapack.spbsv.html#scipy.linalg.lapack.spbsv "scipy.linalg.lapack.spbsv")(ab,b,[lower,ldab,overwrite\_ab,overwrite\_b]) | Wrapper for `spbsv`. |
| [`dpbsv`](generated/scipy.linalg.lapack.dpbsv.html#scipy.linalg.lapack.dpbsv "scipy.linalg.lapack.dpbsv")(ab,b,[lower,ldab,overwrite\_ab,overwrite\_b]) | Wrapper for `dpbsv`. |
| [`cpbsv`](generated/scipy.linalg.lapack.cpbsv.html#scipy.linalg.lapack.cpbsv "scipy.linalg.lapack.cpbsv")(ab,b,[lower,ldab,overwrite\_ab,overwrite\_b]) | Wrapper for `cpbsv`. |
| [`zpbsv`](generated/scipy.linalg.lapack.zpbsv.html#scipy.linalg.lapack.zpbsv "scipy.linalg.lapack.zpbsv")(ab,b,[lower,ldab,overwrite\_ab,overwrite\_b]) | Wrapper for `zpbsv`. |
| [`spbtrf`](generated/scipy.linalg.lapack.spbtrf.html#scipy.linalg.lapack.spbtrf "scipy.linalg.lapack.spbtrf")(ab,[lower,ldab,overwrite\_ab]) | Wrapper for `spbtrf`. |
| [`dpbtrf`](generated/scipy.linalg.lapack.dpbtrf.html#scipy.linalg.lapack.dpbtrf "scipy.linalg.lapack.dpbtrf")(ab,[lower,ldab,overwrite\_ab]) | Wrapper for `dpbtrf`. |
| [`cpbtrf`](generated/scipy.linalg.lapack.cpbtrf.html#scipy.linalg.lapack.cpbtrf "scipy.linalg.lapack.cpbtrf")(ab,[lower,ldab,overwrite\_ab]) | Wrapper for `cpbtrf`. |
| [`zpbtrf`](generated/scipy.linalg.lapack.zpbtrf.html#scipy.linalg.lapack.zpbtrf "scipy.linalg.lapack.zpbtrf")(ab,[lower,ldab,overwrite\_ab]) | Wrapper for `zpbtrf`. |
| [`spbtrs`](generated/scipy.linalg.lapack.spbtrs.html#scipy.linalg.lapack.spbtrs "scipy.linalg.lapack.spbtrs")(ab,b,[lower,ldab,overwrite\_b]) | Wrapper for `spbtrs`. |
| [`dpbtrs`](generated/scipy.linalg.lapack.dpbtrs.html#scipy.linalg.lapack.dpbtrs "scipy.linalg.lapack.dpbtrs")(ab,b,[lower,ldab,overwrite\_b]) | Wrapper for `dpbtrs`. |
| [`cpbtrs`](generated/scipy.linalg.lapack.cpbtrs.html#scipy.linalg.lapack.cpbtrs "scipy.linalg.lapack.cpbtrs")(ab,b,[lower,ldab,overwrite\_b]) | Wrapper for `cpbtrs`. |
| [`zpbtrs`](generated/scipy.linalg.lapack.zpbtrs.html#scipy.linalg.lapack.zpbtrs "scipy.linalg.lapack.zpbtrs")(ab,b,[lower,ldab,overwrite\_b]) | Wrapper for `zpbtrs`. |
| [`spftrf`](generated/scipy.linalg.lapack.spftrf.html#scipy.linalg.lapack.spftrf "scipy.linalg.lapack.spftrf")(n,a,[transr,uplo,overwrite\_a]) | Wrapper for `spftrf`. |
| [`dpftrf`](generated/scipy.linalg.lapack.dpftrf.html#scipy.linalg.lapack.dpftrf "scipy.linalg.lapack.dpftrf")(n,a,[transr,uplo,overwrite\_a]) | Wrapper for `dpftrf`. |
| [`cpftrf`](generated/scipy.linalg.lapack.cpftrf.html#scipy.linalg.lapack.cpftrf "scipy.linalg.lapack.cpftrf")(n,a,[transr,uplo,overwrite\_a]) | Wrapper for `cpftrf`. |
| [`zpftrf`](generated/scipy.linalg.lapack.zpftrf.html#scipy.linalg.lapack.zpftrf "scipy.linalg.lapack.zpftrf")(n,a,[transr,uplo,overwrite\_a]) | Wrapper for `zpftrf`. |
| [`spftri`](generated/scipy.linalg.lapack.spftri.html#scipy.linalg.lapack.spftri "scipy.linalg.lapack.spftri")(n,a,[transr,uplo,overwrite\_a]) | Wrapper for `spftri`. |
| [`dpftri`](generated/scipy.linalg.lapack.dpftri.html#scipy.linalg.lapack.dpftri "scipy.linalg.lapack.dpftri")(n,a,[transr,uplo,overwrite\_a]) | Wrapper for `dpftri`. |
| [`cpftri`](generated/scipy.linalg.lapack.cpftri.html#scipy.linalg.lapack.cpftri "scipy.linalg.lapack.cpftri")(n,a,[transr,uplo,overwrite\_a]) | Wrapper for `cpftri`. |
| [`zpftri`](generated/scipy.linalg.lapack.zpftri.html#scipy.linalg.lapack.zpftri "scipy.linalg.lapack.zpftri")(n,a,[transr,uplo,overwrite\_a]) | Wrapper for `zpftri`. |
| [`spftrs`](generated/scipy.linalg.lapack.spftrs.html#scipy.linalg.lapack.spftrs "scipy.linalg.lapack.spftrs")(n,a,b,[transr,uplo,overwrite\_b]) | Wrapper for `spftrs`. |
| [`dpftrs`](generated/scipy.linalg.lapack.dpftrs.html#scipy.linalg.lapack.dpftrs "scipy.linalg.lapack.dpftrs")(n,a,b,[transr,uplo,overwrite\_b]) | Wrapper for `dpftrs`. |
| [`cpftrs`](generated/scipy.linalg.lapack.cpftrs.html#scipy.linalg.lapack.cpftrs "scipy.linalg.lapack.cpftrs")(n,a,b,[transr,uplo,overwrite\_b]) | Wrapper for `cpftrs`. |
| [`zpftrs`](generated/scipy.linalg.lapack.zpftrs.html#scipy.linalg.lapack.zpftrs "scipy.linalg.lapack.zpftrs")(n,a,b,[transr,uplo,overwrite\_b]) | Wrapper for `zpftrs`. |
| [`spocon`](generated/scipy.linalg.lapack.spocon.html#scipy.linalg.lapack.spocon "scipy.linalg.lapack.spocon")(a,anorm,[uplo]) | Wrapper for `spocon`. |
| [`dpocon`](generated/scipy.linalg.lapack.dpocon.html#scipy.linalg.lapack.dpocon "scipy.linalg.lapack.dpocon")(a,anorm,[uplo]) | Wrapper for `dpocon`. |
| [`cpocon`](generated/scipy.linalg.lapack.cpocon.html#scipy.linalg.lapack.cpocon "scipy.linalg.lapack.cpocon")(a,anorm,[uplo]) | Wrapper for `cpocon`. |
| [`zpocon`](generated/scipy.linalg.lapack.zpocon.html#scipy.linalg.lapack.zpocon "scipy.linalg.lapack.zpocon")(a,anorm,[uplo]) | Wrapper for `zpocon`. |
| [`spstrf`](generated/scipy.linalg.lapack.spstrf.html#scipy.linalg.lapack.spstrf "scipy.linalg.lapack.spstrf")(a,[tol,lower,overwrite\_a]) | Wrapper for `spstrf`. |
| [`dpstrf`](generated/scipy.linalg.lapack.dpstrf.html#scipy.linalg.lapack.dpstrf "scipy.linalg.lapack.dpstrf")(a,[tol,lower,overwrite\_a]) | Wrapper for `dpstrf`. |
| [`cpstrf`](generated/scipy.linalg.lapack.cpstrf.html#scipy.linalg.lapack.cpstrf "scipy.linalg.lapack.cpstrf")(a,[tol,lower,overwrite\_a]) | Wrapper for `cpstrf`. |
| [`zpstrf`](generated/scipy.linalg.lapack.zpstrf.html#scipy.linalg.lapack.zpstrf "scipy.linalg.lapack.zpstrf")(a,[tol,lower,overwrite\_a]) | Wrapper for `zpstrf`. |
| [`spstf2`](generated/scipy.linalg.lapack.spstf2.html#scipy.linalg.lapack.spstf2 "scipy.linalg.lapack.spstf2")(a,[tol,lower,overwrite\_a]) | Wrapper for `spstf2`. |
| [`dpstf2`](generated/scipy.linalg.lapack.dpstf2.html#scipy.linalg.lapack.dpstf2 "scipy.linalg.lapack.dpstf2")(a,[tol,lower,overwrite\_a]) | Wrapper for `dpstf2`. |
| [`cpstf2`](generated/scipy.linalg.lapack.cpstf2.html#scipy.linalg.lapack.cpstf2 "scipy.linalg.lapack.cpstf2")(a,[tol,lower,overwrite\_a]) | Wrapper for `cpstf2`. |
| [`zpstf2`](generated/scipy.linalg.lapack.zpstf2.html#scipy.linalg.lapack.zpstf2 "scipy.linalg.lapack.zpstf2")(a,[tol,lower,overwrite\_a]) | Wrapper for `zpstf2`. |
| [`sposv`](generated/scipy.linalg.lapack.sposv.html#scipy.linalg.lapack.sposv "scipy.linalg.lapack.sposv")(a,b,[lower,overwrite\_a,overwrite\_b]) | Wrapper for `sposv`. |
| [`dposv`](generated/scipy.linalg.lapack.dposv.html#scipy.linalg.lapack.dposv "scipy.linalg.lapack.dposv")(a,b,[lower,overwrite\_a,overwrite\_b]) | Wrapper for `dposv`. |
| [`cposv`](generated/scipy.linalg.lapack.cposv.html#scipy.linalg.lapack.cposv "scipy.linalg.lapack.cposv")(a,b,[lower,overwrite\_a,overwrite\_b]) | Wrapper for `cposv`. |
| [`zposv`](generated/scipy.linalg.lapack.zposv.html#scipy.linalg.lapack.zposv "scipy.linalg.lapack.zposv")(a,b,[lower,overwrite\_a,overwrite\_b]) | Wrapper for `zposv`. |
| [`sposvx`](generated/scipy.linalg.lapack.sposvx.html#scipy.linalg.lapack.sposvx "scipy.linalg.lapack.sposvx")(...) | Wrapper for `sposvx`. |
| [`dposvx`](generated/scipy.linalg.lapack.dposvx.html#scipy.linalg.lapack.dposvx "scipy.linalg.lapack.dposvx")(...) | Wrapper for `dposvx`. |
| [`cposvx`](generated/scipy.linalg.lapack.cposvx.html#scipy.linalg.lapack.cposvx "scipy.linalg.lapack.cposvx")(...) | Wrapper for `cposvx`. |
| [`zposvx`](generated/scipy.linalg.lapack.zposvx.html#scipy.linalg.lapack.zposvx "scipy.linalg.lapack.zposvx")(...) | Wrapper for `zposvx`. |
| [`spotrf`](generated/scipy.linalg.lapack.spotrf.html#scipy.linalg.lapack.spotrf "scipy.linalg.lapack.spotrf")(a,[lower,clean,overwrite\_a]) | Wrapper for `spotrf`. |
| [`dpotrf`](generated/scipy.linalg.lapack.dpotrf.html#scipy.linalg.lapack.dpotrf "scipy.linalg.lapack.dpotrf")(a,[lower,clean,overwrite\_a]) | Wrapper for `dpotrf`. |
| [`cpotrf`](generated/scipy.linalg.lapack.cpotrf.html#scipy.linalg.lapack.cpotrf "scipy.linalg.lapack.cpotrf")(a,[lower,clean,overwrite\_a]) | Wrapper for `cpotrf`. |
| [`zpotrf`](generated/scipy.linalg.lapack.zpotrf.html#scipy.linalg.lapack.zpotrf "scipy.linalg.lapack.zpotrf")(a,[lower,clean,overwrite\_a]) | Wrapper for `zpotrf`. |
| [`spotri`](generated/scipy.linalg.lapack.spotri.html#scipy.linalg.lapack.spotri "scipy.linalg.lapack.spotri")(c,[lower,overwrite\_c]) | Wrapper for `spotri`. |
| [`dpotri`](generated/scipy.linalg.lapack.dpotri.html#scipy.linalg.lapack.dpotri "scipy.linalg.lapack.dpotri")(c,[lower,overwrite\_c]) | Wrapper for `dpotri`. |
| [`cpotri`](generated/scipy.linalg.lapack.cpotri.html#scipy.linalg.lapack.cpotri "scipy.linalg.lapack.cpotri")(c,[lower,overwrite\_c]) | Wrapper for `cpotri`. |
| [`zpotri`](generated/scipy.linalg.lapack.zpotri.html#scipy.linalg.lapack.zpotri "scipy.linalg.lapack.zpotri")(c,[lower,overwrite\_c]) | Wrapper for `zpotri`. |
| [`spotrs`](generated/scipy.linalg.lapack.spotrs.html#scipy.linalg.lapack.spotrs "scipy.linalg.lapack.spotrs")(c,b,[lower,overwrite\_b]) | Wrapper for `spotrs`. |
| [`dpotrs`](generated/scipy.linalg.lapack.dpotrs.html#scipy.linalg.lapack.dpotrs "scipy.linalg.lapack.dpotrs")(c,b,[lower,overwrite\_b]) | Wrapper for `dpotrs`. |
| [`cpotrs`](generated/scipy.linalg.lapack.cpotrs.html#scipy.linalg.lapack.cpotrs "scipy.linalg.lapack.cpotrs")(c,b,[lower,overwrite\_b]) | Wrapper for `cpotrs`. |
| [`zpotrs`](generated/scipy.linalg.lapack.zpotrs.html#scipy.linalg.lapack.zpotrs "scipy.linalg.lapack.zpotrs")(c,b,[lower,overwrite\_b]) | Wrapper for `zpotrs`. |
| [`sppcon`](generated/scipy.linalg.lapack.sppcon.html#scipy.linalg.lapack.sppcon "scipy.linalg.lapack.sppcon")(n,ap,anorm,[lower]) | Wrapper for `sppcon`. |
| [`dppcon`](generated/scipy.linalg.lapack.dppcon.html#scipy.linalg.lapack.dppcon "scipy.linalg.lapack.dppcon")(n,ap,anorm,[lower]) | Wrapper for `dppcon`. |
| [`cppcon`](generated/scipy.linalg.lapack.cppcon.html#scipy.linalg.lapack.cppcon "scipy.linalg.lapack.cppcon")(n,ap,anorm,[lower]) | Wrapper for `cppcon`. |
| [`zppcon`](generated/scipy.linalg.lapack.zppcon.html#scipy.linalg.lapack.zppcon "scipy.linalg.lapack.zppcon")(n,ap,anorm,[lower]) | Wrapper for `zppcon`. |
| [`sppsv`](generated/scipy.linalg.lapack.sppsv.html#scipy.linalg.lapack.sppsv "scipy.linalg.lapack.sppsv")(n,ap,b,[lower,overwrite\_b]) | Wrapper for `sppsv`. |
| [`dppsv`](generated/scipy.linalg.lapack.dppsv.html#scipy.linalg.lapack.dppsv "scipy.linalg.lapack.dppsv")(n,ap,b,[lower,overwrite\_b]) | Wrapper for `dppsv`. |
| [`cppsv`](generated/scipy.linalg.lapack.cppsv.html#scipy.linalg.lapack.cppsv "scipy.linalg.lapack.cppsv")(n,ap,b,[lower,overwrite\_b]) | Wrapper for `cppsv`. |
| [`zppsv`](generated/scipy.linalg.lapack.zppsv.html#scipy.linalg.lapack.zppsv "scipy.linalg.lapack.zppsv")(n,ap,b,[lower,overwrite\_b]) | Wrapper for `zppsv`. |
| [`spptrf`](generated/scipy.linalg.lapack.spptrf.html#scipy.linalg.lapack.spptrf "scipy.linalg.lapack.spptrf")(n,ap,[lower,overwrite\_ap]) | Wrapper for `spptrf`. |
| [`dpptrf`](generated/scipy.linalg.lapack.dpptrf.html#scipy.linalg.lapack.dpptrf "scipy.linalg.lapack.dpptrf")(n,ap,[lower,overwrite\_ap]) | Wrapper for `dpptrf`. |
| [`cpptrf`](generated/scipy.linalg.lapack.cpptrf.html#scipy.linalg.lapack.cpptrf "scipy.linalg.lapack.cpptrf")(n,ap,[lower,overwrite\_ap]) | Wrapper for `cpptrf`. |
| [`zpptrf`](generated/scipy.linalg.lapack.zpptrf.html#scipy.linalg.lapack.zpptrf "scipy.linalg.lapack.zpptrf")(n,ap,[lower,overwrite\_ap]) | Wrapper for `zpptrf`. |
| [`spptri`](generated/scipy.linalg.lapack.spptri.html#scipy.linalg.lapack.spptri "scipy.linalg.lapack.spptri")(n,ap,[lower,overwrite\_ap]) | Wrapper for `spptri`. |
| [`dpptri`](generated/scipy.linalg.lapack.dpptri.html#scipy.linalg.lapack.dpptri "scipy.linalg.lapack.dpptri")(n,ap,[lower,overwrite\_ap]) | Wrapper for `dpptri`. |
| [`cpptri`](generated/scipy.linalg.lapack.cpptri.html#scipy.linalg.lapack.cpptri "scipy.linalg.lapack.cpptri")(n,ap,[lower,overwrite\_ap]) | Wrapper for `cpptri`. |
| [`zpptri`](generated/scipy.linalg.lapack.zpptri.html#scipy.linalg.lapack.zpptri "scipy.linalg.lapack.zpptri")(n,ap,[lower,overwrite\_ap]) | Wrapper for `zpptri`. |
| [`spptrs`](generated/scipy.linalg.lapack.spptrs.html#scipy.linalg.lapack.spptrs "scipy.linalg.lapack.spptrs")(n,ap,b,[lower,overwrite\_b]) | Wrapper for `spptrs`. |
| [`dpptrs`](generated/scipy.linalg.lapack.dpptrs.html#scipy.linalg.lapack.dpptrs "scipy.linalg.lapack.dpptrs")(n,ap,b,[lower,overwrite\_b]) | Wrapper for `dpptrs`. |
| [`cpptrs`](generated/scipy.linalg.lapack.cpptrs.html#scipy.linalg.lapack.cpptrs "scipy.linalg.lapack.cpptrs")(n,ap,b,[lower,overwrite\_b]) | Wrapper for `cpptrs`. |
| [`zpptrs`](generated/scipy.linalg.lapack.zpptrs.html#scipy.linalg.lapack.zpptrs "scipy.linalg.lapack.zpptrs")(n,ap,b,[lower,overwrite\_b]) | Wrapper for `zpptrs`. |
| [`sptsv`](generated/scipy.linalg.lapack.sptsv.html#scipy.linalg.lapack.sptsv "scipy.linalg.lapack.sptsv")(...) | Wrapper for `sptsv`. |
| [`dptsv`](generated/scipy.linalg.lapack.dptsv.html#scipy.linalg.lapack.dptsv "scipy.linalg.lapack.dptsv")(...) | Wrapper for `dptsv`. |
| [`cptsv`](generated/scipy.linalg.lapack.cptsv.html#scipy.linalg.lapack.cptsv "scipy.linalg.lapack.cptsv")(...) | Wrapper for `cptsv`. |
| [`zptsv`](generated/scipy.linalg.lapack.zptsv.html#scipy.linalg.lapack.zptsv "scipy.linalg.lapack.zptsv")(...) | Wrapper for `zptsv`. |
| [`sptsvx`](generated/scipy.linalg.lapack.sptsvx.html#scipy.linalg.lapack.sptsvx "scipy.linalg.lapack.sptsvx")(d,e,b,[fact,df,ef]) | Wrapper for `sptsvx`. |
| [`dptsvx`](generated/scipy.linalg.lapack.dptsvx.html#scipy.linalg.lapack.dptsvx "scipy.linalg.lapack.dptsvx")(d,e,b,[fact,df,ef]) | Wrapper for `dptsvx`. |
| [`cptsvx`](generated/scipy.linalg.lapack.cptsvx.html#scipy.linalg.lapack.cptsvx "scipy.linalg.lapack.cptsvx")(d,e,b,[fact,df,ef]) | Wrapper for `cptsvx`. |
| [`zptsvx`](generated/scipy.linalg.lapack.zptsvx.html#scipy.linalg.lapack.zptsvx "scipy.linalg.lapack.zptsvx")(d,e,b,[fact,df,ef]) | Wrapper for `zptsvx`. |
| [`spttrf`](generated/scipy.linalg.lapack.spttrf.html#scipy.linalg.lapack.spttrf "scipy.linalg.lapack.spttrf")(d,e,[overwrite\_d,overwrite\_e]) | Wrapper for `spttrf`. |
| [`dpttrf`](generated/scipy.linalg.lapack.dpttrf.html#scipy.linalg.lapack.dpttrf "scipy.linalg.lapack.dpttrf")(d,e,[overwrite\_d,overwrite\_e]) | Wrapper for `dpttrf`. |
| [`cpttrf`](generated/scipy.linalg.lapack.cpttrf.html#scipy.linalg.lapack.cpttrf "scipy.linalg.lapack.cpttrf")(d,e,[overwrite\_d,overwrite\_e]) | Wrapper for `cpttrf`. |
| [`zpttrf`](generated/scipy.linalg.lapack.zpttrf.html#scipy.linalg.lapack.zpttrf "scipy.linalg.lapack.zpttrf")(d,e,[overwrite\_d,overwrite\_e]) | Wrapper for `zpttrf`. |
| [`spttrs`](generated/scipy.linalg.lapack.spttrs.html#scipy.linalg.lapack.spttrs "scipy.linalg.lapack.spttrs")(d,e,b,[overwrite\_b]) | Wrapper for `spttrs`. |
| [`dpttrs`](generated/scipy.linalg.lapack.dpttrs.html#scipy.linalg.lapack.dpttrs "scipy.linalg.lapack.dpttrs")(d,e,b,[overwrite\_b]) | Wrapper for `dpttrs`. |
| [`cpttrs`](generated/scipy.linalg.lapack.cpttrs.html#scipy.linalg.lapack.cpttrs "scipy.linalg.lapack.cpttrs")(d,e,b,[lower,overwrite\_b]) | Wrapper for `cpttrs`. |
| [`zpttrs`](generated/scipy.linalg.lapack.zpttrs.html#scipy.linalg.lapack.zpttrs "scipy.linalg.lapack.zpttrs")(d,e,b,[lower,overwrite\_b]) | Wrapper for `zpttrs`. |
| [`spteqr`](generated/scipy.linalg.lapack.spteqr.html#scipy.linalg.lapack.spteqr "scipy.linalg.lapack.spteqr")(...) | Wrapper for `spteqr`. |
| [`dpteqr`](generated/scipy.linalg.lapack.dpteqr.html#scipy.linalg.lapack.dpteqr "scipy.linalg.lapack.dpteqr")(...) | Wrapper for `dpteqr`. |
| [`cpteqr`](generated/scipy.linalg.lapack.cpteqr.html#scipy.linalg.lapack.cpteqr "scipy.linalg.lapack.cpteqr")(...) | Wrapper for `cpteqr`. |
| [`zpteqr`](generated/scipy.linalg.lapack.zpteqr.html#scipy.linalg.lapack.zpteqr "scipy.linalg.lapack.zpteqr")(...) | Wrapper for `zpteqr`. |
| [`crot`](generated/scipy.linalg.lapack.crot.html#scipy.linalg.lapack.crot "scipy.linalg.lapack.crot")(...) | Wrapper for `crot`. |
| [`zrot`](generated/scipy.linalg.lapack.zrot.html#scipy.linalg.lapack.zrot "scipy.linalg.lapack.zrot")(...) | Wrapper for `zrot`. |
| [`ssbev`](generated/scipy.linalg.lapack.ssbev.html#scipy.linalg.lapack.ssbev "scipy.linalg.lapack.ssbev")(ab,[compute\_v,lower,ldab,overwrite\_ab]) | Wrapper for `ssbev`. |
| [`dsbev`](generated/scipy.linalg.lapack.dsbev.html#scipy.linalg.lapack.dsbev "scipy.linalg.lapack.dsbev")(ab,[compute\_v,lower,ldab,overwrite\_ab]) | Wrapper for `dsbev`. |
| [`ssbevd`](generated/scipy.linalg.lapack.ssbevd.html#scipy.linalg.lapack.ssbevd "scipy.linalg.lapack.ssbevd")(...) | Wrapper for `ssbevd`. |
| [`dsbevd`](generated/scipy.linalg.lapack.dsbevd.html#scipy.linalg.lapack.dsbevd "scipy.linalg.lapack.dsbevd")(...) | Wrapper for `dsbevd`. |
| [`ssbevx`](generated/scipy.linalg.lapack.ssbevx.html#scipy.linalg.lapack.ssbevx "scipy.linalg.lapack.ssbevx")(...) | Wrapper for `ssbevx`. |
| [`dsbevx`](generated/scipy.linalg.lapack.dsbevx.html#scipy.linalg.lapack.dsbevx "scipy.linalg.lapack.dsbevx")(...) | Wrapper for `dsbevx`. |
| [`ssfrk`](generated/scipy.linalg.lapack.ssfrk.html#scipy.linalg.lapack.ssfrk "scipy.linalg.lapack.ssfrk")(...) | Wrapper for `ssfrk`. |
| [`dsfrk`](generated/scipy.linalg.lapack.dsfrk.html#scipy.linalg.lapack.dsfrk "scipy.linalg.lapack.dsfrk")(...) | Wrapper for `dsfrk`. |
| [`sstebz`](generated/scipy.linalg.lapack.sstebz.html#scipy.linalg.lapack.sstebz "scipy.linalg.lapack.sstebz")(d,Â e,Â range,Â vl,Â vu,Â il,Â iu,Â tol,Â order) | Wrapper for `sstebz`. |
| [`dstebz`](generated/scipy.linalg.lapack.dstebz.html#scipy.linalg.lapack.dstebz "scipy.linalg.lapack.dstebz")(d,Â e,Â range,Â vl,Â vu,Â il,Â iu,Â tol,Â order) | Wrapper for `dstebz`. |
| [`sstein`](generated/scipy.linalg.lapack.sstein.html#scipy.linalg.lapack.sstein "scipy.linalg.lapack.sstein")(d,Â e,Â w,Â iblock,Â isplit) | Wrapper for `sstein`. |
| [`dstein`](generated/scipy.linalg.lapack.dstein.html#scipy.linalg.lapack.dstein "scipy.linalg.lapack.dstein")(d,Â e,Â w,Â iblock,Â isplit) | Wrapper for `dstein`. |
| [`sstemr`](generated/scipy.linalg.lapack.sstemr.html#scipy.linalg.lapack.sstemr "scipy.linalg.lapack.sstemr")(...) | Wrapper for `sstemr`. |
| [`dstemr`](generated/scipy.linalg.lapack.dstemr.html#scipy.linalg.lapack.dstemr "scipy.linalg.lapack.dstemr")(...) | Wrapper for `dstemr`. |
| [`sstemr_lwork`](generated/scipy.linalg.lapack.sstemr_lwork.html#scipy.linalg.lapack.sstemr_lwork "scipy.linalg.lapack.sstemr_lwork")(...) | Wrapper for `sstemr_lwork`. |
| [`dstemr_lwork`](generated/scipy.linalg.lapack.dstemr_lwork.html#scipy.linalg.lapack.dstemr_lwork "scipy.linalg.lapack.dstemr_lwork")(...) | Wrapper for `dstemr_lwork`. |
| [`ssterf`](generated/scipy.linalg.lapack.ssterf.html#scipy.linalg.lapack.ssterf "scipy.linalg.lapack.ssterf")(d,e,[overwrite\_d,overwrite\_e]) | Wrapper for `ssterf`. |
| [`dsterf`](generated/scipy.linalg.lapack.dsterf.html#scipy.linalg.lapack.dsterf "scipy.linalg.lapack.dsterf")(d,e,[overwrite\_d,overwrite\_e]) | Wrapper for `dsterf`. |
| [`sstev`](generated/scipy.linalg.lapack.sstev.html#scipy.linalg.lapack.sstev "scipy.linalg.lapack.sstev")(d,e,[compute\_v,overwrite\_d,overwrite\_e]) | Wrapper for `sstev`. |
| [`dstev`](generated/scipy.linalg.lapack.dstev.html#scipy.linalg.lapack.dstev "scipy.linalg.lapack.dstev")(d,e,[compute\_v,overwrite\_d,overwrite\_e]) | Wrapper for `dstev`. |
| [`sstevd`](generated/scipy.linalg.lapack.sstevd.html#scipy.linalg.lapack.sstevd "scipy.linalg.lapack.sstevd")(...) | Wrapper for `sstevd`. |
| [`dstevd`](generated/scipy.linalg.lapack.dstevd.html#scipy.linalg.lapack.dstevd "scipy.linalg.lapack.dstevd")(...) | Wrapper for `dstevd`. |
| [`ssycon`](generated/scipy.linalg.lapack.ssycon.html#scipy.linalg.lapack.ssycon "scipy.linalg.lapack.ssycon")(a,ipiv,anorm,[lower]) | Wrapper for `ssycon`. |
| [`dsycon`](generated/scipy.linalg.lapack.dsycon.html#scipy.linalg.lapack.dsycon "scipy.linalg.lapack.dsycon")(a,ipiv,anorm,[lower]) | Wrapper for `dsycon`. |
| [`csycon`](generated/scipy.linalg.lapack.csycon.html#scipy.linalg.lapack.csycon "scipy.linalg.lapack.csycon")(a,ipiv,anorm,[lower]) | Wrapper for `csycon`. |
| [`zsycon`](generated/scipy.linalg.lapack.zsycon.html#scipy.linalg.lapack.zsycon "scipy.linalg.lapack.zsycon")(a,ipiv,anorm,[lower]) | Wrapper for `zsycon`. |
| [`ssyconv`](generated/scipy.linalg.lapack.ssyconv.html#scipy.linalg.lapack.ssyconv "scipy.linalg.lapack.ssyconv")(a,ipiv,[lower,way,overwrite\_a]) | Wrapper for `ssyconv`. |
| [`dsyconv`](generated/scipy.linalg.lapack.dsyconv.html#scipy.linalg.lapack.dsyconv "scipy.linalg.lapack.dsyconv")(a,ipiv,[lower,way,overwrite\_a]) | Wrapper for `dsyconv`. |
| [`csyconv`](generated/scipy.linalg.lapack.csyconv.html#scipy.linalg.lapack.csyconv "scipy.linalg.lapack.csyconv")(a,ipiv,[lower,way,overwrite\_a]) | Wrapper for `csyconv`. |
| [`zsyconv`](generated/scipy.linalg.lapack.zsyconv.html#scipy.linalg.lapack.zsyconv "scipy.linalg.lapack.zsyconv")(a,ipiv,[lower,way,overwrite\_a]) | Wrapper for `zsyconv`. |
| [`ssyequb`](generated/scipy.linalg.lapack.ssyequb.html#scipy.linalg.lapack.ssyequb "scipy.linalg.lapack.ssyequb")(a,[lower]) | Wrapper for `ssyequb`. |
| [`dsyequb`](generated/scipy.linalg.lapack.dsyequb.html#scipy.linalg.lapack.dsyequb "scipy.linalg.lapack.dsyequb")(a,[lower]) | Wrapper for `dsyequb`. |
| [`csyequb`](generated/scipy.linalg.lapack.csyequb.html#scipy.linalg.lapack.csyequb "scipy.linalg.lapack.csyequb")(a,[lower]) | Wrapper for `csyequb`. |
| [`zsyequb`](generated/scipy.linalg.lapack.zsyequb.html#scipy.linalg.lapack.zsyequb "scipy.linalg.lapack.zsyequb")(a,[lower]) | Wrapper for `zsyequb`. |
| [`ssyev`](generated/scipy.linalg.lapack.ssyev.html#scipy.linalg.lapack.ssyev "scipy.linalg.lapack.ssyev")(a,[compute\_v,lower,lwork,overwrite\_a]) | Wrapper for `ssyev`. |
| [`dsyev`](generated/scipy.linalg.lapack.dsyev.html#scipy.linalg.lapack.dsyev "scipy.linalg.lapack.dsyev")(a,[compute\_v,lower,lwork,overwrite\_a]) | Wrapper for `dsyev`. |
| [`ssyev_lwork`](generated/scipy.linalg.lapack.ssyev_lwork.html#scipy.linalg.lapack.ssyev_lwork "scipy.linalg.lapack.ssyev_lwork")(n,[lower]) | Wrapper for `ssyev_lwork`. |
| [`dsyev_lwork`](generated/scipy.linalg.lapack.dsyev_lwork.html#scipy.linalg.lapack.dsyev_lwork "scipy.linalg.lapack.dsyev_lwork")(n,[lower]) | Wrapper for `dsyev_lwork`. |
| [`ssyevd`](generated/scipy.linalg.lapack.ssyevd.html#scipy.linalg.lapack.ssyevd "scipy.linalg.lapack.ssyevd")(...) | Wrapper for `ssyevd`. |
| [`dsyevd`](generated/scipy.linalg.lapack.dsyevd.html#scipy.linalg.lapack.dsyevd "scipy.linalg.lapack.dsyevd")(...) | Wrapper for `dsyevd`. |
| [`ssyevd_lwork`](generated/scipy.linalg.lapack.ssyevd_lwork.html#scipy.linalg.lapack.ssyevd_lwork "scipy.linalg.lapack.ssyevd_lwork")(n,[compute\_v,lower]) | Wrapper for `ssyevd_lwork`. |
| [`dsyevd_lwork`](generated/scipy.linalg.lapack.dsyevd_lwork.html#scipy.linalg.lapack.dsyevd_lwork "scipy.linalg.lapack.dsyevd_lwork")(n,[compute\_v,lower]) | Wrapper for `dsyevd_lwork`. |
| [`ssyevr`](generated/scipy.linalg.lapack.ssyevr.html#scipy.linalg.lapack.ssyevr "scipy.linalg.lapack.ssyevr")(...) | Wrapper for `ssyevr`. |
| [`dsyevr`](generated/scipy.linalg.lapack.dsyevr.html#scipy.linalg.lapack.dsyevr "scipy.linalg.lapack.dsyevr")(...) | Wrapper for `dsyevr`. |
| [`ssyevr_lwork`](generated/scipy.linalg.lapack.ssyevr_lwork.html#scipy.linalg.lapack.ssyevr_lwork "scipy.linalg.lapack.ssyevr_lwork")(n,[lower]) | Wrapper for `ssyevr_lwork`. |
| [`dsyevr_lwork`](generated/scipy.linalg.lapack.dsyevr_lwork.html#scipy.linalg.lapack.dsyevr_lwork "scipy.linalg.lapack.dsyevr_lwork")(n,[lower]) | Wrapper for `dsyevr_lwork`. |
| [`ssyevx`](generated/scipy.linalg.lapack.ssyevx.html#scipy.linalg.lapack.ssyevx "scipy.linalg.lapack.ssyevx")(...) | Wrapper for `ssyevx`. |
| [`dsyevx`](generated/scipy.linalg.lapack.dsyevx.html#scipy.linalg.lapack.dsyevx "scipy.linalg.lapack.dsyevx")(...) | Wrapper for `dsyevx`. |
| [`ssyevx_lwork`](generated/scipy.linalg.lapack.ssyevx_lwork.html#scipy.linalg.lapack.ssyevx_lwork "scipy.linalg.lapack.ssyevx_lwork")(n,[lower]) | Wrapper for `ssyevx_lwork`. |
| [`dsyevx_lwork`](generated/scipy.linalg.lapack.dsyevx_lwork.html#scipy.linalg.lapack.dsyevx_lwork "scipy.linalg.lapack.dsyevx_lwork")(n,[lower]) | Wrapper for `dsyevx_lwork`. |
| [`ssygst`](generated/scipy.linalg.lapack.ssygst.html#scipy.linalg.lapack.ssygst "scipy.linalg.lapack.ssygst")(a,b,[itype,lower,overwrite\_a]) | Wrapper for `ssygst`. |
| [`dsygst`](generated/scipy.linalg.lapack.dsygst.html#scipy.linalg.lapack.dsygst "scipy.linalg.lapack.dsygst")(a,b,[itype,lower,overwrite\_a]) | Wrapper for `dsygst`. |
| [`ssygv`](generated/scipy.linalg.lapack.ssygv.html#scipy.linalg.lapack.ssygv "scipy.linalg.lapack.ssygv")(...) | Wrapper for `ssygv`. |
| [`dsygv`](generated/scipy.linalg.lapack.dsygv.html#scipy.linalg.lapack.dsygv "scipy.linalg.lapack.dsygv")(...) | Wrapper for `dsygv`. |
| [`ssygv_lwork`](generated/scipy.linalg.lapack.ssygv_lwork.html#scipy.linalg.lapack.ssygv_lwork "scipy.linalg.lapack.ssygv_lwork")(n,[uplo]) | Wrapper for `ssygv_lwork`. |
| [`dsygv_lwork`](generated/scipy.linalg.lapack.dsygv_lwork.html#scipy.linalg.lapack.dsygv_lwork "scipy.linalg.lapack.dsygv_lwork")(n,[uplo]) | Wrapper for `dsygv_lwork`. |
| [`ssygvd`](generated/scipy.linalg.lapack.ssygvd.html#scipy.linalg.lapack.ssygvd "scipy.linalg.lapack.ssygvd")(...) | Wrapper for `ssygvd`. |
| [`dsygvd`](generated/scipy.linalg.lapack.dsygvd.html#scipy.linalg.lapack.dsygvd "scipy.linalg.lapack.dsygvd")(...) | Wrapper for `dsygvd`. |
| [`ssygvx`](generated/scipy.linalg.lapack.ssygvx.html#scipy.linalg.lapack.ssygvx "scipy.linalg.lapack.ssygvx")(...) | Wrapper for `ssygvx`. |
| [`dsygvx`](generated/scipy.linalg.lapack.dsygvx.html#scipy.linalg.lapack.dsygvx "scipy.linalg.lapack.dsygvx")(...) | Wrapper for `dsygvx`. |
| [`ssygvx_lwork`](generated/scipy.linalg.lapack.ssygvx_lwork.html#scipy.linalg.lapack.ssygvx_lwork "scipy.linalg.lapack.ssygvx_lwork")(n,[uplo]) | Wrapper for `ssygvx_lwork`. |
| [`dsygvx_lwork`](generated/scipy.linalg.lapack.dsygvx_lwork.html#scipy.linalg.lapack.dsygvx_lwork "scipy.linalg.lapack.dsygvx_lwork")(n,[uplo]) | Wrapper for `dsygvx_lwork`. |
| [`ssysv`](generated/scipy.linalg.lapack.ssysv.html#scipy.linalg.lapack.ssysv "scipy.linalg.lapack.ssysv")(a,b,[lwork,lower,overwrite\_a,overwrite\_b]) | Wrapper for `ssysv`. |
| [`dsysv`](generated/scipy.linalg.lapack.dsysv.html#scipy.linalg.lapack.dsysv "scipy.linalg.lapack.dsysv")(a,b,[lwork,lower,overwrite\_a,overwrite\_b]) | Wrapper for `dsysv`. |
| [`csysv`](generated/scipy.linalg.lapack.csysv.html#scipy.linalg.lapack.csysv "scipy.linalg.lapack.csysv")(a,b,[lwork,lower,overwrite\_a,overwrite\_b]) | Wrapper for `csysv`. |
| [`zsysv`](generated/scipy.linalg.lapack.zsysv.html#scipy.linalg.lapack.zsysv "scipy.linalg.lapack.zsysv")(a,b,[lwork,lower,overwrite\_a,overwrite\_b]) | Wrapper for `zsysv`. |
| [`ssysv_lwork`](generated/scipy.linalg.lapack.ssysv_lwork.html#scipy.linalg.lapack.ssysv_lwork "scipy.linalg.lapack.ssysv_lwork")(n,[lower]) | Wrapper for `ssysv_lwork`. |
| [`dsysv_lwork`](generated/scipy.linalg.lapack.dsysv_lwork.html#scipy.linalg.lapack.dsysv_lwork "scipy.linalg.lapack.dsysv_lwork")(n,[lower]) | Wrapper for `dsysv_lwork`. |
| [`csysv_lwork`](generated/scipy.linalg.lapack.csysv_lwork.html#scipy.linalg.lapack.csysv_lwork "scipy.linalg.lapack.csysv_lwork")(n,[lower]) | Wrapper for `csysv_lwork`. |
| [`zsysv_lwork`](generated/scipy.linalg.lapack.zsysv_lwork.html#scipy.linalg.lapack.zsysv_lwork "scipy.linalg.lapack.zsysv_lwork")(n,[lower]) | Wrapper for `zsysv_lwork`. |
| [`ssysvx`](generated/scipy.linalg.lapack.ssysvx.html#scipy.linalg.lapack.ssysvx "scipy.linalg.lapack.ssysvx")(...) | Wrapper for `ssysvx`. |
| [`dsysvx`](generated/scipy.linalg.lapack.dsysvx.html#scipy.linalg.lapack.dsysvx "scipy.linalg.lapack.dsysvx")(...) | Wrapper for `dsysvx`. |
| [`csysvx`](generated/scipy.linalg.lapack.csysvx.html#scipy.linalg.lapack.csysvx "scipy.linalg.lapack.csysvx")(...) | Wrapper for `csysvx`. |
| [`zsysvx`](generated/scipy.linalg.lapack.zsysvx.html#scipy.linalg.lapack.zsysvx "scipy.linalg.lapack.zsysvx")(...) | Wrapper for `zsysvx`. |
| [`ssysvx_lwork`](generated/scipy.linalg.lapack.ssysvx_lwork.html#scipy.linalg.lapack.ssysvx_lwork "scipy.linalg.lapack.ssysvx_lwork")(n,[lower]) | Wrapper for `ssysvx_lwork`. |
| [`dsysvx_lwork`](generated/scipy.linalg.lapack.dsysvx_lwork.html#scipy.linalg.lapack.dsysvx_lwork "scipy.linalg.lapack.dsysvx_lwork")(n,[lower]) | Wrapper for `dsysvx_lwork`. |
| [`csysvx_lwork`](generated/scipy.linalg.lapack.csysvx_lwork.html#scipy.linalg.lapack.csysvx_lwork "scipy.linalg.lapack.csysvx_lwork")(n,[lower]) | Wrapper for `csysvx_lwork`. |
| [`zsysvx_lwork`](generated/scipy.linalg.lapack.zsysvx_lwork.html#scipy.linalg.lapack.zsysvx_lwork "scipy.linalg.lapack.zsysvx_lwork")(n,[lower]) | Wrapper for `zsysvx_lwork`. |
| [`ssytf2`](generated/scipy.linalg.lapack.ssytf2.html#scipy.linalg.lapack.ssytf2 "scipy.linalg.lapack.ssytf2")(a,[lower,overwrite\_a]) | Wrapper for `ssytf2`. |
| [`dsytf2`](generated/scipy.linalg.lapack.dsytf2.html#scipy.linalg.lapack.dsytf2 "scipy.linalg.lapack.dsytf2")(a,[lower,overwrite\_a]) | Wrapper for `dsytf2`. |
| [`csytf2`](generated/scipy.linalg.lapack.csytf2.html#scipy.linalg.lapack.csytf2 "scipy.linalg.lapack.csytf2")(a,[lower,overwrite\_a]) | Wrapper for `csytf2`. |
| [`zsytf2`](generated/scipy.linalg.lapack.zsytf2.html#scipy.linalg.lapack.zsytf2 "scipy.linalg.lapack.zsytf2")(a,[lower,overwrite\_a]) | Wrapper for `zsytf2`. |
| [`ssytrd`](generated/scipy.linalg.lapack.ssytrd.html#scipy.linalg.lapack.ssytrd "scipy.linalg.lapack.ssytrd")(a,[lower,lwork,overwrite\_a]) | Wrapper for `ssytrd`. |
| [`dsytrd`](generated/scipy.linalg.lapack.dsytrd.html#scipy.linalg.lapack.dsytrd "scipy.linalg.lapack.dsytrd")(a,[lower,lwork,overwrite\_a]) | Wrapper for `dsytrd`. |
| [`ssytrd_lwork`](generated/scipy.linalg.lapack.ssytrd_lwork.html#scipy.linalg.lapack.ssytrd_lwork "scipy.linalg.lapack.ssytrd_lwork")(n,[lower]) | Wrapper for `ssytrd_lwork`. |
| [`dsytrd_lwork`](generated/scipy.linalg.lapack.dsytrd_lwork.html#scipy.linalg.lapack.dsytrd_lwork "scipy.linalg.lapack.dsytrd_lwork")(n,[lower]) | Wrapper for `dsytrd_lwork`. |
| [`ssytrf`](generated/scipy.linalg.lapack.ssytrf.html#scipy.linalg.lapack.ssytrf "scipy.linalg.lapack.ssytrf")(a,[lower,lwork,overwrite\_a]) | Wrapper for `ssytrf`. |
| [`dsytrf`](generated/scipy.linalg.lapack.dsytrf.html#scipy.linalg.lapack.dsytrf "scipy.linalg.lapack.dsytrf")(a,[lower,lwork,overwrite\_a]) | Wrapper for `dsytrf`. |
| [`csytrf`](generated/scipy.linalg.lapack.csytrf.html#scipy.linalg.lapack.csytrf "scipy.linalg.lapack.csytrf")(a,[lower,lwork,overwrite\_a]) | Wrapper for `csytrf`. |
| [`zsytrf`](generated/scipy.linalg.lapack.zsytrf.html#scipy.linalg.lapack.zsytrf "scipy.linalg.lapack.zsytrf")(a,[lower,lwork,overwrite\_a]) | Wrapper for `zsytrf`. |
| [`ssytrf_lwork`](generated/scipy.linalg.lapack.ssytrf_lwork.html#scipy.linalg.lapack.ssytrf_lwork "scipy.linalg.lapack.ssytrf_lwork")(n,[lower]) | Wrapper for `ssytrf_lwork`. |
| [`dsytrf_lwork`](generated/scipy.linalg.lapack.dsytrf_lwork.html#scipy.linalg.lapack.dsytrf_lwork "scipy.linalg.lapack.dsytrf_lwork")(n,[lower]) | Wrapper for `dsytrf_lwork`. |
| [`csytrf_lwork`](generated/scipy.linalg.lapack.csytrf_lwork.html#scipy.linalg.lapack.csytrf_lwork "scipy.linalg.lapack.csytrf_lwork")(n,[lower]) | Wrapper for `csytrf_lwork`. |
| [`zsytrf_lwork`](generated/scipy.linalg.lapack.zsytrf_lwork.html#scipy.linalg.lapack.zsytrf_lwork "scipy.linalg.lapack.zsytrf_lwork")(n,[lower]) | Wrapper for `zsytrf_lwork`. |
| [`ssytri`](generated/scipy.linalg.lapack.ssytri.html#scipy.linalg.lapack.ssytri "scipy.linalg.lapack.ssytri")(a,ipiv,[lower,overwrite\_a]) | Wrapper for `ssytri`. |
| [`dsytri`](generated/scipy.linalg.lapack.dsytri.html#scipy.linalg.lapack.dsytri "scipy.linalg.lapack.dsytri")(a,ipiv,[lower,overwrite\_a]) | Wrapper for `dsytri`. |
| [`csytri`](generated/scipy.linalg.lapack.csytri.html#scipy.linalg.lapack.csytri "scipy.linalg.lapack.csytri")(a,ipiv,[lower,overwrite\_a]) | Wrapper for `csytri`. |
| [`zsytri`](generated/scipy.linalg.lapack.zsytri.html#scipy.linalg.lapack.zsytri "scipy.linalg.lapack.zsytri")(a,ipiv,[lower,overwrite\_a]) | Wrapper for `zsytri`. |
| [`ssytrs`](generated/scipy.linalg.lapack.ssytrs.html#scipy.linalg.lapack.ssytrs "scipy.linalg.lapack.ssytrs")(a,ipiv,b,[lower,overwrite\_b]) | Wrapper for `ssytrs`. |
| [`dsytrs`](generated/scipy.linalg.lapack.dsytrs.html#scipy.linalg.lapack.dsytrs "scipy.linalg.lapack.dsytrs")(a,ipiv,b,[lower,overwrite\_b]) | Wrapper for `dsytrs`. |
| [`csytrs`](generated/scipy.linalg.lapack.csytrs.html#scipy.linalg.lapack.csytrs "scipy.linalg.lapack.csytrs")(a,ipiv,b,[lower,overwrite\_b]) | Wrapper for `csytrs`. |
| [`zsytrs`](generated/scipy.linalg.lapack.zsytrs.html#scipy.linalg.lapack.zsytrs "scipy.linalg.lapack.zsytrs")(a,ipiv,b,[lower,overwrite\_b]) | Wrapper for `zsytrs`. |
| [`stbtrs`](generated/scipy.linalg.lapack.stbtrs.html#scipy.linalg.lapack.stbtrs "scipy.linalg.lapack.stbtrs")(ab,b,[uplo,trans,diag,overwrite\_b]) | Wrapper for `stbtrs`. |
| [`dtbtrs`](generated/scipy.linalg.lapack.dtbtrs.html#scipy.linalg.lapack.dtbtrs "scipy.linalg.lapack.dtbtrs")(ab,b,[uplo,trans,diag,overwrite\_b]) | Wrapper for `dtbtrs`. |
| [`ctbtrs`](generated/scipy.linalg.lapack.ctbtrs.html#scipy.linalg.lapack.ctbtrs "scipy.linalg.lapack.ctbtrs")(ab,b,[uplo,trans,diag,overwrite\_b]) | Wrapper for `ctbtrs`. |
| [`ztbtrs`](generated/scipy.linalg.lapack.ztbtrs.html#scipy.linalg.lapack.ztbtrs "scipy.linalg.lapack.ztbtrs")(ab,b,[uplo,trans,diag,overwrite\_b]) | Wrapper for `ztbtrs`. |
| [`stfsm`](generated/scipy.linalg.lapack.stfsm.html#scipy.linalg.lapack.stfsm "scipy.linalg.lapack.stfsm")(...) | Wrapper for `stfsm`. |
| [`dtfsm`](generated/scipy.linalg.lapack.dtfsm.html#scipy.linalg.lapack.dtfsm "scipy.linalg.lapack.dtfsm")(...) | Wrapper for `dtfsm`. |
| [`ctfsm`](generated/scipy.linalg.lapack.ctfsm.html#scipy.linalg.lapack.ctfsm "scipy.linalg.lapack.ctfsm")(...) | Wrapper for `ctfsm`. |
| [`ztfsm`](generated/scipy.linalg.lapack.ztfsm.html#scipy.linalg.lapack.ztfsm "scipy.linalg.lapack.ztfsm")(...) | Wrapper for `ztfsm`. |
| [`stfttp`](generated/scipy.linalg.lapack.stfttp.html#scipy.linalg.lapack.stfttp "scipy.linalg.lapack.stfttp")(n,arf,[transr,uplo]) | Wrapper for `stfttp`. |
| [`dtfttp`](generated/scipy.linalg.lapack.dtfttp.html#scipy.linalg.lapack.dtfttp "scipy.linalg.lapack.dtfttp")(n,arf,[transr,uplo]) | Wrapper for `dtfttp`. |
| [`ctfttp`](generated/scipy.linalg.lapack.ctfttp.html#scipy.linalg.lapack.ctfttp "scipy.linalg.lapack.ctfttp")(n,arf,[transr,uplo]) | Wrapper for `ctfttp`. |
| [`ztfttp`](generated/scipy.linalg.lapack.ztfttp.html#scipy.linalg.lapack.ztfttp "scipy.linalg.lapack.ztfttp")(n,arf,[transr,uplo]) | Wrapper for `ztfttp`. |
| [`stfttr`](generated/scipy.linalg.lapack.stfttr.html#scipy.linalg.lapack.stfttr "scipy.linalg.lapack.stfttr")(n,arf,[transr,uplo]) | Wrapper for `stfttr`. |
| [`dtfttr`](generated/scipy.linalg.lapack.dtfttr.html#scipy.linalg.lapack.dtfttr "scipy.linalg.lapack.dtfttr")(n,arf,[transr,uplo]) | Wrapper for `dtfttr`. |
| [`ctfttr`](generated/scipy.linalg.lapack.ctfttr.html#scipy.linalg.lapack.ctfttr "scipy.linalg.lapack.ctfttr")(n,arf,[transr,uplo]) | Wrapper for `ctfttr`. |
| [`ztfttr`](generated/scipy.linalg.lapack.ztfttr.html#scipy.linalg.lapack.ztfttr "scipy.linalg.lapack.ztfttr")(n,arf,[transr,uplo]) | Wrapper for `ztfttr`. |
| [`stgexc`](generated/scipy.linalg.lapack.stgexc.html#scipy.linalg.lapack.stgexc "scipy.linalg.lapack.stgexc")(...) | Wrapper for `stgexc`. |
| [`dtgexc`](generated/scipy.linalg.lapack.dtgexc.html#scipy.linalg.lapack.dtgexc "scipy.linalg.lapack.dtgexc")(...) | Wrapper for `dtgexc`. |
| [`ctgexc`](generated/scipy.linalg.lapack.ctgexc.html#scipy.linalg.lapack.ctgexc "scipy.linalg.lapack.ctgexc")(...) | Wrapper for `ctgexc`. |
| [`ztgexc`](generated/scipy.linalg.lapack.ztgexc.html#scipy.linalg.lapack.ztgexc "scipy.linalg.lapack.ztgexc")(...) | Wrapper for `ztgexc`. |
| [`stgsen`](generated/scipy.linalg.lapack.stgsen.html#scipy.linalg.lapack.stgsen "scipy.linalg.lapack.stgsen")(...) | Wrapper for `stgsen`. |
| [`dtgsen`](generated/scipy.linalg.lapack.dtgsen.html#scipy.linalg.lapack.dtgsen "scipy.linalg.lapack.dtgsen")(...) | Wrapper for `dtgsen`. |
| [`ctgsen`](generated/scipy.linalg.lapack.ctgsen.html#scipy.linalg.lapack.ctgsen "scipy.linalg.lapack.ctgsen")(...) | Wrapper for `ctgsen`. |
| [`ztgsen`](generated/scipy.linalg.lapack.ztgsen.html#scipy.linalg.lapack.ztgsen "scipy.linalg.lapack.ztgsen")(...) | Wrapper for `ztgsen`. |
| [`stgsen_lwork`](generated/scipy.linalg.lapack.stgsen_lwork.html#scipy.linalg.lapack.stgsen_lwork "scipy.linalg.lapack.stgsen_lwork")(select,a,[ijob]) | Wrapper for `stgsen_lwork`. |
| [`dtgsen_lwork`](generated/scipy.linalg.lapack.dtgsen_lwork.html#scipy.linalg.lapack.dtgsen_lwork "scipy.linalg.lapack.dtgsen_lwork")(select,a,[ijob]) | Wrapper for `dtgsen_lwork`. |
| [`ctgsen_lwork`](generated/scipy.linalg.lapack.ctgsen_lwork.html#scipy.linalg.lapack.ctgsen_lwork "scipy.linalg.lapack.ctgsen_lwork")(select,a,b,[ijob]) | Wrapper for `ctgsen_lwork`. |
| [`ztgsen_lwork`](generated/scipy.linalg.lapack.ztgsen_lwork.html#scipy.linalg.lapack.ztgsen_lwork "scipy.linalg.lapack.ztgsen_lwork")(select,a,b,[ijob]) | Wrapper for `ztgsen_lwork`. |
| [`stgsyl`](generated/scipy.linalg.lapack.stgsyl.html#scipy.linalg.lapack.stgsyl "scipy.linalg.lapack.stgsyl")(...) | Wrapper for `stgsyl`. |
| [`dtgsyl`](generated/scipy.linalg.lapack.dtgsyl.html#scipy.linalg.lapack.dtgsyl "scipy.linalg.lapack.dtgsyl")(...) | Wrapper for `dtgsyl`. |
| [`stpttf`](generated/scipy.linalg.lapack.stpttf.html#scipy.linalg.lapack.stpttf "scipy.linalg.lapack.stpttf")(n,ap,[transr,uplo]) | Wrapper for `stpttf`. |
| [`dtpttf`](generated/scipy.linalg.lapack.dtpttf.html#scipy.linalg.lapack.dtpttf "scipy.linalg.lapack.dtpttf")(n,ap,[transr,uplo]) | Wrapper for `dtpttf`. |
| [`ctpttf`](generated/scipy.linalg.lapack.ctpttf.html#scipy.linalg.lapack.ctpttf "scipy.linalg.lapack.ctpttf")(n,ap,[transr,uplo]) | Wrapper for `ctpttf`. |
| [`ztpttf`](generated/scipy.linalg.lapack.ztpttf.html#scipy.linalg.lapack.ztpttf "scipy.linalg.lapack.ztpttf")(n,ap,[transr,uplo]) | Wrapper for `ztpttf`. |
| [`stpttr`](generated/scipy.linalg.lapack.stpttr.html#scipy.linalg.lapack.stpttr "scipy.linalg.lapack.stpttr")(n,ap,[uplo]) | Wrapper for `stpttr`. |
| [`dtpttr`](generated/scipy.linalg.lapack.dtpttr.html#scipy.linalg.lapack.dtpttr "scipy.linalg.lapack.dtpttr")(n,ap,[uplo]) | Wrapper for `dtpttr`. |
| [`ctpttr`](generated/scipy.linalg.lapack.ctpttr.html#scipy.linalg.lapack.ctpttr "scipy.linalg.lapack.ctpttr")(n,ap,[uplo]) | Wrapper for `ctpttr`. |
| [`ztpttr`](generated/scipy.linalg.lapack.ztpttr.html#scipy.linalg.lapack.ztpttr "scipy.linalg.lapack.ztpttr")(n,ap,[uplo]) | Wrapper for `ztpttr`. |
| [`strcon`](generated/scipy.linalg.lapack.strcon.html#scipy.linalg.lapack.strcon "scipy.linalg.lapack.strcon")(a,[norm,uplo,diag]) | Wrapper for `strcon`. |
| [`dtrcon`](generated/scipy.linalg.lapack.dtrcon.html#scipy.linalg.lapack.dtrcon "scipy.linalg.lapack.dtrcon")(a,[norm,uplo,diag]) | Wrapper for `dtrcon`. |
| [`ctrcon`](generated/scipy.linalg.lapack.ctrcon.html#scipy.linalg.lapack.ctrcon "scipy.linalg.lapack.ctrcon")(a,[norm,uplo,diag]) | Wrapper for `ctrcon`. |
| [`ztrcon`](generated/scipy.linalg.lapack.ztrcon.html#scipy.linalg.lapack.ztrcon "scipy.linalg.lapack.ztrcon")(a,[norm,uplo,diag]) | Wrapper for `ztrcon`. |
| [`strexc`](generated/scipy.linalg.lapack.strexc.html#scipy.linalg.lapack.strexc "scipy.linalg.lapack.strexc")(...) | Wrapper for `strexc`. |
| [`dtrexc`](generated/scipy.linalg.lapack.dtrexc.html#scipy.linalg.lapack.dtrexc "scipy.linalg.lapack.dtrexc")(...) | Wrapper for `dtrexc`. |
| [`ctrexc`](generated/scipy.linalg.lapack.ctrexc.html#scipy.linalg.lapack.ctrexc "scipy.linalg.lapack.ctrexc")(...) | Wrapper for `ctrexc`. |
| [`ztrexc`](generated/scipy.linalg.lapack.ztrexc.html#scipy.linalg.lapack.ztrexc "scipy.linalg.lapack.ztrexc")(...) | Wrapper for `ztrexc`. |
| [`strsen`](generated/scipy.linalg.lapack.strsen.html#scipy.linalg.lapack.strsen "scipy.linalg.lapack.strsen")(...) | Wrapper for `strsen`. |
| [`dtrsen`](generated/scipy.linalg.lapack.dtrsen.html#scipy.linalg.lapack.dtrsen "scipy.linalg.lapack.dtrsen")(...) | Wrapper for `dtrsen`. |
| [`ctrsen`](generated/scipy.linalg.lapack.ctrsen.html#scipy.linalg.lapack.ctrsen "scipy.linalg.lapack.ctrsen")(...) | Wrapper for `ctrsen`. |
| [`ztrsen`](generated/scipy.linalg.lapack.ztrsen.html#scipy.linalg.lapack.ztrsen "scipy.linalg.lapack.ztrsen")(...) | Wrapper for `ztrsen`. |
| [`strsen_lwork`](generated/scipy.linalg.lapack.strsen_lwork.html#scipy.linalg.lapack.strsen_lwork "scipy.linalg.lapack.strsen_lwork")(select,t,[job]) | Wrapper for `strsen_lwork`. |
| [`dtrsen_lwork`](generated/scipy.linalg.lapack.dtrsen_lwork.html#scipy.linalg.lapack.dtrsen_lwork "scipy.linalg.lapack.dtrsen_lwork")(select,t,[job]) | Wrapper for `dtrsen_lwork`. |
| [`ctrsen_lwork`](generated/scipy.linalg.lapack.ctrsen_lwork.html#scipy.linalg.lapack.ctrsen_lwork "scipy.linalg.lapack.ctrsen_lwork")(select,t,[job]) | Wrapper for `ctrsen_lwork`. |
| [`ztrsen_lwork`](generated/scipy.linalg.lapack.ztrsen_lwork.html#scipy.linalg.lapack.ztrsen_lwork "scipy.linalg.lapack.ztrsen_lwork")(select,t,[job]) | Wrapper for `ztrsen_lwork`. |
| [`strsyl`](generated/scipy.linalg.lapack.strsyl.html#scipy.linalg.lapack.strsyl "scipy.linalg.lapack.strsyl")(a,b,c,[trana,tranb,isgn,overwrite\_c]) | Wrapper for `strsyl`. |
| [`dtrsyl`](generated/scipy.linalg.lapack.dtrsyl.html#scipy.linalg.lapack.dtrsyl "scipy.linalg.lapack.dtrsyl")(a,b,c,[trana,tranb,isgn,overwrite\_c]) | Wrapper for `dtrsyl`. |
| [`ctrsyl`](generated/scipy.linalg.lapack.ctrsyl.html#scipy.linalg.lapack.ctrsyl "scipy.linalg.lapack.ctrsyl")(a,b,c,[trana,tranb,isgn,overwrite\_c]) | Wrapper for `ctrsyl`. |
| [`ztrsyl`](generated/scipy.linalg.lapack.ztrsyl.html#scipy.linalg.lapack.ztrsyl "scipy.linalg.lapack.ztrsyl")(a,b,c,[trana,tranb,isgn,overwrite\_c]) | Wrapper for `ztrsyl`. |
| [`strtri`](generated/scipy.linalg.lapack.strtri.html#scipy.linalg.lapack.strtri "scipy.linalg.lapack.strtri")(c,[lower,unitdiag,overwrite\_c]) | Wrapper for `strtri`. |
| [`dtrtri`](generated/scipy.linalg.lapack.dtrtri.html#scipy.linalg.lapack.dtrtri "scipy.linalg.lapack.dtrtri")(c,[lower,unitdiag,overwrite\_c]) | Wrapper for `dtrtri`. |
| [`ctrtri`](generated/scipy.linalg.lapack.ctrtri.html#scipy.linalg.lapack.ctrtri "scipy.linalg.lapack.ctrtri")(c,[lower,unitdiag,overwrite\_c]) | Wrapper for `ctrtri`. |
| [`ztrtri`](generated/scipy.linalg.lapack.ztrtri.html#scipy.linalg.lapack.ztrtri "scipy.linalg.lapack.ztrtri")(c,[lower,unitdiag,overwrite\_c]) | Wrapper for `ztrtri`. |
| [`strtrs`](generated/scipy.linalg.lapack.strtrs.html#scipy.linalg.lapack.strtrs "scipy.linalg.lapack.strtrs")(...) | Wrapper for `strtrs`. |
| [`dtrtrs`](generated/scipy.linalg.lapack.dtrtrs.html#scipy.linalg.lapack.dtrtrs "scipy.linalg.lapack.dtrtrs")(...) | Wrapper for `dtrtrs`. |
| [`ctrtrs`](generated/scipy.linalg.lapack.ctrtrs.html#scipy.linalg.lapack.ctrtrs "scipy.linalg.lapack.ctrtrs")(...) | Wrapper for `ctrtrs`. |
| [`ztrtrs`](generated/scipy.linalg.lapack.ztrtrs.html#scipy.linalg.lapack.ztrtrs "scipy.linalg.lapack.ztrtrs")(...) | Wrapper for `ztrtrs`. |
| [`strttf`](generated/scipy.linalg.lapack.strttf.html#scipy.linalg.lapack.strttf "scipy.linalg.lapack.strttf")(a,[transr,uplo]) | Wrapper for `strttf`. |
| [`dtrttf`](generated/scipy.linalg.lapack.dtrttf.html#scipy.linalg.lapack.dtrttf "scipy.linalg.lapack.dtrttf")(a,[transr,uplo]) | Wrapper for `dtrttf`. |
| [`ctrttf`](generated/scipy.linalg.lapack.ctrttf.html#scipy.linalg.lapack.ctrttf "scipy.linalg.lapack.ctrttf")(a,[transr,uplo]) | Wrapper for `ctrttf`. |
| [`ztrttf`](generated/scipy.linalg.lapack.ztrttf.html#scipy.linalg.lapack.ztrttf "scipy.linalg.lapack.ztrttf")(a,[transr,uplo]) | Wrapper for `ztrttf`. |
| [`strttp`](generated/scipy.linalg.lapack.strttp.html#scipy.linalg.lapack.strttp "scipy.linalg.lapack.strttp")(a,[uplo]) | Wrapper for `strttp`. |
| [`dtrttp`](generated/scipy.linalg.lapack.dtrttp.html#scipy.linalg.lapack.dtrttp "scipy.linalg.lapack.dtrttp")(a,[uplo]) | Wrapper for `dtrttp`. |
| [`ctrttp`](generated/scipy.linalg.lapack.ctrttp.html#scipy.linalg.lapack.ctrttp "scipy.linalg.lapack.ctrttp")(a,[uplo]) | Wrapper for `ctrttp`. |
| [`ztrttp`](generated/scipy.linalg.lapack.ztrttp.html#scipy.linalg.lapack.ztrttp "scipy.linalg.lapack.ztrttp")(a,[uplo]) | Wrapper for `ztrttp`. |
| [`stzrzf`](generated/scipy.linalg.lapack.stzrzf.html#scipy.linalg.lapack.stzrzf "scipy.linalg.lapack.stzrzf")(a,[lwork,overwrite\_a]) | Wrapper for `stzrzf`. |
| [`dtzrzf`](generated/scipy.linalg.lapack.dtzrzf.html#scipy.linalg.lapack.dtzrzf "scipy.linalg.lapack.dtzrzf")(a,[lwork,overwrite\_a]) | Wrapper for `dtzrzf`. |
| [`ctzrzf`](generated/scipy.linalg.lapack.ctzrzf.html#scipy.linalg.lapack.ctzrzf "scipy.linalg.lapack.ctzrzf")(a,[lwork,overwrite\_a]) | Wrapper for `ctzrzf`. |
| [`ztzrzf`](generated/scipy.linalg.lapack.ztzrzf.html#scipy.linalg.lapack.ztzrzf "scipy.linalg.lapack.ztzrzf")(a,[lwork,overwrite\_a]) | Wrapper for `ztzrzf`. |
| [`stzrzf_lwork`](generated/scipy.linalg.lapack.stzrzf_lwork.html#scipy.linalg.lapack.stzrzf_lwork "scipy.linalg.lapack.stzrzf_lwork")(m,Â n) | Wrapper for `stzrzf_lwork`. |
| [`dtzrzf_lwork`](generated/scipy.linalg.lapack.dtzrzf_lwork.html#scipy.linalg.lapack.dtzrzf_lwork "scipy.linalg.lapack.dtzrzf_lwork")(m,Â n) | Wrapper for `dtzrzf_lwork`. |
| [`ctzrzf_lwork`](generated/scipy.linalg.lapack.ctzrzf_lwork.html#scipy.linalg.lapack.ctzrzf_lwork "scipy.linalg.lapack.ctzrzf_lwork")(m,Â n) | Wrapper for `ctzrzf_lwork`. |
| [`ztzrzf_lwork`](generated/scipy.linalg.lapack.ztzrzf_lwork.html#scipy.linalg.lapack.ztzrzf_lwork "scipy.linalg.lapack.ztzrzf_lwork")(m,Â n) | Wrapper for `ztzrzf_lwork`. |
| [`cunghr`](generated/scipy.linalg.lapack.cunghr.html#scipy.linalg.lapack.cunghr "scipy.linalg.lapack.cunghr")(a,tau,[lo,hi,lwork,overwrite\_a]) | Wrapper for `cunghr`. |
| [`zunghr`](generated/scipy.linalg.lapack.zunghr.html#scipy.linalg.lapack.zunghr "scipy.linalg.lapack.zunghr")(a,tau,[lo,hi,lwork,overwrite\_a]) | Wrapper for `zunghr`. |
| [`cunghr_lwork`](generated/scipy.linalg.lapack.cunghr_lwork.html#scipy.linalg.lapack.cunghr_lwork "scipy.linalg.lapack.cunghr_lwork")(n,[lo,hi]) | Wrapper for `cunghr_lwork`. |
| [`zunghr_lwork`](generated/scipy.linalg.lapack.zunghr_lwork.html#scipy.linalg.lapack.zunghr_lwork "scipy.linalg.lapack.zunghr_lwork")(n,[lo,hi]) | Wrapper for `zunghr_lwork`. |
| [`cungqr`](generated/scipy.linalg.lapack.cungqr.html#scipy.linalg.lapack.cungqr "scipy.linalg.lapack.cungqr")(a,tau,[lwork,overwrite\_a]) | Wrapper for `cungqr`. |
| [`zungqr`](generated/scipy.linalg.lapack.zungqr.html#scipy.linalg.lapack.zungqr "scipy.linalg.lapack.zungqr")(a,tau,[lwork,overwrite\_a]) | Wrapper for `zungqr`. |
| [`cungrq`](generated/scipy.linalg.lapack.cungrq.html#scipy.linalg.lapack.cungrq "scipy.linalg.lapack.cungrq")(a,tau,[lwork,overwrite\_a]) | Wrapper for `cungrq`. |
| [`zungrq`](generated/scipy.linalg.lapack.zungrq.html#scipy.linalg.lapack.zungrq "scipy.linalg.lapack.zungrq")(a,tau,[lwork,overwrite\_a]) | Wrapper for `zungrq`. |
| [`cunmqr`](generated/scipy.linalg.lapack.cunmqr.html#scipy.linalg.lapack.cunmqr "scipy.linalg.lapack.cunmqr")(side,trans,a,tau,c,lwork,[overwrite\_c]) | Wrapper for `cunmqr`. |
| [`zunmqr`](generated/scipy.linalg.lapack.zunmqr.html#scipy.linalg.lapack.zunmqr "scipy.linalg.lapack.zunmqr")(side,trans,a,tau,c,lwork,[overwrite\_c]) | Wrapper for `zunmqr`. |
| [`sgeqrt`](generated/scipy.linalg.lapack.sgeqrt.html#scipy.linalg.lapack.sgeqrt "scipy.linalg.lapack.sgeqrt")(nb,a,[overwrite\_a]) | Wrapper for `sgeqrt`. |
| [`dgeqrt`](generated/scipy.linalg.lapack.dgeqrt.html#scipy.linalg.lapack.dgeqrt "scipy.linalg.lapack.dgeqrt")(nb,a,[overwrite\_a]) | Wrapper for `dgeqrt`. |
| [`cgeqrt`](generated/scipy.linalg.lapack.cgeqrt.html#scipy.linalg.lapack.cgeqrt "scipy.linalg.lapack.cgeqrt")(nb,a,[overwrite\_a]) | Wrapper for `cgeqrt`. |
| [`zgeqrt`](generated/scipy.linalg.lapack.zgeqrt.html#scipy.linalg.lapack.zgeqrt "scipy.linalg.lapack.zgeqrt")(nb,a,[overwrite\_a]) | Wrapper for `zgeqrt`. |
| [`sgemqrt`](generated/scipy.linalg.lapack.sgemqrt.html#scipy.linalg.lapack.sgemqrt "scipy.linalg.lapack.sgemqrt")(v,t,c,[side,trans,overwrite\_c]) | Wrapper for `sgemqrt`. |
| [`dgemqrt`](generated/scipy.linalg.lapack.dgemqrt.html#scipy.linalg.lapack.dgemqrt "scipy.linalg.lapack.dgemqrt")(v,t,c,[side,trans,overwrite\_c]) | Wrapper for `dgemqrt`. |
| [`cgemqrt`](generated/scipy.linalg.lapack.cgemqrt.html#scipy.linalg.lapack.cgemqrt "scipy.linalg.lapack.cgemqrt")(v,t,c,[side,trans,overwrite\_c]) | Wrapper for `cgemqrt`. |
| [`zgemqrt`](generated/scipy.linalg.lapack.zgemqrt.html#scipy.linalg.lapack.zgemqrt "scipy.linalg.lapack.zgemqrt")(v,t,c,[side,trans,overwrite\_c]) | Wrapper for `zgemqrt`. |
| [`sgttrf`](generated/scipy.linalg.lapack.sgttrf.html#scipy.linalg.lapack.sgttrf "scipy.linalg.lapack.sgttrf")(...) | Wrapper for `sgttrf`. |
| [`dgttrf`](generated/scipy.linalg.lapack.dgttrf.html#scipy.linalg.lapack.dgttrf "scipy.linalg.lapack.dgttrf")(...) | Wrapper for `dgttrf`. |
| [`cgttrf`](generated/scipy.linalg.lapack.cgttrf.html#scipy.linalg.lapack.cgttrf "scipy.linalg.lapack.cgttrf")(...) | Wrapper for `cgttrf`. |
| [`zgttrf`](generated/scipy.linalg.lapack.zgttrf.html#scipy.linalg.lapack.zgttrf "scipy.linalg.lapack.zgttrf")(...) | Wrapper for `zgttrf`. |
| [`sgttrs`](generated/scipy.linalg.lapack.sgttrs.html#scipy.linalg.lapack.sgttrs "scipy.linalg.lapack.sgttrs")(dl,d,du,du2,ipiv,b,[trans,overwrite\_b]) | Wrapper for `sgttrs`. |
| [`dgttrs`](generated/scipy.linalg.lapack.dgttrs.html#scipy.linalg.lapack.dgttrs "scipy.linalg.lapack.dgttrs")(dl,d,du,du2,ipiv,b,[trans,overwrite\_b]) | Wrapper for `dgttrs`. |
| [`cgttrs`](generated/scipy.linalg.lapack.cgttrs.html#scipy.linalg.lapack.cgttrs "scipy.linalg.lapack.cgttrs")(dl,d,du,du2,ipiv,b,[trans,overwrite\_b]) | Wrapper for `cgttrs`. |
| [`zgttrs`](generated/scipy.linalg.lapack.zgttrs.html#scipy.linalg.lapack.zgttrs "scipy.linalg.lapack.zgttrs")(dl,d,du,du2,ipiv,b,[trans,overwrite\_b]) | Wrapper for `zgttrs`. |
| [`sgtcon`](generated/scipy.linalg.lapack.sgtcon.html#scipy.linalg.lapack.sgtcon "scipy.linalg.lapack.sgtcon")(dl,d,du,du2,ipiv,anorm,[norm]) | Wrapper for `sgtcon`. |
| [`dgtcon`](generated/scipy.linalg.lapack.dgtcon.html#scipy.linalg.lapack.dgtcon "scipy.linalg.lapack.dgtcon")(dl,d,du,du2,ipiv,anorm,[norm]) | Wrapper for `dgtcon`. |
| [`cgtcon`](generated/scipy.linalg.lapack.cgtcon.html#scipy.linalg.lapack.cgtcon "scipy.linalg.lapack.cgtcon")(dl,d,du,du2,ipiv,anorm,[norm]) | Wrapper for `cgtcon`. |
| [`zgtcon`](generated/scipy.linalg.lapack.zgtcon.html#scipy.linalg.lapack.zgtcon "scipy.linalg.lapack.zgtcon")(dl,d,du,du2,ipiv,anorm,[norm]) | Wrapper for `zgtcon`. |
| [`stpqrt`](generated/scipy.linalg.lapack.stpqrt.html#scipy.linalg.lapack.stpqrt "scipy.linalg.lapack.stpqrt")(l,nb,a,b,[overwrite\_a,overwrite\_b]) | Wrapper for `stpqrt`. |
| [`dtpqrt`](generated/scipy.linalg.lapack.dtpqrt.html#scipy.linalg.lapack.dtpqrt "scipy.linalg.lapack.dtpqrt")(l,nb,a,b,[overwrite\_a,overwrite\_b]) | Wrapper for `dtpqrt`. |
| [`ctpqrt`](generated/scipy.linalg.lapack.ctpqrt.html#scipy.linalg.lapack.ctpqrt "scipy.linalg.lapack.ctpqrt")(l,nb,a,b,[overwrite\_a,overwrite\_b]) | Wrapper for `ctpqrt`. |
| [`ztpqrt`](generated/scipy.linalg.lapack.ztpqrt.html#scipy.linalg.lapack.ztpqrt "scipy.linalg.lapack.ztpqrt")(l,nb,a,b,[overwrite\_a,overwrite\_b]) | Wrapper for `ztpqrt`. |
| [`stpmqrt`](generated/scipy.linalg.lapack.stpmqrt.html#scipy.linalg.lapack.stpmqrt "scipy.linalg.lapack.stpmqrt")(...) | Wrapper for `stpmqrt`. |
| [`dtpmqrt`](generated/scipy.linalg.lapack.dtpmqrt.html#scipy.linalg.lapack.dtpmqrt "scipy.linalg.lapack.dtpmqrt")(...) | Wrapper for `dtpmqrt`. |
| [`ctpmqrt`](generated/scipy.linalg.lapack.ctpmqrt.html#scipy.linalg.lapack.ctpmqrt "scipy.linalg.lapack.ctpmqrt")(...) | Wrapper for `ctpmqrt`. |
| [`ztpmqrt`](generated/scipy.linalg.lapack.ztpmqrt.html#scipy.linalg.lapack.ztpmqrt "scipy.linalg.lapack.ztpmqrt")(...) | Wrapper for `ztpmqrt`. |
| [`cuncsd`](generated/scipy.linalg.lapack.cuncsd.html#scipy.linalg.lapack.cuncsd "scipy.linalg.lapack.cuncsd")(...) | Wrapper for `cuncsd`. |
| [`zuncsd`](generated/scipy.linalg.lapack.zuncsd.html#scipy.linalg.lapack.zuncsd "scipy.linalg.lapack.zuncsd")(...) | Wrapper for `zuncsd`. |
| [`cuncsd_lwork`](generated/scipy.linalg.lapack.cuncsd_lwork.html#scipy.linalg.lapack.cuncsd_lwork "scipy.linalg.lapack.cuncsd_lwork")(m,Â p,Â q) | Wrapper for `cuncsd_lwork`. |
| [`zuncsd_lwork`](generated/scipy.linalg.lapack.zuncsd_lwork.html#scipy.linalg.lapack.zuncsd_lwork "scipy.linalg.lapack.zuncsd_lwork")(m,Â p,Â q) | Wrapper for `zuncsd_lwork`. |
| [`cunmrz`](generated/scipy.linalg.lapack.cunmrz.html#scipy.linalg.lapack.cunmrz "scipy.linalg.lapack.cunmrz")(a,tau,c,[side,trans,lwork,overwrite\_c]) | Wrapper for `cunmrz`. |
| [`zunmrz`](generated/scipy.linalg.lapack.zunmrz.html#scipy.linalg.lapack.zunmrz "scipy.linalg.lapack.zunmrz")(a,tau,c,[side,trans,lwork,overwrite\_c]) | Wrapper for `zunmrz`. |
| [`cunmrz_lwork`](generated/scipy.linalg.lapack.cunmrz_lwork.html#scipy.linalg.lapack.cunmrz_lwork "scipy.linalg.lapack.cunmrz_lwork")(m,n,[side,trans]) | Wrapper for `cunmrz_lwork`. |
| [`zunmrz_lwork`](generated/scipy.linalg.lapack.zunmrz_lwork.html#scipy.linalg.lapack.zunmrz_lwork "scipy.linalg.lapack.zunmrz_lwork")(m,n,[side,trans]) | Wrapper for `zunmrz_lwork`. |
| [`ilaver`](generated/scipy.linalg.lapack.ilaver.html#scipy.linalg.lapack.ilaver "scipy.linalg.lapack.ilaver")() | Wrapper for `ilaver`. |
[previous
estimate\_rank](generated/scipy.linalg.interpolative.estimate_rank.html "previous page")
[next
get\_lapack\_funcs](generated/scipy.linalg.lapack.get_lapack_funcs.html "next page")
On this page
* [Finding functions](#finding-functions)
* [All functions](#all-functions)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/linalg.cython_lapack.html#module-scipy.linalg.cython_lapack -->
* [SciPy API](index.html)
* [Linear algebra (`scipy.linalg`)](linalg.html)
* LAPACK functions for Cython
# LAPACK functions for Cython[#](#lapack-functions-for-cython "Link to this heading")
Usable from Cython via:
```
cimport scipy.linalg.cython_lapack
```
This module provides Cython-level wrappers for all primary routines included
in LAPACK 3.4.0 except for `zcgesv` since its interface is not consistent
from LAPACK 3.4.0 to 3.6.0. It also provides some of the
fixed-api auxiliary routines.
These wrappers do not check for alignment of arrays.
Alignment should be checked before these wrappers are used.
## ILP64 support[#](#ilp64-support "Link to this heading")
Integer parameters in the function signatures use `int` for LP64
builds (the default) and `int64_t` for ILP64 builds. A convenience
typedef `blas_int` (aliasing the appropriate concrete type) is also
exported so that downstream packages can write code that works with
both variants. The build configuration can be checked at runtime via
`scipy.show_config(mode='dicts')['Build Dependencies']['blas']['cython blas ilp64']`.
Boolean (Fortran `logical`) parameters in the function signatures use `bint` for
LP64 builds and `int64_t` for ILP64 builds. A convenience typedef `blas_bint` is
exported in a similar way to `blas_int`.
Downstream packages that want to support both LP64 and ILP64 builds of SciPy
should follow this pattern:
1. Use `blas_int` for all integer variables passed to LAPACK functions. For boolean
   variables, use `blas_bint`.
2. For backwards compatibility with scipy <=1.17.0 (if desired), perform a
   **build-time check** for whether `blas_int` is available, and typedef
   it as `int` otherwise. Example for Meson:
```
# Check if scipy's cython_lapack exports blas_int (ILP64 support).
_blas_int_conf = configuration_data()
if cython.compiles('from scipy.linalg.cython_lapack cimport blas_int')
  _blas_int_conf.set('BLAS_INT_DEF', 'from scipy.linalg.cython_lapack cimport blas_int')
  _blas_int_conf.set('BLAS_BINT_DEF', 'from scipy.linalg.cython_lapack cimport blas_bint')
else
  _blas_int_conf.set('BLAS_INT_DEF', 'ctypedef int blas_int')
  _blas_int_conf.set('BLAS_BINT_DEF', 'ctypedef bint blas_bint')
endif
_blas_int_pxi = configure_file(
  input: '_blas_int.pxi.in',
  output: '_blas_int.pxi',
  configuration: _blas_int_conf,
)
```
With the file `_blas_int.pxi.in` containing two lines:
```
@BLAS_INT_DEF@
@BLAS_BINT_DEF@
```
## `cython_lapack` API[#](#cython-lapack-api "Link to this heading")
Integer types:
* blas\_int: convenience typedef for either `int` (LP64) or `int64_t` (ILP64)
* blas\_bint: convenience typedef for either `bint` (LP64) or `int64_t` (ILP64)
Raw function pointers (Fortran-style pointer arguments):
* cbbcsd
* cbdsqr
* cgbbrd
* cgbcon
* cgbequ
* cgbequb
* cgbrfs
* cgbsv
* cgbsvx
* cgbtf2
* cgbtrf
* cgbtrs
* cgebak
* cgebal
* cgebd2
* cgebrd
* cgecon
* cgeequ
* cgeequb
* cgees
* cgeesx
* cgeev
* cgeevx
* cgehd2
* cgehrd
* cgelq2
* cgelqf
* cgels
* cgelsd
* cgelss
* cgelsy
* cgemqrt
* cgeql2
* cgeqlf
* cgeqp3
* cgeqr2
* cgeqr2p
* cgeqrf
* cgeqrfp
* cgeqrt
* cgeqrt2
* cgeqrt3
* cgerfs
* cgerq2
* cgerqf
* cgesc2
* cgesdd
* cgesv
* cgesvd
* cgesvx
* cgetc2
* cgetf2
* cgetrf
* cgetri
* cgetrs
* cggbak
* cggbal
* cgges
* cggesx
* cggev
* cggevx
* cggglm
* cgghrd
* cgglse
* cggqrf
* cggrqf
* cgtcon
* cgtrfs
* cgtsv
* cgtsvx
* cgttrf
* cgttrs
* cgtts2
* chbev
* chbevd
* chbevx
* chbgst
* chbgv
* chbgvd
* chbgvx
* chbtrd
* checon
* cheequb
* cheev
* cheevd
* cheevr
* cheevx
* chegs2
* chegst
* chegv
* chegvd
* chegvx
* cherfs
* chesv
* chesvx
* cheswapr
* chetd2
* chetf2
* chetrd
* chetrf
* chetri
* chetri2
* chetri2x
* chetrs
* chetrs2
* chfrk
* chgeqz
* chla\_transtype
* chpcon
* chpev
* chpevd
* chpevx
* chpgst
* chpgv
* chpgvd
* chpgvx
* chprfs
* chpsv
* chpsvx
* chptrd
* chptrf
* chptri
* chptrs
* chsein
* chseqr
* clabrd
* clacgv
* clacn2
* clacon
* clacp2
* clacpy
* clacrm
* clacrt
* cladiv
* claed0
* claed7
* claed8
* claein
* claesy
* claev2
* clag2z
* clags2
* clagtm
* clahef
* clahqr
* clahr2
* claic1
* clals0
* clalsa
* clalsd
* clangb
* clange
* clangt
* clanhb
* clanhe
* clanhf
* clanhp
* clanhs
* clanht
* clansb
* clansp
* clansy
* clantb
* clantp
* clantr
* clapll
* clapmr
* clapmt
* claqgb
* claqge
* claqhb
* claqhe
* claqhp
* claqp2
* claqps
* claqr0
* claqr1
* claqr2
* claqr3
* claqr4
* claqr5
* claqsb
* claqsp
* claqsy
* clar1v
* clar2v
* clarcm
* clarf
* clarfb
* clarfg
* clarfgp
* clarft
* clarfx
* clargv
* clarnv
* clarrv
* clartg
* clartv
* clarz
* clarzb
* clarzt
* clascl
* claset
* clasr
* classq
* claswp
* clasyf
* clatbs
* clatdf
* clatps
* clatrd
* clatrs
* clatrz
* clauu2
* clauum
* cpbcon
* cpbequ
* cpbrfs
* cpbstf
* cpbsv
* cpbsvx
* cpbtf2
* cpbtrf
* cpbtrs
* cpftrf
* cpftri
* cpftrs
* cpocon
* cpoequ
* cpoequb
* cporfs
* cposv
* cposvx
* cpotf2
* cpotrf
* cpotri
* cpotrs
* cppcon
* cppequ
* cpprfs
* cppsv
* cppsvx
* cpptrf
* cpptri
* cpptrs
* cpstf2
* cpstrf
* cptcon
* cpteqr
* cptrfs
* cptsv
* cptsvx
* cpttrf
* cpttrs
* cptts2
* crot
* cspcon
* cspmv
* cspr
* csprfs
* cspsv
* cspsvx
* csptrf
* csptri
* csptrs
* csrscl
* cstedc
* cstegr
* cstein
* cstemr
* csteqr
* csycon
* csyconv
* csyequb
* csymv
* csyr
* csyrfs
* csysv
* csysvx
* csyswapr
* csytf2
* csytrf
* csytri
* csytri2
* csytri2x
* csytrs
* csytrs2
* ctbcon
* ctbrfs
* ctbtrs
* ctfsm
* ctftri
* ctfttp
* ctfttr
* ctgevc
* ctgex2
* ctgexc
* ctgsen
* ctgsja
* ctgsna
* ctgsy2
* ctgsyl
* ctpcon
* ctpmqrt
* ctpqrt
* ctpqrt2
* ctprfb
* ctprfs
* ctptri
* ctptrs
* ctpttf
* ctpttr
* ctrcon
* ctrevc
* ctrexc
* ctrrfs
* ctrsen
* ctrsna
* ctrsyl
* ctrti2
* ctrtri
* ctrtrs
* ctrttf
* ctrttp
* ctzrzf
* cunbdb
* cuncsd
* cung2l
* cung2r
* cungbr
* cunghr
* cungl2
* cunglq
* cungql
* cungqr
* cungr2
* cungrq
* cungtr
* cunm2l
* cunm2r
* cunmbr
* cunmhr
* cunml2
* cunmlq
* cunmql
* cunmqr
* cunmr2
* cunmr3
* cunmrq
* cunmrz
* cunmtr
* cupgtr
* cupmtr
* dbbcsd
* dbdsdc
* dbdsqr
* ddisna
* dgbbrd
* dgbcon
* dgbequ
* dgbequb
* dgbrfs
* dgbsv
* dgbsvx
* dgbtf2
* dgbtrf
* dgbtrs
* dgebak
* dgebal
* dgebd2
* dgebrd
* dgecon
* dgeequ
* dgeequb
* dgees
* dgeesx
* dgeev
* dgeevx
* dgehd2
* dgehrd
* dgejsv
* dgelq2
* dgelqf
* dgels
* dgelsd
* dgelss
* dgelsy
* dgemqrt
* dgeql2
* dgeqlf
* dgeqp3
* dgeqr2
* dgeqr2p
* dgeqrf
* dgeqrfp
* dgeqrt
* dgeqrt2
* dgeqrt3
* dgerfs
* dgerq2
* dgerqf
* dgesc2
* dgesdd
* dgesv
* dgesvd
* dgesvj
* dgesvx
* dgetc2
* dgetf2
* dgetrf
* dgetri
* dgetrs
* dggbak
* dggbal
* dgges
* dggesx
* dggev
* dggevx
* dggglm
* dgghrd
* dgglse
* dggqrf
* dggrqf
* dgsvj0
* dgsvj1
* dgtcon
* dgtrfs
* dgtsv
* dgtsvx
* dgttrf
* dgttrs
* dgtts2
* dhgeqz
* dhsein
* dhseqr
* disnan
* dlabad
* dlabrd
* dlacn2
* dlacon
* dlacpy
* dladiv
* dlae2
* dlaebz
* dlaed0
* dlaed1
* dlaed2
* dlaed3
* dlaed4
* dlaed5
* dlaed6
* dlaed7
* dlaed8
* dlaed9
* dlaeda
* dlaein
* dlaev2
* dlaexc
* dlag2
* dlag2s
* dlags2
* dlagtf
* dlagtm
* dlagts
* dlagv2
* dlahqr
* dlahr2
* dlaic1
* dlaln2
* dlals0
* dlalsa
* dlalsd
* dlamch
* dlamrg
* dlaneg
* dlangb
* dlange
* dlangt
* dlanhs
* dlansb
* dlansf
* dlansp
* dlanst
* dlansy
* dlantb
* dlantp
* dlantr
* dlanv2
* dlapll
* dlapmr
* dlapmt
* dlapy2
* dlapy3
* dlaqgb
* dlaqge
* dlaqp2
* dlaqps
* dlaqr0
* dlaqr1
* dlaqr2
* dlaqr3
* dlaqr4
* dlaqr5
* dlaqsb
* dlaqsp
* dlaqsy
* dlaqtr
* dlar1v
* dlar2v
* dlarf
* dlarfb
* dlarfg
* dlarfgp
* dlarft
* dlarfx
* dlargv
* dlarnv
* dlarra
* dlarrb
* dlarrc
* dlarrd
* dlarre
* dlarrf
* dlarrj
* dlarrk
* dlarrr
* dlarrv
* dlartg
* dlartgp
* dlartgs
* dlartv
* dlaruv
* dlarz
* dlarzb
* dlarzt
* dlas2
* dlascl
* dlasd0
* dlasd1
* dlasd2
* dlasd3
* dlasd4
* dlasd5
* dlasd6
* dlasd7
* dlasd8
* dlasda
* dlasdq
* dlasdt
* dlaset
* dlasq1
* dlasq2
* dlasq3
* dlasq4
* dlasq6
* dlasr
* dlasrt
* dlassq
* dlasv2
* dlaswp
* dlasy2
* dlasyf
* dlat2s
* dlatbs
* dlatdf
* dlatps
* dlatrd
* dlatrs
* dlatrz
* dlauu2
* dlauum
* dopgtr
* dopmtr
* dorbdb
* dorcsd
* dorg2l
* dorg2r
* dorgbr
* dorghr
* dorgl2
* dorglq
* dorgql
* dorgqr
* dorgr2
* dorgrq
* dorgtr
* dorm2l
* dorm2r
* dormbr
* dormhr
* dorml2
* dormlq
* dormql
* dormqr
* dormr2
* dormr3
* dormrq
* dormrz
* dormtr
* dpbcon
* dpbequ
* dpbrfs
* dpbstf
* dpbsv
* dpbsvx
* dpbtf2
* dpbtrf
* dpbtrs
* dpftrf
* dpftri
* dpftrs
* dpocon
* dpoequ
* dpoequb
* dporfs
* dposv
* dposvx
* dpotf2
* dpotrf
* dpotri
* dpotrs
* dppcon
* dppequ
* dpprfs
* dppsv
* dppsvx
* dpptrf
* dpptri
* dpptrs
* dpstf2
* dpstrf
* dptcon
* dpteqr
* dptrfs
* dptsv
* dptsvx
* dpttrf
* dpttrs
* dptts2
* drscl
* dsbev
* dsbevd
* dsbevx
* dsbgst
* dsbgv
* dsbgvd
* dsbgvx
* dsbtrd
* dsfrk
* dsgesv
* dspcon
* dspev
* dspevd
* dspevx
* dspgst
* dspgv
* dspgvd
* dspgvx
* dsposv
* dsprfs
* dspsv
* dspsvx
* dsptrd
* dsptrf
* dsptri
* dsptrs
* dstebz
* dstedc
* dstegr
* dstein
* dstemr
* dsteqr
* dsterf
* dstev
* dstevd
* dstevr
* dstevx
* dsycon
* dsyconv
* dsyequb
* dsyev
* dsyevd
* dsyevr
* dsyevx
* dsygs2
* dsygst
* dsygv
* dsygvd
* dsygvx
* dsyrfs
* dsysv
* dsysvx
* dsyswapr
* dsytd2
* dsytf2
* dsytrd
* dsytrf
* dsytri
* dsytri2
* dsytri2x
* dsytrs
* dsytrs2
* dtbcon
* dtbrfs
* dtbtrs
* dtfsm
* dtftri
* dtfttp
* dtfttr
* dtgevc
* dtgex2
* dtgexc
* dtgsen
* dtgsja
* dtgsna
* dtgsy2
* dtgsyl
* dtpcon
* dtpmqrt
* dtpqrt
* dtpqrt2
* dtprfb
* dtprfs
* dtptri
* dtptrs
* dtpttf
* dtpttr
* dtrcon
* dtrevc
* dtrexc
* dtrrfs
* dtrsen
* dtrsna
* dtrsyl
* dtrti2
* dtrtri
* dtrtrs
* dtrttf
* dtrttp
* dtzrzf
* dzsum1
* icmax1
* ieeeck
* ilaclc
* ilaclr
* iladiag
* iladlc
* iladlr
* ilaprec
* ilaslc
* ilaslr
* ilatrans
* ilauplo
* ilaver
* ilazlc
* ilazlr
* izmax1
* sbbcsd
* sbdsdc
* sbdsqr
* scsum1
* sdisna
* sgbbrd
* sgbcon
* sgbequ
* sgbequb
* sgbrfs
* sgbsv
* sgbsvx
* sgbtf2
* sgbtrf
* sgbtrs
* sgebak
* sgebal
* sgebd2
* sgebrd
* sgecon
* sgeequ
* sgeequb
* sgees
* sgeesx
* sgeev
* sgeevx
* sgehd2
* sgehrd
* sgejsv
* sgelq2
* sgelqf
* sgels
* sgelsd
* sgelss
* sgelsy
* sgemqrt
* sgeql2
* sgeqlf
* sgeqp3
* sgeqr2
* sgeqr2p
* sgeqrf
* sgeqrfp
* sgeqrt
* sgeqrt2
* sgeqrt3
* sgerfs
* sgerq2
* sgerqf
* sgesc2
* sgesdd
* sgesv
* sgesvd
* sgesvj
* sgesvx
* sgetc2
* sgetf2
* sgetrf
* sgetri
* sgetrs
* sggbak
* sggbal
* sgges
* sggesx
* sggev
* sggevx
* sggglm
* sgghrd
* sgglse
* sggqrf
* sggrqf
* sgsvj0
* sgsvj1
* sgtcon
* sgtrfs
* sgtsv
* sgtsvx
* sgttrf
* sgttrs
* sgtts2
* shgeqz
* shsein
* shseqr
* slabad
* slabrd
* slacn2
* slacon
* slacpy
* sladiv
* slae2
* slaebz
* slaed0
* slaed1
* slaed2
* slaed3
* slaed4
* slaed5
* slaed6
* slaed7
* slaed8
* slaed9
* slaeda
* slaein
* slaev2
* slaexc
* slag2
* slag2d
* slags2
* slagtf
* slagtm
* slagts
* slagv2
* slahqr
* slahr2
* slaic1
* slaln2
* slals0
* slalsa
* slalsd
* slamch
* slamrg
* slangb
* slange
* slangt
* slanhs
* slansb
* slansf
* slansp
* slanst
* slansy
* slantb
* slantp
* slantr
* slanv2
* slapll
* slapmr
* slapmt
* slapy2
* slapy3
* slaqgb
* slaqge
* slaqp2
* slaqps
* slaqr0
* slaqr1
* slaqr2
* slaqr3
* slaqr4
* slaqr5
* slaqsb
* slaqsp
* slaqsy
* slaqtr
* slar1v
* slar2v
* slarf
* slarfb
* slarfg
* slarfgp
* slarft
* slarfx
* slargv
* slarnv
* slarra
* slarrb
* slarrc
* slarrd
* slarre
* slarrf
* slarrj
* slarrk
* slarrr
* slarrv
* slartg
* slartgp
* slartgs
* slartv
* slaruv
* slarz
* slarzb
* slarzt
* slas2
* slascl
* slasd0
* slasd1
* slasd2
* slasd3
* slasd4
* slasd5
* slasd6
* slasd7
* slasd8
* slasda
* slasdq
* slasdt
* slaset
* slasq1
* slasq2
* slasq3
* slasq4
* slasq6
* slasr
* slasrt
* slassq
* slasv2
* slaswp
* slasy2
* slasyf
* slatbs
* slatdf
* slatps
* slatrd
* slatrs
* slatrz
* slauu2
* slauum
* sopgtr
* sopmtr
* sorbdb
* sorcsd
* sorg2l
* sorg2r
* sorgbr
* sorghr
* sorgl2
* sorglq
* sorgql
* sorgqr
* sorgr2
* sorgrq
* sorgtr
* sorm2l
* sorm2r
* sormbr
* sormhr
* sorml2
* sormlq
* sormql
* sormqr
* sormr2
* sormr3
* sormrq
* sormrz
* sormtr
* spbcon
* spbequ
* spbrfs
* spbstf
* spbsv
* spbsvx
* spbtf2
* spbtrf
* spbtrs
* spftrf
* spftri
* spftrs
* spocon
* spoequ
* spoequb
* sporfs
* sposv
* sposvx
* spotf2
* spotrf
* spotri
* spotrs
* sppcon
* sppequ
* spprfs
* sppsv
* sppsvx
* spptrf
* spptri
* spptrs
* spstf2
* spstrf
* sptcon
* spteqr
* sptrfs
* sptsv
* sptsvx
* spttrf
* spttrs
* sptts2
* srscl
* ssbev
* ssbevd
* ssbevx
* ssbgst
* ssbgv
* ssbgvd
* ssbgvx
* ssbtrd
* ssfrk
* sspcon
* sspev
* sspevd
* sspevx
* sspgst
* sspgv
* sspgvd
* sspgvx
* ssprfs
* sspsv
* sspsvx
* ssptrd
* ssptrf
* ssptri
* ssptrs
* sstebz
* sstedc
* sstegr
* sstein
* sstemr
* ssteqr
* ssterf
* sstev
* sstevd
* sstevr
* sstevx
* ssycon
* ssyconv
* ssyequb
* ssyev
* ssyevd
* ssyevr
* ssyevx
* ssygs2
* ssygst
* ssygv
* ssygvd
* ssygvx
* ssyrfs
* ssysv
* ssysvx
* ssyswapr
* ssytd2
* ssytf2
* ssytrd
* ssytrf
* ssytri
* ssytri2
* ssytri2x
* ssytrs
* ssytrs2
* stbcon
* stbrfs
* stbtrs
* stfsm
* stftri
* stfttp
* stfttr
* stgevc
* stgex2
* stgexc
* stgsen
* stgsja
* stgsna
* stgsy2
* stgsyl
* stpcon
* stpmqrt
* stpqrt
* stpqrt2
* stprfb
* stprfs
* stptri
* stptrs
* stpttf
* stpttr
* strcon
* strevc
* strexc
* strrfs
* strsen
* strsna
* strsyl
* strti2
* strtri
* strtrs
* strttf
* strttp
* stzrzf
* xerbla\_array
* zbbcsd
* zbdsqr
* zcgesv
* zcposv
* zdrscl
* zgbbrd
* zgbcon
* zgbequ
* zgbequb
* zgbrfs
* zgbsv
* zgbsvx
* zgbtf2
* zgbtrf
* zgbtrs
* zgebak
* zgebal
* zgebd2
* zgebrd
* zgecon
* zgeequ
* zgeequb
* zgees
* zgeesx
* zgeev
* zgeevx
* zgehd2
* zgehrd
* zgelq2
* zgelqf
* zgels
* zgelsd
* zgelss
* zgelsy
* zgemqrt
* zgeql2
* zgeqlf
* zgeqp3
* zgeqr2
* zgeqr2p
* zgeqrf
* zgeqrfp
* zgeqrt
* zgeqrt2
* zgeqrt3
* zgerfs
* zgerq2
* zgerqf
* zgesc2
* zgesdd
* zgesv
* zgesvd
* zgesvx
* zgetc2
* zgetf2
* zgetrf
* zgetri
* zgetrs
* zggbak
* zggbal
* zgges
* zggesx
* zggev
* zggevx
* zggglm
* zgghrd
* zgglse
* zggqrf
* zggrqf
* zgtcon
* zgtrfs
* zgtsv
* zgtsvx
* zgttrf
* zgttrs
* zgtts2
* zhbev
* zhbevd
* zhbevx
* zhbgst
* zhbgv
* zhbgvd
* zhbgvx
* zhbtrd
* zhecon
* zheequb
* zheev
* zheevd
* zheevr
* zheevx
* zhegs2
* zhegst
* zhegv
* zhegvd
* zhegvx
* zherfs
* zhesv
* zhesvx
* zheswapr
* zhetd2
* zhetf2
* zhetrd
* zhetrf
* zhetri
* zhetri2
* zhetri2x
* zhetrs
* zhetrs2
* zhfrk
* zhgeqz
* zhpcon
* zhpev
* zhpevd
* zhpevx
* zhpgst
* zhpgv
* zhpgvd
* zhpgvx
* zhprfs
* zhpsv
* zhpsvx
* zhptrd
* zhptrf
* zhptri
* zhptrs
* zhsein
* zhseqr
* zlabrd
* zlacgv
* zlacn2
* zlacon
* zlacp2
* zlacpy
* zlacrm
* zlacrt
* zladiv
* zlaed0
* zlaed7
* zlaed8
* zlaein
* zlaesy
* zlaev2
* zlag2c
* zlags2
* zlagtm
* zlahef
* zlahqr
* zlahr2
* zlaic1
* zlals0
* zlalsa
* zlalsd
* zlangb
* zlange
* zlangt
* zlanhb
* zlanhe
* zlanhf
* zlanhp
* zlanhs
* zlanht
* zlansb
* zlansp
* zlansy
* zlantb
* zlantp
* zlantr
* zlapll
* zlapmr
* zlapmt
* zlaqgb
* zlaqge
* zlaqhb
* zlaqhe
* zlaqhp
* zlaqp2
* zlaqps
* zlaqr0
* zlaqr1
* zlaqr2
* zlaqr3
* zlaqr4
* zlaqr5
* zlaqsb
* zlaqsp
* zlaqsy
* zlar1v
* zlar2v
* zlarcm
* zlarf
* zlarfb
* zlarfg
* zlarfgp
* zlarft
* zlarfx
* zlargv
* zlarnv
* zlarrv
* zlartg
* zlartv
* zlarz
* zlarzb
* zlarzt
* zlascl
* zlaset
* zlasr
* zlassq
* zlaswp
* zlasyf
* zlat2c
* zlatbs
* zlatdf
* zlatps
* zlatrd
* zlatrs
* zlatrz
* zlauu2
* zlauum
* zpbcon
* zpbequ
* zpbrfs
* zpbstf
* zpbsv
* zpbsvx
* zpbtf2
* zpbtrf
* zpbtrs
* zpftrf
* zpftri
* zpftrs
* zpocon
* zpoequ
* zpoequb
* zporfs
* zposv
* zposvx
* zpotf2
* zpotrf
* zpotri
* zpotrs
* zppcon
* zppequ
* zpprfs
* zppsv
* zppsvx
* zpptrf
* zpptri
* zpptrs
* zpstf2
* zpstrf
* zptcon
* zpteqr
* zptrfs
* zptsv
* zptsvx
* zpttrf
* zpttrs
* zptts2
* zrot
* zspcon
* zspmv
* zspr
* zsprfs
* zspsv
* zspsvx
* zsptrf
* zsptri
* zsptrs
* zstedc
* zstegr
* zstein
* zstemr
* zsteqr
* zsycon
* zsyconv
* zsyequb
* zsymv
* zsyr
* zsyrfs
* zsysv
* zsysvx
* zsyswapr
* zsytf2
* zsytrf
* zsytri
* zsytri2
* zsytri2x
* zsytrs
* zsytrs2
* ztbcon
* ztbrfs
* ztbtrs
* ztfsm
* ztftri
* ztfttp
* ztfttr
* ztgevc
* ztgex2
* ztgexc
* ztgsen
* ztgsja
* ztgsna
* ztgsy2
* ztgsyl
* ztpcon
* ztpmqrt
* ztpqrt
* ztpqrt2
* ztprfb
* ztprfs
* ztptri
* ztptrs
* ztpttf
* ztpttr
* ztrcon
* ztrevc
* ztrexc
* ztrrfs
* ztrsen
* ztrsna
* ztrsyl
* ztrti2
* ztrtri
* ztrtrs
* ztrttf
* ztrttp
* ztzrzf
* zunbdb
* zuncsd
* zung2l
* zung2r
* zungbr
* zunghr
* zungl2
* zunglq
* zungql
* zungqr
* zungr2
* zungrq
* zungtr
* zunm2l
* zunm2r
* zunmbr
* zunmhr
* zunml2
* zunmlq
* zunmql
* zunmqr
* zunmr2
* zunmr3
* zunmrq
* zunmrz
* zunmtr
* zupgtr
* zupmtr
[previous
BLAS Functions for Cython](linalg.cython_blas.html "previous page")
[next
Interpolative matrix decomposition (`scipy.linalg.interpolative`)](linalg.interpolative.html "next page")
On this page
* [ILP64 support](#ilp64-support)
* [`cython_lapack` API](#cython-lapack-api)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/linalg.interpolative.html#module-scipy.linalg.interpolative -->
* [SciPy API](index.html)
* [Linear algebra (`scipy.linalg`)](linalg.html)
* Interpolative matrix decomposition (`scipy.linalg.interpolative`)
# Interpolative matrix decomposition ([`scipy.linalg.interpolative`](#module-scipy.linalg.interpolative "scipy.linalg.interpolative"))[#](#interpolative-matrix-decomposition-scipy-linalg-interpolative "Link to this heading")
Added in version 0.13.
Changed in version 1.15.0: The underlying algorithms have been ported to Python from the original Fortran77
code. See references below for more details.
An interpolative decomposition (ID) of a matrix \(A \in
\mathbb{C}^{m \times n}\) of rank \(k \leq \min \{ m, n \}\) is a
factorization
\[A \Pi =
\begin{bmatrix}
A \Pi\_{1} & A \Pi\_{2}
\end{bmatrix} =
A \Pi\_{1}
\begin{bmatrix}
I & T
\end{bmatrix},\]
where \(\Pi = [\Pi\_{1}, \Pi\_{2}]\) is a permutation matrix with
\(\Pi\_{1} \in \{ 0, 1 \}^{n \times k}\), i.e., \(A \Pi\_{2} =
A \Pi\_{1} T\). This can equivalently be written as \(A = BP\),
where \(B = A \Pi\_{1}\) and \(P = [I, T] \Pi^{\mathsf{T}}\)
are the *skeleton* and *interpolation matrices*, respectively.
If \(A\) does not have exact rank \(k\), then there exists an
approximation in the form of an ID such that \(A = BP + E\), where
\(\| E \| \sim \sigma\_{k + 1}\) is on the order of the \((k +
1)\)-th largest singular value of \(A\). Note that \(\sigma\_{k
+ 1}\) is the best possible error for a rank-\(k\) approximation
and, in fact, is achieved by the singular value decomposition (SVD)
\(A \approx U S V^{\*}\), where \(U \in \mathbb{C}^{m \times
k}\) and \(V \in \mathbb{C}^{n \times k}\) have orthonormal columns
and \(S = \mathop{\mathrm{diag}} (\sigma\_{i}) \in \mathbb{C}^{k
\times k}\) is diagonal with nonnegative entries. The principal
advantages of using an ID over an SVD are that:
* it is cheaper to construct;
* it preserves the structure of \(A\); and
* it is more efficient to compute with in light of the identity submatrix of \(P\).
## Routines[#](#routines "Link to this heading")
Main functionality:
|  |  |
| --- | --- |
| [`interp_decomp`](generated/scipy.linalg.interpolative.interp_decomp.html#scipy.linalg.interpolative.interp_decomp "scipy.linalg.interpolative.interp_decomp")(A,Â eps\_or\_k[,Â rand,Â rng]) | Compute ID of a matrix. |
| [`reconstruct_matrix_from_id`](generated/scipy.linalg.interpolative.reconstruct_matrix_from_id.html#scipy.linalg.interpolative.reconstruct_matrix_from_id "scipy.linalg.interpolative.reconstruct_matrix_from_id")(B,Â idx,Â proj) | Reconstruct matrix from its ID. |
| [`reconstruct_interp_matrix`](generated/scipy.linalg.interpolative.reconstruct_interp_matrix.html#scipy.linalg.interpolative.reconstruct_interp_matrix "scipy.linalg.interpolative.reconstruct_interp_matrix")(idx,Â proj) | Reconstruct interpolation matrix from ID. |
| [`reconstruct_skel_matrix`](generated/scipy.linalg.interpolative.reconstruct_skel_matrix.html#scipy.linalg.interpolative.reconstruct_skel_matrix "scipy.linalg.interpolative.reconstruct_skel_matrix")(A,Â k,Â idx) | Reconstruct skeleton matrix from ID. |
| [`id_to_svd`](generated/scipy.linalg.interpolative.id_to_svd.html#scipy.linalg.interpolative.id_to_svd "scipy.linalg.interpolative.id_to_svd")(B,Â idx,Â proj) | Convert ID to SVD. |
| [`svd`](generated/scipy.linalg.interpolative.svd.html#scipy.linalg.interpolative.svd "scipy.linalg.interpolative.svd")(A,Â eps\_or\_k[,Â rand,Â rng]) | Compute SVD of a matrix via an ID. |
| [`estimate_spectral_norm`](generated/scipy.linalg.interpolative.estimate_spectral_norm.html#scipy.linalg.interpolative.estimate_spectral_norm "scipy.linalg.interpolative.estimate_spectral_norm")(A[,Â its,Â rng]) | Estimate spectral norm of a matrix by the randomized power method. |
| [`estimate_spectral_norm_diff`](generated/scipy.linalg.interpolative.estimate_spectral_norm_diff.html#scipy.linalg.interpolative.estimate_spectral_norm_diff "scipy.linalg.interpolative.estimate_spectral_norm_diff")(A,Â B[,Â its,Â rng]) | Estimate spectral norm of the difference of two matrices by the randomized power method. |
| [`estimate_rank`](generated/scipy.linalg.interpolative.estimate_rank.html#scipy.linalg.interpolative.estimate_rank "scipy.linalg.interpolative.estimate_rank")(A,Â eps[,Â rng]) | Estimate matrix rank to a specified relative precision using randomized methods. |
## References[#](#references "Link to this heading")
This module uses the algorithms found in ID software package [[R5a82238cdab4-1]](#r5a82238cdab4-1) by Martinsson,
Rokhlin, Shkolnisky, and Tygert, which is a Fortran library for computing IDs using
various algorithms, including the rank-revealing QR approach of [[R5a82238cdab4-2]](#r5a82238cdab4-2) and the more
recent randomized methods described in [[R5a82238cdab4-3]](#r5a82238cdab4-3), [[R5a82238cdab4-4]](#r5a82238cdab4-4), and [[R5a82238cdab4-5]](#r5a82238cdab4-5).
We advise the user to consult also the documentation for the [ID package](http://tygert.com/software.html).
[[R5a82238cdab4-1](#id1)]
P.G. Martinsson, V. Rokhlin, Y. Shkolnisky, M. Tygert. âID: a
software package for low-rank approximation of matrices via interpolative
decompositions, version 0.2.â <http://tygert.com/id_doc.4.pdf>.
[[R5a82238cdab4-2](#id2)]
H. Cheng, Z. Gimbutas, P.G. Martinsson, V. Rokhlin. âOn the
compression of low rank matrices.â *SIAM J. Sci. Comput.* 26 (4): 1389â1404,
2005. [DOI:10.1137/030602678](https://doi.org/10.1137/030602678).
[[R5a82238cdab4-3](#id3)]
E. Liberty, F. Woolfe, P.G. Martinsson, V. Rokhlin, M.
Tygert. âRandomized algorithms for the low-rank approximation of matrices.â
*Proc. Natl. Acad. Sci. U.S.A.* 104 (51): 20167â20172, 2007.
[DOI:10.1073/pnas.0709640104](https://doi.org/10.1073/pnas.0709640104).
[[R5a82238cdab4-4](#id4)]
P.G. Martinsson, V. Rokhlin, M. Tygert. âA randomized
algorithm for the decomposition of matrices.â *Appl. Comput. Harmon. Anal.* 30
(1): 47â68, 2011. [DOI:10.1016/j.acha.2010.02.003](https://doi.org/10.1016/j.acha.2010.02.003).
[[R5a82238cdab4-5](#id5)]
F. Woolfe, E. Liberty, V. Rokhlin, M. Tygert. âA fast
randomized algorithm for the approximation of matrices.â *Appl. Comput.
Harmon. Anal.* 25 (3): 335â366, 2008. [DOI:10.1016/j.acha.2007.12.002](https://doi.org/10.1016/j.acha.2007.12.002).
## Tutorial[#](#tutorial "Link to this heading")
### Initializing[#](#initializing "Link to this heading")
The first step is to import [`scipy.linalg.interpolative`](#module-scipy.linalg.interpolative "scipy.linalg.interpolative") by issuing the
command:
```
>>> import scipy.linalg.interpolative as sli
```
Now letâs build a matrix. For this, we consider a Hilbert matrix, which is well
know to have low rank:
```
>>> from scipy.linalg import hilbert
>>> n = 1000
>>> A = hilbert(n)
```
We can also do this explicitly via:
```
>>> import numpy as np
>>> n = 1000
>>> A = np.empty((n, n), order='F')
>>> for j in range(n):
...     for i in range(n):
...         A[i,j] = 1. / (i + j + 1)
```
Note the use of the flag `order='F'` in [`numpy.empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "(in NumPy v2.4)"). This
instantiates the matrix in Fortran-contiguous order and is important for
avoiding data copying when passing to the backend.
We then define multiplication routines for the matrix by regarding it as a
[`scipy.sparse.linalg.LinearOperator`](generated/scipy.sparse.linalg.LinearOperator.html#scipy.sparse.linalg.LinearOperator "scipy.sparse.linalg.LinearOperator"):
```
>>> from scipy.sparse.linalg import aslinearoperator
>>> L = aslinearoperator(A)
```
This automatically sets up methods describing the action of the matrix and its
adjoint on a vector.
### Computing an ID[#](#computing-an-id "Link to this heading")
We have several choices of algorithm to compute an ID. These fall largely
according to two dichotomies:
1. how the matrix is represented, i.e., via its entries or via its action on a
   vector; and
2. whether to approximate it to a fixed relative precision or to a fixed rank.
We step through each choice in turn below.
In all cases, the ID is represented by three parameters:
1. a rank `k`;
2. an index array `idx`; and
3. interpolation coefficients `proj`.
The ID is specified by the relation
`np.dot(A[:,idx[:k]], proj) == A[:,idx[k:]]`.
#### From matrix entries[#](#from-matrix-entries "Link to this heading")
We first consider a matrix given in terms of its entries.
To compute an ID to a fixed precision, type:
```
>>> eps = 1e-3
>>> k, idx, proj = sli.interp_decomp(A, eps)
```
where `eps < 1` is the desired precision.
To compute an ID to a fixed rank, use:
```
>>> idx, proj = sli.interp_decomp(A, k)
```
where `k >= 1` is the desired rank.
Both algorithms use random sampling and are usually faster than the
corresponding older, deterministic algorithms, which can be accessed via the
commands:
```
>>> k, idx, proj = sli.interp_decomp(A, eps, rand=False)
```
and:
```
>>> idx, proj = sli.interp_decomp(A, k, rand=False)
```
respectively.
#### From matrix action[#](#from-matrix-action "Link to this heading")
Now consider a matrix given in terms of its action on a vector as a
[`scipy.sparse.linalg.LinearOperator`](generated/scipy.sparse.linalg.LinearOperator.html#scipy.sparse.linalg.LinearOperator "scipy.sparse.linalg.LinearOperator").
To compute an ID to a fixed precision, type:
```
>>> k, idx, proj = sli.interp_decomp(L, eps)
```
To compute an ID to a fixed rank, use:
```
>>> idx, proj = sli.interp_decomp(L, k)
```
These algorithms are randomized.
### Reconstructing an ID[#](#reconstructing-an-id "Link to this heading")
The ID routines above do not output the skeleton and interpolation matrices
explicitly but instead return the relevant information in a more compact (and
sometimes more useful) form. To build these matrices, write:
```
>>> B = sli.reconstruct_skel_matrix(A, k, idx)
```
for the skeleton matrix and:
```
>>> P = sli.reconstruct_interp_matrix(idx, proj)
```
for the interpolation matrix. The ID approximation can then be computed as:
```
>>> C = np.dot(B, P)
```
This can also be constructed directly using:
```
>>> C = sli.reconstruct_matrix_from_id(B, idx, proj)
```
without having to first compute `P`.
Alternatively, this can be done explicitly as well using:
```
>>> B = A[:,idx[:k]]
>>> P = np.hstack([np.eye(k), proj])[:,np.argsort(idx)]
>>> C = np.dot(B, P)
```
### Computing an SVD[#](#computing-an-svd "Link to this heading")
An ID can be converted to an SVD via the command:
```
>>> U, S, V = sli.id_to_svd(B, idx, proj)
```
The SVD approximation is then:
```
>>> approx = U @ np.diag(S) @ V.conj().T
```
The SVD can also be computed âfreshâ by combining both the ID and conversion
steps into one command. Following the various ID algorithms above, there are
correspondingly various SVD algorithms that one can employ.
#### From matrix entries[#](#id6 "Link to this heading")
We consider first SVD algorithms for a matrix given in terms of its entries.
To compute an SVD to a fixed precision, type:
```
>>> U, S, V = sli.svd(A, eps)
```
To compute an SVD to a fixed rank, use:
```
>>> U, S, V = sli.svd(A, k)
```
Both algorithms use random sampling; for the deterministic versions, issue the
keyword `rand=False` as above.
#### From matrix action[#](#id7 "Link to this heading")
Now consider a matrix given in terms of its action on a vector.
To compute an SVD to a fixed precision, type:
```
>>> U, S, V = sli.svd(L, eps)
```
To compute an SVD to a fixed rank, use:
```
>>> U, S, V = sli.svd(L, k)
```
### Utility routines[#](#utility-routines "Link to this heading")
Several utility routines are also available.
To estimate the spectral norm of a matrix, use:
```
>>> snorm = sli.estimate_spectral_norm(A)
```
This algorithm is based on the randomized power method and thus requires only
matrix-vector products. The number of iterations to take can be set using the
keyword `its` (default: `its=20`). The matrix is interpreted as a
[`scipy.sparse.linalg.LinearOperator`](generated/scipy.sparse.linalg.LinearOperator.html#scipy.sparse.linalg.LinearOperator "scipy.sparse.linalg.LinearOperator"), but it is also valid to supply it
as a [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.4)"), in which case it is trivially converted using
[`scipy.sparse.linalg.aslinearoperator`](generated/scipy.sparse.linalg.aslinearoperator.html#scipy.sparse.linalg.aslinearoperator "scipy.sparse.linalg.aslinearoperator").
The same algorithm can also estimate the spectral norm of the difference of two
matrices `A1` and `A2` as follows:
```
>>> A1, A2 = A**2, A
>>> diff = sli.estimate_spectral_norm_diff(A1, A2)
```
This is often useful for checking the accuracy of a matrix approximation.
Some routines in [`scipy.linalg.interpolative`](#module-scipy.linalg.interpolative "scipy.linalg.interpolative") require estimating the rank
of a matrix as well. This can be done with either:
```
>>> k = sli.estimate_rank(A, eps)
```
or:
```
>>> k = sli.estimate_rank(L, eps)
```
depending on the representation. The parameter `eps` controls the definition
of the numerical rank.
Finally, the random number generation required for all randomized routines can
be controlled via providing NumPy pseudo-random generators with a fixed seed. See
[`numpy.random.Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "(in NumPy v2.4)") and [`numpy.random.default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "(in NumPy v2.4)") for more details.
### Remarks[#](#remarks "Link to this heading")
The above functions all automatically detect the appropriate interface and work
with both real and complex data types, passing input arguments to the proper
backend routine.
[previous
LAPACK functions for Cython](linalg.cython_lapack.html "previous page")
[next
interp\_decomp](generated/scipy.linalg.interpolative.interp_decomp.html "next page")
On this page
* [Routines](#routines)
* [References](#references)
* [Tutorial](#tutorial)
  + [Initializing](#initializing)
  + [Computing an ID](#computing-an-id)
    - [From matrix entries](#from-matrix-entries)
    - [From matrix action](#from-matrix-action)
  + [Reconstructing an ID](#reconstructing-an-id)
  + [Computing an SVD](#computing-an-svd)
    - [From matrix entries](#id6)
    - [From matrix action](#id7)
  + [Utility routines](#utility-routines)
  + [Remarks](#remarks)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/ndimage.html#module-scipy.ndimage -->
* [SciPy API](index.html)
* Multidimensional image processing (`scipy.ndimage`)
# Multidimensional image processing ([`scipy.ndimage`](#module-scipy.ndimage "scipy.ndimage"))[#](#multidimensional-image-processing-scipy-ndimage "Link to this heading")
This package contains various functions for multidimensional image
processing.
## Filters[#](#filters "Link to this heading")
|  |  |
| --- | --- |
| [`convolve`](generated/scipy.ndimage.convolve.html#scipy.ndimage.convolve "scipy.ndimage.convolve")(input,Â weights[,Â output,Â mode,Â ...]) | Multidimensional convolution. |
| [`convolve1d`](generated/scipy.ndimage.convolve1d.html#scipy.ndimage.convolve1d "scipy.ndimage.convolve1d")(input,Â weights[,Â axis,Â output,Â ...]) | Calculate a 1-D convolution along the given axis. |
| [`correlate`](generated/scipy.ndimage.correlate.html#scipy.ndimage.correlate "scipy.ndimage.correlate")(input,Â weights[,Â output,Â mode,Â ...]) | Multidimensional correlation. |
| [`correlate1d`](generated/scipy.ndimage.correlate1d.html#scipy.ndimage.correlate1d "scipy.ndimage.correlate1d")(input,Â weights[,Â axis,Â output,Â ...]) | Calculate a 1-D correlation along the given axis. |
| [`gaussian_filter`](generated/scipy.ndimage.gaussian_filter.html#scipy.ndimage.gaussian_filter "scipy.ndimage.gaussian_filter")(input,Â sigma[,Â order,Â ...]) | Multidimensional Gaussian filter. |
| [`gaussian_filter1d`](generated/scipy.ndimage.gaussian_filter1d.html#scipy.ndimage.gaussian_filter1d "scipy.ndimage.gaussian_filter1d")(input,Â sigma[,Â axis,Â ...]) | 1-D Gaussian filter. |
| [`gaussian_gradient_magnitude`](generated/scipy.ndimage.gaussian_gradient_magnitude.html#scipy.ndimage.gaussian_gradient_magnitude "scipy.ndimage.gaussian_gradient_magnitude")(input,Â sigma[,Â ...]) | Multidimensional gradient magnitude using Gaussian derivatives. |
| [`gaussian_laplace`](generated/scipy.ndimage.gaussian_laplace.html#scipy.ndimage.gaussian_laplace "scipy.ndimage.gaussian_laplace")(input,Â sigma[,Â output,Â ...]) | Multidimensional Laplace filter using Gaussian second derivatives. |
| [`generic_filter`](generated/scipy.ndimage.generic_filter.html#scipy.ndimage.generic_filter "scipy.ndimage.generic_filter")(input,Â function[,Â size,Â ...]) | Calculate a multidimensional filter using the given function. |
| [`generic_filter1d`](generated/scipy.ndimage.generic_filter1d.html#scipy.ndimage.generic_filter1d "scipy.ndimage.generic_filter1d")(input,Â function,Â filter\_size) | Calculate a 1-D filter along the given axis. |
| [`generic_gradient_magnitude`](generated/scipy.ndimage.generic_gradient_magnitude.html#scipy.ndimage.generic_gradient_magnitude "scipy.ndimage.generic_gradient_magnitude")(input,Â derivative) | Gradient magnitude using a provided gradient function. |
| [`generic_laplace`](generated/scipy.ndimage.generic_laplace.html#scipy.ndimage.generic_laplace "scipy.ndimage.generic_laplace")(input,Â derivative2[,Â ...]) | N-D Laplace filter using a provided second derivative function. |
| [`laplace`](generated/scipy.ndimage.laplace.html#scipy.ndimage.laplace "scipy.ndimage.laplace")(input[,Â output,Â mode,Â cval,Â axes]) | N-D Laplace filter based on approximate second derivatives. |
| [`maximum_filter`](generated/scipy.ndimage.maximum_filter.html#scipy.ndimage.maximum_filter "scipy.ndimage.maximum_filter")(input[,Â size,Â footprint,Â ...]) | Calculate a multidimensional maximum filter. |
| [`maximum_filter1d`](generated/scipy.ndimage.maximum_filter1d.html#scipy.ndimage.maximum_filter1d "scipy.ndimage.maximum_filter1d")(input,Â size[,Â axis,Â ...]) | Calculate a 1-D maximum filter along the given axis. |
| [`median_filter`](generated/scipy.ndimage.median_filter.html#scipy.ndimage.median_filter "scipy.ndimage.median_filter")(input[,Â size,Â footprint,Â ...]) | Calculate a multidimensional median filter. |
| [`minimum_filter`](generated/scipy.ndimage.minimum_filter.html#scipy.ndimage.minimum_filter "scipy.ndimage.minimum_filter")(input[,Â size,Â footprint,Â ...]) | Calculate a multidimensional minimum filter. |
| [`minimum_filter1d`](generated/scipy.ndimage.minimum_filter1d.html#scipy.ndimage.minimum_filter1d "scipy.ndimage.minimum_filter1d")(input,Â size[,Â axis,Â ...]) | Calculate a 1-D minimum filter along the given axis. |
| [`percentile_filter`](generated/scipy.ndimage.percentile_filter.html#scipy.ndimage.percentile_filter "scipy.ndimage.percentile_filter")(input,Â percentile[,Â size,Â ...]) | Calculate a multidimensional percentile filter. |
| [`prewitt`](generated/scipy.ndimage.prewitt.html#scipy.ndimage.prewitt "scipy.ndimage.prewitt")(input[,Â axis,Â output,Â mode,Â cval]) | Calculate a Prewitt filter. |
| [`rank_filter`](generated/scipy.ndimage.rank_filter.html#scipy.ndimage.rank_filter "scipy.ndimage.rank_filter")(input,Â rank[,Â size,Â footprint,Â ...]) | Calculate a multidimensional rank filter. |
| [`sobel`](generated/scipy.ndimage.sobel.html#scipy.ndimage.sobel "scipy.ndimage.sobel")(input[,Â axis,Â output,Â mode,Â cval]) | Calculate a Sobel filter. |
| [`uniform_filter`](generated/scipy.ndimage.uniform_filter.html#scipy.ndimage.uniform_filter "scipy.ndimage.uniform_filter")(input[,Â size,Â output,Â mode,Â ...]) | Multidimensional uniform filter. |
| [`uniform_filter1d`](generated/scipy.ndimage.uniform_filter1d.html#scipy.ndimage.uniform_filter1d "scipy.ndimage.uniform_filter1d")(input,Â size[,Â axis,Â ...]) | Calculate a 1-D uniform filter along the given axis. |
| [`vectorized_filter`](generated/scipy.ndimage.vectorized_filter.html#scipy.ndimage.vectorized_filter "scipy.ndimage.vectorized_filter")(input,Â function,Â \*[,Â ...]) | Filter an array with a vectorized Python callable as the kernel. |
## Fourier filters[#](#fourier-filters "Link to this heading")
|  |  |
| --- | --- |
| [`fourier_ellipsoid`](generated/scipy.ndimage.fourier_ellipsoid.html#scipy.ndimage.fourier_ellipsoid "scipy.ndimage.fourier_ellipsoid")(input,Â size[,Â n,Â axis,Â output]) | Multidimensional ellipsoid Fourier filter. |
| [`fourier_gaussian`](generated/scipy.ndimage.fourier_gaussian.html#scipy.ndimage.fourier_gaussian "scipy.ndimage.fourier_gaussian")(input,Â sigma[,Â n,Â axis,Â output]) | Multidimensional Gaussian fourier filter. |
| [`fourier_shift`](generated/scipy.ndimage.fourier_shift.html#scipy.ndimage.fourier_shift "scipy.ndimage.fourier_shift")(input,Â shift[,Â n,Â axis,Â output]) | Multidimensional Fourier shift filter. |
| [`fourier_uniform`](generated/scipy.ndimage.fourier_uniform.html#scipy.ndimage.fourier_uniform "scipy.ndimage.fourier_uniform")(input,Â size[,Â n,Â axis,Â output]) | Multidimensional uniform fourier filter. |
## Interpolation[#](#interpolation "Link to this heading")
|  |  |
| --- | --- |
| [`affine_transform`](generated/scipy.ndimage.affine_transform.html#scipy.ndimage.affine_transform "scipy.ndimage.affine_transform")(input,Â matrix[,Â offset,Â ...]) | Apply an affine transformation. |
| [`geometric_transform`](generated/scipy.ndimage.geometric_transform.html#scipy.ndimage.geometric_transform "scipy.ndimage.geometric_transform")(input,Â mapping[,Â ...]) | Apply an arbitrary geometric transform. |
| [`map_coordinates`](generated/scipy.ndimage.map_coordinates.html#scipy.ndimage.map_coordinates "scipy.ndimage.map_coordinates")(input,Â coordinates[,Â ...]) | Map the input array to new coordinates by interpolation. |
| [`rotate`](generated/scipy.ndimage.rotate.html#scipy.ndimage.rotate "scipy.ndimage.rotate")(input,Â angle[,Â axes,Â reshape,Â ...]) | Rotate an array. |
| [`shift`](generated/scipy.ndimage.shift.html#scipy.ndimage.shift "scipy.ndimage.shift")(input,Â shift[,Â output,Â order,Â mode,Â ...]) | Shift an array. |
| [`spline_filter`](generated/scipy.ndimage.spline_filter.html#scipy.ndimage.spline_filter "scipy.ndimage.spline_filter")(input[,Â order,Â output,Â mode]) | Multidimensional spline filter. |
| [`spline_filter1d`](generated/scipy.ndimage.spline_filter1d.html#scipy.ndimage.spline_filter1d "scipy.ndimage.spline_filter1d")(input[,Â order,Â axis,Â ...]) | Calculate a 1-D spline filter along the given axis. |
| [`zoom`](generated/scipy.ndimage.zoom.html#scipy.ndimage.zoom "scipy.ndimage.zoom")(input,Â zoom[,Â output,Â order,Â mode,Â ...]) | Zoom an array. |
## Measurements[#](#measurements "Link to this heading")
|  |  |
| --- | --- |
| [`center_of_mass`](generated/scipy.ndimage.center_of_mass.html#scipy.ndimage.center_of_mass "scipy.ndimage.center_of_mass")(input[,Â labels,Â index]) | Calculate the center of mass of the values of an array at labels. |
| [`extrema`](generated/scipy.ndimage.extrema.html#scipy.ndimage.extrema "scipy.ndimage.extrema")(input[,Â labels,Â index]) | Calculate the minimums and maximums of the values of an array at labels, along with their positions. |
| [`find_objects`](generated/scipy.ndimage.find_objects.html#scipy.ndimage.find_objects "scipy.ndimage.find_objects")(input[,Â max\_label]) | Find objects in a labeled array. |
| [`histogram`](generated/scipy.ndimage.histogram.html#scipy.ndimage.histogram "scipy.ndimage.histogram")(input,Â min,Â max,Â bins[,Â labels,Â index]) | Calculate the histogram of the values of an array, optionally at labels. |
| [`label`](generated/scipy.ndimage.label.html#scipy.ndimage.label "scipy.ndimage.label")(input[,Â structure,Â output]) | Label features in an array. |
| [`labeled_comprehension`](generated/scipy.ndimage.labeled_comprehension.html#scipy.ndimage.labeled_comprehension "scipy.ndimage.labeled_comprehension")(input,Â labels,Â index,Â ...) | Roughly equivalent to [func(input[labels == i]) for i in index]. |
| [`maximum`](generated/scipy.ndimage.maximum.html#scipy.ndimage.maximum "scipy.ndimage.maximum")(input[,Â labels,Â index]) | Calculate the maximum of the values of an array over labeled regions. |
| [`maximum_position`](generated/scipy.ndimage.maximum_position.html#scipy.ndimage.maximum_position "scipy.ndimage.maximum_position")(input[,Â labels,Â index]) | Find the positions of the maximums of the values of an array at labels. |
| [`mean`](generated/scipy.ndimage.mean.html#scipy.ndimage.mean "scipy.ndimage.mean")(input[,Â labels,Â index]) | Calculate the mean of the values of an array at labels. |
| [`median`](generated/scipy.ndimage.median.html#scipy.ndimage.median "scipy.ndimage.median")(input[,Â labels,Â index]) | Calculate the median of the values of an array over labeled regions. |
| [`minimum`](generated/scipy.ndimage.minimum.html#scipy.ndimage.minimum "scipy.ndimage.minimum")(input[,Â labels,Â index]) | Calculate the minimum of the values of an array over labeled regions. |
| [`minimum_position`](generated/scipy.ndimage.minimum_position.html#scipy.ndimage.minimum_position "scipy.ndimage.minimum_position")(input[,Â labels,Â index]) | Find the positions of the minimums of the values of an array at labels. |
| [`standard_deviation`](generated/scipy.ndimage.standard_deviation.html#scipy.ndimage.standard_deviation "scipy.ndimage.standard_deviation")(input[,Â labels,Â index]) | Calculate the standard deviation of the values of an N-D image array, optionally at specified sub-regions. |
| [`sum_labels`](generated/scipy.ndimage.sum_labels.html#scipy.ndimage.sum_labels "scipy.ndimage.sum_labels")(input[,Â labels,Â index]) | Calculate the sum of the values of the array. |
| [`value_indices`](generated/scipy.ndimage.value_indices.html#scipy.ndimage.value_indices "scipy.ndimage.value_indices")(arr,Â \*[,Â ignore\_value]) | Find indices of each distinct value in given array. |
| [`variance`](generated/scipy.ndimage.variance.html#scipy.ndimage.variance "scipy.ndimage.variance")(input[,Â labels,Â index]) | Calculate the variance of the values of an N-D image array, optionally at specified sub-regions. |
| [`watershed_ift`](generated/scipy.ndimage.watershed_ift.html#scipy.ndimage.watershed_ift "scipy.ndimage.watershed_ift")(input,Â markers[,Â structure,Â ...]) | Apply watershed from markers using image foresting transform algorithm. |
## Morphology[#](#morphology "Link to this heading")
|  |  |
| --- | --- |
| [`binary_closing`](generated/scipy.ndimage.binary_closing.html#scipy.ndimage.binary_closing "scipy.ndimage.binary_closing")(input[,Â structure,Â ...]) | Multidimensional binary closing with the given structuring element. |
| [`binary_dilation`](generated/scipy.ndimage.binary_dilation.html#scipy.ndimage.binary_dilation "scipy.ndimage.binary_dilation")(input[,Â structure,Â ...]) | Multidimensional binary dilation with the given structuring element. |
| [`binary_erosion`](generated/scipy.ndimage.binary_erosion.html#scipy.ndimage.binary_erosion "scipy.ndimage.binary_erosion")(input[,Â structure,Â ...]) | Multidimensional binary erosion with a given structuring element. |
| [`binary_fill_holes`](generated/scipy.ndimage.binary_fill_holes.html#scipy.ndimage.binary_fill_holes "scipy.ndimage.binary_fill_holes")(input[,Â structure,Â ...]) | Fill the holes in binary objects. |
| [`binary_hit_or_miss`](generated/scipy.ndimage.binary_hit_or_miss.html#scipy.ndimage.binary_hit_or_miss "scipy.ndimage.binary_hit_or_miss")(input[,Â structure1,Â ...]) | Multidimensional binary hit-or-miss transform. |
| [`binary_opening`](generated/scipy.ndimage.binary_opening.html#scipy.ndimage.binary_opening "scipy.ndimage.binary_opening")(input[,Â structure,Â ...]) | Multidimensional binary opening with the given structuring element. |
| [`binary_propagation`](generated/scipy.ndimage.binary_propagation.html#scipy.ndimage.binary_propagation "scipy.ndimage.binary_propagation")(input[,Â structure,Â mask,Â ...]) | Multidimensional binary propagation with the given structuring element. |
| [`black_tophat`](generated/scipy.ndimage.black_tophat.html#scipy.ndimage.black_tophat "scipy.ndimage.black_tophat")(input[,Â size,Â footprint,Â ...]) | Multidimensional black tophat filter. |
| [`distance_transform_bf`](generated/scipy.ndimage.distance_transform_bf.html#scipy.ndimage.distance_transform_bf "scipy.ndimage.distance_transform_bf")(input[,Â metric,Â ...]) | Distance transform function by a brute force algorithm. |
| [`distance_transform_cdt`](generated/scipy.ndimage.distance_transform_cdt.html#scipy.ndimage.distance_transform_cdt "scipy.ndimage.distance_transform_cdt")(input[,Â metric,Â ...]) | Distance transform for chamfer type of transforms. |
| [`distance_transform_edt`](generated/scipy.ndimage.distance_transform_edt.html#scipy.ndimage.distance_transform_edt "scipy.ndimage.distance_transform_edt")(input[,Â sampling,Â ...]) | Exact Euclidean distance transform. |
| [`generate_binary_structure`](generated/scipy.ndimage.generate_binary_structure.html#scipy.ndimage.generate_binary_structure "scipy.ndimage.generate_binary_structure")(rank,Â connectivity) | Generate a binary structure for binary morphological operations. |
| [`grey_closing`](generated/scipy.ndimage.grey_closing.html#scipy.ndimage.grey_closing "scipy.ndimage.grey_closing")(input[,Â size,Â footprint,Â ...]) | Multidimensional grayscale closing. |
| [`grey_dilation`](generated/scipy.ndimage.grey_dilation.html#scipy.ndimage.grey_dilation "scipy.ndimage.grey_dilation")(input[,Â size,Â footprint,Â ...]) | Calculate a greyscale dilation, using either a structuring element, or a footprint corresponding to a flat structuring element. |
| [`grey_erosion`](generated/scipy.ndimage.grey_erosion.html#scipy.ndimage.grey_erosion "scipy.ndimage.grey_erosion")(input[,Â size,Â footprint,Â ...]) | Calculate a greyscale erosion, using either a structuring element, or a footprint corresponding to a flat structuring element. |
| [`grey_opening`](generated/scipy.ndimage.grey_opening.html#scipy.ndimage.grey_opening "scipy.ndimage.grey_opening")(input[,Â size,Â footprint,Â ...]) | Multidimensional grayscale opening. |
| [`iterate_structure`](generated/scipy.ndimage.iterate_structure.html#scipy.ndimage.iterate_structure "scipy.ndimage.iterate_structure")(structure,Â iterations[,Â ...]) | Iterate a structure by dilating it with itself. |
| [`morphological_gradient`](generated/scipy.ndimage.morphological_gradient.html#scipy.ndimage.morphological_gradient "scipy.ndimage.morphological_gradient")(input[,Â size,Â ...]) | Multidimensional morphological gradient. |
| [`morphological_laplace`](generated/scipy.ndimage.morphological_laplace.html#scipy.ndimage.morphological_laplace "scipy.ndimage.morphological_laplace")(input[,Â size,Â ...]) | Multidimensional morphological laplace. |
| [`white_tophat`](generated/scipy.ndimage.white_tophat.html#scipy.ndimage.white_tophat "scipy.ndimage.white_tophat")(input[,Â size,Â footprint,Â ...]) | Multidimensional white tophat filter. |
[previous
find\_best\_blas\_type](generated/scipy.linalg.find_best_blas_type.html "previous page")
[next
convolve](generated/scipy.ndimage.convolve.html "next page")
On this page
* [Filters](#filters)
* [Fourier filters](#fourier-filters)
* [Interpolation](#interpolation)
* [Measurements](#measurements)
* [Morphology](#morphology)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/odr.html#module-scipy.odr -->
* [SciPy API](index.html)
* Orthogonal distance regression (`scipy.odr`)
# Orthogonal distance regression ([`scipy.odr`](#module-scipy.odr "scipy.odr"))[#](#orthogonal-distance-regression-scipy-odr "Link to this heading")
Deprecated since version 1.17.0: [`scipy.odr`](#module-scipy.odr "scipy.odr") is deprecated and will be removed in SciPy 1.19.0. Please use
[pypi.org/project/odrpack/](https://pypi.org/project/odrpack/)
instead.
The following example shows a brief comparison of the APIs:
```
import numpy as np
import scipy.odr
import odrpack
# Classic "Pearson data" that motivates ODR.
# Errors are in both variables, and if you don't account for this,
# doing a linear fit of X vs. Y or Y vs. X will give you quite
# different results.
p_x = np.array([0., .9, 1.8, 2.6, 3.3, 4.4, 5.2, 6.1, 6.5, 7.4])
p_y = np.array([5.9, 5.4, 4.4, 4.6, 3.5, 3.7, 2.8, 2.8, 2.4, 1.5])
p_sx = np.array([.03, .03, .04, .035, .07, .11, .13, .22, .74, 1.])
p_sy = np.array([1., .74, .5, .35, .22, .22, .12, .12, .1, .04])
# Old-style
# The RealData class takes care of details like turning
# standard-deviation error bars into weights.
p_dat = scipy.odr.RealData(p_x, p_y, sx=p_sx, sy=p_sy)
# Note, parameters come before `x` in scipy.odr
p_mod = scipy.odr.Model(lambda beta, x: beta[0] + beta[1]*x)
p_odr = scipy.odr.ODR(p_dat, p_mod, beta0=[1., 1.])
old_out = p_odr.run()
# New-style
# Parameters come after data, in the new API.
# We must convert the error bars into weights ourselves.
new_out = odrpack.odr_fit(lambda x, beta: beta[0] + beta[1] * x,
    p_x, p_y, beta0=np.array([1.0, 1.0]),
    weight_x=p_sx**-2, weight_y=p_sy**-2)
assert np.isclose(old_out.beta, new_out.beta).all()
```
## Package Content[#](#package-content "Link to this heading")
|  |  |
| --- | --- |
| [`Data`](generated/scipy.odr.Data.html#scipy.odr.Data "scipy.odr.Data")(x[,Â y,Â we,Â wd,Â fix,Â meta]) | The data to fit. |
| [`RealData`](generated/scipy.odr.RealData.html#scipy.odr.RealData "scipy.odr.RealData")(x[,Â y,Â sx,Â sy,Â covx,Â covy,Â fix,Â meta]) | The data, with weightings as actual standard deviations and/or covariances. |
| [`Model`](generated/scipy.odr.Model.html#scipy.odr.Model "scipy.odr.Model")(fcn[,Â fjacb,Â fjacd,Â extra\_args,Â ...]) | The Model class stores information about the function you wish to fit. |
| [`ODR`](generated/scipy.odr.ODR.html#scipy.odr.ODR "scipy.odr.ODR")(data,Â model[,Â beta0,Â delta0,Â ifixb,Â ...]) | The ODR class gathers all information and coordinates the running of the main fitting routine. |
| [`Output`](generated/scipy.odr.Output.html#scipy.odr.Output "scipy.odr.Output")(output) | The Output class stores the output of an ODR run. |
| [`odr`](generated/odr-function.html#scipy.odr.odr "scipy.odr.odr")(fcn,Â beta0,Â y,Â x[,Â we,Â wd,Â fjacb,Â ...]) | Low-level function for ODR. |
| [`OdrWarning`](generated/scipy.odr.OdrWarning.html#scipy.odr.OdrWarning "scipy.odr.OdrWarning") | Warning indicating that the data passed into ODR will cause problems when passed into 'odr' that the user should be aware of. |
| [`OdrError`](generated/scipy.odr.OdrError.html#scipy.odr.OdrError "scipy.odr.OdrError") | Exception indicating an error in fitting. |
| [`OdrStop`](generated/scipy.odr.OdrStop.html#scipy.odr.OdrStop "scipy.odr.OdrStop") | Exception stopping fitting. |
| [`polynomial`](generated/scipy.odr.polynomial.html#scipy.odr.polynomial "scipy.odr.polynomial")(order) | Factory function for a general polynomial model. |
| [`exponential`](generated/scipy.odr.exponential.html#scipy.odr.exponential "scipy.odr.exponential") | Exponential model |
| [`multilinear`](generated/scipy.odr.multilinear.html#scipy.odr.multilinear "scipy.odr.multilinear") | Arbitrary-dimensional linear model |
| [`unilinear`](generated/scipy.odr.unilinear.html#scipy.odr.unilinear "scipy.odr.unilinear") | Univariate linear model |
| [`quadratic`](generated/scipy.odr.quadratic.html#scipy.odr.quadratic "scipy.odr.quadratic") | Quadratic model |
## Usage information[#](#usage-information "Link to this heading")
### Introduction[#](#introduction "Link to this heading")
Why Orthogonal Distance Regression (ODR)? Sometimes one has
measurement errors in the explanatory (a.k.a., âindependentâ)
variable(s), not just the response (a.k.a., âdependentâ) variable(s).
Ordinary Least Squares (OLS) fitting procedures treat the data for
explanatory variables as fixed, i.e., not subject to error of any kind.
Furthermore, OLS procedures require that the response variables be an
explicit function of the explanatory variables; sometimes making the
equation explicit is impractical and/or introduces errors. ODR can
handle both of these cases with ease, and can even reduce to the OLS
case if that is sufficient for the problem.
ODRPACK is a FORTRAN-77 library for performing ODR with possibly
non-linear fitting functions. It uses a modified trust-region
Levenberg-Marquardt-type algorithm [[1]](#r12d0b3321264-1) to estimate the function
parameters. The fitting functions are provided by Python functions
operating on NumPy arrays. The required derivatives may be provided
by Python functions as well, or may be estimated numerically. ODRPACK
can do explicit or implicit ODR fits, or it can do OLS. Input and
output variables may be multidimensional. Weights can be provided to
account for different variances of the observations, and even
covariances between dimensions of the variables.
The [`scipy.odr`](#module-scipy.odr "scipy.odr") package offers an object-oriented interface to
ODRPACK, in addition to the low-level [`odr`](generated/odr-function.html#scipy.odr.odr "scipy.odr.odr") function.
Additional background information about ODRPACK can be found in the
[ODRPACK Userâs Guide](https://docs.scipy.org/doc/external/odrpack_guide.pdf), reading
which is recommended.
### Basic usage[#](#basic-usage "Link to this heading")
1. Define the function you want to fit against.:
   ```
   def f(B, x):
       '''Linear function y = m*x + b'''
       # B is a vector of the parameters.
       # x is an array of the current x values.
       # x is in the same format as the x passed to Data or RealData.
       #
       # Return an array in the same format as y passed to Data or RealData.
       return B[0]*x + B[1]
   ```
2. Create a Model.:
   ```
   linear = Model(f)
   ```
3. Create a Data or RealData instance.:
   ```
   mydata = Data(x, y, wd=1./power(sx,2), we=1./power(sy,2))
   ```
   or, when the actual covariances are known:
   ```
   mydata = RealData(x, y, sx=sx, sy=sy)
   ```
4. Instantiate ODR with your data, model and initial parameter estimate.:
   ```
   myodr = ODR(mydata, linear, beta0=[1., 2.])
   ```
5. Run the fit.:
   ```
   myoutput = myodr.run()
   ```
6. Examine output.:
   ```
   myoutput.pprint()
   ```
### References[#](#references "Link to this heading")
[[1](#id1)]
P. T. Boggs and J. E. Rogers, âOrthogonal Distance Regression,â
in âStatistical analysis of measurement error models and
applications: proceedings of the AMS-IMS-SIAM joint summer research
conference held June 10-16, 1989,â Contemporary Mathematics,
vol. 112, pg. 186, 1990.
[previous
white\_tophat](generated/scipy.ndimage.white_tophat.html "previous page")
[next
Data](generated/scipy.odr.Data.html "next page")
On this page
* [Package Content](#package-content)
* [Usage information](#usage-information)
  + [Introduction](#introduction)
  + [Basic usage](#basic-usage)
  + [References](#references)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/optimize.html#module-scipy.optimize -->
* [SciPy API](index.html)
* Optimization and root finding (`scipy.optimize`)
# Optimization and root finding ([`scipy.optimize`](#module-scipy.optimize "scipy.optimize"))[#](#optimization-and-root-finding-scipy-optimize "Link to this heading")
SciPy `optimize` provides functions for minimizing (or maximizing)
objective functions, possibly subject to constraints. It includes
solvers for nonlinear problems (with support for both local and global
optimization algorithms), linear programming, constrained
and nonlinear least-squares, root finding, and curve fitting.
Common functions and objects, shared across different solvers, are:
|  |  |
| --- | --- |
| [`show_options`](generated/scipy.optimize.show_options.html#scipy.optimize.show_options "scipy.optimize.show_options")([solver,Â method,Â disp]) | Show documentation for additional options of optimization solvers. |
| [`OptimizeResult`](generated/scipy.optimize.OptimizeResult.html#scipy.optimize.OptimizeResult "scipy.optimize.OptimizeResult") | Represents the optimization result. |
| [`OptimizeWarning`](generated/scipy.optimize.OptimizeWarning.html#scipy.optimize.OptimizeWarning "scipy.optimize.OptimizeWarning") | General warning for [`scipy.optimize`](#module-scipy.optimize "scipy.optimize"). |
## Optimization[#](#optimization "Link to this heading")
### Scalar functions optimization[#](#scalar-functions-optimization "Link to this heading")
|  |  |
| --- | --- |
| [`minimize_scalar`](generated/scipy.optimize.minimize_scalar.html#scipy.optimize.minimize_scalar "scipy.optimize.minimize_scalar")(fun[,Â bracket,Â bounds,Â ...]) | Local minimization of scalar function of one variable. |
The [`minimize_scalar`](generated/scipy.optimize.minimize_scalar.html#scipy.optimize.minimize_scalar "scipy.optimize.minimize_scalar") function supports the following methods:
* [minimize\_scalar(method=âbrentâ)](optimize.minimize_scalar-brent.html)
* [minimize\_scalar(method=âboundedâ)](optimize.minimize_scalar-bounded.html)
* [minimize\_scalar(method=âgoldenâ)](optimize.minimize_scalar-golden.html)
### Local (multivariate) optimization[#](#local-multivariate-optimization "Link to this heading")
|  |  |
| --- | --- |
| [`minimize`](generated/scipy.optimize.minimize.html#scipy.optimize.minimize "scipy.optimize.minimize")(fun,Â x0[,Â args,Â method,Â jac,Â hess,Â ...]) | Minimization of scalar function of one or more variables. |
The [`minimize`](generated/scipy.optimize.minimize.html#scipy.optimize.minimize "scipy.optimize.minimize") function supports the following methods:
* [minimize(method=âNelder-Meadâ)](optimize.minimize-neldermead.html)
* [minimize(method=âPowellâ)](optimize.minimize-powell.html)
* [minimize(method=âCGâ)](optimize.minimize-cg.html)
* [minimize(method=âBFGSâ)](optimize.minimize-bfgs.html)
* [minimize(method=âNewton-CGâ)](optimize.minimize-newtoncg.html)
* [minimize(method=âL-BFGS-Bâ)](optimize.minimize-lbfgsb.html)
* [minimize(method=âTNCâ)](optimize.minimize-tnc.html)
* [minimize(method=âCOBYLAâ)](optimize.minimize-cobyla.html)
* [minimize(method=âCOBYQAâ)](optimize.minimize-cobyqa.html)
* [minimize(method=âSLSQPâ)](optimize.minimize-slsqp.html)
* [minimize(method=âtrust-constrâ)](optimize.minimize-trustconstr.html)
* [minimize(method=âdoglegâ)](optimize.minimize-dogleg.html)
* [minimize(method=âtrust-ncgâ)](optimize.minimize-trustncg.html)
* [minimize(method=âtrust-krylovâ)](optimize.minimize-trustkrylov.html)
* [minimize(method=âtrust-exactâ)](optimize.minimize-trustexact.html)
Constraints are passed to [`minimize`](generated/scipy.optimize.minimize.html#scipy.optimize.minimize "scipy.optimize.minimize") function as a single object or
as a list of objects from the following classes:
|  |  |
| --- | --- |
| [`NonlinearConstraint`](generated/scipy.optimize.NonlinearConstraint.html#scipy.optimize.NonlinearConstraint "scipy.optimize.NonlinearConstraint")(fun,Â lb,Â ub[,Â jac,Â ...]) | Nonlinear constraint on the variables. |
| [`LinearConstraint`](generated/scipy.optimize.LinearConstraint.html#scipy.optimize.LinearConstraint "scipy.optimize.LinearConstraint")(A[,Â lb,Â ub,Â keep\_feasible]) | Linear constraint on the variables. |
Simple bound constraints are handled separately and there is a special class
for them:
|  |  |
| --- | --- |
| [`Bounds`](generated/scipy.optimize.Bounds.html#scipy.optimize.Bounds "scipy.optimize.Bounds")([lb,Â ub,Â keep\_feasible]) | Bounds constraint on the variables. |
Quasi-Newton strategies implementing [`HessianUpdateStrategy`](generated/scipy.optimize.HessianUpdateStrategy.html#scipy.optimize.HessianUpdateStrategy "scipy.optimize.HessianUpdateStrategy")
interface can be used to approximate the Hessian in [`minimize`](generated/scipy.optimize.minimize.html#scipy.optimize.minimize "scipy.optimize.minimize")
function (available only for the âtrust-constrâ method). Available
quasi-Newton methods implementing this interface are:
|  |  |
| --- | --- |
| [`BFGS`](generated/scipy.optimize.BFGS.html#scipy.optimize.BFGS "scipy.optimize.BFGS")([exception\_strategy,Â min\_curvature,Â ...]) | Broyden-Fletcher-Goldfarb-Shanno (BFGS) Hessian update strategy. |
| [`SR1`](generated/scipy.optimize.SR1.html#scipy.optimize.SR1 "scipy.optimize.SR1")([min\_denominator,Â init\_scale]) | Symmetric-rank-1 Hessian update strategy. |
### Global optimization[#](#global-optimization "Link to this heading")
|  |  |
| --- | --- |
| [`basinhopping`](generated/scipy.optimize.basinhopping.html#scipy.optimize.basinhopping "scipy.optimize.basinhopping")(func,Â x0[,Â niter,Â T,Â stepsize,Â ...]) | Find the global minimum of a function using the basin-hopping algorithm. |
| [`brute`](generated/scipy.optimize.brute.html#scipy.optimize.brute "scipy.optimize.brute")(func,Â ranges[,Â args,Â Ns,Â full\_output,Â ...]) | Minimize a function over a given range by brute force. |
| [`differential_evolution`](generated/scipy.optimize.differential_evolution.html#scipy.optimize.differential_evolution "scipy.optimize.differential_evolution")(func,Â bounds[,Â args,Â ...]) | Finds the global minimum of a multivariate function. |
| [`shgo`](generated/scipy.optimize.shgo.html#scipy.optimize.shgo "scipy.optimize.shgo")(func,Â bounds[,Â args,Â constraints,Â n,Â ...]) | Finds the global minimum of a function using SHG optimization. |
| [`dual_annealing`](generated/scipy.optimize.dual_annealing.html#scipy.optimize.dual_annealing "scipy.optimize.dual_annealing")(func,Â bounds[,Â args,Â ...]) | Find the global minimum of a function using Dual Annealing. |
| [`direct`](generated/scipy.optimize.direct.html#scipy.optimize.direct "scipy.optimize.direct")(func,Â bounds,Â \*[,Â args,Â eps,Â maxfun,Â ...]) | Finds the global minimum of a function using the DIRECT algorithm. |
## Least-squares and curve fitting[#](#least-squares-and-curve-fitting "Link to this heading")
### Nonlinear least-squares[#](#nonlinear-least-squares "Link to this heading")
|  |  |
| --- | --- |
| [`least_squares`](generated/scipy.optimize.least_squares.html#scipy.optimize.least_squares "scipy.optimize.least_squares")(fun,Â x0[,Â jac,Â bounds,Â ...]) | Solve a nonlinear least-squares problem with bounds on the variables. |
### Linear least-squares[#](#linear-least-squares "Link to this heading")
|  |  |
| --- | --- |
| [`nnls`](generated/scipy.optimize.nnls.html#scipy.optimize.nnls "scipy.optimize.nnls")(A,Â b,Â \*[,Â maxiter]) | Solve `argmin_x || Ax - b ||_2^2` for `x>=0`. |
| [`lsq_linear`](generated/scipy.optimize.lsq_linear.html#scipy.optimize.lsq_linear "scipy.optimize.lsq_linear")(A,Â b[,Â bounds,Â method,Â tol,Â ...]) | Solve a linear least-squares problem with bounds on the variables. |
| [`isotonic_regression`](generated/scipy.optimize.isotonic_regression.html#scipy.optimize.isotonic_regression "scipy.optimize.isotonic_regression")(y,Â \*[,Â weights,Â increasing]) | Nonparametric isotonic regression. |
### Curve fitting[#](#curve-fitting "Link to this heading")
|  |  |
| --- | --- |
| [`curve_fit`](generated/scipy.optimize.curve_fit.html#scipy.optimize.curve_fit "scipy.optimize.curve_fit")(f,Â xdata,Â ydata[,Â p0,Â sigma,Â ...]) | Use non-linear least squares to fit a function, f, to data. |
## Root finding[#](#root-finding "Link to this heading")
### Scalar functions[#](#scalar-functions "Link to this heading")
|  |  |
| --- | --- |
| [`root_scalar`](generated/scipy.optimize.root_scalar.html#scipy.optimize.root_scalar "scipy.optimize.root_scalar")(f[,Â args,Â method,Â bracket,Â ...]) | Find a root of a scalar function. |
| [`brentq`](generated/scipy.optimize.brentq.html#scipy.optimize.brentq "scipy.optimize.brentq")(f,Â a,Â b[,Â args,Â xtol,Â rtol,Â maxiter,Â ...]) | Find a root of a function in a bracketing interval using Brent's method. |
| [`brenth`](generated/scipy.optimize.brenth.html#scipy.optimize.brenth "scipy.optimize.brenth")(f,Â a,Â b[,Â args,Â xtol,Â rtol,Â maxiter,Â ...]) | Find a root of a function in a bracketing interval using Brent's method with hyperbolic extrapolation. |
| [`ridder`](generated/scipy.optimize.ridder.html#scipy.optimize.ridder "scipy.optimize.ridder")(f,Â a,Â b[,Â args,Â xtol,Â rtol,Â maxiter,Â ...]) | Find a root of a function in an interval using Ridder's method. |
| [`bisect`](generated/scipy.optimize.bisect.html#scipy.optimize.bisect "scipy.optimize.bisect")(f,Â a,Â b[,Â args,Â xtol,Â rtol,Â maxiter,Â ...]) | Find root of a function within an interval using bisection. |
| [`newton`](generated/scipy.optimize.newton.html#scipy.optimize.newton "scipy.optimize.newton")(func,Â x0[,Â fprime,Â args,Â tol,Â ...]) | Find a root of a real or complex function using the Newton-Raphson (or secant or Halley's) method. |
| [`toms748`](generated/scipy.optimize.toms748.html#scipy.optimize.toms748 "scipy.optimize.toms748")(f,Â a,Â b[,Â args,Â k,Â xtol,Â rtol,Â ...]) | Find a root using TOMS Algorithm 748 method. |
| [`RootResults`](generated/scipy.optimize.RootResults.html#scipy.optimize.RootResults "scipy.optimize.RootResults")(root,Â iterations,Â ...) | Represents the root finding result. |
The [`root_scalar`](generated/scipy.optimize.root_scalar.html#scipy.optimize.root_scalar "scipy.optimize.root_scalar") function supports the following methods:
* [root\_scalar(method=âbrentqâ)](optimize.root_scalar-brentq.html)
* [root\_scalar(method=âbrenthâ)](optimize.root_scalar-brenth.html)
* [root\_scalar(method=âbisectâ)](optimize.root_scalar-bisect.html)
* [root\_scalar(method=âridderâ)](optimize.root_scalar-ridder.html)
* [root\_scalar(method=ânewtonâ)](optimize.root_scalar-newton.html)
* [root\_scalar(method=âtoms748â)](optimize.root_scalar-toms748.html)
* [root\_scalar(method=âsecantâ)](optimize.root_scalar-secant.html)
* [root\_scalar(method=âhalleyâ)](optimize.root_scalar-halley.html)
The table below lists situations and appropriate methods, along with
*asymptotic* convergence rates per iteration (and per function evaluation)
for successful convergence to a simple root(\*).
Bisection is the slowest of them all, adding one bit of accuracy for each
function evaluation, but is guaranteed to converge.
The other bracketing methods all (eventually) increase the number of accurate
bits by about 50% for every function evaluation.
The derivative-based methods, all built on [`newton`](generated/scipy.optimize.newton.html#scipy.optimize.newton "scipy.optimize.newton"), can converge quite quickly
if the initial value is close to the root. They can also be applied to
functions defined on (a subset of) the complex plane.
| Domain of f | Bracket? | Derivatives? | | Solvers | Convergence | |
| --- | --- | --- | --- | --- | --- | --- |
| *fprime* | *fprime2* | Guaranteed? | Rate(s)(\*) |
| *R* | Yes | N/A | N/A | * bisection * brentq * brenth * ridder * toms748 | * Yes * Yes * Yes * Yes * Yes | * 1 âLinearâ * >=1, <= 1.62 * >=1, <= 1.62 * 2.0 (1.41) * 2.7 (1.65) |
| *R* or *C* | No | No | No | secant | No | 1.62 (1.62) |
| *R* or *C* | No | Yes | No | newton | No | 2.00 (1.41) |
| *R* or *C* | No | Yes | Yes | halley | No | 3.00 (1.44) |
See also
[`scipy.optimize.cython_optimize`](optimize.cython_optimize.html#module-scipy.optimize.cython_optimize "scipy.optimize.cython_optimize") â Typed Cython versions of root finding functions
Fixed point finding:
|  |  |
| --- | --- |
| [`fixed_point`](generated/scipy.optimize.fixed_point.html#scipy.optimize.fixed_point "scipy.optimize.fixed_point")(func,Â x0[,Â args,Â xtol,Â maxiter,Â ...]) | Find a fixed point of the function. |
### Multidimensional[#](#multidimensional "Link to this heading")
|  |  |
| --- | --- |
| [`root`](generated/scipy.optimize.root.html#scipy.optimize.root "scipy.optimize.root")(fun,Â x0[,Â args,Â method,Â jac,Â tol,Â ...]) | Find a root of a vector function. |
The [`root`](generated/scipy.optimize.root.html#scipy.optimize.root "scipy.optimize.root") function supports the following methods:
* [root(method=âhybrâ)](optimize.root-hybr.html)
* [root(method=âlmâ)](optimize.root-lm.html)
* [root(method=âbroyden1â)](optimize.root-broyden1.html)
* [root(method=âbroyden2â)](optimize.root-broyden2.html)
* [root(method=âandersonâ)](optimize.root-anderson.html)
* [root(method=âlinearmixingâ)](optimize.root-linearmixing.html)
* [root(method=âdiagbroydenâ)](optimize.root-diagbroyden.html)
* [root(method=âexcitingmixingâ)](optimize.root-excitingmixing.html)
* [root(method=âkrylovâ)](optimize.root-krylov.html)
* [root(method=âdf-saneâ)](optimize.root-dfsane.html)
## Elementwise Minimization and Root Finding[#](#elementwise-minimization-and-root-finding "Link to this heading")
* [Elementwise Scalar Optimization (`scipy.optimize.elementwise`)](optimize.elementwise.html)
  + [Root finding](optimize.elementwise.html#root-finding)
    - [find\_root](generated/scipy.optimize.elementwise.find_root.html)
    - [bracket\_root](generated/scipy.optimize.elementwise.bracket_root.html)
  + [Minimization](optimize.elementwise.html#minimization)
    - [find\_minimum](generated/scipy.optimize.elementwise.find_minimum.html)
    - [bracket\_minimum](generated/scipy.optimize.elementwise.bracket_minimum.html)
## Linear programming / MILP[#](#linear-programming-milp "Link to this heading")
|  |  |
| --- | --- |
| [`milp`](generated/scipy.optimize.milp.html#scipy.optimize.milp "scipy.optimize.milp")(c,Â \*[,Â integrality,Â bounds,Â ...]) | Mixed-integer linear programming. |
| [`linprog`](generated/scipy.optimize.linprog.html#scipy.optimize.linprog "scipy.optimize.linprog")(c[,Â A\_ub,Â b\_ub,Â A\_eq,Â b\_eq,Â bounds,Â ...]) | Linear programming: minimize a linear objective function subject to linear equality and inequality constraints. |
The [`linprog`](generated/scipy.optimize.linprog.html#scipy.optimize.linprog "scipy.optimize.linprog") function supports the following methods:
* [linprog(method=âsimplexâ)](optimize.linprog-simplex.html)
* [linprog(method=âinterior-pointâ)](optimize.linprog-interior-point.html)
* [linprog(method=ârevised simplexâ)](optimize.linprog-revised_simplex.html)
* [linprog(method=âhighs-ipmâ)](optimize.linprog-highs-ipm.html)
* [linprog(method=âhighs-dsâ)](optimize.linprog-highs-ds.html)
* [linprog(method=âhighsâ)](optimize.linprog-highs.html)
The simplex, interior-point, and revised simplex methods support callback
functions, such as:
|  |  |
| --- | --- |
| [`linprog_verbose_callback`](generated/scipy.optimize.linprog_verbose_callback.html#scipy.optimize.linprog_verbose_callback "scipy.optimize.linprog_verbose_callback")(res) | A sample callback function demonstrating the linprog callback interface. |
## Assignment problems[#](#assignment-problems "Link to this heading")
|  |  |
| --- | --- |
| [`linear_sum_assignment`](generated/scipy.optimize.linear_sum_assignment.html#scipy.optimize.linear_sum_assignment "scipy.optimize.linear_sum_assignment")(cost\_matrix[,Â maximize]) | Solve the linear sum assignment problem. |
| [`quadratic_assignment`](generated/scipy.optimize.quadratic_assignment.html#scipy.optimize.quadratic_assignment "scipy.optimize.quadratic_assignment")(A,Â B[,Â method,Â options]) | Approximates solution to the quadratic assignment problem and the graph matching problem. |
The [`quadratic_assignment`](generated/scipy.optimize.quadratic_assignment.html#scipy.optimize.quadratic_assignment "scipy.optimize.quadratic_assignment") function supports the following methods:
* [quadratic\_assignment(method=âfaqâ)](optimize.qap-faq.html)
* [quadratic\_assignment(method=â2optâ)](optimize.qap-2opt.html)
## Utilities[#](#utilities "Link to this heading")
### Finite-difference approximation[#](#finite-difference-approximation "Link to this heading")
|  |  |
| --- | --- |
| [`approx_fprime`](generated/scipy.optimize.approx_fprime.html#scipy.optimize.approx_fprime "scipy.optimize.approx_fprime")(xk,Â f[,Â epsilon]) | Finite difference approximation of the derivatives of a scalar or vector-valued function. |
| [`check_grad`](generated/scipy.optimize.check_grad.html#scipy.optimize.check_grad "scipy.optimize.check_grad")(func,Â grad,Â x0,Â \*args[,Â epsilon,Â ...]) | Check the correctness of a gradient function by comparing it against a (forward) finite-difference approximation of the gradient. |
### Line search[#](#line-search "Link to this heading")
|  |  |
| --- | --- |
| [`bracket`](generated/scipy.optimize.bracket.html#scipy.optimize.bracket "scipy.optimize.bracket")(func[,Â xa,Â xb,Â args,Â grow\_limit,Â ...]) | Bracket the minimum of a function. |
| [`line_search`](generated/scipy.optimize.line_search.html#scipy.optimize.line_search "scipy.optimize.line_search")(f,Â myfprime,Â xk,Â pk[,Â gfk,Â ...]) | Find alpha that satisfies strong Wolfe conditions. |
### Hessian approximation[#](#hessian-approximation "Link to this heading")
|  |  |
| --- | --- |
| [`LbfgsInvHessProduct`](generated/scipy.optimize.LbfgsInvHessProduct.html#scipy.optimize.LbfgsInvHessProduct "scipy.optimize.LbfgsInvHessProduct")(\*args,Â \*\*kwargs) | Linear operator for the L-BFGS approximate inverse Hessian. |
| [`HessianUpdateStrategy`](generated/scipy.optimize.HessianUpdateStrategy.html#scipy.optimize.HessianUpdateStrategy "scipy.optimize.HessianUpdateStrategy")() | Interface for implementing Hessian update strategies. |
### Benchmark problems[#](#benchmark-problems "Link to this heading")
|  |  |
| --- | --- |
| [`rosen`](generated/scipy.optimize.rosen.html#scipy.optimize.rosen "scipy.optimize.rosen")(x) | The Rosenbrock function. |
| [`rosen_der`](generated/scipy.optimize.rosen_der.html#scipy.optimize.rosen_der "scipy.optimize.rosen_der")(x) | The derivative (i.e. gradient) of the Rosenbrock function. |
| [`rosen_hess`](generated/scipy.optimize.rosen_hess.html#scipy.optimize.rosen_hess "scipy.optimize.rosen_hess")(x) | The Hessian matrix of the Rosenbrock function. |
| [`rosen_hess_prod`](generated/scipy.optimize.rosen_hess_prod.html#scipy.optimize.rosen_hess_prod "scipy.optimize.rosen_hess_prod")(x,Â p) | Product of the Hessian matrix of the Rosenbrock function with a vector. |
## Legacy functions[#](#legacy-functions "Link to this heading")
The functions below are not recommended for use in new scripts;
all of these methods are accessible via a newer, more consistent
interfaces, provided by the interfaces above.
### Optimization[#](#id2 "Link to this heading")
General-purpose multivariate methods:
|  |  |
| --- | --- |
| [`fmin`](generated/scipy.optimize.fmin.html#scipy.optimize.fmin "scipy.optimize.fmin")(func,Â x0[,Â args,Â xtol,Â ftol,Â maxiter,Â ...]) | Minimize a function using the downhill simplex algorithm. |
| [`fmin_powell`](generated/scipy.optimize.fmin_powell.html#scipy.optimize.fmin_powell "scipy.optimize.fmin_powell")(func,Â x0[,Â args,Â xtol,Â ftol,Â ...]) | Minimize a function using modified Powell's method. |
| [`fmin_cg`](generated/scipy.optimize.fmin_cg.html#scipy.optimize.fmin_cg "scipy.optimize.fmin_cg")(f,Â x0[,Â fprime,Â args,Â gtol,Â norm,Â ...]) | Minimize a function using a nonlinear conjugate gradient algorithm. |
| [`fmin_bfgs`](generated/scipy.optimize.fmin_bfgs.html#scipy.optimize.fmin_bfgs "scipy.optimize.fmin_bfgs")(f,Â x0[,Â fprime,Â args,Â gtol,Â norm,Â ...]) | Minimize a function using the BFGS algorithm. |
| [`fmin_ncg`](generated/scipy.optimize.fmin_ncg.html#scipy.optimize.fmin_ncg "scipy.optimize.fmin_ncg")(f,Â x0,Â fprime[,Â fhess\_p,Â fhess,Â ...]) | Unconstrained minimization of a function using the Newton-CG method. |
Constrained multivariate methods:
|  |  |
| --- | --- |
| [`fmin_l_bfgs_b`](generated/scipy.optimize.fmin_l_bfgs_b.html#scipy.optimize.fmin_l_bfgs_b "scipy.optimize.fmin_l_bfgs_b")(func,Â x0[,Â fprime,Â args,Â ...]) | Minimize a function func using the L-BFGS-B algorithm. |
| [`fmin_tnc`](generated/scipy.optimize.fmin_tnc.html#scipy.optimize.fmin_tnc "scipy.optimize.fmin_tnc")(func,Â x0[,Â fprime,Â args,Â ...]) | Minimize a function with variables subject to bounds, using gradient information in a truncated Newton algorithm. |
| [`fmin_cobyla`](generated/scipy.optimize.fmin_cobyla.html#scipy.optimize.fmin_cobyla "scipy.optimize.fmin_cobyla")(func,Â x0,Â cons[,Â args,Â ...]) | Minimize a function using the Constrained Optimization By Linear Approximation (COBYLA) method. |
| [`fmin_slsqp`](generated/scipy.optimize.fmin_slsqp.html#scipy.optimize.fmin_slsqp "scipy.optimize.fmin_slsqp")(func,Â x0[,Â eqcons,Â f\_eqcons,Â ...]) | Minimize a function using Sequential Least Squares Programming. |
Univariate (scalar) minimization methods:
|  |  |
| --- | --- |
| [`fminbound`](generated/scipy.optimize.fminbound.html#scipy.optimize.fminbound "scipy.optimize.fminbound")(func,Â x1,Â x2[,Â args,Â xtol,Â ...]) | Bounded minimization for scalar functions. |
| [`brent`](generated/scipy.optimize.brent.html#scipy.optimize.brent "scipy.optimize.brent")(func[,Â args,Â brack,Â tol,Â full\_output,Â ...]) | Given a function of one variable and a possible bracket, return a local minimizer of the function isolated to a fractional precision of tol. |
| [`golden`](generated/scipy.optimize.golden.html#scipy.optimize.golden "scipy.optimize.golden")(func[,Â args,Â brack,Â tol,Â ...]) | Return the minimizer of a function of one variable using the golden section method. |
### Least-squares[#](#least-squares "Link to this heading")
|  |  |
| --- | --- |
| [`leastsq`](generated/scipy.optimize.leastsq.html#scipy.optimize.leastsq "scipy.optimize.leastsq")(func,Â x0[,Â args,Â Dfun,Â full\_output,Â ...]) | Minimize the sum of squares of a set of equations. |
### Root finding[#](#id3 "Link to this heading")
General nonlinear solvers:
|  |  |
| --- | --- |
| [`fsolve`](generated/scipy.optimize.fsolve.html#scipy.optimize.fsolve "scipy.optimize.fsolve")(func,Â x0[,Â args,Â fprime,Â ...]) | Find the roots of a function. |
| [`broyden1`](generated/scipy.optimize.broyden1.html#scipy.optimize.broyden1 "scipy.optimize.broyden1")(F,Â xin[,Â iter,Â alpha,Â ...]) | Find a root of a function, using Broyden's first Jacobian approximation. |
| [`broyden2`](generated/scipy.optimize.broyden2.html#scipy.optimize.broyden2 "scipy.optimize.broyden2")(F,Â xin[,Â iter,Â alpha,Â ...]) | Find a root of a function, using Broyden's second Jacobian approximation. |
| [`NoConvergence`](generated/scipy.optimize.NoConvergence.html#scipy.optimize.NoConvergence "scipy.optimize.NoConvergence") | Exception raised when nonlinear solver fails to converge within the specified *maxiter*. |
Large-scale nonlinear solvers:
|  |  |
| --- | --- |
| [`newton_krylov`](generated/scipy.optimize.newton_krylov.html#scipy.optimize.newton_krylov "scipy.optimize.newton_krylov")(F,Â xin[,Â iter,Â rdiff,Â method,Â ...]) | Find a root of a function, using Krylov approximation for inverse Jacobian. |
| [`anderson`](generated/scipy.optimize.anderson.html#scipy.optimize.anderson "scipy.optimize.anderson")(F,Â xin[,Â iter,Â alpha,Â w0,Â M,Â ...]) | Find a root of a function, using (extended) Anderson mixing. |
| [`BroydenFirst`](generated/scipy.optimize.BroydenFirst.html#scipy.optimize.BroydenFirst "scipy.optimize.BroydenFirst")([alpha,Â reduction\_method,Â max\_rank]) | Find a root of a function, using Broyden's first Jacobian approximation. |
| [`InverseJacobian`](generated/scipy.optimize.InverseJacobian.html#scipy.optimize.InverseJacobian "scipy.optimize.InverseJacobian")(jacobian) | A simple wrapper that inverts the Jacobian using the *solve* method. |
| [`KrylovJacobian`](generated/scipy.optimize.KrylovJacobian.html#scipy.optimize.KrylovJacobian "scipy.optimize.KrylovJacobian")([rdiff,Â method,Â ...]) | Find a root of a function, using Krylov approximation for inverse Jacobian. |
Simple iteration solvers:
|  |  |
| --- | --- |
| [`excitingmixing`](generated/scipy.optimize.excitingmixing.html#scipy.optimize.excitingmixing "scipy.optimize.excitingmixing")(F,Â xin[,Â iter,Â alpha,Â ...]) | Find a root of a function, using a tuned diagonal Jacobian approximation. |
| [`linearmixing`](generated/scipy.optimize.linearmixing.html#scipy.optimize.linearmixing "scipy.optimize.linearmixing")(F,Â xin[,Â iter,Â alpha,Â verbose,Â ...]) | Find a root of a function, using a scalar Jacobian approximation. |
| [`diagbroyden`](generated/scipy.optimize.diagbroyden.html#scipy.optimize.diagbroyden "scipy.optimize.diagbroyden")(F,Â xin[,Â iter,Â alpha,Â verbose,Â ...]) | Find a root of a function, using diagonal Broyden Jacobian approximation. |
[previous
scipy.odr.quadratic](generated/scipy.odr.quadratic.html "previous page")
[next
Cython optimize root finding API](optimize.cython_optimize.html "next page")
On this page
* [Optimization](#optimization)
  + [Scalar functions optimization](#scalar-functions-optimization)
  + [Local (multivariate) optimization](#local-multivariate-optimization)
  + [Global optimization](#global-optimization)
* [Least-squares and curve fitting](#least-squares-and-curve-fitting)
  + [Nonlinear least-squares](#nonlinear-least-squares)
  + [Linear least-squares](#linear-least-squares)
  + [Curve fitting](#curve-fitting)
* [Root finding](#root-finding)
  + [Scalar functions](#scalar-functions)
  + [Multidimensional](#multidimensional)
* [Elementwise Minimization and Root Finding](#elementwise-minimization-and-root-finding)
* [Linear programming / MILP](#linear-programming-milp)
* [Assignment problems](#assignment-problems)
* [Utilities](#utilities)
  + [Finite-difference approximation](#finite-difference-approximation)
  + [Line search](#line-search)
  + [Hessian approximation](#hessian-approximation)
  + [Benchmark problems](#benchmark-problems)
* [Legacy functions](#legacy-functions)
  + [Optimization](#id2)
  + [Least-squares](#least-squares)
  + [Root finding](#id3)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/optimize.cython_optimize.html#module-scipy.optimize.cython_optimize -->
* [SciPy API](index.html)
* [Optimization and root finding (`scipy.optimize`)](optimize.html)
* Cython optimize root finding API
# Cython optimize root finding API[#](#cython-optimize-root-finding-api "Link to this heading")
The underlying C functions for the following root finders can be accessed
directly using Cython:
* [`bisect`](generated/scipy.optimize.bisect.html#scipy.optimize.bisect "scipy.optimize.bisect")
* [`ridder`](generated/scipy.optimize.ridder.html#scipy.optimize.ridder "scipy.optimize.ridder")
* [`brenth`](generated/scipy.optimize.brenth.html#scipy.optimize.brenth "scipy.optimize.brenth")
* [`brentq`](generated/scipy.optimize.brentq.html#scipy.optimize.brentq "scipy.optimize.brentq")
The Cython API for the root finding functions is similar except there is no
`disp` argument. Import the root finding functions using `cimport` from
[`scipy.optimize.cython_optimize`](#module-scipy.optimize.cython_optimize "scipy.optimize.cython_optimize").
```
from scipy.optimize.cython_optimize cimport bisect, ridder, brentq, brenth
```
## Callback signature[#](#callback-signature "Link to this heading")
The zeros functions in [`cython_optimize`](#module-scipy.optimize.cython_optimize "scipy.optimize.cython_optimize") expect a callback that
takes a double for the scalar independent variable as the 1st argument and a
user defined `struct` with any extra parameters as the 2nd argument.
```
double (*callback_type)(double, void*) noexcept
```
## Examples[#](#examples "Link to this heading")
Usage of [`cython_optimize`](#module-scipy.optimize.cython_optimize "scipy.optimize.cython_optimize") requires Cython to write callbacks
that are compiled into C. For more information on compiling Cython, see the
[Cython Documentation](http://docs.cython.org/en/latest/index.html).
These are the basic steps:
1. Create a Cython `.pyx` file, for example: `myexample.pyx`.
2. Import the desired root finder from [`cython_optimize`](#module-scipy.optimize.cython_optimize "scipy.optimize.cython_optimize").
3. Write the callback function, and call the selected root finding function
   passing the callback, any extra arguments, and the other solver
   parameters.
   ```
   from scipy.optimize.cython_optimize cimport brentq
   # import math from Cython
   from libc cimport math
   myargs = {'C0': 1.0, 'C1': 0.7}  # a dictionary of extra arguments
   XLO, XHI = 0.5, 1.0  # lower and upper search boundaries
   XTOL, RTOL, MITR = 1e-3, 1e-3, 10  # other solver parameters
   # user-defined struct for extra parameters
   ctypedef struct test_params:
       double C0
       double C1
   # user-defined callback
   cdef double f(double x, void *args) noexcept:
       cdef test_params *myargs = <test_params *> args
       return myargs.C0 - math.exp(-(x - myargs.C1))
   # Cython wrapper function
   cdef double brentq_wrapper_example(dict args, double xa, double xb,
                                      double xtol, double rtol, int mitr):
       # Cython automatically casts dictionary to struct
       cdef test_params myargs = args
       return brentq(
           f, xa, xb, <test_params *> &myargs, xtol, rtol, mitr, NULL)
   # Python function
   def brentq_example(args=myargs, xa=XLO, xb=XHI, xtol=XTOL, rtol=RTOL,
                      mitr=MITR):
       '''Calls Cython wrapper from Python.'''
       return brentq_wrapper_example(args, xa, xb, xtol, rtol, mitr)
   ```
4. If you want to call your function from Python, create a Cython wrapper, and
   a Python function that calls the wrapper, or use `cpdef`. Then, in Python,
   you can import and run the example.
   ```
   from myexample import brentq_example
   x = brentq_example()
   # 0.6999942848231314
   ```
5. Create a Cython `.pxd` file if you need to export any Cython functions.
## Full output[#](#full-output "Link to this heading")
The functions in [`cython_optimize`](#module-scipy.optimize.cython_optimize "scipy.optimize.cython_optimize") can also copy the full
output from the solver to a C `struct` that is passed as its last argument.
If you donât want the full output, just pass `NULL`. The full output
`struct` must be type `zeros_full_output`, which is defined in
[`scipy.optimize.cython_optimize`](#module-scipy.optimize.cython_optimize "scipy.optimize.cython_optimize") with the following fields:
* `int funcalls`: number of function calls
* `int iterations`: number of iterations
* `int error_num`: error number
* `double root`: root of function
The root is copied by [`cython_optimize`](#module-scipy.optimize.cython_optimize "scipy.optimize.cython_optimize") to the full output
`struct`. An error number of -1 means a sign error, -2 means a convergence
error, and 0 means the solver converged. Continuing from the previous example:
```
from scipy.optimize.cython_optimize cimport zeros_full_output
# cython brentq solver with full output
cdef zeros_full_output brentq_full_output_wrapper_example(
        dict args, double xa, double xb, double xtol, double rtol,
        int mitr):
    cdef test_params myargs = args
    cdef zeros_full_output my_full_output
    # use my_full_output instead of NULL
    brentq(f, xa, xb, &myargs, xtol, rtol, mitr, &my_full_output)
    return my_full_output
# Python function
def brent_full_output_example(args=myargs, xa=XLO, xb=XHI, xtol=XTOL,
                              rtol=RTOL, mitr=MITR):
    '''Returns full output'''
    return brentq_full_output_wrapper_example(args, xa, xb, xtol, rtol,
                                              mitr)
result = brent_full_output_example()
# {'error_num': 0,
#  'funcalls': 6,
#  'iterations': 5,
#  'root': 0.6999942848231314}
```
[previous
Optimization and root finding (`scipy.optimize`)](optimize.html "previous page")
[next
show\_options](generated/scipy.optimize.show_options.html "next page")
On this page
* [Callback signature](#callback-signature)
* [Examples](#examples)
* [Full output](#full-output)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/optimize.elementwise.html#module-scipy.optimize.elementwise -->
* [SciPy API](index.html)
* [Optimization and root finding (`scipy.optimize`)](optimize.html)
* Elementwise Scalar Optimization (`scipy.optimize.elementwise`)
# Elementwise Scalar Optimization ([`scipy.optimize.elementwise`](#module-scipy.optimize.elementwise "scipy.optimize.elementwise"))[#](#elementwise-scalar-optimization-scipy-optimize-elementwise "Link to this heading")
This module provides a collection of functions for root finding and
minimization of scalar, real-valued functions of one variable. Unlike their
counterparts in the base [`scipy.optimize`](optimize.html#module-scipy.optimize "scipy.optimize") namespace, these functions work
elementwise, enabling the solution of many related problems in an efficient,
vectorized call. Furthermore, when environment variable `SCIPY_ARRAY_API=1`,
these functions can accept non-NumPy, array API standard compatible arrays and
perform all calculations using the corresponding array library (e.g. PyTorch,
JAX, CuPy).
## Root finding[#](#root-finding "Link to this heading")
|  |  |
| --- | --- |
| [`find_root`](generated/scipy.optimize.elementwise.find_root.html#scipy.optimize.elementwise.find_root "scipy.optimize.elementwise.find_root")(f,Â init,Â /,Â \*[,Â args,Â kwargs,Â ...]) | Find the root of a monotonic, real-valued function of a real variable. |
| [`bracket_root`](generated/scipy.optimize.elementwise.bracket_root.html#scipy.optimize.elementwise.bracket_root "scipy.optimize.elementwise.bracket_root")(f,Â xl0[,Â xr0,Â xmin,Â xmax,Â ...]) | Bracket the root of a monotonic, real-valued function of a real variable. |
## Minimization[#](#minimization "Link to this heading")
|  |  |
| --- | --- |
| [`find_minimum`](generated/scipy.optimize.elementwise.find_minimum.html#scipy.optimize.elementwise.find_minimum "scipy.optimize.elementwise.find_minimum")(f,Â init,Â /,Â \*[,Â args,Â kwargs,Â ...]) | Find the minimum of a unimodal, real-valued function of a real variable. |
| [`bracket_minimum`](generated/scipy.optimize.elementwise.bracket_minimum.html#scipy.optimize.elementwise.bracket_minimum "scipy.optimize.elementwise.bracket_minimum")(f,Â xm0,Â \*[,Â xl0,Â xr0,Â xmin,Â ...]) | Bracket the minimum of a unimodal, real-valued function of a real variable. |
[previous
root(method=âdf-saneâ)](optimize.root-dfsane.html "previous page")
[next
find\_root](generated/scipy.optimize.elementwise.find_root.html "next page")
On this page
* [Root finding](#root-finding)
* [Minimization](#minimization)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/signal.html#module-scipy.signal -->
* [SciPy API](index.html)
* Signal processing (`scipy.signal`)
# Signal processing ([`scipy.signal`](#module-scipy.signal "scipy.signal"))[#](#signal-processing-scipy-signal "Link to this heading")
## Convolution[#](#convolution "Link to this heading")
|  |  |
| --- | --- |
| [`convolve`](generated/scipy.signal.convolve.html#scipy.signal.convolve "scipy.signal.convolve")(in1,Â in2[,Â mode,Â method]) | Convolve two N-dimensional arrays. |
| [`correlate`](generated/scipy.signal.correlate.html#scipy.signal.correlate "scipy.signal.correlate")(in1,Â in2[,Â mode,Â method]) | Cross-correlate two N-dimensional arrays. |
| [`fftconvolve`](generated/scipy.signal.fftconvolve.html#scipy.signal.fftconvolve "scipy.signal.fftconvolve")(in1,Â in2[,Â mode,Â axes]) | Convolve two N-dimensional arrays using FFT. |
| [`oaconvolve`](generated/scipy.signal.oaconvolve.html#scipy.signal.oaconvolve "scipy.signal.oaconvolve")(in1,Â in2[,Â mode,Â axes]) | Convolve two N-dimensional arrays using the overlap-add method. |
| [`convolve2d`](generated/scipy.signal.convolve2d.html#scipy.signal.convolve2d "scipy.signal.convolve2d")(in1,Â in2[,Â mode,Â boundary,Â fillvalue]) | Convolve two 2-dimensional arrays. |
| [`correlate2d`](generated/scipy.signal.correlate2d.html#scipy.signal.correlate2d "scipy.signal.correlate2d")(in1,Â in2[,Â mode,Â boundary,Â ...]) | Cross-correlate two 2-dimensional arrays. |
| [`sepfir2d`](generated/scipy.signal.sepfir2d.html#scipy.signal.sepfir2d "scipy.signal.sepfir2d")(input,Â hrow,Â hcol) | Convolve with a 2-D separable FIR filter. |
| [`choose_conv_method`](generated/scipy.signal.choose_conv_method.html#scipy.signal.choose_conv_method "scipy.signal.choose_conv_method")(in1,Â in2[,Â mode,Â measure]) | Find the fastest convolution/correlation method. |
| [`correlation_lags`](generated/scipy.signal.correlation_lags.html#scipy.signal.correlation_lags "scipy.signal.correlation_lags")(in1\_len,Â in2\_len[,Â mode]) | Calculates the lag / displacement indices array for 1D cross-correlation. |
## B-splines[#](#b-splines "Link to this heading")
|  |  |
| --- | --- |
| [`gauss_spline`](generated/scipy.signal.gauss_spline.html#scipy.signal.gauss_spline "scipy.signal.gauss_spline")(x,Â n) | Gaussian approximation to B-spline basis function of order n. |
| [`cspline1d`](generated/scipy.signal.cspline1d.html#scipy.signal.cspline1d "scipy.signal.cspline1d")(signal[,Â lamb]) | Compute cubic spline coefficients for rank-1 array. |
| [`qspline1d`](generated/scipy.signal.qspline1d.html#scipy.signal.qspline1d "scipy.signal.qspline1d")(signal[,Â lamb]) | Compute quadratic spline coefficients for rank-1 array. |
| [`cspline2d`](generated/scipy.signal.cspline2d.html#scipy.signal.cspline2d "scipy.signal.cspline2d")(signal[,Â lamb,Â precision]) | Coefficients for 2-D cubic (3rd order) B-spline. |
| [`qspline2d`](generated/scipy.signal.qspline2d.html#scipy.signal.qspline2d "scipy.signal.qspline2d")(signal[,Â lamb,Â precision]) | Coefficients for 2-D quadratic (2nd order) B-spline. |
| [`cspline1d_eval`](generated/scipy.signal.cspline1d_eval.html#scipy.signal.cspline1d_eval "scipy.signal.cspline1d_eval")(cj,Â newx[,Â dx,Â x0]) | Evaluate a cubic spline at the new set of points. |
| [`qspline1d_eval`](generated/scipy.signal.qspline1d_eval.html#scipy.signal.qspline1d_eval "scipy.signal.qspline1d_eval")(cj,Â newx[,Â dx,Â x0]) | Evaluate a quadratic spline at the new set of points. |
| [`spline_filter`](generated/scipy.signal.spline_filter.html#scipy.signal.spline_filter "scipy.signal.spline_filter")(Iin[,Â lmbda]) | Smoothing spline (cubic) filtering of a rank-2 array. |
| [`whittaker_henderson`](generated/scipy.signal.whittaker_henderson.html#scipy.signal.whittaker_henderson "scipy.signal.whittaker_henderson")(signal,Â \*[,Â lamb,Â ...]) | Whittaker-Henderson (WH) smoothing/graduation of a discrete signal. |
## Filtering[#](#filtering "Link to this heading")
|  |  |
| --- | --- |
| [`order_filter`](generated/scipy.signal.order_filter.html#scipy.signal.order_filter "scipy.signal.order_filter")(a,Â domain,Â rank) | Perform an order filter on an N-D array. |
| [`medfilt`](generated/scipy.signal.medfilt.html#scipy.signal.medfilt "scipy.signal.medfilt")(volume[,Â kernel\_size]) | Perform a median filter on an N-dimensional array. |
| [`medfilt2d`](generated/scipy.signal.medfilt2d.html#scipy.signal.medfilt2d "scipy.signal.medfilt2d")(input[,Â kernel\_size]) | Median filter a 2-dimensional array. |
| [`wiener`](generated/scipy.signal.wiener.html#scipy.signal.wiener "scipy.signal.wiener")(im[,Â mysize,Â noise]) | Perform a Wiener filter on an N-dimensional array. |
| [`symiirorder1`](generated/scipy.signal.symiirorder1.html#scipy.signal.symiirorder1 "scipy.signal.symiirorder1")(signal,Â c0,Â z1[,Â precision]) | Implement a smoothing IIR filter with mirror-symmetric boundary conditions using a cascade of first-order sections. |
| [`symiirorder2`](generated/scipy.signal.symiirorder2.html#scipy.signal.symiirorder2 "scipy.signal.symiirorder2")(input,Â r,Â omega[,Â precision]) | Implement a smoothing IIR filter with mirror-symmetric boundary conditions using a cascade of second-order sections. |
| [`lfilter`](generated/scipy.signal.lfilter.html#scipy.signal.lfilter "scipy.signal.lfilter")(b,Â a,Â x[,Â axis,Â zi]) | Filter data along one-dimension with an IIR or FIR filter. |
| [`lfiltic`](generated/scipy.signal.lfiltic.html#scipy.signal.lfiltic "scipy.signal.lfiltic")(b,Â a,Â y[,Â x]) | Construct initial conditions for lfilter given input and output vectors. |
| [`lfilter_zi`](generated/scipy.signal.lfilter_zi.html#scipy.signal.lfilter_zi "scipy.signal.lfilter_zi")(b,Â a) | Construct initial conditions for [`lfilter`](generated/scipy.signal.lfilter.html#scipy.signal.lfilter "scipy.signal.lfilter") for step response steady-state. |
| [`filtfilt`](generated/scipy.signal.filtfilt.html#scipy.signal.filtfilt "scipy.signal.filtfilt")(b,Â a,Â x[,Â axis,Â padtype,Â padlen,Â ...]) | Apply a digital filter forward and backward to a signal. |
| [`savgol_filter`](generated/scipy.signal.savgol_filter.html#scipy.signal.savgol_filter "scipy.signal.savgol_filter")(x,Â window\_length,Â polyorder[,Â ...]) | Apply a Savitzky-Golay filter to an array. |
| [`deconvolve`](generated/scipy.signal.deconvolve.html#scipy.signal.deconvolve "scipy.signal.deconvolve")(signal,Â divisor) | Deconvolves `divisor` out of `signal` using inverse filtering. |
| [`sosfilt`](generated/scipy.signal.sosfilt.html#scipy.signal.sosfilt "scipy.signal.sosfilt")(sos,Â x[,Â axis,Â zi]) | Filter data along one dimension using cascaded second-order sections. |
| [`sosfilt_zi`](generated/scipy.signal.sosfilt_zi.html#scipy.signal.sosfilt_zi "scipy.signal.sosfilt_zi")(sos) | Construct initial conditions for sosfilt for step response steady-state. |
| [`sosfiltfilt`](generated/scipy.signal.sosfiltfilt.html#scipy.signal.sosfiltfilt "scipy.signal.sosfiltfilt")(sos,Â x[,Â axis,Â padtype,Â padlen]) | A forward-backward digital filter using cascaded second-order sections. |
| [`hilbert`](generated/scipy.signal.hilbert.html#scipy.signal.hilbert "scipy.signal.hilbert")(x[,Â N,Â axis]) | FFT-based computation of the analytic signal. |
| [`hilbert2`](generated/scipy.signal.hilbert2.html#scipy.signal.hilbert2 "scipy.signal.hilbert2")(x[,Â N,Â axes]) | Compute the '2-D' analytic signal of *x*. |
| [`envelope`](generated/scipy.signal.envelope.html#scipy.signal.envelope "scipy.signal.envelope")(z[,Â bp\_in,Â n\_out,Â squared,Â ...]) | Compute the envelope of a real- or complex-valued signal. |
| [`decimate`](generated/scipy.signal.decimate.html#scipy.signal.decimate "scipy.signal.decimate")(x,Â q[,Â n,Â ftype,Â axis,Â zero\_phase]) | Downsample the signal after applying an anti-aliasing filter. |
| [`detrend`](generated/scipy.signal.detrend.html#scipy.signal.detrend "scipy.signal.detrend")(data[,Â axis,Â type,Â bp,Â overwrite\_data]) | Remove linear or constant trend along axis from data. |
| [`resample`](generated/scipy.signal.resample.html#scipy.signal.resample "scipy.signal.resample")(x,Â num[,Â t,Â axis,Â window,Â domain]) | Resample *x* to *num* samples using the Fourier method along the given *axis*. |
| [`resample_poly`](generated/scipy.signal.resample_poly.html#scipy.signal.resample_poly "scipy.signal.resample_poly")(x,Â up,Â down[,Â axis,Â window,Â ...]) | Resample *x* along the given axis using polyphase filtering. |
| [`upfirdn`](generated/scipy.signal.upfirdn.html#scipy.signal.upfirdn "scipy.signal.upfirdn")(h,Â x[,Â up,Â down,Â axis,Â mode,Â cval]) | Upsample, FIR filter, and downsample. |
## Filter design[#](#filter-design "Link to this heading")
|  |  |
| --- | --- |
| [`bilinear`](generated/scipy.signal.bilinear.html#scipy.signal.bilinear "scipy.signal.bilinear")(b,Â a[,Â fs]) | Calculate a digital IIR filter from an analog transfer function by utilizing the bilinear transform. |
| [`bilinear_zpk`](generated/scipy.signal.bilinear_zpk.html#scipy.signal.bilinear_zpk "scipy.signal.bilinear_zpk")(z,Â p,Â k,Â fs) | Return a digital IIR filter from an analog one using a bilinear transform. |
| [`findfreqs`](generated/scipy.signal.findfreqs.html#scipy.signal.findfreqs "scipy.signal.findfreqs")(num,Â den,Â N[,Â kind]) | Find array of frequencies for computing the response of an analog filter. |
| [`firls`](generated/scipy.signal.firls.html#scipy.signal.firls "scipy.signal.firls")(numtaps,Â bands,Â desired,Â \*[,Â weight,Â fs]) | FIR filter design using least-squares error minimization. |
| [`firwin`](generated/scipy.signal.firwin.html#scipy.signal.firwin "scipy.signal.firwin")(numtaps,Â cutoff,Â \*[,Â width,Â window,Â ...]) | FIR filter design using the window method. |
| [`firwin2`](generated/scipy.signal.firwin2.html#scipy.signal.firwin2 "scipy.signal.firwin2")(numtaps,Â freq,Â gain,Â \*[,Â nfreqs,Â ...]) | FIR filter design using the window method. |
| [`firwin_2d`](generated/scipy.signal.firwin_2d.html#scipy.signal.firwin_2d "scipy.signal.firwin_2d")(hsize,Â window,Â \*[,Â fc,Â fs,Â ...]) | 2D FIR filter design using the window method. |
| [`freqs`](generated/scipy.signal.freqs.html#scipy.signal.freqs "scipy.signal.freqs")(b,Â a[,Â worN,Â plot]) | Compute frequency response of analog filter. |
| [`freqs_zpk`](generated/scipy.signal.freqs_zpk.html#scipy.signal.freqs_zpk "scipy.signal.freqs_zpk")(z,Â p,Â k[,Â worN]) | Compute frequency response of analog filter. |
| [`freqz`](generated/scipy.signal.freqz.html#scipy.signal.freqz "scipy.signal.freqz")(b[,Â a,Â worN,Â whole,Â plot,Â fs,Â ...]) | Compute the frequency response of a digital filter. |
| [`sosfreqz`](generated/scipy.signal.sosfreqz.html#scipy.signal.sosfreqz "scipy.signal.sosfreqz")(\*args,Â \*\*kwargs) | Compute the frequency response of a digital filter in SOS format (legacy). |
| [`freqz_sos`](generated/scipy.signal.freqz_sos.html#scipy.signal.freqz_sos "scipy.signal.freqz_sos")(sos[,Â worN,Â whole,Â fs]) | Compute the frequency response of a digital filter in SOS format. |
| [`freqz_zpk`](generated/scipy.signal.freqz_zpk.html#scipy.signal.freqz_zpk "scipy.signal.freqz_zpk")(z,Â p,Â k[,Â worN,Â whole,Â fs]) | Compute the frequency response of a digital filter in ZPK form. |
| [`gammatone`](generated/scipy.signal.gammatone.html#scipy.signal.gammatone "scipy.signal.gammatone")(freq,Â ftype[,Â order,Â numtaps,Â fs,Â ...]) | Gammatone filter design. |
| [`group_delay`](generated/scipy.signal.group_delay.html#scipy.signal.group_delay "scipy.signal.group_delay")(system[,Â w,Â whole,Â fs]) | Compute the group delay of a digital filter. |
| [`iirdesign`](generated/scipy.signal.iirdesign.html#scipy.signal.iirdesign "scipy.signal.iirdesign")(wp,Â ws,Â gpass,Â gstop[,Â analog,Â ...]) | Complete IIR digital and analog filter design. |
| [`iirfilter`](generated/scipy.signal.iirfilter.html#scipy.signal.iirfilter "scipy.signal.iirfilter")(N,Â Wn[,Â rp,Â rs,Â btype,Â analog,Â ...]) | IIR digital and analog filter design given order and critical points. |
| [`kaiser_atten`](generated/scipy.signal.kaiser_atten.html#scipy.signal.kaiser_atten "scipy.signal.kaiser_atten")(numtaps,Â width) | Compute the attenuation of a Kaiser FIR filter. |
| [`kaiser_beta`](generated/scipy.signal.kaiser_beta.html#scipy.signal.kaiser_beta "scipy.signal.kaiser_beta")(a) | Compute the Kaiser parameter *beta*, given the attenuation *a*. |
| [`kaiserord`](generated/scipy.signal.kaiserord.html#scipy.signal.kaiserord "scipy.signal.kaiserord")(ripple,Â width) | Determine the filter window parameters for the Kaiser window method. |
| [`minimum_phase`](generated/scipy.signal.minimum_phase.html#scipy.signal.minimum_phase "scipy.signal.minimum_phase")(h[,Â method,Â n\_fft,Â half]) | Convert a linear-phase FIR filter to minimum phase. |
| [`savgol_coeffs`](generated/scipy.signal.savgol_coeffs.html#scipy.signal.savgol_coeffs "scipy.signal.savgol_coeffs")(window\_length,Â polyorder[,Â ...]) | Compute the coefficients for a 1-D Savitzky-Golay FIR filter. |
| [`remez`](generated/scipy.signal.remez.html#scipy.signal.remez "scipy.signal.remez")(numtaps,Â bands,Â desired,Â \*[,Â weight,Â ...]) | Calculate the minimax optimal filter using the Remez exchange algorithm. |
| [`unique_roots`](generated/scipy.signal.unique_roots.html#scipy.signal.unique_roots "scipy.signal.unique_roots")(p[,Â tol,Â rtype]) | Determine unique roots and their multiplicities from a list of roots. |
| [`residue`](generated/scipy.signal.residue.html#scipy.signal.residue "scipy.signal.residue")(b,Â a[,Â tol,Â rtype]) | Compute partial-fraction expansion of b(s) / a(s). |
| [`residuez`](generated/scipy.signal.residuez.html#scipy.signal.residuez "scipy.signal.residuez")(b,Â a[,Â tol,Â rtype]) | Compute partial-fraction expansion of b(z) / a(z). |
| [`invres`](generated/scipy.signal.invres.html#scipy.signal.invres "scipy.signal.invres")(r,Â p,Â k[,Â tol,Â rtype]) | Compute b(s) and a(s) from partial fraction expansion. |
| [`invresz`](generated/scipy.signal.invresz.html#scipy.signal.invresz "scipy.signal.invresz")(r,Â p,Â k[,Â tol,Â rtype]) | Compute b(z) and a(z) from partial fraction expansion. |
| [`BadCoefficients`](generated/scipy.signal.BadCoefficients.html#scipy.signal.BadCoefficients "scipy.signal.BadCoefficients") | Warning about badly conditioned filter coefficients. |
Lower-level filter design functions:
|  |  |
| --- | --- |
| [`abcd_normalize`](generated/scipy.signal.abcd_normalize.html#scipy.signal.abcd_normalize "scipy.signal.abcd_normalize")([A,Â B,Â C,Â D]) | Check state-space matrices compatibility and ensure they are 2d arrays. |
| [`band_stop_obj`](generated/scipy.signal.band_stop_obj.html#scipy.signal.band_stop_obj "scipy.signal.band_stop_obj")(wp,Â ind,Â passb,Â stopb,Â gpass,Â ...) | Band Stop Objective Function for order minimization. |
| [`besselap`](generated/scipy.signal.besselap.html#scipy.signal.besselap "scipy.signal.besselap")(N[,Â norm,Â xp,Â device]) | Return (z,p,k) for analog prototype of an Nth-order Bessel filter. |
| [`buttap`](generated/scipy.signal.buttap.html#scipy.signal.buttap "scipy.signal.buttap")(N,Â \*[,Â xp,Â device]) | Return (z,p,k) for analog prototype of Nth-order Butterworth filter. |
| [`cheb1ap`](generated/scipy.signal.cheb1ap.html#scipy.signal.cheb1ap "scipy.signal.cheb1ap")(N,Â rp,Â \*[,Â xp,Â device]) | Return (z,p,k) for Nth-order Chebyshev type I analog lowpass filter. |
| [`cheb2ap`](generated/scipy.signal.cheb2ap.html#scipy.signal.cheb2ap "scipy.signal.cheb2ap")(N,Â rs,Â \*[,Â xp,Â device]) | Return (z,p,k) for Nth-order Chebyshev type II analog lowpass filter. |
| [`ellipap`](generated/scipy.signal.ellipap.html#scipy.signal.ellipap "scipy.signal.ellipap")(N,Â rp,Â rs,Â \*[,Â xp,Â device]) | Return (z,p,k) of Nth-order elliptic analog lowpass filter. |
| [`lp2bp`](generated/scipy.signal.lp2bp.html#scipy.signal.lp2bp "scipy.signal.lp2bp")(b,Â a[,Â wo,Â bw]) | Transform a lowpass filter prototype to a bandpass filter. |
| [`lp2bp_zpk`](generated/scipy.signal.lp2bp_zpk.html#scipy.signal.lp2bp_zpk "scipy.signal.lp2bp_zpk")(z,Â p,Â k[,Â wo,Â bw]) | Transform a lowpass filter prototype to a bandpass filter. |
| [`lp2bs`](generated/scipy.signal.lp2bs.html#scipy.signal.lp2bs "scipy.signal.lp2bs")(b,Â a[,Â wo,Â bw]) | Transform a lowpass filter prototype to a bandstop filter. |
| [`lp2bs_zpk`](generated/scipy.signal.lp2bs_zpk.html#scipy.signal.lp2bs_zpk "scipy.signal.lp2bs_zpk")(z,Â p,Â k[,Â wo,Â bw]) | Transform a lowpass filter prototype to a bandstop filter. |
| [`lp2hp`](generated/scipy.signal.lp2hp.html#scipy.signal.lp2hp "scipy.signal.lp2hp")(b,Â a[,Â wo]) | Transform a lowpass filter prototype to a highpass filter. |
| [`lp2hp_zpk`](generated/scipy.signal.lp2hp_zpk.html#scipy.signal.lp2hp_zpk "scipy.signal.lp2hp_zpk")(z,Â p,Â k[,Â wo]) | Transform a lowpass filter prototype to a highpass filter. |
| [`lp2lp`](generated/scipy.signal.lp2lp.html#scipy.signal.lp2lp "scipy.signal.lp2lp")(b,Â a[,Â wo]) | Transform a lowpass filter prototype to a different frequency. |
| [`lp2lp_zpk`](generated/scipy.signal.lp2lp_zpk.html#scipy.signal.lp2lp_zpk "scipy.signal.lp2lp_zpk")(z,Â p,Â k[,Â wo]) | Transform a lowpass filter prototype to a different frequency. |
| [`normalize`](generated/scipy.signal.normalize.html#scipy.signal.normalize "scipy.signal.normalize")(b,Â a) | Normalize numerator/denominator of a continuous-time transfer function. |
## Matlab-style IIR filter design[#](#matlab-style-iir-filter-design "Link to this heading")
|  |  |
| --- | --- |
| [`butter`](generated/scipy.signal.butter.html#scipy.signal.butter "scipy.signal.butter")(N,Â Wn[,Â btype,Â analog,Â output,Â fs]) | Butterworth digital and analog filter design. |
| [`buttord`](generated/scipy.signal.buttord.html#scipy.signal.buttord "scipy.signal.buttord")(wp,Â ws,Â gpass,Â gstop[,Â analog,Â fs]) | Butterworth filter order selection. |
| [`cheby1`](generated/scipy.signal.cheby1.html#scipy.signal.cheby1 "scipy.signal.cheby1")(N,Â rp,Â Wn[,Â btype,Â analog,Â output,Â fs]) | Chebyshev type I digital and analog filter design. |
| [`cheb1ord`](generated/scipy.signal.cheb1ord.html#scipy.signal.cheb1ord "scipy.signal.cheb1ord")(wp,Â ws,Â gpass,Â gstop[,Â analog,Â fs]) | Chebyshev type I filter order selection. |
| [`cheby2`](generated/scipy.signal.cheby2.html#scipy.signal.cheby2 "scipy.signal.cheby2")(N,Â rs,Â Wn[,Â btype,Â analog,Â output,Â fs]) | Chebyshev type II digital and analog filter design. |
| [`cheb2ord`](generated/scipy.signal.cheb2ord.html#scipy.signal.cheb2ord "scipy.signal.cheb2ord")(wp,Â ws,Â gpass,Â gstop[,Â analog,Â fs]) | Chebyshev type II filter order selection. |
| [`ellip`](generated/scipy.signal.ellip.html#scipy.signal.ellip "scipy.signal.ellip")(N,Â rp,Â rs,Â Wn[,Â btype,Â analog,Â output,Â fs]) | Elliptic (Cauer) digital and analog filter design. |
| [`ellipord`](generated/scipy.signal.ellipord.html#scipy.signal.ellipord "scipy.signal.ellipord")(wp,Â ws,Â gpass,Â gstop[,Â analog,Â fs]) | Elliptic (Cauer) filter order selection. |
| [`bessel`](generated/scipy.signal.bessel.html#scipy.signal.bessel "scipy.signal.bessel")(N,Â Wn[,Â btype,Â analog,Â output,Â norm,Â fs]) | Bessel/Thomson digital and analog filter design. |
| [`iirnotch`](generated/scipy.signal.iirnotch.html#scipy.signal.iirnotch "scipy.signal.iirnotch")(w0,Â Q[,Â fs,Â xp,Â device]) | Design second-order IIR notch digital filter. |
| [`iirpeak`](generated/scipy.signal.iirpeak.html#scipy.signal.iirpeak "scipy.signal.iirpeak")(w0,Â Q[,Â fs,Â xp,Â device]) | Design second-order IIR peak (resonant) digital filter. |
| [`iircomb`](generated/scipy.signal.iircomb.html#scipy.signal.iircomb "scipy.signal.iircomb")(w0,Â Q[,Â ftype,Â fs,Â pass\_zero,Â xp,Â ...]) | Design IIR notching or peaking digital comb filter. |
## Continuous-time linear systems[#](#continuous-time-linear-systems "Link to this heading")
|  |  |
| --- | --- |
| [`lti`](generated/scipy.signal.lti.html#scipy.signal.lti "scipy.signal.lti")(\*system) | Continuous-time linear time invariant system base class. |
| [`StateSpace`](generated/scipy.signal.StateSpace.html#scipy.signal.StateSpace "scipy.signal.StateSpace")(\*system[,Â dt]) | Linear Time Invariant system in state-space form. |
| [`TransferFunction`](generated/scipy.signal.TransferFunction.html#scipy.signal.TransferFunction "scipy.signal.TransferFunction")(\*system[,Â dt]) | Linear Time Invariant system class in transfer function form. |
| [`ZerosPolesGain`](generated/scipy.signal.ZerosPolesGain.html#scipy.signal.ZerosPolesGain "scipy.signal.ZerosPolesGain")(\*system[,Â dt]) | Linear Time Invariant system class in zeros, poles, gain form. |
| [`lsim`](generated/scipy.signal.lsim.html#scipy.signal.lsim "scipy.signal.lsim")(system,Â U,Â T[,Â X0,Â interp]) | Simulate output of a continuous-time linear system. |
| [`impulse`](generated/scipy.signal.impulse.html#scipy.signal.impulse "scipy.signal.impulse")(system[,Â X0,Â T,Â N]) | Impulse response of continuous-time system. |
| [`step`](generated/scipy.signal.step.html#scipy.signal.step "scipy.signal.step")(system[,Â X0,Â T,Â N]) | Step response of continuous-time system. |
| [`freqresp`](generated/scipy.signal.freqresp.html#scipy.signal.freqresp "scipy.signal.freqresp")(system[,Â w,Â n]) | Calculate the frequency response of a continuous-time system. |
| [`bode`](generated/scipy.signal.bode.html#scipy.signal.bode "scipy.signal.bode")(system[,Â w,Â n]) | Calculate Bode magnitude and phase data of a continuous-time system. |
## Discrete-time linear systems[#](#discrete-time-linear-systems "Link to this heading")
|  |  |
| --- | --- |
| [`dlti`](generated/scipy.signal.dlti.html#scipy.signal.dlti "scipy.signal.dlti")(\*system[,Â dt]) | Discrete-time linear time invariant system base class. |
| [`StateSpace`](generated/scipy.signal.StateSpace.html#scipy.signal.StateSpace "scipy.signal.StateSpace")(\*system[,Â dt]) | Linear Time Invariant system in state-space form. |
| [`TransferFunction`](generated/scipy.signal.TransferFunction.html#scipy.signal.TransferFunction "scipy.signal.TransferFunction")(\*system[,Â dt]) | Linear Time Invariant system class in transfer function form. |
| [`ZerosPolesGain`](generated/scipy.signal.ZerosPolesGain.html#scipy.signal.ZerosPolesGain "scipy.signal.ZerosPolesGain")(\*system[,Â dt]) | Linear Time Invariant system class in zeros, poles, gain form. |
| [`dlsim`](generated/scipy.signal.dlsim.html#scipy.signal.dlsim "scipy.signal.dlsim")(system,Â u[,Â t,Â x0]) | Simulate output of a discrete-time linear system. |
| [`dimpulse`](generated/scipy.signal.dimpulse.html#scipy.signal.dimpulse "scipy.signal.dimpulse")(system[,Â x0,Â t,Â n]) | Impulse response of discrete-time system. |
| [`dstep`](generated/scipy.signal.dstep.html#scipy.signal.dstep "scipy.signal.dstep")(system[,Â x0,Â t,Â n]) | Step response of discrete-time system. |
| [`dfreqresp`](generated/scipy.signal.dfreqresp.html#scipy.signal.dfreqresp "scipy.signal.dfreqresp")(system[,Â w,Â n,Â whole]) | Calculate the frequency response of a discrete-time system. |
| [`dbode`](generated/scipy.signal.dbode.html#scipy.signal.dbode "scipy.signal.dbode")(system[,Â w,Â n]) | Calculate Bode magnitude and phase data of a discrete-time system. |
## LTI representations[#](#lti-representations "Link to this heading")
|  |  |
| --- | --- |
| [`tf2zpk`](generated/scipy.signal.tf2zpk.html#scipy.signal.tf2zpk "scipy.signal.tf2zpk")(b,Â a) | Return zero, pole, gain (z, p, k) representation from a numerator, denominator representation of a linear filter. |
| [`tf2sos`](generated/scipy.signal.tf2sos.html#scipy.signal.tf2sos "scipy.signal.tf2sos")(b,Â a[,Â pairing,Â analog]) | Return second-order sections from transfer function representation. |
| [`tf2ss`](generated/scipy.signal.tf2ss.html#scipy.signal.tf2ss "scipy.signal.tf2ss")(num,Â den) | Transfer function to state-space representation. |
| [`zpk2tf`](generated/scipy.signal.zpk2tf.html#scipy.signal.zpk2tf "scipy.signal.zpk2tf")(z,Â p,Â k) | Return polynomial transfer function representation from zeros and poles. |
| [`zpk2sos`](generated/scipy.signal.zpk2sos.html#scipy.signal.zpk2sos "scipy.signal.zpk2sos")(z,Â p,Â k[,Â pairing,Â analog]) | Return second-order sections from zeros, poles, and gain of a system. |
| [`zpk2ss`](generated/scipy.signal.zpk2ss.html#scipy.signal.zpk2ss "scipy.signal.zpk2ss")(z,Â p,Â k) | Zero-pole-gain representation to state-space representation. |
| [`ss2tf`](generated/scipy.signal.ss2tf.html#scipy.signal.ss2tf "scipy.signal.ss2tf")(A,Â B,Â C,Â D[,Â input]) | State-space to transfer function. |
| [`ss2zpk`](generated/scipy.signal.ss2zpk.html#scipy.signal.ss2zpk "scipy.signal.ss2zpk")(A,Â B,Â C,Â D[,Â input]) | State-space representation to zero-pole-gain representation. |
| [`sos2zpk`](generated/scipy.signal.sos2zpk.html#scipy.signal.sos2zpk "scipy.signal.sos2zpk")(sos) | Return zeros, poles, and gain of a series of second-order sections. |
| [`sos2tf`](generated/scipy.signal.sos2tf.html#scipy.signal.sos2tf "scipy.signal.sos2tf")(sos) | Return a single transfer function from a series of second-order sections. |
| [`cont2discrete`](generated/scipy.signal.cont2discrete.html#scipy.signal.cont2discrete "scipy.signal.cont2discrete")(system,Â dt[,Â method,Â alpha]) | Transform a continuous to a discrete state-space system. |
| [`place_poles`](generated/scipy.signal.place_poles.html#scipy.signal.place_poles "scipy.signal.place_poles")(A,Â B,Â poles[,Â method,Â rtol,Â maxiter]) | Compute K such that eigenvalues (A - dot(B, K))=poles. |
## Waveforms[#](#waveforms "Link to this heading")
|  |  |
| --- | --- |
| [`chirp`](generated/scipy.signal.chirp.html#scipy.signal.chirp "scipy.signal.chirp")(t,Â f0,Â t1,Â f1[,Â method,Â phi,Â ...]) | Frequency-swept cosine generator. |
| [`gausspulse`](generated/scipy.signal.gausspulse.html#scipy.signal.gausspulse "scipy.signal.gausspulse")(t[,Â fc,Â bw,Â bwr,Â tpr,Â retquad,Â ...]) | Return a Gaussian modulated sinusoid. |
| [`max_len_seq`](generated/scipy.signal.max_len_seq.html#scipy.signal.max_len_seq "scipy.signal.max_len_seq")(nbits[,Â state,Â length,Â taps]) | Maximum length sequence (MLS) generator. |
| [`sawtooth`](generated/scipy.signal.sawtooth.html#scipy.signal.sawtooth "scipy.signal.sawtooth")(t[,Â width]) | Return a periodic sawtooth or triangle waveform. |
| [`square`](generated/scipy.signal.square.html#scipy.signal.square "scipy.signal.square")(t[,Â duty]) | Return a periodic square-wave waveform. |
| [`sweep_poly`](generated/scipy.signal.sweep_poly.html#scipy.signal.sweep_poly "scipy.signal.sweep_poly")(t,Â poly[,Â phi]) | Frequency-swept cosine generator, with a time-dependent frequency. |
| [`unit_impulse`](generated/scipy.signal.unit_impulse.html#scipy.signal.unit_impulse "scipy.signal.unit_impulse")(shape[,Â idx,Â dtype]) | Unit impulse signal (discrete delta function) or unit basis vector. |
## Window functions[#](#window-functions "Link to this heading")
For window functions, see the [`scipy.signal.windows`](signal.windows.html#module-scipy.signal.windows "scipy.signal.windows") namespace.
In the [`scipy.signal`](#module-scipy.signal "scipy.signal") namespace, there is a convenience function to
obtain these windows by name:
|  |  |
| --- | --- |
| [`get_window`](generated/scipy.signal.get_window.html#scipy.signal.get_window "scipy.signal.get_window")(window,Â Nx[,Â fftbins,Â xp,Â device]) | Convenience function for creating various windows. |
## Peak finding[#](#peak-finding "Link to this heading")
|  |  |
| --- | --- |
| [`argrelmin`](generated/scipy.signal.argrelmin.html#scipy.signal.argrelmin "scipy.signal.argrelmin")(data[,Â axis,Â order,Â mode]) | Calculate the relative minima of *data*. |
| [`argrelmax`](generated/scipy.signal.argrelmax.html#scipy.signal.argrelmax "scipy.signal.argrelmax")(data[,Â axis,Â order,Â mode]) | Calculate the relative maxima of *data*. |
| [`argrelextrema`](generated/scipy.signal.argrelextrema.html#scipy.signal.argrelextrema "scipy.signal.argrelextrema")(data,Â comparator[,Â axis,Â ...]) | Calculate the relative extrema of *data*. |
| [`find_peaks`](generated/scipy.signal.find_peaks.html#scipy.signal.find_peaks "scipy.signal.find_peaks")(x[,Â height,Â threshold,Â distance,Â ...]) | Find peaks inside a signal based on peak properties. |
| [`find_peaks_cwt`](generated/scipy.signal.find_peaks_cwt.html#scipy.signal.find_peaks_cwt "scipy.signal.find_peaks_cwt")(vector,Â widths[,Â wavelet,Â ...]) | Find peaks in a 1-D array with wavelet transformation. |
| [`peak_prominences`](generated/scipy.signal.peak_prominences.html#scipy.signal.peak_prominences "scipy.signal.peak_prominences")(x,Â peaks[,Â wlen]) | Calculate the prominence of each peak in a signal. |
| [`peak_widths`](generated/scipy.signal.peak_widths.html#scipy.signal.peak_widths "scipy.signal.peak_widths")(x,Â peaks[,Â rel\_height,Â ...]) | Calculate the width of each peak in a signal. |
## Spectral analysis[#](#spectral-analysis "Link to this heading")
|  |  |
| --- | --- |
| [`periodogram`](generated/scipy.signal.periodogram.html#scipy.signal.periodogram "scipy.signal.periodogram")(x[,Â fs,Â window,Â nfft,Â detrend,Â ...]) | Estimate power spectral density using a periodogram. |
| [`welch`](generated/scipy.signal.welch.html#scipy.signal.welch "scipy.signal.welch")(x[,Â fs,Â window,Â nperseg,Â noverlap,Â ...]) | Estimate power spectral density using Welch's method. |
| [`csd`](generated/scipy.signal.csd.html#scipy.signal.csd "scipy.signal.csd")(x,Â y[,Â fs,Â window,Â nperseg,Â noverlap,Â ...]) | Estimate the cross power spectral density, Pxy, using Welch's method. |
| [`coherence`](generated/scipy.signal.coherence.html#scipy.signal.coherence "scipy.signal.coherence")(x,Â y[,Â fs,Â window,Â nperseg,Â ...]) | Estimate the magnitude squared coherence estimate, Cxy, of discrete-time signals X and Y using Welch's method. |
| [`spectrogram`](generated/scipy.signal.spectrogram.html#scipy.signal.spectrogram "scipy.signal.spectrogram")(x[,Â fs,Â window,Â nperseg,Â ...]) | Compute a spectrogram with consecutive Fourier transforms (legacy function). |
| [`lombscargle`](generated/scipy.signal.lombscargle.html#scipy.signal.lombscargle "scipy.signal.lombscargle")(x,Â y,Â freqs,Â \*[,Â precenter,Â ...]) | Compute the generalized Lomb-Scargle periodogram. |
| [`vectorstrength`](generated/scipy.signal.vectorstrength.html#scipy.signal.vectorstrength "scipy.signal.vectorstrength")(events,Â period) | Determine the vector strength of the events corresponding to the given period. |
| [`ShortTimeFFT`](generated/scipy.signal.ShortTimeFFT.html#scipy.signal.ShortTimeFFT "scipy.signal.ShortTimeFFT")(win,Â hop,Â fs,Â \*[,Â fft\_mode,Â ...]) | Provide a parametrized discrete Short-time Fourier transform (stft) and its inverse (istft). |
| [`closest_STFT_dual_window`](generated/scipy.signal.closest_STFT_dual_window.html#scipy.signal.closest_STFT_dual_window "scipy.signal.closest_STFT_dual_window")(win,Â hop[,Â ...]) | Calculate the STFT dual window of a given window closest to a desired dual window. |
| [`stft`](generated/scipy.signal.stft.html#scipy.signal.stft "scipy.signal.stft")(x[,Â fs,Â window,Â nperseg,Â noverlap,Â ...]) | Compute the Short Time Fourier Transform (legacy function). |
| [`istft`](generated/scipy.signal.istft.html#scipy.signal.istft "scipy.signal.istft")(Zxx[,Â fs,Â window,Â nperseg,Â noverlap,Â ...]) | Perform the inverse Short Time Fourier transform (legacy function). |
| [`check_COLA`](generated/scipy.signal.check_COLA.html#scipy.signal.check_COLA "scipy.signal.check_COLA")(window,Â nperseg,Â noverlap[,Â tol]) | Check whether the Constant OverLap Add (COLA) constraint is met (legacy function). |
| [`check_NOLA`](generated/scipy.signal.check_NOLA.html#scipy.signal.check_NOLA "scipy.signal.check_NOLA")(window,Â nperseg,Â noverlap[,Â tol]) | Check whether the Nonzero Overlap Add (NOLA) constraint is met. |
## Chirp Z-transform and Zoom FFT[#](#chirp-z-transform-and-zoom-fft "Link to this heading")
|  |  |
| --- | --- |
| [`czt`](generated/czt-function.html#scipy.signal.czt "scipy.signal.czt")(x[,Â m,Â w,Â a,Â axis]) | Compute the frequency response around a spiral in the Z plane. |
| [`zoom_fft`](generated/scipy.signal.zoom_fft.html#scipy.signal.zoom_fft "scipy.signal.zoom_fft")(x,Â fn[,Â m,Â fs,Â endpoint,Â axis]) | Compute the DFT of *x* only for frequencies in range *fn*. |
| [`CZT`](generated/scipy.signal.CZT.html#scipy.signal.CZT "scipy.signal.CZT")(n[,Â m,Â w,Â a]) | Create a callable chirp z-transform function. |
| [`ZoomFFT`](generated/scipy.signal.ZoomFFT.html#scipy.signal.ZoomFFT "scipy.signal.ZoomFFT")(n,Â fn[,Â m,Â fs,Â endpoint]) | Create a callable zoom FFT transform function. |
| [`czt_points`](generated/scipy.signal.czt_points.html#scipy.signal.czt_points "scipy.signal.czt_points")(m[,Â w,Â a]) | Return the points at which the chirp z-transform is computed. |
The functions are simpler to use than the classes, but are less efficient when
using the same transform on many arrays of the same length, since they
repeatedly generate the same chirp signal with every call. In these cases,
use the classes to create a reusable function instead.
[previous
diagbroyden](generated/scipy.optimize.diagbroyden.html "previous page")
[next
Window functions (`scipy.signal.windows`)](signal.windows.html "next page")
On this page
* [Convolution](#convolution)
* [B-splines](#b-splines)
* [Filtering](#filtering)
* [Filter design](#filter-design)
* [Matlab-style IIR filter design](#matlab-style-iir-filter-design)
* [Continuous-time linear systems](#continuous-time-linear-systems)
* [Discrete-time linear systems](#discrete-time-linear-systems)
* [LTI representations](#lti-representations)
* [Waveforms](#waveforms)
* [Window functions](#window-functions)
* [Peak finding](#peak-finding)
* [Spectral analysis](#spectral-analysis)
* [Chirp Z-transform and Zoom FFT](#chirp-z-transform-and-zoom-fft)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/signal.windows.html#module-scipy.signal.windows -->
* [SciPy API](index.html)
* [Signal processing (`scipy.signal`)](signal.html)
* Window functions (`scipy.signal.windows`)
# Window functions ([`scipy.signal.windows`](#module-scipy.signal.windows "scipy.signal.windows"))[#](#window-functions-scipy-signal-windows "Link to this heading")
The suite of window functions for filtering and spectral estimation.
|  |  |
| --- | --- |
| [`get_window`](generated/scipy.signal.windows.get_window.html#scipy.signal.windows.get_window "scipy.signal.windows.get_window")(window,Â Nx[,Â fftbins,Â xp,Â device]) | Convenience function for creating various windows. |
| [`barthann`](generated/scipy.signal.windows.barthann.html#scipy.signal.windows.barthann "scipy.signal.windows.barthann")(M[,Â sym,Â xp,Â device]) | Return a modified Bartlett-Hann window. |
| [`bartlett`](generated/scipy.signal.windows.bartlett.html#scipy.signal.windows.bartlett "scipy.signal.windows.bartlett")(M[,Â sym,Â xp,Â device]) | Return a Bartlett window. |
| [`blackman`](generated/scipy.signal.windows.blackman.html#scipy.signal.windows.blackman "scipy.signal.windows.blackman")(M[,Â sym,Â xp,Â device]) | Return a Blackman window. |
| [`blackmanharris`](generated/scipy.signal.windows.blackmanharris.html#scipy.signal.windows.blackmanharris "scipy.signal.windows.blackmanharris")(M[,Â sym,Â xp,Â device]) | Return a minimum 4-term Blackman-Harris window. |
| [`bohman`](generated/scipy.signal.windows.bohman.html#scipy.signal.windows.bohman "scipy.signal.windows.bohman")(M[,Â sym,Â xp,Â device]) | Return a Bohman window. |
| [`boxcar`](generated/scipy.signal.windows.boxcar.html#scipy.signal.windows.boxcar "scipy.signal.windows.boxcar")(M[,Â sym,Â xp,Â device]) | Return a boxcar or rectangular window. |
| [`chebwin`](generated/scipy.signal.windows.chebwin.html#scipy.signal.windows.chebwin "scipy.signal.windows.chebwin")(M,Â at[,Â sym,Â xp,Â device]) | Return a Dolph-Chebyshev window. |
| [`cosine`](generated/scipy.signal.windows.cosine.html#scipy.signal.windows.cosine "scipy.signal.windows.cosine")(M[,Â sym,Â xp,Â device]) | Return a window with a simple cosine shape. |
| [`dpss`](generated/scipy.signal.windows.dpss.html#scipy.signal.windows.dpss "scipy.signal.windows.dpss")(M,Â NW[,Â Kmax,Â sym,Â norm,Â ...]) | Compute the Discrete Prolate Spheroidal Sequences (DPSS). |
| [`exponential`](generated/scipy.signal.windows.exponential.html#scipy.signal.windows.exponential "scipy.signal.windows.exponential")(M[,Â center,Â tau,Â sym,Â xp,Â device]) | Return an exponential (or Poisson) window. |
| [`flattop`](generated/scipy.signal.windows.flattop.html#scipy.signal.windows.flattop "scipy.signal.windows.flattop")(M[,Â sym,Â xp,Â device]) | Return a flat top window. |
| [`gaussian`](generated/scipy.signal.windows.gaussian.html#scipy.signal.windows.gaussian "scipy.signal.windows.gaussian")(M,Â std[,Â sym,Â xp,Â device]) | Return a Gaussian window. |
| [`general_cosine`](generated/scipy.signal.windows.general_cosine.html#scipy.signal.windows.general_cosine "scipy.signal.windows.general_cosine")(M,Â a[,Â sym]) | Generic weighted sum of cosine terms window. |
| [`general_gaussian`](generated/scipy.signal.windows.general_gaussian.html#scipy.signal.windows.general_gaussian "scipy.signal.windows.general_gaussian")(M,Â p,Â sig[,Â sym,Â xp,Â device]) | Return a window with a generalized Gaussian shape. |
| [`general_hamming`](generated/scipy.signal.windows.general_hamming.html#scipy.signal.windows.general_hamming "scipy.signal.windows.general_hamming")(M,Â alpha[,Â sym,Â xp,Â device]) | Return a generalized Hamming window. |
| [`hamming`](generated/scipy.signal.windows.hamming.html#scipy.signal.windows.hamming "scipy.signal.windows.hamming")(M[,Â sym,Â xp,Â device]) | Return a Hamming window. |
| [`hann`](generated/scipy.signal.windows.hann.html#scipy.signal.windows.hann "scipy.signal.windows.hann")(M[,Â sym,Â xp,Â device]) | Return a Hann window. |
| [`kaiser`](generated/scipy.signal.windows.kaiser.html#scipy.signal.windows.kaiser "scipy.signal.windows.kaiser")(M,Â beta[,Â sym,Â xp,Â device]) | Return a Kaiser window. |
| [`kaiser_bessel_derived`](generated/scipy.signal.windows.kaiser_bessel_derived.html#scipy.signal.windows.kaiser_bessel_derived "scipy.signal.windows.kaiser_bessel_derived")(M,Â beta,Â \*[,Â sym,Â xp,Â ...]) | Return a Kaiser-Bessel derived window. |
| [`lanczos`](generated/scipy.signal.windows.lanczos.html#scipy.signal.windows.lanczos "scipy.signal.windows.lanczos")(M,Â \*[,Â sym,Â xp,Â device]) | Return a Lanczos window also known as a sinc window. |
| [`nuttall`](generated/scipy.signal.windows.nuttall.html#scipy.signal.windows.nuttall "scipy.signal.windows.nuttall")(M[,Â sym,Â xp,Â device]) | Return a minimum 4-term Blackman-Harris window according to Nuttall. |
| [`parzen`](generated/scipy.signal.windows.parzen.html#scipy.signal.windows.parzen "scipy.signal.windows.parzen")(M[,Â sym,Â xp,Â device]) | Return a Parzen window. |
| [`taylor`](generated/scipy.signal.windows.taylor.html#scipy.signal.windows.taylor "scipy.signal.windows.taylor")(M[,Â nbar,Â sll,Â norm,Â sym,Â xp,Â device]) | Return a Taylor window. |
| [`triang`](generated/scipy.signal.windows.triang.html#scipy.signal.windows.triang "scipy.signal.windows.triang")(M[,Â sym,Â xp,Â device]) | Return a triangular window. |
| [`tukey`](generated/scipy.signal.windows.tukey.html#scipy.signal.windows.tukey "scipy.signal.windows.tukey")(M[,Â alpha,Â sym,Â xp,Â device]) | Return a Tukey window, also known as a tapered cosine window. |
[previous
Signal processing (`scipy.signal`)](signal.html "previous page")
[next
get\_window](generated/scipy.signal.windows.get_window.html "next page")
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/sparse.html#module-scipy.sparse -->
* [SciPy API](index.html)
* Sparse arrays (`scipy.sparse`)
# Sparse arrays ([`scipy.sparse`](#module-scipy.sparse "scipy.sparse"))[#](#sparse-arrays-scipy-sparse "Link to this heading")
SciPy 2-D sparse array package for numeric data.
Warning
SciPy sparse is shifting from a sparse matrix interface to a sparse
array interface. In the next few releases we expect to deprecate the
sparse matrix interface. For documentation of the matrix
interface, see the [spmatrix interface docs](sparse.spmatrix_api.html#spmatrix-api).
For guidance on converting existing code to sparse arrays, see
[Migration from spmatrix to sparray](sparse.migration_to_sparray.html#migration-to-sparray).
## Submodules[#](#submodules "Link to this heading")
|  |  |
| --- | --- |
| [`csgraph`](sparse.csgraph.html#module-scipy.sparse.csgraph "scipy.sparse.csgraph") | Compressed sparse graph routines (scipy.sparse.csgraph) |
| [`linalg`](sparse.linalg.html#module-scipy.sparse.linalg "scipy.sparse.linalg") | Sparse linear algebra (scipy.sparse.linalg) |
## Sparse array classes[#](#sparse-array-classes "Link to this heading")
|  |  |
| --- | --- |
| [`bsr_array`](generated/scipy.sparse.bsr_array.html#scipy.sparse.bsr_array "scipy.sparse.bsr_array")(arg1[,Â shape,Â dtype,Â copy,Â ...]) | Block Sparse Row format sparse array. |
| [`coo_array`](generated/scipy.sparse.coo_array.html#scipy.sparse.coo_array "scipy.sparse.coo_array")(arg1[,Â shape,Â dtype,Â copy,Â maxprint]) | A sparse array in COOrdinate format. |
| [`csc_array`](generated/scipy.sparse.csc_array.html#scipy.sparse.csc_array "scipy.sparse.csc_array")(arg1[,Â shape,Â dtype,Â copy,Â maxprint]) | Compressed Sparse Column array. |
| [`csr_array`](generated/scipy.sparse.csr_array.html#scipy.sparse.csr_array "scipy.sparse.csr_array")(arg1[,Â shape,Â dtype,Â copy,Â maxprint]) | Compressed Sparse Row array. |
| [`dia_array`](generated/scipy.sparse.dia_array.html#scipy.sparse.dia_array "scipy.sparse.dia_array")(arg1[,Â shape,Â dtype,Â copy,Â maxprint]) | Sparse array with DIAgonal storage. |
| [`dok_array`](generated/scipy.sparse.dok_array.html#scipy.sparse.dok_array "scipy.sparse.dok_array")(arg1[,Â shape,Â dtype,Â copy,Â maxprint]) | Dictionary Of Keys based sparse array. |
| [`lil_array`](generated/scipy.sparse.lil_array.html#scipy.sparse.lil_array "scipy.sparse.lil_array")(arg1[,Â shape,Â dtype,Â copy,Â maxprint]) | Row-based LIst of Lists sparse array. |
| [`sparray`](generated/scipy.sparse.sparray.html#scipy.sparse.sparray "scipy.sparse.sparray")() | This class provides a base class for all sparse array and matrix classes. |
### Building sparse arrays[#](#building-sparse-arrays "Link to this heading")
|  |  |
| --- | --- |
| [`diags_array`](generated/scipy.sparse.diags_array.html#scipy.sparse.diags_array "scipy.sparse.diags_array")(diagonals,Â /,Â \*[,Â offsets,Â ...]) | Construct a sparse array from diagonals. |
| [`eye_array`](generated/scipy.sparse.eye_array.html#scipy.sparse.eye_array "scipy.sparse.eye_array")(m[,Â n,Â k,Â dtype,Â format]) | Sparse array of chosen shape with ones on the kth diagonal and zeros elsewhere. |
| [`random_array`](generated/scipy.sparse.random_array.html#scipy.sparse.random_array "scipy.sparse.random_array")(shape,Â \*[,Â density,Â format,Â ...]) | Return a sparse array of uniformly random numbers in [0, 1). |
| [`block_array`](generated/scipy.sparse.block_array.html#scipy.sparse.block_array "scipy.sparse.block_array")(blocks,Â \*[,Â format,Â dtype]) | Build a sparse array from sparse sub-blocks. |
### Combining arrays[#](#combining-arrays "Link to this heading")
|  |  |
| --- | --- |
| [`kron`](generated/scipy.sparse.kron.html#scipy.sparse.kron "scipy.sparse.kron")(A,Â B[,Â format]) | Sparse representation of the Kronecker product of *A* and *B*. |
| [`kronsum`](generated/scipy.sparse.kronsum.html#scipy.sparse.kronsum "scipy.sparse.kronsum")(A,Â B[,Â format]) | Kronecker sum of square sparse matrices *A* and *B*. |
| [`block_diag`](generated/scipy.sparse.block_diag.html#scipy.sparse.block_diag "scipy.sparse.block_diag")(mats[,Â format,Â dtype]) | Build a block diagonal sparse matrix or array from provided matrices. |
| [`tril`](generated/scipy.sparse.tril.html#scipy.sparse.tril "scipy.sparse.tril")(A[,Â k,Â format]) | Return the lower triangular portion of a sparse array or matrix. |
| [`triu`](generated/scipy.sparse.triu.html#scipy.sparse.triu "scipy.sparse.triu")(A[,Â k,Â format]) | Return the upper triangular portion of a sparse array or matrix. |
| [`hstack`](generated/scipy.sparse.hstack.html#scipy.sparse.hstack "scipy.sparse.hstack")(blocks[,Â format,Â dtype]) | Stack sparse matrices horizontally (column wise). |
| [`vstack`](generated/scipy.sparse.vstack.html#scipy.sparse.vstack "scipy.sparse.vstack")(blocks[,Â format,Â dtype]) | Stack sparse arrays vertically (row wise). |
### Manipulating arrays[#](#manipulating-arrays "Link to this heading")
|  |  |
| --- | --- |
| [`matrix_transpose`](generated/scipy.sparse.matrix_transpose.html#scipy.sparse.matrix_transpose "scipy.sparse.matrix_transpose")(A) | Return the matrix transpose of *A*. |
| [`swapaxes`](generated/scipy.sparse.swapaxes.html#scipy.sparse.swapaxes "scipy.sparse.swapaxes")(A,Â axis1,Â axis2) | Interchange two axes of an array. |
| [`expand_dims`](generated/scipy.sparse.expand_dims.html#scipy.sparse.expand_dims "scipy.sparse.expand_dims")(A,Â /,Â \*[,Â axis]) | Add trivial axes to an array. |
| [`permute_dims`](generated/scipy.sparse.permute_dims.html#scipy.sparse.permute_dims "scipy.sparse.permute_dims")(A[,Â axes,Â copy]) | Permute the axes of the sparse array *A* to the order *axes*. |
### Sparse tools[#](#sparse-tools "Link to this heading")
|  |  |
| --- | --- |
| [`save_npz`](generated/scipy.sparse.save_npz.html#scipy.sparse.save_npz "scipy.sparse.save_npz")(file,Â matrix[,Â compressed]) | Save a sparse matrix or array to a file using `.npz` format. |
| [`load_npz`](generated/scipy.sparse.load_npz.html#scipy.sparse.load_npz "scipy.sparse.load_npz")(file) | Load a sparse array/matrix from a file using `.npz` format. |
| [`find`](generated/scipy.sparse.find.html#scipy.sparse.find "scipy.sparse.find")(A) | Return the indices and values of the nonzero elements of a matrix. |
| [`get_index_dtype`](generated/scipy.sparse.get_index_dtype.html#scipy.sparse.get_index_dtype "scipy.sparse.get_index_dtype")([arrays,Â maxval,Â check\_contents]) | Based on input (integer) arrays *a*, determine a suitable index data type that can hold the data in the arrays. |
| [`safely_cast_index_arrays`](generated/scipy.sparse.safely_cast_index_arrays.html#scipy.sparse.safely_cast_index_arrays "scipy.sparse.safely_cast_index_arrays")(A[,Â idx\_dtype,Â msg]) | Safely cast sparse array indices to *idx\_dtype*. |
### Identifying sparse arrays[#](#identifying-sparse-arrays "Link to this heading")
|  |  |
| --- | --- |
| [`issparse`](generated/scipy.sparse.issparse.html#scipy.sparse.issparse "scipy.sparse.issparse")(x) | Is *x* either sparse array or sparse matrix type? |
| [`isspmatrix`](generated/scipy.sparse.isspmatrix.html#scipy.sparse.isspmatrix "scipy.sparse.isspmatrix")(x) | Is *x* of a sparse matrix type? |
## Warnings[#](#warnings "Link to this heading")
|  |  |
| --- | --- |
| [`SparseEfficiencyWarning`](generated/scipy.sparse.SparseEfficiencyWarning.html#scipy.sparse.SparseEfficiencyWarning "scipy.sparse.SparseEfficiencyWarning") | The warning emitted when the operation is inefficient for sparse matrices. |
| [`SparseWarning`](generated/scipy.sparse.SparseWarning.html#scipy.sparse.SparseWarning "scipy.sparse.SparseWarning") | General warning for [`scipy.sparse`](#module-scipy.sparse "scipy.sparse"). |
## Usage information[#](#usage-information "Link to this heading")
There are seven available sparse array types:
1. csc\_array: Compressed Sparse Column format
2. csr\_array: Compressed Sparse Row format
3. bsr\_array: Block Sparse Row format
4. lil\_array: List of Lists format
5. dok\_array: Dictionary of Keys format
6. coo\_array: COOrdinate format (aka IJV, triplet format)
7. dia\_array: DIAgonal format
To construct an array efficiently, use any of [`coo_array`](generated/scipy.sparse.coo_array.html#scipy.sparse.coo_array "scipy.sparse.coo_array"),
[`dok_array`](generated/scipy.sparse.dok_array.html#scipy.sparse.dok_array "scipy.sparse.dok_array") or [`lil_array`](generated/scipy.sparse.lil_array.html#scipy.sparse.lil_array "scipy.sparse.lil_array"). They each support basic slicing
and fancy indexing with a similar syntax to NumPy arrays.
The COO format is recommended and other formats use it under the hood to
allow efficient construction using data values and coordinate arrays.
Despite their similarity to NumPy arrays, it is **strongly discouraged**
to use NumPy functions directly on these arrays because NumPy typically
treats them as generic Python objects rather than arrays, leading to
unexpected (and incorrect) results. If you are tempted to apply a NumPy
function to these arrays, check if SciPy has its own implementation
for the given sparse array class and, if not, **convert the sparse array
to a NumPy array** (e.g., using the *toarray* method of the class)
before applying the method.
All conversions among the CSR, CSC, and COO formats are efficient,
linear-time operations.
To perform manipulations such as multiplication or inversion, first
convert the array to either CSC or CSR format. The [`lil_array`](generated/scipy.sparse.lil_array.html#scipy.sparse.lil_array "scipy.sparse.lil_array")
format is row-based, so conversion to CSR is efficient, but
conversion to CSC is less so.
### Matrix vector product[#](#matrix-vector-product "Link to this heading")
To do a vector product between a 2D sparse array and a vector use
the matmul operator (i.e., `@`) which performs a dot product (like the
`dot` method):
```
>>> import numpy as np
>>> from scipy.sparse import csr_array
>>> A = csr_array([[1, 2, 0], [0, 0, 3], [4, 0, 5]])
>>> v = np.array([1, 0, -1])
>>> A @ v
array([ 1, -3, -1], dtype=int64)
```
The CSR format is especially suitable for fast matrix vector products.
### Example 1[#](#example-1 "Link to this heading")
Construct a 1000x1000 [`lil_array`](generated/scipy.sparse.lil_array.html#scipy.sparse.lil_array "scipy.sparse.lil_array") and add some values to it:
```
>>> from scipy.sparse import lil_array
>>> from scipy.sparse.linalg import spsolve
>>> from numpy.linalg import solve, norm
>>> from numpy.random import rand
```
```
>>> A = lil_array((1000, 1000))
>>> A[0, :100] = rand(100)
>>> A.setdiag(rand(1000))
```
Now convert it to CSR format and solve A x = b for x:
```
>>> A = A.tocsr()
>>> b = rand(1000)
>>> x = spsolve(A, b)
```
Convert it to a dense array and solve, and check that the result
is the same:
```
>>> x_ = solve(A.toarray(), b)
```
Now we can compute norm of the error with:
```
>>> err = norm(x-x_)
>>> err < 1e-9
True
```
It should be small :)
### Example 2[#](#example-2 "Link to this heading")
Construct an array in COO format:
```
>>> from scipy import sparse
>>> from numpy import array
>>> I = array([0,3,1,0])
>>> J = array([0,3,1,2])
>>> V = array([4,5,7,9])
>>> A = sparse.coo_array((V,(I,J)),shape=(4,4))
```
Notice that the indices do not need to be sorted.
Duplicate (i,j) entries are summed when converting to CSR or CSC.
```
>>> I = array([0,0,1,3,1,0,0])
>>> J = array([0,2,1,3,1,0,0])
>>> V = array([1,1,1,1,1,1,1])
>>> B = sparse.coo_array((V,(I,J)),shape=(4,4)).tocsr()
```
This is useful for constructing finite-element stiffness and mass matrices.
### Further details[#](#further-details "Link to this heading")
CSR column indices are not necessarily sorted. Likewise for CSC row
indices. And similarly for COO coordinates. Use the `.sorted_indices()`
and `.sort_indices()` methods when sorted indices are required (e.g.,
when passing data to other libraries).
[previous
czt\_points](generated/scipy.signal.czt_points.html "previous page")
[next
Compressed sparse graph routines (`scipy.sparse.csgraph`)](sparse.csgraph.html "next page")
On this page
* [Submodules](#submodules)
* [Sparse array classes](#sparse-array-classes)
  + [Building sparse arrays](#building-sparse-arrays)
  + [Combining arrays](#combining-arrays)
  + [Manipulating arrays](#manipulating-arrays)
  + [Sparse tools](#sparse-tools)
  + [Identifying sparse arrays](#identifying-sparse-arrays)
* [Warnings](#warnings)
* [Usage information](#usage-information)
  + [Matrix vector product](#matrix-vector-product)
  + [Example 1](#example-1)
  + [Example 2](#example-2)
  + [Further details](#further-details)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html#module-scipy.sparse.linalg -->
* [SciPy API](index.html)
* [Sparse arrays (`scipy.sparse`)](sparse.html)
* Sparse linear algebra (`scipy.sparse.linalg`)
# Sparse linear algebra ([`scipy.sparse.linalg`](#module-scipy.sparse.linalg "scipy.sparse.linalg"))[#](#sparse-linear-algebra-scipy-sparse-linalg "Link to this heading")
## Abstract linear operators[#](#abstract-linear-operators "Link to this heading")
|  |  |
| --- | --- |
| [`LinearOperator`](generated/scipy.sparse.linalg.LinearOperator.html#scipy.sparse.linalg.LinearOperator "scipy.sparse.linalg.LinearOperator")(\*args,Â \*\*kwargs) | Common interface for performing matrix vector products. |
| [`aslinearoperator`](generated/scipy.sparse.linalg.aslinearoperator.html#scipy.sparse.linalg.aslinearoperator "scipy.sparse.linalg.aslinearoperator")(A) | Return *A* as a [`LinearOperator`](generated/scipy.sparse.linalg.LinearOperator.html#scipy.sparse.linalg.LinearOperator "scipy.sparse.linalg.LinearOperator"). |
## Matrix Operations[#](#matrix-operations "Link to this heading")
|  |  |
| --- | --- |
| [`inv`](generated/scipy.sparse.linalg.inv.html#scipy.sparse.linalg.inv "scipy.sparse.linalg.inv")(A) | Compute the inverse of a sparse arrays. |
| [`expm`](generated/scipy.sparse.linalg.expm.html#scipy.sparse.linalg.expm "scipy.sparse.linalg.expm")(A) | Compute the matrix exponential using Pade approximation. |
| [`expm_multiply`](generated/scipy.sparse.linalg.expm_multiply.html#scipy.sparse.linalg.expm_multiply "scipy.sparse.linalg.expm_multiply")(A,Â B[,Â start,Â stop,Â num,Â ...]) | Compute the action of the matrix exponential of A on B. |
| [`funm_multiply_krylov`](generated/scipy.sparse.linalg.funm_multiply_krylov.html#scipy.sparse.linalg.funm_multiply_krylov "scipy.sparse.linalg.funm_multiply_krylov")(f,Â A,Â b,Â \*[,Â assume\_a,Â ...]) | A restarted Krylov method for evaluating `y = f(tA) b` from [[R4392c003a72c-1]](generated/scipy.sparse.linalg.funm_multiply_krylov.html#r4392c003a72c-1) [[R4392c003a72c-2]](generated/scipy.sparse.linalg.funm_multiply_krylov.html#r4392c003a72c-2). |
| [`matrix_power`](generated/scipy.sparse.linalg.matrix_power.html#scipy.sparse.linalg.matrix_power "scipy.sparse.linalg.matrix_power")(A,Â power) | Raise a square matrix to the integer power, *power*. |
## Matrix norms[#](#matrix-norms "Link to this heading")
|  |  |
| --- | --- |
| [`norm`](generated/scipy.sparse.linalg.norm.html#scipy.sparse.linalg.norm "scipy.sparse.linalg.norm")(x[,Â ord,Â axis]) | Norm of a sparse matrix. |
| [`onenormest`](generated/scipy.sparse.linalg.onenormest.html#scipy.sparse.linalg.onenormest "scipy.sparse.linalg.onenormest")(A[,Â t,Â itmax,Â compute\_v,Â compute\_w]) | Compute a lower bound of the 1-norm of a sparse array. |
## Solving linear problems[#](#solving-linear-problems "Link to this heading")
Direct methods for linear equation systems:
|  |  |
| --- | --- |
| [`spsolve`](generated/scipy.sparse.linalg.spsolve.html#scipy.sparse.linalg.spsolve "scipy.sparse.linalg.spsolve")(A,Â b[,Â permc\_spec,Â use\_umfpack]) | Solve the sparse linear system Ax=b, where b may be a vector or a matrix. |
| [`spsolve_triangular`](generated/scipy.sparse.linalg.spsolve_triangular.html#scipy.sparse.linalg.spsolve_triangular "scipy.sparse.linalg.spsolve_triangular")(A,Â b[,Â lower,Â ...]) | Solve the equation `A x = b` for *x*, assuming A is a triangular matrix. |
| [`is_sptriangular`](generated/scipy.sparse.linalg.is_sptriangular.html#scipy.sparse.linalg.is_sptriangular "scipy.sparse.linalg.is_sptriangular")(A) | Returns 2-tuple indicating lower/upper triangular structure for sparse `A`. |
| [`spbandwidth`](generated/scipy.sparse.linalg.spbandwidth.html#scipy.sparse.linalg.spbandwidth "scipy.sparse.linalg.spbandwidth")(A) | Return the lower and upper bandwidth of a 2D numeric array. |
| [`factorized`](generated/scipy.sparse.linalg.factorized.html#scipy.sparse.linalg.factorized "scipy.sparse.linalg.factorized")(A) | Return a function for solving a sparse linear system, with A pre-factorized. |
| [`MatrixRankWarning`](generated/scipy.sparse.linalg.MatrixRankWarning.html#scipy.sparse.linalg.MatrixRankWarning "scipy.sparse.linalg.MatrixRankWarning") | Warning for exactly singular matrices. |
| [`use_solver`](generated/scipy.sparse.linalg.use_solver.html#scipy.sparse.linalg.use_solver "scipy.sparse.linalg.use_solver")(\*\*kwargs) | Select default sparse direct solver to be used. |
Iterative methods for linear equation systems:
|  |  |
| --- | --- |
| [`bicg`](generated/scipy.sparse.linalg.bicg.html#scipy.sparse.linalg.bicg "scipy.sparse.linalg.bicg")(A,Â b[,Â x0,Â rtol,Â atol,Â maxiter,Â M,Â ...]) | Solve `Ax = b` with the BIConjugate Gradient method. |
| [`bicgstab`](generated/scipy.sparse.linalg.bicgstab.html#scipy.sparse.linalg.bicgstab "scipy.sparse.linalg.bicgstab")(A,Â b[,Â x0,Â rtol,Â atol,Â maxiter,Â M,Â ...]) | Solve `Ax = b` with the BIConjugate Gradient STABilized method. |
| [`cg`](generated/scipy.sparse.linalg.cg.html#scipy.sparse.linalg.cg "scipy.sparse.linalg.cg")(A,Â b[,Â x0,Â rtol,Â atol,Â maxiter,Â M,Â callback]) | Solve `Ax = b` with the Conjugate Gradient method, for a symmetric, positive-definite *A*. |
| [`cgs`](generated/scipy.sparse.linalg.cgs.html#scipy.sparse.linalg.cgs "scipy.sparse.linalg.cgs")(A,Â b[,Â x0,Â rtol,Â atol,Â maxiter,Â M,Â callback]) | Solve `Ax = b` with the Conjugate Gradient Squared method. |
| [`gmres`](generated/scipy.sparse.linalg.gmres.html#scipy.sparse.linalg.gmres "scipy.sparse.linalg.gmres")(A,Â b[,Â x0,Â rtol,Â atol,Â restart,Â ...]) | Solve `Ax = b` with the Generalized Minimal RESidual method. |
| [`lgmres`](generated/scipy.sparse.linalg.lgmres.html#scipy.sparse.linalg.lgmres "scipy.sparse.linalg.lgmres")(A,Â b[,Â x0,Â rtol,Â atol,Â maxiter,Â M,Â ...]) | Solve `Ax = b` with the LGMRES algorithm. |
| [`minres`](generated/scipy.sparse.linalg.minres.html#scipy.sparse.linalg.minres "scipy.sparse.linalg.minres")(A,Â b[,Â x0,Â rtol,Â shift,Â maxiter,Â M,Â ...]) | Solve `Ax = b` with the MINimum RESidual method, for a real symmetric or complex hermitian matrix *A*. |
| [`qmr`](generated/scipy.sparse.linalg.qmr.html#scipy.sparse.linalg.qmr "scipy.sparse.linalg.qmr")(A,Â b[,Â x0,Â rtol,Â atol,Â maxiter,Â M1,Â M2,Â ...]) | Solve `Ax = b` with the Quasi-Minimal Residual method. |
| [`gcrotmk`](generated/scipy.sparse.linalg.gcrotmk.html#scipy.sparse.linalg.gcrotmk "scipy.sparse.linalg.gcrotmk")(A,Â b[,Â x0,Â rtol,Â atol,Â maxiter,Â M,Â ...]) | Solve `Ax = b` with the flexible GCROT(m,k) algorithm. |
| [`tfqmr`](generated/scipy.sparse.linalg.tfqmr.html#scipy.sparse.linalg.tfqmr "scipy.sparse.linalg.tfqmr")(A,Â b[,Â x0,Â rtol,Â atol,Â maxiter,Â M,Â ...]) | Solve `Ax = b` with the Transpose-Free Quasi-Minimal Residual method. |
Iterative methods for least-squares problems:
|  |  |
| --- | --- |
| [`lsqr`](generated/scipy.sparse.linalg.lsqr.html#scipy.sparse.linalg.lsqr "scipy.sparse.linalg.lsqr")(A,Â b[,Â damp,Â atol,Â btol,Â conlim,Â ...]) | Find the least-squares solution to a large, sparse, linear system of equations. |
| [`lsmr`](generated/scipy.sparse.linalg.lsmr.html#scipy.sparse.linalg.lsmr "scipy.sparse.linalg.lsmr")(A,Â b[,Â damp,Â atol,Â btol,Â conlim,Â ...]) | Iterative solver for least-squares problems. |
## Matrix factorizations[#](#matrix-factorizations "Link to this heading")
Eigenvalue problems:
|  |  |
| --- | --- |
| [`eigs`](generated/scipy.sparse.linalg.eigs.html#scipy.sparse.linalg.eigs "scipy.sparse.linalg.eigs")(A[,Â k,Â M,Â sigma,Â which,Â v0,Â ncv,Â ...]) | Find k eigenvalues and eigenvectors of the square matrix A. |
| [`eigsh`](generated/scipy.sparse.linalg.eigsh.html#scipy.sparse.linalg.eigsh "scipy.sparse.linalg.eigsh")(A[,Â k,Â M,Â sigma,Â which,Â v0,Â ncv,Â ...]) | Find k eigenvalues and eigenvectors of the real symmetric square matrix or complex Hermitian matrix A. |
| [`lobpcg`](generated/scipy.sparse.linalg.lobpcg.html#scipy.sparse.linalg.lobpcg "scipy.sparse.linalg.lobpcg")(A,Â X[,Â B,Â M,Â Y,Â tol,Â maxiter,Â ...]) | Locally Optimal Block Preconditioned Conjugate Gradient Method (LOBPCG). |
Singular values problems:
|  |  |
| --- | --- |
| [`svds`](generated/scipy.sparse.linalg.svds.html#scipy.sparse.linalg.svds "scipy.sparse.linalg.svds")(A[,Â k,Â ncv,Â tol,Â which,Â v0,Â maxiter,Â ...]) | Partial singular value decomposition of a sparse matrix. |
The [`svds`](generated/scipy.sparse.linalg.svds.html#scipy.sparse.linalg.svds "scipy.sparse.linalg.svds") function supports the following solvers:
* [svds(solver=âarpackâ)](sparse.linalg.svds-arpack.html)
* [svds(solver=âlobpcgâ)](sparse.linalg.svds-lobpcg.html)
* [svds(solver=âpropackâ)](sparse.linalg.svds-propack.html)
Complete or incomplete LU factorizations
|  |  |
| --- | --- |
| [`splu`](generated/scipy.sparse.linalg.splu.html#scipy.sparse.linalg.splu "scipy.sparse.linalg.splu")(A[,Â permc\_spec,Â diag\_pivot\_thresh,Â ...]) | Compute the LU decomposition of a sparse, square matrix. |
| [`spilu`](generated/scipy.sparse.linalg.spilu.html#scipy.sparse.linalg.spilu "scipy.sparse.linalg.spilu")(A[,Â drop\_tol,Â fill\_factor,Â drop\_rule,Â ...]) | Compute an incomplete LU decomposition for a sparse, square matrix. |
| [`SuperLU`](generated/scipy.sparse.linalg.SuperLU.html#scipy.sparse.linalg.SuperLU "scipy.sparse.linalg.SuperLU")() | LU factorization of a sparse matrix. |
## Sparse arrays with structure[#](#sparse-arrays-with-structure "Link to this heading")
|  |  |
| --- | --- |
| [`LaplacianNd`](generated/scipy.sparse.linalg.LaplacianNd.html#scipy.sparse.linalg.LaplacianNd "scipy.sparse.linalg.LaplacianNd")(\*args,Â \*\*kwargs) | The grid Laplacian in `N` dimensions and its eigenvalues/eigenvectors. |
## Exceptions[#](#exceptions "Link to this heading")
|  |  |
| --- | --- |
| [`ArpackNoConvergence`](generated/scipy.sparse.linalg.ArpackNoConvergence.html#scipy.sparse.linalg.ArpackNoConvergence "scipy.sparse.linalg.ArpackNoConvergence")(msg,Â eigenvalues,Â ...) | ARPACK iteration did not converge. |
| [`ArpackError`](generated/scipy.sparse.linalg.ArpackError.html#scipy.sparse.linalg.ArpackError "scipy.sparse.linalg.ArpackError")(info[,Â infodict]) | ARPACK error. |
[previous
reconstruct\_path](generated/scipy.sparse.csgraph.reconstruct_path.html "previous page")
[next
LinearOperator](generated/scipy.sparse.linalg.LinearOperator.html "next page")
On this page
* [Abstract linear operators](#abstract-linear-operators)
* [Matrix Operations](#matrix-operations)
* [Matrix norms](#matrix-norms)
* [Solving linear problems](#solving-linear-problems)
* [Matrix factorizations](#matrix-factorizations)
* [Sparse arrays with structure](#sparse-arrays-with-structure)
* [Exceptions](#exceptions)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html#module-scipy.sparse.csgraph -->
* [SciPy API](index.html)
* [Sparse arrays (`scipy.sparse`)](sparse.html)
* Compressed sparse graph routines (`scipy.sparse.csgraph`)
# Compressed sparse graph routines ([`scipy.sparse.csgraph`](#module-scipy.sparse.csgraph "scipy.sparse.csgraph"))[#](#compressed-sparse-graph-routines-scipy-sparse-csgraph "Link to this heading")
Fast graph algorithms based on sparse matrix representations.
## Contents[#](#contents "Link to this heading")
|  |  |
| --- | --- |
| [`connected_components`](generated/scipy.sparse.csgraph.connected_components.html#scipy.sparse.csgraph.connected_components "scipy.sparse.csgraph.connected_components")(csgraph[,Â directed,Â ...]) | Analyze the connected components of a sparse graph. |
| [`laplacian`](generated/scipy.sparse.csgraph.laplacian.html#scipy.sparse.csgraph.laplacian "scipy.sparse.csgraph.laplacian")(csgraph[,Â normed,Â return\_diag,Â ...]) | Return the Laplacian of a directed graph. |
| [`shortest_path`](generated/scipy.sparse.csgraph.shortest_path.html#scipy.sparse.csgraph.shortest_path "scipy.sparse.csgraph.shortest_path")(csgraph[,Â method,Â directed,Â ...]) | Perform a shortest-path graph search on a positive directed or undirected graph. |
| [`dijkstra`](generated/scipy.sparse.csgraph.dijkstra.html#scipy.sparse.csgraph.dijkstra "scipy.sparse.csgraph.dijkstra")(csgraph[,Â directed,Â indices,Â ...]) | Dijkstra algorithm using priority queue. |
| [`floyd_warshall`](generated/scipy.sparse.csgraph.floyd_warshall.html#scipy.sparse.csgraph.floyd_warshall "scipy.sparse.csgraph.floyd_warshall")(csgraph[,Â directed,Â ...]) | Compute the shortest path lengths using the Floyd-Warshall algorithm. |
| [`bellman_ford`](generated/scipy.sparse.csgraph.bellman_ford.html#scipy.sparse.csgraph.bellman_ford "scipy.sparse.csgraph.bellman_ford")(csgraph[,Â directed,Â indices,Â ...]) | Compute the shortest path lengths using the Bellman-Ford algorithm. |
| [`johnson`](generated/scipy.sparse.csgraph.johnson.html#scipy.sparse.csgraph.johnson "scipy.sparse.csgraph.johnson")(csgraph[,Â directed,Â indices,Â ...]) | Compute the shortest path lengths using Johnson's algorithm. |
| [`yen`](generated/scipy.sparse.csgraph.yen.html#scipy.sparse.csgraph.yen "scipy.sparse.csgraph.yen")(csgraph,Â source,Â sink,Â K,Â \*[,Â directed,Â ...]) | Yen's K-Shortest Paths algorithm on a directed or undirected graph. |
| [`breadth_first_order`](generated/scipy.sparse.csgraph.breadth_first_order.html#scipy.sparse.csgraph.breadth_first_order "scipy.sparse.csgraph.breadth_first_order")(csgraph,Â i\_start[,Â ...]) | Return a breadth-first ordering starting with specified node. |
| [`depth_first_order`](generated/scipy.sparse.csgraph.depth_first_order.html#scipy.sparse.csgraph.depth_first_order "scipy.sparse.csgraph.depth_first_order")(csgraph,Â i\_start[,Â ...]) | Return a depth-first ordering starting with specified node. |
| [`breadth_first_tree`](generated/scipy.sparse.csgraph.breadth_first_tree.html#scipy.sparse.csgraph.breadth_first_tree "scipy.sparse.csgraph.breadth_first_tree")(csgraph,Â i\_start[,Â directed]) | Return the tree generated by a breadth-first search. |
| [`depth_first_tree`](generated/scipy.sparse.csgraph.depth_first_tree.html#scipy.sparse.csgraph.depth_first_tree "scipy.sparse.csgraph.depth_first_tree")(csgraph,Â i\_start[,Â directed]) | Return a tree generated by a depth-first search. |
| [`minimum_spanning_tree`](generated/scipy.sparse.csgraph.minimum_spanning_tree.html#scipy.sparse.csgraph.minimum_spanning_tree "scipy.sparse.csgraph.minimum_spanning_tree")(csgraph[,Â overwrite]) | Return a minimum spanning tree of an undirected graph. |
| [`reverse_cuthill_mckee`](generated/scipy.sparse.csgraph.reverse_cuthill_mckee.html#scipy.sparse.csgraph.reverse_cuthill_mckee "scipy.sparse.csgraph.reverse_cuthill_mckee")(graph[,Â symmetric\_mode]) | Returns the permutation array that orders a sparse CSR or CSC matrix in Reverse-Cuthill McKee ordering. |
| [`maximum_flow`](generated/scipy.sparse.csgraph.maximum_flow.html#scipy.sparse.csgraph.maximum_flow "scipy.sparse.csgraph.maximum_flow")(csgraph,Â source,Â sink) | Maximize the flow between two vertices in a graph. |
| [`maximum_bipartite_matching`](generated/scipy.sparse.csgraph.maximum_bipartite_matching.html#scipy.sparse.csgraph.maximum_bipartite_matching "scipy.sparse.csgraph.maximum_bipartite_matching")(graph[,Â perm\_type]) | Returns a matching of a bipartite graph whose cardinality is at least that of any given matching of the graph. |
| [`min_weight_full_bipartite_matching`](generated/scipy.sparse.csgraph.min_weight_full_bipartite_matching.html#scipy.sparse.csgraph.min_weight_full_bipartite_matching "scipy.sparse.csgraph.min_weight_full_bipartite_matching")(biadjacency) | Returns the minimum weight full matching of a bipartite graph. |
| [`structural_rank`](generated/scipy.sparse.csgraph.structural_rank.html#scipy.sparse.csgraph.structural_rank "scipy.sparse.csgraph.structural_rank")(graph) | Compute the structural rank of a graph (matrix) with a given sparsity pattern. |
| [`NegativeCycleError`](generated/scipy.sparse.csgraph.NegativeCycleError.html#scipy.sparse.csgraph.NegativeCycleError "scipy.sparse.csgraph.NegativeCycleError")([message]) | Negative cycle in graph. |
|  |  |
| --- | --- |
| [`construct_dist_matrix`](generated/scipy.sparse.csgraph.construct_dist_matrix.html#scipy.sparse.csgraph.construct_dist_matrix "scipy.sparse.csgraph.construct_dist_matrix")(graph,Â predecessors[,Â ...]) | Construct distance matrix from a predecessor matrix. |
| [`csgraph_from_dense`](generated/scipy.sparse.csgraph.csgraph_from_dense.html#scipy.sparse.csgraph.csgraph_from_dense "scipy.sparse.csgraph.csgraph_from_dense")(graph[,Â null\_value,Â ...]) | Construct a CSR-format sparse graph from a dense matrix. |
| [`csgraph_from_masked`](generated/scipy.sparse.csgraph.csgraph_from_masked.html#scipy.sparse.csgraph.csgraph_from_masked "scipy.sparse.csgraph.csgraph_from_masked")(graph) | Construct a CSR-format graph from a masked array. |
| [`csgraph_masked_from_dense`](generated/scipy.sparse.csgraph.csgraph_masked_from_dense.html#scipy.sparse.csgraph.csgraph_masked_from_dense "scipy.sparse.csgraph.csgraph_masked_from_dense")(graph[,Â ...]) | Construct a masked array graph representation from a dense matrix. |
| [`csgraph_to_dense`](generated/scipy.sparse.csgraph.csgraph_to_dense.html#scipy.sparse.csgraph.csgraph_to_dense "scipy.sparse.csgraph.csgraph_to_dense")(csgraph[,Â null\_value]) | Convert a sparse graph representation to a dense representation. |
| [`csgraph_to_masked`](generated/scipy.sparse.csgraph.csgraph_to_masked.html#scipy.sparse.csgraph.csgraph_to_masked "scipy.sparse.csgraph.csgraph_to_masked")(csgraph) | Convert a sparse graph representation to a masked array representation. |
| [`reconstruct_path`](generated/scipy.sparse.csgraph.reconstruct_path.html#scipy.sparse.csgraph.reconstruct_path "scipy.sparse.csgraph.reconstruct_path")(csgraph,Â predecessors[,Â ...]) | Construct a tree from a graph and a predecessor list. |
## Graph Representations[#](#graph-representations "Link to this heading")
This module uses graphs which are stored in a matrix format. A
graph with N nodes can be represented by an (N x N) adjacency matrix G.
If there is a connection from node i to node j, then G[i, j] = w, where
w is the weight of the connection. For nodes i and j which are
not connected, the value depends on the representation:
* for dense array representations, non-edges are represented by
  G[i, j] = 0, infinity, or NaN.
* for dense masked representations (of type np.ma.MaskedArray), non-edges
  are represented by masked values. This can be useful when graphs with
  zero-weight edges are desired.
* for sparse array representations, non-edges are represented by
  non-entries in the matrix. This sort of sparse representation also
  allows for edges with zero weights.
As a concrete example, imagine that you would like to represent the following
undirected graph:
```
      G
     (0)
    /   \
   1     2
  /       \
(2)       (1)
```
This graph has three nodes, where node 0 and 1 are connected by an edge of
weight 2, and nodes 0 and 2 are connected by an edge of weight 1.
We can construct the dense, masked, and sparse representations as follows,
keeping in mind that an undirected graph is represented by a symmetric matrix:
```
>>> import numpy as np
>>> G_dense = np.array([[0, 2, 1],
...                     [2, 0, 0],
...                     [1, 0, 0]])
>>> G_masked = np.ma.masked_values(G_dense, 0)
>>> from scipy.sparse import csr_array
>>> G_sparse = csr_array(G_dense)
```
This becomes more difficult when zero edges are significant. For example,
consider the situation when we slightly modify the above graph:
```
     G2
     (0)
    /   \
   0     2
  /       \
(2)       (1)
```
This is identical to the previous graph, except nodes 0 and 2 are connected
by an edge of zero weight. In this case, the dense representation above
leads to ambiguities: how can non-edges be represented if zero is a meaningful
value? In this case, either a masked or sparse representation must be used
to eliminate the ambiguity:
```
>>> import numpy as np
>>> G2_data = np.array([[np.inf, 2,      0     ],
...                     [2,      np.inf, np.inf],
...                     [0,      np.inf, np.inf]])
>>> G2_masked = np.ma.masked_invalid(G2_data)
>>> from scipy.sparse.csgraph import csgraph_from_dense
>>> # G2_sparse = csr_array(G2_data) would give the wrong result
>>> G2_sparse = csgraph_from_dense(G2_data, null_value=np.inf)
>>> G2_sparse.data
array([ 2.,  0.,  2.,  0.])
```
Here we have used a utility routine from the csgraph submodule in order to
convert the dense representation to a sparse representation which can be
understood by the algorithms in submodule. By viewing the data array, we
can see that the zero values are explicitly encoded in the graph.
### Directed vs. undirected[#](#directed-vs-undirected "Link to this heading")
Matrices may represent either directed or undirected graphs. This is
specified throughout the csgraph module by a boolean keyword. Graphs are
assumed to be directed by default. In a directed graph, traversal from node
i to node j can be accomplished over the edge G[i, j], but not the edge
G[j, i]. Consider the following dense graph:
```
>>> import numpy as np
>>> G_dense = np.array([[0, 1, 0],
...                     [2, 0, 3],
...                     [0, 4, 0]])
```
When `directed=True` we get the graph:
```
  ---1--> ---3-->
(0)     (1)     (2)
  <--2--- <--4---
```
In a non-directed graph, traversal from node i to node j can be
accomplished over either G[i, j] or G[j, i]. If both edges are not null,
and the two have unequal weights, then the smaller of the two is used.
So for the same graph, when `directed=False` we get the graph:
```
(0)--1--(1)--3--(2)
```
Note that a symmetric matrix will represent an undirected graph, regardless
of whether the âdirectedâ keyword is set to True or False. In this case,
using `directed=True` generally leads to more efficient computation.
The routines in this module accept as input either scipy.sparse representations
(csr, csc, or lil format), masked representations, or dense representations
with non-edges indicated by zeros, infinities, and NaN entries.
[previous
Sparse arrays (`scipy.sparse`)](sparse.html "previous page")
[next
connected\_components](generated/scipy.sparse.csgraph.connected_components.html "next page")
On this page
* [Contents](#contents)
* [Graph Representations](#graph-representations)
  + [Directed vs. undirected](#directed-vs-undirected)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/spatial.html#module-scipy.spatial -->
* [SciPy API](index.html)
* Spatial algorithms and data structures (`scipy.spatial`)
# Spatial algorithms and data structures ([`scipy.spatial`](#module-scipy.spatial "scipy.spatial"))[#](#spatial-algorithms-and-data-structures-scipy-spatial "Link to this heading")
## Spatial transformations[#](#spatial-transformations "Link to this heading")
These are contained in the [`scipy.spatial.transform`](spatial.transform.html#module-scipy.spatial.transform "scipy.spatial.transform") submodule.
## Nearest-neighbor queries[#](#nearest-neighbor-queries "Link to this heading")
|  |  |
| --- | --- |
| [`KDTree`](generated/scipy.spatial.KDTree.html#scipy.spatial.KDTree "scipy.spatial.KDTree")(data[,Â leafsize,Â compact\_nodes,Â ...]) | kd-tree for quick nearest-neighbor lookup. |
| [`cKDTree`](generated/scipy.spatial.cKDTree.html#scipy.spatial.cKDTree "scipy.spatial.cKDTree")(data[,Â leafsize,Â compact\_nodes,Â ...]) | kd-tree for quick nearest-neighbor lookup. |
| [`Rectangle`](generated/scipy.spatial.Rectangle.html#scipy.spatial.Rectangle "scipy.spatial.Rectangle")(maxes,Â mins) | Hyperrectangle class. |
## Distance metrics[#](#distance-metrics "Link to this heading")
Distance metrics are contained in the [`scipy.spatial.distance`](spatial.distance.html#module-scipy.spatial.distance "scipy.spatial.distance") submodule.
## Delaunay triangulation, convex hulls, and Voronoi diagrams[#](#delaunay-triangulation-convex-hulls-and-voronoi-diagrams "Link to this heading")
|  |  |
| --- | --- |
| [`Delaunay`](generated/scipy.spatial.Delaunay.html#scipy.spatial.Delaunay "scipy.spatial.Delaunay")(points[,Â furthest\_site,Â ...]) | Delaunay tessellation in N dimensions. |
| [`ConvexHull`](generated/scipy.spatial.ConvexHull.html#scipy.spatial.ConvexHull "scipy.spatial.ConvexHull")(points[,Â incremental,Â qhull\_options]) | Convex hulls in N dimensions. |
| [`Voronoi`](generated/scipy.spatial.Voronoi.html#scipy.spatial.Voronoi "scipy.spatial.Voronoi")(points[,Â furthest\_site,Â ...]) | Voronoi diagrams in N dimensions. |
| [`SphericalVoronoi`](generated/scipy.spatial.SphericalVoronoi.html#scipy.spatial.SphericalVoronoi "scipy.spatial.SphericalVoronoi")(points[,Â radius,Â center,Â ...]) | Voronoi diagrams on the surface of a sphere. |
| [`HalfspaceIntersection`](generated/scipy.spatial.HalfspaceIntersection.html#scipy.spatial.HalfspaceIntersection "scipy.spatial.HalfspaceIntersection")(halfspaces,Â interior\_point) | Halfspace intersections in N dimensions. |
## Plotting helpers[#](#plotting-helpers "Link to this heading")
|  |  |
| --- | --- |
| [`delaunay_plot_2d`](generated/scipy.spatial.delaunay_plot_2d.html#scipy.spatial.delaunay_plot_2d "scipy.spatial.delaunay_plot_2d")(tri[,Â ax]) | Plot the given Delaunay triangulation in 2-D. |
| [`convex_hull_plot_2d`](generated/scipy.spatial.convex_hull_plot_2d.html#scipy.spatial.convex_hull_plot_2d "scipy.spatial.convex_hull_plot_2d")(hull[,Â ax]) | Plot the given convex hull diagram in 2-D. |
| [`voronoi_plot_2d`](generated/scipy.spatial.voronoi_plot_2d.html#scipy.spatial.voronoi_plot_2d "scipy.spatial.voronoi_plot_2d")(vor[,Â ax]) | Plot the given Voronoi diagram in 2-D. |
See also
[Tutorial](../tutorial/spatial.html#qhulltutorial)
## Simplex representation[#](#simplex-representation "Link to this heading")
The simplices (triangles, tetrahedra, etc.) appearing in the Delaunay
tessellation (N-D simplices), convex hull facets, and Voronoi ridges
(N-1-D simplices) are represented in the following scheme:
```
tess = Delaunay(points)
hull = ConvexHull(points)
voro = Voronoi(points)
# coordinates of the jth vertex of the ith simplex
tess.points[tess.simplices[i, j], :]        # tessellation element
hull.points[hull.simplices[i, j], :]        # convex hull facet
voro.vertices[voro.ridge_vertices[i, j], :] # ridge between Voronoi cells
```
For Delaunay triangulations and convex hulls, the neighborhood
structure of the simplices satisfies the condition:
`tess.neighbors[i,j]` is the neighboring simplex of the ith
simplex, opposite to the `j`-vertex. It is -1 in case of no neighbor.
Convex hull facets also define a hyperplane equation:
```
(hull.equations[i,:-1] * coord).sum() + hull.equations[i,-1] == 0
```
Similar hyperplane equations for the Delaunay triangulation correspond
to the convex hull facets on the corresponding N+1-D
paraboloid.
The Delaunay triangulation objects offer a method for locating the
simplex containing a given point, and barycentric coordinate
computations.
## Miscellaneous Functions[#](#miscellaneous-functions "Link to this heading")
|  |  |
| --- | --- |
| [`tsearch`](generated/scipy.spatial.tsearch.html#scipy.spatial.tsearch "scipy.spatial.tsearch")(tri,Â xi) | Find simplices containing the given points. |
| [`distance_matrix`](generated/scipy.spatial.distance_matrix.html#scipy.spatial.distance_matrix "scipy.spatial.distance_matrix")(x,Â y[,Â p,Â threshold]) | Compute the distance matrix. |
| [`minkowski_distance`](generated/scipy.spatial.minkowski_distance.html#scipy.spatial.minkowski_distance "scipy.spatial.minkowski_distance")(x,Â y[,Â p]) | Compute the L\*\*p distance between two arrays. |
| [`minkowski_distance_p`](generated/scipy.spatial.minkowski_distance_p.html#scipy.spatial.minkowski_distance_p "scipy.spatial.minkowski_distance_p")(x,Â y[,Â p]) | Compute the pth power of the L\*\*p distance between two arrays. |
| [`procrustes`](generated/scipy.spatial.procrustes.html#scipy.spatial.procrustes "scipy.spatial.procrustes")(data1,Â data2) | Procrustes analysis, a similarity test for two data sets. |
| [`geometric_slerp`](generated/scipy.spatial.geometric_slerp.html#scipy.spatial.geometric_slerp "scipy.spatial.geometric_slerp")(start,Â end,Â t[,Â tol]) | Geometric spherical linear interpolation. |
## Warnings / Errors used in [`scipy.spatial`](#module-scipy.spatial "scipy.spatial")[#](#warnings-errors-used-in-scipy-spatial "Link to this heading")
|  |  |
| --- | --- |
| [`QhullError`](generated/scipy.spatial.QhullError.html#scipy.spatial.QhullError "scipy.spatial.QhullError") | Raised when Qhull encounters an error condition, such as geometrical degeneracy when options to resolve are not enabled. |
[previous
scipy.sparse.SparseWarning](generated/scipy.sparse.SparseWarning.html "previous page")
[next
Distance computations (`scipy.spatial.distance`)](spatial.distance.html "next page")
On this page
* [Spatial transformations](#spatial-transformations)
* [Nearest-neighbor queries](#nearest-neighbor-queries)
* [Distance metrics](#distance-metrics)
* [Delaunay triangulation, convex hulls, and Voronoi diagrams](#delaunay-triangulation-convex-hulls-and-voronoi-diagrams)
* [Plotting helpers](#plotting-helpers)
* [Simplex representation](#simplex-representation)
* [Miscellaneous Functions](#miscellaneous-functions)
* [Warnings / Errors used in `scipy.spatial`](#warnings-errors-used-in-scipy-spatial)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/spatial.distance.html#module-scipy.spatial.distance -->
* [SciPy API](index.html)
* [Spatial algorithms and data structures (`scipy.spatial`)](spatial.html)
* Distance computations (`scipy.spatial.distance`)
# Distance computations ([`scipy.spatial.distance`](#module-scipy.spatial.distance "scipy.spatial.distance"))[#](#distance-computations-scipy-spatial-distance "Link to this heading")
## Function reference[#](#function-reference "Link to this heading")
Distance matrix computation from a collection of raw observation vectors
stored in a rectangular array.
|  |  |
| --- | --- |
| [`pdist`](generated/scipy.spatial.distance.pdist.html#scipy.spatial.distance.pdist "scipy.spatial.distance.pdist")(X[,Â metric,Â out]) | Pairwise distances between observations in n-dimensional space. |
| [`cdist`](generated/scipy.spatial.distance.cdist.html#scipy.spatial.distance.cdist "scipy.spatial.distance.cdist")(XA,Â XB[,Â metric,Â out]) | Compute distance between each pair of the two collections of inputs. |
| [`squareform`](generated/scipy.spatial.distance.squareform.html#scipy.spatial.distance.squareform "scipy.spatial.distance.squareform")(X[,Â force,Â checks]) | Convert a vector-form distance vector to a square-form distance matrix, and vice-versa. |
| [`directed_hausdorff`](generated/scipy.spatial.distance.directed_hausdorff.html#scipy.spatial.distance.directed_hausdorff "scipy.spatial.distance.directed_hausdorff")(u,Â v[,Â rng,Â seed]) | Compute the directed Hausdorff distance between two 2-D arrays. |
Predicates for checking the validity of distance matrices, both
condensed and redundant. Also contained in this module are functions
for computing the number of observations in a distance matrix.
|  |  |
| --- | --- |
| [`is_valid_dm`](generated/scipy.spatial.distance.is_valid_dm.html#scipy.spatial.distance.is_valid_dm "scipy.spatial.distance.is_valid_dm")(D[,Â tol,Â throw,Â name,Â warning]) | Return True if input array satisfies basic distance matrix properties (symmetry and zero diagonal). |
| [`is_valid_y`](generated/scipy.spatial.distance.is_valid_y.html#scipy.spatial.distance.is_valid_y "scipy.spatial.distance.is_valid_y")(y[,Â warning,Â throw,Â name]) | Return True if the input array is a valid condensed distance matrix. |
| [`num_obs_dm`](generated/scipy.spatial.distance.num_obs_dm.html#scipy.spatial.distance.num_obs_dm "scipy.spatial.distance.num_obs_dm")(d) | Return the number of original observations that correspond to a square, redundant distance matrix. |
| [`num_obs_y`](generated/scipy.spatial.distance.num_obs_y.html#scipy.spatial.distance.num_obs_y "scipy.spatial.distance.num_obs_y")(Y) | Return the number of original observations that correspond to a condensed distance matrix. |
Distance functions between two numeric vectors `u` and `v`. Computing
distances over a large collection of vectors is inefficient for these
functions. Use `pdist` for this purpose.
|  |  |
| --- | --- |
| [`braycurtis`](generated/scipy.spatial.distance.braycurtis.html#scipy.spatial.distance.braycurtis "scipy.spatial.distance.braycurtis")(u,Â v[,Â w]) | Compute the Bray-Curtis distance between two 1-D arrays. |
| [`canberra`](generated/scipy.spatial.distance.canberra.html#scipy.spatial.distance.canberra "scipy.spatial.distance.canberra")(u,Â v[,Â w]) | Compute the Canberra distance between two 1-D arrays. |
| [`chebyshev`](generated/scipy.spatial.distance.chebyshev.html#scipy.spatial.distance.chebyshev "scipy.spatial.distance.chebyshev")(u,Â v[,Â w]) | Compute the Chebyshev distance. |
| [`cityblock`](generated/scipy.spatial.distance.cityblock.html#scipy.spatial.distance.cityblock "scipy.spatial.distance.cityblock")(u,Â v[,Â w]) | Compute the City Block (Manhattan) distance. |
| [`correlation`](generated/scipy.spatial.distance.correlation.html#scipy.spatial.distance.correlation "scipy.spatial.distance.correlation")(u,Â v[,Â w,Â centered]) | Compute the correlation distance between two 1-D arrays. |
| [`cosine`](generated/scipy.spatial.distance.cosine.html#scipy.spatial.distance.cosine "scipy.spatial.distance.cosine")(u,Â v[,Â w]) | Compute the Cosine distance between 1-D arrays. |
| [`euclidean`](generated/scipy.spatial.distance.euclidean.html#scipy.spatial.distance.euclidean "scipy.spatial.distance.euclidean")(u,Â v[,Â w]) | Computes the Euclidean distance between two arrays. |
| [`jensenshannon`](generated/scipy.spatial.distance.jensenshannon.html#scipy.spatial.distance.jensenshannon "scipy.spatial.distance.jensenshannon")(p,Â q[,Â base,Â axis,Â keepdims]) | Compute the Jensen-Shannon distance (metric) between two probability arrays. |
| [`mahalanobis`](generated/scipy.spatial.distance.mahalanobis.html#scipy.spatial.distance.mahalanobis "scipy.spatial.distance.mahalanobis")(u,Â v,Â VI) | Compute the Mahalanobis distance between two 1-D arrays. |
| [`minkowski`](generated/scipy.spatial.distance.minkowski.html#scipy.spatial.distance.minkowski "scipy.spatial.distance.minkowski")(u,Â v[,Â p,Â w]) | Compute the Minkowski distance between two arrays. |
| [`seuclidean`](generated/scipy.spatial.distance.seuclidean.html#scipy.spatial.distance.seuclidean "scipy.spatial.distance.seuclidean")(u,Â v,Â V) | Return the standardized Euclidean distance between two 1-D arrays. |
| [`sqeuclidean`](generated/scipy.spatial.distance.sqeuclidean.html#scipy.spatial.distance.sqeuclidean "scipy.spatial.distance.sqeuclidean")(u,Â v[,Â w]) | Compute the squared Euclidean distance between two arrays. |
Distance functions between two boolean vectors (representing sets) `u` and
`v`. As in the case of numerical vectors, `pdist` is more efficient for
computing the distances between all pairs.
|  |  |
| --- | --- |
| [`dice`](generated/scipy.spatial.distance.dice.html#scipy.spatial.distance.dice "scipy.spatial.distance.dice")(u,Â v[,Â w]) | Compute the Dice dissimilarity between two boolean 1-D arrays. |
| [`hamming`](generated/scipy.spatial.distance.hamming.html#scipy.spatial.distance.hamming "scipy.spatial.distance.hamming")(u,Â v[,Â w]) | Compute the Hamming distance between two 1-D arrays. |
| [`jaccard`](generated/scipy.spatial.distance.jaccard.html#scipy.spatial.distance.jaccard "scipy.spatial.distance.jaccard")(u,Â v[,Â w]) | Compute the Jaccard dissimilarity between two boolean vectors. |
| [`rogerstanimoto`](generated/scipy.spatial.distance.rogerstanimoto.html#scipy.spatial.distance.rogerstanimoto "scipy.spatial.distance.rogerstanimoto")(u,Â v[,Â w]) | Compute the Rogers-Tanimoto dissimilarity between two boolean 1-D arrays. |
| [`russellrao`](generated/scipy.spatial.distance.russellrao.html#scipy.spatial.distance.russellrao "scipy.spatial.distance.russellrao")(u,Â v[,Â w]) | Compute the Russell-Rao dissimilarity between two boolean 1-D arrays. |
| [`sokalsneath`](generated/scipy.spatial.distance.sokalsneath.html#scipy.spatial.distance.sokalsneath "scipy.spatial.distance.sokalsneath")(u,Â v[,Â w]) | Compute the Sokal-Sneath dissimilarity between two boolean 1-D arrays. |
| [`yule`](generated/scipy.spatial.distance.yule.html#scipy.spatial.distance.yule "scipy.spatial.distance.yule")(u,Â v[,Â w]) | Compute the Yule dissimilarity between two boolean 1-D arrays. |
[`hamming`](generated/scipy.spatial.distance.hamming.html#scipy.spatial.distance.hamming "scipy.spatial.distance.hamming") also operates over discrete numerical vectors.
[previous
Spatial algorithms and data structures (`scipy.spatial`)](spatial.html "previous page")
[next
pdist](generated/scipy.spatial.distance.pdist.html "next page")
On this page
* [Function reference](#function-reference)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/spatial.transform.html#module-scipy.spatial.transform -->
* [SciPy API](index.html)
* [Spatial algorithms and data structures (`scipy.spatial`)](spatial.html)
* Spatial Transformations (`scipy.spatial.transform`)
# Spatial Transformations ([`scipy.spatial.transform`](#module-scipy.spatial.transform "scipy.spatial.transform"))[#](#spatial-transformations-scipy-spatial-transform "Link to this heading")
This package implements various spatial transformations. For now, rotations
and rigid transforms (rotations and translations) are supported.
## Rotations in 3 dimensions[#](#rotations-in-3-dimensions "Link to this heading")
|  |  |
| --- | --- |
| [`RigidTransform`](generated/scipy.spatial.transform.RigidTransform.html#scipy.spatial.transform.RigidTransform "scipy.spatial.transform.RigidTransform")(matrix[,Â normalize,Â copy]) | Rigid transform in 3 dimensions. |
| [`Rotation`](generated/scipy.spatial.transform.Rotation.html#scipy.spatial.transform.Rotation "scipy.spatial.transform.Rotation")(quat[,Â normalize,Â copy,Â scalar\_first]) | Rotation in 3 dimensions. |
| [`Slerp`](generated/scipy.spatial.transform.Slerp.html#scipy.spatial.transform.Slerp "scipy.spatial.transform.Slerp")(times,Â rotations) | Spherical Linear Interpolation of Rotations. |
| [`RotationSpline`](generated/scipy.spatial.transform.RotationSpline.html#scipy.spatial.transform.RotationSpline "scipy.spatial.transform.RotationSpline")(times,Â rotations) | Interpolate rotations with continuous angular rate and acceleration. |
[previous
yule](generated/scipy.spatial.distance.yule.html "previous page")
[next
RigidTransform](generated/scipy.spatial.transform.RigidTransform.html "next page")
On this page
* [Rotations in 3 dimensions](#rotations-in-3-dimensions)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/special.html#module-scipy.special -->
* [SciPy API](index.html)
* Special functions (`scipy.special`)
# Special functions ([`scipy.special`](#module-scipy.special "scipy.special"))[#](#special-functions-scipy-special "Link to this heading")
Almost all of the functions below accept NumPy arrays as input
arguments as well as single numbers. This means they follow
broadcasting and automatic array-looping rules. Technically,
they are [NumPy universal functions](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-basics).
Functions which do not accept NumPy arrays are marked by a warning
in the section description.
See also
[`scipy.special.cython_special`](special.cython_special.html#module-scipy.special.cython_special "scipy.special.cython_special") â Typed Cython versions of special functions
## Error handling[#](#error-handling "Link to this heading")
Errors are handled by returning NaNs or other appropriate values.
Some of the special function routines can emit warnings or raise
exceptions when an error occurs. By default this is disabled, except
for memory allocation errors, which result in an exception being raised.
To query and control the current error handling state the following
functions are provided.
|  |  |
| --- | --- |
| [`geterr`](generated/scipy.special.geterr.html#scipy.special.geterr "scipy.special.geterr")() | Get the current way of handling special-function errors. |
| [`seterr`](generated/scipy.special.seterr.html#scipy.special.seterr "scipy.special.seterr")(\*\*kwargs) | Set how special-function errors are handled. |
| [`errstate`](generated/scipy.special.errstate.html#scipy.special.errstate "scipy.special.errstate")(\*\*kwargs) | Context manager for special-function error handling. |
| [`SpecialFunctionWarning`](generated/scipy.special.SpecialFunctionWarning.html#scipy.special.SpecialFunctionWarning "scipy.special.SpecialFunctionWarning") | Warning that can be emitted by special functions. |
| [`SpecialFunctionError`](generated/scipy.special.SpecialFunctionError.html#scipy.special.SpecialFunctionError "scipy.special.SpecialFunctionError") | Exception that can be raised by special functions. |
## Available functions[#](#available-functions "Link to this heading")
### Airy functions[#](#airy-functions "Link to this heading")
|  |  |
| --- | --- |
| [`airy`](generated/scipy.special.airy.html#scipy.special.airy "scipy.special.airy")(z[,Â out]) | Airy functions and their derivatives. |
| [`airye`](generated/scipy.special.airye.html#scipy.special.airye "scipy.special.airye")(z[,Â out]) | Exponentially scaled Airy functions and their derivatives. |
| [`ai_zeros`](generated/scipy.special.ai_zeros.html#scipy.special.ai_zeros "scipy.special.ai_zeros")(nt) | Compute *nt* zeros and values of the Airy function Ai and its derivative. |
| [`bi_zeros`](generated/scipy.special.bi_zeros.html#scipy.special.bi_zeros "scipy.special.bi_zeros")(nt) | Compute *nt* zeros and values of the Airy function Bi and its derivative. |
| [`itairy`](generated/scipy.special.itairy.html#scipy.special.itairy "scipy.special.itairy")(x[,Â out]) | Integrals of Airy functions. |
### Elliptic functions and integrals[#](#elliptic-functions-and-integrals "Link to this heading")
|  |  |
| --- | --- |
| [`ellipj`](generated/scipy.special.ellipj.html#scipy.special.ellipj "scipy.special.ellipj")(u,Â m[,Â out]) | Jacobi elliptic functions. |
| [`ellipk`](generated/scipy.special.ellipk.html#scipy.special.ellipk "scipy.special.ellipk")(m[,Â out]) | Complete elliptic integral of the first kind. |
| [`ellipkm1`](generated/scipy.special.ellipkm1.html#scipy.special.ellipkm1 "scipy.special.ellipkm1")(p[,Â out]) | Complete elliptic integral of the first kind around *m* = 1. |
| [`ellipkinc`](generated/scipy.special.ellipkinc.html#scipy.special.ellipkinc "scipy.special.ellipkinc")(phi,Â m[,Â out]) | Incomplete elliptic integral of the first kind. |
| [`ellipe`](generated/scipy.special.ellipe.html#scipy.special.ellipe "scipy.special.ellipe")(m[,Â out]) | Complete elliptic integral of the second kind. |
| [`ellipeinc`](generated/scipy.special.ellipeinc.html#scipy.special.ellipeinc "scipy.special.ellipeinc")(phi,Â m[,Â out]) | Incomplete elliptic integral of the second kind. |
| [`elliprc`](generated/scipy.special.elliprc.html#scipy.special.elliprc "scipy.special.elliprc")(x,Â y[,Â out]) | Degenerate symmetric elliptic integral. |
| [`elliprd`](generated/scipy.special.elliprd.html#scipy.special.elliprd "scipy.special.elliprd")(x,Â y,Â z[,Â out]) | Symmetric elliptic integral of the second kind. |
| [`elliprf`](generated/scipy.special.elliprf.html#scipy.special.elliprf "scipy.special.elliprf")(x,Â y,Â z[,Â out]) | Completely-symmetric elliptic integral of the first kind. |
| [`elliprg`](generated/scipy.special.elliprg.html#scipy.special.elliprg "scipy.special.elliprg")(x,Â y,Â z[,Â out]) | Completely-symmetric elliptic integral of the second kind. |
| [`elliprj`](generated/scipy.special.elliprj.html#scipy.special.elliprj "scipy.special.elliprj")(x,Â y,Â z,Â p[,Â out]) | Symmetric elliptic integral of the third kind. |
### Bessel functions[#](#bessel-functions "Link to this heading")
|  |  |
| --- | --- |
| [`jv`](generated/scipy.special.jv.html#scipy.special.jv "scipy.special.jv")(v,Â z[,Â out]) | Bessel function of the first kind of real order and complex argument. |
| [`jve`](generated/scipy.special.jve.html#scipy.special.jve "scipy.special.jve")(v,Â z[,Â out]) | Exponentially scaled Bessel function of the first kind of order *v*. |
| [`yn`](generated/scipy.special.yn.html#scipy.special.yn "scipy.special.yn")(n,Â x[,Â out]) | Bessel function of the second kind of integer order and real argument. |
| [`yv`](generated/scipy.special.yv.html#scipy.special.yv "scipy.special.yv")(v,Â z[,Â out]) | Bessel function of the second kind of real order and complex argument. |
| [`yve`](generated/scipy.special.yve.html#scipy.special.yve "scipy.special.yve")(v,Â z[,Â out]) | Exponentially scaled Bessel function of the second kind of real order. |
| [`iv`](generated/scipy.special.iv.html#scipy.special.iv "scipy.special.iv")(v,Â z[,Â out]) | Modified Bessel function of the first kind of real order. |
| [`ive`](generated/scipy.special.ive.html#scipy.special.ive "scipy.special.ive")(v,Â z[,Â out]) | Exponentially scaled modified Bessel function of the first kind. |
| [`kn`](generated/scipy.special.kn.html#scipy.special.kn "scipy.special.kn")(n,Â x[,Â out]) | Modified Bessel function of the second kind of integer order *n*. |
| [`kv`](generated/scipy.special.kv.html#scipy.special.kv "scipy.special.kv")(v,Â z[,Â out]) | Modified Bessel function of the second kind of real order *v*. |
| [`kve`](generated/scipy.special.kve.html#scipy.special.kve "scipy.special.kve")(v,Â z[,Â out]) | Exponentially scaled modified Bessel function of the second kind. |
| [`hankel1`](generated/scipy.special.hankel1.html#scipy.special.hankel1 "scipy.special.hankel1")(v,Â z[,Â out]) | Hankel function of the first kind. |
| [`hankel1e`](generated/scipy.special.hankel1e.html#scipy.special.hankel1e "scipy.special.hankel1e")(v,Â z[,Â out]) | Exponentially scaled Hankel function of the first kind. |
| [`hankel2`](generated/scipy.special.hankel2.html#scipy.special.hankel2 "scipy.special.hankel2")(v,Â z[,Â out]) | Hankel function of the second kind. |
| [`hankel2e`](generated/scipy.special.hankel2e.html#scipy.special.hankel2e "scipy.special.hankel2e")(v,Â z[,Â out]) | Exponentially scaled Hankel function of the second kind. |
| [`wright_bessel`](generated/scipy.special.wright_bessel.html#scipy.special.wright_bessel "scipy.special.wright_bessel")(a,Â b,Â x[,Â out]) | Wright's generalized Bessel function. |
| [`log_wright_bessel`](generated/scipy.special.log_wright_bessel.html#scipy.special.log_wright_bessel "scipy.special.log_wright_bessel")(a,Â b,Â x[,Â out]) | Natural logarithm of Wright's generalized Bessel function, see [`wright_bessel`](generated/scipy.special.wright_bessel.html#scipy.special.wright_bessel "scipy.special.wright_bessel"). |
The following function does not accept NumPy arrays (it is not a
universal function):
|  |  |
| --- | --- |
| [`lmbda`](generated/scipy.special.lmbda.html#scipy.special.lmbda "scipy.special.lmbda")(v,Â x) | Jahnke-Emden Lambda function, Lambdav(x). |
#### Zeros of Bessel functions[#](#zeros-of-bessel-functions "Link to this heading")
The following functions do not accept NumPy arrays (they are not
universal functions):
|  |  |
| --- | --- |
| [`jnjnp_zeros`](generated/scipy.special.jnjnp_zeros.html#scipy.special.jnjnp_zeros "scipy.special.jnjnp_zeros")(nt) | Compute zeros of integer-order Bessel functions Jn and Jn'. |
| [`jnyn_zeros`](generated/scipy.special.jnyn_zeros.html#scipy.special.jnyn_zeros "scipy.special.jnyn_zeros")(n,Â nt) | Compute nt zeros of Bessel functions Jn(x), Jn'(x), Yn(x), and Yn'(x). |
| [`jn_zeros`](generated/scipy.special.jn_zeros.html#scipy.special.jn_zeros "scipy.special.jn_zeros")(n,Â nt) | Compute zeros of integer-order Bessel functions Jn. |
| [`jnp_zeros`](generated/scipy.special.jnp_zeros.html#scipy.special.jnp_zeros "scipy.special.jnp_zeros")(n,Â nt) | Compute zeros of integer-order Bessel function derivatives Jn'. |
| [`yn_zeros`](generated/scipy.special.yn_zeros.html#scipy.special.yn_zeros "scipy.special.yn_zeros")(n,Â nt) | Compute zeros of integer-order Bessel function Yn(x). |
| [`ynp_zeros`](generated/scipy.special.ynp_zeros.html#scipy.special.ynp_zeros "scipy.special.ynp_zeros")(n,Â nt) | Compute zeros of integer-order Bessel function derivatives Yn'(x). |
| [`y0_zeros`](generated/scipy.special.y0_zeros.html#scipy.special.y0_zeros "scipy.special.y0_zeros")(nt[,Â complex]) | Compute nt zeros of Bessel function Y0(z), and derivative at each zero. |
| [`y1_zeros`](generated/scipy.special.y1_zeros.html#scipy.special.y1_zeros "scipy.special.y1_zeros")(nt[,Â complex]) | Compute nt zeros of Bessel function Y1(z), and derivative at each zero. |
| [`y1p_zeros`](generated/scipy.special.y1p_zeros.html#scipy.special.y1p_zeros "scipy.special.y1p_zeros")(nt[,Â complex]) | Compute nt zeros of Bessel derivative Y1'(z), and value at each zero. |
#### Faster versions of common Bessel functions[#](#faster-versions-of-common-bessel-functions "Link to this heading")
|  |  |
| --- | --- |
| [`j0`](generated/scipy.special.j0.html#scipy.special.j0 "scipy.special.j0")(x[,Â out]) | Bessel function of the first kind of order 0. |
| [`j1`](generated/scipy.special.j1.html#scipy.special.j1 "scipy.special.j1")(x[,Â out]) | Bessel function of the first kind of order 1. |
| [`y0`](generated/scipy.special.y0.html#scipy.special.y0 "scipy.special.y0")(x[,Â out]) | Bessel function of the second kind of order 0. |
| [`y1`](generated/scipy.special.y1.html#scipy.special.y1 "scipy.special.y1")(x[,Â out]) | Bessel function of the second kind of order 1. |
| [`i0`](generated/scipy.special.i0.html#scipy.special.i0 "scipy.special.i0")(x[,Â out]) | Modified Bessel function of order 0. |
| [`i0e`](generated/scipy.special.i0e.html#scipy.special.i0e "scipy.special.i0e")(x[,Â out]) | Exponentially scaled modified Bessel function of order 0. |
| [`i1`](generated/scipy.special.i1.html#scipy.special.i1 "scipy.special.i1")(x[,Â out]) | Modified Bessel function of order 1. |
| [`i1e`](generated/scipy.special.i1e.html#scipy.special.i1e "scipy.special.i1e")(x[,Â out]) | Exponentially scaled modified Bessel function of order 1. |
| [`k0`](generated/scipy.special.k0.html#scipy.special.k0 "scipy.special.k0")(x[,Â out]) | Modified Bessel function of the second kind of order 0, \(K\_0\). |
| [`k0e`](generated/scipy.special.k0e.html#scipy.special.k0e "scipy.special.k0e")(x[,Â out]) | Exponentially scaled modified Bessel function K of order 0. |
| [`k1`](generated/scipy.special.k1.html#scipy.special.k1 "scipy.special.k1")(x[,Â out]) | Modified Bessel function of the second kind of order 1, \(K\_1(x)\). |
| [`k1e`](generated/scipy.special.k1e.html#scipy.special.k1e "scipy.special.k1e")(x[,Â out]) | Exponentially scaled modified Bessel function K of order 1. |
#### Integrals of Bessel functions[#](#integrals-of-bessel-functions "Link to this heading")
|  |  |
| --- | --- |
| [`itj0y0`](generated/scipy.special.itj0y0.html#scipy.special.itj0y0 "scipy.special.itj0y0")(x[,Â out]) | Integrals of Bessel functions of the first kind of order 0. |
| [`it2j0y0`](generated/scipy.special.it2j0y0.html#scipy.special.it2j0y0 "scipy.special.it2j0y0")(x[,Â out]) | Integrals related to Bessel functions of the first kind of order 0. |
| [`iti0k0`](generated/scipy.special.iti0k0.html#scipy.special.iti0k0 "scipy.special.iti0k0")(x[,Â out]) | Integrals of modified Bessel functions of order 0. |
| [`it2i0k0`](generated/scipy.special.it2i0k0.html#scipy.special.it2i0k0 "scipy.special.it2i0k0")(x[,Â out]) | Integrals related to modified Bessel functions of order 0. |
| [`besselpoly`](generated/scipy.special.besselpoly.html#scipy.special.besselpoly "scipy.special.besselpoly")(a,Â lmb,Â nu[,Â out]) | Weighted integral of the Bessel function of the first kind. |
#### Derivatives of Bessel functions[#](#derivatives-of-bessel-functions "Link to this heading")
|  |  |
| --- | --- |
| [`jvp`](generated/scipy.special.jvp.html#scipy.special.jvp "scipy.special.jvp")(v,Â z[,Â n]) | Compute derivatives of Bessel functions of the first kind. |
| [`yvp`](generated/scipy.special.yvp.html#scipy.special.yvp "scipy.special.yvp")(v,Â z[,Â n]) | Compute derivatives of Bessel functions of the second kind. |
| [`ivp`](generated/scipy.special.ivp.html#scipy.special.ivp "scipy.special.ivp")(v,Â z[,Â n]) | Compute derivatives of modified Bessel functions of the first kind. |
| [`kvp`](generated/scipy.special.kvp.html#scipy.special.kvp "scipy.special.kvp")(v,Â z[,Â n]) | Compute derivatives of real-order modified Bessel function Kv(z). |
| [`h1vp`](generated/scipy.special.h1vp.html#scipy.special.h1vp "scipy.special.h1vp")(v,Â z[,Â n]) | Compute derivatives of Hankel function H1v(z) with respect to *z*. |
| [`h2vp`](generated/scipy.special.h2vp.html#scipy.special.h2vp "scipy.special.h2vp")(v,Â z[,Â n]) | Compute derivatives of Hankel function H2v(z) with respect to *z*. |
#### Spherical Bessel functions[#](#spherical-bessel-functions "Link to this heading")
|  |  |
| --- | --- |
| [`spherical_jn`](generated/scipy.special.spherical_jn.html#scipy.special.spherical_jn "scipy.special.spherical_jn")(n,Â z[,Â derivative]) | Spherical Bessel function of the first kind or its derivative. |
| [`spherical_yn`](generated/scipy.special.spherical_yn.html#scipy.special.spherical_yn "scipy.special.spherical_yn")(n,Â z[,Â derivative]) | Spherical Bessel function of the second kind or its derivative. |
| [`spherical_in`](generated/scipy.special.spherical_in.html#scipy.special.spherical_in "scipy.special.spherical_in")(n,Â z[,Â derivative]) | Modified spherical Bessel function of the first kind or its derivative. |
| [`spherical_kn`](generated/scipy.special.spherical_kn.html#scipy.special.spherical_kn "scipy.special.spherical_kn")(n,Â z[,Â derivative]) | Modified spherical Bessel function of the second kind or its derivative. |
#### Riccati-Bessel functions[#](#riccati-bessel-functions "Link to this heading")
The following functions do not accept NumPy arrays (they are not
universal functions):
|  |  |
| --- | --- |
| [`riccati_jn`](generated/scipy.special.riccati_jn.html#scipy.special.riccati_jn "scipy.special.riccati_jn")(n,Â x) | Compute Riccati-Bessel function of the first kind and its derivative. |
| [`riccati_yn`](generated/scipy.special.riccati_yn.html#scipy.special.riccati_yn "scipy.special.riccati_yn")(n,Â x) | Compute Riccati-Bessel function of the second kind and its derivative. |
### Struve functions[#](#struve-functions "Link to this heading")
|  |  |
| --- | --- |
| [`struve`](generated/scipy.special.struve.html#scipy.special.struve "scipy.special.struve")(v,Â x[,Â out]) | Struve function. |
| [`modstruve`](generated/scipy.special.modstruve.html#scipy.special.modstruve "scipy.special.modstruve")(v,Â x[,Â out]) | Modified Struve function. |
| [`itstruve0`](generated/scipy.special.itstruve0.html#scipy.special.itstruve0 "scipy.special.itstruve0")(x[,Â out]) | Integral of the Struve function of order 0. |
| [`it2struve0`](generated/scipy.special.it2struve0.html#scipy.special.it2struve0 "scipy.special.it2struve0")(x[,Â out]) | Integral related to the Struve function of order 0. |
| [`itmodstruve0`](generated/scipy.special.itmodstruve0.html#scipy.special.itmodstruve0 "scipy.special.itmodstruve0")(x[,Â out]) | Integral of the modified Struve function of order 0. |
### Raw statistical functions[#](#raw-statistical-functions "Link to this heading")
See also
[`scipy.stats`](stats.html#module-scipy.stats "scipy.stats"): Friendly versions of these functions.
#### Binomial distribution[#](#binomial-distribution "Link to this heading")
|  |  |
| --- | --- |
| [`bdtr`](generated/scipy.special.bdtr.html#scipy.special.bdtr "scipy.special.bdtr")(k,Â n,Â p[,Â out]) | Binomial distribution cumulative distribution function. |
| [`bdtrc`](generated/scipy.special.bdtrc.html#scipy.special.bdtrc "scipy.special.bdtrc")(k,Â n,Â p[,Â out]) | Binomial distribution survival function. |
| [`bdtri`](generated/scipy.special.bdtri.html#scipy.special.bdtri "scipy.special.bdtri")(k,Â n,Â y[,Â out]) | Inverse function to [`bdtr`](generated/scipy.special.bdtr.html#scipy.special.bdtr "scipy.special.bdtr") with respect to *p*. |
| [`bdtrik`](generated/scipy.special.bdtrik.html#scipy.special.bdtrik "scipy.special.bdtrik")(y,Â n,Â p[,Â out]) | Inverse function to [`bdtr`](generated/scipy.special.bdtr.html#scipy.special.bdtr "scipy.special.bdtr") with respect to *k*. |
| [`bdtrin`](generated/scipy.special.bdtrin.html#scipy.special.bdtrin "scipy.special.bdtrin")(k,Â y,Â p[,Â out]) | Inverse function to [`bdtr`](generated/scipy.special.bdtr.html#scipy.special.bdtr "scipy.special.bdtr") with respect to *n*. |
#### Beta distribution[#](#beta-distribution "Link to this heading")
|  |  |
| --- | --- |
| [`btdtria`](generated/scipy.special.btdtria.html#scipy.special.btdtria "scipy.special.btdtria")(p,Â b,Â x[,Â out]) | Inverse of [`betainc`](generated/scipy.special.betainc.html#scipy.special.betainc "scipy.special.betainc") with respect to *a*. |
| [`btdtrib`](generated/scipy.special.btdtrib.html#scipy.special.btdtrib "scipy.special.btdtrib")(a,Â p,Â x[,Â out]) | Inverse of [`betainc`](generated/scipy.special.betainc.html#scipy.special.betainc "scipy.special.betainc") with respect to *b*. |
#### F distribution[#](#f-distribution "Link to this heading")
|  |  |
| --- | --- |
| [`fdtr`](generated/scipy.special.fdtr.html#scipy.special.fdtr "scipy.special.fdtr")(dfn,Â dfd,Â x[,Â out]) | F cumulative distribution function. |
| [`fdtrc`](generated/scipy.special.fdtrc.html#scipy.special.fdtrc "scipy.special.fdtrc")(dfn,Â dfd,Â x[,Â out]) | F survival function. |
| [`fdtri`](generated/scipy.special.fdtri.html#scipy.special.fdtri "scipy.special.fdtri")(dfn,Â dfd,Â p[,Â out]) | The *p*-th quantile of the F-distribution. |
| [`fdtridfd`](generated/scipy.special.fdtridfd.html#scipy.special.fdtridfd "scipy.special.fdtridfd")(dfn,Â p,Â x[,Â out]) | Inverse to [`fdtr`](generated/scipy.special.fdtr.html#scipy.special.fdtr "scipy.special.fdtr") vs dfd. |
#### Gamma distribution[#](#gamma-distribution "Link to this heading")
|  |  |
| --- | --- |
| [`gdtr`](generated/scipy.special.gdtr.html#scipy.special.gdtr "scipy.special.gdtr")(a,Â b,Â x[,Â out]) | Gamma distribution cumulative distribution function. |
| [`gdtrc`](generated/scipy.special.gdtrc.html#scipy.special.gdtrc "scipy.special.gdtrc")(a,Â b,Â x[,Â out]) | Gamma distribution survival function. |
| [`gdtria`](generated/scipy.special.gdtria.html#scipy.special.gdtria "scipy.special.gdtria")(p,Â b,Â x[,Â out]) | Inverse of [`gdtr`](generated/scipy.special.gdtr.html#scipy.special.gdtr "scipy.special.gdtr") vs a. |
| [`gdtrib`](generated/scipy.special.gdtrib.html#scipy.special.gdtrib "scipy.special.gdtrib")(a,Â p,Â x[,Â out]) | Inverse of [`gdtr`](generated/scipy.special.gdtr.html#scipy.special.gdtr "scipy.special.gdtr") vs b. |
| [`gdtrix`](generated/scipy.special.gdtrix.html#scipy.special.gdtrix "scipy.special.gdtrix")(a,Â b,Â p[,Â out]) | Inverse of [`gdtr`](generated/scipy.special.gdtr.html#scipy.special.gdtr "scipy.special.gdtr") vs x. |
#### Negative binomial distribution[#](#negative-binomial-distribution "Link to this heading")
|  |  |
| --- | --- |
| [`nbdtr`](generated/scipy.special.nbdtr.html#scipy.special.nbdtr "scipy.special.nbdtr")(k,Â n,Â p[,Â out]) | Negative binomial cumulative distribution function. |
| [`nbdtrc`](generated/scipy.special.nbdtrc.html#scipy.special.nbdtrc "scipy.special.nbdtrc")(k,Â n,Â p[,Â out]) | Negative binomial survival function. |
| [`nbdtri`](generated/scipy.special.nbdtri.html#scipy.special.nbdtri "scipy.special.nbdtri")(k,Â n,Â y[,Â out]) | Returns the inverse with respect to the parameter *p* of `y = nbdtr(k, n, p)`, the negative binomial cumulative distribution function. |
| [`nbdtrik`](generated/scipy.special.nbdtrik.html#scipy.special.nbdtrik "scipy.special.nbdtrik")(y,Â n,Â p[,Â out]) | Negative binomial percentile function. |
| [`nbdtrin`](generated/scipy.special.nbdtrin.html#scipy.special.nbdtrin "scipy.special.nbdtrin")(k,Â y,Â p[,Â out]) | Inverse of [`nbdtr`](generated/scipy.special.nbdtr.html#scipy.special.nbdtr "scipy.special.nbdtr") vs *n*. |
#### Noncentral F distribution[#](#noncentral-f-distribution "Link to this heading")
|  |  |
| --- | --- |
| [`ncfdtr`](generated/scipy.special.ncfdtr.html#scipy.special.ncfdtr "scipy.special.ncfdtr")(dfn,Â dfd,Â nc,Â f[,Â out]) | Cumulative distribution function of the non-central F distribution. |
| [`ncfdtridfd`](generated/scipy.special.ncfdtridfd.html#scipy.special.ncfdtridfd "scipy.special.ncfdtridfd")(dfn,Â p,Â nc,Â f[,Â out]) | Calculate degrees of freedom (denominator) for the noncentral F-distribution. |
| [`ncfdtridfn`](generated/scipy.special.ncfdtridfn.html#scipy.special.ncfdtridfn "scipy.special.ncfdtridfn")(p,Â dfd,Â nc,Â f[,Â out]) | Calculate degrees of freedom (numerator) for the noncentral F-distribution. |
| [`ncfdtri`](generated/scipy.special.ncfdtri.html#scipy.special.ncfdtri "scipy.special.ncfdtri")(dfn,Â dfd,Â nc,Â p[,Â out]) | Inverse with respect to *f* of the CDF of the non-central F distribution. |
| [`ncfdtrinc`](generated/scipy.special.ncfdtrinc.html#scipy.special.ncfdtrinc "scipy.special.ncfdtrinc")(dfn,Â dfd,Â p,Â f[,Â out]) | Calculate non-centrality parameter for non-central F distribution. |
#### Noncentral t distribution[#](#noncentral-t-distribution "Link to this heading")
|  |  |
| --- | --- |
| [`nctdtr`](generated/scipy.special.nctdtr.html#scipy.special.nctdtr "scipy.special.nctdtr")(df,Â nc,Â t[,Â out]) | Cumulative distribution function of the non-central *t* distribution. |
| [`nctdtridf`](generated/scipy.special.nctdtridf.html#scipy.special.nctdtridf "scipy.special.nctdtridf")(p,Â nc,Â t[,Â out]) | Calculate degrees of freedom for non-central t distribution. |
| [`nctdtrit`](generated/scipy.special.nctdtrit.html#scipy.special.nctdtrit "scipy.special.nctdtrit")(df,Â nc,Â p[,Â out]) | Inverse cumulative distribution function of the non-central t distribution. |
| [`nctdtrinc`](generated/scipy.special.nctdtrinc.html#scipy.special.nctdtrinc "scipy.special.nctdtrinc")(df,Â p,Â t[,Â out]) | Calculate non-centrality parameter for non-central t distribution. |
#### Normal distribution[#](#normal-distribution "Link to this heading")
|  |  |
| --- | --- |
| [`nrdtrimn`](generated/scipy.special.nrdtrimn.html#scipy.special.nrdtrimn "scipy.special.nrdtrimn")(p,Â std,Â x[,Â out]) | Calculate mean of normal distribution given other params. |
| [`nrdtrisd`](generated/scipy.special.nrdtrisd.html#scipy.special.nrdtrisd "scipy.special.nrdtrisd")(mn,Â p,Â x[,Â out]) | Calculate standard deviation of normal distribution given other params. |
| [`ndtr`](generated/scipy.special.ndtr.html#scipy.special.ndtr "scipy.special.ndtr")(x[,Â out]) | Cumulative distribution of the standard normal distribution. |
| [`log_ndtr`](generated/scipy.special.log_ndtr.html#scipy.special.log_ndtr "scipy.special.log_ndtr")(x[,Â out]) | Logarithm of Gaussian cumulative distribution function. |
| [`ndtri`](generated/scipy.special.ndtri.html#scipy.special.ndtri "scipy.special.ndtri")(p[,Â out]) | Inverse of [`ndtr`](generated/scipy.special.ndtr.html#scipy.special.ndtr "scipy.special.ndtr"). |
| [`ndtri_exp`](generated/scipy.special.ndtri_exp.html#scipy.special.ndtri_exp "scipy.special.ndtri_exp")(y[,Â out]) | Inverse of [`log_ndtr`](generated/scipy.special.log_ndtr.html#scipy.special.log_ndtr "scipy.special.log_ndtr") vs x. |
#### Poisson distribution[#](#poisson-distribution "Link to this heading")
|  |  |
| --- | --- |
| [`pdtr`](generated/scipy.special.pdtr.html#scipy.special.pdtr "scipy.special.pdtr")(k,Â m[,Â out]) | Poisson cumulative distribution function. |
| [`pdtrc`](generated/scipy.special.pdtrc.html#scipy.special.pdtrc "scipy.special.pdtrc")(k,Â m[,Â out]) | Poisson survival function. |
| [`pdtri`](generated/scipy.special.pdtri.html#scipy.special.pdtri "scipy.special.pdtri")(k,Â y[,Â out]) | Inverse of [`pdtr`](generated/scipy.special.pdtr.html#scipy.special.pdtr "scipy.special.pdtr") with respect to *m*. |
| [`pdtrik`](generated/scipy.special.pdtrik.html#scipy.special.pdtrik "scipy.special.pdtrik")(p,Â m[,Â out]) | Inverse of [`pdtr`](generated/scipy.special.pdtr.html#scipy.special.pdtr "scipy.special.pdtr") with respect to *k*. |
#### Student t distribution[#](#student-t-distribution "Link to this heading")
|  |  |
| --- | --- |
| [`stdtr`](generated/scipy.special.stdtr.html#scipy.special.stdtr "scipy.special.stdtr")(df,Â t[,Â out]) | Student t distribution cumulative distribution function. |
| [`stdtridf`](generated/scipy.special.stdtridf.html#scipy.special.stdtridf "scipy.special.stdtridf")(p,Â t[,Â out]) | Inverse of [`stdtr`](generated/scipy.special.stdtr.html#scipy.special.stdtr "scipy.special.stdtr") vs df. |
| [`stdtrit`](generated/scipy.special.stdtrit.html#scipy.special.stdtrit "scipy.special.stdtrit")(df,Â p[,Â out]) | The *p*-th quantile of the student t distribution. |
#### Chi square distribution[#](#chi-square-distribution "Link to this heading")
|  |  |
| --- | --- |
| [`chdtr`](generated/scipy.special.chdtr.html#scipy.special.chdtr "scipy.special.chdtr")(v,Â x[,Â out]) | Chi square cumulative distribution function. |
| [`chdtrc`](generated/scipy.special.chdtrc.html#scipy.special.chdtrc "scipy.special.chdtrc")(v,Â x[,Â out]) | Chi square survival function. |
| [`chdtri`](generated/scipy.special.chdtri.html#scipy.special.chdtri "scipy.special.chdtri")(v,Â p[,Â out]) | Inverse to [`chdtrc`](generated/scipy.special.chdtrc.html#scipy.special.chdtrc "scipy.special.chdtrc") with respect to *x*. |
| [`chdtriv`](generated/scipy.special.chdtriv.html#scipy.special.chdtriv "scipy.special.chdtriv")(p,Â x[,Â out]) | Inverse to [`chdtr`](generated/scipy.special.chdtr.html#scipy.special.chdtr "scipy.special.chdtr") with respect to *v*. |
#### Non-central chi square distribution[#](#non-central-chi-square-distribution "Link to this heading")
|  |  |
| --- | --- |
| [`chndtr`](generated/scipy.special.chndtr.html#scipy.special.chndtr "scipy.special.chndtr")(x,Â df,Â nc[,Â out]) | Non-central chi-squared cumulative distribution function. |
| [`chndtridf`](generated/scipy.special.chndtridf.html#scipy.special.chndtridf "scipy.special.chndtridf")(x,Â p,Â nc[,Â out]) | Inverse to [`chndtr`](generated/scipy.special.chndtr.html#scipy.special.chndtr "scipy.special.chndtr") vs *df*. |
| [`chndtrinc`](generated/scipy.special.chndtrinc.html#scipy.special.chndtrinc "scipy.special.chndtrinc")(x,Â df,Â p[,Â out]) | Inverse of [`chndtr`](generated/scipy.special.chndtr.html#scipy.special.chndtr "scipy.special.chndtr") with respect to *nc*. |
| [`chndtrix`](generated/scipy.special.chndtrix.html#scipy.special.chndtrix "scipy.special.chndtrix")(p,Â df,Â nc[,Â out]) | Inverse to [`chndtr`](generated/scipy.special.chndtr.html#scipy.special.chndtr "scipy.special.chndtr") vs *x*. |
#### Kolmogorov distribution[#](#kolmogorov-distribution "Link to this heading")
|  |  |
| --- | --- |
| [`smirnov`](generated/scipy.special.smirnov.html#scipy.special.smirnov "scipy.special.smirnov")(n,Â d[,Â out]) | Kolmogorov-Smirnov complementary cumulative distribution function. |
| [`smirnovi`](generated/scipy.special.smirnovi.html#scipy.special.smirnovi "scipy.special.smirnovi")(n,Â p[,Â out]) | Inverse to [`smirnov`](generated/scipy.special.smirnov.html#scipy.special.smirnov "scipy.special.smirnov"). |
| [`kolmogorov`](generated/scipy.special.kolmogorov.html#scipy.special.kolmogorov "scipy.special.kolmogorov")(y[,Â out]) | Complementary cumulative distribution (Survival Function) function of Kolmogorov distribution. |
| [`kolmogi`](generated/scipy.special.kolmogi.html#scipy.special.kolmogi "scipy.special.kolmogi")(p[,Â out]) | Inverse Survival Function of Kolmogorov distribution. |
#### Box-Cox transformation[#](#box-cox-transformation "Link to this heading")
|  |  |
| --- | --- |
| [`boxcox`](generated/scipy.special.boxcox.html#scipy.special.boxcox "scipy.special.boxcox")(x,Â lmbda[,Â out]) | Compute the Box-Cox transformation. |
| [`boxcox1p`](generated/scipy.special.boxcox1p.html#scipy.special.boxcox1p "scipy.special.boxcox1p")(x,Â lmbda[,Â out]) | Compute the Box-Cox transformation of \(1 + x\). |
| [`inv_boxcox`](generated/scipy.special.inv_boxcox.html#scipy.special.inv_boxcox "scipy.special.inv_boxcox")(y,Â lmbda[,Â out]) | Compute the inverse of the Box-Cox transformation. |
| [`inv_boxcox1p`](generated/scipy.special.inv_boxcox1p.html#scipy.special.inv_boxcox1p "scipy.special.inv_boxcox1p")(y,Â lmbda[,Â out]) | Compute the inverse of the Box-Cox transformation of \(1 + x\). |
#### Sigmoidal functions[#](#sigmoidal-functions "Link to this heading")
|  |  |
| --- | --- |
| [`logit`](generated/scipy.special.logit.html#scipy.special.logit "scipy.special.logit")(x[,Â out]) | Logit ufunc for ndarrays. |
| [`expit`](generated/scipy.special.expit.html#scipy.special.expit "scipy.special.expit")(x[,Â out]) | Expit (also known as logistic sigmoid) ufunc for ndarrays. |
| [`log_expit`](generated/scipy.special.log_expit.html#scipy.special.log_expit "scipy.special.log_expit")(x[,Â out]) | Logarithm of the logistic sigmoid function. |
#### Miscellaneous[#](#miscellaneous "Link to this heading")
|  |  |
| --- | --- |
| [`tklmbda`](generated/scipy.special.tklmbda.html#scipy.special.tklmbda "scipy.special.tklmbda")(x,Â lmbda[,Â out]) | Cumulative distribution function of the Tukey lambda distribution. |
| [`owens_t`](generated/scipy.special.owens_t.html#scipy.special.owens_t "scipy.special.owens_t")(h,Â a[,Â out]) | Owen's T Function. |
### Information Theory functions[#](#information-theory-functions "Link to this heading")
|  |  |
| --- | --- |
| [`entr`](generated/scipy.special.entr.html#scipy.special.entr "scipy.special.entr")(x[,Â out]) | Elementwise function for computing entropy. |
| [`rel_entr`](generated/scipy.special.rel_entr.html#scipy.special.rel_entr "scipy.special.rel_entr")(x,Â y[,Â out]) | Elementwise function for computing relative entropy. |
| [`kl_div`](generated/scipy.special.kl_div.html#scipy.special.kl_div "scipy.special.kl_div")(x,Â y[,Â out]) | Elementwise function for computing Kullback-Leibler divergence. |
| [`huber`](generated/scipy.special.huber.html#scipy.special.huber "scipy.special.huber")(delta,Â r[,Â out]) | Huber loss function. |
| [`pseudo_huber`](generated/scipy.special.pseudo_huber.html#scipy.special.pseudo_huber "scipy.special.pseudo_huber")(delta,Â r[,Â out]) | Pseudo-Huber loss function. |
### Gamma and related functions[#](#gamma-and-related-functions "Link to this heading")
|  |  |
| --- | --- |
| [`gamma`](generated/scipy.special.gamma.html#scipy.special.gamma "scipy.special.gamma")(z[,Â out]) | Compute the gamma function. |
| [`gammaln`](generated/scipy.special.gammaln.html#scipy.special.gammaln "scipy.special.gammaln")(x[,Â out]) | Logarithm of the absolute value of the gamma function. |
| [`loggamma`](generated/scipy.special.loggamma.html#scipy.special.loggamma "scipy.special.loggamma")(z[,Â out]) | Principal branch of the logarithm of the gamma function. |
| [`gammasgn`](generated/scipy.special.gammasgn.html#scipy.special.gammasgn "scipy.special.gammasgn")(x[,Â out]) | Sign of the gamma function. |
| [`gammainc`](generated/scipy.special.gammainc.html#scipy.special.gammainc "scipy.special.gammainc")(a,Â x[,Â out]) | Regularized lower incomplete gamma function. |
| [`gammaincinv`](generated/scipy.special.gammaincinv.html#scipy.special.gammaincinv "scipy.special.gammaincinv")(a,Â y[,Â out]) | Inverse to the regularized lower incomplete gamma function. |
| [`gammaincc`](generated/scipy.special.gammaincc.html#scipy.special.gammaincc "scipy.special.gammaincc")(a,Â x[,Â out]) | Regularized upper incomplete gamma function. |
| [`gammainccinv`](generated/scipy.special.gammainccinv.html#scipy.special.gammainccinv "scipy.special.gammainccinv")(a,Â y[,Â out]) | Inverse of the regularized upper incomplete gamma function. |
| [`beta`](generated/scipy.special.beta.html#scipy.special.beta "scipy.special.beta")(a,Â b[,Â out]) | Beta function. |
| [`betaln`](generated/scipy.special.betaln.html#scipy.special.betaln "scipy.special.betaln")(a,Â b[,Â out]) | Natural logarithm of absolute value of beta function. |
| [`betainc`](generated/scipy.special.betainc.html#scipy.special.betainc "scipy.special.betainc")(a,Â b,Â x[,Â out]) | Regularized incomplete beta function. |
| [`betaincc`](generated/scipy.special.betaincc.html#scipy.special.betaincc "scipy.special.betaincc")(a,Â b,Â x[,Â out]) | Complement of the regularized incomplete beta function. |
| [`betaincinv`](generated/scipy.special.betaincinv.html#scipy.special.betaincinv "scipy.special.betaincinv")(a,Â b,Â y[,Â out]) | Inverse of the regularized incomplete beta function. |
| [`betainccinv`](generated/scipy.special.betainccinv.html#scipy.special.betainccinv "scipy.special.betainccinv")(a,Â b,Â y[,Â out]) | Inverse of the complemented regularized incomplete beta function. |
| [`psi`](generated/scipy.special.psi.html#scipy.special.psi "scipy.special.psi")(z[,Â out]) | The digamma function. |
| [`rgamma`](generated/scipy.special.rgamma.html#scipy.special.rgamma "scipy.special.rgamma")(z[,Â out]) | Reciprocal of the gamma function. |
| [`polygamma`](generated/scipy.special.polygamma.html#scipy.special.polygamma "scipy.special.polygamma")(n,Â x) | Polygamma functions. |
| [`multigammaln`](generated/scipy.special.multigammaln.html#scipy.special.multigammaln "scipy.special.multigammaln")(a,Â d) | Returns the log of multivariate gamma, also sometimes called the generalized gamma. |
| [`digamma`](generated/scipy.special.digamma.html#scipy.special.digamma "scipy.special.digamma")(z[,Â out]) | The digamma function. |
| [`poch`](generated/scipy.special.poch.html#scipy.special.poch "scipy.special.poch")(z,Â m[,Â out]) | Pochhammer symbol. |
### Error function and Fresnel integrals[#](#error-function-and-fresnel-integrals "Link to this heading")
|  |  |
| --- | --- |
| [`erf`](generated/scipy.special.erf.html#scipy.special.erf "scipy.special.erf")(z[,Â out]) | Error function of real or complex argument. |
| [`erfc`](generated/scipy.special.erfc.html#scipy.special.erfc "scipy.special.erfc")(x[,Â out]) | Complementary error function. |
| [`erfcx`](generated/scipy.special.erfcx.html#scipy.special.erfcx "scipy.special.erfcx")(x[,Â out]) | Scaled complementary error function. |
| [`erfi`](generated/scipy.special.erfi.html#scipy.special.erfi "scipy.special.erfi")(z[,Â out]) | Imaginary error function. |
| [`erfinv`](generated/scipy.special.erfinv.html#scipy.special.erfinv "scipy.special.erfinv")(y[,Â out]) | Inverse of the error function. |
| [`erfcinv`](generated/scipy.special.erfcinv.html#scipy.special.erfcinv "scipy.special.erfcinv")(y[,Â out]) | Inverse of the complementary error function. |
| [`wofz`](generated/scipy.special.wofz.html#scipy.special.wofz "scipy.special.wofz")(z[,Â out]) | Faddeeva function. |
| [`dawsn`](generated/scipy.special.dawsn.html#scipy.special.dawsn "scipy.special.dawsn")(x[,Â out]) | Dawson's integral. |
| [`fresnel`](generated/scipy.special.fresnel.html#scipy.special.fresnel "scipy.special.fresnel")(z[,Â out]) | Fresnel integrals. |
| [`fresnel_zeros`](generated/scipy.special.fresnel_zeros.html#scipy.special.fresnel_zeros "scipy.special.fresnel_zeros")(nt) | Compute nt complex zeros of sine and cosine Fresnel integrals S(z) and C(z). |
| [`modfresnelp`](generated/scipy.special.modfresnelp.html#scipy.special.modfresnelp "scipy.special.modfresnelp")(x[,Â out]) | Modified Fresnel positive integrals. |
| [`modfresnelm`](generated/scipy.special.modfresnelm.html#scipy.special.modfresnelm "scipy.special.modfresnelm")(x[,Â out]) | Modified Fresnel negative integrals. |
| [`voigt_profile`](generated/scipy.special.voigt_profile.html#scipy.special.voigt_profile "scipy.special.voigt_profile")(x,Â sigma,Â gamma[,Â out]) | Voigt profile. |
The following functions do not accept NumPy arrays (they are not
universal functions):
|  |  |
| --- | --- |
| [`erf_zeros`](generated/scipy.special.erf_zeros.html#scipy.special.erf_zeros "scipy.special.erf_zeros")(nt) | Compute the first nt zero in the first quadrant, ordered by absolute value. |
| [`fresnelc_zeros`](generated/scipy.special.fresnelc_zeros.html#scipy.special.fresnelc_zeros "scipy.special.fresnelc_zeros")(nt) | Compute nt complex zeros of cosine Fresnel integral C(z). |
| [`fresnels_zeros`](generated/scipy.special.fresnels_zeros.html#scipy.special.fresnels_zeros "scipy.special.fresnels_zeros")(nt) | Compute nt complex zeros of sine Fresnel integral S(z). |
### Legendre functions[#](#legendre-functions "Link to this heading")
|  |  |
| --- | --- |
| [`legendre_p`](generated/scipy.special.legendre_p.html#scipy.special.legendre_p "scipy.special.legendre_p")(n,Â z,Â \*[,Â diff\_n]) | Legendre polynomial of the first kind. |
| [`legendre_p_all`](generated/scipy.special.legendre_p_all.html#scipy.special.legendre_p_all "scipy.special.legendre_p_all")(n,Â z,Â \*[,Â diff\_n]) | All Legendre polynomials of the first kind up to the specified degree *n* and all derivatives up to order *diff\_n*. |
| [`assoc_legendre_p`](generated/scipy.special.assoc_legendre_p.html#scipy.special.assoc_legendre_p "scipy.special.assoc_legendre_p")(n,Â m,Â z,Â \*[,Â branch\_cut,Â ...]) | Associated Legendre polynomial of the first kind. |
| [`assoc_legendre_p_all`](generated/scipy.special.assoc_legendre_p_all.html#scipy.special.assoc_legendre_p_all "scipy.special.assoc_legendre_p_all")(n,Â m,Â z,Â \*[,Â ...]) | All associated Legendre polynomials of the first kind up to the specified degree *n*, order *m*, and all derivatives up to order *diff\_n*. |
| [`sph_legendre_p`](generated/scipy.special.sph_legendre_p.html#scipy.special.sph_legendre_p "scipy.special.sph_legendre_p")(n,Â m,Â theta,Â \*[,Â diff\_n]) | Spherical Legendre polynomial of the first kind. |
| [`sph_legendre_p_all`](generated/scipy.special.sph_legendre_p_all.html#scipy.special.sph_legendre_p_all "scipy.special.sph_legendre_p_all")(n,Â m,Â theta,Â \*[,Â diff\_n]) | All spherical Legendre polynomials of the first kind up to the specified degree *n*, order *m*, and all derivatives up to order *diff\_n*. |
| [`sph_harm_y`](generated/scipy.special.sph_harm_y.html#scipy.special.sph_harm_y "scipy.special.sph_harm_y")(n,Â m,Â theta,Â phi,Â \*[,Â diff\_n]) | Spherical harmonics. |
| [`sph_harm_y_all`](generated/scipy.special.sph_harm_y_all.html#scipy.special.sph_harm_y_all "scipy.special.sph_harm_y_all")(n,Â m,Â theta,Â phi,Â \*[,Â diff\_n]) | All spherical harmonics up to the specified degree *n*, order *m*, and all derivatives up to order *diff\_n*. |
The following functions are in the process of being deprecated in favor of the above,
which provide a more flexible and consistent interface.
|  |  |
| --- | --- |
| [`lpmv`](generated/scipy.special.lpmv.html#scipy.special.lpmv "scipy.special.lpmv")(m,Â v,Â x[,Â out]) | Associated Legendre function of integer order and real degree. |
| [`lqn`](generated/scipy.special.lqn.html#scipy.special.lqn "scipy.special.lqn")(n,Â z) | Legendre functions of the second kind. |
| [`lqmn`](generated/scipy.special.lqmn.html#scipy.special.lqmn "scipy.special.lqmn")(m,Â n,Â z) | Sequence of associated Legendre functions of the second kind. |
### Ellipsoidal harmonics[#](#ellipsoidal-harmonics "Link to this heading")
|  |  |
| --- | --- |
| [`ellip_harm`](generated/scipy.special.ellip_harm.html#scipy.special.ellip_harm "scipy.special.ellip_harm")(h2,Â k2,Â n,Â p,Â s[,Â signm,Â signn]) | Ellipsoidal harmonic functions E^p\_n(l). |
| [`ellip_harm_2`](generated/scipy.special.ellip_harm_2.html#scipy.special.ellip_harm_2 "scipy.special.ellip_harm_2")(h2,Â k2,Â n,Â p,Â s) | Ellipsoidal harmonic functions F^p\_n(l). |
| [`ellip_normal`](generated/scipy.special.ellip_normal.html#scipy.special.ellip_normal "scipy.special.ellip_normal")(h2,Â k2,Â n,Â p) | Ellipsoidal harmonic normalization constants gamma^p\_n. |
### Orthogonal polynomials[#](#orthogonal-polynomials "Link to this heading")
The following functions evaluate values of orthogonal polynomials:
|  |  |
| --- | --- |
| [`assoc_laguerre`](generated/scipy.special.assoc_laguerre.html#scipy.special.assoc_laguerre "scipy.special.assoc_laguerre")(x,Â n[,Â k]) | Compute the generalized (associated) Laguerre polynomial of degree \(n\) and order \(k\). |
| [`eval_legendre`](generated/scipy.special.eval_legendre.html#scipy.special.eval_legendre "scipy.special.eval_legendre")(n,Â x[,Â out]) | Evaluate Legendre polynomial at a point. |
| [`eval_chebyt`](generated/scipy.special.eval_chebyt.html#scipy.special.eval_chebyt "scipy.special.eval_chebyt")(n,Â x[,Â out]) | Evaluate Chebyshev polynomial of the first kind at a point. |
| [`eval_chebyu`](generated/scipy.special.eval_chebyu.html#scipy.special.eval_chebyu "scipy.special.eval_chebyu")(n,Â x[,Â out]) | Evaluate Chebyshev polynomial of the second kind at a point. |
| [`eval_chebyc`](generated/scipy.special.eval_chebyc.html#scipy.special.eval_chebyc "scipy.special.eval_chebyc")(n,Â x[,Â out]) | Evaluate Chebyshev polynomial of the first kind on [-2, 2] at a point. |
| [`eval_chebys`](generated/scipy.special.eval_chebys.html#scipy.special.eval_chebys "scipy.special.eval_chebys")(n,Â x[,Â out]) | Evaluate Chebyshev polynomial of the second kind on [-2, 2] at a point. |
| [`eval_jacobi`](generated/scipy.special.eval_jacobi.html#scipy.special.eval_jacobi "scipy.special.eval_jacobi")(n,Â alpha,Â beta,Â x[,Â out]) | Evaluate Jacobi polynomial at a point. |
| [`eval_laguerre`](generated/scipy.special.eval_laguerre.html#scipy.special.eval_laguerre "scipy.special.eval_laguerre")(n,Â x[,Â out]) | Evaluate Laguerre polynomial at a point. |
| [`eval_genlaguerre`](generated/scipy.special.eval_genlaguerre.html#scipy.special.eval_genlaguerre "scipy.special.eval_genlaguerre")(n,Â alpha,Â x[,Â out]) | Evaluate generalized Laguerre polynomial at a point. |
| [`eval_hermite`](generated/scipy.special.eval_hermite.html#scipy.special.eval_hermite "scipy.special.eval_hermite")(n,Â x[,Â out]) | Evaluate physicist's Hermite polynomial at a point. |
| [`eval_hermitenorm`](generated/scipy.special.eval_hermitenorm.html#scipy.special.eval_hermitenorm "scipy.special.eval_hermitenorm")(n,Â x[,Â out]) | Evaluate probabilist's (normalized) Hermite polynomial at a point. |
| [`eval_gegenbauer`](generated/scipy.special.eval_gegenbauer.html#scipy.special.eval_gegenbauer "scipy.special.eval_gegenbauer")(n,Â alpha,Â x[,Â out]) | Evaluate Gegenbauer (ultraspherical) polynomial at a point. |
| [`eval_sh_legendre`](generated/scipy.special.eval_sh_legendre.html#scipy.special.eval_sh_legendre "scipy.special.eval_sh_legendre")(n,Â x[,Â out]) | Evaluate shifted Legendre polynomial at a point. |
| [`eval_sh_chebyt`](generated/scipy.special.eval_sh_chebyt.html#scipy.special.eval_sh_chebyt "scipy.special.eval_sh_chebyt")(n,Â x[,Â out]) | Evaluate shifted Chebyshev polynomial of the first kind at a point. |
| [`eval_sh_chebyu`](generated/scipy.special.eval_sh_chebyu.html#scipy.special.eval_sh_chebyu "scipy.special.eval_sh_chebyu")(n,Â x[,Â out]) | Evaluate shifted Chebyshev polynomial of the second kind at a point. |
| [`eval_sh_jacobi`](generated/scipy.special.eval_sh_jacobi.html#scipy.special.eval_sh_jacobi "scipy.special.eval_sh_jacobi")(n,Â p,Â q,Â x[,Â out]) | Evaluate shifted Jacobi polynomial at a point. |
The following functions compute roots and quadrature weights for
orthogonal polynomials:
|  |  |
| --- | --- |
| [`roots_legendre`](generated/scipy.special.roots_legendre.html#scipy.special.roots_legendre "scipy.special.roots_legendre")(n[,Â mu]) | Gauss-Legendre quadrature. |
| [`roots_chebyt`](generated/scipy.special.roots_chebyt.html#scipy.special.roots_chebyt "scipy.special.roots_chebyt")(n[,Â mu]) | Gauss-Chebyshev (first kind) quadrature. |
| [`roots_chebyu`](generated/scipy.special.roots_chebyu.html#scipy.special.roots_chebyu "scipy.special.roots_chebyu")(n[,Â mu]) | Gauss-Chebyshev (second kind) quadrature. |
| [`roots_chebyc`](generated/scipy.special.roots_chebyc.html#scipy.special.roots_chebyc "scipy.special.roots_chebyc")(n[,Â mu]) | Gauss-Chebyshev (first kind) quadrature. |
| [`roots_chebys`](generated/scipy.special.roots_chebys.html#scipy.special.roots_chebys "scipy.special.roots_chebys")(n[,Â mu]) | Gauss-Chebyshev (second kind) quadrature. |
| [`roots_jacobi`](generated/scipy.special.roots_jacobi.html#scipy.special.roots_jacobi "scipy.special.roots_jacobi")(n,Â alpha,Â beta[,Â mu]) | Gauss-Jacobi quadrature. |
| [`roots_laguerre`](generated/scipy.special.roots_laguerre.html#scipy.special.roots_laguerre "scipy.special.roots_laguerre")(n[,Â mu]) | Gauss-Laguerre quadrature. |
| [`roots_genlaguerre`](generated/scipy.special.roots_genlaguerre.html#scipy.special.roots_genlaguerre "scipy.special.roots_genlaguerre")(n,Â alpha[,Â mu]) | Gauss-generalized Laguerre quadrature. |
| [`roots_hermite`](generated/scipy.special.roots_hermite.html#scipy.special.roots_hermite "scipy.special.roots_hermite")(n[,Â mu]) | Gauss-Hermite (physicist's) quadrature. |
| [`roots_hermitenorm`](generated/scipy.special.roots_hermitenorm.html#scipy.special.roots_hermitenorm "scipy.special.roots_hermitenorm")(n[,Â mu]) | Gauss-Hermite (statistician's) quadrature. |
| [`roots_gegenbauer`](generated/scipy.special.roots_gegenbauer.html#scipy.special.roots_gegenbauer "scipy.special.roots_gegenbauer")(n,Â alpha[,Â mu]) | Gauss-Gegenbauer quadrature. |
| [`roots_sh_legendre`](generated/scipy.special.roots_sh_legendre.html#scipy.special.roots_sh_legendre "scipy.special.roots_sh_legendre")(n[,Â mu]) | Gauss-Legendre (shifted) quadrature. |
| [`roots_sh_chebyt`](generated/scipy.special.roots_sh_chebyt.html#scipy.special.roots_sh_chebyt "scipy.special.roots_sh_chebyt")(n[,Â mu]) | Gauss-Chebyshev (first kind, shifted) quadrature. |
| [`roots_sh_chebyu`](generated/scipy.special.roots_sh_chebyu.html#scipy.special.roots_sh_chebyu "scipy.special.roots_sh_chebyu")(n[,Â mu]) | Gauss-Chebyshev (second kind, shifted) quadrature. |
| [`roots_sh_jacobi`](generated/scipy.special.roots_sh_jacobi.html#scipy.special.roots_sh_jacobi "scipy.special.roots_sh_jacobi")(n,Â p1,Â q1[,Â mu]) | Gauss-Jacobi (shifted) quadrature. |
The functions below, in turn, return the polynomial coefficients in
`orthopoly1d` objects, which function similarly as [`numpy.poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "(in NumPy v2.4)").
The `orthopoly1d` class also has an attribute `weights`, which returns
the roots, weights, and total weights for the appropriate form of Gaussian
quadrature. These are returned in an `n x 3` array with roots in the first
column, weights in the second column, and total weights in the final column.
Note that `orthopoly1d` objects are converted to [`poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "(in NumPy v2.4)") when doing
arithmetic, and lose information of the original orthogonal polynomial.
|  |  |
| --- | --- |
| [`legendre`](generated/scipy.special.legendre.html#scipy.special.legendre "scipy.special.legendre")(n[,Â monic]) | Legendre polynomial. |
| [`chebyt`](generated/scipy.special.chebyt.html#scipy.special.chebyt "scipy.special.chebyt")(n[,Â monic]) | Chebyshev polynomial of the first kind. |
| [`chebyu`](generated/scipy.special.chebyu.html#scipy.special.chebyu "scipy.special.chebyu")(n[,Â monic]) | Chebyshev polynomial of the second kind. |
| [`chebyc`](generated/scipy.special.chebyc.html#scipy.special.chebyc "scipy.special.chebyc")(n[,Â monic]) | Chebyshev polynomial of the first kind on \([-2, 2]\). |
| [`chebys`](generated/scipy.special.chebys.html#scipy.special.chebys "scipy.special.chebys")(n[,Â monic]) | Chebyshev polynomial of the second kind on \([-2, 2]\). |
| [`jacobi`](generated/scipy.special.jacobi.html#scipy.special.jacobi "scipy.special.jacobi")(n,Â alpha,Â beta[,Â monic]) | Jacobi polynomial. |
| [`laguerre`](generated/scipy.special.laguerre.html#scipy.special.laguerre "scipy.special.laguerre")(n[,Â monic]) | Laguerre polynomial. |
| [`genlaguerre`](generated/scipy.special.genlaguerre.html#scipy.special.genlaguerre "scipy.special.genlaguerre")(n,Â alpha[,Â monic]) | Generalized (associated) Laguerre polynomial. |
| [`hermite`](generated/scipy.special.hermite.html#scipy.special.hermite "scipy.special.hermite")(n[,Â monic]) | Physicist's Hermite polynomial. |
| [`hermitenorm`](generated/scipy.special.hermitenorm.html#scipy.special.hermitenorm "scipy.special.hermitenorm")(n[,Â monic]) | Probabilist's Hermite polynomial. |
| [`gegenbauer`](generated/scipy.special.gegenbauer.html#scipy.special.gegenbauer "scipy.special.gegenbauer")(n,Â alpha[,Â monic]) | Gegenbauer (ultraspherical) polynomial. |
| [`sh_legendre`](generated/scipy.special.sh_legendre.html#scipy.special.sh_legendre "scipy.special.sh_legendre")(n[,Â monic]) | Shifted Legendre polynomial. |
| [`sh_chebyt`](generated/scipy.special.sh_chebyt.html#scipy.special.sh_chebyt "scipy.special.sh_chebyt")(n[,Â monic]) | Shifted Chebyshev polynomial of the first kind. |
| [`sh_chebyu`](generated/scipy.special.sh_chebyu.html#scipy.special.sh_chebyu "scipy.special.sh_chebyu")(n[,Â monic]) | Shifted Chebyshev polynomial of the second kind. |
| [`sh_jacobi`](generated/scipy.special.sh_jacobi.html#scipy.special.sh_jacobi "scipy.special.sh_jacobi")(n,Â p,Â q[,Â monic]) | Shifted Jacobi polynomial. |
Warning
Computing values of high-order polynomials (around `order > 20`) using
polynomial coefficients is numerically unstable. To evaluate polynomial
values, the `eval_*` functions should be used instead.
### Hypergeometric functions[#](#hypergeometric-functions "Link to this heading")
|  |  |
| --- | --- |
| [`hyp2f1`](generated/scipy.special.hyp2f1.html#scipy.special.hyp2f1 "scipy.special.hyp2f1")(a,Â b,Â c,Â z[,Â out]) | Gauss hypergeometric function 2F1(a, b; c; z). |
| [`hyp1f1`](generated/scipy.special.hyp1f1.html#scipy.special.hyp1f1 "scipy.special.hyp1f1")(a,Â b,Â x[,Â out]) | Confluent hypergeometric function 1F1. |
| [`hyperu`](generated/scipy.special.hyperu.html#scipy.special.hyperu "scipy.special.hyperu")(a,Â b,Â x[,Â out]) | Confluent hypergeometric function U. |
| [`hyp0f1`](generated/scipy.special.hyp0f1.html#scipy.special.hyp0f1 "scipy.special.hyp0f1")(v,Â z[,Â out]) | Confluent hypergeometric limit function 0F1. |
### Parabolic cylinder functions[#](#parabolic-cylinder-functions "Link to this heading")
|  |  |
| --- | --- |
| [`pbdv`](generated/scipy.special.pbdv.html#scipy.special.pbdv "scipy.special.pbdv")(v,Â x[,Â out]) | Parabolic cylinder function D. |
| [`pbvv`](generated/scipy.special.pbvv.html#scipy.special.pbvv "scipy.special.pbvv")(v,Â x[,Â out]) | Parabolic cylinder function V. |
| [`pbwa`](generated/scipy.special.pbwa.html#scipy.special.pbwa "scipy.special.pbwa")(a,Â x[,Â out]) | Parabolic cylinder function W. |
The following functions do not accept NumPy arrays (they are not
universal functions):
|  |  |
| --- | --- |
| [`pbdv_seq`](generated/scipy.special.pbdv_seq.html#scipy.special.pbdv_seq "scipy.special.pbdv_seq")(v,Â x) | Parabolic cylinder functions Dv(x) and derivatives. |
| [`pbvv_seq`](generated/scipy.special.pbvv_seq.html#scipy.special.pbvv_seq "scipy.special.pbvv_seq")(v,Â x) | Parabolic cylinder functions Vv(x) and derivatives. |
| [`pbdn_seq`](generated/scipy.special.pbdn_seq.html#scipy.special.pbdn_seq "scipy.special.pbdn_seq")(n,Â z) | Parabolic cylinder functions Dn(z) and derivatives. |
### Mathieu and related functions[#](#mathieu-and-related-functions "Link to this heading")
|  |  |
| --- | --- |
| [`mathieu_a`](generated/scipy.special.mathieu_a.html#scipy.special.mathieu_a "scipy.special.mathieu_a")(m,Â q[,Â out]) | Characteristic value of even Mathieu functions. |
| [`mathieu_b`](generated/scipy.special.mathieu_b.html#scipy.special.mathieu_b "scipy.special.mathieu_b")(m,Â q[,Â out]) | Characteristic value of odd Mathieu functions. |
The following functions do not accept NumPy arrays (they are not
universal functions):
|  |  |
| --- | --- |
| [`mathieu_even_coef`](generated/scipy.special.mathieu_even_coef.html#scipy.special.mathieu_even_coef "scipy.special.mathieu_even_coef")(m,Â q) | Fourier coefficients for even Mathieu and modified Mathieu functions. |
| [`mathieu_odd_coef`](generated/scipy.special.mathieu_odd_coef.html#scipy.special.mathieu_odd_coef "scipy.special.mathieu_odd_coef")(m,Â q) | Fourier coefficients for odd Mathieu and modified Mathieu functions. |
The following return both function and first derivative:
|  |  |
| --- | --- |
| [`mathieu_cem`](generated/scipy.special.mathieu_cem.html#scipy.special.mathieu_cem "scipy.special.mathieu_cem")(m,Â q,Â x[,Â out]) | Even Mathieu function and its derivative. |
| [`mathieu_sem`](generated/scipy.special.mathieu_sem.html#scipy.special.mathieu_sem "scipy.special.mathieu_sem")(m,Â q,Â x[,Â out]) | Odd Mathieu function and its derivative. |
| [`mathieu_modcem1`](generated/scipy.special.mathieu_modcem1.html#scipy.special.mathieu_modcem1 "scipy.special.mathieu_modcem1")(m,Â q,Â x[,Â out]) | Even modified Mathieu function of the first kind and its derivative. |
| [`mathieu_modcem2`](generated/scipy.special.mathieu_modcem2.html#scipy.special.mathieu_modcem2 "scipy.special.mathieu_modcem2")(m,Â q,Â x[,Â out]) | Even modified Mathieu function of the second kind and its derivative. |
| [`mathieu_modsem1`](generated/scipy.special.mathieu_modsem1.html#scipy.special.mathieu_modsem1 "scipy.special.mathieu_modsem1")(m,Â q,Â x[,Â out]) | Odd modified Mathieu function of the first kind and its derivative. |
| [`mathieu_modsem2`](generated/scipy.special.mathieu_modsem2.html#scipy.special.mathieu_modsem2 "scipy.special.mathieu_modsem2")(m,Â q,Â x[,Â out]) | Odd modified Mathieu function of the second kind and its derivative. |
### Spheroidal wave functions[#](#spheroidal-wave-functions "Link to this heading")
|  |  |
| --- | --- |
| [`pro_ang1`](generated/scipy.special.pro_ang1.html#scipy.special.pro_ang1 "scipy.special.pro_ang1")(m,Â n,Â c,Â x[,Â out]) | Prolate spheroidal angular function of the first kind and its derivative. |
| [`pro_rad1`](generated/scipy.special.pro_rad1.html#scipy.special.pro_rad1 "scipy.special.pro_rad1")(m,Â n,Â c,Â x[,Â out]) | Prolate spheroidal radial function of the first kind and its derivative. |
| [`pro_rad2`](generated/scipy.special.pro_rad2.html#scipy.special.pro_rad2 "scipy.special.pro_rad2")(m,Â n,Â c,Â x[,Â out]) | Prolate spheroidal radial function of the second kind and its derivative. |
| [`obl_ang1`](generated/scipy.special.obl_ang1.html#scipy.special.obl_ang1 "scipy.special.obl_ang1")(m,Â n,Â c,Â x[,Â out]) | Oblate spheroidal angular function of the first kind and its derivative. |
| [`obl_rad1`](generated/scipy.special.obl_rad1.html#scipy.special.obl_rad1 "scipy.special.obl_rad1")(m,Â n,Â c,Â x[,Â out]) | Oblate spheroidal radial function of the first kind and its derivative. |
| [`obl_rad2`](generated/scipy.special.obl_rad2.html#scipy.special.obl_rad2 "scipy.special.obl_rad2")(m,Â n,Â c,Â x[,Â out]) | Oblate spheroidal radial function of the second kind and its derivative. |
| [`pro_cv`](generated/scipy.special.pro_cv.html#scipy.special.pro_cv "scipy.special.pro_cv")(m,Â n,Â c[,Â out]) | Characteristic value of prolate spheroidal function. |
| [`obl_cv`](generated/scipy.special.obl_cv.html#scipy.special.obl_cv "scipy.special.obl_cv")(m,Â n,Â c[,Â out]) | Characteristic value of oblate spheroidal function. |
| [`pro_cv_seq`](generated/scipy.special.pro_cv_seq.html#scipy.special.pro_cv_seq "scipy.special.pro_cv_seq")(m,Â n,Â c) | Characteristic values for prolate spheroidal wave functions. |
| [`obl_cv_seq`](generated/scipy.special.obl_cv_seq.html#scipy.special.obl_cv_seq "scipy.special.obl_cv_seq")(m,Â n,Â c) | Characteristic values for oblate spheroidal wave functions. |
The following functions require pre-computed characteristic value:
|  |  |
| --- | --- |
| [`pro_ang1_cv`](generated/scipy.special.pro_ang1_cv.html#scipy.special.pro_ang1_cv "scipy.special.pro_ang1_cv")(m,Â n,Â c,Â cv,Â x[,Â out]) | Prolate spheroidal angular function pro\_ang1 for precomputed characteristic value. |
| [`pro_rad1_cv`](generated/scipy.special.pro_rad1_cv.html#scipy.special.pro_rad1_cv "scipy.special.pro_rad1_cv")(m,Â n,Â c,Â cv,Â x[,Â out]) | Prolate spheroidal radial function pro\_rad1 for precomputed characteristic value. |
| [`pro_rad2_cv`](generated/scipy.special.pro_rad2_cv.html#scipy.special.pro_rad2_cv "scipy.special.pro_rad2_cv")(m,Â n,Â c,Â cv,Â x[,Â out]) | Prolate spheroidal radial function pro\_rad2 for precomputed characteristic value. |
| [`obl_ang1_cv`](generated/scipy.special.obl_ang1_cv.html#scipy.special.obl_ang1_cv "scipy.special.obl_ang1_cv")(m,Â n,Â c,Â cv,Â x[,Â out]) | Oblate spheroidal angular function obl\_ang1 for precomputed characteristic value. |
| [`obl_rad1_cv`](generated/scipy.special.obl_rad1_cv.html#scipy.special.obl_rad1_cv "scipy.special.obl_rad1_cv")(m,Â n,Â c,Â cv,Â x[,Â out]) | Oblate spheroidal radial function obl\_rad1 for precomputed characteristic value. |
| [`obl_rad2_cv`](generated/scipy.special.obl_rad2_cv.html#scipy.special.obl_rad2_cv "scipy.special.obl_rad2_cv")(m,Â n,Â c,Â cv,Â x[,Â out]) | Oblate spheroidal radial function obl\_rad2 for precomputed characteristic value. |
### Kelvin functions[#](#kelvin-functions "Link to this heading")
|  |  |
| --- | --- |
| [`kelvin`](generated/scipy.special.kelvin.html#scipy.special.kelvin "scipy.special.kelvin")(x[,Â out]) | Kelvin functions as complex numbers. |
| [`kelvin_zeros`](generated/scipy.special.kelvin_zeros.html#scipy.special.kelvin_zeros "scipy.special.kelvin_zeros")(nt) | Compute *nt* zeros of all Kelvin functions. |
| [`ber`](generated/scipy.special.ber.html#scipy.special.ber "scipy.special.ber")(x[,Â out]) | Kelvin function ber. |
| [`bei`](generated/scipy.special.bei.html#scipy.special.bei "scipy.special.bei")(x[,Â out]) | Kelvin function bei. |
| [`berp`](generated/scipy.special.berp.html#scipy.special.berp "scipy.special.berp")(x[,Â out]) | Derivative of the Kelvin function ber. |
| [`beip`](generated/scipy.special.beip.html#scipy.special.beip "scipy.special.beip")(x[,Â out]) | Derivative of the Kelvin function bei. |
| [`ker`](generated/scipy.special.ker.html#scipy.special.ker "scipy.special.ker")(x[,Â out]) | Kelvin function ker. |
| [`kei`](generated/scipy.special.kei.html#scipy.special.kei "scipy.special.kei")(x[,Â out]) | Kelvin function kei. |
| [`kerp`](generated/scipy.special.kerp.html#scipy.special.kerp "scipy.special.kerp")(x[,Â out]) | Derivative of the Kelvin function ker. |
| [`keip`](generated/scipy.special.keip.html#scipy.special.keip "scipy.special.keip")(x[,Â out]) | Derivative of the Kelvin function kei. |
The following functions do not accept NumPy arrays (they are not
universal functions):
|  |  |
| --- | --- |
| [`ber_zeros`](generated/scipy.special.ber_zeros.html#scipy.special.ber_zeros "scipy.special.ber_zeros")(nt) | Compute nt zeros of the Kelvin function ber. |
| [`bei_zeros`](generated/scipy.special.bei_zeros.html#scipy.special.bei_zeros "scipy.special.bei_zeros")(nt) | Compute nt zeros of the Kelvin function bei. |
| [`berp_zeros`](generated/scipy.special.berp_zeros.html#scipy.special.berp_zeros "scipy.special.berp_zeros")(nt) | Compute nt zeros of the derivative of the Kelvin function ber. |
| [`beip_zeros`](generated/scipy.special.beip_zeros.html#scipy.special.beip_zeros "scipy.special.beip_zeros")(nt) | Compute nt zeros of the derivative of the Kelvin function bei. |
| [`ker_zeros`](generated/scipy.special.ker_zeros.html#scipy.special.ker_zeros "scipy.special.ker_zeros")(nt) | Compute nt zeros of the Kelvin function ker. |
| [`kei_zeros`](generated/scipy.special.kei_zeros.html#scipy.special.kei_zeros "scipy.special.kei_zeros")(nt) | Compute nt zeros of the Kelvin function kei. |
| [`kerp_zeros`](generated/scipy.special.kerp_zeros.html#scipy.special.kerp_zeros "scipy.special.kerp_zeros")(nt) | Compute nt zeros of the derivative of the Kelvin function ker. |
| [`keip_zeros`](generated/scipy.special.keip_zeros.html#scipy.special.keip_zeros "scipy.special.keip_zeros")(nt) | Compute nt zeros of the derivative of the Kelvin function kei. |
### Combinatorics[#](#combinatorics "Link to this heading")
|  |  |
| --- | --- |
| [`comb`](generated/scipy.special.comb.html#scipy.special.comb "scipy.special.comb")(N,Â k,Â \*[,Â exact,Â repetition]) | The number of combinations of N things taken k at a time. |
| [`perm`](generated/scipy.special.perm.html#scipy.special.perm "scipy.special.perm")(N,Â k[,Â exact]) | Permutations of N things taken k at a time, i.e., k-permutations of N. |
| [`stirling2`](generated/scipy.special.stirling2.html#scipy.special.stirling2 "scipy.special.stirling2")(N,Â K,Â \*[,Â exact]) | Generate Stirling number(s) of the second kind. |
### Lambert W and related functions[#](#lambert-w-and-related-functions "Link to this heading")
|  |  |
| --- | --- |
| [`lambertw`](generated/scipy.special.lambertw.html#scipy.special.lambertw "scipy.special.lambertw")(z[,Â k,Â tol]) | Lambert W function. |
| [`wrightomega`](generated/scipy.special.wrightomega.html#scipy.special.wrightomega "scipy.special.wrightomega")(z[,Â out]) | Wright Omega function. |
### Other special functions[#](#other-special-functions "Link to this heading")
|  |  |
| --- | --- |
| [`agm`](generated/scipy.special.agm.html#scipy.special.agm "scipy.special.agm")(a,Â b[,Â out]) | Compute the arithmetic-geometric mean of *a* and *b*. |
| [`bernoulli`](generated/scipy.special.bernoulli.html#scipy.special.bernoulli "scipy.special.bernoulli")(n) | Bernoulli numbers B0..Bn (inclusive). |
| [`binom`](generated/scipy.special.binom.html#scipy.special.binom "scipy.special.binom")(x,Â y[,Â out]) | Binomial coefficient considered as a function of two real variables. |
| [`diric`](generated/scipy.special.diric.html#scipy.special.diric "scipy.special.diric")(x,Â n) | Periodic sinc function, also called the Dirichlet kernel. |
| [`euler`](generated/scipy.special.euler.html#scipy.special.euler "scipy.special.euler")(n) | Euler numbers E(0), E(1), ..., E(n). |
| [`expn`](generated/scipy.special.expn.html#scipy.special.expn "scipy.special.expn")(n,Â x[,Â out]) | Generalized exponential integral En. |
| [`exp1`](generated/scipy.special.exp1.html#scipy.special.exp1 "scipy.special.exp1")(z[,Â out]) | Exponential integral E1. |
| [`expi`](generated/scipy.special.expi.html#scipy.special.expi "scipy.special.expi")(x[,Â out]) | Exponential integral Ei. |
| [`factorial`](generated/scipy.special.factorial.html#scipy.special.factorial "scipy.special.factorial")(n[,Â exact,Â extend]) | The factorial of a number or array of numbers. |
| [`factorial2`](generated/scipy.special.factorial2.html#scipy.special.factorial2 "scipy.special.factorial2")(n[,Â exact,Â extend]) | Double factorial. |
| [`factorialk`](generated/scipy.special.factorialk.html#scipy.special.factorialk "scipy.special.factorialk")(n,Â k[,Â exact,Â extend]) | Multifactorial of n of order k, n(!!...!). |
| [`shichi`](generated/scipy.special.shichi.html#scipy.special.shichi "scipy.special.shichi")(x[,Â out]) | Hyperbolic sine and cosine integrals. |
| [`sici`](generated/scipy.special.sici.html#scipy.special.sici "scipy.special.sici")(x[,Â out]) | Sine and cosine integrals. |
| [`softmax`](generated/scipy.special.softmax.html#scipy.special.softmax "scipy.special.softmax")(x[,Â axis]) | Compute the softmax function. |
| [`log_softmax`](generated/scipy.special.log_softmax.html#scipy.special.log_softmax "scipy.special.log_softmax")(x[,Â axis]) | Compute the logarithm of the softmax function. |
| [`spence`](generated/scipy.special.spence.html#scipy.special.spence "scipy.special.spence")(z[,Â out]) | Spence's function, also known as the dilogarithm. |
| [`zeta`](generated/scipy.special.zeta.html#scipy.special.zeta "scipy.special.zeta")(x[,Â q,Â out]) | Riemann or Hurwitz zeta function. |
| [`zetac`](generated/scipy.special.zetac.html#scipy.special.zetac "scipy.special.zetac")(x[,Â out]) | Riemann zeta function minus 1. |
| [`softplus`](generated/scipy.special.softplus.html#scipy.special.softplus "scipy.special.softplus")(x,Â \*\*kwargs) | Compute the softplus function element-wise. |
### Convenience functions[#](#convenience-functions "Link to this heading")
|  |  |
| --- | --- |
| [`cbrt`](generated/scipy.special.cbrt.html#scipy.special.cbrt "scipy.special.cbrt")(x[,Â out]) | Element-wise cube root of *x*. |
| [`exp10`](generated/scipy.special.exp10.html#scipy.special.exp10 "scipy.special.exp10")(x[,Â out]) | Compute `10**x` element-wise. |
| [`exp2`](generated/scipy.special.exp2.html#scipy.special.exp2 "scipy.special.exp2")(x[,Â out]) | Compute `2**x` element-wise. |
| [`radian`](generated/scipy.special.radian.html#scipy.special.radian "scipy.special.radian")(d,Â m,Â s[,Â out]) | Convert from degrees to radians. |
| [`cosdg`](generated/scipy.special.cosdg.html#scipy.special.cosdg "scipy.special.cosdg")(x[,Â out]) | Cosine of the angle *x* given in degrees. |
| [`sindg`](generated/scipy.special.sindg.html#scipy.special.sindg "scipy.special.sindg")(x[,Â out]) | Sine of the angle *x* given in degrees. |
| [`tandg`](generated/scipy.special.tandg.html#scipy.special.tandg "scipy.special.tandg")(x[,Â out]) | Tangent of angle *x* given in degrees. |
| [`cotdg`](generated/scipy.special.cotdg.html#scipy.special.cotdg "scipy.special.cotdg")(x[,Â out]) | Cotangent of the angle *x* given in degrees. |
| [`log1p`](generated/scipy.special.log1p.html#scipy.special.log1p "scipy.special.log1p")(x[,Â out]) | Calculates log(1 + x) for use when *x* is near zero. |
| [`expm1`](generated/scipy.special.expm1.html#scipy.special.expm1 "scipy.special.expm1")(x[,Â out]) | Compute `exp(x) - 1`. |
| [`cosm1`](generated/scipy.special.cosm1.html#scipy.special.cosm1 "scipy.special.cosm1")(x[,Â out]) | Compute `cos(x) - 1`, especially when *x* is near zero. |
| [`powm1`](generated/scipy.special.powm1.html#scipy.special.powm1 "scipy.special.powm1")(x,Â y[,Â out]) | Computes `x**y - 1`. |
| [`round`](generated/scipy.special.round.html#scipy.special.round "scipy.special.round")(x[,Â out]) | Round to the nearest integer. |
| [`xlogy`](generated/scipy.special.xlogy.html#scipy.special.xlogy "scipy.special.xlogy")(x,Â y[,Â out]) | Compute `x*log(y)` so that the result is 0 if `x = 0`. |
| [`xlog1py`](generated/scipy.special.xlog1py.html#scipy.special.xlog1py "scipy.special.xlog1py")(x,Â y[,Â out]) | Compute `x*log1p(y)` so that the result is 0 if `x = 0`. |
| [`logsumexp`](generated/scipy.special.logsumexp.html#scipy.special.logsumexp "scipy.special.logsumexp")(a[,Â axis,Â b,Â keepdims,Â return\_sign]) | Compute the log of the sum of exponentials of input elements. |
| [`exprel`](generated/scipy.special.exprel.html#scipy.special.exprel "scipy.special.exprel")(x[,Â out]) | Relative error exponential, `(exp(x) - 1)/x`. |
| [`sinc`](generated/scipy.special.sinc.html#scipy.special.sinc "scipy.special.sinc")(x) | Return the normalized sinc function. |
[previous
scipy.spatial.QhullError](generated/scipy.spatial.QhullError.html "previous page")
[next
Cython API for special functions](special.cython_special.html "next page")
On this page
* [Error handling](#error-handling)
* [Available functions](#available-functions)
  + [Airy functions](#airy-functions)
  + [Elliptic functions and integrals](#elliptic-functions-and-integrals)
  + [Bessel functions](#bessel-functions)
    - [Zeros of Bessel functions](#zeros-of-bessel-functions)
    - [Faster versions of common Bessel functions](#faster-versions-of-common-bessel-functions)
    - [Integrals of Bessel functions](#integrals-of-bessel-functions)
    - [Derivatives of Bessel functions](#derivatives-of-bessel-functions)
    - [Spherical Bessel functions](#spherical-bessel-functions)
    - [Riccati-Bessel functions](#riccati-bessel-functions)
  + [Struve functions](#struve-functions)
  + [Raw statistical functions](#raw-statistical-functions)
    - [Binomial distribution](#binomial-distribution)
    - [Beta distribution](#beta-distribution)
    - [F distribution](#f-distribution)
    - [Gamma distribution](#gamma-distribution)
    - [Negative binomial distribution](#negative-binomial-distribution)
    - [Noncentral F distribution](#noncentral-f-distribution)
    - [Noncentral t distribution](#noncentral-t-distribution)
    - [Normal distribution](#normal-distribution)
    - [Poisson distribution](#poisson-distribution)
    - [Student t distribution](#student-t-distribution)
    - [Chi square distribution](#chi-square-distribution)
    - [Non-central chi square distribution](#non-central-chi-square-distribution)
    - [Kolmogorov distribution](#kolmogorov-distribution)
    - [Box-Cox transformation](#box-cox-transformation)
    - [Sigmoidal functions](#sigmoidal-functions)
    - [Miscellaneous](#miscellaneous)
  + [Information Theory functions](#information-theory-functions)
  + [Gamma and related functions](#gamma-and-related-functions)
  + [Error function and Fresnel integrals](#error-function-and-fresnel-integrals)
  + [Legendre functions](#legendre-functions)
  + [Ellipsoidal harmonics](#ellipsoidal-harmonics)
  + [Orthogonal polynomials](#orthogonal-polynomials)
  + [Hypergeometric functions](#hypergeometric-functions)
  + [Parabolic cylinder functions](#parabolic-cylinder-functions)
  + [Mathieu and related functions](#mathieu-and-related-functions)
  + [Spheroidal wave functions](#spheroidal-wave-functions)
  + [Kelvin functions](#kelvin-functions)
  + [Combinatorics](#combinatorics)
  + [Lambert W and related functions](#lambert-w-and-related-functions)
  + [Other special functions](#other-special-functions)
  + [Convenience functions](#convenience-functions)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/stats.html#module-scipy.stats -->
* [SciPy API](index.html)
* Statistical functions (`scipy.stats`)
# Statistical functions ([`scipy.stats`](#module-scipy.stats "scipy.stats"))[#](#statistical-functions-scipy-stats "Link to this heading")
This module contains a large number of probability distributions,
summary and frequency statistics, correlation functions and statistical
tests, masked statistics, kernel density estimation, quasi-Monte Carlo
functionality, and more.
Statistics is a very large area, and there are topics that are out of scope
for SciPy and are covered by other packages. Some of the most important ones
are:
* [statsmodels](https://www.statsmodels.org/stable/index.html):
  regression, linear models, time series analysis, extensions to topics
  also covered by `scipy.stats`.
* [Pandas](https://pandas.pydata.org/): tabular data, time series
  functionality, interfaces to other statistical languages.
* [PyMC](https://docs.pymc.io/): Bayesian statistical
  modeling, probabilistic machine learning.
* [scikit-learn](https://scikit-learn.org/): classification, regression,
  model selection.
* [Seaborn](https://seaborn.pydata.org/): statistical data visualization.
* [rpy2](https://rpy2.github.io/): Python to R bridge.
## Probability distributions[#](#probability-distributions "Link to this heading")
Each univariate distribution is an instance of a subclass of [`rv_continuous`](generated/scipy.stats.rv_continuous.html#scipy.stats.rv_continuous "scipy.stats.rv_continuous")
([`rv_discrete`](generated/scipy.stats.rv_discrete.html#scipy.stats.rv_discrete "scipy.stats.rv_discrete") for discrete distributions):
|  |  |
| --- | --- |
| [`rv_continuous`](generated/scipy.stats.rv_continuous.html#scipy.stats.rv_continuous "scipy.stats.rv_continuous")([momtype,Â a,Â b,Â xtol,Â ...]) | A generic continuous random variable class meant for subclassing. |
| [`rv_discrete`](generated/scipy.stats.rv_discrete.html#scipy.stats.rv_discrete "scipy.stats.rv_discrete")([a,Â b,Â name,Â badvalue,Â ...]) | A generic discrete random variable class meant for subclassing. |
| [`rv_histogram`](generated/scipy.stats.rv_histogram.html#scipy.stats.rv_histogram "scipy.stats.rv_histogram")(histogram,Â \*args[,Â density]) | Generates a distribution given by a histogram. |
### Continuous distributions[#](#continuous-distributions "Link to this heading")
|  |  |
| --- | --- |
| [`alpha`](generated/scipy.stats.alpha.html#scipy.stats.alpha "scipy.stats.alpha") | An alpha continuous random variable. |
| [`anglit`](generated/scipy.stats.anglit.html#scipy.stats.anglit "scipy.stats.anglit") | An anglit continuous random variable. |
| [`arcsine`](generated/scipy.stats.arcsine.html#scipy.stats.arcsine "scipy.stats.arcsine") | An arcsine continuous random variable. |
| [`argus`](generated/scipy.stats.argus.html#scipy.stats.argus "scipy.stats.argus") | Argus distribution. |
| [`beta`](generated/scipy.stats.beta.html#scipy.stats.beta "scipy.stats.beta") | A beta continuous random variable. |
| [`betaprime`](generated/scipy.stats.betaprime.html#scipy.stats.betaprime "scipy.stats.betaprime") | A beta prime continuous random variable. |
| [`bradford`](generated/scipy.stats.bradford.html#scipy.stats.bradford "scipy.stats.bradford") | A Bradford continuous random variable. |
| [`burr`](generated/scipy.stats.burr.html#scipy.stats.burr "scipy.stats.burr") | A Burr (Type III) continuous random variable. |
| [`burr12`](generated/scipy.stats.burr12.html#scipy.stats.burr12 "scipy.stats.burr12") | A Burr (Type XII) continuous random variable. |
| [`cauchy`](generated/scipy.stats.cauchy.html#scipy.stats.cauchy "scipy.stats.cauchy") | A Cauchy continuous random variable. |
| [`chi`](generated/scipy.stats.chi.html#scipy.stats.chi "scipy.stats.chi") | A chi continuous random variable. |
| [`chi2`](generated/scipy.stats.chi2.html#scipy.stats.chi2 "scipy.stats.chi2") | A chi-squared continuous random variable. |
| [`cosine`](generated/scipy.stats.cosine.html#scipy.stats.cosine "scipy.stats.cosine") | A cosine continuous random variable. |
| [`crystalball`](generated/scipy.stats.crystalball.html#scipy.stats.crystalball "scipy.stats.crystalball") | Crystalball distribution. |
| [`dgamma`](generated/scipy.stats.dgamma.html#scipy.stats.dgamma "scipy.stats.dgamma") | A double gamma continuous random variable. |
| [`dpareto_lognorm`](generated/scipy.stats.dpareto_lognorm.html#scipy.stats.dpareto_lognorm "scipy.stats.dpareto_lognorm") | A double Pareto lognormal continuous random variable. |
| [`dweibull`](generated/scipy.stats.dweibull.html#scipy.stats.dweibull "scipy.stats.dweibull") | A double Weibull continuous random variable. |
| [`erlang`](generated/scipy.stats.erlang.html#scipy.stats.erlang "scipy.stats.erlang") | An Erlang continuous random variable. |
| [`expon`](generated/scipy.stats.expon.html#scipy.stats.expon "scipy.stats.expon") | An exponential continuous random variable. |
| [`exponnorm`](generated/scipy.stats.exponnorm.html#scipy.stats.exponnorm "scipy.stats.exponnorm") | An exponentially modified Normal continuous random variable. |
| [`exponweib`](generated/scipy.stats.exponweib.html#scipy.stats.exponweib "scipy.stats.exponweib") | An exponentiated Weibull continuous random variable. |
| [`exponpow`](generated/scipy.stats.exponpow.html#scipy.stats.exponpow "scipy.stats.exponpow") | An exponential power continuous random variable. |
| [`f`](generated/scipy.stats.f.html#scipy.stats.f "scipy.stats.f") | An F continuous random variable. |
| [`fatiguelife`](generated/scipy.stats.fatiguelife.html#scipy.stats.fatiguelife "scipy.stats.fatiguelife") | A fatigue-life (Birnbaum-Saunders) continuous random variable. |
| [`fisk`](generated/scipy.stats.fisk.html#scipy.stats.fisk "scipy.stats.fisk") | A Fisk continuous random variable. |
| [`foldcauchy`](generated/scipy.stats.foldcauchy.html#scipy.stats.foldcauchy "scipy.stats.foldcauchy") | A folded Cauchy continuous random variable. |
| [`foldnorm`](generated/scipy.stats.foldnorm.html#scipy.stats.foldnorm "scipy.stats.foldnorm") | A folded normal continuous random variable. |
| [`genlogistic`](generated/scipy.stats.genlogistic.html#scipy.stats.genlogistic "scipy.stats.genlogistic") | A generalized logistic continuous random variable. |
| [`gennorm`](generated/scipy.stats.gennorm.html#scipy.stats.gennorm "scipy.stats.gennorm") | A (symmetric) generalized normal continuous random variable. |
| [`genpareto`](generated/scipy.stats.genpareto.html#scipy.stats.genpareto "scipy.stats.genpareto") | A generalized Pareto continuous random variable. |
| [`genexpon`](generated/scipy.stats.genexpon.html#scipy.stats.genexpon "scipy.stats.genexpon") | A generalized exponential continuous random variable. |
| [`genextreme`](generated/scipy.stats.genextreme.html#scipy.stats.genextreme "scipy.stats.genextreme") | A generalized extreme value continuous random variable. |
| [`gausshyper`](generated/scipy.stats.gausshyper.html#scipy.stats.gausshyper "scipy.stats.gausshyper") | A Gauss hypergeometric continuous random variable. |
| [`gamma`](generated/scipy.stats.gamma.html#scipy.stats.gamma "scipy.stats.gamma") | A gamma continuous random variable. |
| [`gengamma`](generated/scipy.stats.gengamma.html#scipy.stats.gengamma "scipy.stats.gengamma") | A generalized gamma continuous random variable. |
| [`genhalflogistic`](generated/scipy.stats.genhalflogistic.html#scipy.stats.genhalflogistic "scipy.stats.genhalflogistic") | A generalized half-logistic continuous random variable. |
| [`genhyperbolic`](generated/scipy.stats.genhyperbolic.html#scipy.stats.genhyperbolic "scipy.stats.genhyperbolic") | A generalized hyperbolic continuous random variable. |
| [`geninvgauss`](generated/scipy.stats.geninvgauss.html#scipy.stats.geninvgauss "scipy.stats.geninvgauss") | A Generalized Inverse Gaussian continuous random variable. |
| [`gibrat`](generated/scipy.stats.gibrat.html#scipy.stats.gibrat "scipy.stats.gibrat") | A Gibrat continuous random variable. |
| [`gompertz`](generated/scipy.stats.gompertz.html#scipy.stats.gompertz "scipy.stats.gompertz") | A Gompertz (or truncated Gumbel) continuous random variable. |
| [`gumbel_r`](generated/scipy.stats.gumbel_r.html#scipy.stats.gumbel_r "scipy.stats.gumbel_r") | A right-skewed Gumbel continuous random variable. |
| [`gumbel_l`](generated/scipy.stats.gumbel_l.html#scipy.stats.gumbel_l "scipy.stats.gumbel_l") | A left-skewed Gumbel continuous random variable. |
| [`halfcauchy`](generated/scipy.stats.halfcauchy.html#scipy.stats.halfcauchy "scipy.stats.halfcauchy") | A Half-Cauchy continuous random variable. |
| [`halflogistic`](generated/scipy.stats.halflogistic.html#scipy.stats.halflogistic "scipy.stats.halflogistic") | A half-logistic continuous random variable. |
| [`halfnorm`](generated/scipy.stats.halfnorm.html#scipy.stats.halfnorm "scipy.stats.halfnorm") | A half-normal continuous random variable. |
| [`halfgennorm`](generated/scipy.stats.halfgennorm.html#scipy.stats.halfgennorm "scipy.stats.halfgennorm") | The upper half of a generalized normal continuous random variable. |
| [`hypsecant`](generated/scipy.stats.hypsecant.html#scipy.stats.hypsecant "scipy.stats.hypsecant") | A hyperbolic secant continuous random variable. |
| [`invgamma`](generated/scipy.stats.invgamma.html#scipy.stats.invgamma "scipy.stats.invgamma") | An inverted gamma continuous random variable. |
| [`invgauss`](generated/scipy.stats.invgauss.html#scipy.stats.invgauss "scipy.stats.invgauss") | An inverse Gaussian continuous random variable. |
| [`invweibull`](generated/scipy.stats.invweibull.html#scipy.stats.invweibull "scipy.stats.invweibull") | An inverted Weibull continuous random variable. |
| [`irwinhall`](generated/scipy.stats.irwinhall.html#scipy.stats.irwinhall "scipy.stats.irwinhall") | An Irwin-Hall (Uniform Sum) continuous random variable. |
| [`jf_skew_t`](generated/scipy.stats.jf_skew_t.html#scipy.stats.jf_skew_t "scipy.stats.jf_skew_t") | Jones and Faddy skew-t distribution. |
| [`johnsonsb`](generated/scipy.stats.johnsonsb.html#scipy.stats.johnsonsb "scipy.stats.johnsonsb") | A Johnson SB continuous random variable. |
| [`johnsonsu`](generated/scipy.stats.johnsonsu.html#scipy.stats.johnsonsu "scipy.stats.johnsonsu") | A Johnson SU continuous random variable. |
| [`kappa4`](generated/scipy.stats.kappa4.html#scipy.stats.kappa4 "scipy.stats.kappa4") | Kappa 4 parameter distribution. |
| [`kappa3`](generated/scipy.stats.kappa3.html#scipy.stats.kappa3 "scipy.stats.kappa3") | Kappa 3 parameter distribution. |
| [`ksone`](generated/scipy.stats.ksone.html#scipy.stats.ksone "scipy.stats.ksone") | Kolmogorov-Smirnov one-sided test statistic distribution. |
| [`kstwo`](generated/scipy.stats.kstwo.html#scipy.stats.kstwo "scipy.stats.kstwo") | Kolmogorov-Smirnov two-sided test statistic distribution. |
| [`kstwobign`](generated/scipy.stats.kstwobign.html#scipy.stats.kstwobign "scipy.stats.kstwobign") | Limiting distribution of scaled Kolmogorov-Smirnov two-sided test statistic. |
| [`landau`](generated/scipy.stats.landau.html#scipy.stats.landau "scipy.stats.landau") | A Landau continuous random variable. |
| [`laplace`](generated/scipy.stats.laplace.html#scipy.stats.laplace "scipy.stats.laplace") | A Laplace continuous random variable. |
| [`laplace_asymmetric`](generated/scipy.stats.laplace_asymmetric.html#scipy.stats.laplace_asymmetric "scipy.stats.laplace_asymmetric") | An asymmetric Laplace continuous random variable. |
| [`levy`](generated/scipy.stats.levy.html#scipy.stats.levy "scipy.stats.levy") | A Levy continuous random variable. |
| [`levy_l`](generated/scipy.stats.levy_l.html#scipy.stats.levy_l "scipy.stats.levy_l") | A left-skewed Levy continuous random variable. |
| [`levy_stable`](generated/scipy.stats.levy_stable.html#scipy.stats.levy_stable "scipy.stats.levy_stable") | A Levy-stable continuous random variable. |
| [`logistic`](generated/scipy.stats.logistic.html#scipy.stats.logistic "scipy.stats.logistic") | A logistic (or Sech-squared) continuous random variable. |
| [`loggamma`](generated/scipy.stats.loggamma.html#scipy.stats.loggamma "scipy.stats.loggamma") | A log gamma continuous random variable. |
| [`loglaplace`](generated/scipy.stats.loglaplace.html#scipy.stats.loglaplace "scipy.stats.loglaplace") | A log-Laplace continuous random variable. |
| [`lognorm`](generated/scipy.stats.lognorm.html#scipy.stats.lognorm "scipy.stats.lognorm") | A lognormal continuous random variable. |
| [`loguniform`](generated/scipy.stats.loguniform.html#scipy.stats.loguniform "scipy.stats.loguniform") | A loguniform or reciprocal continuous random variable. |
| [`lomax`](generated/scipy.stats.lomax.html#scipy.stats.lomax "scipy.stats.lomax") | A Lomax (Pareto of the second kind) continuous random variable. |
| [`maxwell`](generated/scipy.stats.maxwell.html#scipy.stats.maxwell "scipy.stats.maxwell") | A Maxwell continuous random variable. |
| [`mielke`](generated/scipy.stats.mielke.html#scipy.stats.mielke "scipy.stats.mielke") | A Mielke Beta-Kappa / Dagum continuous random variable. |
| [`moyal`](generated/scipy.stats.moyal.html#scipy.stats.moyal "scipy.stats.moyal") | A Moyal continuous random variable. |
| [`nakagami`](generated/scipy.stats.nakagami.html#scipy.stats.nakagami "scipy.stats.nakagami") | A Nakagami continuous random variable. |
| [`ncx2`](generated/scipy.stats.ncx2.html#scipy.stats.ncx2 "scipy.stats.ncx2") | A non-central chi-squared continuous random variable. |
| [`ncf`](generated/scipy.stats.ncf.html#scipy.stats.ncf "scipy.stats.ncf") | A non-central F distribution continuous random variable. |
| [`nct`](generated/scipy.stats.nct.html#scipy.stats.nct "scipy.stats.nct") | A non-central Student's t continuous random variable. |
| [`norm`](generated/scipy.stats.norm.html#scipy.stats.norm "scipy.stats.norm") | A normal continuous random variable. |
| [`norminvgauss`](generated/scipy.stats.norminvgauss.html#scipy.stats.norminvgauss "scipy.stats.norminvgauss") | A Normal Inverse Gaussian continuous random variable. |
| [`pareto`](generated/scipy.stats.pareto.html#scipy.stats.pareto "scipy.stats.pareto") | A Pareto continuous random variable. |
| [`pearson3`](generated/scipy.stats.pearson3.html#scipy.stats.pearson3 "scipy.stats.pearson3") | A pearson type III continuous random variable. |
| [`powerlaw`](generated/scipy.stats.powerlaw.html#scipy.stats.powerlaw "scipy.stats.powerlaw") | A power-function continuous random variable. |
| [`powerlognorm`](generated/scipy.stats.powerlognorm.html#scipy.stats.powerlognorm "scipy.stats.powerlognorm") | A power log-normal continuous random variable. |
| [`powernorm`](generated/scipy.stats.powernorm.html#scipy.stats.powernorm "scipy.stats.powernorm") | A power normal continuous random variable. |
| [`rdist`](generated/scipy.stats.rdist.html#scipy.stats.rdist "scipy.stats.rdist") | An R-distributed (symmetric beta) continuous random variable. |
| [`rayleigh`](generated/scipy.stats.rayleigh.html#scipy.stats.rayleigh "scipy.stats.rayleigh") | A Rayleigh continuous random variable. |
| [`rel_breitwigner`](generated/scipy.stats.rel_breitwigner.html#scipy.stats.rel_breitwigner "scipy.stats.rel_breitwigner") | A relativistic Breit-Wigner random variable. |
| [`rice`](generated/scipy.stats.rice.html#scipy.stats.rice "scipy.stats.rice") | A Rice continuous random variable. |
| [`recipinvgauss`](generated/scipy.stats.recipinvgauss.html#scipy.stats.recipinvgauss "scipy.stats.recipinvgauss") | A reciprocal inverse Gaussian continuous random variable. |
| [`semicircular`](generated/scipy.stats.semicircular.html#scipy.stats.semicircular "scipy.stats.semicircular") | A semicircular continuous random variable. |
| [`skewcauchy`](generated/scipy.stats.skewcauchy.html#scipy.stats.skewcauchy "scipy.stats.skewcauchy") | A skewed Cauchy random variable. |
| [`skewnorm`](generated/scipy.stats.skewnorm.html#scipy.stats.skewnorm "scipy.stats.skewnorm") | A skew-normal random variable. |
| [`studentized_range`](generated/scipy.stats.studentized_range.html#scipy.stats.studentized_range "scipy.stats.studentized_range") | A studentized range continuous random variable. |
| [`t`](generated/scipy.stats.t.html#scipy.stats.t "scipy.stats.t") | A Student's t continuous random variable. |
| [`trapezoid`](generated/scipy.stats.trapezoid.html#scipy.stats.trapezoid "scipy.stats.trapezoid") | A trapezoidal continuous random variable. |
| [`triang`](generated/scipy.stats.triang.html#scipy.stats.triang "scipy.stats.triang") | A triangular continuous random variable. |
| [`truncexpon`](generated/scipy.stats.truncexpon.html#scipy.stats.truncexpon "scipy.stats.truncexpon") | A truncated exponential continuous random variable. |
| [`truncnorm`](generated/scipy.stats.truncnorm.html#scipy.stats.truncnorm "scipy.stats.truncnorm") | A truncated normal continuous random variable. |
| [`truncpareto`](generated/scipy.stats.truncpareto.html#scipy.stats.truncpareto "scipy.stats.truncpareto") | An upper truncated Pareto continuous random variable. |
| [`truncweibull_min`](generated/scipy.stats.truncweibull_min.html#scipy.stats.truncweibull_min "scipy.stats.truncweibull_min") | A doubly truncated Weibull minimum continuous random variable. |
| [`tukeylambda`](generated/scipy.stats.tukeylambda.html#scipy.stats.tukeylambda "scipy.stats.tukeylambda") | A Tukey-Lamdba continuous random variable. |
| [`uniform`](generated/scipy.stats.uniform.html#scipy.stats.uniform "scipy.stats.uniform") | A uniform continuous random variable. |
| [`vonmises`](generated/scipy.stats.vonmises.html#scipy.stats.vonmises "scipy.stats.vonmises") | A Von Mises continuous random variable. |
| [`vonmises_line`](generated/scipy.stats.vonmises_line.html#scipy.stats.vonmises_line "scipy.stats.vonmises_line") | A Von Mises continuous random variable. |
| [`wald`](generated/scipy.stats.wald.html#scipy.stats.wald "scipy.stats.wald") | A Wald continuous random variable. |
| [`weibull_min`](generated/scipy.stats.weibull_min.html#scipy.stats.weibull_min "scipy.stats.weibull_min") | Weibull minimum continuous random variable. |
| [`weibull_max`](generated/scipy.stats.weibull_max.html#scipy.stats.weibull_max "scipy.stats.weibull_max") | Weibull maximum continuous random variable. |
| [`wrapcauchy`](generated/scipy.stats.wrapcauchy.html#scipy.stats.wrapcauchy "scipy.stats.wrapcauchy") | A wrapped Cauchy continuous random variable. |
The `fit` method of the univariate continuous distributions uses
maximum likelihood estimation to fit the distribution to a data set.
The `fit` method can accept regular data or *censored data*.
Censored data is represented with instances of the [`CensoredData`](generated/scipy.stats.CensoredData.html#scipy.stats.CensoredData "scipy.stats.CensoredData")
class.
|  |  |
| --- | --- |
| [`CensoredData`](generated/scipy.stats.CensoredData.html#scipy.stats.CensoredData "scipy.stats.CensoredData")([uncensored,Â left,Â right,Â interval]) | Instances of this class represent censored data. |
### Multivariate distributions[#](#multivariate-distributions "Link to this heading")
|  |  |
| --- | --- |
| [`multivariate_normal`](generated/scipy.stats.multivariate_normal.html#scipy.stats.multivariate_normal "scipy.stats.multivariate_normal") | A multivariate normal random variable. |
| [`matrix_normal`](generated/scipy.stats.matrix_normal.html#scipy.stats.matrix_normal "scipy.stats.matrix_normal") | A matrix normal random variable. |
| [`dirichlet`](generated/scipy.stats.dirichlet.html#scipy.stats.dirichlet "scipy.stats.dirichlet") | A Dirichlet random variable. |
| [`dirichlet_multinomial`](generated/scipy.stats.dirichlet_multinomial.html#scipy.stats.dirichlet_multinomial "scipy.stats.dirichlet_multinomial") | A Dirichlet multinomial random variable. |
| [`wishart`](generated/scipy.stats.wishart.html#scipy.stats.wishart "scipy.stats.wishart") | A Wishart random variable. |
| [`invwishart`](generated/scipy.stats.invwishart.html#scipy.stats.invwishart "scipy.stats.invwishart") | An inverse Wishart random variable. |
| [`multinomial`](generated/scipy.stats.multinomial.html#scipy.stats.multinomial "scipy.stats.multinomial") | A multinomial random variable. |
| [`special_ortho_group`](generated/scipy.stats.special_ortho_group.html#scipy.stats.special_ortho_group "scipy.stats.special_ortho_group") | A Special Orthogonal matrix (SO(N)) random variable. |
| [`ortho_group`](generated/scipy.stats.ortho_group.html#scipy.stats.ortho_group "scipy.stats.ortho_group") | An Orthogonal matrix (O(N)) random variable. |
| [`unitary_group`](generated/scipy.stats.unitary_group.html#scipy.stats.unitary_group "scipy.stats.unitary_group") | A matrix-valued U(N) random variable. |
| [`random_correlation`](generated/scipy.stats.random_correlation.html#scipy.stats.random_correlation "scipy.stats.random_correlation") | A random correlation matrix. |
| [`multivariate_t`](generated/scipy.stats.multivariate_t.html#scipy.stats.multivariate_t "scipy.stats.multivariate_t") | A multivariate t-distributed random variable. |
| [`multivariate_hypergeom`](generated/scipy.stats.multivariate_hypergeom.html#scipy.stats.multivariate_hypergeom "scipy.stats.multivariate_hypergeom") | A multivariate hypergeometric random variable. |
| [`normal_inverse_gamma`](generated/scipy.stats.normal_inverse_gamma.html#scipy.stats.normal_inverse_gamma "scipy.stats.normal_inverse_gamma") | Normal-inverse-gamma distribution. |
| [`random_table`](generated/scipy.stats.random_table.html#scipy.stats.random_table "scipy.stats.random_table") | Contingency tables from independent samples with fixed marginal sums. |
| [`uniform_direction`](generated/scipy.stats.uniform_direction.html#scipy.stats.uniform_direction "scipy.stats.uniform_direction") | A vector-valued uniform direction. |
| [`vonmises_fisher`](generated/scipy.stats.vonmises_fisher.html#scipy.stats.vonmises_fisher "scipy.stats.vonmises_fisher") | A von Mises-Fisher variable. |
| [`matrix_t`](generated/scipy.stats.matrix_t.html#scipy.stats.matrix_t "scipy.stats.matrix_t") | A matrix t-random variable. |
[`scipy.stats.multivariate_normal`](generated/scipy.stats.multivariate_normal.html#scipy.stats.multivariate_normal "scipy.stats.multivariate_normal") methods accept instances
of the following class to represent the covariance.
|  |  |
| --- | --- |
| [`Covariance`](generated/scipy.stats.Covariance.html#scipy.stats.Covariance "scipy.stats.Covariance")() | Representation of a covariance matrix. |
### Discrete distributions[#](#discrete-distributions "Link to this heading")
|  |  |
| --- | --- |
| [`bernoulli`](generated/scipy.stats.bernoulli.html#scipy.stats.bernoulli "scipy.stats.bernoulli") | A Bernoulli discrete random variable. |
| [`betabinom`](generated/scipy.stats.betabinom.html#scipy.stats.betabinom "scipy.stats.betabinom") | A beta-binomial discrete random variable. |
| [`betanbinom`](generated/scipy.stats.betanbinom.html#scipy.stats.betanbinom "scipy.stats.betanbinom") | A beta-negative-binomial discrete random variable. |
| [`binom`](generated/scipy.stats.binom.html#scipy.stats.binom "scipy.stats.binom") | A binomial discrete random variable. |
| [`boltzmann`](generated/scipy.stats.boltzmann.html#scipy.stats.boltzmann "scipy.stats.boltzmann") | A Boltzmann (Truncated Discrete Exponential) random variable. |
| [`dlaplace`](generated/scipy.stats.dlaplace.html#scipy.stats.dlaplace "scipy.stats.dlaplace") | A Laplacian discrete random variable. |
| [`geom`](generated/scipy.stats.geom.html#scipy.stats.geom "scipy.stats.geom") | A geometric discrete random variable. |
| [`hypergeom`](generated/scipy.stats.hypergeom.html#scipy.stats.hypergeom "scipy.stats.hypergeom") | A hypergeometric discrete random variable. |
| [`logser`](generated/scipy.stats.logser.html#scipy.stats.logser "scipy.stats.logser") | A Logarithmic (Log-Series, Series) discrete random variable. |
| [`nbinom`](generated/scipy.stats.nbinom.html#scipy.stats.nbinom "scipy.stats.nbinom") | A negative binomial discrete random variable. |
| [`nchypergeom_fisher`](generated/scipy.stats.nchypergeom_fisher.html#scipy.stats.nchypergeom_fisher "scipy.stats.nchypergeom_fisher") | A Fisher's noncentral hypergeometric discrete random variable. |
| [`nchypergeom_wallenius`](generated/scipy.stats.nchypergeom_wallenius.html#scipy.stats.nchypergeom_wallenius "scipy.stats.nchypergeom_wallenius") | A Wallenius' noncentral hypergeometric discrete random variable. |
| [`nhypergeom`](generated/scipy.stats.nhypergeom.html#scipy.stats.nhypergeom "scipy.stats.nhypergeom") | A negative hypergeometric discrete random variable. |
| [`planck`](generated/scipy.stats.planck.html#scipy.stats.planck "scipy.stats.planck") | A Planck discrete exponential random variable. |
| [`poisson`](generated/scipy.stats.poisson.html#scipy.stats.poisson "scipy.stats.poisson") | A Poisson discrete random variable. |
| [`poisson_binom`](generated/scipy.stats.poisson_binom.html#scipy.stats.poisson_binom "scipy.stats.poisson_binom") | A Poisson Binomial discrete random variable. |
| [`randint`](generated/scipy.stats.randint.html#scipy.stats.randint "scipy.stats.randint") | A uniform discrete random variable. |
| [`skellam`](generated/scipy.stats.skellam.html#scipy.stats.skellam "scipy.stats.skellam") | A Skellam discrete random variable. |
| [`yulesimon`](generated/scipy.stats.yulesimon.html#scipy.stats.yulesimon "scipy.stats.yulesimon") | A Yule-Simon discrete random variable. |
| [`zipf`](generated/scipy.stats.zipf.html#scipy.stats.zipf "scipy.stats.zipf") | A Zipf (Zeta) discrete random variable. |
| [`zipfian`](generated/scipy.stats.zipfian.html#scipy.stats.zipfian "scipy.stats.zipfian") | A Zipfian discrete random variable. |
An overview of statistical functions is given below. Many of these functions
have a similar version in [`scipy.stats.mstats`](stats.mstats.html#module-scipy.stats.mstats "scipy.stats.mstats") which work for masked arrays.
## Summary statistics[#](#summary-statistics "Link to this heading")
|  |  |
| --- | --- |
| [`describe`](generated/scipy.stats.describe.html#scipy.stats.describe "scipy.stats.describe")(a[,Â axis,Â ddof,Â bias,Â nan\_policy]) | Compute several descriptive statistics of the passed array. |
| [`gmean`](generated/scipy.stats.gmean.html#scipy.stats.gmean "scipy.stats.gmean")(a[,Â axis,Â dtype,Â weights,Â nan\_policy,Â ...]) | Compute the weighted geometric mean along the specified axis. |
| [`hmean`](generated/scipy.stats.hmean.html#scipy.stats.hmean "scipy.stats.hmean")(a[,Â axis,Â dtype,Â weights,Â nan\_policy,Â ...]) | Calculate the weighted harmonic mean along the specified axis. |
| [`pmean`](generated/scipy.stats.pmean.html#scipy.stats.pmean "scipy.stats.pmean")(a,Â p,Â \*[,Â axis,Â dtype,Â weights,Â ...]) | Calculate the weighted power mean along the specified axis. |
| [`kurtosis`](generated/scipy.stats.kurtosis.html#scipy.stats.kurtosis "scipy.stats.kurtosis")(a[,Â axis,Â fisher,Â bias,Â ...]) | Compute the kurtosis (Fisher or Pearson) of a dataset. |
| [`mode`](generated/scipy.stats.mode.html#scipy.stats.mode "scipy.stats.mode")(a[,Â axis,Â nan\_policy,Â keepdims]) | Return an array of the modal (most common) value in the passed array. |
| [`moment`](generated/scipy.stats.moment.html#scipy.stats.moment "scipy.stats.moment")(a[,Â order,Â axis,Â nan\_policy,Â center,Â ...]) | Calculate the nth moment about the mean for a sample. |
| [`lmoment`](generated/scipy.stats.lmoment.html#scipy.stats.lmoment "scipy.stats.lmoment")(sample[,Â order,Â axis,Â sorted,Â ...]) | Compute L-moments of a sample from a continuous distribution. |
| [`expectile`](generated/scipy.stats.expectile.html#scipy.stats.expectile "scipy.stats.expectile")(a[,Â alpha,Â weights,Â axis,Â ...]) | Compute the expectile at the specified level. |
| [`skew`](generated/scipy.stats.skew.html#scipy.stats.skew "scipy.stats.skew")(a[,Â axis,Â bias,Â nan\_policy,Â keepdims]) | Compute the sample skewness of a data set. |
| [`kstat`](generated/scipy.stats.kstat.html#scipy.stats.kstat "scipy.stats.kstat")(data[,Â n,Â axis,Â nan\_policy,Â keepdims]) | Return the *n* th k-statistic ( `1<=n<=4` so far). |
| [`kstatvar`](generated/scipy.stats.kstatvar.html#scipy.stats.kstatvar "scipy.stats.kstatvar")(data[,Â n,Â axis,Â nan\_policy,Â keepdims]) | Return an unbiased estimator of the variance of the k-statistic. |
| [`tmean`](generated/scipy.stats.tmean.html#scipy.stats.tmean "scipy.stats.tmean")(a[,Â limits,Â inclusive,Â axis,Â ...]) | Compute the trimmed mean. |
| [`tvar`](generated/scipy.stats.tvar.html#scipy.stats.tvar "scipy.stats.tvar")(a[,Â limits,Â inclusive,Â axis,Â ddof,Â ...]) | Compute the trimmed variance. |
| [`tmin`](generated/scipy.stats.tmin.html#scipy.stats.tmin "scipy.stats.tmin")(a[,Â lowerlimit,Â axis,Â inclusive,Â ...]) | Compute the trimmed minimum. |
| [`tmax`](generated/scipy.stats.tmax.html#scipy.stats.tmax "scipy.stats.tmax")(a[,Â upperlimit,Â axis,Â inclusive,Â ...]) | Compute the trimmed maximum. |
| [`tstd`](generated/scipy.stats.tstd.html#scipy.stats.tstd "scipy.stats.tstd")(a[,Â limits,Â inclusive,Â axis,Â ddof,Â ...]) | Compute the trimmed sample standard deviation. |
| [`tsem`](generated/scipy.stats.tsem.html#scipy.stats.tsem "scipy.stats.tsem")(a[,Â limits,Â inclusive,Â axis,Â ddof,Â ...]) | Compute the trimmed standard error of the mean. |
| [`variation`](generated/scipy.stats.variation.html#scipy.stats.variation "scipy.stats.variation")(a[,Â axis,Â nan\_policy,Â ddof,Â keepdims]) | Compute the coefficient of variation. |
| [`rankdata`](generated/scipy.stats.rankdata.html#scipy.stats.rankdata "scipy.stats.rankdata")(a[,Â method,Â axis,Â nan\_policy]) | Assign ranks to data, dealing with ties appropriately. |
| [`tiecorrect`](generated/scipy.stats.tiecorrect.html#scipy.stats.tiecorrect "scipy.stats.tiecorrect")(rankvals) | Tie correction factor for Mann-Whitney U and Kruskal-Wallis H tests. |
| [`trim_mean`](generated/scipy.stats.trim_mean.html#scipy.stats.trim_mean "scipy.stats.trim_mean")(a,Â proportiontocut[,Â axis,Â ...]) | Return mean of array after trimming a specified fraction of extreme values. |
| [`gstd`](generated/scipy.stats.gstd.html#scipy.stats.gstd "scipy.stats.gstd")(a[,Â axis,Â ddof,Â keepdims,Â nan\_policy]) | Calculate the geometric standard deviation of an array. |
| [`iqr`](generated/scipy.stats.iqr.html#scipy.stats.iqr "scipy.stats.iqr")(x[,Â axis,Â rng,Â scale,Â nan\_policy,Â ...]) | Compute the interquartile range of the data along the specified axis. |
| [`sem`](generated/scipy.stats.sem.html#scipy.stats.sem "scipy.stats.sem")(a[,Â axis,Â ddof,Â nan\_policy,Â keepdims]) | Compute standard error of the mean. |
| [`bayes_mvs`](generated/scipy.stats.bayes_mvs.html#scipy.stats.bayes_mvs "scipy.stats.bayes_mvs")(data[,Â alpha]) | Bayesian confidence intervals for the mean, var, and std. |
| [`mvsdist`](generated/scipy.stats.mvsdist.html#scipy.stats.mvsdist "scipy.stats.mvsdist")(data) | 'Frozen' distributions for mean, variance, and standard deviation of data. |
| [`entropy`](generated/scipy.stats.entropy.html#scipy.stats.entropy "scipy.stats.entropy")(pk[,Â qk,Â base,Â axis,Â nan\_policy,Â ...]) | Calculate the Shannon entropy/relative entropy of given distribution(s). |
| [`differential_entropy`](generated/scipy.stats.differential_entropy.html#scipy.stats.differential_entropy "scipy.stats.differential_entropy")(values,Â \*[,Â ...]) | Given a sample of a distribution, estimate the differential entropy. |
| [`median_abs_deviation`](generated/scipy.stats.median_abs_deviation.html#scipy.stats.median_abs_deviation "scipy.stats.median_abs_deviation")(x[,Â axis,Â center,Â ...]) | Compute the median absolute deviation of the data along the given axis. |
## Frequency statistics[#](#frequency-statistics "Link to this heading")
|  |  |
| --- | --- |
| [`quantile`](generated/scipy.stats.quantile.html#scipy.stats.quantile "scipy.stats.quantile")(x,Â p,Â \*[,Â method,Â axis,Â ...]) | Compute the p-th quantile of the data along the specified axis. |
| [`estimated_cdf`](generated/scipy.stats.estimated_cdf.html#scipy.stats.estimated_cdf "scipy.stats.estimated_cdf")(x,Â y,Â \*[,Â method,Â axis,Â ...]) | Estimate the CDF of the distribution underlying a sample. |
| [`cumfreq`](generated/scipy.stats.cumfreq.html#scipy.stats.cumfreq "scipy.stats.cumfreq")(a[,Â numbins,Â defaultreallimits,Â weights]) | Return a cumulative frequency histogram, using the histogram function. |
| [`relfreq`](generated/scipy.stats.relfreq.html#scipy.stats.relfreq "scipy.stats.relfreq")(a[,Â numbins,Â defaultreallimits,Â weights]) | Return a relative frequency histogram, using the histogram function. |
| [`percentileofscore`](generated/scipy.stats.percentileofscore.html#scipy.stats.percentileofscore "scipy.stats.percentileofscore")(a,Â score[,Â kind,Â nan\_policy]) | Compute the percentile rank of a score relative to a list of scores. |
| [`scoreatpercentile`](generated/scipy.stats.scoreatpercentile.html#scipy.stats.scoreatpercentile "scipy.stats.scoreatpercentile")(a,Â per[,Â limit,Â ...]) | Calculate the score at a given percentile of the input sequence. |
|  |  |
| --- | --- |
| [`binned_statistic`](generated/scipy.stats.binned_statistic.html#scipy.stats.binned_statistic "scipy.stats.binned_statistic")(x,Â values[,Â statistic,Â ...]) | Compute a binned statistic for one or more sets of data. |
| [`binned_statistic_2d`](generated/scipy.stats.binned_statistic_2d.html#scipy.stats.binned_statistic_2d "scipy.stats.binned_statistic_2d")(x,Â y,Â values[,Â ...]) | Compute a bidimensional binned statistic for one or more sets of data. |
| [`binned_statistic_dd`](generated/scipy.stats.binned_statistic_dd.html#scipy.stats.binned_statistic_dd "scipy.stats.binned_statistic_dd")(sample,Â values[,Â ...]) | Compute a multidimensional binned statistic for a set of data. |
## Hypothesis Tests and related functions[#](#hypothesis-tests-and-related-functions "Link to this heading")
SciPy has many functions for performing hypothesis tests that return a
test statistic and a p-value, and several of them return confidence intervals
and/or other related information.
The headings below are based on common uses of the functions within, but due to
the wide variety of statistical procedures, any attempt at coarse-grained
categorization will be imperfect. Also, note that tests within the same heading
are not interchangeable in general (e.g. many have different distributional
assumptions).
### One Sample Tests / Paired Sample Tests[#](#one-sample-tests-paired-sample-tests "Link to this heading")
One sample tests are typically used to assess whether a single sample was
drawn from a specified distribution or a distribution with specified properties
(e.g. zero mean).
|  |  |
| --- | --- |
| [`ttest_1samp`](generated/scipy.stats.ttest_1samp.html#scipy.stats.ttest_1samp "scipy.stats.ttest_1samp")(a,Â popmean[,Â axis,Â nan\_policy,Â ...]) | Calculate the T-test for the mean of ONE group of scores. |
| [`binomtest`](generated/scipy.stats.binomtest.html#scipy.stats.binomtest "scipy.stats.binomtest")(k,Â n[,Â p,Â alternative]) | Perform a test that the probability of success is p. |
| [`quantile_test`](generated/scipy.stats.quantile_test.html#scipy.stats.quantile_test "scipy.stats.quantile_test")(x,Â \*[,Â q,Â p,Â alternative,Â ...]) | Perform a quantile test and compute a confidence interval of the quantile. |
| [`skewtest`](generated/scipy.stats.skewtest.html#scipy.stats.skewtest "scipy.stats.skewtest")(a[,Â axis,Â nan\_policy,Â alternative,Â ...]) | Test whether the skew is different from the normal distribution. |
| [`kurtosistest`](generated/scipy.stats.kurtosistest.html#scipy.stats.kurtosistest "scipy.stats.kurtosistest")(a[,Â axis,Â nan\_policy,Â ...]) | Test whether a dataset has normal kurtosis. |
| [`normaltest`](generated/scipy.stats.normaltest.html#scipy.stats.normaltest "scipy.stats.normaltest")(a[,Â axis,Â nan\_policy,Â keepdims]) | Test whether a sample differs from a normal distribution. |
| [`jarque_bera`](generated/scipy.stats.jarque_bera.html#scipy.stats.jarque_bera "scipy.stats.jarque_bera")(x,Â \*[,Â axis,Â nan\_policy,Â keepdims]) | Perform the Jarque-Bera goodness of fit test on sample data. |
| [`shapiro`](generated/scipy.stats.shapiro.html#scipy.stats.shapiro "scipy.stats.shapiro")(x,Â \*[,Â axis,Â nan\_policy,Â keepdims]) | Perform the Shapiro-Wilk test for normality. |
| [`anderson`](generated/scipy.stats.anderson.html#scipy.stats.anderson "scipy.stats.anderson")(x[,Â dist,Â method]) | Anderson-Darling test for data coming from a particular distribution. |
| [`cramervonmises`](generated/scipy.stats.cramervonmises.html#scipy.stats.cramervonmises "scipy.stats.cramervonmises")(rvs,Â cdf[,Â args,Â axis,Â ...]) | Perform the one-sample CramÃ©r-von Mises test for goodness of fit. |
| [`ks_1samp`](generated/scipy.stats.ks_1samp.html#scipy.stats.ks_1samp "scipy.stats.ks_1samp")(x,Â cdf[,Â args,Â alternative,Â ...]) | Performs the one-sample Kolmogorov-Smirnov test for goodness of fit. |
| [`goodness_of_fit`](generated/scipy.stats.goodness_of_fit.html#scipy.stats.goodness_of_fit "scipy.stats.goodness_of_fit")(dist,Â data,Â \*[,Â ...]) | Perform a goodness of fit test comparing data to a distribution family. |
| [`chisquare`](generated/scipy.stats.chisquare.html#scipy.stats.chisquare "scipy.stats.chisquare")(f\_obs[,Â f\_exp,Â ddof,Â axis,Â ...]) | Perform Pearson's chi-squared test. |
| [`power_divergence`](generated/scipy.stats.power_divergence.html#scipy.stats.power_divergence "scipy.stats.power_divergence")(f\_obs[,Â f\_exp,Â ddof,Â axis,Â ...]) | Cressie-Read power divergence statistic and goodness of fit test. |
Paired sample tests are often used to assess whether two samples were drawn
from the same distribution; they differ from the independent sample tests below
in that each observation in one sample is treated as paired with a
closely-related observation in the other sample (e.g. when environmental
factors are controlled between observations within a pair but not among pairs).
They can also be interpreted or used as one-sample tests (e.g. tests on the
mean or median of *differences* between paired observations).
|  |  |
| --- | --- |
| [`ttest_rel`](generated/scipy.stats.ttest_rel.html#scipy.stats.ttest_rel "scipy.stats.ttest_rel")(a,Â b[,Â axis,Â nan\_policy,Â ...]) | Calculate the t-test on TWO RELATED samples of scores, a and b. |
| [`wilcoxon`](generated/scipy.stats.wilcoxon.html#scipy.stats.wilcoxon "scipy.stats.wilcoxon")(x[,Â y,Â zero\_method,Â correction,Â ...]) | Calculate the Wilcoxon signed-rank test. |
### Association/Correlation Tests[#](#association-correlation-tests "Link to this heading")
These tests are often used to assess whether there is a relationship (e.g.
linear) between paired observations in multiple samples or among the
coordinates of multivariate observations.
|  |  |
| --- | --- |
| [`linregress`](generated/scipy.stats.linregress.html#scipy.stats.linregress "scipy.stats.linregress")(x,Â y[,Â alternative,Â axis,Â ...]) | Calculate a linear least-squares regression for two sets of measurements. |
| [`pearsonr`](generated/scipy.stats.pearsonr.html#scipy.stats.pearsonr "scipy.stats.pearsonr")(x,Â y,Â \*[,Â alternative,Â method,Â axis]) | Pearson correlation coefficient and p-value for testing non-correlation. |
| [`spearmanrho`](generated/scipy.stats.spearmanrho.html#scipy.stats.spearmanrho "scipy.stats.spearmanrho")(x,Â y,Â /,Â \*[,Â alternative,Â ...]) | Calculate a Spearman rho correlation coefficient with associated p-value. |
| [`pointbiserialr`](generated/scipy.stats.pointbiserialr.html#scipy.stats.pointbiserialr "scipy.stats.pointbiserialr")(x,Â y,Â \*[,Â axis,Â nan\_policy,Â ...]) | Calculate a point biserial correlation coefficient and its p-value. |
| [`kendalltau`](generated/scipy.stats.kendalltau.html#scipy.stats.kendalltau "scipy.stats.kendalltau")(x,Â y,Â \*[,Â nan\_policy,Â method,Â ...]) | Calculate Kendall's tau, a correlation measure for ordinal data. |
| [`chatterjeexi`](generated/scipy.stats.chatterjeexi.html#scipy.stats.chatterjeexi "scipy.stats.chatterjeexi")(x,Â y,Â \*[,Â axis,Â y\_continuous,Â ...]) | Compute the xi correlation and perform a test of independence. |
| [`weightedtau`](generated/scipy.stats.weightedtau.html#scipy.stats.weightedtau "scipy.stats.weightedtau")(x,Â y[,Â rank,Â weigher,Â additive,Â ...]) | Compute a weighted version of Kendall's \(\tau\). |
| [`somersd`](generated/scipy.stats.somersd.html#scipy.stats.somersd "scipy.stats.somersd")(x[,Â y,Â alternative]) | Calculates Somers' D, an asymmetric measure of ordinal association. |
| [`siegelslopes`](generated/scipy.stats.siegelslopes.html#scipy.stats.siegelslopes "scipy.stats.siegelslopes")(y[,Â x,Â method,Â axis,Â ...]) | Computes the Siegel estimator for a set of points (x, y). |
| [`theilslopes`](generated/scipy.stats.theilslopes.html#scipy.stats.theilslopes "scipy.stats.theilslopes")(y[,Â x,Â alpha,Â method,Â axis,Â ...]) | Computes the Theil-Sen estimator for a set of points (x, y). |
| [`page_trend_test`](generated/scipy.stats.page_trend_test.html#scipy.stats.page_trend_test "scipy.stats.page_trend_test")(data[,Â ranked,Â ...]) | Perform Page's Test, a measure of trend in observations between treatments. |
| [`multiscale_graphcorr`](generated/scipy.stats.multiscale_graphcorr.html#scipy.stats.multiscale_graphcorr "scipy.stats.multiscale_graphcorr")(x,Â y[,Â ...]) | Computes the Multiscale Graph Correlation (MGC) test statistic. |
| [`spearmanr`](generated/scipy.stats.spearmanr.html#scipy.stats.spearmanr "scipy.stats.spearmanr")(a[,Â b,Â axis,Â nan\_policy,Â alternative]) | Calculate a Spearman correlation coefficient with associated p-value. |
These association tests and are to work with samples in the form of contingency
tables. Supporting functions are available in [`scipy.stats.contingency`](stats.contingency.html#module-scipy.stats.contingency "scipy.stats.contingency").
|  |  |
| --- | --- |
| [`chi2_contingency`](generated/scipy.stats.chi2_contingency.html#scipy.stats.chi2_contingency "scipy.stats.chi2_contingency")(observed[,Â correction,Â ...]) | Chi-square test of independence of variables in a contingency table. |
| [`fisher_exact`](generated/scipy.stats.fisher_exact.html#scipy.stats.fisher_exact "scipy.stats.fisher_exact")(table[,Â alternative,Â method]) | Perform a Fisher exact test on a contingency table. |
| [`barnard_exact`](generated/scipy.stats.barnard_exact.html#scipy.stats.barnard_exact "scipy.stats.barnard_exact")(table[,Â alternative,Â pooled,Â n]) | Perform a Barnard exact test on a 2x2 contingency table. |
| [`boschloo_exact`](generated/scipy.stats.boschloo_exact.html#scipy.stats.boschloo_exact "scipy.stats.boschloo_exact")(table[,Â alternative,Â n]) | Perform Boschloo's exact test on a 2x2 contingency table. |
### Independent Sample Tests[#](#independent-sample-tests "Link to this heading")
Independent sample tests are typically used to assess whether multiple samples
were independently drawn from the same distribution or different distributions
with a shared property (e.g. equal means).
Some tests are specifically for comparing two samples.
|  |  |
| --- | --- |
| [`ttest_ind_from_stats`](generated/scipy.stats.ttest_ind_from_stats.html#scipy.stats.ttest_ind_from_stats "scipy.stats.ttest_ind_from_stats")(mean1,Â std1,Â nobs1,Â ...) | T-test for means of two independent samples from descriptive statistics. |
| [`poisson_means_test`](generated/scipy.stats.poisson_means_test.html#scipy.stats.poisson_means_test "scipy.stats.poisson_means_test")(k1,Â n1,Â k2,Â n2,Â \*[,Â ...]) | Performs the Poisson means test, AKA the "E-test". |
| [`ttest_ind`](generated/scipy.stats.ttest_ind.html#scipy.stats.ttest_ind "scipy.stats.ttest_ind")(a,Â b,Â \*[,Â axis,Â equal\_var,Â ...]) | Calculate the T-test for the means of *two independent* samples of scores. |
| [`mannwhitneyu`](generated/scipy.stats.mannwhitneyu.html#scipy.stats.mannwhitneyu "scipy.stats.mannwhitneyu")(x,Â y[,Â use\_continuity,Â ...]) | Perform the Mann-Whitney U rank test on two independent samples. |
| [`bws_test`](generated/scipy.stats.bws_test.html#scipy.stats.bws_test "scipy.stats.bws_test")(x,Â y,Â \*[,Â alternative,Â axis,Â method]) | Perform the Baumgartner-Weiss-Schindler test on two independent samples. |
| [`ranksums`](generated/scipy.stats.ranksums.html#scipy.stats.ranksums "scipy.stats.ranksums")(x,Â y[,Â alternative,Â axis,Â ...]) | Compute the Wilcoxon rank-sum statistic for two samples. |
| [`brunnermunzel`](generated/scipy.stats.brunnermunzel.html#scipy.stats.brunnermunzel "scipy.stats.brunnermunzel")(x,Â y[,Â alternative,Â ...]) | Compute the Brunner-Munzel test on samples x and y. |
| [`mood`](generated/scipy.stats.mood.html#scipy.stats.mood "scipy.stats.mood")(x,Â y[,Â axis,Â alternative,Â nan\_policy,Â ...]) | Perform Mood's test for equal scale parameters. |
| [`ansari`](generated/scipy.stats.ansari.html#scipy.stats.ansari "scipy.stats.ansari")(x,Â y[,Â alternative,Â axis,Â method,Â ...]) | Perform the Ansari-Bradley test for equal scale parameters. |
| [`cramervonmises_2samp`](generated/scipy.stats.cramervonmises_2samp.html#scipy.stats.cramervonmises_2samp "scipy.stats.cramervonmises_2samp")(x,Â y[,Â method,Â axis,Â ...]) | Perform the two-sample CramÃ©r-von Mises test for goodness of fit. |
| [`epps_singleton_2samp`](generated/scipy.stats.epps_singleton_2samp.html#scipy.stats.epps_singleton_2samp "scipy.stats.epps_singleton_2samp")(x,Â y[,Â t,Â axis,Â ...]) | Compute the Epps-Singleton (ES) test statistic. |
| [`ks_2samp`](generated/scipy.stats.ks_2samp.html#scipy.stats.ks_2samp "scipy.stats.ks_2samp")(data1,Â data2[,Â alternative,Â ...]) | Performs the two-sample Kolmogorov-Smirnov test for goodness of fit. |
| [`kstest`](generated/scipy.stats.kstest.html#scipy.stats.kstest "scipy.stats.kstest")(rvs,Â cdf[,Â args,Â N,Â alternative,Â ...]) | Performs the (one-sample or two-sample) Kolmogorov-Smirnov test for goodness of fit. |
Others are generalized to multiple samples.
|  |  |
| --- | --- |
| [`f_oneway`](generated/scipy.stats.f_oneway.html#scipy.stats.f_oneway "scipy.stats.f_oneway")(\*samples[,Â axis,Â equal\_var,Â ...]) | Perform one-way ANOVA. |
| [`tukey_hsd`](generated/scipy.stats.tukey_hsd.html#scipy.stats.tukey_hsd "scipy.stats.tukey_hsd")(\*samples[,Â equal\_var]) | Perform Tukey's HSD test for equality of means over multiple treatments. |
| [`dunnett`](generated/scipy.stats.dunnett.html#scipy.stats.dunnett "scipy.stats.dunnett")(\*samples,Â control[,Â alternative,Â ...]) | Dunnett's test: multiple comparisons of means against a control group. |
| [`kruskal`](generated/scipy.stats.kruskal.html#scipy.stats.kruskal "scipy.stats.kruskal")(\*samples[,Â nan\_policy,Â axis,Â keepdims]) | Compute the Kruskal-Wallis H-test for independent samples. |
| [`alexandergovern`](generated/scipy.stats.alexandergovern.html#scipy.stats.alexandergovern "scipy.stats.alexandergovern")(\*samples[,Â nan\_policy,Â ...]) | Performs the Alexander Govern test. |
| [`fligner`](generated/scipy.stats.fligner.html#scipy.stats.fligner "scipy.stats.fligner")(\*samples[,Â center,Â proportiontocut,Â ...]) | Perform Fligner-Killeen test for equality of variance. |
| [`levene`](generated/scipy.stats.levene.html#scipy.stats.levene "scipy.stats.levene")(\*samples[,Â center,Â proportiontocut,Â ...]) | Perform Levene test for equal variances. |
| [`bartlett`](generated/scipy.stats.bartlett.html#scipy.stats.bartlett "scipy.stats.bartlett")(\*samples[,Â axis,Â nan\_policy,Â keepdims]) | Perform Bartlett's test for equal variances. |
| [`median_test`](generated/scipy.stats.median_test.html#scipy.stats.median_test "scipy.stats.median_test")(\*samples[,Â ties,Â correction,Â ...]) | Perform a Mood's median test. |
| [`friedmanchisquare`](generated/scipy.stats.friedmanchisquare.html#scipy.stats.friedmanchisquare "scipy.stats.friedmanchisquare")(\*samples[,Â axis,Â ...]) | Compute the Friedman test for repeated samples. |
| [`anderson_ksamp`](generated/scipy.stats.anderson_ksamp.html#scipy.stats.anderson_ksamp "scipy.stats.anderson_ksamp")(samples[,Â midrank,Â variant,Â ...]) | The Anderson-Darling test for k-samples. |
### Resampling and Monte Carlo Methods[#](#resampling-and-monte-carlo-methods "Link to this heading")
The following functions can reproduce the p-value and confidence interval
results of most of the functions above, and often produce accurate results in a
wider variety of conditions. They can also be used to perform hypothesis tests
and generate confidence intervals for custom statistics. This flexibility comes
at the cost of greater computational requirements and stochastic results.
|  |  |
| --- | --- |
| [`monte_carlo_test`](generated/scipy.stats.monte_carlo_test.html#scipy.stats.monte_carlo_test "scipy.stats.monte_carlo_test")(data,Â rvs,Â statistic,Â \*[,Â ...]) | Perform a Monte Carlo hypothesis test. |
| [`permutation_test`](generated/scipy.stats.permutation_test.html#scipy.stats.permutation_test "scipy.stats.permutation_test")(data,Â statistic,Â \*[,Â ...]) | Performs a permutation test of a given statistic on provided data. |
| [`bootstrap`](generated/scipy.stats.bootstrap.html#scipy.stats.bootstrap "scipy.stats.bootstrap")(data,Â statistic,Â \*[,Â n\_resamples,Â ...]) | Compute a two-sided bootstrap confidence interval of a statistic. |
| [`power`](generated/scipy.stats.power.html#scipy.stats.power "scipy.stats.power")(test,Â rvs,Â n\_observations,Â \*[,Â ...]) | Simulate the power of a hypothesis test under an alternative hypothesis. |
Instances of the following object can be passed into some hypothesis test
functions to perform a resampling or Monte Carlo version of the hypothesis
test.
|  |  |
| --- | --- |
| [`MonteCarloMethod`](generated/scipy.stats.MonteCarloMethod.html#scipy.stats.MonteCarloMethod "scipy.stats.MonteCarloMethod")([n\_resamples,Â batch,Â rvs,Â rng]) | Configuration information for a Monte Carlo hypothesis test. |
| [`PermutationMethod`](generated/scipy.stats.PermutationMethod.html#scipy.stats.PermutationMethod "scipy.stats.PermutationMethod")([n\_resamples,Â batch,Â ...]) | Configuration information for a permutation hypothesis test. |
| [`BootstrapMethod`](generated/scipy.stats.BootstrapMethod.html#scipy.stats.BootstrapMethod "scipy.stats.BootstrapMethod")([n\_resamples,Â batch,Â ...]) | Configuration information for a bootstrap confidence interval. |
### Multiple Hypothesis Testing and Meta-Analysis[#](#multiple-hypothesis-testing-and-meta-analysis "Link to this heading")
These functions are for assessing the results of individual tests as a whole.
Functions for performing specific multiple hypothesis tests (e.g. post hoc
tests) are listed above.
|  |  |
| --- | --- |
| [`combine_pvalues`](generated/scipy.stats.combine_pvalues.html#scipy.stats.combine_pvalues "scipy.stats.combine_pvalues")(pvalues[,Â method,Â weights,Â ...]) | Combine p-values from independent tests that bear upon the same hypothesis. |
| [`false_discovery_control`](generated/scipy.stats.false_discovery_control.html#scipy.stats.false_discovery_control "scipy.stats.false_discovery_control")(ps,Â \*[,Â axis,Â method]) | Adjust p-values to control the false discovery rate. |
## Random Variables[#](#random-variables "Link to this heading")
|  |  |
| --- | --- |
| [`make_distribution`](generated/scipy.stats.make_distribution.html#scipy.stats.make_distribution "scipy.stats.make_distribution")(dist) | Generate a *UnivariateDistribution* class from a compatible object. |
| [`Normal`](generated/scipy.stats.Normal.html#scipy.stats.Normal "scipy.stats.Normal")([mu,Â sigma]) | Normal distribution with prescribed mean and standard deviation. |
| [`Logistic`](generated/scipy.stats.Logistic.html#scipy.stats.Logistic "scipy.stats.Logistic")(\*[,Â tol,Â validation\_policy,Â ...]) | Standard logistic distribution. |
| [`Uniform`](generated/scipy.stats.Uniform.html#scipy.stats.Uniform "scipy.stats.Uniform")(\*[,Â a,Â b]) | Uniform distribution. |
| [`Binomial`](generated/scipy.stats.Binomial.html#scipy.stats.Binomial "scipy.stats.Binomial")(\*,Â n,Â p,Â \*\*kwargs) | Binomial distribution with prescribed success probability and number of trials |
| [`Mixture`](generated/scipy.stats.Mixture.html#scipy.stats.Mixture "scipy.stats.Mixture")(components,Â \*[,Â weights]) | Representation of a mixture distribution. |
| [`order_statistic`](generated/scipy.stats.order_statistic.html#scipy.stats.order_statistic "scipy.stats.order_statistic")(X,Â /,Â \*,Â r,Â n) | Probability distribution of an order statistic. |
| [`truncate`](generated/scipy.stats.truncate.html#scipy.stats.truncate "scipy.stats.truncate")(X[,Â lb,Â ub]) | Truncate the support of a random variable. |
| [`abs`](generated/scipy.stats.abs.html#scipy.stats.abs "scipy.stats.abs")(X,Â /) | Absolute value of a random variable. |
| [`exp`](generated/scipy.stats.exp.html#scipy.stats.exp "scipy.stats.exp")(X,Â /) | Natural exponential of a random variable. |
| [`log`](generated/scipy.stats.log.html#scipy.stats.log "scipy.stats.log")(X,Â /) | Natural logarithm of a non-negative random variable. |
## Other statistical functionality[#](#other-statistical-functionality "Link to this heading")
* [Quasi-Monte Carlo submodule (`scipy.stats.qmc`)](stats.qmc.html)
* [Contingency table functions (`scipy.stats.contingency`)](stats.contingency.html)
* [Statistical functions for masked arrays (`scipy.stats.mstats`)](stats.mstats.html)
* [Random Number Generators (`scipy.stats.sampling`)](stats.sampling.html)
### Transformations[#](#transformations "Link to this heading")
|  |  |
| --- | --- |
| [`boxcox`](generated/scipy.stats.boxcox.html#scipy.stats.boxcox "scipy.stats.boxcox")(x[,Â lmbda,Â alpha,Â optimizer,Â nan\_policy]) | Return a dataset transformed by a Box-Cox power transformation. |
| [`boxcox_normmax`](generated/scipy.stats.boxcox_normmax.html#scipy.stats.boxcox_normmax "scipy.stats.boxcox_normmax")(x[,Â brack,Â method,Â ...]) | Compute optimal Box-Cox transform parameter for input data. |
| [`boxcox_llf`](generated/scipy.stats.boxcox_llf.html#scipy.stats.boxcox_llf "scipy.stats.boxcox_llf")(lmb,Â data,Â \*[,Â axis,Â keepdims,Â ...]) | The boxcox log-likelihood function. |
| [`yeojohnson`](generated/scipy.stats.yeojohnson.html#scipy.stats.yeojohnson "scipy.stats.yeojohnson")(x[,Â lmbda,Â nan\_policy]) | Return a dataset transformed by a Yeo-Johnson power transformation. |
| [`yeojohnson_normmax`](generated/scipy.stats.yeojohnson_normmax.html#scipy.stats.yeojohnson_normmax "scipy.stats.yeojohnson_normmax")(x[,Â brack,Â nan\_policy]) | Compute optimal Yeo-Johnson transform parameter. |
| [`yeojohnson_llf`](generated/scipy.stats.yeojohnson_llf.html#scipy.stats.yeojohnson_llf "scipy.stats.yeojohnson_llf")(lmb,Â data,Â \*[,Â axis,Â ...]) | The Yeo-Johnson log-likelihood function. |
| [`obrientransform`](generated/scipy.stats.obrientransform.html#scipy.stats.obrientransform "scipy.stats.obrientransform")(\*samples[,Â nan\_policy]) | Compute the O'Brien transform on input data (any number of arrays). |
| [`sigmaclip`](generated/scipy.stats.sigmaclip.html#scipy.stats.sigmaclip "scipy.stats.sigmaclip")(a[,Â low,Â high,Â nan\_policy]) | Perform iterative sigma-clipping of array elements. |
| [`trimboth`](generated/scipy.stats.trimboth.html#scipy.stats.trimboth "scipy.stats.trimboth")(a,Â proportiontocut[,Â axis]) | Slice off a proportion of items from both ends of an array. |
| [`trim1`](generated/scipy.stats.trim1.html#scipy.stats.trim1 "scipy.stats.trim1")(a,Â proportiontocut[,Â tail,Â axis]) | Slice off a proportion from ONE end of the passed array distribution. |
| [`zmap`](generated/scipy.stats.zmap.html#scipy.stats.zmap "scipy.stats.zmap")(scores,Â compare[,Â axis,Â ddof,Â nan\_policy]) | Calculate the relative z-scores. |
| [`zscore`](generated/scipy.stats.zscore.html#scipy.stats.zscore "scipy.stats.zscore")(a[,Â axis,Â ddof,Â nan\_policy]) | Compute the z score. |
| [`gzscore`](generated/scipy.stats.gzscore.html#scipy.stats.gzscore "scipy.stats.gzscore")(a,Â \*[,Â axis,Â ddof,Â nan\_policy]) | Compute the geometric standard score. |
### Statistical distances[#](#statistical-distances "Link to this heading")
|  |  |
| --- | --- |
| [`wasserstein_distance`](generated/scipy.stats.wasserstein_distance.html#scipy.stats.wasserstein_distance "scipy.stats.wasserstein_distance")(u\_values,Â v\_values[,Â ...]) | Compute the Wasserstein-1 distance between two 1D discrete distributions. |
| [`wasserstein_distance_nd`](generated/scipy.stats.wasserstein_distance_nd.html#scipy.stats.wasserstein_distance_nd "scipy.stats.wasserstein_distance_nd")(u\_values,Â v\_values) | Compute the Wasserstein-1 distance between two N-D discrete distributions. |
| [`energy_distance`](generated/scipy.stats.energy_distance.html#scipy.stats.energy_distance "scipy.stats.energy_distance")(u\_values,Â v\_values[,Â ...]) | Compute the energy distance between two 1D distributions. |
### Fitting / Survival Analysis[#](#fitting-survival-analysis "Link to this heading")
|  |  |
| --- | --- |
| [`fit`](generated/scipy.stats.fit.html#scipy.stats.fit "scipy.stats.fit")(dist,Â data[,Â bounds,Â guess,Â method,Â ...]) | Fit a discrete or continuous distribution to data. |
| [`ecdf`](generated/scipy.stats.ecdf.html#scipy.stats.ecdf "scipy.stats.ecdf")(sample) | Empirical cumulative distribution function of a sample. |
| [`logrank`](generated/scipy.stats.logrank.html#scipy.stats.logrank "scipy.stats.logrank")(x,Â y[,Â alternative]) | Compare the survival distributions of two samples via the logrank test. |
### Directional statistical functions[#](#directional-statistical-functions "Link to this heading")
|  |  |
| --- | --- |
| [`directional_stats`](generated/scipy.stats.directional_stats.html#scipy.stats.directional_stats "scipy.stats.directional_stats")(samples,Â \*[,Â axis,Â normalize]) | Computes sample statistics for directional data. |
| [`circmean`](generated/scipy.stats.circmean.html#scipy.stats.circmean "scipy.stats.circmean")(samples[,Â high,Â low,Â axis,Â ...]) | Compute the circular mean of a sample of angle observations. |
| [`circvar`](generated/scipy.stats.circvar.html#scipy.stats.circvar "scipy.stats.circvar")(samples[,Â high,Â low,Â axis,Â ...]) | Compute the circular variance of a sample of angle observations. |
| [`circstd`](generated/scipy.stats.circstd.html#scipy.stats.circstd "scipy.stats.circstd")(samples[,Â high,Â low,Â axis,Â ...]) | Compute the circular standard deviation of a sample of angle observations. |
### Sensitivity Analysis[#](#sensitivity-analysis "Link to this heading")
|  |  |
| --- | --- |
| [`sobol_indices`](generated/scipy.stats.sobol_indices.html#scipy.stats.sobol_indices "scipy.stats.sobol_indices")(\*,Â func,Â n[,Â dists,Â method,Â ...]) | Global sensitivity indices of Sobol'. |
### Plot-tests[#](#plot-tests "Link to this heading")
|  |  |
| --- | --- |
| [`ppcc_max`](generated/scipy.stats.ppcc_max.html#scipy.stats.ppcc_max "scipy.stats.ppcc_max")(x[,Â brack,Â dist]) | Calculate the shape parameter that maximizes the PPCC. |
| [`ppcc_plot`](generated/scipy.stats.ppcc_plot.html#scipy.stats.ppcc_plot "scipy.stats.ppcc_plot")(x,Â a,Â b[,Â dist,Â plot,Â N]) | Calculate and optionally plot probability plot correlation coefficient. |
| [`probplot`](generated/scipy.stats.probplot.html#scipy.stats.probplot "scipy.stats.probplot")(x[,Â sparams,Â dist,Â fit,Â plot,Â rvalue]) | Calculate quantiles for a probability plot, and optionally show the plot. |
| [`boxcox_normplot`](generated/scipy.stats.boxcox_normplot.html#scipy.stats.boxcox_normplot "scipy.stats.boxcox_normplot")(x,Â la,Â lb[,Â plot,Â N]) | Compute parameters for a Box-Cox normality plot, optionally show it. |
| [`yeojohnson_normplot`](generated/scipy.stats.yeojohnson_normplot.html#scipy.stats.yeojohnson_normplot "scipy.stats.yeojohnson_normplot")(x,Â la,Â lb[,Â plot,Â N]) | Compute parameters for a Yeo-Johnson normality plot, optionally show it. |
### Univariate and multivariate kernel density estimation[#](#univariate-and-multivariate-kernel-density-estimation "Link to this heading")
|  |  |
| --- | --- |
| [`gaussian_kde`](generated/scipy.stats.gaussian_kde.html#scipy.stats.gaussian_kde "scipy.stats.gaussian_kde")(dataset[,Â bw\_method,Â weights]) | Representation of a kernel-density estimate using Gaussian kernels. |
### Warnings / Errors used in [`scipy.stats`](#module-scipy.stats "scipy.stats")[#](#warnings-errors-used-in-scipy-stats "Link to this heading")
|  |  |
| --- | --- |
| [`DegenerateDataWarning`](generated/scipy.stats.DegenerateDataWarning.html#scipy.stats.DegenerateDataWarning "scipy.stats.DegenerateDataWarning")([msg]) | Warns when data is degenerate and results may not be reliable. |
| [`ConstantInputWarning`](generated/scipy.stats.ConstantInputWarning.html#scipy.stats.ConstantInputWarning "scipy.stats.ConstantInputWarning")([msg]) | Warns when all values in data are exactly equal. |
| [`NearConstantInputWarning`](generated/scipy.stats.NearConstantInputWarning.html#scipy.stats.NearConstantInputWarning "scipy.stats.NearConstantInputWarning")([msg]) | Warns when all values in data are nearly equal. |
| [`FitError`](generated/scipy.stats.FitError.html#scipy.stats.FitError "scipy.stats.FitError")([msg]) | Represents an error condition when fitting a distribution to data. |
### Result classes used in [`scipy.stats`](#module-scipy.stats "scipy.stats")[#](#result-classes-used-in-scipy-stats "Link to this heading")
Warning
These classes are private, but they are included here because instances
of them are returned by other statistical functions. User import and
instantiation is not supported.
* [Result classes](stats._result_classes.html)
  + [RelativeRiskResult](generated/scipy.stats._result_classes.RelativeRiskResult.html)
  + [BinomTestResult](generated/scipy.stats._result_classes.BinomTestResult.html)
  + [TukeyHSDResult](generated/scipy.stats._result_classes.TukeyHSDResult.html)
  + [DunnettResult](generated/scipy.stats._result_classes.DunnettResult.html)
  + [PearsonRResult](generated/scipy.stats._result_classes.PearsonRResult.html)
  + [FitResult](generated/scipy.stats._result_classes.FitResult.html)
  + [OddsRatioResult](generated/scipy.stats._result_classes.OddsRatioResult.html)
  + [TtestResult](generated/scipy.stats._result_classes.TtestResult.html)
  + [ECDFResult](generated/scipy.stats._result_classes.ECDFResult.html)
  + [EmpiricalDistributionFunction](generated/scipy.stats._result_classes.EmpiricalDistributionFunction.html)
[previous
sinc](generated/scipy.special.sinc.html "previous page")
[next
rv\_continuous](generated/scipy.stats.rv_continuous.html "next page")
On this page
* [Probability distributions](#probability-distributions)
  + [Continuous distributions](#continuous-distributions)
  + [Multivariate distributions](#multivariate-distributions)
  + [Discrete distributions](#discrete-distributions)
* [Summary statistics](#summary-statistics)
* [Frequency statistics](#frequency-statistics)
* [Hypothesis Tests and related functions](#hypothesis-tests-and-related-functions)
  + [One Sample Tests / Paired Sample Tests](#one-sample-tests-paired-sample-tests)
  + [Association/Correlation Tests](#association-correlation-tests)
  + [Independent Sample Tests](#independent-sample-tests)
  + [Resampling and Monte Carlo Methods](#resampling-and-monte-carlo-methods)
  + [Multiple Hypothesis Testing and Meta-Analysis](#multiple-hypothesis-testing-and-meta-analysis)
* [Random Variables](#random-variables)
* [Other statistical functionality](#other-statistical-functionality)
  + [Transformations](#transformations)
  + [Statistical distances](#statistical-distances)
  + [Fitting / Survival Analysis](#fitting-survival-analysis)
  + [Directional statistical functions](#directional-statistical-functions)
  + [Sensitivity Analysis](#sensitivity-analysis)
  + [Plot-tests](#plot-tests)
  + [Univariate and multivariate kernel density estimation](#univariate-and-multivariate-kernel-density-estimation)
  + [Warnings / Errors used in `scipy.stats`](#warnings-errors-used-in-scipy-stats)
  + [Result classes used in `scipy.stats`](#result-classes-used-in-scipy-stats)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/stats.contingency.html#module-scipy.stats.contingency -->
* [SciPy API](index.html)
* [Statistical functions (`scipy.stats`)](stats.html)
* Contingency table functions (`scipy.stats.contingency`)
# Contingency table functions ([`scipy.stats.contingency`](#module-scipy.stats.contingency "scipy.stats.contingency"))[#](#contingency-table-functions-scipy-stats-contingency "Link to this heading")
Functions for creating and analyzing contingency tables.
|  |  |
| --- | --- |
| [`chi2_contingency`](generated/scipy.stats.contingency.chi2_contingency.html#scipy.stats.contingency.chi2_contingency "scipy.stats.contingency.chi2_contingency")(observed[,Â correction,Â ...]) | Chi-square test of independence of variables in a contingency table. |
| [`relative_risk`](generated/scipy.stats.contingency.relative_risk.html#scipy.stats.contingency.relative_risk "scipy.stats.contingency.relative_risk")(exposed\_cases,Â exposed\_total,Â ...) | Compute the relative risk (also known as the risk ratio). |
| [`odds_ratio`](generated/scipy.stats.contingency.odds_ratio.html#scipy.stats.contingency.odds_ratio "scipy.stats.contingency.odds_ratio")(table,Â \*[,Â kind]) | Compute the odds ratio for a 2x2 contingency table. |
| [`crosstab`](generated/scipy.stats.contingency.crosstab.html#scipy.stats.contingency.crosstab "scipy.stats.contingency.crosstab")(\*args[,Â levels,Â sparse]) | Return table of counts for each possible unique combination in `*args`. |
| [`association`](generated/scipy.stats.contingency.association.html#scipy.stats.contingency.association "scipy.stats.contingency.association")(observed[,Â method,Â correction,Â ...]) | Calculates degree of association between two nominal variables. |
| [`expected_freq`](generated/scipy.stats.contingency.expected_freq.html#scipy.stats.contingency.expected_freq "scipy.stats.contingency.expected_freq")(observed) | Compute the expected frequencies from a contingency table. |
| [`margins`](generated/scipy.stats.contingency.margins.html#scipy.stats.contingency.margins "scipy.stats.contingency.margins")(a) | Return a list of the marginal sums of the array *a*. |
[previous
scale](generated/scipy.stats.qmc.scale.html "previous page")
[next
chi2\_contingency](generated/scipy.stats.contingency.chi2_contingency.html "next page")
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/stats.mstats.html#module-scipy.stats.mstats -->
* [SciPy API](index.html)
* [Statistical functions (`scipy.stats`)](stats.html)
* Statistical functions for masked arrays (`scipy.stats.mstats`)
# Statistical functions for masked arrays ([`scipy.stats.mstats`](#module-scipy.stats.mstats "scipy.stats.mstats"))[#](#statistical-functions-for-masked-arrays-scipy-stats-mstats "Link to this heading")
This module contains a large number of statistical functions that can
be used with masked arrays.
Most of these functions are similar to those in [`scipy.stats`](stats.html#module-scipy.stats "scipy.stats") but might
have small differences in the API or in the algorithm used. Since this
is a relatively new package, some API changes are still possible.
## Summary statistics[#](#summary-statistics "Link to this heading")
|  |  |
| --- | --- |
| [`describe`](generated/scipy.stats.mstats.describe.html#scipy.stats.mstats.describe "scipy.stats.mstats.describe")(a[,Â axis,Â ddof,Â bias]) | Computes several descriptive statistics of the passed array. |
| [`gmean`](generated/scipy.stats.mstats.gmean.html#scipy.stats.mstats.gmean "scipy.stats.mstats.gmean")(a[,Â axis,Â dtype,Â weights,Â nan\_policy,Â ...]) | Compute the weighted geometric mean along the specified axis. |
| [`hmean`](generated/scipy.stats.mstats.hmean.html#scipy.stats.mstats.hmean "scipy.stats.mstats.hmean")(a[,Â axis,Â dtype,Â weights,Â nan\_policy,Â ...]) | Calculate the weighted harmonic mean along the specified axis. |
| [`kurtosis`](generated/scipy.stats.mstats.kurtosis.html#scipy.stats.mstats.kurtosis "scipy.stats.mstats.kurtosis")(a[,Â axis,Â fisher,Â bias]) | Computes the kurtosis (Fisher or Pearson) of a dataset. |
| [`mode`](generated/scipy.stats.mstats.mode.html#scipy.stats.mstats.mode "scipy.stats.mstats.mode")(a[,Â axis]) | Returns an array of the modal (most common) value in the passed array. |
| [`mquantiles`](generated/scipy.stats.mstats.mquantiles.html#scipy.stats.mstats.mquantiles "scipy.stats.mstats.mquantiles")(a[,Â prob,Â alphap,Â betap,Â axis,Â limit]) | Computes empirical quantiles for a data array. |
| [`hdmedian`](generated/scipy.stats.mstats.hdmedian.html#scipy.stats.mstats.hdmedian "scipy.stats.mstats.hdmedian")(data[,Â axis,Â var]) | Returns the Harrell-Davis estimate of the median along the given axis. |
| [`hdquantiles`](generated/scipy.stats.mstats.hdquantiles.html#scipy.stats.mstats.hdquantiles "scipy.stats.mstats.hdquantiles")(data[,Â prob,Â axis,Â var]) | Computes quantile estimates with the Harrell-Davis method. |
| [`hdquantiles_sd`](generated/scipy.stats.mstats.hdquantiles_sd.html#scipy.stats.mstats.hdquantiles_sd "scipy.stats.mstats.hdquantiles_sd")(data[,Â prob,Â axis]) | The standard error of the Harrell-Davis quantile estimates by jackknife. |
| [`idealfourths`](generated/scipy.stats.mstats.idealfourths.html#scipy.stats.mstats.idealfourths "scipy.stats.mstats.idealfourths")(data[,Â axis]) | Returns an estimate of the lower and upper quartiles. |
| [`plotting_positions`](generated/scipy.stats.mstats.plotting_positions.html#scipy.stats.mstats.plotting_positions "scipy.stats.mstats.plotting_positions")(data[,Â alpha,Â beta]) | Returns plotting positions (or empirical percentile points) for the data. |
| [`meppf`](generated/scipy.stats.mstats.meppf.html#scipy.stats.mstats.meppf "scipy.stats.mstats.meppf")(data[,Â alpha,Â beta]) | Returns plotting positions (or empirical percentile points) for the data. |
| [`moment`](generated/scipy.stats.mstats.moment.html#scipy.stats.mstats.moment "scipy.stats.mstats.moment")(a[,Â moment,Â axis]) | Calculates the nth moment about the mean for a sample. |
| [`skew`](generated/scipy.stats.mstats.skew.html#scipy.stats.mstats.skew "scipy.stats.mstats.skew")(a[,Â axis,Â bias]) | Computes the skewness of a data set. |
| [`tmean`](generated/scipy.stats.mstats.tmean.html#scipy.stats.mstats.tmean "scipy.stats.mstats.tmean")(a[,Â limits,Â inclusive,Â axis]) | Compute the trimmed mean. |
| [`tvar`](generated/scipy.stats.mstats.tvar.html#scipy.stats.mstats.tvar "scipy.stats.mstats.tvar")(a[,Â limits,Â inclusive,Â axis,Â ddof]) | Compute the trimmed variance |
| [`tmin`](generated/scipy.stats.mstats.tmin.html#scipy.stats.mstats.tmin "scipy.stats.mstats.tmin")(a[,Â lowerlimit,Â axis,Â inclusive]) | Compute the trimmed minimum |
| [`tmax`](generated/scipy.stats.mstats.tmax.html#scipy.stats.mstats.tmax "scipy.stats.mstats.tmax")(a[,Â upperlimit,Â axis,Â inclusive]) | Compute the trimmed maximum |
| [`tsem`](generated/scipy.stats.mstats.tsem.html#scipy.stats.mstats.tsem "scipy.stats.mstats.tsem")(a[,Â limits,Â inclusive,Â axis,Â ddof]) | Compute the trimmed standard error of the mean. |
| [`variation`](generated/scipy.stats.mstats.variation.html#scipy.stats.mstats.variation "scipy.stats.mstats.variation")(a[,Â axis,Â ddof]) | Compute the coefficient of variation. |
| [`find_repeats`](generated/scipy.stats.mstats.find_repeats.html#scipy.stats.mstats.find_repeats "scipy.stats.mstats.find_repeats")(arr) | Find repeats in arr and return a tuple (repeats, repeat\_count). |
| [`sem`](generated/scipy.stats.mstats.sem.html#scipy.stats.mstats.sem "scipy.stats.mstats.sem")(a[,Â axis,Â ddof]) | Calculates the standard error of the mean of the input array. |
| [`trimmed_mean`](generated/scipy.stats.mstats.trimmed_mean.html#scipy.stats.mstats.trimmed_mean "scipy.stats.mstats.trimmed_mean")(a[,Â limits,Â inclusive,Â ...]) | Returns the trimmed mean of the data along the given axis. |
| [`trimmed_mean_ci`](generated/scipy.stats.mstats.trimmed_mean_ci.html#scipy.stats.mstats.trimmed_mean_ci "scipy.stats.mstats.trimmed_mean_ci")(data[,Â limits,Â inclusive,Â ...]) | Selected confidence interval of the trimmed mean along the given axis. |
| [`trimmed_std`](generated/scipy.stats.mstats.trimmed_std.html#scipy.stats.mstats.trimmed_std "scipy.stats.mstats.trimmed_std")(a[,Â limits,Â inclusive,Â ...]) | Returns the trimmed standard deviation of the data along the given axis. |
| [`trimmed_var`](generated/scipy.stats.mstats.trimmed_var.html#scipy.stats.mstats.trimmed_var "scipy.stats.mstats.trimmed_var")(a[,Â limits,Â inclusive,Â ...]) | Returns the trimmed variance of the data along the given axis. |
## Frequency statistics[#](#frequency-statistics "Link to this heading")
|  |  |
| --- | --- |
| [`scoreatpercentile`](generated/scipy.stats.mstats.scoreatpercentile.html#scipy.stats.mstats.scoreatpercentile "scipy.stats.mstats.scoreatpercentile")(data,Â per[,Â limit,Â ...]) | Calculate the score at the given 'per' percentile of the sequence a. |
## Correlation functions[#](#correlation-functions "Link to this heading")
|  |  |
| --- | --- |
| [`f_oneway`](generated/scipy.stats.mstats.f_oneway.html#scipy.stats.mstats.f_oneway "scipy.stats.mstats.f_oneway")(\*args) | Performs a 1-way ANOVA, returning an F-value and probability given any number of groups. |
| [`pearsonr`](generated/scipy.stats.mstats.pearsonr.html#scipy.stats.mstats.pearsonr "scipy.stats.mstats.pearsonr")(x,Â y) | Pearson correlation coefficient and p-value for testing non-correlation. |
| [`spearmanr`](generated/scipy.stats.mstats.spearmanr.html#scipy.stats.mstats.spearmanr "scipy.stats.mstats.spearmanr")(x[,Â y,Â use\_ties,Â axis,Â ...]) | Calculates a Spearman rank-order correlation coefficient and the p-value to test for non-correlation. |
| [`pointbiserialr`](generated/scipy.stats.mstats.pointbiserialr.html#scipy.stats.mstats.pointbiserialr "scipy.stats.mstats.pointbiserialr")(x,Â y) | Calculates a point biserial correlation coefficient and its p-value. |
| [`kendalltau`](generated/scipy.stats.mstats.kendalltau.html#scipy.stats.mstats.kendalltau "scipy.stats.mstats.kendalltau")(x,Â y[,Â use\_ties,Â use\_missing,Â ...]) | Computes Kendall's rank correlation tau on two variables *x* and *y*. |
| [`kendalltau_seasonal`](generated/scipy.stats.mstats.kendalltau_seasonal.html#scipy.stats.mstats.kendalltau_seasonal "scipy.stats.mstats.kendalltau_seasonal")(x) | Computes a multivariate Kendall's rank correlation tau, for seasonal data. |
| [`linregress`](generated/scipy.stats.mstats.linregress.html#scipy.stats.mstats.linregress "scipy.stats.mstats.linregress")(x[,Â y]) | Calculate a linear least-squares regression for two sets of measurements. |
| [`siegelslopes`](generated/scipy.stats.mstats.siegelslopes.html#scipy.stats.mstats.siegelslopes "scipy.stats.mstats.siegelslopes")(y[,Â x,Â method]) | Computes the Siegel estimator for a set of points (x, y). |
| [`theilslopes`](generated/scipy.stats.mstats.theilslopes.html#scipy.stats.mstats.theilslopes "scipy.stats.mstats.theilslopes")(y[,Â x,Â alpha,Â method]) | Computes the Theil-Sen estimator for a set of points (x, y). |
| [`sen_seasonal_slopes`](generated/scipy.stats.mstats.sen_seasonal_slopes.html#scipy.stats.mstats.sen_seasonal_slopes "scipy.stats.mstats.sen_seasonal_slopes")(x) | Computes seasonal Theil-Sen and Kendall slope estimators. |
## Statistical tests[#](#statistical-tests "Link to this heading")
|  |  |
| --- | --- |
| [`ttest_1samp`](generated/scipy.stats.mstats.ttest_1samp.html#scipy.stats.mstats.ttest_1samp "scipy.stats.mstats.ttest_1samp")(a,Â popmean[,Â axis,Â alternative]) | Calculates the T-test for the mean of ONE group of scores. |
| [`ttest_onesamp`](generated/scipy.stats.mstats.ttest_onesamp.html#scipy.stats.mstats.ttest_onesamp "scipy.stats.mstats.ttest_onesamp")(a,Â popmean[,Â axis,Â alternative]) | Calculates the T-test for the mean of ONE group of scores. |
| [`ttest_ind`](generated/scipy.stats.mstats.ttest_ind.html#scipy.stats.mstats.ttest_ind "scipy.stats.mstats.ttest_ind")(a,Â b[,Â axis,Â equal\_var,Â alternative]) | Calculates the T-test for the means of TWO INDEPENDENT samples of scores. |
| [`ttest_rel`](generated/scipy.stats.mstats.ttest_rel.html#scipy.stats.mstats.ttest_rel "scipy.stats.mstats.ttest_rel")(a,Â b[,Â axis,Â alternative]) | Calculates the T-test on TWO RELATED samples of scores, a and b. |
| [`chisquare`](generated/scipy.stats.mstats.chisquare.html#scipy.stats.mstats.chisquare "scipy.stats.mstats.chisquare")(f\_obs[,Â f\_exp,Â ddof,Â axis,Â ...]) | Perform Pearson's chi-squared test. |
| [`kstest`](generated/scipy.stats.mstats.kstest.html#scipy.stats.mstats.kstest "scipy.stats.mstats.kstest")(data1,Â data2[,Â args,Â alternative,Â method]) | Performs the Kolmogorov-Smirnov test for goodness of fit. |
| [`ks_2samp`](generated/scipy.stats.mstats.ks_2samp.html#scipy.stats.mstats.ks_2samp "scipy.stats.mstats.ks_2samp")(data1,Â data2[,Â alternative,Â method]) | Computes the Kolmogorov-Smirnov test on two samples. |
| [`ks_1samp`](generated/scipy.stats.mstats.ks_1samp.html#scipy.stats.mstats.ks_1samp "scipy.stats.mstats.ks_1samp")(x,Â cdf[,Â args,Â alternative,Â method]) | Computes the Kolmogorov-Smirnov test on one sample of masked values. |
| [`ks_twosamp`](generated/scipy.stats.mstats.ks_twosamp.html#scipy.stats.mstats.ks_twosamp "scipy.stats.mstats.ks_twosamp")(data1,Â data2[,Â alternative,Â method]) | Computes the Kolmogorov-Smirnov test on two samples. |
| [`mannwhitneyu`](generated/scipy.stats.mstats.mannwhitneyu.html#scipy.stats.mstats.mannwhitneyu "scipy.stats.mstats.mannwhitneyu")(x,Â y[,Â use\_continuity]) | Computes the Mann-Whitney statistic |
| [`rankdata`](generated/scipy.stats.mstats.rankdata.html#scipy.stats.mstats.rankdata "scipy.stats.mstats.rankdata")(data[,Â axis,Â use\_missing]) | Returns the rank (also known as order statistics) of each data point along the given axis. |
| [`kruskal`](generated/scipy.stats.mstats.kruskal.html#scipy.stats.mstats.kruskal "scipy.stats.mstats.kruskal")(\*samples) | Compute the Kruskal-Wallis H-test for independent samples |
| [`kruskalwallis`](generated/scipy.stats.mstats.kruskalwallis.html#scipy.stats.mstats.kruskalwallis "scipy.stats.mstats.kruskalwallis")(\*samples) | Compute the Kruskal-Wallis H-test for independent samples |
| [`friedmanchisquare`](generated/scipy.stats.mstats.friedmanchisquare.html#scipy.stats.mstats.friedmanchisquare "scipy.stats.mstats.friedmanchisquare")(\*args) | Friedman Chi-Square is a non-parametric, one-way within-subjects ANOVA. |
| [`brunnermunzel`](generated/scipy.stats.mstats.brunnermunzel.html#scipy.stats.mstats.brunnermunzel "scipy.stats.mstats.brunnermunzel")(x,Â y[,Â alternative,Â distribution]) | Compute the Brunner-Munzel test on samples x and y. |
| [`skewtest`](generated/scipy.stats.mstats.skewtest.html#scipy.stats.mstats.skewtest "scipy.stats.mstats.skewtest")(a[,Â axis,Â alternative]) | Tests whether the skew is different from the normal distribution. |
| [`kurtosistest`](generated/scipy.stats.mstats.kurtosistest.html#scipy.stats.mstats.kurtosistest "scipy.stats.mstats.kurtosistest")(a[,Â axis,Â alternative]) | Tests whether a dataset has normal kurtosis |
| [`normaltest`](generated/scipy.stats.mstats.normaltest.html#scipy.stats.mstats.normaltest "scipy.stats.mstats.normaltest")(a[,Â axis]) | Tests whether a sample differs from a normal distribution. |
## Transformations[#](#transformations "Link to this heading")
|  |  |
| --- | --- |
| [`obrientransform`](generated/scipy.stats.mstats.obrientransform.html#scipy.stats.mstats.obrientransform "scipy.stats.mstats.obrientransform")(\*args) | Computes a transform on input data (any number of columns). |
| [`trim`](generated/scipy.stats.mstats.trim.html#scipy.stats.mstats.trim "scipy.stats.mstats.trim")(a[,Â limits,Â inclusive,Â relative,Â axis]) | Trims an array by masking the data outside some given limits. |
| [`trima`](generated/scipy.stats.mstats.trima.html#scipy.stats.mstats.trima "scipy.stats.mstats.trima")(a[,Â limits,Â inclusive]) | Trims an array by masking the data outside some given limits. |
| [`trimmed_stde`](generated/scipy.stats.mstats.trimmed_stde.html#scipy.stats.mstats.trimmed_stde "scipy.stats.mstats.trimmed_stde")(a[,Â limits,Â inclusive,Â axis]) | Returns the standard error of the trimmed mean along the given axis. |
| [`trimr`](generated/scipy.stats.mstats.trimr.html#scipy.stats.mstats.trimr "scipy.stats.mstats.trimr")(a[,Â limits,Â inclusive,Â axis]) | Trims an array by masking some proportion of the data on each end. |
| [`trimtail`](generated/scipy.stats.mstats.trimtail.html#scipy.stats.mstats.trimtail "scipy.stats.mstats.trimtail")(data[,Â proportiontocut,Â tail,Â ...]) | Trims the data by masking values from one tail. |
| [`trimboth`](generated/scipy.stats.mstats.trimboth.html#scipy.stats.mstats.trimboth "scipy.stats.mstats.trimboth")(data[,Â proportiontocut,Â inclusive,Â ...]) | Trims the smallest and largest data values. |
| [`winsorize`](generated/scipy.stats.mstats.winsorize.html#scipy.stats.mstats.winsorize "scipy.stats.mstats.winsorize")(a[,Â limits,Â inclusive,Â inplace,Â ...]) | Returns a Winsorized version of the input array. |
| [`zmap`](generated/scipy.stats.mstats.zmap.html#scipy.stats.mstats.zmap "scipy.stats.mstats.zmap")(scores,Â compare[,Â axis,Â ddof,Â nan\_policy]) | Calculate the relative z-scores. |
| [`zscore`](generated/scipy.stats.mstats.zscore.html#scipy.stats.mstats.zscore "scipy.stats.mstats.zscore")(a[,Â axis,Â ddof,Â nan\_policy]) | Compute the z score. |
## Other[#](#other "Link to this heading")
|  |  |
| --- | --- |
| [`argstoarray`](generated/scipy.stats.mstats.argstoarray.html#scipy.stats.mstats.argstoarray "scipy.stats.mstats.argstoarray")(\*args) | Constructs a 2D array from a group of sequences. |
| [`count_tied_groups`](generated/scipy.stats.mstats.count_tied_groups.html#scipy.stats.mstats.count_tied_groups "scipy.stats.mstats.count_tied_groups")(x[,Â use\_missing]) | Counts the number of tied values. |
| [`msign`](generated/scipy.stats.mstats.msign.html#scipy.stats.mstats.msign "scipy.stats.mstats.msign")(x) | Returns the sign of x, or 0 if x is masked. |
| [`compare_medians_ms`](generated/scipy.stats.mstats.compare_medians_ms.html#scipy.stats.mstats.compare_medians_ms "scipy.stats.mstats.compare_medians_ms")(group\_1,Â group\_2[,Â axis]) | Compares the medians from two independent groups along the given axis. |
| [`median_cihs`](generated/scipy.stats.mstats.median_cihs.html#scipy.stats.mstats.median_cihs "scipy.stats.mstats.median_cihs")(data[,Â alpha,Â axis]) | Computes the alpha-level confidence interval for the median of the data. |
| [`mjci`](generated/scipy.stats.mstats.mjci.html#scipy.stats.mstats.mjci "scipy.stats.mstats.mjci")(data[,Â prob,Â axis]) | Returns the Maritz-Jarrett estimators of the standard error of selected experimental quantiles of the data. |
| [`mquantiles_cimj`](generated/scipy.stats.mstats.mquantiles_cimj.html#scipy.stats.mstats.mquantiles_cimj "scipy.stats.mstats.mquantiles_cimj")(data[,Â prob,Â alpha,Â axis]) | Computes the alpha confidence interval for the selected quantiles of the data, with Maritz-Jarrett estimators. |
| [`rsh`](generated/scipy.stats.mstats.rsh.html#scipy.stats.mstats.rsh "scipy.stats.mstats.rsh")(data[,Â points]) | Evaluates Rosenblatt's shifted histogram estimators for each data point. |
[previous
margins](generated/scipy.stats.contingency.margins.html "previous page")
[next
describe](generated/scipy.stats.mstats.describe.html "next page")
On this page
* [Summary statistics](#summary-statistics)
* [Frequency statistics](#frequency-statistics)
* [Correlation functions](#correlation-functions)
* [Statistical tests](#statistical-tests)
* [Transformations](#transformations)
* [Other](#other)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/stats.qmc.html#module-scipy.stats.qmc -->
* [SciPy API](index.html)
* [Statistical functions (`scipy.stats`)](stats.html)
* Quasi-Monte Carlo submodule (`scipy.stats.qmc`)
# Quasi-Monte Carlo submodule ([`scipy.stats.qmc`](#module-scipy.stats.qmc "scipy.stats.qmc"))[#](#quasi-monte-carlo-submodule-scipy-stats-qmc "Link to this heading")
This module provides Quasi-Monte Carlo generators and associated helper
functions.
## Quasi-Monte Carlo[#](#quasi-monte-carlo "Link to this heading")
### Engines[#](#engines "Link to this heading")
|  |  |
| --- | --- |
| [`QMCEngine`](generated/scipy.stats.qmc.QMCEngine.html#scipy.stats.qmc.QMCEngine "scipy.stats.qmc.QMCEngine")(d,Â \*[,Â optimization,Â rng,Â seed]) | A generic Quasi-Monte Carlo sampler class meant for subclassing. |
| [`Sobol`](generated/scipy.stats.qmc.Sobol.html#scipy.stats.qmc.Sobol "scipy.stats.qmc.Sobol")(d,Â \*[,Â scramble,Â bits,Â rng,Â ...]) | Engine for generating (scrambled) Sobol' sequences. |
| [`Halton`](generated/scipy.stats.qmc.Halton.html#scipy.stats.qmc.Halton "scipy.stats.qmc.Halton")(d,Â \*[,Â scramble,Â optimization,Â rng,Â seed]) | Halton sequence. |
| [`LatinHypercube`](generated/scipy.stats.qmc.LatinHypercube.html#scipy.stats.qmc.LatinHypercube "scipy.stats.qmc.LatinHypercube")(d,Â \*[,Â scramble,Â strength,Â ...]) | Latin hypercube sampling (LHS). |
| [`PoissonDisk`](generated/scipy.stats.qmc.PoissonDisk.html#scipy.stats.qmc.PoissonDisk "scipy.stats.qmc.PoissonDisk")(d,Â \*[,Â radius,Â hypersphere,Â ...]) | Poisson disk sampling. |
| [`MultinomialQMC`](generated/scipy.stats.qmc.MultinomialQMC.html#scipy.stats.qmc.MultinomialQMC "scipy.stats.qmc.MultinomialQMC")(pvals,Â n\_trials,Â \*[,Â engine,Â ...]) | QMC sampling from a multinomial distribution. |
| [`MultivariateNormalQMC`](generated/scipy.stats.qmc.MultivariateNormalQMC.html#scipy.stats.qmc.MultivariateNormalQMC "scipy.stats.qmc.MultivariateNormalQMC")(mean[,Â cov,Â cov\_root,Â ...]) | QMC sampling from a multivariate Normal \(N(\mu, \Sigma)\). |
### Helpers[#](#helpers "Link to this heading")
|  |  |
| --- | --- |
| [`discrepancy`](generated/scipy.stats.qmc.discrepancy.html#scipy.stats.qmc.discrepancy "scipy.stats.qmc.discrepancy")(sample,Â \*[,Â iterative,Â method,Â ...]) | Discrepancy of a given sample. |
| [`geometric_discrepancy`](generated/scipy.stats.qmc.geometric_discrepancy.html#scipy.stats.qmc.geometric_discrepancy "scipy.stats.qmc.geometric_discrepancy")(sample[,Â method,Â metric]) | Discrepancy of a given sample based on its geometric properties. |
| [`update_discrepancy`](generated/scipy.stats.qmc.update_discrepancy.html#scipy.stats.qmc.update_discrepancy "scipy.stats.qmc.update_discrepancy")(x\_new,Â sample,Â initial\_disc) | Update the centered discrepancy with a new sample. |
| [`scale`](generated/scipy.stats.qmc.scale.html#scipy.stats.qmc.scale "scipy.stats.qmc.scale")(sample,Â l\_bounds,Â u\_bounds,Â \*[,Â reverse]) | Sample scaling from unit hypercube to different bounds. |
## Introduction to Quasi-Monte Carlo[#](#introduction-to-quasi-monte-carlo "Link to this heading")
Quasi-Monte Carlo (QMC) methods [[1]](#rbfd6def8ed08-1), [[2]](#rbfd6def8ed08-2), [[3]](#rbfd6def8ed08-3) provide an
\(n \times d\) array of numbers in \([0,1]\). They can be used in
place of \(n\) points from the \(U[0,1]^{d}\) distribution. Compared to
random points, QMC points are designed to have fewer gaps and clumps. This is
quantified by discrepancy measures [[4]](#rbfd6def8ed08-4). From the Koksma-Hlawka
inequality [[5]](#rbfd6def8ed08-5) we know that low discrepancy reduces a bound on
integration error. Averaging a function \(f\) over \(n\) QMC points
can achieve an integration error close to \(O(n^{-1})\) for well
behaved functions [[2]](#rbfd6def8ed08-2).
Most QMC constructions are designed for special values of \(n\)
such as powers of 2 or large primes. Changing the sample
size by even one can degrade their performance, even their
rate of convergence [[6]](#rbfd6def8ed08-6). For instance \(n=100\) points may give less
accuracy than \(n=64\) if the method was designed for \(n=2^m\).
Some QMC constructions are extensible in \(n\): we can find
another special sample size \(n' > n\) and often an infinite
sequence of increasing special sample sizes. Some QMC
constructions are extensible in \(d\): we can increase the dimension,
possibly to some upper bound, and typically without requiring
special values of \(d\). Some QMC methods are extensible in
both \(n\) and \(d\).
QMC points are deterministic. That makes it hard to estimate the accuracy of
integrals estimated by averages over QMC points. Randomized QMC (RQMC) [[7]](#rbfd6def8ed08-7)
points are constructed so that each point is individually \(U[0,1]^{d}\)
while collectively the \(n\) points retain their low discrepancy.
One can make \(R\) independent replications of RQMC points to
see how stable a computation is. From \(R\) independent values,
a t-test (or bootstrap t-test [[8]](#rbfd6def8ed08-8)) then gives approximate confidence
intervals on the mean value. Some RQMC methods produce a
root mean squared error that is actually \(o(1/n)\) and smaller than
the rate seen in unrandomized QMC. An intuitive explanation is
that the error is a sum of many small ones and random errors
cancel in a way that deterministic ones do not. RQMC also
has advantages on integrands that are singular or, for other
reasons, fail to be Riemann integrable.
(R)QMC cannot beat Bahkvalovâs curse of dimension (see [[9]](#rbfd6def8ed08-9)). For
any random or deterministic method, there are worst case functions
that will give it poor performance in high dimensions. A worst
case function for QMC might be 0 at all n points but very
large elsewhere. Worst case analyses get very pessimistic
in high dimensions. (R)QMC can bring a great improvement over
MC when the functions on which it is used are not worst case.
For instance (R)QMC can be especially effective on integrands
that are well approximated by sums of functions of
some small number of their input variables at a time [[10]](#rbfd6def8ed08-10), [[11]](#rbfd6def8ed08-11).
That property is often a surprising finding about those functions.
Also, to see an improvement over IID MC, (R)QMC requires a bit of smoothness of
the integrand, roughly the mixed first order derivative in each direction,
\(\partial^d f/\partial x\_1 \cdots \partial x\_d\), must be integral.
For instance, a function that is 1 inside the hypersphere and 0 outside of it
has infinite variation in the sense of Hardy and Krause for any dimension
\(d = 2\).
Scrambled nets are a kind of RQMC that have some valuable robustness
properties [[12]](#rbfd6def8ed08-12). If the integrand is square integrable, they give variance
\(var\_{SNET} = o(1/n)\). There is a finite upper bound on
\(var\_{SNET} / var\_{MC}\) that holds simultaneously for every square
integrable integrand. Scrambled nets satisfy a strong law of large numbers
for \(f\) in \(L^p\) when \(p>1\). In some
special cases there is a central limit theorem [[13]](#rbfd6def8ed08-13). For smooth enough
integrands they can achieve RMSE nearly \(O(n^{-3})\). See [[12]](#rbfd6def8ed08-12)
for references about these properties.
The main kinds of QMC methods are lattice rules [[14]](#rbfd6def8ed08-14) and digital
nets and sequences [[2]](#rbfd6def8ed08-2), [[15]](#rbfd6def8ed08-15). The theories meet up in polynomial
lattice rules [[16]](#rbfd6def8ed08-16) which can produce digital nets. Lattice rules
require some form of search for good constructions. For digital
nets there are widely used default constructions.
The most widely used QMC methods are Sobolâ sequences [[17]](#rbfd6def8ed08-17).
These are digital nets. They are extensible in both \(n\) and \(d\).
They can be scrambled. The special sample sizes are powers
of 2. Another popular method are Halton sequences [[18]](#rbfd6def8ed08-18).
The constructions resemble those of digital nets. The earlier
dimensions have much better equidistribution properties than
later ones. There are essentially no special sample sizes.
They are not thought to be as accurate as Sobolâ sequences.
They can be scrambled. The nets of Faure [[19]](#rbfd6def8ed08-19) are also widely
used. All dimensions are equally good, but the special sample
sizes grow rapidly with dimension \(d\). They can be scrambled.
The nets of Niederreiter and Xing [[20]](#rbfd6def8ed08-20) have the best asymptotic
properties but have not shown good empirical performance [[21]](#rbfd6def8ed08-21).
Higher order digital nets are formed by a digit interleaving process
in the digits of the constructed points. They can achieve higher
levels of asymptotic accuracy given higher smoothness conditions on \(f\)
and they can be scrambled [[22]](#rbfd6def8ed08-22). There is little or no empirical work
showing the improved rate to be attained.
Using QMC is like using the entire period of a small random
number generator. The constructions are similar and so
therefore are the computational costs [[23]](#rbfd6def8ed08-23).
(R)QMC is sometimes improved by passing the points through
a bakerâs transformation (tent function) prior to using them.
That function has the form \(1-2|x-1/2|\). As \(x\) goes from 0 to
1, this function goes from 0 to 1 and then back. It is very
useful to produce a periodic function for lattice rules [[14]](#rbfd6def8ed08-14),
and sometimes it improves the convergence rate [[24]](#rbfd6def8ed08-24).
It is not straightforward to apply QMC methods to Markov
chain Monte Carlo (MCMC). We can think of MCMC as using
\(n=1\) point in \([0,1]^{d}\) for very large \(d\), with
ergodic results corresponding to \(d \to \infty\). One proposal is
in [[25]](#rbfd6def8ed08-25) and under strong conditions an improved rate of convergence
has been shown [[26]](#rbfd6def8ed08-26).
Returning to Sobolâ points: there are many versions depending
on what are called direction numbers. Those are the result of
searches and are tabulated. A very widely used set of direction
numbers come from [[27]](#rbfd6def8ed08-27). It is extensible in dimension up to
\(d=21201\).
### References[#](#references "Link to this heading")
[[1](#id1)]
Owen, Art B. âMonte Carlo Book: the Quasi-Monte Carlo parts.â 2019.
[2]
([1](#id2),[2](#id6),[3](#id17))
Niederreiter, Harald. âRandom number generation and quasi-Monte Carlo
methods.â Society for Industrial and Applied Mathematics, 1992.
[[3](#id3)]
Dick, Josef, Frances Y. Kuo, and Ian H. Sloan. âHigh-dimensional
integration: the quasi-Monte Carlo way.â Acta Numerica no. 22: 133, 2013.
[[4](#id4)]
Aho, A. V., C. Aistleitner, T. Anderson, K. Appel, V. Arnolâd, N.
Aronszajn, D. Asotsky et al. âW. Chen et al.(eds.), âA Panorama of
Discrepancy Theoryâ, Sringer International Publishing,
Switzerland: 679, 2014.
[[5](#id5)]
Hickernell, Fred J. âKoksma-Hlawka Inequality.â Wiley StatsRef:
Statistics Reference Online, 2014.
[[6](#id7)]
Owen, Art B. âOn dropping the first Sobolâ point.â [arXiv:2008.08051](https://arxiv.org/abs/2008.08051),
2020.
[[7](#id8)]
LâEcuyer, Pierre, and Christiane Lemieux. âRecent advances in randomized
quasi-Monte Carlo methods.â In Modeling uncertainty, pp. 419-474. Springer,
New York, NY, 2002.
[[8](#id9)]
DiCiccio, Thomas J., and Bradley Efron. âBootstrap confidence
intervals.â Statistical science: 189-212, 1996.
[[9](#id10)]
Dimov, Ivan T. âMonte Carlo methods for applied scientists.â World
Scientific, 2008.
[[10](#id11)]
Caflisch, Russel E., William J. Morokoff, and Art B. Owen. âValuation
of mortgage backed securities using Brownian bridges to reduce effective
dimension.â Journal of Computational Finance: no. 1 27-46, 1997.
[[11](#id12)]
Sloan, Ian H., and Henryk Wozniakowski. âWhen are quasi-Monte Carlo
algorithms efficient for high dimensional integrals?.â Journal of Complexity
14, no. 1 (1998): 1-33.
[12]
([1](#id13),[2](#id15))
Owen, Art B., and Daniel Rudolf, âA strong law of large numbers for
scrambled net integration.â SIAM Review, to appear.
[[13](#id14)]
Loh, Wei-Liem. âOn the asymptotic distribution of scrambled net
quadrature.â The Annals of Statistics 31, no. 4: 1282-1324, 2003.
[14]
([1](#id16),[2](#id27))
Sloan, Ian H. and S. Joe. âLattice methods for multiple integration.â
Oxford University Press, 1994.
[[15](#id18)]
Dick, Josef, and Friedrich Pillichshammer. âDigital nets and sequences:
discrepancy theory and quasi-Monte Carlo integration.â Cambridge University
Press, 2010.
[[16](#id19)]
Dick, Josef, F. Kuo, Friedrich Pillichshammer, and I. Sloan.
âConstruction algorithms for polynomial lattice rules for multivariate
integration.â Mathematics of computation 74, no. 252: 1895-1921, 2005.
[[17](#id20)]
Sobolâ, Ilâya Meerovich. âOn the distribution of points in a cube and
the approximate evaluation of integrals.â Zhurnal Vychislitelânoi Matematiki
i Matematicheskoi Fiziki 7, no. 4: 784-802, 1967.
[[18](#id21)]
Halton, John H. âOn the efficiency of certain quasi-random sequences of
points in evaluating multi-dimensional integrals.â Numerische Mathematik 2,
no. 1: 84-90, 1960.
[[19](#id22)]
Faure, Henri. âDiscrepance de suites associees a un systeme de
numeration (en dimension s).â Acta arithmetica 41, no. 4: 337-351, 1982.
[[20](#id23)]
Niederreiter, Harold, and Chaoping Xing. âLow-discrepancy sequences and
global function fields with many rational places.â Finite Fields and their
applications 2, no. 3: 241-273, 1996.
[[21](#id24)]
Hong, Hee Sun, and Fred J. Hickernell. âAlgorithm 823: Implementing
scrambled digital sequences.â ACM Transactions on Mathematical Software
(TOMS) 29, no. 2: 95-109, 2003.
[[22](#id25)]
Dick, Josef. âHigher order scrambled digital nets achieve the optimal
rate of the root mean square error for smooth integrands.â The Annals of
Statistics 39, no. 3: 1372-1398, 2011.
[[23](#id26)]
Niederreiter, Harald. âMultidimensional numerical integration using
pseudorandom numbers.â In Stochastic Programming 84 Part I, pp. 17-38.
Springer, Berlin, Heidelberg, 1986.
[[24](#id28)]
Hickernell, Fred J. âObtaining O (N-2+e) Convergence for Lattice
Quadrature Rules.â In Monte Carlo and Quasi-Monte Carlo Methods 2000,
pp. 274-289. Springer, Berlin, Heidelberg, 2002.
[[25](#id29)]
Owen, Art B., and Seth D. Tribble. âA quasi-Monte Carlo Metropolis
algorithm.â Proceedings of the National Academy of Sciences 102,
no. 25: 8844-8849, 2005.
[[26](#id30)]
Chen, Su. âConsistency and convergence rate of Markov chain quasi Monte
Carlo with examples.â PhD diss., Stanford University, 2011.
[[27](#id31)]
Joe, Stephen, and Frances Y. Kuo. âConstructing Sobol sequences with
better two-dimensional projections.â SIAM Journal on Scientific Computing
30, no. 5: 2635-2654, 2008.
[previous
log](generated/scipy.stats.log.html "previous page")
[next
QMCEngine](generated/scipy.stats.qmc.QMCEngine.html "next page")
On this page
* [Quasi-Monte Carlo](#quasi-monte-carlo)
  + [Engines](#engines)
  + [Helpers](#helpers)
* [Introduction to Quasi-Monte Carlo](#introduction-to-quasi-monte-carlo)
  + [References](#references)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/stats.sampling.html#module-scipy.stats.sampling -->
* [SciPy API](index.html)
* [Statistical functions (`scipy.stats`)](stats.html)
* Random Number Generators (`scipy.stats.sampling`)
# Random Number Generators ([`scipy.stats.sampling`](#module-scipy.stats.sampling "scipy.stats.sampling"))[#](#random-number-generators-scipy-stats-sampling "Link to this heading")
This module contains a collection of random number generators to sample
from univariate continuous and discrete distributions. It uses the
implementation of a C library called âUNU.RANâ. The only exception is
RatioUniforms, which is a pure Python implementation of the
Ratio-of-Uniforms method.
## Generators Wrapped[#](#generators-wrapped "Link to this heading")
### For continuous distributions[#](#for-continuous-distributions "Link to this heading")
|  |  |
| --- | --- |
| [`NumericalInverseHermite`](generated/scipy.stats.sampling.NumericalInverseHermite.html#scipy.stats.sampling.NumericalInverseHermite "scipy.stats.sampling.NumericalInverseHermite")(dist,Â \*[,Â domain,Â ...]) | Hermite interpolation based INVersion of CDF (HINV). |
| [`NumericalInversePolynomial`](generated/scipy.stats.sampling.NumericalInversePolynomial.html#scipy.stats.sampling.NumericalInversePolynomial "scipy.stats.sampling.NumericalInversePolynomial")(dist,Â \*[,Â mode,Â ...]) | Polynomial interpolation based INVersion of CDF (PINV). |
| [`TransformedDensityRejection`](generated/scipy.stats.sampling.TransformedDensityRejection.html#scipy.stats.sampling.TransformedDensityRejection "scipy.stats.sampling.TransformedDensityRejection")(dist,Â \*[,Â mode,Â ...]) | Transformed Density Rejection (TDR) Method. |
| [`SimpleRatioUniforms`](generated/scipy.stats.sampling.SimpleRatioUniforms.html#scipy.stats.sampling.SimpleRatioUniforms "scipy.stats.sampling.SimpleRatioUniforms")(dist,Â \*[,Â mode,Â ...]) | Simple Ratio-of-Uniforms (SROU) Method. |
| [`RatioUniforms`](generated/scipy.stats.sampling.RatioUniforms.html#scipy.stats.sampling.RatioUniforms "scipy.stats.sampling.RatioUniforms")(pdf,Â \*,Â umax,Â vmin,Â vmax[,Â c,Â ...]) | Generate random samples from a probability density function using the ratio-of-uniforms method. |
### For discrete distributions[#](#for-discrete-distributions "Link to this heading")
|  |  |
| --- | --- |
| [`DiscreteAliasUrn`](generated/scipy.stats.sampling.DiscreteAliasUrn.html#scipy.stats.sampling.DiscreteAliasUrn "scipy.stats.sampling.DiscreteAliasUrn")(dist,Â \*[,Â domain,Â ...]) | Discrete Alias-Urn Method. |
| [`DiscreteGuideTable`](generated/scipy.stats.sampling.DiscreteGuideTable.html#scipy.stats.sampling.DiscreteGuideTable "scipy.stats.sampling.DiscreteGuideTable")(dist,Â \*[,Â domain,Â ...]) | Discrete Guide Table method. |
### Warnings / Errors used in [`scipy.stats.sampling`](#module-scipy.stats.sampling "scipy.stats.sampling")[#](#warnings-errors-used-in-scipy-stats-sampling "Link to this heading")
|  |  |
| --- | --- |
| [`UNURANError`](generated/scipy.stats.sampling.UNURANError.html#scipy.stats.sampling.UNURANError "scipy.stats.sampling.UNURANError") | Raised when an error occurs in the UNU.RAN library. |
## Generators for pre-defined distributions[#](#generators-for-pre-defined-distributions "Link to this heading")
To easily apply the above methods for some of the continuous distributions
in [`scipy.stats`](stats.html#module-scipy.stats "scipy.stats"), the following functionality can be used:
|  |  |
| --- | --- |
| [`FastGeneratorInversion`](generated/scipy.stats.sampling.FastGeneratorInversion.html#scipy.stats.sampling.FastGeneratorInversion "scipy.stats.sampling.FastGeneratorInversion")(dist,Â \*[,Â domain,Â ...]) | Fast sampling by numerical inversion of the CDF for a large class of continuous distributions in [`scipy.stats`](stats.html#module-scipy.stats "scipy.stats"). |
[previous
rsh](generated/scipy.stats.mstats.rsh.html "previous page")
[next
NumericalInverseHermite](generated/scipy.stats.sampling.NumericalInverseHermite.html "next page")
On this page
* [Generators Wrapped](#generators-wrapped)
  + [For continuous distributions](#for-continuous-distributions)
  + [For discrete distributions](#for-discrete-distributions)
  + [Warnings / Errors used in `scipy.stats.sampling`](#warnings-errors-used-in-scipy-stats-sampling)
* [Generators for pre-defined distributions](#generators-for-pre-defined-distributions)
---
<!-- Source: https://docs.scipy.org/doc/scipy/tutorial/thread_safety.html -->
* [SciPy User Guide](index.html)
* Thread Safety in SciPy
# Thread Safety in SciPy[#](#thread-safety-in-scipy "Link to this heading")
SciPy supports use in a multithreaded context via the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "(in Python v3.14)") module in
the standard library. Many SciPy operations release the GIL, as does NumPy (and
a lot of SciPy functionality is implemented as calls to NumPy functions) - so
unlike many situations in Python, it is possible to improve parallel
performance by exploiting multithreaded parallelism in Python.
The easiest performance gains happen when each worker thread owns its own array
or set of array objects, with no data directly shared between threads. Threads
that spend most of their time in low-level code will typically run in parallel.
It is possible to share NumPy arrays between threads, but extreme care must be
taken to avoid creating thread safety issues when mutating arrays that are
shared between multiple threads - please see the NumPy documentation on thread
safety for more details. SciPy functions will not mutate arrays that the user
passes in, unless a function explicitly documents that it will do so (which is
rare). Hence calling SciPy functions in a threaded fashion on the same NumPy array
is safe.
While most of SciPy consists of *functions*, more care has to be taken with
*classes* and *data structures*.
Classes that have state, such as some of the integration and interpolation
objects in [`scipy.integrate`](../reference/integrate.html#module-scipy.integrate "scipy.integrate") and [`scipy.interpolate`](../reference/interpolate.html#module-scipy.interpolate "scipy.interpolate"), are typically robust
against being called in parallel. They either accept parallel calls or raise an
informative error. For example, [`scipy.integrate.ode`](../reference/generated/scipy.integrate.ode.html#scipy.integrate.ode "scipy.integrate.ode") may raise an
`IntegratorConcurrencyError` for integration methods that do not support
parallel execution.
The KDTree provided by [`scipy.spatial`](../reference/spatial.html#module-scipy.spatial "scipy.spatial") is also thread-safe, because there is no
interface to mutate the KDTree after creating it. It is safe to query the KDTree
simultaneously from multiple threads.
SciPy offers a couple of data structures, namely sparse arrays and matrices in
[`scipy.sparse`](../reference/sparse.html#module-scipy.sparse "scipy.sparse"), that are *mutable*. These data structures are *currently not
thread-safe*. Please avoid in particular operations that mutate a data
structure, like using item or slice assignment on sparse arrays, while the data
is shared across multiple threads. That may result in data corruption, crashes,
or other unwanted behavior. If you must support shared mutation of these
objects, take care to synchronize access or ensure there is no possibility of
shared mutation. See the sections in the Python free-threading guide on
[copy-on-write](https://py-free-threading.github.io/porting/#copy-on-write)
and [locks](https://py-free-threading.github.io/porting/#locking) for more
guidance on ways to deal with thread-unsafe objects in Python.
Note that operations that *do not* release the GIL will see no performance
gains from use of the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "(in Python v3.14)") module, and instead might be better served
with [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "(in Python v3.14)"). However, see below for details about SciPyâs support
for the free-threaded build, which does not have this limitation.
## Free-threaded Python[#](#free-threaded-python "Link to this heading")
Added in version 1.15.0.
Starting with SciPy 1.15.0 and CPython 3.13, SciPy has experimental support
for Python runtimes with the GIL disabled on all platforms. See
<https://py-free-threading.github.io> for more information about installing and
using free-threaded Python.
Because free-threaded Python does not have a global interpreter lock (GIL) to
serialize access to Python objects, there are more opportunities for threads to
mutate shared state and create thread safety issues. All SciPy functionality is
tested for usage from parallel threads, however we expect there to be issues
that are as yet undiscovered - if you run into a problem, please check the
[GitHub issues with the free-threading label](https://github.com/scipy/scipy/issues?q=is%3Aopen+is%3Aissue+label%3Afree-threading)
and open a new issue if one does not exist yet for the function that is
misbehaving.
[previous
Security](security.html "previous page")
[next
SciPy API](../reference/index.html "next page")
On this page
* [Free-threaded Python](#free-threaded-python)
---
<!-- Source: https://docs.scipy.org/doc/scipy/reference/main_namespace.html -->
* [SciPy API](index.html)
* The main SciPy namespace
# The main SciPy namespace[#](#the-main-scipy-namespace "Link to this heading")
The main `scipy` namespace has very few objects in it by design. Only show
generical functionality related to testing, build info and versioning, and one
class ([`LowLevelCallable`](generated/scipy.LowLevelCallable.html#scipy.LowLevelCallable "scipy.LowLevelCallable")) that didnât fit in one of the
submodules, are present:
|  |  |
| --- | --- |
| [`LowLevelCallable`](generated/scipy.LowLevelCallable.html#scipy.LowLevelCallable "scipy.LowLevelCallable")(function[,Â user\_data,Â ...]) | Low-level callback function. |
| [`show_config`](generated/scipy.show_config.html#scipy.show_config "scipy.show_config")([mode]) | Show libraries and system information on which SciPy was built and is being used |
| [`test`](generated/scipy.test.html#scipy.test "scipy.test") | Run tests for this namespace |
The one public attribute is:
|  |  |
| --- | --- |
| `__version__` | SciPy version string |
## Submodules[#](#submodules "Link to this heading")
|  |  |
| --- | --- |
| [`cluster`](cluster.html#module-scipy.cluster "scipy.cluster") | Clustering functionality |
| [`constants`](constants.html#module-scipy.constants "scipy.constants") | Physical and mathematical constants and units |
| [`datasets`](datasets.html#module-scipy.datasets "scipy.datasets") | Load SciPy datasets |
| [`fft`](fft.html#module-scipy.fft "scipy.fft") | Discrete Fourier and related transforms |
| [`fftpack`](fftpack.html#module-scipy.fftpack "scipy.fftpack") | Discrete Fourier transforms (legacy) |
| [`integrate`](integrate.html#module-scipy.integrate "scipy.integrate") | Numerical integration and ODEs |
| [`interpolate`](interpolate.html#module-scipy.interpolate "scipy.interpolate") | Interpolation |
| [`io`](io.html#module-scipy.io "scipy.io") | Scientific data format reading and writing |
| [`linalg`](linalg.html#module-scipy.linalg "scipy.linalg") | Linear algebra functionality |
| *misc* | Utility routines (deprecated) |
| [`ndimage`](ndimage.html#module-scipy.ndimage "scipy.ndimage") | N-dimensional image processing and interpolation |
| [`odr`](odr.html#module-scipy.odr "scipy.odr") | Orthogonal distance regression |
| [`optimize`](optimize.html#module-scipy.optimize "scipy.optimize") | Numerical optimization |
| [`signal`](signal.html#module-scipy.signal "scipy.signal") | Signal processing |
| [`sparse`](sparse.html#module-scipy.sparse "scipy.sparse") | Sparse arrays, linear algebra and graph algorithms |
| [`spatial`](spatial.html#module-scipy.spatial "scipy.spatial") | Spatial data structures and algorithms |
| [`special`](special.html#module-scipy.special "scipy.special") | Special functions |
| [`stats`](stats.html#module-scipy.stats "scipy.stats") | Statistical functions |
[previous
SciPy API](index.html "previous page")
[next
LowLevelCallable](generated/scipy.LowLevelCallable.html "next page")
On this page
* [Submodules](#submodules)