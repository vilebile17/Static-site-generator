import os, shutil

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
            directories = path_to_static.split("/")
            print(directories)
            current_path = "./public"
            for i in range(len(directories) - 1):
                print(f"{current_path}/{directories[i]}")
                os.mkdir(f"{current_path}/{directories[i]}")
                current_path = f"{current_path}/{directories[i]}"
            shutil.copy(file, current_path)




     

files = get_file_list()
copy_to_public(files)
