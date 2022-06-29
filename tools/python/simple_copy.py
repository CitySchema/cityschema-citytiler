#attempts to copy folders out of virtual filesystem

import shutil, errno

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

src_dir = r'c:\Users\pbcote\3D Objects\ESRI3DO\ModelMgt_20210127\Edits\edits_before'
#Path/Location of the source directory

dst_dir = r'f:\current_work\projects\Boston\Bos3d\Bos3dDevpbc\Workflows\ModelMgt_20201214\ModelBatch\test3do\apricot\\'  #Path to the destination folder


copyanything(src_dir,dst_dir)

