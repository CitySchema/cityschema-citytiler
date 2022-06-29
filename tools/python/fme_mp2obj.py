# The script takes a geodatabase multipatch feature class and converts it to 
# a wavefront obj file using an FME workspace. 

import csv, os, sys
from shutil import copyfile
from pathlib import Path

print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
#print("PYTHONPATH is " + os.environ['PYTHONPATH'])



# If we are running in an ESRI geoprocesing model...
try:
    import arcpy
    inarc = True
    arcpy.AddMessage("Detect running in ArcGIS")
except ImportError as e:
    inarc = False
    print("Running outside of ArcMap")
    pass  # module doesn't exist, deal with it.

def arcPrint(msg):
    print(msg)
    if inarc:
        arcpy.AddMessage(msg)

# This ibrary contains required FME code. 
fmePath = r'C:\Program Files\FME_2020\fmeobjects\python37'

if os.path.isdir(fmePath):
    #if os.system('dir ' + esrivfolder )
    arcPrint("Found fme python module at " + fmePath)

    sys.path.append(r'C:\Program Files\FME_2020\fmepython37')
    sys.path.append(r'C:\Python37\DLLs')

    sys.path.append(r'C:\Program Files\FME_2020\plugins')
    sys.path.append(r'C:\Program Files\FME_2020')
    sys.path.append(r'C:\Program Files\FME_2020\python')
    sys.path.append(r'C:\Program Files\FME_2020\python\python37')
    sys.path.append(r'C:\Program Files\FME_2020\fmeobjects\python37')
    os.environ['PYTHONPATH'] = fmePath
    import fmeobjects
    arcPrint("Successfully loaded FMEObjects.")
else:
    arcPrint("FME Objects folder not found at: " + fmePath)
    exit()


#These hardcoded values are for testing 
featureclass = r'C:\Users\pbcote\3D Objects\ESRI3DO\ModelMgt_20210127\Edits\test3do_b4edits'
#Path/Location of the source directory
outputfolder = r'f:\current_work\projects\Boston\Bos3d\Bos3dDevpbc\Workflows\ModelMgt_20201214\ModelBatch\testing'  
#Path to the destination folder



if inarc:
    geodatabase = arcpy.GetParameterAsText(0)
    batchfolder = arcpy.GetParameterAsText(1)



#if os.path.isdir(esrivfolder):
#if os.system('dir ' + esrivfolder )
#    arcPrint(esrivfolder + " Exists")
#else:
#    arcPrint(esrivfolder + " Does not Exists")
#    exit()

if os.path.isdir(outputfolder):
    arcPrint(outputfolder + " Exists")
else:
    arcPrint(outputfolder + " Does not Exists")
    os.system('mkdir ' +  outputfolder)

runner = fmeobjects.FMEWorkspaceRunner()
workspace = r'F:\current_work\projects\Boston\Bos3d\Bos3dDevpbc\Workflows\ModelMgt_20201214\Tools\fme\gdb_mp2obj.fmw'
parameters = {}
parameters['GeoDatabase'] = r'F:\current_work\projects\Boston\Bos3d\Bos3dDevpbc\Workflows\ModelMgt_20201214\Scratch\Scratch.gdb'
parameters['BatchFolder'] = r'F:\current_work\projects\Boston\Bos3d\Bos3dDevpbc\Workflows\ModelMgt_20201214\ModelBatch\Testing' 

try:
    # Run Workspace with parameters set in above directory
    runner.runWithParameters(workspace, parameters)
    # or use promptRun to prompt for published parameters
    #runner.promptRun(workspace)
except fmeobjects.FMEException as ex:
    # Print out FME Exception if workspace failed
    arcPrint(ex.message)
else:
    #Tell user the workspace ran
    arcPrint('The Workspace %s ran successfully'.format(workspace))
# get rid of FMEWorkspace runner so we don't leave an FME process running
runner = None



