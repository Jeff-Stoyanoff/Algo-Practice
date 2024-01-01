def speed_limit(speed, signals):
    fines = 0
    for i in range(len(signals)):
        if speed - signals[i] > 29:
            fines += 500
        elif speed - signals[i] > 19 and  speed - signals[i] < 30:
            fines += 250
        elif speed - signals[i] > 9 and speed - signals[i] < 20:
            fines += 100
        else:
            fines += 0
    return fines

print(speed_limit(60, [80, 70, 60]))
print(speed_limit(90, [80]))
print(speed_limit(100, [110, 100, 80]))
print(speed_limit(130, [140, 130, 100]))
print(speed_limit(110, [120, 110, 100]))

def mispelled(word1, word2):
    err_count = 0
    spell_error = False
    for i in word2:
        if i not in word1:
            err_count += 1
            if err_count > 1:
                spell_error = True
                break
    return not spell_error


print(mispelled('versed', 'xersed')) # returns True
print(mispelled('versed', 'applb')) # returns False
print(mispelled('versed', 'v5rsed')) # returns True
print(mispelled('1versed', 'versed')) # returns True
print(mispelled('versed', 'versed')) #returns True 

def sphere(rad, mass):
    vol = round(((3.14 * 4) / 3) * (rad**3), 5)
    area = round((4*3.14159*(rad**2)), 5)
    density = round((mass / vol), 5)
    return rad, mass, vol, area, density
print(sphere(2, 50)) 

def div_con(arr):
    x = 0
    y = 0
    for i in arr:
        if type(i) == int:
            x = x + i
        elif type(i) == str:
            y = y + int(i)
    return x - y

print(div_con([9, 3, "7", "3"]))
print(div_con(['5','0',9,3,2,1,'9',6,7]))
print(div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']))
print(div_con(['1', '5', '8', 8, 9, 9, 2, '3']))
print(div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]))

def real_numbers(n):
    count = 0
    i = 1
    while i <= n:
        if i % 5 != 0 and i % 3 != 0 and i % 2 != 0:
            count += 1
        i += 1
    return count

print(real_numbers(5))
print(real_numbers(10))
print(real_numbers(20))
print(real_numbers(30))
print(real_numbers(40))
print(real_numbers(55))

def nonCons():
    arr1 = [1,2,3,4,6,7,8,15,16]
    arr2 = []
    arr3 = []
    arr2.append(arr1[0])
    for i in range(1, len(arr1)):
        if arr1[i] - arr1[i-1] > 1:
            arr3.append(arr1[i])
        else:
            arr2.append(arr1[i])
    return arr3

print(nonCons())

def nonCons():
    arr1 = [1,2,3,4,6,7,8,15,16]
    arr2 = []
    arr3 = []
    for i in range(1, len(arr1)):
        if arr1[i] - arr1[i-1] > 1:
            arr3.append(arr1[i])
            arr2.append(arr1[i-1])
    kvs = []
    for i in range(len(arr2)):
        kvs.append({"i": arr2[i], "n": arr3[i]})
    return kvs

print(nonCons())


def nonCons():  #This one loses arr2 which is unnecessary
    arr1 = [1,2,3,4,6,7,8,15,16]
    arr3 = []
    for i in range(1, len(arr1)):
        if arr1[i] - arr1[i-1] > 1:
            arr3.append(arr1[i])
    return arr3

print(nonCons())

def nonCons():  #This one I don't fully understand yet, but it sets a boolean variable which changes
    arr1 = [1, 2, 3, 4, 6, 7, 8, 15, 16]
    arr2 = []
    arr3 = []
    prev_i = None  # initialize previous i to None
    for i in arr1:
        if prev_i is None:
            arr2.append(i)
        elif i - prev_i > 1:
            arr3.append(i)
        else:
            arr2.append(i)
        prev_i = i  # update previous i to current i
    print(arr2)
    return arr3

print(nonCons())

def onlyEvens(arr):
    i = 0
    total = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            total = total + arr[i]

    return total

print(onlyEvens([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))

def between_extremes(arr):
    high = -200
    low = 200
    for i in range(len(arr)):
        if arr[i] > high:
            high = arr[i]
        elif arr[i] < low:
            low = arr[i]
    return high - low
    
print(between_extremes([1, 1]))
print(between_extremes([-1, -1]))
print(between_extremes([1, -1]))
print(between_extremes([21, 34, 54, 43, 26, 12]))
print(between_extremes([-1, -41, -77, -100]))

def is_it_a_num(str):
    list2 = []
    validPhone = ""
    for char in str:
        if char.isdigit():
            list2.append(char)
    if len(list2) == 11 and list2[0] == '0':
        for i in list2:
            validPhone += i
        return validPhone
    else:
        return "Not a phone number"

    #return ''.join(list2)  #This returns a string instead of a list
print(is_it_a_num("S:)0207ERGQREG88349F82!efRF)"))
print(is_it_a_num("sjfniebienvr12312312312ehfWh"))
print(is_it_a_num("0192387415456"))
print(is_it_a_num("v   uf  f 0tt2eg qe0b 8rtyq4eyq564()(((((165"))
print(is_it_a_num("stop calling me no I have never been in an accident"))

my_string = "abc123"
for char in my_string:
    if char.isdigit():
        print(char, "is a digit")

def findMiddle(arr):
    i = 0
    arr2 = []
    high = 0
    sechigh = 0
    if len(arr) == 1:
        return "Array must have two values"
    for i in range(len(arr)):
        if arr[i] > high:
            high = arr[i]
    arr2.append(high)
    for i in range(len(arr)):
        if arr[i] > sechigh and arr[i] != high:
            sechigh = arr[i]
        elif arr.count(high) > 1:
            return high
    return sechigh
        
print(findMiddle([3,11,7,9,2,8]))

def second_symbol(str, letter, instance):
    count = 0
    for i in range(len(str)):
        if str[i] == letter:
            count += 1
        if str[i] == letter and count == instance:
            return i
    if str.count(letter) == 0:
        return "-1"
        
print(second_symbol('Hello world!!!','l', 2))
print(second_symbol('Hello world!!!', 'o', 2))
print(second_symbol('Hello world!!!', 'A', 1))
print(second_symbol('', 'q', 1))
print(second_symbol('Hello', '!', 1))
    
def find_caterer(budget, people):
    if budget < 15 or people == 0:
        return -1
    arr = []
    basic = budget - (people * 15)
    economy = budget - (people * 20)

    if people > 60:
        premium = (budget - ((people * 30) * .8))
    else:
        premium = budget - (people * 30)

    if basic < 0 and economy < 0 and premium < 0:
        return -1

    if basic >= 0:
        arr.append(basic)
    if economy >= 0:
        arr.append(economy)
    if premium >= 0:
        arr.append(premium)
    
    for i in arr:
        choice = min(arr)
    return arr.index(choice) + 1

print(find_caterer(150, 10))
print(find_caterer(1500, 60))
print(find_caterer(1500, 61))
print(find_caterer(100, 0))
print(find_caterer(200, 5))
print(find_caterer(1000, 45))
print(find_caterer(940, 70))

def max_sum_between_two_negatives(my_list):
    new_list = []
    x = min(my_list)
    neg_count = 0
    
    for i in my_list:
        if i < 0:
            neg_count += 1
            new_list.append(i)
    if neg_count < 2:
        return "The list must contain two negative numbers"

    y = max(new_list)
    z = abs(x - y)

    return z

print(max_sum_between_two_negatives([1,-2,3,4,5,6,7,-8,9]))

#How to do it without creating second list
def max_sum_between_two_negatives(my_list):
    count = 0
    neg_nums = [x for x in my_list if x < 0]
    count = len(neg_nums)
    if len(neg_nums) < 2:
        return -1
    return max(neg_nums) - min(neg_nums), count

print(max_sum_between_two_negatives([1,-2,3,-4,5,-6,7,-8,9])) # output: 15

def max_sum_between_two_negatives(my_list):
    new_list = []
    current_sum = 0
    neg_index = -1
    for i in range(len(my_list)):
        if my_list[i] < 0:
            if neg_index >= 0:
                new_list.append(current_sum)
            current_sum = 0
            neg_index = i
        else:
            current_sum += my_list[i]
    if neg_index >= 0:
        new_list.append(current_sum)

    if len(new_list) == 0 or max(new_list) == 0:
        return "No sum can be returned from this list"
    print(my_list)      
    return max(new_list)

print(max_sum_between_two_negatives([-1,6,-2,3,5,-7]))
print(max_sum_between_two_negatives([5,-1,-2]))

def get_count(string):
    count = 0
    vowel = "aeiou"

    for i in range(len(string)):
        if string[i] in vowel:
            count += 1
    return count

print(get_count("Should count all vowels"))
print(get_count("aeiou"))

def disemvowel(string):
    vowel = "aeiouAEIOU"
    new_str = ""
    for i in range(len(string)):
        if string[i] not in vowel:
            new_str += string[i]
    return new_str

print(disemvowel("This website is for losers LOL"))
print(disemvowel("No offense but, Your writing is among the worst I've ever read")) 
print(disemvowel("What are you, a communist?")) 

def disemvowel(string):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        string = string.replace(vowel, "")
    return string

print(disemvowel("This website is for losers LOL"))
print(disemvowel("No offense but, Your writing is among the worst I've ever read")) 
print(disemvowel("What are you, a communist?")) 

def square_digits(num):
    my_list = [int(x) for x in str(num)]
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
        my_list[i] = my_list[i] * my_list[i]
        my_list[i] = str(my_list[i])

    new_int = int("".join(my_list))

    return new_int

print(square_digits(9119))
print(square_digits(0))

def solution(number):
    total = 0
    i = 1
    if number < 0:
        return 0
    while i < number:
        if i % 3 == 0 or i % 5 == 0:
            total = total + i
        if i % 5 == 0 and number < 6:
            return 3
        if number < 4:
            return 0
        i += 1

    return total

print(solution(15))

def high_and_low(fuck_mcfuck):
    fuck_me = [int(x) for x in fuck_mcfuck.split(' ')]
    print(fuck_me)
    maxx = max(fuck_me)
    minn = min(fuck_me)
    print(f"{maxx} {minn}")
high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
high_and_low("1 2 3")

def descending_order(num):
    high = 0
    str_list2 = []
    str_list = [int(x) for x in str(num)]
    orig_length = len(str_list)
    while len(str_list2) < orig_length:
        for i in range(len(str_list)):
            if str_list[i] > high:
                high = str_list[i]
        str_list2.append(high)
        str_list.remove(high)
        high = 0
    str_list2 = [str(x) for x in str_list2]
    final = int("".join(str_list2))
    return final

print(descending_order(0))
print(descending_order(15))
print(descending_order(123456789))

def descending_order(num):
    str_list = sorted(str(num), reverse=True)
    return int(''.join(str_list))

print(descending_order(3867291))
print(descending_order(357528416))

def get_middle(str):
    #my_str = [char for char in str]
    #my_str = list(str)
    my_str = [x for x in str]

    if len(my_str) % 2 == 0:
        x = int(len(my_str) / 2) - 1
        zed = my_str[x], my_str[x+1]
        dead = ''.join(zed)
        return dead

    if len(my_str) % 2 != 0:
        y = int((len(my_str) - 1) / 2)
        return my_str[y]

print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
print(get_middle("of"))

def accum(str_exm):
    str_list = [char for char in str_exm]
    j = 1
    new_list = []

    for i in range(len(str_list)):
        if str_list[i].islower():
            new_list.append(str_list[i].upper() + str_list[i].lower() * (j - 1))
        else:
            new_list.append(str_list[i]  * j)
        j += 1
    str_final = '-'.join(new_list)

    return '"' + str_final + '"'

print(accum("hello"))
print(accum("ZpglnRxqenU"))
print(accum("NyffsGeyylB"))
print(accum("MjtkuBovqrU"))
print(accum("EvidjUnokmM"))
print(accum("HbideVbxncC"))

def accum(str_exm):
    str_list = [char for char in str_exm]
    j = 1
    new_list = []

    for i in range(len(str_list)):
        new_list.append(str_list[i].upper() + str_list[i].lower() * (j - 1))
        j += 1
    
    str_final = '-'.join(new_list)

    return "'" + str_final + "'"

print(accum("hello"))
print(accum("ZpglnRxqenU"))
print(accum("NyffsGeyylB"))
print(accum("MjtkuBovqrU"))
print(accum("EvidjUnokmM"))
print(accum("HbideVbxncC"))

import math

def is_square(num):
    if num < 0:
        message = str(num) + ": Negative numbers cannot be square numbers"
        return False, message
    
    x = math.sqrt(num)
    if x % 1 == 0:
        return True
    else:
        return False
    
print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
print(is_square(25))
print(is_square(26))


def filter_list(list):
    new_list = []
    for i in range(len(list)):
        if not isinstance(list[i], str):
            new_list.append(list[i])
    return new_list

print(filter_list([1,2,'a','b']))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,2,'aasf','1','123',123]))


def isogram(this_str):
    my_str = [char.lower() for char in this_str]
    
    for i in range(len(my_str)):
        for j in range(i + 1, len(my_str)):
            if my_str[i] == my_str[j]:
                return False
            
    return True

print(isogram("Dermatoglyphics"))
print(isogram("isogram"))
print(isogram("aba"))
print(isogram("MoOse"))
print(isogram("isIsogram"))
print(isogram(""))

def xo(s):
    my_str = [char.lower() for char in s]
    xtot = 0
    ototal = 0

    for i in range(len(my_str)):
        if my_str[i] == "x":
            xtot += 1
        if my_str[i] == "o":
            ototal += 1

    if xtot == ototal:
        return True
    
    return False

print(xo("xo"))
print(xo("xo0"))
print(xo("xxxoo"))

def to_jaden_case(string):
    working_list = string.split(" ")
    new_list = []
    
    for j in range(len(working_list)):
        cap_string = [char for char in working_list[j]]
        new_list.append(cap_string[0].upper() + ''.join(cap_string[1:]))

    str_final = ' '.join(new_list)

    return str_final

print(to_jaden_case("how can mirrors be real if our eyes aren't real"))

def to_jaden_case(string):
    working_list = string.split(" ")
    new_list = []
    new_list2 = []

    for donuts in working_list:
        cap_string = [char for char in donuts]
        new_list.append(cap_string[0].upper() + ''.join(cap_string[1:]))
        if len(donuts) >= 2:
            new_donut = donuts[0] + str(donuts[1].upper()) + donuts[2:]
            new_list2.append(new_donut)
    str_final = ' '.join(new_list)
    str_final2 = ' '.join(new_list2)

    return str_final, str_final2

print(to_jaden_case("let me see if this works"))

def find_short(s):
    working_list = s.split(" ")
    length = 0
    short = 100
    
    for i in working_list:
        length = len(i)
        if length <= short:
            short = length
    return short
    
print(find_short("What would be the shortest word in this sentence"))

def DNA_strand(dna):
    new_strand = ""
    for char in dna:
        if char == "A":
            new_strand += "T"
        if char == "T":
            new_strand += "A"
        if char == "G":
            new_strand += "C"
        if char == "C":
            new_strand += "G"

    return new_strand

print(DNA_strand("ATTGC"))

def maskify(text):
    new_str = ""
    
    for index in range(len(text)):
        length = len(text)
        if index < length - 4:
            new_str += "#"
        else:
            new_str += text[index]

    return new_str

print(maskify("SocialSecurityNumber"))
print(maskify(""))
print(maskify("123"))
print(maskify("SF$SDfgsd2eA"))

def sum_two_smallest_numbers(numbers):
    low = float('inf')
    sec_low = float('inf')

    for i in range(len(numbers)):
        if numbers[i] < low:
            sec_low = low
            low = numbers[i]
    for i in range(len(numbers)):
        if numbers[i] < sec_low and numbers[i] > low:
            sec_low = numbers[i]

    return low + sec_low

print(sum_two_smallest_numbers([3,7,5,11,4,13,124])) 

def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    x = len(sorted_numbers)
    return sum(sorted_numbers[x-2:]), sum(sorted_numbers[:2])

print(sum_two_smallest_numbers([3, 7, 5, 11, 4, 3, 124]))  # Output: 6

def get_sum(a,b):
    total = 0
    work_list = []

    if b - a >= 0:
        while a <= b:
            work_list.append(a)
            a += 1
    else:
        while b <= a:
            work_list.append(b)
            b += 1

    for j in work_list:
        total = total + j

    return total

print(get_sum(0,1))
print(get_sum(0,-1))

def longest(a1, a2):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    long_str = a1 + a2
    work_list = []

    work_string = [char for char in alpha]
    print(work_string)
    for i in long_str:
        if i in work_string and i not in work_list:
            work_list.append(i)
            
    str_final = ''.join(sorted(work_list))
    
    return str_final



print(longest(("aretheyhere"), ("yestheyarehere")))
print(longest(("loopingisfunbutdangerous"), ("lessdangerousthancoding")))
print(longest(("inmanylanguages"), ("theresapairoffunctions")))

def friend(start_list):
    friend_list = []

    for i in start_list:
        if len(i) == 4:
            friend_list.append(i)
    return friend_list

print(friend(["Ryan", "Kieran", "Mark"]))
print(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]))
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))

def friend(start_list):
    friend_list = []

    for i in range(len(start_list)):
        if len(start_list[i]) == 4:
            friend_list.append(start_list[i])
    return friend_list

print(friend(["Ryan", "Kieran", "Mark"]))
print(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]))
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))

def open_or_senior(data):
    output = []

    for i in data:
        if i[0] >= 55 and i[1] > 7:
            output.append("Senior")
        else:
            output.append("Open")

    return output

print(open_or_senior([(45,12),(55,21),(19,-2),(104,20)]))
print(open_or_senior([(16,23),(73,1),(56,20),(1,-1)]))

import math

def find_next_square(sq):
    root = math.sqrt(sq)
    decimal_place = str(root).split('.')[1]
    if len(decimal_place) < 2:
        root = int(root)
        return (root + 1) ** 2
    else:
        return -1
    
print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(319225))
print(find_next_square(15241383936))

def printer_error(s):
    denominator = len(s)
    alpha = 'nopqrstuvwxyz'
    numerator = 0

    alpha_list = [char for char in alpha]

    for i in s:
        if i in alpha_list:
            numerator += 1

    final = str(numerator) + "/" + str(denominator)

    return final

print(printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'))
print(printer_error('kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'))
print(printer_error('kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu'))

my_tuple = (1, 2, 'Hello')
string_representation = str(my_tuple)  # Converts tuple to string '(1, 2, 'Hello')'

# Remove the parentheses and commas from the string using replace()
without_parentheses = string_representation.replace("(", "").replace(")", "").replace(",", "")

print(without_parentheses)  # Output: 1 2 'Hello'

# Alternatively, remove the parentheses and commas using join() and split()
without_parentheses = ' '.join(string_representation.split(', ')).replace("(", "").replace(")", "")

print(without_parentheses)  # Output: 1 2 'Hello'

def nb_year(p0, percent, avg, p):
    n = 0
    percent_float = float(percent) / 100
    while p0 <= p:
        p0 = p0 + (p0 * percent_float) + avg
        n += 1
    return n

print(nb_year(1500, 5, 100, 5000))
print(nb_year(1500000, 2.5, 10000, 2000000))
print(nb_year(1500000, 0.25, 1000, 2000000))

def validate_pin(pin):
    nums = "0123456789"
    list_num = [char for char in nums]
    list_pin = [char for char in pin]
    print(list_num)
    
    for i in list_pin:
        if i not in list_num:
            return False
    if len(list_pin) == 4 or len(list_pin) == 6:
        return True
    else:
        return False

print(validate_pin("12.0"))
print(validate_pin("12"))
print(validate_pin("123"))
print(validate_pin("12345"))
print(validate_pin("1234567"))
print(validate_pin("-1234"))
print(validate_pin("-12345"))

num = 16
binary = bin(num)
print(binary)

def add_binary(a,b):
    x = a + b
    x_binary = bin(x)[2:]
    return x_binary

print(add_binary(1,1))
print(add_binary(0,1))
print(add_binary(1,0))
print(add_binary(2,2))
print(add_binary(51,12))

def add_binary(a,b):
    x = a + b
    x_binary = ""
    
    while x > 0:
        if x % 2 == 1:
            x_binary += "1"
        else:
            x_binary += "0"
        x //= 2

    #Or reverse function rev_x_binary = ''.join(reversed(x_binary))
    
    return x_binary[::-1]

print(add_binary(1,1))
print(add_binary(0,1))
print(add_binary(1,0))
print(add_binary(2,2))
print(add_binary(51,12))
    

def row_sum_odd_numbers(n):
    start_num = 1 + sum(range(n)) * 2
    odd_nums = [start_num + 2*i for i in range(n)]
    total = sum(odd_nums)
    return total

print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(13))
print(row_sum_odd_numbers(19))
print(row_sum_odd_numbers(41))

def solution(text, ending):
    x = len(ending)

    text_sub = text[len(text)-len(ending):len(text)]
    if text_sub == ending:
        return True
    else:
        return False

print(solution('samurai', 'ai'))
print(solution('ninja', 'ja'))
print(solution('sensei', 'i'))
print(solution('abc', 'abc'))
print(solution('abcabc', 'bc'))
print(solution('fails', 'ails'))

print(solution('sumo', 'omo'))
print(solution('samurai', 'ra'))
print(solution('abc', 'abcd'))
print(solution('ails', 'fails'))
print(solution('this', 'fails'))
print(solution('spam', 'eggs'))

my_string = "Putting an A in a string list"
my_str_list = [1 if char == 'a' else char for char in my_string]
print(my_str_list)

my_string = "Putting an A in a string list"
my_str_list = [char.upper() if char != ' ' else 'SPACE' for char in my_string]
print(my_str_list)

def number(bus_stops):
    passengers = 0

    for num in bus_stops:
        passengers = passengers + num[0]
        passengers = passengers - num[1]

    return passengers

print(number([[10,0],[3,5],[5,8]]))
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))

def odd_or_even(arr):
    total = 0

    for i in arr:
        total += i

    if total % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(odd_or_even([0,1,2]))
print(odd_or_even([0,1,3]))
print(odd_or_even([1023,1,2]))

def divisors(integer):
    divisors = []
    i = 2

    while i < integer:
        if integer % i == 0:
            divisors.append(i)
        i += 1

    if len(divisors) == 0:
        return str(integer) + " is prime"

    return divisors

print(divisors(13))
print(divisors(253))
print(divisors(24))
print(divisors(25))
print(divisors(13))
print(divisors(3))
print(divisors(29))

def remove_smallest(numbers):
    lowest = float('inf')

    if len(numbers) == 0:
        return []
    
    for i in numbers:
        if i < lowest:
            lowest = i
    index = numbers.index(lowest)
    numbers.pop(index)  # pop needs the index NOT the value

    return numbers

print(remove_smallest([1,2,3,4,5]))
print(remove_smallest([5,3,2,1,4]))
print(remove_smallest([1,2,3,1,1]))
print(remove_smallest([]))

def number(lines):
    
    for i in range(len(lines)):
        lines[i] = str(i+1) + ": " + lines[i]

    return lines

print(number(["a", "b", "c"]))

def min_max(lst):
    low = float('inf')
    high = float('-inf')
    new_list = []

    for i in lst:
        if i < low:
            low = i
        if i > high:
            high = i
    
    new_list.append(low)
    new_list.append(high)

    return new_list

print(min_max([1,2,3,4,5]))
print(min_max([2334454,5]))

def dont_give_me_five(start,end):
    i = start
    my_list = []
    
    while i <= end:
        if i % 2 != 0 and i % 5 == 0:
            pass
        elif '5' not in str(i):
            my_list.append(i)  #This is all that is actually needed
        i += 1

    print(my_list)
    return len(my_list)

print(dont_give_me_five(1,9))
print(dont_give_me_five(4,17))
print(dont_give_me_five(1,90))

def dont_give_me_five(start, end):
    my_list = [i for i in range(start, end + 1) if '5' not in str(i)]
    print(my_list)
    return len(my_list)


print(dont_give_me_five(1,9))
print(dont_give_me_five(4, 17))

def odds_evens(l1, l2):
    final = []
    
    for i in range(len(l1)):
        if i % 2 != 0:
            final.append(l1[i])

    for i in range(len(l2)):
        if i % 2 == 0:
            final.append(l2[i])

    return final

print(odds_evens([3,6,9,12,15,18,21], [4,8,12,16,20,24,28]))

def stray(arr):
    a = arr[0]
    b = 0
    a_count = 0
    b_count = 0

    for i in arr:
        if i == a:
            a_count += 1
        if i != a:
            b = i
            b_count += 1

    if a_count - b_count > 0:
        return b
    else:
        return a
    
print(stray([1,1,1,1,1,1,2]))
print(stray([2, 3, 2, 2, 2]))
print(stray([3, 2, 2, 2, 2]))

def stray(arr):
    unique_numbers = set(arr)
    for num in unique_numbers:
        if arr.count(num) == 1:
            return num

    
print(stray([1,1,1,1,1,1,2]))
print(stray([2, 3, 2, 2, 2]))
print(stray([3, 2, 2, 2, 2]))

def divisors(n):
    count = 0
    i = 1
    
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1

    return count

print(divisors(1))
print(divisors(4))
print(divisors(5))
print(divisors(12))
print(divisors(30))
print(divisors(4096))

from fractions import Fraction

def series_sum(n):
    my_list = [1, Fraction(1,4), Fraction(1,7), Fraction(1,10), Fraction(1,13), Fraction(1,16)]
    total = 0
    
    for i in range(n):
        total += float(my_list[i])
            
    return '{:.2f}'.format(total)
    # return round(total * 100) / 100

print(series_sum(1))
print(series_sum(2))
print(series_sum(3))

def calculate_years(principal, interest, tax, desired):
    years = 0
    taxable = (principal * interest)
    
    if principal >= desired:
        return 0

    while principal < desired:
        principal += (principal * interest) - (taxable * tax)
        years += 1

    return years

print(calculate_years(1000, 0.05, 0.18, 1100))
print(calculate_years(1000, 0.01625, 0.18, 1200))
print(calculate_years(1000, 0.05, 0.018, 1000))

def break_chocolate(n, m):
    z = (n * m) - 1
    if z > 0:
        return z
    else:
        return 0
    
print(break_chocolate(5, 5))
print(break_chocolate(7, 4))
print(break_chocolate(1, 1))
print(break_chocolate(0, 0))
print(break_chocolate(6, 1))
    
def nb_dig(n, d):
    square_list = []
    i = 0

    while i <= n:
        square_list.append(i ** 2)
        i  += 1

    string_list = [str(j) for j in square_list]
    count = 0
    
    for number in string_list:
        count += number.count(str(d))

    return count

print(nb_dig(5750, 0))
print(nb_dig(11011, 2))
print(nb_dig(12224, 8))
print(nb_dig(11549, 1))
print(nb_dig(14550, 7))
print(nb_dig(8304, 7))

def arithmetic(a, b, operator):

    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return round(a / b, 2)
    else:
        return "Not a recognized operator"
    
print(arithmetic(1, 2, "add"))
print(arithmetic(8, 2, "subtract"))
print(arithmetic(5, 2, "multiply"))
print(arithmetic(8, 2, "divide"))

def arithmetic(a, b, operator):
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: round(x / y, 2),
    }
    return operations.get(operator, lambda x, y: "Not a recognized operator")(a, b)

def gimme(input_array):
    high = float('-inf')
    low = float('inf')
    mid = 0

    for i in input_array:
        if i > high:
            high = i
        if i < low:
            low = i
    for k in input_array:
        if k != high and k != low:
            mid = k

    return input_array.index(mid)

print(gimme([2,3,1]))
print(gimme([5,10,14]))
    
def round_to_next5(n):
    if n % 5 == 0:
        y = n
    elif n > 0:
        x = n % 5
        y = n + (5 - x)
    elif n < 0:
        x = n % -5
        y = n - x
    elif n == 0:
        return 0
    
    return y

print(round_to_next5(0))
print(round_to_next5(1))
print(round_to_next5(-1))
print(round_to_next5(5))
print(round_to_next5(7))
print(round_to_next5(20))
print(round_to_next5(39))

def sequence_sum(begin_number, end_number, step):
    final_sum = 0
    num = begin_number

    if begin_number > end_number:
        return 0

    while num < end_number + 1:
        final_sum += num
        num += step

    return final_sum

print(sequence_sum(2, 6, 2))
print(sequence_sum(1, 5, 1)) 
print(sequence_sum(1, 5, 3)) 
print(sequence_sum(0, 15, 3)) 
print(sequence_sum(16, 15, 3)) 
print(sequence_sum(2, 24, 22)) 
print(sequence_sum(2, 2, 2))  

from collections import Counter

def is_anagram(test, original):
    new_str = ""

    if len(test) != len(original):
        return False
    
    original_lower = original.lower()
    test_lower = test.lower()
    
    for i in original_lower:
        if i in test_lower:
            new_str = new_str + i

    if new_str == original_lower:
        return True
    else:
        return False
    
# The only way for the fourth one to work is with the Counter function
    
print(is_anagram("foefet", "toffee"))
print(is_anagram("Buckethead", "DeathCubeK"))
print(is_anagram("Twoo", "Woot"))
print(is_anagram("dumble", "bumble"))
print(is_anagram("ound", "round"))
print(is_anagram("apple", "pale"))

from collections import Counter

def is_anagram(test, original):
    # Convert both strings to lowercase
    original_lower = original.lower()
    test_lower = test.lower()

    # Check if the lowercase versions are anagrams
    return Counter(original_lower) == Counter(test_lower)

# Test cases
print(is_anagram("foefet", "toffee"))  # Output: True
print(is_anagram("Buckethead", "DeathCubeK"))  # Output: True
print(is_anagram("Twoo", "Woot"))
print(is_anagram("dumble", "bumble"))
print(is_anagram("ound", "round"))
print(is_anagram("apple", "pale"))

def solution(nums):
    if nums == None:
        return []
    
    sorted_list = sorted(nums)
    
    return sorted_list

print(solution([1,2,3,10,5]))
print(solution(None))
print(solution([]))
print(solution([20,2,10]))
print(solution([2,20,10]))

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            print(i)
            print(n)
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print(my_list)  # Output: [11, 12, 22, 25, 34, 64, 90]

def remove_url_anchor(url):
    new_str = ""
    for i in url:
        if i != "#":
            new_str = new_str + i
        if i == "#":
            break

    return new_str

print(remove_url_anchor("www.codewars.com#about"))
print(remove_url_anchor("www.codewars.com/katas/?page=1#about"))
print(remove_url_anchor("www.codewars.com/katas/"))

def remove_url_anchor(url):
    return url.split("#")[0]

def capitals(word):
    list_word = [char for char in word]
    cap_list =[]

    for i in range(len(list_word)):
        if list_word[i].isupper():
            cap_list.append(i)

    return cap_list

print(capitals("CodEWaRs"))

def two_oldest_ages(ages):
    second_oldest = 0
    oldest = 0

    for i in ages:
        if i > oldest:
            oldest = i
    for j in ages:
        x = ages.count(oldest)
        if j > second_oldest and j < oldest:
            second_oldest = j
        elif x >= 2:
            second_oldest = oldest
    
    return [second_oldest,oldest]

print(two_oldest_ages([1,5,87,45,8,8]))
print(two_oldest_ages([6,5,83,5,3,18]))
print(two_oldest_ages([10,1]))
print(two_oldest_ages([88,85,88,88]))

def small_enough(array, limit):
    large_count = 0

    for i in range(len(array)):
        if array[i] < limit:
            i += 1
        elif array[i] > limit:
            large_count += 1
            return False

    if large_count == 0:
        return True
    
print(small_enough([66, 101], 200))
print(small_enough([78,117,110,99,104,117,107,115], 100))
print(small_enough([101, 45, 75, 105, 99, 107], 107)),
print(small_enough([80, 117, 115, 104, 45, 85, 112, 115] ,120))
print(small_enough([1, 1, 1, 1, 1, 2] ,1))

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__

def declare_winner(fighter1, fighter2, first_attacker):
    second = ""
    
    if first_attacker == fighter1.name:
        first_attacker = fighter1
        second = fighter2
    else:
        first_attacker = fighter2
        second = fighter1
    
    while first_attacker.health > 0 and second.health > 0:
        second.health -= first_attacker.damage_per_attack
        
        if second.health <= 0:
            print(f"{first_attacker.name} attacks {second.name}: {second.name} now has {second.health} health and is dead. {first_attacker.name} wins.")
            break
        
        else:
            print(f"{first_attacker.name} attacks {second.name}; {second.name} now has {second.health} health. ")
        
        first_attacker.health -= second.damage_per_attack

        if first_attacker.health <= 0:
            print(f"{second.name} attacks {first_attacker.name}: {first_attacker.name} now has {first_attacker.health} health and is dead. {second.name} wins.")
            break
        
        else:
            print(f"{second.name} attacks {first_attacker.name}; {first_attacker.name} now has {first_attacker.health} health. ")
        
declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew")
declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Harry")
declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry")

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self):
        return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__

def declare_winner(fighter1, fighter2, first_attacker):
    second = ""

    if first_attacker == fighter1.name:
        first_attacker = fighter1
        second = fighter2
    else:
        first_attacker = fighter2
        second = fighter1
    
    while first_attacker.health > 0 and second.health > 0:
        second.health -= first_attacker.damage_per_attack
        
        if second.health <= 0:
            return first_attacker.name
        
        first_attacker.health -= second.damage_per_attack
        
        if first_attacker.health <= 0:
            return second.name

# Test cases
winner1 = declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew")
print("Winner:", winner1)  # This should print 'Lew'

winner2 = declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Harry")
print("Winner:", winner2)  # This should print 'Harry'

winner3 = declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry")
print("Winner:", winner3)  # This should print 'Harald'


def reverse_letter(string):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    first_list = [char for char in string]
    rev_list = []
    i = len(first_list) - 1
    
    while i > -1:
        if first_list[i] in alpha:
            rev_list.append(first_list[i])
        i -= 1

    rev_str = ''.join(rev_list)
    
    return rev_str
        

print(reverse_letter("krishan"))
print(reverse_letter("ultr53o?n"))
print(reverse_letter("ab23c"))
print(reverse_letter("krish21an"))

def sum_digits(number):
    nums = "123456789"
    str_num = str(number)
    sum_list = ['0' if char not in nums else char for char in str_num]
    final_num = 0

    for char in sum_list:
        char_num = int(char)
        final_num += char_num

    return final_num

print(sum_digits(10))
print(sum_digits(99))
print(sum_digits(-32))

def sum_digits(number):
    str_num = str(abs(number))
    digit_sum = sum(int(char) for char in str_num if char.isdigit())
    return digit_sum

print(sum_digits(10))
print(sum_digits(99))
print(sum_digits(-32))

def check_exam(arr1, arr2):
    score = 0

    for i in range(len(arr2)):
        if arr2[i] == "":
            score += 0
        elif arr1[i] == arr2[i]:
            score += 4
        else:
            score -= 1

    return max(0, score)

print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]))
print(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]))
print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]))

def max_multiple(divisor, bound):
    high_num = 0
    i = divisor

    while i <= bound:
        if i % divisor == 0:
            high_num = i
        i += 1

    return high_num

print(max_multiple(2, 7))
print(max_multiple(3, 10))
print(max_multiple(7, 17))
print(max_multiple(10, 50))
print(max_multiple(37, 200))
print(max_multiple(7, 100))

def solve(s):
    upper_count = 0
    lower_count = 0
    s_list = [char for char in s]

    for char in s_list:
        if char.isupper() == True:
            upper_count += 1
        else:
            lower_count += 1

    s_str = ''.join(s_list)

    if upper_count > lower_count:
        s_str = s_str.upper()
    else:
        s_str = s_str.lower()

    return s_str

print(solve("code"))
print(solve("CODe"))
print(solve("COde"))
print(solve("Code"))

def min_value(digits):
    low_num_list = []

    # Find the lowest number and add it to the list
    low = min(digits)
    low_num_list.append(low)
    
    # Find the second lowest number greater than the lowest number
    second_low = min(num for num in digits if num > low and num != min(digits))
    low_num_list.append(second_low)

    # Add the remaining numbers to the list
    for num in digits:
        if num != low and num != second_low and num not in low_num_list:
            low_num_list.append(num)

    final = int(''.join(map(str, low_num_list)))

    return final

print(min_value([1, 3, 1]))
print(min_value([4, 7, 5, 7]))
print(min_value([4, 8, 1, 4]))
print(min_value([1, 4, 1, 1, 1, 3, 7, 8, 8, 7, 3, 8, 6, 2, 5, 5, 7]))

def min_value(digits):
    sorted_digits = sorted(digits)  # Sort the digits in ascending order
    sorted_digits = [str(digit) for digit in sorted_digits]  # Convert digits to strings

    low_num_list = [sorted_digits[0]]  # Start with the lowest digit

    for _ in range(1, len(sorted_digits)):
        # Find the next highest digit that hasn't been used yet
        next_highest = None
        for digit in sorted_digits:
            if digit > low_num_list[-1] and digit not in low_num_list:
                next_highest = digit
                break
        
        if next_highest is None:
            # If no next highest digit is found, break the loop
            break
        
        low_num_list.append(next_highest)

    final = int(''.join(low_num_list))
    
    return final

print(min_value([1, 3, 1]))  # Output: 123
print(min_value([4, 7, 5, 7]))  # Output: 4577
print(min_value([4, 8, 1, 4]))  # Output: 1484
print(min_value([1, 4, 1, 1, 1, 3, 7, 8, 8, 7, 3, 8, 6, 2, 5, 5, 7]))  # Output: 112345678

def factorial(n):
    if n < 0 or n > 12:
        raise ValueError("Number must be between 1 and 12")
    
    total = 1
    i = 1

    while i <= n:
        total = total * i
        i += 1

    return total

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))

def capitalize(s):
    my_str = [char for char in s]
    my_str_two = [char for char in s]

    for char, c in enumerate(my_str):
        if char % 2 == 0:
            my_str[char] = c.upper()

    for char, d in enumerate(my_str_two):
        if char % 2 != 0:
            my_str_two[char] = d.upper()

    return [''.join(my_str),''.join(my_str_two)]

print(capitalize("abcdef"))
print(capitalize("codewars"))
print(capitalize("abracadabra"))
print(capitalize("codewarriors"))

def sum_of_minimums(*args):
    count = 0

    for lst in args:
        min_value = min(lst)  # Find the minimum value in the current list
        count += min_value

    return count

print(sum_of_minimums([1,2,3], [5,6,7], [7,8,2]))

def sum_of_minimums(numbers):
    #results = []
    count = 0
    
    for inner_list in numbers:
        min_value = 1000
        for num in inner_list:
            if num < min_value:
                min_value = num
        count += min_value
            
        #results.append(min_value)
    return count

print(sum_of_minimums([[ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]))
print(sum_of_minimums([[11,12,14,54], [67,89,90,56], [7,9,4,3], [9,8,6,7] ]))

def flatten_and_sort(array):
    flat_and_ascending = []
    
    for inner_list in array:
        flat_and_ascending.extend(inner_list)

    flat_and_ascending.sort()
    return flat_and_ascending

print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    print(pivot)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage
my_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quick_sort(my_list)
print(sorted_list)

def in_asc_order(arr):
    i = 0

    for i in range(len(arr)-1):
        if arr[i+1] <= arr[i]:
            break
    else:
        return True
        
    return False
        
print(in_asc_order([1,2]))
print(in_asc_order([2,1]))
print(in_asc_order([1,2,3]))
print(in_asc_order([1,3,2]))
print(in_asc_order([1,4,13,97,508,1047,20058]))
print(in_asc_order([56,98,123,67,742,1024,32,90969]))

from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    date_format = "%B %d, %Y"
    purchase_date = datetime.strptime(current_date, date_format)
    coup_expiration_date = datetime.strptime(expiration_date, date_format)

    if entered_code != correct_code or purchase_date > coup_expiration_date:
        return False
    
    return True

print(check_coupon("123", "123", "September 5, 2014", "October 1, 2014"))
print(check_coupon("123a", "123", "September 5, 2014", "October 1, 2014"))

def row_weights(array):
    team_1 = []
    team_2 = []
    team_1_weight = 0
    team_2_weight = 0

    for i in range(len(array)):
        if i % 2 == 0:
            team_1.append(array[i])
        else:
            team_2.append(array[i])

    for num in team_1:
        team_1_weight += num

    for num in team_2:
        team_2_weight += num

    return team_1_weight, team_2_weight


print(row_weights([80]))
print(row_weights([100,50]))
print(row_weights([50,60,70,80]))
print(row_weights([13,27,49]))
print(row_weights([70,58,75,34,91]))
print(row_weights([29,83,67,53,19,28,96]))
print(row_weights([0]))

def row_weights(array):  #THIS IS THE WAY WITH SLICING
    team_1_weight = sum(array[::2])
    team_2_weight = sum(array[1::2])
    return team_1_weight, team_2_weight

print(row_weights([4, 5, 6, 7]))

def remove_duplicate_words(s):
    updated_list = []
    words = s.split()

    for word in words:
        if word not in updated_list:
            updated_list.append(word)

    updated_string = ' '.join(updated_list)

    return updated_string

print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
print(remove_duplicate_words("my cat is my cat fat"))

#creating SETS versus arrays
def remove_duplicate_words(s):
    updated_list = []
    seen_words = set()
    words = s.split()

    for word in words:
        if word not in seen_words:
            seen_words.add(word)
            updated_list.append(word)

    updated_string = ' '.join(updated_list)

    return updated_string

print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
print(remove_duplicate_words("my cat is my cat fat"))

def mxdiflg(a1,a2):
    nums_a1 = []
    nums_a2 = []

    if len(a1) == 0 or len(a2) == 0:
        return -1

    for string in a1:
        nums_a1.append(len(string))
    for string in a2:
        nums_a2.append(len(string))

    if max(nums_a2) - min(nums_a1) > max(nums_a1) - min(nums_a2):
        return max(nums_a2) - min(nums_a1)
    else:
        return max(nums_a1) - min(nums_a2)

print(mxdiflg(["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"], ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]))
print(mxdiflg(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], ["bbbaaayddqbbrrrv"]))
print(mxdiflg(["ejjjjmmtthh"], ["bbbaaayddqbbrrrv"]))

import string

def words_to_marks(s):
    #I don't have to convert to a list, but I'll leave this to have a list comprehension to reference
    letter_to_number = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase)}
    s_list = [char for char in s]
    total = 0

    for char in s_list:
        total += letter_to_number[char]

    return total

print(words_to_marks('attitude'))
print(words_to_marks('friends'))

def largest_pair_sum(numbers):
    ascending = sorted(numbers, reverse=True)
    leaders = ascending[0] + ascending[1]
    
    if leaders < 0:
        return 0
    
    return leaders

print(largest_pair_sum([10,14,2,23,19]))
print(largest_pair_sum([-100,-29,-24,-19,19]))
print(largest_pair_sum([1,2,3,4,6,-1,2]))
print(largest_pair_sum([-10, -8, -16, -18, -19]))

