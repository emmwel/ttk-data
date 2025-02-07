# Welcome to the TTK Examples!

This website hosts a list of data analysis pipelines exemplifying the usage of [TTK](https://topology-tool-kit.github.io/) with
[ParaView](http://paraview.org) and its Python API `pvpython`.

This website is targeting novice users who are not power users of [ParaView](http://paraview.org) but who would like to get started with topological data analysis with [TTK](https://topology-tool-kit.github.io/) in Python.

Each example includes:

- a screenshot (or a tutorial video)
- a short description
- the command line to reproduce the example with [ParaView](http://paraview.org)
- the corresponding Python code, to:
    - load the input data 
    - execute the analysis pipeline
    - store the output to disk (for later analysis or visualization, e.g. with [ParaView](http://paraview.org))
- a description of the inputs and outputs
- pointers to the corresponding C++/Python documentation

This documentation assumes a default TTK installation (with the `pvpython` API support enabled) and that the repository [ttk-data](https://github.com/topology-tool-kit/ttk-data) has been downloaded locally.

## List of available examples

### Scalar data

| Name | Screenshot |
|:-:|:-:|
| [Dragon](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/dragon.jpg) |
| [Morse persistence](morsePersistence/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/morsePersistence.jpg) |
| [Built-in example 1](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/builtinExample1.jpg) |
| [Interaction site](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/interactionSites.jpg) |
| [Viscous fingering](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/viscousFingering.jpg) |
| [Morse molecule](morseMolecule/) |![ExampleImage](https://topology-tool-kit.github.io/img/gallery/morseMolecule.jpg) |
| [Tectonic puzzle](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/geology.jpg) |
| [Ocean vortices](dragon/) | !![ExampleImage](https://topology-tool-kit.github.io/img/gallery/climate.jpg) |
| [Contour around point](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/contourAroundPoint.jpg) |
| [CT bones](ctBones/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/ctBones.jpg) |
| [Tribute](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/tribute.jpg) |
| [Image processing](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/imageProcessing.jpg) |
| [Persistence driven compression](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceDrivenCompression.jpg) |
| [Morse-Smale quadrangulation](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/morseSmaleQuadrangulation.jpg) |

### Bivariate scalar data

| Name | Screenshot |
|:-:|:-:|
| [Built-in example 2](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/builtinExample2.jpg) |
| [Bivariate toy](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/bivariateToy.jpg) |
| [Bivariate toy CSP peeling](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/bivariateToyCspPeeling.jpg) |
| [Mechanical](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/mechanical.jpg) |

### Uncertain scalar data

| Name | Screenshot |
|:-:|:-:|
| [Built-in example 3](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/builtinExample3.jpg) |
| [Uncertain starting vortex](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/uncertainStartingVortex.jpg) |

### Time-varying scalar data

| Name | Screenshot |
|:-:|:-:|
| [Time tracking](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/timeTracking.jpeg) |
| [Merge tree feature tracking](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/mergeTreeFeatureTracking.jpg) |
| [Merge tree temporal reduction](mergeTreeTemporalReduction/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/mergeTreeTemporalReduction.jpg) |
| [Nested tracking graph](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/nestedTrackingGraph.jpg) |

### Ensemble scalar data

| Name | Screenshot |
|:-:|:-:|
| [Persistence diagram distance](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceDiagramDistance.jpg) |
| [Persistence diagram clustering](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceDiagramClustering.jpg) |
| [Merge tree clustering](mergeTreeClustering/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/mergeTreeClustering.jpg) |
| [Contour tree alignment](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/contourTreeAlignment.jpg) |

### High-dimensional / point cloud data

| Name | Screenshot |
|:-:|:-:|
| [Persistence clustering gallery](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClusteringGallery.jpeg) |
| [Persistence clustering0](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering0.jpeg) |
| [Persistence clustering1](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering1.jpeg) |
| [Persistence clustering2](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering2.jpeg) |
| [Persistence clustering3](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering3.jpeg) |
| [Persistence clustering4](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/persistenceClustering4.jpeg) |
| [Karhunen-Love Digits 64-Dimensions](karhunenLoveDigits64Dimensions/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/karhunenLoveDigits64Dimensions.jpg) |
| [1-manifold learning](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/1manifoldLearning.jpeg) |
| [1-manifold learning circles ](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/1manifoldLearningCircles.jpeg) |
| [2-manifold learning](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/2manifoldLearning.jpeg) |

### In-situ features

| Name | Screenshot |
|:-:|:-:|
| [Geometry approximation](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/geometryApproximation.jpg) |
| [Cinema darkroom](dragon/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/cinemaDarkroom.jpg) |

### Misc features

| Name | Screenshot |
|:-:|:-:|
| [Manifold checks](manifoldCheck/) | ![ExampleImage](https://topology-tool-kit.github.io/img/gallery/manifoldCheck.jpg) |

