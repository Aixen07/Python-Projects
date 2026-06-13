import os

def arrange_files(files, ext):
    rename = input("Enter what you want to rename: ")

    files_with_ext = [f for f in files if f.endswith(ext)]

    for i, filename in enumerate(files_with_ext, start=1):
        new_name = f"{rename}{i}{ext}"
        os.rename(filename, new_name)

if __name__ == "__main__":
    files = os.listdir()
    extension = input("Enter the extension : ") #always use a dot(.) before entering an extension
    arrange_files(files, extension)