# from PIL.ImageChops import difference
#
# from python_base import set_numbers
#
# numbers = [4,6,7]
# def sum_numbers(numbers):
#     summ = sum(numbers)
#     return summ
#
# sum_result = sum_numbers(numbers)
# print(sum_result)
#
#
# def mult_numbers(numbers):
#     mult = 1
#     for i in numbers:
#         mult = mult * i
#     return mult
#
# mult_result = mult_numbers(numbers)
# print(mult_result)
#
#
# def  maximum(numbers):
#     max_number = max(numbers)
#     return max_number
#
# max_result = maximum(numbers)
# print(max_result)
#
#
# def  minimum(numbers):
#     min_number = min(numbers)
#     return min_number
#
# min_result = minimum(numbers)
# print(min_result)
#
# # ---------------------------
#
# strike = input(str('Enter the strike: '))
#
# def strike_value(strike):
#     words = strike.split()
#     total_words = len(words)
#     length_word = sum(1 for l in words if len(l) > 2)
#
#
#     return f'Total words: {total_words}', f'Words more then 2 symbols: {length_word}'
#
# strike_value = strike_value(strike)
# print(strike_value)
#
# low_symbols = strike.lower()
# print (low_symbols)
#
# upper_symbols = strike.upper()
# print (upper_symbols)


#------------------------------
#
# set_a = [1, 30, 30, 25, 24, 30, 1, 27, 25, 40]
# uniq_numbers = list(set(set_a))
# print(uniq_numbers)
#
# def new_numbers(uniq_numbers):
#     new_list = []
#     new = set(uniq_numbers)
#     for x in new:
#         if x > 24:
#             new_list.append(x)
#
#     return new_list
#
# result = new_numbers(uniq_numbers)
# print(result)

# -----------------------------

sm = 25
def meters(sm):
    meter = sm / 100
    return meter

result2 = meters(sm)
print(result2)

# -----------------------------

