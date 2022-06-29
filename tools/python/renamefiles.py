# This is a program torename files in a directory usng regular expressions

import glob, re, os
from shutil import move

print('Hello world')

dir = r'F:\current_work\projects\Boston\Bos3d\Bos3dDevpbc\Workflows\create_grid\bos3d_masp_exports\tile_data\bos3d_orthophoto_2020_jpg'

count = 0
for filename in glob.glob(dir + '\*jpg.jpg*'):
    new_name = re.sub('jpg.jpg', 'jpg', filename)
    count += 1
    print(str(count) + " " + os.path.basename(filename) + ' Becomes:' + os.path.basename(new_name))
    move(filename, new_name)