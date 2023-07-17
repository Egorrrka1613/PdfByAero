import os


def get_path_to_file(file_name: str):
    project_path = os.path.dirname(os.path.abspath(__file__))
    data_dir_path = os.path.join(project_path, "../data/")
    return os.path.join(data_dir_path, file_name)
