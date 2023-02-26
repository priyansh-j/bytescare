import re
# Take the file location input from the user
file_path=input("Enter the path:")

# Open the file at the given location in read mode
with open(file_path, 'r') as f:
  # Read the contents of the file
        content = f.read()
        # Use Regular Expression to find URLs in the text
        url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        url_matches = re.findall(url_regex, content)
        # Check if any URLs were found in the text
        if url_matches:
            # Return the number of URL occurrences and the first occurrence
           print(len(url_matches), url_matches[0])
        else:
          #if no url present return 0
            print( 0, None)
