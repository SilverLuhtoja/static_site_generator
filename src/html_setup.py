def markdown_to_html_node(markdown):
    pass

def quote_block_to_html(markdown):
    return f"<blockquote>{markdown[2:]}</blockquote>"

def un_list_to_html(markdown):
    lines = markdown.split("\n")
    li_list = ""
    for line in lines:
        li_list += f"<li>{line[2:]}</li>"
    return f"<ul>{li_list}</ul>"

def ord_list_to_html(markdown):
    lines = markdown.split("\n")
    li_list = ""
    for line in lines:
        li_list += f"<li>{line[3:]}</li>"
    return f"<ol>{li_list}</ol>"


def code_block_to_html(markdown):
    return f"<code><pre>{markdown[3:-3]}</pre></code>"

def heading_block_to_html(markdown):
    lines = markdown.split(" ")
    heading_nr = len(lines[0])
    return f"<h{heading_nr}>{markdown[heading_nr+1:]}</h{heading_nr}>"

def paragraph_block_to_html(markdown):
    return f"<p>{markdown}</p>"