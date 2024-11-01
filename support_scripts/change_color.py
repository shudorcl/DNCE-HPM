import os
import random

def generate_random_color():
    return [random.randint(0, 255) for _ in range(3)]

def replace_color_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    if not lines:
        print(f"File {file_path} is empty.")
        return
    
    first_line = lines[0].strip()
    if first_line.startswith("color = {"):
        # Extract the current color values
        start = first_line.find("{") + 1
        end = first_line.find("}")
        current_color = first_line[start:end].split()
        
        # Generate a new random color
        new_color = generate_random_color()
        
        # Replace the old color with the new color
        new_first_line = f"color = {{{new_color[0]} {new_color[1]} {new_color[2]}}}\n"
        
        # Write the modified content back to the file
        lines[0] = new_first_line
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print(f"Updated color in {file_path} from {current_color} to {new_color}")
    else:
        print(f"First line of {file_path} does not match the expected format.")

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            replace_color_in_file(file_path)

# Example usage
folder_path = '../temp/countries'
process_folder(folder_path)