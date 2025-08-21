import os, shutil, sys
from markdown_to_html_node import markdown_to_html_node
from extract_markdown_links import extract_title

def get_file_list(first_run=True, current_dir="./static"):
    # these two if statements are to make sure that the public directory is empty
    if first_run:
        if not os.path.exists("./docs"):
            os.mkdir("./docs")
        else:
            shutil.rmtree("./docs")
            os.mkdir("./docs")

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
            shutil.copy(file, "./docs")
        else:
            directories_only = os.path.dirname(file.replace("static", "docs"))
            os.makedirs(directories_only, exist_ok=True)
            shutil.copy(file, file.replace("static", "docs"))



def generate_page(from_path, template_path, dest_path, basepath):
    print("base path is : ", basepath)

    with open(from_path, "r") as f:
        markdown_content = f.read()
    with open(template_path, "r") as g:
        template_content = g.read()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    title = extract_title(markdown_content)

    html_page = template_content.replace("{{ Title }}", title)
    html_page = html_page.replace("{{ Content }}", html_content)
    html_page = html_page.replace('href="/', f'href="{basepath}')
    html_page = html_page.replace('src="/', f'src="{basepath}')

    directories_only = os.path.dirname(dest_path)
    os.makedirs(directories_only, exist_ok=True)
    with open(dest_path, "w") as f:
        print(html_page, file=f)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if os.path.isdir(dir_path_content):
        for file in os.listdir(dir_path_content):
            generate_pages_recursive(os.path.join(dir_path_content, file), template_path, os.path.join(dest_dir_path, file), basepath)
    
    elif os.path.isfile(dir_path_content):
        if dir_path_content.endswith(".md"):
            relative_path = os.path.relpath(dest_dir_path, "content").replace(".md", ".html")
            dest_path = os.path.join("docs", relative_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            generate_page(dir_path_content, template_path, dest_path, basepath) 
    else:
        raise ValueError(f"Somehow, the selected object : {dir_path_content} isn't a directory nor a file")

    

    
def main():
    try:
        basepath = sys.argv[1]
    except:
        basepath = "/"

    files = get_file_list()
    copy_to_public(files)
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()
