# Copy's a new ModelFinder.htm into the ModelCatalog folders within all of the ModelCatalog_OBJ folders

import os, shutil

path = r'F:\current_work\projects\Boston\Bos3d\Bos3dDevpbc\Bos3d_City_Model_Stage\Bos3d_Tiled_Data\Bos3d_ModelCollection_OBJ'

newcat = r'F:\current_work\projects\Boston\Bos3d\Bos3dDevpbc\Bos3d_City_Model_Stage\Bos3d_Tiled_Data\Bos3d_ModelCollection_OBJ\ModelCatalogTemplate'

for f in os.scandir(path): 
    #Test first!
    #if f.is_dir() and f.name[:3] == 'AAA':
    if f.is_dir() and f.name[:3] == 'BOS':
        print(f)
        catfolder = os.path.join(f.path, 'ModelCatalog')
        print("Folder is " + catfolder )
        
        print("Replacing " + catfolder + r'\ModelFinder.htm') 
        shutil.copy2(newcat + r'\ModelFinder.htm', catfolder + r'\ModelFinder.htm') 

        #print("Removing " + catfolder + r'\data_dictionary.js' ) 
        #shutil.rmtree(catfolder + r'\css_js')
        #print("Replacing " + catfolder + r'\css_js' )
        #shutil.copytree(newcat + r'\css_js', catfolder + r'\css_js')
    
        #print("Removing " + catfolder + r'\data_dictionary.js' ) 
        #os.remove(catfolder + r'\data_dictionary.js')
        print("Copying " + catfolder + r'\data_dictionary_copy.js')
        shutil.copy2(newcat + r'\data_dictionary_copy.js', catfolder + r'\data_dictionary_copy.js') 
    

    



