# Import system modules
import arcpy

# Set the parameters
message = arcpy.GetParameterAsText(0)
level = arcpy.GetParameterAsText(1)


if level == "warn":
    arcpy.AddWarning(message)

elif level == "remark":
    arcpy.AddMessage(message)

elif level == "error":
    arcpy.AddError(message)

else:
    arcpy.AddError("Value for level must be in warn, remark, or error." )
       

