import arcpy, os

# Prints to the GeoProcessing Results Window
def arcPrint(message):
    arcpy.AddMessage(message)
    print(message)

arcPrint("Hello World")

# These arguments are provided by the geoprocessing model
mapName = arcpy.GetParameterAsText(0)
outfolder = arcpy.GetParameterAsText(1)
fileNameStub = arcpy.GetParameterAsText(2)
dpi = arcpy.GetParameterAsText(3)
format = arcpy.GetParameterAsText(4)
tilePoly  = arcpy.GetParameterAsText(5)


#outfolder = os.path.split(fileName)[0]
if (os.path.isdir(outfolder)): arcPrint ("Tile path is " + outfolder)
else : arcPrint ("Tile folder " + outfolder +  "does not exist")
if arcpy.Exists(tilePoly) : arcPrint ("Tile Shape file is " + tilePoly)
else : arcPrint ("Shape file " + tilePoly +  "does not exist")
desc = arcpy.Describe(tilePoly)
spatRef = desc.spatialReference
arcPrint ("Shape type is " + desc.shapeType)
arcPrint("FIlename stub is: "  + fileNameStub)



# Define Handy Subroutines

def expPng(fileName, dpi):
    arcPrint("exporting..." + tileImage)
    mf.exportToPNG(outFile, 2400, True, '8-BIT_ADAPTIVE_PALETTE')


def createWorldFile(tileImage,tileExtent, suffix):
    imageRowCountResult = arcpy.GetRasterProperties_management(tileImage, "ROWCOUNT")
    imageRowCount = imageRowCountResult.getOutput(0)
    xMin = tileExtent.XMin
    xMax = tileExtent.XMax
    yMax = tileExtent.YMax

    cellSize = (xMax - xMin) / float(imageRowCount)

    # This is a boiler-plate world file that assumes that the image and the extent are both square
    # and there is no rotation required.
    preFileName = tileImage.split('.')[0]
    wldFileName = preFileName + suffix
    worldFile = open(wldFileName,'w')
    worldFileLine1 = cellSize
    worldFileLine2 = 0.00000000000000
    worldFileLine3 = 0.00000000000000
    worldFileLine4 = -cellSize
    worldFileLine5 = repr(xMin + cellSize / 2.0)
    worldFileLine6 = repr(yMax - cellSize / 2.0)
    arcPrint("Creating World File... Rowcount: " + str(imageRowCount) + ", XMin: " + repr(xMin) + ", YMax: " + repr(yMax))
    worldFile.write(str(worldFileLine1)+'\n'+str(worldFileLine2)+'\n'+str(worldFileLine3)+'\n'+str(worldFileLine4)+'\n'+str(worldFileLine5)+'\n'+str(worldFileLine6)+'\n')
    worldFile.close()
    # Here we write the .aux.xml file that contains the projection information.  The spatial reference has
    # been scraped form the data frame above.





# This is the main program.

# Declare what layout, map and map frame to use. 
aprx = arcpy.mp.ArcGISProject("CURRENT")
#m = aprx.listMaps(mapName)[0]
lyt = aprx.listLayouts("groundplans")[0]
#m = aprx.listMaps(mapName)[0]
#lyr = m.listLayers(tilePoly)[0]
mapframes = lyt.listElements("MAPFRAME_ELEMENT")

arcPrint("Map Frames:")
for frame in mapframes :
    print(frame.name)

mf = lyt.listElements("MAPFRAME_ELEMENT", mapName)[0]

# Count rows in the table
arcpy.MakeTableView_management(tilePoly,"tmpLayer")
rowCount = int(arcpy.GetCount_management("tmpLayer").getOutput(0))
arcPrint("looking at " + str(rowCount) + " rows")

cursor = arcpy.da.SearchCursor(tilePoly, ['SHAPE@', 'tile_id'])

for row in cursor:
    arcPrint("Now processing " + row[1])
    tileExtent = row[0].extent
    arcPrint('XMin: {}, YMin: {}'.format(tileExtent.XMin, tileExtent.YMin))
    arcPrint('XMax: {}, YMax: {}'.format(tileExtent.XMax, tileExtent.YMax))
    mf.camera.setExtent(tileExtent)

    #tile_layer=m.listLayers("tilePoly")[0]
    fileName = row[1] + "_" + fileNameStub 
    outfile = os.path.join(outfolder,fileName)
    arcPrint("Exporting: " + outfile)
    mf.exportToJPEG (outfile, resolution = 200, jpeg_quality = 95)
    arcPrint("Creatng World File " )
    createWorldFile(outfile, tileExtent, ".jgw")
    arcpy.management.DefineProjection(outfile, spatRef)


del cursor, row
arcPrint("Thank you.  Good night.")

