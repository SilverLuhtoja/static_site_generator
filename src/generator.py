
def extract_title(markdown):
    lines = markdown.split("\n")
    h1_count = 0
    title = ""
    for line in lines: 
        if line.startswith("# "):
            h1_count += 1
            title = line.split(" ")[1]
    if h1_count != 1 or title == "":
        raise ValueError("No title present, provide [ # your_title ]")
    return title

def generate_page(from_path, template_path, dest_path):
    pass
