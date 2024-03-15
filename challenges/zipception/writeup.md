# zipception Walkthrough

## Introduction

Dive into the layers of compression: Can you find what's inside the zip?


After accessing the IP and port provided by the container, we find ourselves here:

![image](https://github.com/CTF-Citadel/challenges/assets/115781703/afe49104-609e-45b6-878b-76078b330c86)


So, let's go ahead and download 'goldnugget.zip' and save it to a directory, after opening the zip a few times, it seems like it's counting down from 9999, so the files have been zipped 9999 times:

![image](https://github.com/CTF-Citadel/challenges/assets/115781703/40f2bc9d-2749-4a8b-88c8-38cbceb6b95d)


So we gonna use a python script as a solution:

```python
import zipfile
import os

def unzip_recursive(zip_path, output_dir):
    while os.path.exists(zip_path) and zip_path.endswith('.zip'):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
            
            # Get the names of the extracted files
            extracted_files = zip_ref.namelist()
            
            # Assuming there is only one file in the nested zip, update zip_path
            if len(extracted_files) == 1 and os.path.splitext(extracted_files[0])[1] == '.zip':
                zip_path = os.path.join(output_dir, extracted_files[0])
            else:
                break
        print(f"Unzipped: {zip_path}")

# Specify the path to your initial zip file and the output directory
initial_zip_path = "/home/kali/zipception_writeup/goldnugget.zip"
output_directory = "/home/kali/zipception_writeup/"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Call the function to unzip recursively
unzip_recursive(initial_zip_path, output_directory)

print("Unzipping completed.")
```

The script unzips every file in the provided directory repeatedly until there are no zip files left. The script also makes sure every file only gets unzipped once and it doesnt repeatedly unzip the same files. So, in the end, we should get our flag. Let's go ahead and execute it and see what happens:

![image](https://github.com/CTF-Citadel/challenges/assets/115781703/bac6cbfa-0f35-49a1-afbc-b53cf144a49e)

We can see that it unzipped all the files, and we found a 'goldnugget.txt' in our directory. I'm sure you know what's inside ; )











