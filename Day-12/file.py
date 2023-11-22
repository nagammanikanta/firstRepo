def update_server_config(file_path, key, value):
      with open(file_path, 'r') as file:
        lines = file.readlines()