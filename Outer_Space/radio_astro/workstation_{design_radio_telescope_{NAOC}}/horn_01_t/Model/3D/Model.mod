'# MWS Version: Version 2025.2 - Dec 16 2024 - ACIS 34.0.1 -

'# length = mm
'# frequency = GHz
'# time = ns
'# frequency range: fmin = 8 fmax = 12
'# created = '[VERSION]2025.2|34.0.1|20241216[/VERSION]


'@ new component: component1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Component.New "component1"

'@ define cylinder: component1:solid1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Cylinder 
     .Reset 
     .Name "solid1" 
     .Component "component1" 
     .Material "PEC" 
     .OuterRadius "10" 
     .InnerRadius "0" 
     .Axis "z" 
     .Zrange "0", "20" 
     .Xcenter "0" 
     .Ycenter "0" 
     .Segments "0" 
     .Create 
End With

'@ clear picks

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.ClearAllPicks

'@ pick face

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.PickFaceFromId "component1:solid1", "3"

'@ define extrude: component1:solid2

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Extrude 
     .Reset 
     .Name "solid2" 
     .Component "component1" 
     .Material "PEC" 
     .Mode "Picks" 
     .Height "20" 
     .Twist "0.0" 
     .Taper "30" 
     .UsePicksForHeight "False" 
     .DeleteBaseFaceSolid "False" 
     .KeepMaterials "False" 
     .ClearPickedFace "True" 
     .Create 
End With

'@ boolean add shapes: component1:solid1, component1:solid2

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Solid.Add "component1:solid1", "component1:solid2"

'@ pick face

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.PickFaceFromId "component1:solid1", "2"

'@ pick face

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.PickFaceFromId "component1:solid1", "4"

'@ shell object: component1:solid1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Solid.ShellAdvanced "component1:solid1", "Outside", "2", "True"

'@ define frequency range

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Solver.FrequencyRange "8", "12"

'@ pick face

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Pick.PickFaceFromId "component1:solid1", "9"

'@ define port: 1

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Port 
     .Reset 
     .PortNumber "1" 
     .Label ""
     .Folder ""
     .NumberOfModes "5"
     .AdjustPolarization "False"
     .PolarizationAngle "0.0"
     .ReferencePlaneDistance "0"
     .TextSize "50"
     .TextMaxLimit "0"
     .Coordinates "Picks"
     .Orientation "positive"
     .PortOnBound "False"
     .ClipPickedPortToBound "False"
     .Xrange "-12", "12"
     .Yrange "-12", "12"
     .Zrange "0", "0"
     .XrangeAdd "0.0", "0.0"
     .YrangeAdd "0.0", "0.0"
     .ZrangeAdd "0.0", "0.0"
     .SingleEnded "False"
     .WaveguideMonitor "False"
     .Create 
End With

'@ define farfield monitor: farfield (f=10)

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Monitor 
     .Reset 
     .Name "farfield (f=10)" 
     .Domain "Frequency" 
     .FieldType "Farfield" 
     .MonitorValue "10" 
     .ExportFarfieldSource "False" 
     .UseSubvolume "False" 
     .Coordinates "Structure" 
     .SetSubvolume "-23.856406460551", "23.856406460551", "-23.856406460551", "23.856406460551", "0", "40" 
     .SetSubvolumeOffset "10", "10", "10", "10", "10", "10" 
     .SetSubvolumeInflateWithOffset "False" 
     .SetSubvolumeOffsetType "FractionOfWavelength" 
     .EnableNearfieldCalculation "True" 
     .Create 
End With

'@ define farfield monitor: farfield (f=9)

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Monitor 
     .Reset 
     .Name "farfield (f=9)" 
     .Domain "Frequency" 
     .FieldType "Farfield" 
     .MonitorValue "9" 
     .ExportFarfieldSource "False" 
     .UseSubvolume "False" 
     .Coordinates "Structure" 
     .SetSubvolume "-23.856406460551", "23.856406460551", "-23.856406460551", "23.856406460551", "0", "40" 
     .SetSubvolumeOffset "10", "10", "10", "10", "10", "10" 
     .SetSubvolumeInflateWithOffset "False" 
     .SetSubvolumeOffsetType "FractionOfWavelength" 
     .EnableNearfieldCalculation "True" 
     .Create 
End With

'@ define farfield monitor: farfield (f=11)

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With Monitor 
     .Reset 
     .Name "farfield (f=11)" 
     .Domain "Frequency" 
     .FieldType "Farfield" 
     .MonitorValue "11" 
     .ExportFarfieldSource "False" 
     .UseSubvolume "False" 
     .Coordinates "Structure" 
     .SetSubvolume "-23.856406460551", "23.856406460551", "-23.856406460551", "23.856406460551", "0", "40" 
     .SetSubvolumeOffset "10", "10", "10", "10", "10", "10" 
     .SetSubvolumeInflateWithOffset "False" 
     .SetSubvolumeOffsetType "FractionOfWavelength" 
     .EnableNearfieldCalculation "True" 
     .Create 
End With

'@ define time domain solver parameters

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
Mesh.SetCreator "High Frequency" 

With Solver 
     .Method "Hexahedral"
     .CalculationType "TD-S"
     .StimulationPort "All"
     .StimulationMode "1"
     .SteadyStateLimit "-30"
     .MeshAdaption "False"
     .AutoNormImpedance "False"
     .NormingImpedance "50"
     .CalculateModesOnly "False"
     .SParaSymmetry "False"
     .StoreTDResultsInCache  "False"
     .RunDiscretizerOnly "False"
     .FullDeembedding "False"
     .SuperimposePLWExcitation "False"
     .UseSensitivityAnalysis "False"
End With

'@ farfield plot options

'[VERSION]2025.2|34.0.1|20241216[/VERSION]
With FarfieldPlot 
     .Plottype "3D" 
     .Vary "angle1" 
     .Theta "90" 
     .Phi "90" 
     .Step "5" 
     .Step2 "5" 
     .SetLockSteps "True" 
     .SetPlotRangeOnly "False" 
     .SetThetaStart "0" 
     .SetThetaEnd "180" 
     .SetPhiStart "0" 
     .SetPhiEnd "360" 
     .SetTheta360 "False" 
     .SymmetricRange "False" 
     .SetTimeDomainFF "False" 
     .SetFrequency "11" 
     .SetTime "0" 
     .SetColorByValue "True" 
     .DrawStepLines "False" 
     .DrawIsoLongitudeLatitudeLines "False" 
     .ShowStructure "False" 
     .ShowStructureProfile "False" 
     .SetStructureTransparent "False" 
     .SetFarfieldTransparent "False" 
     .AspectRatio "Free" 
     .ShowGridlines "True" 
     .InvertAxes "False", "False" 
     .SetSpecials "enablepolarextralines" 
     .SetPlotMode "Gain" 
     .Distance "1" 
     .UseFarfieldApproximation "True" 
     .IncludeUnitCellSidewalls "True" 
     .SetScaleLinear "False" 
     .SetLogRange "40" 
     .SetLogNorm "0" 
     .DBUnit "0" 
     .SetMaxReferenceMode "abs" 
     .EnableFixPlotMaximum "False" 
     .SetFixPlotMaximumValue "1.0" 
     .SetInverseAxialRatio "False" 
     .SetAxesType "user" 
     .SetAntennaType "unknown" 
     .Phistart "1.000000e+00", "0.000000e+00", "0.000000e+00" 
     .Thetastart "0.000000e+00", "0.000000e+00", "1.000000e+00" 
     .PolarizationVector "0.000000e+00", "1.000000e+00", "0.000000e+00" 
     .SetCoordinateSystemType "spherical" 
     .SetAutomaticCoordinateSystem "True" 
     .SetPolarizationType "Linear" 
     .SlantAngle 0.000000e+00 
     .Origin "bbox" 
     .Userorigin "0.000000e+00", "0.000000e+00", "0.000000e+00" 
     .SetUserDecouplingPlane "False" 
     .UseDecouplingPlane "False" 
     .DecouplingPlaneAxis "X" 
     .DecouplingPlanePosition "0.000000e+00" 
     .LossyGround "False" 
     .GroundEpsilon "1" 
     .GroundKappa "0" 
     .EnablePhaseCenterCalculation "False" 
     .SetPhaseCenterAngularLimit "3.000000e+01" 
     .SetPhaseCenterComponent "boresight" 
     .SetPhaseCenterPlane "both" 
     .ShowPhaseCenter "True" 
     .ClearCuts 

     .StoreSettings
End With

