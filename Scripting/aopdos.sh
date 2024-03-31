#!/bin/bash
# How to use
# ./aopdos.sh "(Cs)" "(d)"
# Check if at least two command-line arguments are provided
if [ $# -lt 2 ]; then
    echo "Usage: $0 <word1> <word2>"
    exit 1
fi

# Extract the search words from the command-line arguments
search_word1="$1"
search_word2="$2"

# Search for files containing both search words in their names within the current directory
found_files=$(find . -maxdepth 1 -type f -name "*$search_word1*$search_word2*")

# Check if any files were found
if [ -n "$found_files" ]; then
    echo "Files containing '$search_word1' followed by any character(s) followed by '$search_word2' in their names:"
    # Call sumpdos.x on the list of found files
    sumpdos.x $found_files > "${search_word1}_${search_word2}.dat"
    echo "Output saved as '${search_word1}_${search_word2}.dat'"
else
    echo "No files containing '$search_word1' followed by any character(s) followed by '$search_word2' in their names found."
fi
