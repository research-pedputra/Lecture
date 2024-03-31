#!/bin/bash
# How to use
# ./apdos.sh "(Cs)"
# Check if at least one command-line argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <word>"
    exit 1
fi

# Extract the search word from the command-line argument
search_word="$1"

# Search for files containing the specified word in their names within the current directory
found_files=$(find . -maxdepth 1 -type f -name "*$search_word*")

# Check if any files were found
if [ -n "$found_files" ]; then
    echo "Files containing '$search_word' in their names:"
    # Call sumpdos.x on the list of found files
    sumpdos.x $found_files > "${search_word}.dat"
    echo "Output saved as '${search_word}.dat'"
else
    echo "No files containing '$search_word' in their names found."
fi
