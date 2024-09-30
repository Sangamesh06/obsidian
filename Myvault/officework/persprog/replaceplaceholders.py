import argparse

def replace_placeholders(input_file, sitekeyv1, sitekeyv2, apikeyv1, apikeyv2, secretkeyv1, secretkeyv2, output_file):
    # Read the content of the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Replace the placeholders with the provided values
    content = content.replace('sitekeyv1', sitekeyv1)
    content = content.replace('sitekeyv2', sitekeyv2)
    content = content.replace('apikeyv1', apikeyv1)
    content = content.replace('apikeyv2', apikeyv2)
    content = content.replace('secretkeyv1', secretkeyv1)
    content = content.replace('secretkeyv2', secretkeyv2)

    # Write the modified content to the output file
    with open(output_file, 'w') as file:
        file.write(content)

    print(f"File '{output_file}' has been created with the provided values.")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Replace placeholders in a text file.")
    parser.add_argument('input_file', help="The path to the input file.")
    parser.add_argument('sitekeyv1', help="The site key to replace {sitekeyv1}.")
    parser.add_argument('sitekeyv2', help="The site key to replace {sitekeyv2}.")
    parser.add_argument('apikeyv1', help="The API key to replace {apikeyv1}.")
    parser.add_argument('apikeyv2', help="The API key to replace {apikeyv2}.")
    parser.add_argument('secretkeyv1', help="The secret key to replace {secretkeyv1}.")
    parser.add_argument('secretkeyv2', help="The secret key to replace {secretkeyv2}.")
    parser.add_argument('output_file', help="The name of the output file.")

    # Parse the arguments
    args = parser.parse_args()

    # Call the function with the parsed arguments
    replace_placeholders(
        args.input_file, 
        args.sitekeyv1, 
        args.sitekeyv2, 
        args.apikeyv1, 
        args.apikeyv2, 
        args.secretkeyv1, 
        args.secretkeyv2, 
        args.output_file
    )

# Command to run the program:
# python replaceplaceholders.py input.txt sitekeyv1 sitekeyv2 apikeyv1 apikeyv2 secretkeyv1 secretkeyv2 output.txt

