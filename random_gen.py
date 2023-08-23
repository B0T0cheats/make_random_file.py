

#888888b.    .d88888b. 88888888888 .d88888b.
#888  "88b  d88P" "Y88b    888    d88P" "Y88b
#888  .88P  888     888    888    888     888
#8888888K.  888     888    888    888     888
#888  "Y88b 888     888    888    888     888
#888    888 888     888    888    888     888
#888   d88P Y88b. .d88P    888    Y88b. .d88P
#8888888P"   "Y88888P"     888     "Y88888P"
#
#
#
#discord: mmloli
#_________________________________________________

import os
import random
import string

def generate_random_content(length):
    characters = string.ascii_letters + string.digits + string.punctuation + " "
    return ''.join(random.choice(characters) for _ in range(length))

def create_random_file(filename, size_in_bytes):
    content = generate_random_content(size_in_bytes)
    with open(filename, 'w') as f:
        f.write(content)

def main():
    folder_path = r"E:\hell0d"  # Change this to the desired folder path on your E drive
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_count = 10000  # Change this to the number of files you want to generate
    min_size = 10240000  # Minimum size in bytes
    max_size = 102400000  # Maximum size in bytes

    for i in range(1, file_count + 1):
        file_size = random.randint(min_size, max_size)
        filename = os.path.join(folder_path, f"{file_size}bytes_{i}.txt")
        create_random_file(filename, file_size)
        print(f"Random file '{filename}' created with {file_size} bytes.")

if __name__ == "__main__":
    main()
