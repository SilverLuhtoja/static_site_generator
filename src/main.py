import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"

def recurse_copy(source_path, to_path):
    if not os.path.exists(to_path):
        os.mkdir(to_path)
    
    for filepath in os.listdir(source_path):
        from_path = os.path.join(source_path, filepath)
        destination_path = os.path.join(to_path, filepath)
        if os.path.isfile(from_path):
            print("file:", filepath)
            shutil.copy(from_path, destination_path)
        else:
            print("directory:", from_path)
            recurse_copy(from_path, destination_path)

def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
        
    recurse_copy(dir_path_static, dir_path_public)
main()
