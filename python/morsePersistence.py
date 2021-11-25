#!/usr/bin/env python

from paraview.simple import *

# create a new 'Plane'
plane1 = Plane(registrationName='Plane1')
plane1.XResolution = 300
plane1.YResolution = 300

# create a new 'Tetrahedralize'
tetrahedralize2 = Tetrahedralize(registrationName='Tetrahedralize2', Input=plane1)

# create a new 'Random Attributes'
randomAttributes1 = RandomAttributes(registrationName='RandomAttributes1', Input=tetrahedralize2)
randomAttributes1.DataType = 'Float'
randomAttributes1.ComponentRange = [0.0, 1.0]
randomAttributes1.GeneratePointScalars = 1
randomAttributes1.GenerateCellVectors = 0

# create a new 'TTK ScalarFieldSmoother'
tTKScalarFieldSmoother1 = TTKScalarFieldSmoother(registrationName='TTKScalarFieldSmoother1', Input=randomAttributes1)
tTKScalarFieldSmoother1.ScalarField = ['POINTS', 'RandomPointScalars']
tTKScalarFieldSmoother1.IterationNumber = 6
tTKScalarFieldSmoother1.MaskField = ['POINTS', '']

# create a new 'Calculator'
sine = Calculator(registrationName='Sine', Input=tTKScalarFieldSmoother1)
sine.ResultArrayName = 'Sine'
sine.Function = 'sin(20*coordsX+1.5)+sin(20*coordsY+1.5)'

# create a new 'Calculator'
distanceField = Calculator(registrationName='DistanceField', Input=sine)
distanceField.ResultArrayName = 'DistanceField'
distanceField.Function = '-sqrt(coordsX*coordsX+coordsY*coordsY)'

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=distanceField)
calculator1.ResultArrayName = 'Blend'
calculator1.Function = 'Sine+5*DistanceField+5*RandomPointScalars'

# create a new 'Extract Surface'
extractSurface6 = ExtractSurface(registrationName='ExtractSurface6', Input=calculator1)

# create a new 'Warp By Scalar'
warpByScalar1 = WarpByScalar(registrationName='WarpByScalar1', Input=extractSurface6)
warpByScalar1.Scalars = ['POINTS', 'Blend']
warpByScalar1.ScaleFactor = 0.05

# create a new 'TTK PersistenceCurve'
tTKPersistenceCurve1 = TTKPersistenceCurve(registrationName='TTKPersistenceCurve1', Input=warpByScalar1)
tTKPersistenceCurve1.ScalarField = ['POINTS', 'Blend']
tTKPersistenceCurve1.InputOffsetField = ['POINTS', '']

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=warpByScalar1)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'Blend']
tTKPersistenceDiagram1.InputOffsetField = ['POINTS', '']

# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=tTKPersistenceDiagram1)
threshold2.Scalars = ['CELLS', 'PairIdentifier']
threshold2.ThresholdRange = [-1.0, -0.1]

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.ThresholdRange = [0.0, 100000.0]

# create a new 'Threshold'
persistenceThreshold = Threshold(registrationName='PersistenceThreshold', Input=threshold1)
persistenceThreshold.Scalars = ['CELLS', 'Persistence']
persistenceThreshold.ThresholdRange = [0.7, 10000.0]

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(registrationName='TTKTopologicalSimplification1', Domain=warpByScalar1,
    Constraints=persistenceThreshold)
tTKTopologicalSimplification1.ScalarField = ['POINTS', 'Blend']
tTKTopologicalSimplification1.InputOffsetField = ['POINTS', '']
tTKTopologicalSimplification1.VertexIdentifierField = ['POINTS', '']

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(registrationName='TTKMorseSmaleComplex1', Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = ['POINTS', 'Blend']
tTKMorseSmaleComplex1.OffsetField = ['POINTS', 'OutputOffsetScalarField']
tTKMorseSmaleComplex1.SaddleConnectors = 0

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Extract Surface'
extractSurface5 = ExtractSurface(registrationName='ExtractSurface5', Input=OutputPort(tTKMorseSmaleComplex1_1,1))

# create a new 'Tube'
tube3 = Tube(registrationName='Tube3', Input=extractSurface5)
tube3.Scalars = ['POINTS', 'CellDimension']
tube3.Vectors = ['POINTS', '']
tube3.Radius = 0.005

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints2 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints2', Input=tTKMorseSmaleComplex1)
tTKIcospheresFromPoints2.Radius = 0.02

# find source
tTKMorseSmaleComplex1_2 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(registrationName='CleantoGrid1', Input=OutputPort(tTKMorseSmaleComplex1_2,3))

# create a new 'Extract Surface'
extractSurface4 = ExtractSurface(registrationName='ExtractSurface4', Input=cleantoGrid1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals2 = GenerateSurfaceNormals(registrationName='GenerateSurfaceNormals2', Input=extractSurface4)

# save the ouput
SaveData('PersistenceDiagram.vtu', tTKPersistenceDiagram1)
SaveData('PersistenceCurve.csv', OutputPort(tTKPersistenceCurve1, 3))
SaveData('MorseComplexeCriticalPoints.vtp', tTKIcospheresFromPoints2)
SaveData('MorseComplexeEdge.vtp', tube3)
SaveData('MorseComplexeSurface.vtp', generateSurfaceNormals2)
