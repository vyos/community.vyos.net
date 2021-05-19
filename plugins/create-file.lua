file_name = config["name"]
content = config["content"]

file_path = Sys.join_path(build_dir, file_name)
Sys.write_file(file_path, content)
