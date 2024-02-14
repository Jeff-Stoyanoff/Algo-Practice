def spin_words(sentence):
    list_sentence = sentence.split()
    new_list = []
    
    for word in list_sentence:
        if len(word) > 4:
            word_list = [char for char in word]
            word_list.reverse()
            new_word = ''.join(word_list)
            new_list.append(new_word)
        else:
            new_list.append(word)

    new_sentence = ' '.join(new_list)
    return new_sentence

print(spin_words("Welcome Home"))

def find_it(seq):
    value = 0

    for num in range(len(seq)):
        value = seq.count(seq[num])
        if value % 2 != 0:
            return seq[num]
        
    return "No values appear an odd number of times"
        
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))
print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]))
print(find_it([10]))
print(find_it([10, 10, 10]))
print(find_it([1,1,1,1,1,1,10,1,1,1,1]))
print(find_it([5,4,3,2,1,5,4,3,2,10,10]))

def digital_root(n):
    list_n = [int(digit) for digit in str(n)]
    x = 0

    for i in list_n:
        x += i

    x_list = [int(digit) for digit in str(x)]

    if len(str(x)) != 1 or sum(x_list) >= 10:
        y = 0
        y = digital_root(x)

        #for digit in x_list:
            #y += digit
        
        return y
    
    return x

print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        name = names[0]
        result = f"{name} likes this"
        return result
    elif len(names)  == 2:
        name1 = names[0]
        name2 = names[1]
        result = f"{name1} and {name2} like this"
        return result
    elif len(names) == 3:
        name1 = names[0]
        name2 = names[1]
        name3 = names[2]
        result = f"{name1}, {name2} and {name3} like this"
        return result
    elif len(names) > 3:
        length = len(names) - 2
        name1 = names[0]
        name2 = names[1]
        result = f"{name1}, {name2} and {length} others like this"
        return result
    
print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))

def likes(names):
    num_names = len(names)

    if num_names == 0:
        return "no one likes this"
    elif num_names == 1:
        return f"{names[0]} likes this"
    elif num_names == 2:
        return f"{names[0]} and {names[1]} like this"
    elif num_names == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {num_names - 2} others like this"

# Test cases
print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))


def array_diff(a, b):
    return [x for x in a if x not in b]


print(array_diff([1,2], [1]))
print(array_diff([1,2,2], [1]))
print(array_diff([1,2,2], [2]))
print(array_diff([1,2,2], []))
print(array_diff([], [1,2]))
print(array_diff([1,2,3], [1,2]))

import math

def count_bits(n):
    bit_arr = []
    count = 0

    while n >= 1:
        if n % 2 == 1:
            bit_arr.append(1)
        else:
            bit_arr.append(0)

        n = math.floor(n / 2)

    for j in bit_arr:
        if j == 1:
            count += 1

    return count

print(count_bits(0))
print(count_bits(4))
print(count_bits(7))
print(count_bits(9))
print(count_bits(10))

def find_outlier(integers):
    odds = [x for x in integers if x % 2 != 0]
    evens = [x for x in integers if x % 2 == 0]

    if len(odds) == 1:
        return odds[0]
    return evens[0]

print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

def duplicate_count(text):
    lower_text = text.lower()
    dubs = []
    count = 0
    text_arr = [char for char in lower_text]

    for i in range(len(text_arr)):
        for j in range(i+1, len(text_arr)):
            if text_arr[i] == text_arr[j] and text_arr[i] not in dubs:
                dubs.append(text_arr[i])
                count += 1

    return dubs, count

print(duplicate_count(""))
print(duplicate_count("abcde"))
print(duplicate_count("abcdeaa"))
print(duplicate_count("abcdeaB"))
print(duplicate_count("Indivisibilities"))

def duplicate_encode(word):
    lower_word = word.lower()
    frequency_dict = {}
    new_arr = []
    word_arr = [char for char in lower_word]

    for i in word_arr:
        if i in frequency_dict:
            frequency_dict[i] += 1
        else:
            frequency_dict[i] = 1
    
    for char in word_arr:
        if frequency_dict[char] > 1:
            new_arr.append(")")
        else:
            new_arr.append("(")

    new_word = ''.join(new_arr)

    return new_word
    

print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))

from collections import Counter

def duplicate_encode(word):
    lower_word = word.lower()
    frequency_dict = Counter(lower_word)
    new_word = ''.join([')' if frequency_dict[char] > 1 else '(' for char in lower_word])
    return new_word

print(duplicate_encode("din"))  # Output: (((
print(duplicate_encode("recede"))  # Output: ()()()

def is_valid_walk(walk):
    frequency_dict = {}

    for i in walk:
        if i in frequency_dict:
            frequency_dict[i] += 1
        else:
            frequency_dict[i] = 1

    if len(walk) == 10 and frequency_dict.get('n', 0) == frequency_dict.get('s', 0) and frequency_dict.get('w', 0) == frequency_dict.get('e', 0):
        return True
    
    return False

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
print(is_valid_walk(['w']))
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))

def alphabet_position(text):
    text_lower = text.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_list = [char for char in alpha]
    position_dict = {}

    for i, char in enumerate(alpha_list, 1):
        position_dict[char] = i

    text_list = [char for char in text_lower]
    text_arr = []

    for j in text_list:
        if j in position_dict:
            text_arr.append(position_dict[j])

    new_str = " ".join(map(str, text_arr))

    return new_str

print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))

#MORE EFFICIENT VERSION
def alphabet_position(text):
    position_dict = {char: i for i, char in enumerate("abcdefghijklmnopqrstuvwxyz", 1)}

    text_arr = [position_dict[char] for char in text.lower() if char in position_dict]

    return " ".join(map(str, text_arr))

print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))

#MORE EFFICIENT VERSION
def persistence(n):
    count = 0
    total = n
    n_list = [num for num in str(n)]

    while total > 9:
        new_total = 1
        for i in n_list:
            new_total *= int(i)
            
        total = new_total
        count += 1
        n_list = [num for num in str(total)]
        
    return total, count

print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))

def to_camel_case(text):
    text_list = [char for char in text]

    #If I don't want the for loop, this is the list comprehension
    #text_list = [char if char != "_" and char != "-" else " " for char in text]

    for i in range(len(text_list)):
        if text_list[i] == "_" or text_list[i] == "-":
            text_list[i] = " "

    new_text = "".join(text_list)

    words = new_text.split()
    
    for i in range(len(words)):
        for j in range(len(words[i])):
            if i > 0 and j == 0:
                words[i] = words[i][:j] + words[i][j].upper() + words[i][j+1:]
    
    final_text = "".join(words)

    return final_text

print(to_camel_case(""))
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))

def order(sentence):
    word_arr = []
    count = 1
    words = sentence.split()
    word_list = [word for word in words]
    
    while count <= len(word_list):
        for i in range(len(word_list)):
            if str(count) in word_list[i]:
                word_arr.append(word_list[i])
                count += 1 

    sentence_final = " ".join(word_arr)
    return sentence_final

print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order(""))

def narcissistic(value):
    total = 0

    value_arr = [num for num in str(value)]

    for i in value_arr:
        total += int(i) ** len(value_arr)
        print(total)

    if total == value:
        return True
    
    return False

print(narcissistic(7))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))

def tribonacci(signature, n):
    i = len(signature)
    
    while i < n:
        num = sum(signature[-3:])
        signature.append(num)
        i += 1

    return signature

print(tribonacci([1,1,1], 10)) 

def tribonacci(signature, n):
    num = 0
    i = len(signature)
    temp_arr = []

    if n == 0:
        return []
    
    elif n > 0 and n < 4:

        for i in range(min(n, len(signature))):
            temp_arr.append(signature[i])
        return temp_arr 
    
    while i < n:
        for j in range(len(signature[-3:])):
            num = sum(signature[-3:])
        signature.append(num)
        i += 1

    return signature

print(tribonacci([1,1,1], 10))
print(tribonacci([0,0,1], 10))
print(tribonacci([0,1,1], 10))
print(tribonacci([1,0,0], 10))
print(tribonacci([0,0,0], 10))
print(tribonacci([1,2,3], 10))
print(tribonacci([3,2,1], 10))
print(tribonacci([1,1,1], 2))
print(tribonacci([300,200,100], 0))
print(tribonacci([0.5,0.5,0.5], 30))

def unique_in_order(sequence):
    sequence_arr = [char for char in sequence]
    final_arr = []

    if len(sequence_arr) > 0:
        final_arr.append(sequence_arr[0])

    for i in range(1, len(sequence_arr)):
        
        if sequence_arr[i-1] != sequence_arr[i]:
            final_arr.append(sequence_arr[i])
    
    #if all(isinstance(element, str) for element in final_arr) == True:
        #sentence_final = "".join(final_arr)
        #return sentence_final
    
    return final_arr

print(unique_in_order(""))
print(unique_in_order([]))
print(unique_in_order(()))
print(unique_in_order("A"))
print(unique_in_order(["A"]))
print(unique_in_order("A"))
print(unique_in_order("AA"))
print(unique_in_order("AAAABBBCCDAABBB"))
print(unique_in_order("abba"))
print(unique_in_order([1,2,3,3,-1]))
print(unique_in_order("ABBCcA"))

def dig_pow(n, p):
    n_arr = [int(num) for num in str(n)]
    product = 0
    j = p + (len(n_arr) - 1)

    while p <= j:
        for i in n_arr:
            product += i ** p
            p += 1

    if product % n == 0:
        return int(product / n)
    else:
        return -1

print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))
print(dig_pow(41, 5))
print(dig_pow(114, 3))
print(dig_pow(8, 3))

def is_pangram(s):
    s_list = [char.lower() for char in s]
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_list = [char for char in alpha]

    for i in alpha_list:
        if i not in s_list:
            return False
    
    return True

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))
print(is_pangram("Cwm fjord bank glyphs vext quiz"))

def find_even_index(arr):
    index = 0

    while index < len(arr):
        count_LR = 0
        
        for i in range(index):
            count_LR += arr[i]
        count_RL = 0
        for j in range(len(arr) - 1, index, -1):
            count_RL += arr[j]
            
        if count_LR == count_RL:
            return index    
        index += 1
            
    return -1

print(find_even_index([1,2,3,4,3,2,1]))
print(find_even_index([1,100,50,-51,1,1]))
print(find_even_index([1,2,3,4,5,6]))
print(find_even_index([20,10,30,10,10,15,35]))
print(find_even_index([20,10,-80,10,10,15,35]))
print(find_even_index([10,-80,10,10,15,35,20]))
print(find_even_index([1,100]))
print(find_even_index([0,0,0,0,0]))
print(find_even_index([-1,-2,-3,-4,-3,-2,-1]))
print(find_even_index([-100, -1]))

def find_uniq(arr):
    arr.sort()

    if arr[0] != arr[1]:
        return arr[0]
    else:
        return arr[len(arr) - 1]

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
print(find_uniq([ 3, 10, 3, 3, 3 ]))

def find_uniq(arr):
    #Set method to keep count
    for num in set(arr):
        if arr.count(num) == 1:
            return num

print(find_uniq([1, 1, 0, 1, 1, 1]))

def solution(s):
    s_list = [char for char in s]
    new_arr = []

    if len(s_list) % 2 != 0:
        s_list.append("_")

    for i in range(0, len(s_list), 2):
        if i + 1 < len(s_list):
            new_arr.append(s_list[i] + s_list[i + 1])

    return new_arr

print(solution("asdfadsf"))
print(solution("asdfads"))
print(solution(""))
print(solution("x"))

def sort_array(source_array):
    even_arr = []
    odd_arr = []

    for i in source_array:
        if i % 2 == 1:
            odd_arr.append(i)
        if i % 2 == 0:
            even_arr.append(i)

    odd_arr.sort()

    sorted_array = [odd_arr.pop(0) if x % 2 == 1 else x for x in source_array]

    return sorted_array

print(sort_array([5, 3, 2, 8, 1, 4]))
print(sort_array([5, 3, 1, 8, 0]))
print(sort_array([]))
print(sort_array([5, 3, 2, 8, 1, 4, 11]))
print(sort_array([2, 22, 37, 11, 4, 1, 5, 0]))
print(sort_array([1, 111, 11, 11, 2, 1, 5, 0]))
print(sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(sort_array([0, 1, 2, 3, 4, 9, 8, 7, 6, 5]))

def find_missing_letter(chars):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_list = [char for char in alpha]
    alpha_upper_list = [char for char in alpha_upper]

    if chars[0].islower(): 
        for i in range(alpha_list.index(chars[0]), len(alpha_list)):
            if alpha_list[i] not in chars:
                return alpha_list[i]
    else:
        for j in range(alpha_upper_list.index(chars[0]), len(alpha_upper_list)):
            if alpha_upper_list[j] not in chars: 
                return alpha_upper_list[j]
        
print(find_missing_letter(['a','b','c','d','f']))
print(find_missing_letter(['O','Q','R','S']))
print(find_missing_letter(['b', 'd']))

def tower_builder(n_floors):
    tower_arr = []
    i = 1

    while i <= n_floors:
        if i < n_floors:
            tower_arr.append(" " * (n_floors - i) + ("*" * i) + ("*" * (i - 1)) + " " * (n_floors - i))
        else:
            tower_arr.append(("*" * i) + ("*" * (i - 1)))
        i += 1

    return tower_arr

print(tower_builder(1))
print(tower_builder(2))
print(tower_builder(3))

def high(x):
    x_array = [word for word in x.split()]
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_dict = {char: index + 1 for index, char in enumerate(alpha)}
    letter_count = 1
    word_count = 0
    count_array = []

    for i in x_array:
        letter_count = 1
        for letter in i:
            letter_count += alpha_dict.get(letter, 0)
        word_count += letter_count
        count_array.append(word_count)
        word_count = 0

    max_num = max(count_array)
    longest_word = count_array.index(max_num)
    final_word = x_array[longest_word]

    return final_word


print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))
print(high('aa b'))
print(high('b aa'))
print(high('bb d'))
print(high('d bb'))
print(high("aaa b"))

def delete_nth(order, max_e):
    final_arr = []
    
    for i, num in enumerate(order):
        count_at_index = order[:i+1].count(order[i])
        if count_at_index <= max_e:
            final_arr.append(num)

    return final_arr

print(delete_nth([20,37,20,21], 1))
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
print(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3))
print(delete_nth([1, 1, 1, 1, 1], 5))
print(delete_nth([], 5))

def count_smileys(arr):
    #valid_faces = [':)', ':D',';-D',':~)']
    smiley_count = 0

    for value in arr:
            if len(value) == 3:
                if (value[0] == ':' or value[0] == ';') and (value[1] == '-' or value[1] == '~') and (value[2] == ')' or value[2] == 'D'):
                        smiley_count += 1
            elif len(value) == 2:
                if (value[0] == ':' or value[0] == ';') and (value[1] == ')' or value[1] == 'D'):
                        smiley_count += 1

    return smiley_count

print (count_smileys([]))
print (count_smileys([':D',':~)',';~D',':)']))
print (count_smileys([':)',':(',':D',':O',':;']))
print (count_smileys([';]', ':[', ';*', ':$', ';-D']))

def count_smileys(arr):
    smiley_count = 0

    for value in arr:
        if len(value) == 3:
            # Check the first and third characters
            if (value[0] == ':' or value[0] == ';') and (value[2] == ')' or value[2] == 'D'):
                smiley_count += 1
        elif len(value) == 2:
            # Check the first and second characters
            if (value[0] == ':' or value[0] == ';') and (value[1] == ')' or value[1] == 'D'):
                smiley_count += 1

    return smiley_count

print(count_smileys([]))
print(count_smileys([':D', ':~)', ';~D', ':)']))

def valid_braces(string):
    stack = []
    bracket_mapping = {'(': ')', '[': ']', '{': '}'}

    for i in string:
        if i in "([{":
            stack.append(i)

        elif i in ")]}":
            if not stack:
                return False

            if bracket_mapping[stack.pop()] != i:
                return False
                        
    return True

print(valid_braces("()"))
print(valid_braces("(}"))
print(valid_braces("[]"))
print(valid_braces("[(])"))
print(valid_braces("{}"))
print(valid_braces("{}()[]"))
print(valid_braces("([{}])"))
print(valid_braces("([}{])"))
print(valid_braces("{}({})[]"))
print(valid_braces("(({{[[]]}}))"))
print(valid_braces("(((({{"))
print(valid_braces(")(}{]["))
print(valid_braces("())({}}{()][]["))

def valid_braces(string):
    stack = []
    bracket_mapping = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in '({[':
            # Push opening brace onto the stack
            stack.append(char)
        elif char in ')}]':
            # Check if the stack is not empty
            if not stack:
                return False

            # Check if the top element's corresponding closing brace matches the current closing brace
            if bracket_mapping[stack.pop()] != char:
                return False

    # The string is valid if the stack is empty at the end
    return not stack

# Test cases
print(valid_braces("()"))            # Output: True
print(valid_braces("(}"))            # Output: False
print(valid_braces("[]"))            # Output: True
print(valid_braces("[(])"))          # Output: False
print(valid_braces("{}"))            # Output: True
print(valid_braces("{}()[]"))        # Output: True
print(valid_braces("([{}])"))        # Output: True
print(valid_braces("([}{])"))        # Output: False
print(valid_braces("{}({})[]"))      # Output: True
print(valid_braces("(({{[[]]}}))"))  # Output: True
print(valid_braces("(((({{"))        # Output: False
print(valid_braces(")(}{]["))        # Output: False
print(valid_braces("())({}}{()][]["))


import math
from sympy import isprime

def is_prime(num):
    abs_num = abs(num)
    square_root = math.sqrt(abs_num)
    root_num = math.ceil(square_root)
    i = 2
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]

    if num < 2:
        return False
    
    if num == 2:
        return True
    
    if num > 3000:
        return isprime(num)

    for i in primes:
        if i <= root_num:
            if abs_num % i == 0:
                return False
        else:
            return True
        
print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(73))
print(is_prime(75))
print(is_prime(-1))
print(is_prime(1000003))
        
def solution(s):
    new_s = ""

    for char in s:
        if char.islower():
            new_s += char

        elif char.isupper():
            new_s += " "
            new_s += char

    return new_s

print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))

def largest_consec(strarr, k):
    new_arr = []
    
    long_str = ""

    if k <= 0:
        return ""

    for i in range(len(strarr) - k + 1):
        str_combo = ""
        for j in range(i, i + k):
            str_combo += strarr[j]
        new_arr.append(str_combo)
            
    for i in new_arr:
        if len(i) > len(long_str):
            long_str = i

    return long_str

print(largest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(largest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
print(largest_consec([], 3))
print(largest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2))
print(largest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2))
print(largest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2))
print(largest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))
print(largest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15))
print(largest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0))

sample = ["Hello", "World"]

sample_str = "".join(sample)
print(sample_str)

def expanded_form(num):
    arr = []
    num_list = [int(digit) for digit in str(num)]
    my_dict = {10 ** i: value for i, value in enumerate(range(len(num_list) - 1, -1, -1))}
    my_dict = {key: num_list[value] for key, value in sorted(my_dict.items(), reverse=True)}
    result_dict = {key: key * value for key, value in my_dict.items()}

    for value in result_dict.values():
        if value > 0:
            arr.append(str(value))

    final_str = " + ".join(arr)


    return final_str

print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))

def expanded_form(num):
    # Convert the number to a list of integers
    num_list = [int(digit) for digit in str(num)]

    # Get the powers of 10 in reverse order
    powers_of_10 = [10 ** i for i in range(len(num_list) - 1, -1, -1)]

    # Create a dictionary with powers of 10 as keys and digits as values
    my_dict = dict(zip(powers_of_10, num_list))

    # Filter out entries with value 0
    my_dict = {key: value for key, value in my_dict.items() if value != 0}

    # Create a list of strings for each term in the expanded form
    terms = [str(value * key) for key, value in my_dict.items()]

    # Join the terms with ' + ' to create the final string
    final_str = " + ".join(terms)

    return final_str

# Test cases
print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))


def comp(array1, array2):
    sq_array = [num ** 2 for num in array1]

    if array1 is None or array2 is None:
        return False

    if array1 == [] and array2 == []:
        return True

    for i in sq_array:
        if i not in array2:
            return False

    for j in array2:
        if j not in sq_array:
            return False
        
    if len(sq_array) != len(array2):
        return False

    return True

print(comp([2,2,3,4,5,6,7,7], [4,9,16,25,36,49]))

print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]))


import math

def comp(array1, array2):
    # Check for None, empty list, or empty dictionary
    if array1 is None or array2 is None:
        return False
    
    if array1 == [] and array2 == []:
        return True
    
    # Square each element in array1
    squared_array1 = [num ** 2 for num in array1]
    
    # Sort the squared_array1 and array2
    squared_array1.sort()
    array2.sort()
    
    # Check if the sorted arrays are equal
    return squared_array1 == array2

print(comp([2,2,3,4,5,6,7,7], [4,9,16,25,36,49]))

print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]))

def bouncing_ball(h, bounce, window):
    count = 0
    current_height = h

    if h <= 0 or window <= 0 or bounce <= 0 or bounce > 1:
        return -1
    
    if current_height < window:
        return -1
    
    while current_height > window:
        if current_height > window:
            count += 1
        
        current_height *= bounce

        if current_height > window:
            count += 1

    return count

print(bouncing_ball(200000000, 0.5, 1.5))
print(bouncing_ball(3, 0.66, 1.5))
print(bouncing_ball(30, 0.66, 1.5))
print(bouncing_ball(30, 0.75, 1.5))



def bouncing_ball(h, bounce, window):
    if h <= 0 or window <= 0 or bounce <= 0 or bounce >= 1:
        return -1
    
    count = 0
    current_height = h

    while current_height > window:
        count += 1  # Increment for each bounce, including the first one
        current_height *= bounce

    return count * 2 - 1  # Adjust count to account for the initial drop

print(bouncing_ball(20000000, 0.5, 1))
print(bouncing_ball(3, 0.66, 1.5))
print(bouncing_ball(30, 0.66, 1.5))
print(bouncing_ball(30, 0.75, 1.5))

def in_array(array1, array2):
    final_array = []

    for word in array1:
        for string in array2:
            if word in string and word not in final_array:
                final_array.append(word)

    sorted_array = sorted(final_array)

    return sorted_array

print(in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
print(in_array(["arp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))

def queue_time(customers, n):
    first_five = customers[0:n]
    remaining = customers[n:]

    if customers == []:
        return 0

    for customer_time in remaining:
        open_till = min(first_five)
        open_spot = first_five.index(open_till)
        first_five[open_spot] = open_till + customer_time

    return max(first_five)
    

print(queue_time([11, 29, 12, 3, 5, 42, 9, 39, 20, 15, 9], 5))
print(queue_time([1,2,3,4,5], 1))
print(queue_time([2], 5))
print(queue_time([], 1))

def count(s):
    char_lib = {}

    for i in range(len(s)):
        char = s[i]
        char_lib[char] = s.count(char)

    return char_lib

print(count("aba"))
print(count(""))
print(count("aa"))
print(count("aabb"))