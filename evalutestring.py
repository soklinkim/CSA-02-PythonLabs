
# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes a hyphen will separate the two letters in the string.
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# user_range = input("Enter a range of letters (e.g., a-z): ")
# print(result_string)

# My answer
# Get user input for the range
user_input = input("Enter a range of letters (e.g. 'a-z'): ")
# Remove quotes from the user input
user_input = user_input.strip('"')
# Split the range into start and end characters
startChr, endChr = user_input.split('-')
# Convert start and end characters to ASCII codes using 'ord'
start_ascii = ord(startChr)
end_ascii = ord(endChr)
# Generate the string of characters in the range using 'chr' and list 
character_range = char_range = list(map(chr, range(start_ascii, end_ascii + 1)))
# join character
result_string = ''.join(character_range)
# Dispaly result
print(result_string)
