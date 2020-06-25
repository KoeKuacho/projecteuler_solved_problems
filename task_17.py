"""
Problem 17: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

lst_numbers = []

units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
         'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds_thousands = ['hundred', 'thousand']

lst_numbers.extend(units)

for i in tens:
    lst_numbers.append(i)  # 20, 30, 40 - 90
    for j in units[0:9]:
        digit = f'{i} {j}'
        lst_numbers.append(digit)  # 21, 31, 41 - 91

for i in hundreds_thousands[:1]:
    for j in units[0:9]:
        hundreds = f'{j} {i}'
        lst_numbers.append(hundreds)   # 100 - 900
        for u in units:
            hundreds_u = f'{hundreds} and {u}'
            lst_numbers.append(hundreds_u)   # 101, 102 - 119
        for t in tens:
            hundreds_t = f'{hundreds} and {t}'
            lst_numbers.append(hundreds_t)  # 110, 120 - 190
            for uu in units[0:9]:
                digit = f'{hundreds} and {t}-{uu}'
                lst_numbers.append(digit)  # 121, 131, 141 - 191

lst_numbers.append(f'{units[0]} {hundreds_thousands[1]}')

counter_letter = 0

for i in lst_numbers:
    count = len(i.replace(' ', '').replace('-', ''))
    counter_letter += count

print(lst_numbers)
print('Length of list =', len(lst_numbers))
print('Result =', counter_letter)
