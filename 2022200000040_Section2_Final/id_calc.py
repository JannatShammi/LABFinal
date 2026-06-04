def sum_of_odds_from_id(student_id):

    student_id = student_id.replace(" ", "")

    if not student_id:
        return 0

    if not student_id.isdigit():
        return 0

    digit_sum = sum(int(digit) for digit in student_id)

    odd_sum = 0

    for i in range(1, digit_sum + 1):
        if i % 2 != 0:
            odd_sum += i

    return odd_sum