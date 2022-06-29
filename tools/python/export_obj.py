import csv, os
### Takes advantage of ESRI's 3D Object Layers.  Finds the Virtual Folder 
# associated with a 3D Objects feature class, and it copies the obj folders
# to a folder identified by the user. 


from shutil import copyfile
from pathlib import Path

# If I can import ArcPy, then I'm running within ArcMap
try:
    import arcpy
    inarc = True
    arcpy.AddMessage("Detect running in ArcGIS")
except ImportError as e:
    inarc = False
    print("Running outside of ArcMap")
    pass  # module doesn't exist, deal with it.


#These hardcoded values are for testing 
esrivfolder = r'C:\Users\pbcote\3D Objects\ESRI3DO\ModelMgt_20210127\Edits\test3do_b4edits'
#Path/Location of the source directory
objfolder = r'f:\current_work\projects\Boston\Bos3d\Bos3dDevpbc\Workflows\ModelMgt_20201214\ModelBatch\test3do\obj'  
#Path to the destination folder
modelscsv = r'f:\current_work\projects\Boston\Bos3d\Bos3dDevpbc\Workflows\ModelMgt_20201214\ModelBatch\test3do\models.csv'


def arcPrint(msg):
    print(msg)
    if inarc:  # arcPrint writes to ArcMap console. 
        arcpy.AddMessage(msg)

def load_esri_args():
    esrivfolder = arcpy.GetParameterAsText(0)
    # The folder towrite output
    objfolder = arcpy.GetParameterAsText(1)
    # a csv file of attributes that, at least contains a Model_ID field 
    modelscsv = arcpy.GetParameterAsText(2)    

if inarc:  # Get arguments from geoprocessing model context.
    load_esri_args()


if os.path.isdir(esrivfolder):
#if os.system('dir ' + esrivfolder )
    arcPrint(esrivfolder + " Exists")
else:
    arcPrint(esrivfolder + " Does not Exist")
    exit()

if os.path.isdir(objfolder):
    arcPrint(objfolder + " Exists")
else:
    arcPrint(objfolder + " Does not Exists")
    os.system('mkdir ' +  objfolder)

## This is where stuff happens
## Go through CSV file and for each row, copy the obj file 
## Substituting the model id for the file name.
## Future feature: copy only if destination file does not exist
with open(modelscsv, mode='r', encoding='utf-8-sig') as csvfile:
     spamreader = csv.DictReader(csvfile, delimiter=',')
     for row in spamreader:
         arcPrint (row.keys())
         #print('* '.join(row))
         arcPrint('OID_ is:' + row['OBJECTID'] + ' Tile is: ' + row['Tile'] + ' Model_ID is: ' + row['Model_ID'])
         src = os.path.join(esrivfolder, row['OBJECTID'],'esriGeometryMultiPatch.obj')
         dstdir = os.path.join(objfolder,row['Tile'],row['Model_ID'],'obj' )
         Path(dstdir).mkdir(parents=True, exist_ok=True)
         dst = os.path.join(dstdir, row['Model_ID'] + '.obj')
         arcPrint("Source: " + src + " Dest: " + dst)
         
         copycommand = 'copy ' + src + ' ' + dst
         arcPrint("Copycommand is: " + copycommand)
         copyfile(src, dst)
         #os.system(copycommand)


