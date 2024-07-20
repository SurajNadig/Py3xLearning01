# WALK in to Directories
# Listing all the files of directories

import os

for root,dir,files in os.walk('/Python Practice/OOPS'):
    print(f"Root is {root}")
    print(f"Dir are {dir}")
    print(f"Files are {files}")

#Sometimes this is useful.......