

OpenDatabase("dbreak3d_fluid.visit")
AddPlot("Contour", "alpha1")
AddPlot("Vector", "U", 1, 1)


ContourAtts = ContourAttributes()
ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(0).position = 0
ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(29).position = 1
ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
ContourAtts.defaultPalette.equalSpacingFlag = 1
ContourAtts.defaultPalette.discreteFlag = 1
ContourAtts.defaultPalette.categoryName = "Standard"
ContourAtts.changedColors = ()
ContourAtts.colorType = ContourAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
ContourAtts.colorTableName = "plasma"
ContourAtts.invertColorTable = 1
ContourAtts.legendFlag = 1
ContourAtts.lineStyle = ContourAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
ContourAtts.lineWidth = 0
ContourAtts.singleColor = (255, 0, 0, 255)
ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
ContourAtts.contourNLevels = 1
ContourAtts.contourValue = ()
ContourAtts.contourPercent = ()
ContourAtts.contourMethod = ContourAtts.Level  # Level, Value, Percent
ContourAtts.minFlag = 0
ContourAtts.maxFlag = 0
ContourAtts.min = 0
ContourAtts.max = 1
ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
ContourAtts.wireframe = 0
SetPlotOptions(ContourAtts)
VectorAtts = VectorAttributes()
VectorAtts.glyphLocation = VectorAtts.AdaptsToMeshResolution  # AdaptsToMeshResolution, UniformInSpace
VectorAtts.useStride = 0
VectorAtts.stride = 1
VectorAtts.nVectors = 400
VectorAtts.lineStyle = VectorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
VectorAtts.lineWidth = 0
VectorAtts.scale = 0.25
VectorAtts.scaleByMagnitude = 1
VectorAtts.autoScale = 1
VectorAtts.headSize = 0.5
VectorAtts.headOn = 1
VectorAtts.colorByMag = 1
VectorAtts.useLegend = 1
VectorAtts.vectorColor = (0, 0, 0, 255)
VectorAtts.colorTableName = "Default"
VectorAtts.invertColorTable = 0
VectorAtts.vectorOrigin = VectorAtts.Tail  # Head, Middle, Tail
VectorAtts.minFlag = 0
VectorAtts.maxFlag = 0
VectorAtts.limitsMode = VectorAtts.OriginalData  # OriginalData, CurrentPlot
VectorAtts.min = 0
VectorAtts.max = 1
VectorAtts.lineStem = VectorAtts.Line  # Cylinder, Line
VectorAtts.geometryQuality = VectorAtts.Fast  # Fast, High
VectorAtts.stemWidth = 0.08
VectorAtts.origOnly = 1
VectorAtts.glyphType = VectorAtts.Arrow  # Arrow, Ellipsoid
SetPlotOptions(VectorAtts)
VectorAtts = VectorAttributes()
VectorAtts.glyphLocation = VectorAtts.AdaptsToMeshResolution  # AdaptsToMeshResolution, UniformInSpace
VectorAtts.useStride = 0
VectorAtts.stride = 1
VectorAtts.nVectors = 400
VectorAtts.lineStyle = VectorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
VectorAtts.lineWidth = 0
VectorAtts.scale = 0.25
VectorAtts.scaleByMagnitude = 1
VectorAtts.autoScale = 1
VectorAtts.headSize = 0.5
VectorAtts.headOn = 1
VectorAtts.colorByMag = 1
VectorAtts.useLegend = 1
VectorAtts.vectorColor = (0, 0, 0, 255)
VectorAtts.colorTableName = "OrRd"
VectorAtts.invertColorTable = 0
VectorAtts.vectorOrigin = VectorAtts.Tail  # Head, Middle, Tail
VectorAtts.minFlag = 0
VectorAtts.maxFlag = 0
VectorAtts.limitsMode = VectorAtts.OriginalData  # OriginalData, CurrentPlot
VectorAtts.min = 0
VectorAtts.max = 1
VectorAtts.lineStem = VectorAtts.Line  # Cylinder, Line
VectorAtts.geometryQuality = VectorAtts.Fast  # Fast, High
VectorAtts.stemWidth = 0.08
VectorAtts.origOnly = 1
VectorAtts.glyphType = VectorAtts.Arrow  # Arrow, Ellipsoid
SetPlotOptions(VectorAtts)
# Logging for SetAnnotationObjectOptions is not implemented yet.
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 0
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 0
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 1
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 1
AnnotationAtts.axes3D.bboxFlag = 1
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.userInfoFlag = 1
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# Logging for SetAnnotationObjectOptions is not implemented yet.
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 0
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 0
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 1
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 1
AnnotationAtts.axes3D.bboxFlag = 1
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# Logging for SetAnnotationObjectOptions is not implemented yet.
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 0
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 0
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 1
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.axes3D.bboxFlag = 1
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# Logging for SetAnnotationObjectOptions is not implemented yet.
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 0
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 0
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 1
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.axes3D.bboxFlag = 0
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# Logging for SetAnnotationObjectOptions is not implemented yet.
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 0
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 0
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 1
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.axes3D.bboxFlag = 1
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# Logging for SetAnnotationObjectOptions is not implemented yet.
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 0
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 0
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 0
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.axes3D.bboxFlag = 1
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# Logging for SetAnnotationObjectOptions is not implemented yet.
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 0
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 0
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 0
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.axes3D.bboxFlag = 1
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 0
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# Logging for SetAnnotationObjectOptions is not implemented yet.
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 1
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 0
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 0
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 0
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.axes3D.bboxFlag = 1
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Image  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = "/home/jesse/Downloads/Beach_Background-885.jpg"
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 0
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.
SaveSession("/home/jesse/.visit/crash_recovery.session")
# MAINTENANCE ISSUE: SetSuppressMessagesRPC is not handled in Logging.C. Please contact a VisIt developer.





DrawPlots()
sw = SaveWindowAttributes()
sw.family = 0
sw.width = 800
sw.height = 800
sw.format = sw.PPM
frame_idx=0
actually_do_a_save= 1

def MySaveWindow():
	global actually_do_a_save
	if (actually_do_a_save):
		SaveWindow()

def PauseOneSecond():
  global frame_idx
  for i in range(15):
    sw.fileName="frames/m%02d" %(frame_idx)
    frame_idx = frame_idx + 1
    SetSaveWindowAttributes(sw)
    MySaveWindow()



def setContours():
	print("setting up contour stuff")
	ContourAtts = ContourAttributes()
	ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(0).position = 0
	ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
	ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
	ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
	ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
	ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
	ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
	ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
	ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
	ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
	ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
	ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
	ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
	ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
	ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
	ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
	ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
	ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
	ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
	ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
	ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
	ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
	ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
	ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
	ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
	ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
	ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
	ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
	ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
	ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
	ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
	ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
	ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
	ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
	ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
	ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
	ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
	ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
	ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(29).position = 1
	ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
	ContourAtts.defaultPalette.equalSpacingFlag = 1
	ContourAtts.defaultPalette.discreteFlag = 1
	ContourAtts.defaultPalette.categoryName = "Standard"
	ContourAtts.changedColors = ()
	ContourAtts.colorType = ContourAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
	ContourAtts.colorTableName = "plasma"
	ContourAtts.invertColorTable = 1
	ContourAtts.legendFlag = 1
	ContourAtts.lineStyle = ContourAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	ContourAtts.lineWidth = 0
	ContourAtts.singleColor = (255, 0, 0, 255)
	ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
	ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
	ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
	ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
	ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
	ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
	ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
	ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
	ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
	ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
	ContourAtts.contourNLevels = 2
	ContourAtts.contourValue = ()
	ContourAtts.contourPercent = ()
	ContourAtts.contourMethod = ContourAtts.Level  # Level, Value, Percent
	ContourAtts.minFlag = 0
	ContourAtts.maxFlag = 0
	ContourAtts.min = 0
	ContourAtts.max = 1
	ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
	ContourAtts.wireframe = 0
	SetPlotOptions(ContourAtts)
	PauseOneSecond()

	#2 go!
	ContourAtts = ContourAttributes()
	ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(0).position = 0
	ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
	ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
	ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
	ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
	ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
	ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
	ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
	ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
	ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
	ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
	ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
	ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
	ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
	ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
	ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
	ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
	ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
	ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
	ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
	ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
	ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
	ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
	ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
	ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
	ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
	ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
	ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
	ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
	ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
	ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
	ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
	ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
	ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
	ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
	ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
	ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
	ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
	ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(29).position = 1
	ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
	ContourAtts.defaultPalette.equalSpacingFlag = 1
	ContourAtts.defaultPalette.discreteFlag = 1
	ContourAtts.defaultPalette.categoryName = "Standard"
	ContourAtts.changedColors = ()
	ContourAtts.colorType = ContourAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
	ContourAtts.colorTableName = "plasma"
	ContourAtts.invertColorTable = 1
	ContourAtts.legendFlag = 1
	ContourAtts.lineStyle = ContourAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	ContourAtts.lineWidth = 0
	ContourAtts.singleColor = (255, 0, 0, 255)
	ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
	ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
	ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
	ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
	ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
	ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
	ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
	ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
	ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
	ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
	ContourAtts.contourNLevels = 3
	ContourAtts.contourValue = ()
	ContourAtts.contourPercent = ()
	ContourAtts.contourMethod = ContourAtts.Level  # Level, Value, Percent
	ContourAtts.minFlag = 0
	ContourAtts.maxFlag = 0
	ContourAtts.min = 0
	ContourAtts.max = 1
	ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
	ContourAtts.wireframe = 0
	SetPlotOptions(ContourAtts)

	PauseOneSecond()

	ContourAtts = ContourAttributes()
	ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(0).position = 0
	ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
	ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
	ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
	ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
	ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
	ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
	ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
	ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
	ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
	ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
	ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
	ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
	ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
	ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
	ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
	ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
	ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
	ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
	ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
	ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
	ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
	ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
	ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
	ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
	ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
	ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
	ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
	ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
	ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
	ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
	ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
	ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
	ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
	ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
	ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
	ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
	ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
	ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(29).position = 1
	ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
	ContourAtts.defaultPalette.equalSpacingFlag = 1
	ContourAtts.defaultPalette.discreteFlag = 1
	ContourAtts.defaultPalette.categoryName = "Standard"
	ContourAtts.changedColors = ()
	ContourAtts.colorType = ContourAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
	ContourAtts.colorTableName = "plasma"
	ContourAtts.invertColorTable = 1
	ContourAtts.legendFlag = 1
	ContourAtts.lineStyle = ContourAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	ContourAtts.lineWidth = 0
	ContourAtts.singleColor = (255, 0, 0, 255)
	ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
	ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
	ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
	ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
	ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
	ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
	ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
	ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
	ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
	ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
	ContourAtts.contourNLevels = 4
	ContourAtts.contourValue = ()
	ContourAtts.contourPercent = ()
	ContourAtts.contourMethod = ContourAtts.Level  # Level, Value, Percent
	ContourAtts.minFlag = 0
	ContourAtts.maxFlag = 0
	ContourAtts.min = 0
	ContourAtts.max = 1
	ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
	ContourAtts.wireframe = 0
	SetPlotOptions(ContourAtts)
	PauseOneSecond()

	ContourAtts = ContourAttributes()
	ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(0).position = 0
	ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
	ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
	ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
	ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
	ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
	ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
	ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
	ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
	ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
	ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
	ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
	ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
	ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
	ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
	ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
	ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
	ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
	ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
	ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
	ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
	ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
	ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
	ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
	ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
	ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
	ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
	ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
	ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
	ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
	ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
	ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
	ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
	ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
	ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
	ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
	ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
	ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
	ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(29).position = 1
	ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
	ContourAtts.defaultPalette.equalSpacingFlag = 1
	ContourAtts.defaultPalette.discreteFlag = 1
	ContourAtts.defaultPalette.categoryName = "Standard"
	ContourAtts.changedColors = ()
	ContourAtts.colorType = ContourAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
	ContourAtts.colorTableName = "plasma"
	ContourAtts.invertColorTable = 1
	ContourAtts.legendFlag = 1
	ContourAtts.lineStyle = ContourAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	ContourAtts.lineWidth = 0
	ContourAtts.singleColor = (255, 0, 0, 255)
	ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
	ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
	ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
	ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
	ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
	ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
	ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
	ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
	ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
	ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
	ContourAtts.contourNLevels = 5
	ContourAtts.contourValue = ()
	ContourAtts.contourPercent = ()
	ContourAtts.contourMethod = ContourAtts.Level  # Level, Value, Percent
	ContourAtts.minFlag = 0
	ContourAtts.maxFlag = 0
	ContourAtts.min = 0
	ContourAtts.max = 1
	ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
	ContourAtts.wireframe = 0
	SetPlotOptions(ContourAtts)
	PauseOneSecond()
	ContourAtts = ContourAttributes()
	ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(0).position = 0
	ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
	ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
	ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
	ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
	ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
	ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
	ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
	ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
	ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
	ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
	ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
	ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
	ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
	ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
	ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
	ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
	ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
	ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
	ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
	ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
	ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
	ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
	ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
	ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
	ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
	ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
	ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
	ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
	ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
	ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
	ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
	ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
	ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
	ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
	ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
	ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
	ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
	ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(29).position = 1
	ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
	ContourAtts.defaultPalette.equalSpacingFlag = 1
	ContourAtts.defaultPalette.discreteFlag = 1
	ContourAtts.defaultPalette.categoryName = "Standard"
	ContourAtts.changedColors = ()
	ContourAtts.colorType = ContourAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
	ContourAtts.colorTableName = "plasma"
	ContourAtts.invertColorTable = 1
	ContourAtts.legendFlag = 1
	ContourAtts.lineStyle = ContourAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	ContourAtts.lineWidth = 0
	ContourAtts.singleColor = (255, 0, 0, 255)
	ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
	ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
	ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
	ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
	ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
	ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
	ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
	ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
	ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
	ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
	ContourAtts.contourNLevels = 6
	ContourAtts.contourValue = ()
	ContourAtts.contourPercent = ()
	ContourAtts.contourMethod = ContourAtts.Level  # Level, Value, Percent
	ContourAtts.minFlag = 0
	ContourAtts.maxFlag = 0
	ContourAtts.min = 0
	ContourAtts.max = 1
	ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
	ContourAtts.wireframe = 0
	SetPlotOptions(ContourAtts)
	PauseOneSecond()
	ContourAtts = ContourAttributes()
	ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(0).position = 0
	ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
	ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
	ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
	ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
	ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
	ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
	ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
	ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
	ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
	ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
	ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
	ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
	ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
	ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
	ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
	ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
	ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
	ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
	ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
	ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
	ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
	ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
	ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
	ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
	ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
	ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
	ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
	ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
	ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
	ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
	ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
	ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
	ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
	ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
	ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
	ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
	ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
	ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(29).position = 1
	ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
	ContourAtts.defaultPalette.equalSpacingFlag = 1
	ContourAtts.defaultPalette.discreteFlag = 1
	ContourAtts.defaultPalette.categoryName = "Standard"
	ContourAtts.changedColors = ()
	ContourAtts.colorType = ContourAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
	ContourAtts.colorTableName = "plasma"
	ContourAtts.invertColorTable = 1
	ContourAtts.legendFlag = 1
	ContourAtts.lineStyle = ContourAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	ContourAtts.lineWidth = 0
	ContourAtts.singleColor = (255, 0, 0, 255)
	ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
	ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
	ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
	ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
	ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
	ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
	ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
	ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
	ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
	ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
	ContourAtts.contourNLevels = 7
	ContourAtts.contourValue = ()
	ContourAtts.contourPercent = ()
	ContourAtts.contourMethod = ContourAtts.Level  # Level, Value, Percent
	ContourAtts.minFlag = 0
	ContourAtts.maxFlag = 0
	ContourAtts.min = 0
	ContourAtts.max = 1
	ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
	ContourAtts.wireframe = 0
	SetPlotOptions(ContourAtts)
	PauseOneSecond()
	ContourAtts = ContourAttributes()
	ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(0).position = 0
	ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
	ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
	ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
	ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
	ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
	ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
	ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
	ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
	ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
	ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
	ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
	ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
	ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
	ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
	ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
	ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
	ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
	ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
	ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
	ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
	ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
	ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
	ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
	ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
	ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
	ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
	ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
	ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
	ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
	ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
	ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
	ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
	ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
	ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
	ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
	ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
	ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
	ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(29).position = 1
	ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
	ContourAtts.defaultPalette.equalSpacingFlag = 1
	ContourAtts.defaultPalette.discreteFlag = 1
	ContourAtts.defaultPalette.categoryName = "Standard"
	ContourAtts.changedColors = ()
	ContourAtts.colorType = ContourAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
	ContourAtts.colorTableName = "plasma"
	ContourAtts.invertColorTable = 1
	ContourAtts.legendFlag = 1
	ContourAtts.lineStyle = ContourAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	ContourAtts.lineWidth = 0
	ContourAtts.singleColor = (255, 0, 0, 255)
	ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
	ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
	ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
	ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
	ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
	ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
	ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
	ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
	ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
	ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
	ContourAtts.contourNLevels = 8
	ContourAtts.contourValue = ()
	ContourAtts.contourPercent = ()
	ContourAtts.contourMethod = ContourAtts.Level  # Level, Value, Percent
	ContourAtts.minFlag = 0
	ContourAtts.maxFlag = 0
	ContourAtts.min = 0
	ContourAtts.max = 1
	ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
	ContourAtts.wireframe = 0
	SetPlotOptions(ContourAtts)
	PauseOneSecond()
	ContourAtts = ContourAttributes()
	ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(0).position = 0
	ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
	ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
	ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
	ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
	ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
	ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
	ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
	ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
	ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
	ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
	ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
	ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
	ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
	ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
	ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
	ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
	ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
	ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
	ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
	ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
	ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
	ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
	ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
	ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
	ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
	ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
	ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
	ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
	ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
	ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
	ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
	ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
	ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
	ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
	ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
	ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
	ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
	ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(29).position = 1
	ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
	ContourAtts.defaultPalette.equalSpacingFlag = 1
	ContourAtts.defaultPalette.discreteFlag = 1
	ContourAtts.defaultPalette.categoryName = "Standard"
	ContourAtts.changedColors = ()
	ContourAtts.colorType = ContourAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
	ContourAtts.colorTableName = "plasma"
	ContourAtts.invertColorTable = 1
	ContourAtts.legendFlag = 1
	ContourAtts.lineStyle = ContourAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	ContourAtts.lineWidth = 0
	ContourAtts.singleColor = (255, 0, 0, 255)
	ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
	ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
	ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
	ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
	ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
	ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
	ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
	ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
	ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
	ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
	ContourAtts.contourNLevels = 9
	ContourAtts.contourValue = ()
	ContourAtts.contourPercent = ()
	ContourAtts.contourMethod = ContourAtts.Level  # Level, Value, Percent
	ContourAtts.minFlag = 0
	ContourAtts.maxFlag = 0
	ContourAtts.min = 0
	ContourAtts.max = 1
	ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
	ContourAtts.wireframe = 0
	SetPlotOptions(ContourAtts)
	PauseOneSecond()
	ContourAtts = ContourAttributes()
	ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(0).position = 0
	ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
	ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
	ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
	ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
	ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
	ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
	ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
	ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
	ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
	ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
	ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
	ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
	ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
	ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
	ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
	ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
	ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
	ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
	ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
	ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
	ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
	ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
	ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
	ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
	ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
	ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
	ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
	ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
	ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
	ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
	ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
	ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
	ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
	ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
	ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
	ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
	ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
	ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
	ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
	ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
	ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
	ContourAtts.defaultPalette.GetControlPoints(29).position = 1
	ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.None  # None, Linear, CubicSpline
	ContourAtts.defaultPalette.equalSpacingFlag = 1
	ContourAtts.defaultPalette.discreteFlag = 1
	ContourAtts.defaultPalette.categoryName = "Standard"
	ContourAtts.changedColors = ()
	ContourAtts.colorType = ContourAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
	ContourAtts.colorTableName = "plasma"
	ContourAtts.invertColorTable = 1
	ContourAtts.legendFlag = 1
	ContourAtts.lineStyle = ContourAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	ContourAtts.lineWidth = 0
	ContourAtts.singleColor = (255, 0, 0, 255)
	ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
	ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
	ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
	ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
	ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
	ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
	ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
	ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
	ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
	ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
	ContourAtts.contourNLevels = 10
	ContourAtts.contourValue = ()
	ContourAtts.contourPercent = ()
	ContourAtts.contourMethod = ContourAtts.Level  # Level, Value, Percent
	ContourAtts.minFlag = 0
	ContourAtts.maxFlag = 0
	ContourAtts.min = 0
	ContourAtts.max = 1
	ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
	ContourAtts.wireframe = 0
	SetPlotOptions(ContourAtts)
	PauseOneSecond()





def zoom():
 # Begin spontaneous state
 	global frame_idx
 	# Begin spontaneous state
	c0 = View3DAttributes()
	c0.viewNormal = (0, 0, 1)
	c0.focus = (0.292, 0.292, 0.219)
	c0.viewUp = (0, 1, 0)
	c0.viewAngle = 30
	c0.parallelScale = 0.467428
	c0.nearPlane = -0.934856
	c0.farPlane = 0.934856
	c0.imagePan = (0, 0)
	c0.imageZoom = 0.179859
	# End spontaneous state

	c1 = View3DAttributes()
	c1.viewNormal = (0, 0, 1)
	c1.focus = (0.292, 0.292, 0.219)
	c1.viewUp = (0, 1, 0)
	c1.viewAngle = 30
	c1.parallelScale = 0.467428
	c1.nearPlane = -0.934856
	c1.farPlane = 0.934856
	c1.imagePan = (0, 0)
	c1.imageZoom = 0.58
	

	c2 = View3DAttributes()
	c2.viewNormal = (0, 0, 1)
	c2.focus = (0.292, 0.292, 0.219)
	c2.viewUp = (0, 1, 0)
	c2.viewAngle = 30
	c2.parallelScale = 0.467428
	c2.nearPlane = -0.934856
	c2.farPlane = 0.934856
	c2.imagePan = (0, 0)
	c2.imageZoom = 1

 	cpts = (c0, c1, c2) #, c2, c3, c4, c5, c6)
	x=[]
	for i in range(3):
		x = x + [float(i) / float(2.)]
 
    # Animate the camera. Note that we use the new built-in EvalCubicSpline
    # function which takes a t value from [0,1] a tuple of t values and a tuple
    # of control points. In this case, the control points are View3DAttributes
    # objects that we are using to animate the camera but they can be any object
    # that supports +, * operators.
	nsteps = 50
	for i in range(nsteps):
		t = float(i) / float(nsteps - 1)
		c = EvalCubicSpline(t, x, cpts)
		c.nearPlane = -34.461
		c.farPlane = 34.461
		SetView3D(c)
		for j in range(4):
			sw.fileName="frames/m%02d" %(frame_idx)
			frame_idx = frame_idx + 1
			SetSaveWindowAttributes(sw)
			MySaveWindow()




def fly():
 # Begin spontaneous state
    print("setting up fly")
    global frame_idx
    c0 = View3DAttributes()
    c0.viewNormal = (0, 0, 1)
    c0.focus = (0.292, 0.292, 0.219)
    c0.viewUp = (0, 1, 0)
    c0.viewAngle = 30
    c0.parallelScale = 0.467428
    c0.nearPlane = -0.934856
    c0.farPlane = 0.934856
    c0.perspective = 1
    # End spontaneous state
    
    # Begin spontaneous state
    c1 = View3DAttributes()
    c1.viewNormal = (0.803177, 0.0509209, 0.59356)
    c1.focus = (0.292, 0.292, 0.219)
    c1.viewUp = (-0.0436263, 0.998693, -0.0266437)
    c1.viewAngle = 30
    c1.parallelScale = 0.467428
    c1.nearPlane = -0.934856
    c1.farPlane = 0.934856
    c1.imagePan = (0, 0)
    c1.imageZoom = 1
    c1.perspective = 1
    # End spontaneous state


    # Begin spontaneous state
    c2 = View3DAttributes()
    c2.viewNormal = (0.996553, 0.0752248, 0.0349895)
    c2.focus = (0.292, 0.292, 0.219)
    c2.viewUp = (0, 1, 0)
    c2.viewAngle = 30
    c2.parallelScale = 0.467428
    c2.nearPlane = -0.934856
    c2.farPlane = 0.934856
    c2.imagePan = (0, 0)
    c2.imageZoom = 1
    c2.perspective = 1
    # End spontaneous state

 
    # Create a tuple of camera values and x values. The x values are weights
    # that help to determine where in [0,1] the control points occur.
    cpts = (c0, c1, c2) #, c2, c3, c4, c5, c6)
    x=[]
    for i in range(3):
        x = x + [float(i) / float(2.)]
 
    # Animate the camera. Note that we use the new built-in EvalCubicSpline
    # function which takes a t value from [0,1] a tuple of t values and a tuple
    # of control points. In this case, the control points are View3DAttributes
    # objects that we are using to animate the camera but they can be any object
    # that supports +, * operators.
    nsteps = 50
    for i in range(nsteps):
        t = float(i) / float(nsteps - 1)
        c = EvalCubicSpline(t, x, cpts)
        c.nearPlane = -34.461
        c.farPlane = 34.461
        SetView3D(c)
        for i in range(4):
	        sw.fileName="frames/m%02d" %(frame_idx)
	    	frame_idx = frame_idx + 1
	    	SetSaveWindowAttributes(sw)
	    	MySaveWindow()



def fly2():
    global frame_idx
    c0 = View3DAttributes()
    c0.viewNormal = (0.996553, 0.0752248, 0.0349895)
    c0.focus = (0.292, 0.292, 0.219)
    c0.viewUp = (0, 1, 0)
    c0.viewAngle = 30
    c0.parallelScale = 0.467428
    c0.nearPlane = -0.934856
    c0.farPlane = 0.934856
    c0.imagePan = (0, 0)
    c0.imageZoom = 1
    c0.perspective = 1
    # End spontaneous state
# Begin spontaneous state
    c1 = View3DAttributes()
    c1.viewNormal = (0.706443, -0.707389, 0.0232047)
    c1.focus = (0.292, 0.292, 0.219)
    c1.viewUp = (0.707631, 0.706574, -0.00338448)
    c1.viewAngle = 30
    c1.parallelScale = 0.467428
    c1.nearPlane = -0.934856
    c1.farPlane = 0.934856
    c1.imagePan = (0, 0)
    c1.imageZoom = 1
    # End spontaneous state

# Begin spontaneous state
    c2 = View3DAttributes()
    c2.viewNormal = (0.00921269, -0.998438, 0.0550977)
    c2.focus = (0.292, 0.292, 0.219)
    c2.viewUp = (0.999934, 0.00881729, -0.00741509)
    c2.viewAngle = 30
    c2.parallelScale = 0.467428
    c2.nearPlane = -0.934856
    c2.farPlane = 0.934856
    c2.imagePan = (0, 0)
    c2.imageZoom = 1
# End spontaneous state

 
    # Create a tuple of camera values and x values. The x values are weights
    # that help to determine where in [0,1] the control points occur.
    cpts = (c0, c1, c2) #, c2, c3, c4, c5, c6)
    x=[]
    for i in range(3):
        x = x + [float(i) / float(2.)]
 
    # Animate the camera. Note that we use the new built-in EvalCubicSpline
    # function which takes a t value from [0,1] a tuple of t values and a tuple
    # of control points. In this case, the control points are View3DAttributes
    # objects that we are using to animate the camera but they can be any object
    # that supports +, * operators.
    nsteps = 35
    for i in range(nsteps):
        t = float(i) / float(nsteps - 1)
        c = EvalCubicSpline(t, x, cpts)
        c.nearPlane = -34.461
        c.farPlane = 34.461
        SetView3D(c)
        for j in range(3):
	        sw.fileName="frames/m%02d" %(frame_idx)
	    	frame_idx = frame_idx + 1
	    	SetSaveWindowAttributes(sw)
	    	MySaveWindow()



def fly3():
    global frame_idx
# Begin spontaneous state
    c0 = View3DAttributes()
    c0.viewNormal = (-0.00729852, 0.00161159, 0.999972)
    c0.focus = (0.292, 0.292, 0.219)
    c0.viewUp = (0.00143997, 0.999998, -0.00160112)
    c0.viewAngle = 30
    c0.parallelScale = 0.467428
    c0.nearPlane = -0.934856
    c0.farPlane = 0.934856
# End spontaneous state

# Begin spontaneous state
    c1 = View3DAttributes()
    c1.viewNormal = (0.226669, 0.0151431, 0.973854)
    c1.focus = (0.292, 0.292, 0.219)
    c1.viewUp = (0.00634829, 0.999835, -0.0170247)
    c1.viewAngle = 30
# End spontaneous state

# Begin spontaneous state
    c2 = View3DAttributes()
    c2.viewNormal = (0.439761, 0.0705583, 0.895339)
    c2.focus = (0.292, 0.292, 0.219)
    c2.viewUp = (-0.0222346, 0.997459, -0.0676851)
    c2.viewAngle = 30
    c2.imageZoom = 1.5
# End spontaneous state



 
    # Create a tuple of camera values and x values. The x values are weights
    # that help to determine where in [0,1] the control points occur.
    cpts = (c0, c1, c2) #, c2, c3, c4, c5, c6)
    x=[]
    for i in range(3):
        x = x + [float(i) / float(2.)]
 
    # Animate the camera. Note that we use the new built-in EvalCubicSpline
    # function which takes a t value from [0,1] a tuple of t values and a tuple
    # of control points. In this case, the control points are View3DAttributes
    # objects that we are using to animate the camera but they can be any object
    # that supports +, * operators.
    nsteps = 25
    for i in range(nsteps):
        t = float(i) / float(nsteps - 1)
        c = EvalCubicSpline(t, x, cpts)
        c.nearPlane = -34.461
        c.farPlane = 34.461
        SetView3D(c)
        for j in range(3):
	        sw.fileName="frames/m%02d" %(frame_idx)
	    	frame_idx = frame_idx + 1
	    	SetSaveWindowAttributes(sw)
	    	MySaveWindow()


zoom()
#for i in range(TimeSliderGetNStates()):
for i in range(40):
    TimeSliderSetState(i)
    for j in range(4):
	    sw.fileName="frames/m%02d" %(frame_idx)
	    frame_idx = frame_idx + 1
	    SetSaveWindowAttributes(sw)
	    MySaveWindow()
    if(i == 10):
    	fly()
    if(i == 20):
        setContours()
    if(i == 30):
        fly2()

DeleteActivePlots()
ResetView()
SetTimeSliderState(0)

OpenDatabase("localhost:/home/jesse/cis410/final/water/dbreak3d_fluid.visit", 0)
TimeSliderNextState()
AddPlot("Vector", "U", 1, 1)
AddPlot("Volume", "alpha1", 1, 1)


VectorAtts = VectorAttributes()
VectorAtts.glyphLocation = VectorAtts.AdaptsToMeshResolution  # AdaptsToMeshResolution, UniformInSpace
VectorAtts.useStride = 0
VectorAtts.stride = 1
VectorAtts.nVectors = 400
VectorAtts.lineStyle = VectorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
VectorAtts.lineWidth = 0
VectorAtts.scale = 0.25
VectorAtts.scaleByMagnitude = 1
VectorAtts.autoScale = 1
VectorAtts.headSize = 0.5
VectorAtts.headOn = 1
VectorAtts.colorByMag = 1
VectorAtts.useLegend = 1
VectorAtts.vectorColor = (0, 0, 0, 255)
VectorAtts.colorTableName = "Default"
VectorAtts.invertColorTable = 0
VectorAtts.vectorOrigin = VectorAtts.Tail  # Head, Middle, Tail
VectorAtts.minFlag = 0
VectorAtts.maxFlag = 0
VectorAtts.limitsMode = VectorAtts.OriginalData  # OriginalData, CurrentPlot
VectorAtts.min = 0
VectorAtts.max = 1
VectorAtts.lineStem = VectorAtts.Line  # Cylinder, Line
VectorAtts.geometryQuality = VectorAtts.Fast  # Fast, High
VectorAtts.stemWidth = 0.08
VectorAtts.origOnly = 1
VectorAtts.glyphType = VectorAtts.Arrow  # Arrow, Ellipsoid
SetPlotOptions(VectorAtts)
VectorAtts = VectorAttributes()
VectorAtts.glyphLocation = VectorAtts.AdaptsToMeshResolution  # AdaptsToMeshResolution, UniformInSpace
VectorAtts.useStride = 0
VectorAtts.stride = 1
VectorAtts.nVectors = 400
VectorAtts.lineStyle = VectorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
VectorAtts.lineWidth = 0
VectorAtts.scale = 0.25
VectorAtts.scaleByMagnitude = 1
VectorAtts.autoScale = 1
VectorAtts.headSize = 0.5
VectorAtts.headOn = 1
VectorAtts.colorByMag = 1
VectorAtts.useLegend = 1
VectorAtts.vectorColor = (0, 0, 0, 255)
VectorAtts.colorTableName = "OrRd"
VectorAtts.invertColorTable = 0
VectorAtts.vectorOrigin = VectorAtts.Tail  # Head, Middle, Tail
VectorAtts.minFlag = 0
VectorAtts.maxFlag = 0
VectorAtts.limitsMode = VectorAtts.OriginalData  # OriginalData, CurrentPlot
VectorAtts.min = 0
VectorAtts.max = 1
VectorAtts.lineStem = VectorAtts.Line  # Cylinder, Line
VectorAtts.geometryQuality = VectorAtts.Fast  # Fast, High
VectorAtts.stemWidth = 0.08
VectorAtts.origOnly = 1
VectorAtts.glyphType = VectorAtts.Arrow  # Arrow, Ellipsoid
SetPlotOptions(VectorAtts)
VolumeAtts = VolumeAttributes()
VolumeAtts.legendFlag = 1
VolumeAtts.lightingFlag = 1
VolumeAtts.colorControlPoints.GetControlPoints(0).colors = (0, 0, 255, 255)
VolumeAtts.colorControlPoints.GetControlPoints(0).position = 0
VolumeAtts.colorControlPoints.GetControlPoints(1).colors = (0, 255, 255, 255)
VolumeAtts.colorControlPoints.GetControlPoints(1).position = 0.25
VolumeAtts.colorControlPoints.GetControlPoints(2).colors = (0, 255, 0, 255)
VolumeAtts.colorControlPoints.GetControlPoints(2).position = 0.5
VolumeAtts.colorControlPoints.GetControlPoints(3).colors = (255, 255, 0, 255)
VolumeAtts.colorControlPoints.GetControlPoints(3).position = 0.75
VolumeAtts.colorControlPoints.GetControlPoints(4).colors = (255, 0, 0, 255)
VolumeAtts.colorControlPoints.GetControlPoints(4).position = 1
VolumeAtts.colorControlPoints.smoothing = VolumeAtts.colorControlPoints.Linear  # None, Linear, CubicSpline
VolumeAtts.colorControlPoints.equalSpacingFlag = 0
VolumeAtts.colorControlPoints.discreteFlag = 0
VolumeAtts.colorControlPoints.categoryName = ""
VolumeAtts.opacityAttenuation = 1
VolumeAtts.opacityMode = VolumeAtts.FreeformMode  # FreeformMode, GaussianMode, ColorTableMode
#controlPoints does not contain any GaussianControlPoint objects.
VolumeAtts.resampleFlag = 1
VolumeAtts.resampleTarget = 50000
VolumeAtts.opacityVariable = "default"
VolumeAtts.compactVariable = "default"
VolumeAtts.freeformOpacity = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255)
VolumeAtts.useColorVarMin = 0
VolumeAtts.colorVarMin = 0
VolumeAtts.useColorVarMax = 0
VolumeAtts.colorVarMax = 0
VolumeAtts.useOpacityVarMin = 0
VolumeAtts.opacityVarMin = 0
VolumeAtts.useOpacityVarMax = 0
VolumeAtts.opacityVarMax = 0
VolumeAtts.smoothData = 0
VolumeAtts.samplesPerRay = 500
VolumeAtts.rendererType = VolumeAtts.Texture3D  # Splatting, Texture3D, RayCasting, RayCastingIntegration, SLIVR, RayCastingSLIVR, Tuvok
VolumeAtts.gradientType = VolumeAtts.SobelOperator  # CenteredDifferences, SobelOperator
VolumeAtts.num3DSlices = 200
VolumeAtts.scaling = VolumeAtts.Linear  # Linear, Log, Skew
VolumeAtts.skewFactor = 1
VolumeAtts.limitsMode = VolumeAtts.OriginalData  # OriginalData, CurrentPlot
VolumeAtts.sampling = VolumeAtts.Rasterization  # KernelBased, Rasterization, Trilinear
VolumeAtts.rendererSamples = 3
#transferFunction2DWidgets does not contain any TransferFunctionWidget objects.
VolumeAtts.transferFunctionDim = 1
VolumeAtts.lowGradientLightingReduction = VolumeAtts.Higher  # Off, Lowest, Lower, Low, Medium, High, Higher, Highest
VolumeAtts.lowGradientLightingClampFlag = 0
VolumeAtts.lowGradientLightingClampValue = 1
VolumeAtts.materialProperties = (0.4, 0.75, 0, 15)
SetPlotOptions(VolumeAtts)

DrawPlots()


for i in range(1, 40):
    TimeSliderSetState(i)
    for j in range(4):
	    sw.fileName="frames/m%02d" %(frame_idx)
	    frame_idx = frame_idx + 1
	    SetSaveWindowAttributes(sw)
	    MySaveWindow()
    if(i == 10):
        fly3()

print(frame_idx)
import sys
sys.exit()
