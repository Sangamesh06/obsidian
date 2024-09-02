```
import argparse

def replace_placeholders(input_file, sitekey, apikey, output_file):
    # Read the content of the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Replace the placeholders with the provided values
    content = content.replace('{sitekey}', sitekey)
    content = content.replace('{apikey}', apikey)

    # Write the modified content to the output file
    with open(output_file, 'w') as file:
        file.write(content)

    print(f"File '{output_file}' has been created with the provided values.")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Replace placeholders in a text file.")
    parser.add_argument('input_file', help="The path to the input file.")
    parser.add_argument('sitekey', help="The site key to replace {sitekey}.")
    parser.add_argument('apikey', help="The API key to replace {apikey}.")
    parser.add_argument('output_file', help="The name of the output file.")

    # Parse the arguments
    args = parser.parse_args()

    # Call the function with the parsed arguments
    replace_placeholders(args.input_file, args.sitekey, args.apikey, args.output_file)

```

command to run above program
```
python replace_placeholders.py input.txt your_site_key your_api_key output.txt
```

