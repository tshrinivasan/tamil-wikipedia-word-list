#!/bin/bash

# Ask the user for the filename
read -p "Enter the filename: " filename

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "File not found."
    exit 1
fi

# Display a completion message
echo "Processing started. Huge files can take many minutes to complete the task. Please wait. You will be informed once the task is complete."

# Extract the Tamil words from the XML file using xmlstarlet and awk
xmlstarlet sel -t -m "//text()" -v "." "$filename" |
awk '
    BEGIN { RS=" "; ORS="\n" }
    /[ஃ-௿]/ {
        # Remove non-Tamil characters
        gsub(/[^ஃ-௿]/, "")
        # Print non-empty words
        if (length($0) > 0) print
    }
' > words

# Display a completion message
echo "Processing complete. The file 'words' contains the extracted Tamil words."