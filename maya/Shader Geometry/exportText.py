baseanim = r"C:\Users\normal\Projects\robot-milagroso\Unity\Robot Milagroso\Assets\Animation\Base.anim"

# with open(baseanim) as data:
# 	rez = data.read()

t='''%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!74 &7400000
AnimationClip:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_Name: Base
  serializedVersion: 6
  m_Legacy: 0
  m_Compressed: 0
  m_UseHighQualityCurve: 1
  m_RotationCurves: []
  m_CompressedRotationCurves: []
  m_EulerCurves: []
  m_PositionCurves:
  - curve:
      serializedVersion: 2
      m_Curve:
      - serializedVersion: 3
        time: 0
        value: {x: 0, y: 0, z: 0}
        inSlope: {x: 0, y: 0, z: 0}
        outSlope: {x: 0, y: 0, z: 0}
        tangentMode: 0
        weightedMode: 0
        inWeight: {x: 0.33333334, y: 0.33333334, z: 0.33333334}
        outWeight: {x: 0.33333334, y: 0.33333334, z: 0.33333334}
      - serializedVersion: 3
        time: 1
        value: {x: 0, y: 0, z: 0}
        inSlope: {x: 0, y: 0, z: 0}
        outSlope: {x: 0, y: 0, z: 0}
        tangentMode: 0
        weightedMode: 0
        inWeight: {x: 0.33333334, y: 0.33333334, z: 0.33333334}
        outWeight: {x: 0.33333334, y: 0.33333334, z: 0.33333334}
      m_PreInfinity: 2
      m_PostInfinity: 2
      m_RotationOrder: 4
    path: 
  m_ScaleCurves: []
  m_FloatCurves: []
  m_PPtrCurves: []
  m_SampleRate: 60
  m_WrapMode: 0
  m_Bounds:
    m_Center: {x: 0, y: 0, z: 0}
    m_Extent: {x: 0, y: 0, z: 0}
  m_ClipBindingConstant:
    genericBindings:
    - serializedVersion: 2
      path: 0
      attribute: 1
      script: {fileID: 0}
      typeID: 4
      customType: 0
      isPPtrCurve: 0
    pptrCurveMapping: []
  m_AnimationClipSettings:
    serializedVersion: 2
    m_AdditiveReferencePoseClip: {fileID: 0}
    m_AdditiveReferencePoseTime: 0
    m_StartTime: 0
    m_StopTime: 1
    m_OrientationOffsetY: 0
    m_Level: 0
    m_CycleOffset: 0
    m_HasAdditiveReferencePose: 0
    m_LoopTime: 0
    m_LoopBlend: 0
    m_LoopBlendOrientation: 0
    m_LoopBlendPositionY: 0
    m_LoopBlendPositionXZ: 0
    m_KeepOriginalOrientation: 0
    m_KeepOriginalPositionY: 1
    m_KeepOriginalPositionXZ: 0
    m_HeightFromFeet: 0
    m_Mirror: 0
  m_EditorCurves:
  - curve:
      serializedVersion: 2
      m_Curve:
      - serializedVersion: 3
        time: 0
        value: 0
        inSlope: 0
        outSlope: 0
        tangentMode: 136
        weightedMode: 0
        inWeight: 0.33333334
        outWeight: 0.33333334
      - serializedVersion: 3
        time: 1
        value: 0
        inSlope: 0
        outSlope: 0
        tangentMode: 136
        weightedMode: 0
        inWeight: 0.33333334
        outWeight: 0.33333334
      m_PreInfinity: 2
      m_PostInfinity: 2
      m_RotationOrder: 4
    attribute: m_LocalPosition.x
    path: 
    classID: 4
    script: {fileID: 0}
  - curve:
      serializedVersion: 2
      m_Curve:
      - serializedVersion: 3
        time: 0
        value: 0
        inSlope: 0
        outSlope: 0
        tangentMode: 136
        weightedMode: 0
        inWeight: 0.33333334
        outWeight: 0.33333334
      - serializedVersion: 3
        time: 1
        value: 150
        inSlope: 0
        outSlope: 0
        tangentMode: 136
        weightedMode: 0
        inWeight: 0.33333334
        outWeight: 0.33333334
      m_PreInfinity: 2
      m_PostInfinity: 2
      m_RotationOrder: 4
    attribute: m_LocalPosition.y
    path: 
    classID: 4
    script: {fileID: 0}
  - curve:
      serializedVersion: 2
      m_Curve:
      - serializedVersion: 3
        time: 0
        value: 0
        inSlope: 0
        outSlope: 0
        tangentMode: 136
        weightedMode: 0
        inWeight: 0.33333334
        outWeight: 0.33333334
      - serializedVersion: 3
        time: 1
        value: 0
        inSlope: 0
        outSlope: 0
        tangentMode: 136
        weightedMode: 0
        inWeight: 0.33333334
        outWeight: 0.33333334
      m_PreInfinity: 2
      m_PostInfinity: 2
      m_RotationOrder: 4
    attribute: m_LocalPosition.z
    path: 
    classID: 4
    script: {fileID: 0}
  m_EulerEditorCurves: []
  m_HasGenericRootTransform: 1
  m_HasMotionFloatCurves: 0
  m_Events: []'''

with open(baseanim,'w') as data:

	for n in t.split('\n'):
		print(n)
		data.write('%s\n'%n)