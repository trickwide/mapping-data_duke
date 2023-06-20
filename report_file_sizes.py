import os

while True:
    try:
        size = int(input("Enter the size of the file: "))
    except ValueError:
        print("Please enter a number!")
        continue

    path = input("Enter the path of the directory: ")

    if os.path.exists(path):
        break

    print("The path does not exist!")

file_count = 0

for root, dirs, files in os.walk(path):
    for file in files:
        try:
            filepath = os.path.join(root, file)

            file_size = os.path.getsize(filepath)

            if file_size >= size:
                print(f"Size of the file: {file_size}b, filepath: {filepath}")
                file_count += 1

            if file_count >= 20:
                break

        except OSError:
            print("OSError")
            continue

    if file_count >= 20:
        break
