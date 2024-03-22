import os


folder_path = input("Enter the path to the folder: ")


if not os.path.isdir(folder_path):
    print("Invalid folder path. Please try again.")
    exit()


video_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]


video_files.sort()


for i, file_name in enumerate(video_files):
    file_extension = os.path.splitext(file_name)[1]
    new_name = str(i + 1) + file_extension
    os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_name))

print("File renaming completed successfully.")
