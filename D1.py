# %% [markdown]
# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.
# 
# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.
# 
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
# 
# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").
# 
# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.
# 
# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
# 
# For example:
# 
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
# 
# Consider your entire calibration document. What is the sum of all of the calibration values?

# %%
import pandas as pd
n = pd.DataFrame()
import re

# %%
input = r'C:\Python\Advent of code\2023\1\input.txt'

# %%
file = open(input,'r')
lines = file.readlines()

# %%
for line in lines:
    #print(line)
    num = ""
    for c in line:
        if c.isdigit():
            num = num+c
    num = num[0]+ num[-1]
    #print(f'len: {len(num)}')
    #print(num)
    if len(num) == 2:
        n= pd.concat([n, pd.DataFrame([num])],ignore_index=True)
    #print(num)

# %%
n.info()
n[0] = n[0].astype(int)

# %%
n[0].sum()

# %% [markdown]
# Part 1 compleate

# %% [markdown]
# --- Part Two ---
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
# 
# Equipped with this new information, you now need to find the real first and last digit on each line. For example:
# 
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
# 
# What is the sum of all of the calibration values?

# %%
words_to_numbers = {
 'one': '1', 
 'two': '2', 
 'three': '3', 
 'four': '4', 
 'five': '5',
 'six': '6', 
 'seven': '7', 
 'eight': '8', 
 'nine': '9', 
 'ten': '10',
 'eleven': '11', 
 'twelve': '12', 
 'thirteen': '13', 
 'fourteen': '14', 
 'fifteen': '15',
 'sixteen': '16', 
 'seventeen': '17', 
 'eighteen': '18', 
 'nineteen': '19', 
 'twenty': '20',
 'twentyone': '21', 
 'twentytwo': '22', 
 'twentythree': '23', 
 'twentyfour': '24', 
 'twentyfive': '25',
 'twentysix': '26', 
 'twentyseven': '27', 
 'twentyeight': '28', 
 'twentynine': '29', 
 'thirty': '30',
 'thirtyone': '31', 
 'thirtytwo': '32', 
 'thirtythree': '33', 
 'thirtyfour': '34', 
 'thirtyfive': '35',
 'thirtysix': '36', 
 'thirtyseven': '37', 
 'thirtyeight': '38', 
 'thirtynine': '39', 
 'forty': '40',
 'fortyone': '41', 
 'fortytwo': '42', 
 'fortythree': '43', 
 'fortyfour': '44', 
 'fortyfive': '45',
 'fortysix': '46', 
 'fortyseven': '47', 
 'fortyeight': '48', 
 'fortynine': '49', 
 'fifty': '50',
 'fiftyone': '51', 
 'fiftytwo': '52', 
 'fiftythree': '53', 
 'fiftyfour': '54', 
 'fiftyfive': '55',
 'fiftysix': '56', 
 'fiftyseven': '57', 
 'fiftyeight': '58', 
 'fiftynine': '59', 
 'sixty': '60',
 'sixtyone': '61', 
 'sixtytwo': '62', 
 'sixtythree': '63', 
 'sixtyfour': '64', 
 'sixtyfive': '65',
 'sixtysix': '66', 
 'sixtyseven': '67', 
 'sixtyeight': '68', 
 'sixtynine': '69', 
 'seventy': '70',
 'seventyone': '71', 
 'seventytwo': '72', 
 'seventythree': '73', 
 'seventyfour': '74', 
 'seventyfive': '75',
 'seventysix': '76', 
 'seventyseven': '77', 
 'seventyeight': '78', 
 'seventynine': '79', 
 'eighty': '80',
 'eightyone': '81', 
 'eightytwo': '82', 
 'eightythree': '83', 
 'eightyfour': '84', 
 'eightyfive': '85',
 'eightysix': '86', 
 'eightyseven': '87', 
 'eightyeight': '88', 
 'eightynine': '89', 
 'ninety': '90',
 'ninetyone': '91', 
 'ninetytwo': '92', 
 'ninetythree': '93', 
 'ninetyfour': '94', 
 'ninetyfive': '95',
 'ninetysix': '96', 
 'ninetyseven': '97', 
 'ninetyeight': '98', 
 'ninetynine': '99', 
 'onehundred': '100'
}

# %%
def convert_to_numbers(s):
    pattern = re.compile(r'\b(' + '|'.join(words_to_numbers.keys()) + r')\b')
    return re.sub(pattern, lambda x: words_to_numbers[x.group()], s)

# %%
def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

# %%
n2 = pd.DataFrame(columns=['num','tweaked','line'])

# %%
n2.head()

# %%
for line in lines:
    line_len = len(line)
    #print('#############################')
    #print(f'Orignial: {line}')
    og_line = line
    for word,num in words_to_numbers.items():
        #print(f'word: {word}')
        word_len = len(word)
        for n in line:
            if line.find(word) != -1:
                x = line.find(word)
                #print(x)
                xx = len(word)
                numn = sum((x,xx))-1
                #line = replacer(line,num,numn)
                line = line[:numn] + num + line[numn:]
                linx = num
                #print(f'changed:{line}')
            
        #print(word)
    #print(f'tweaked: {line}')
    #print(f'linex: {linx}')
    #print(convert_to_numbers(line))
    num = ""
    for c in line:
        if c.isdigit():
            num = num+c
    num = num[0]+ num[-1]
    #print(f'len: {len(num)}')
    #print(num)
   # if len(num) == 2:
   
    n2= pd.concat([n2, pd.DataFrame([[num,line, og_line,]],columns=['num','tweaked','line'])],ignore_index=True)
    #print(num)

# %%
n2.info()
n2['num'] = n2['num'].astype(int)

# %%
n2['num'].sum()

# %% [markdown]
# 54540
# 55166
# 55230
# 55218


