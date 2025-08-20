import os, shutil
from markdown_to_html_node import markdown_to_html_node
from extract_markdown_links import extract_title

def get_file_list(first_run=True, current_dir="./static"):
    # these two if statements are to make sure that the public directory is empty
    if first_run:
        if not os.path.exists("./public"):
            os.mkdir("./public")
        else:
            shutil.rmtree("./public")
            os.mkdir("./public")

    file_list = []
    static_files = os.listdir(current_dir)
    for file in static_files:
        if os.path.isfile(f'{current_dir}/{file}'):
            file_list.append(f"{current_dir}/{file}")
        else:
            file_list.extend(get_file_list(False, f"{current_dir}/{file}"))

    return file_list
    

def copy_to_public(file_list):
    for file in file_list:
        path_to_static = file.split("./static/",1)[1]
        if not "/" in path_to_static:
            shutil.copy(file, "./public")
        else:
            directories_only = os.path.dirname(file.replace("static", "public"))
            os.makedirs(directories_only, exist_ok=True)
            shutil.copy(file, file.replace("static", "public"))



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown_content = f.read()
    with open(template_path, "r") as g:
        template_content = g.read()

    html_node = markdown_to_html_node(markdown_content)
    print("Successfully made a html node")
    html_content = html_node.to_html()
    print("Successfully converted the html node into a string object")
    
    title = extract_title(markdown_content)
    print("Successfully extracted the title, it should be ", title)

    html_page = template_content.replace("{{ Title }}", title)
    html_page = html_page.replace("{{ Content }}", html_content)
    print("Filled in the html template")

    directories_only = os.path.dirname(dest_path)
    os.makedirs(directories_only, exist_ok=True)
    with open(dest_path, "w") as f:
        print(html_page, file=f)
    print("Successfully wrote the file!\n")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isdir(dir_path_content):
        for file in os.listdir(dir_path_content):
            print(f"I'm going to go searching in {os.path.join(dest_dir_path, file)}")
            generate_pages_recursive(os.path.join(dir_path_content, file), template_path, os.path.join(dest_dir_path, file))
    
    elif os.path.isfile(dir_path_content):
        if dir_path_content.endswith(".md"):
            relative_path = os.path.relpath(dest_dir_path, "content").replace(".md", ".html")
            dest_path = os.path.join("public", relative_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            generate_page(dir_path_content, template_path, dest_path) 
    else:
        raise ValueError(f"Somehow, the selected object : {dir_path_content} isn't a directory nor a file")

    

    


files = get_file_list()
copy_to_public(files)
generate_pages_recursive("content", "template.html", "public")
