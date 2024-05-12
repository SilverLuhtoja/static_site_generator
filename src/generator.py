
import os

from html_setup import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    h1_count = 0
    title = ""
    for line in lines: 
        if line.startswith("# "):
            h1_count += 1
            title = line.split("# ")[1]
    if h1_count != 1 or title == "":
        raise ValueError("No title present, provide [ # your_title ]")
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_path_content = getFileContent(from_path)
    template_path_content = getFileContent(template_path)

    generated_html = markdown_to_html_node(from_path_content).to_html()
    html_title = extract_title(from_path_content)
    
    template_path_content = template_path_content.replace("{{ Title }}", html_title)
    template_path_content = template_path_content.replace("{{ Content }}", generated_html)
    print(template_path_content)
    print(generated_html)
    
    writeFile(dest_path, template_path_content)

def writeFile(dest_path, content):
    dir_path = os.path.dirname(dest_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    file  = open(dest_path, 'w')
    
    file.write(content)
    file.close()
    print(file)

def getFileContent(file_path):
    content = ""
    if os.path.exists(file_path):
        for line in open(file_path, 'r'):
            if "{{ Content }}" in line:
                content += line.strip() + "\n"
                continue
            content += line
                
        return content
    raise OSError("No file in this path: ", file_path)
