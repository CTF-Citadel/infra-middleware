import os
import random
import string
import uuid

# Function to generate a string with 10,000 different letters, numbers, and signs with random paragraphs
def generate_large_random_string():
    num_chars_before_paragraph = random.randint(500, 1000)  # Adjust the range as needed
    content = ''

    while len(content) < 10000:
        num_chars_in_paragraph = random.randint(100, 500)  # Adjust the range as needed
        content += ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(num_chars_in_paragraph))
        
        # Add a paragraph after a random amount of characters
        if len(content) < 10000 and random.choice([True, False]):
            content += '\n\n'
    
    return content

# Directory to store the files inside the Docker container
directory = '/usr/local/apache2/htdocs'

# Create 100 files
for i in range(1, 101):
    filename = os.path.join(directory, f'file_{i}.txt')

    # For one file, use the specified format
    if i == 1:
        content = generate_large_random_string()
    else:
        content = generate_large_random_string()

    with open(filename, 'w') as file:
        file.write(content)

# Choose a random file
chosen_file = os.path.join(directory, random.choice([f for f in os.listdir(directory) if f.endswith('.txt')]))

# Generate the content for the chosen file
content = f'TH{{{str(uuid.uuid4())}}}\n' + generate_large_random_string()

# Write the content to a random location in the file
with open(chosen_file, 'r') as file:
    file_content = file.read()

    # Choose a random position to insert the content
    insert_position = random.randint(0, len(file_content))

    # Insert the content at the chosen position
    updated_content = file_content[:insert_position] + content + file_content[insert_position:]

# Write the updated content back to the file
with open(chosen_file, 'w') as file:
    file.write(updated_content)

print(f"Pattern 'TH{{UUID}}' written to {chosen_file} at a random location.")
