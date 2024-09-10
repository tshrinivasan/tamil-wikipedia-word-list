#!/bin/bash

# Ask the user for the filename
read -p "Enter the filename: " filename

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "File not found."
    exit 1
fi

# Process the file
< "$filename" sed 's/[a-zA-Z]//g' |
tr "\012\015\041\042\043\044\045\046\047\050\051\053\054\055\056\057\060\061\062\063\064\065\066\067\070\071\073\074\075\076\077\100\101\102\103\104\105\106\107\110\111\112\113\114\115\116\117\120\121\122\123\124\125\126\127\130\131\132\133\135\140\173\174\175" '\n' |
sed -e 's/^[ \t]*//' | grep -v ^$ |
xargs -n 1 > words
