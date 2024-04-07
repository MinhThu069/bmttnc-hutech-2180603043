def sum_positive_and_negative_numbers(input_string):
    numbers = []
    current_number = ""
    for char in input_string:
        if char.isdigit() or (char == '-' and current_number == ""):
            current_number += char
        elif current_number:
            numbers.append(int(current_number))
            current_number = ""
    if current_number:
        numbers.append(int(current_number))
    positive_sum = sum(x for x in numbers if x > 0)
    negative_sum = sum(x for x in numbers if x < 0)
    return positive_sum, negative_sum
input_string = input("Nhập chuỗi ký tự: ")
positive_sum, negative_sum = sum_positive_and_negative_numbers(input_string)
print("Tổng các số nguyên dương là:", positive_sum)
print("Tổng các số nguyên âm là:", negative_sum)
