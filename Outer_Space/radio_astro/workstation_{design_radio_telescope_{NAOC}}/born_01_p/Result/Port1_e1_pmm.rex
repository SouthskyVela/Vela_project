<?xml version="1.0" encoding="UTF-8"?>
<MetaResultFile version="20211011" creator="FE Port mode solver">
  <MetaGeometryFile filename="" lod="1"/>
  <SimulationProperties fieldname="Port1 e1" frequency="1.4199999999999999" encoded_unit="&amp;U:V^1.:m^-1" quantity="e-field" fieldtype="E-Field" fieldscaling="PEAK" dB_Amplitude="20"/>
  <ResultDataType vector="1" complex="1" timedomain="0" frequencymap="1"/>
  <SimulationDomain min="0 0 0" max="0 0 0"/>
  <PlotSettings Plot="1" ignore_symmetry="0" deformation="0" enforce_culling="0" integer_values="0" combine="CombineNone" default_arrow_type="ARROWS" default_scaling="NONE">
    <Plane normal="0 0 1" distance="0"/>
  </PlotSettings>
  <Source type="SOLVER"/>
  <SpecialMaterials>
    <Background type="NORMAL"/>
  </SpecialMaterials>
  <SupplementalMesh/>
  <AuxGeometryFile/>
  <AuxResultFile filename="Port1_e1[1.42]_prt^res.axg" add_to_tree="0" default="0"/>
  <FieldFreeNodes/>
  <SurfaceFieldCoefficients/>
  <UnitCell/>
  <SubVolume/>
  <Units/>
  <ProjectUnits>
    <Quantity name="length" unit="&amp;Um:m^1"/>
    <Quantity name="frequency" unit="&amp;UG:Hz^1"/>
    <Quantity name="time" unit="&amp;Un:s^1"/>
    <Quantity name="temperature" unit="&amp;U:Cel^1"/>
  </ProjectUnits>
  <TimeSampling/>
  <LocalAxes/>
  <MeshViewSettings/>
  <WaveguidePort points="-46 -46 0 46 -46 0 46 46 0 -46 46 0" normal="0 0 1"/>
  <ResultGroups num_steps="1" transformation="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1" process_mesh_group="0">
    <SharedDataWith/>
    <Frame index="0" characteristic="1.4199999999999999">
      <PortModeInfoFile filename="Port1_Info1[1.42].mmd"/>
      <FieldResultFile filename="Port1_e1[1.42]_prt.sct" type="sct" meshname="Port^Mesh^1_1.slm"/>
    </Frame>
  </ResultGroups>
  <AutoScale>
    <SmartScaling log_strength="1" log_anchor="0" log_anchor_type="0" db_range="40" phase="0"/>
  </AutoScale>
</MetaResultFile>
