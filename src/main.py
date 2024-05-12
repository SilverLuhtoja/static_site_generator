import os
import shutil

from generator import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def copy_files_recursive(source_path, to_path):
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
            copy_files_recursive(from_path, destination_path)

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    
    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)
    
main()
