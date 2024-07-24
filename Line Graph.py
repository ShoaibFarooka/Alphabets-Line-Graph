# Initialize an empty list to store the numeric positions
number_input = []

# Function to convert an alphabet to its numeric position
def alphabet_to_number(char):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if 'a' <= char <= 'z':
        return lowercase_letters.index(char) + 1
    elif 'A' <= char <= 'Z':
        return uppercase_letters.index(char) + 1
    else:
        return None

# Input from the user
user_input = input("Enter a string of alphabets: ")

# Convert the input string to a list of numbers
for char in user_input:
    position = alphabet_to_number(char)
    if position is not None:
        number_input.append(position)

# Print the numeric positions
print("Numeric positions of the alphabets:", number_input)

# default pattern
pattern_row = 50
pattern_column=50
pattern = [[0 for _ in range(pattern_row)] for _ in range(pattern_column)]
height = 10 # starting row (adaptable)
rows = 30 # rows of the pattern
lines = 10 # lines added to the pattern
def figure(height, lines, nums):
    last_value = None
    initial_height = rows-height-1
    max_height = initial_height
    peak_row = initial_height
    peak_column = lines
    for i in range(len(nums)):
        # if i is even it adds '/'
        if nums[i] % 2 == 0 and last_value == 'even':
            #Even Even Case
            pattern[rows-height-2][lines-1]='|'
            pattern[rows-height-3][lines-1]='|'
            height += 3
            lines -= 1
            for j in range(nums[i]):
                pattern[rows-height-1][lines] = '/'
                height += 1 # increase height by 1
                lines += 1 # count the lines added to the pattern
                current_height = rows-height-1
                if current_height < max_height:
                  max_height = current_height
                  peak_row = current_height
                  peak_column = lines
            height -= 1
        elif nums[i] % 2 == 0:
            last_value='even'
            for j in range(nums[i]):
                pattern[rows-height-1][lines] = '/'
                height += 1 # increase height by 1
                lines += 1 # count the lines added to the pattern
                current_height = rows-height-1
                if current_height < max_height:
                  max_height = current_height
                  peak_row = current_height
                  peak_column = lines
            height -= 1
        # if i is odd it adds '\'
        elif nums[i] % 2 == 1 and last_value == 'odd':
            #Odd Odd Case
            pattern[rows-height][lines-1]='|'
            pattern[rows-height+1][lines-1]='|'
            height -= 3
            lines -= 1
            for j in range(nums[i]):
                pattern[rows-height-1][lines] = '\\'
                height -= 1 # decrease height by 1
                lines += 1
                current_height = rows-height-1
                if current_height < max_height:
                  max_height = current_height
                  peak_row = current_height
                  peak_column = lines
            height += 1
        elif nums[i] % 2 == 1:
            last_value='odd'
            for j in range(nums[i]):
                pattern[rows-height-1][lines] = '\\'
                height -= 1 # decrease height by 1
                lines += 1
                current_height = rows-height-1
                if current_height < max_height:
                  max_height = current_height
                  peak_row = current_height
                  peak_column = lines
            height += 1
    print('Initial Height: ', initial_height)
    print('Peak Row:', peak_row)
    print('Peak Column:', peak_column)
    #Man at Peak
    pattern[peak_row][peak_column+1]='>'
    pattern[peak_row][peak_column-1]='<'
    pattern[peak_row-1][peak_column]='|'
    pattern[peak_row-1][peak_column-1]='\\'
    pattern[peak_row-1][peak_column+1]='/'
    pattern[peak_row-2][peak_column]='o'
    
figure(height, lines, number_input)

# replace zeros with spaces
for line in pattern:
    for i, num in enumerate(line):
        if num == 0:
            line[i] = ' '
    # print the lines
    print(*line)
