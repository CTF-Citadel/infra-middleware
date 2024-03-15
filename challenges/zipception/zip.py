import os
import zipfile

def zip_file(input_file, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        zipf.write(input_file, arcname=os.path.basename(input_file))

def generate_zip_files(input_text_file, output_zip, num_iterations, flag):
    # Create the goldnugget.txt file
    file_content = flag.encode("utf-8")
    with open(input_text_file, "wb") as file:
        file.write(file_content)

    for i in range(num_iterations):
        current_zip = f'zip{i}.zip'
        zip_file(input_text_file, current_zip)
        input_text_file = current_zip

    # Move the final zip file to the desired name
    os.rename(input_text_file, output_zip)

    # Remove intermediate zip files
    for i in range(num_iterations):
        current_zip = f'zip{i}.zip'
        if os.path.exists(current_zip):
            os.remove(current_zip)

def main():
    env_variable = os.getenv("FLAG")  # Updated to use "flag" as the environment variable

    # Set the flag for the file content
    flag = f"TH{{{env_variable}}}"

    input_text_file = 'goldnugget.txt'
    output_zip = 'goldnugget.zip'
    num_iterations = 9999

    generate_zip_files(input_text_file, output_zip, num_iterations, flag)

if __name__ == "__main__":
    main()