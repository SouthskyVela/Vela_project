'# MWS Version: Version 2025.2 - Dec 16 2024 - ACIS 34.0.1 -

'# length = mm
'# frequency = GHz
'# time = ns
'# frequency range: fmin = 1.410 fmax = 1.430
'# created = '[VERSION]2025.2|34.0.1|20241216[/VERSION]


'@ use template: Antenna - Reflector.cfg

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
'set the units
With Units
    .SetUnit "Length", "mm"
    .SetUnit "Frequency", "GHz"
    .SetUnit "Voltage", "V"
    .SetUnit "Resistance", "Ohm"
    .SetUnit "Inductance", "nH"
    .SetUnit "Temperature",  "degC"
    .SetUnit "Time", "ns"
    .SetUnit "Current", "A"
    .SetUnit "Conductance", "S"
    .SetUnit "Capacitance", "pF"
End With

ThermalSolver.AmbientTemperature "0"

'----------------------------------------------------------------------------

Plot.DrawBox True

With Background
     .Type "Normal"
     .Epsilon "1.0"
     .Mu "1.0"
     .XminSpace "0.0"
     .XmaxSpace "0.0"
     .YminSpace "0.0"
     .YmaxSpace "0.0"
     .ZminSpace "0.0"
     .ZmaxSpace "0.0"
End With

With Boundary
     .Xmin "expanded open"
     .Xmax "expanded open"
     .Ymin "expanded open"
     .Ymax "expanded open"
     .Zmin "expanded open"
     .Zmax "expanded open"
     .Xsymmetry "none"
     .Ysymmetry "none"
     .Zsymmetry "none"
End With

' switch on FD-TET setting for accurate farfields

FDSolver.ExtrudeOpenBC "True"

Mesh.FPBAAvoidNonRegUnite "True"
Mesh.ConsiderSpaceForLowerMeshLimit "False"
Mesh.MinimumStepNumber "5"

With MeshSettings
     .SetMeshType "Hex"
     .Set "RatioLimitGeometry", "20"
End With

With MeshSettings
     .SetMeshType "HexTLM"
     .Set "RatioLimitGeometry", "20"
End With

PostProcess1D.ActivateOperation "vswr", "true"
PostProcess1D.ActivateOperation "yz-matrices", "true"

With FarfieldPlot
	.ClearCuts ' lateral=phi, polar=theta
	.AddCut "lateral", "0", "1"
	.AddCut "lateral", "90", "1"
	.AddCut "polar", "90", "1"
End With

'----------------------------------------------------------------------------

With MeshSettings
     .SetMeshType "Hex"
     .Set "Version", 1%
End With

With Mesh
     .MeshType "PBA"
End With

'set the solver type
ChangeSolverType("HF Time Domain")

'----------------------------------------------------------------------------

'@ define curve analytical: curve1:analytical1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With AnalyticalCurve
     .Reset 
     .Name "analytical1" 
     .Curve "curve1" 
     .LawX "(t^2)/(4*fff)" 
     .LawY "t" 
     .LawZ "0" 
     .ParameterRange "0", "200" 
     .Create
End With

'@ pick end point

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.PickCurveEndpointFromId "curve1:analytical1", "1"

'@ pick mid point

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.PickCurveMidpointFromId "curve1:analytical1", "1"

'@ pick end point

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.PickCurveEndpointFromId "curve1:analytical1", "2"

'@ define curve line: curve1:line1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Line
     .Reset 
     .Name "line1" 
     .Curve "curve1" 
     .X1 "-0" 
     .Y1 "200" 
     .X2 "1000" 
     .Y2 "200" 
     .Create
End With

'@ define curve line: curve1:line2

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Line
     .Reset 
     .Name "line2" 
     .Curve "curve1" 
     .X1 "-0" 
     .Y1 "200" 
     .X2 "0" 
     .Y2 "-0" 
     .Create
End With

'@ new component: component1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Component.New "component1"

'@ define coverprofiles: component1:solid1
_*

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With CoverCurve
     .Reset 
     .Name "solid1_1" 
     .Component "component1" 
     .Material "PEC" 
     .Curve "curve1:analytical1" 
     .DeleteCurve "True" 
     .Create
End With

'@ pick face

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.PickFaceFromId "component1:solid1_1", "1"

'@ set edge

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.AddEdge "0", "175", "0", "0", "-0", "0"

'@ define rotate: component1:solid1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Rotate 
     .Reset 
     .Name "solid1" 
     .Component "component1" 
     .NumberOfPickedFaces "1" 
     .Material "PEC" 
     .Mode "Picks" 
     .Angle "360.0" 
     .Height "0.0" 
     .RadiusRatio "1.0" 
     .TaperAngle "0.0" 
     .NSteps "0" 
     .SplitClosedEdges "True" 
     .SegmentedProfile "False" 
     .DeleteBaseFaceSolid "False" 
     .ClearPickedFace "True" 
     .SimplifySolid "True" 
     .UseAdvancedSegmentedRotation "True" 
     .CutEndOff "False" 
     .Create 
End With

'@ rename block: component1:solid1_1 to: component1:jooj

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Solid.Rename "component1:solid1_1", "jooj"

'@ delete shape: component1:jooj

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Solid.Delete "component1:jooj"

'@ delete shape: component1:solid1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Solid.Delete "component1:solid1"

'@ define curve analytical: curve1:analytical1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With AnalyticalCurve
     .Reset 
     .Name "analytical1" 
     .Curve "curve1" 
     .LawX "t" 
     .LawY "0" 
     .LawZ "t^2/1.824" 
     .ParameterRange "0", "0.6" 
     .Create
End With

'@ pick end point

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.PickCurveEndpointFromId "curve1:analytical1", "1"

'@ pick end point

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.PickCurveEndpointFromId "curve1:analytical1", "2"

'@ align wcs with point

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
WCS.AlignWCSWithSelected "Point"

'@ activate global coordinates

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
WCS.ActivateWCS "global"

'@ align wcs with point

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
WCS.AlignWCSWithSelected "Point"

'@ activate global coordinates

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
WCS.ActivateWCS "global"

'@ activate local coordinates

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
WCS.ActivateWCS "local"

'@ pick end point

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.PickCurveEndpointFromId "curve1:analytical1", "2"

'@ pick end point

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.PickCurveEndpointFromId "curve1:analytical1", "1"

'@ activate global coordinates

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
WCS.ActivateWCS "global"

'@ store picked point: 1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.NextPickToDatabase "1" 
Pick.PickCurveEndpointFromId "curve1:analytical1", "1"

'@ store picked point: 2

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.NextPickToDatabase "2" 
Pick.PickCurveMidpointFromId "curve1:analytical1", "1"

'@ store picked point: 3

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.NextPickToDatabase "3" 
Pick.PickCurveMidpointFromId "curve1:analytical1", "1"

'@ store picked point: 4

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.NextPickToDatabase "4" 
Pick.PickCurveEndpointFromId "curve1:analytical1", "1"

'@ store picked point: 5

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.NextPickToDatabase "5" 
Pick.PickCurveEndpointFromId "curve1:analytical1", "2"

'@ define curve 3dpolygon: curve1:3dpolygon1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Polygon3D 
     .Reset 
     .Version 10 
     .Name "3dpolygon1" 
     .Curve "curve1" 
     .Point "0", "0", "0" 
     .Point "0", "0", "0.19736842105263" 
     .Point "0.6", "0", "0.19736842105263" 
     .Create 
End With

'@ define coverprofiles: component1:solid1
_*

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With CoverCurve
     .Reset 
     .Name "solid1_1" 
     .Component "component1" 
     .Material "PEC" 
     .Curve "curve1:analytical1" 
     .DeleteCurve "True" 
     .Create
End With

'@ pick face

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.PickFaceFromId "component1:solid1_1", "1"

'@ set edge

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.AddEdge "0", "-0", "0", "0", "0", "0.19736842105263"

'@ define rotate: component1:solid1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Rotate 
     .Reset 
     .Name "solid1" 
     .Component "component1" 
     .NumberOfPickedFaces "1" 
     .Material "PEC" 
     .Mode "Picks" 
     .Angle "360.0" 
     .Height "0.0" 
     .RadiusRatio "1.0" 
     .TaperAngle "0.0" 
     .NSteps "0" 
     .SplitClosedEdges "True" 
     .SegmentedProfile "False" 
     .DeleteBaseFaceSolid "False" 
     .ClearPickedFace "True" 
     .SimplifySolid "True" 
     .UseAdvancedSegmentedRotation "True" 
     .CutEndOff "False" 
     .Create 
End With

'@ transform: translate component1:solid1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Transform 
     .Reset 
     .Name "component1:solid1" 
     .Vector "0", "0", "-0.025" 
     .UsePickedPoints "False" 
     .InvertPickedPoints "False" 
     .MultipleObjects "True" 
     .GroupObjects "False" 
     .Repetitions "1" 
     .MultipleSelection "False" 
     .Destination "" 
     .Material "" 
     .AutoDestination "True" 
     .Transform "Shape", "Translate" 
End With

'@ pick face

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.PickFaceFromId "component1:solid1", "1"

'@ define extrude: component1:solid2

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Extrude 
     .Reset 
     .Name "solid2" 
     .Component "component1" 
     .Material "PEC" 
     .Mode "Picks" 
     .Height "-0.025" 
     .Twist "0.0" 
     .Taper "0.0" 
     .UsePicksForHeight "False" 
     .DeleteBaseFaceSolid "False" 
     .KeepMaterials "False" 
     .ClearPickedFace "True" 
     .Create 
End With

'@ boolean add shapes: component1:solid1_2, component1:solid2

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Solid.Add "component1:solid1_2", "component1:solid2"

'@ boolean subtract shapes: component1:solid1_2, component1:solid1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Solid.Subtract "component1:solid1_2", "component1:solid1"

'@ transform: scale component1:solid1_2

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Transform 
     .Reset 
     .Name "component1:solid1_2" 
     .Origin "Free" 
     .Center "0", "0", "0" 
     .ScaleFactor "1000", "1000", "1000" 
     .MultipleObjects "False" 
     .GroupObjects "False" 
     .Repetitions "1" 
     .MultipleSelection "False" 
     .AutoDestination "True" 
     .Transform "Shape", "Scale" 
End With

'@ transform: translate component1:solid1_2

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Transform 
     .Reset 
     .Name "component1:solid1_2" 
     .Vector "0", "0", "-3" 
     .UsePickedPoints "False" 
     .InvertPickedPoints "False" 
     .MultipleObjects "True" 
     .GroupObjects "False" 
     .Repetitions "1" 
     .MultipleSelection "False" 
     .Destination "" 
     .Material "" 
     .AutoDestination "True" 
     .Transform "Shape", "Translate" 
End With

'@ boolean subtract shapes: component1:solid1_2_1, component1:solid1_2

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Solid.Subtract "component1:solid1_2_1", "component1:solid1_2"

'@ transform: translate component1:solid1_2_1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Transform 
     .Reset 
     .Name "component1:solid1_2_1" 
     .Vector "0", "0", "3" 
     .UsePickedPoints "False" 
     .InvertPickedPoints "False" 
     .MultipleObjects "False" 
     .GroupObjects "False" 
     .Repetitions "1" 
     .MultipleSelection "False" 
     .AutoDestination "True" 
     .Transform "Shape", "Translate" 
End With

'@ define frequency range

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Solver.FrequencyRange "1.410", "1.430"

'@ define farfield monitor: farfield (f=1.42)

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Monitor 
     .Reset 
     .Name "farfield (f=1.42)" 
     .Domain "Frequency" 
     .FieldType "Farfield" 
     .MonitorValue "1.42" 
     .ExportFarfieldSource "False" 
     .UseSubvolume "False" 
     .Coordinates "Structure" 
     .SetSubvolume "-600", "600", "-600", "600", "-25", "175.36842105263" 
     .SetSubvolumeOffset "10", "10", "10", "10", "10", "10" 
     .SetSubvolumeInflateWithOffset "False" 
     .SetSubvolumeOffsetType "FractionOfWavelength" 
     .EnableNearfieldCalculation "True" 
     .Create 
End With

'@ define plane wave properties

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With PlaneWave
     .Reset 
     .Normal "0", "0", "1" 
     .EVector "1", "0", "0" 
     .Polarization "Linear" 
     .ReferenceFrequency "1.42" 
     .PhaseDifference "-90.0" 
     .CircularDirection "Left" 
     .AxialRatio "0.0" 
     .SetUserDecouplingPlane "False" 
     .Store
End With

'@ define time domain solver parameters

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Mesh.SetCreator "High Frequency" 

With Solver 
     .Method "Hexahedral"
     .CalculationType "TD-PLW"
     .StimulationPort "Plane wave"
     .StimulationMode "1"
     .SteadyStateLimit "-40"
     .MeshAdaption "True"
     .StoreTDResultsInCache  "False"
     .RunDiscretizerOnly "False"
     .FullDeembedding "False"
     .SuperimposePLWExcitation "False"
     .UseSensitivityAnalysis "False"
End With

