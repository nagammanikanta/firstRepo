def update_server_config(file_path, key, value):
      with open(file_path, 'r') as file:
        lines = file.readlines()
      with open(file_path, 'w') as file:
        for line in lines:
     #Check if the line starts with the specified key
          if key in line:
                # Update the line with the new value
                file.write(key + "=" + value + "\n")
        else:
                # Keep the existing line as it is
                file.write(line)
