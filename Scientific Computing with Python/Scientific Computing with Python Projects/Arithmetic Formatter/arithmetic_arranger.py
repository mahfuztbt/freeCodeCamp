def arithmetic_arranger(problems, show_results=False):

    problems_list = []
    for problem in problems:
        problems_list += problem.split(" ")

    problems_digits = [pr.replace("+", '1') for pr in problems_list]
    problems_digits = [pr.replace("-", '-1') for pr in problems_digits]

    test_total = 0

    #  too many problems 
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        test_total += 1

    # Test Incorrect Operator 
    count_pl = 1
    tio = 0

    while count_pl < len(problems_list):

        count_ele = problems_list[count_pl]

        if count_ele == "+":
            count_ele = count_ele.replace("+", "0")
        if count_ele == "-":
            count_ele = count_ele.replace("-", "0")
        if count_ele.isdigit():
            tio += 1

        count_pl += 3

    if tio < len(problems):
        arranged_problems = "Error: Operator must be '+' or '-'."
        test_total += 1

    # Test Only Digits 
    count_pl = 0
    tod = 0

    while count_pl < len(problems_list):
        count_ele = problems_list[count_pl]
        count_ele2 = problems_list[count_pl + 2]
        if count_ele.isnumeric() and count_ele2.isnumeric():
            tod += 1
        count_pl += 3

    if tod < len(problems):
        arranged_problems = "Error: Numbers must only contain digits."
        test_total += 1

    # Test Too Many Digits 
    test_to_many_times = 0
    for pd in problems_digits:
        if len(pd) > 4:
            test_to_many_times += 1
    if test_to_many_times > 0:
        arranged_problems = "Error: Numbers cannot be more than four digits."
        test_total += 1

    if test_total == 0:
        total_test = 0
        first_row = ""
        second_row = ""
        underline_row = ""
        results = ""

        while total_test < len(problems_digits):

            if len(problems_digits[total_test]) > len(problems_digits[total_test + 2]):
                longest_digit = len(problems_digits[total_test])
            else:
                longest_digit = len(problems_digits[total_test + 2])

            # First numbers row
            first_row_spaces = longest_digit - len(problems_digits[total_test])
            first_row_formatted = (' ' * first_row_spaces) + problems_digits[total_test]
            first_row += "  " + first_row_formatted + "    "

            # Second numbers row
            second_row += problems_list[total_test + 1]
            second_row_spaces = longest_digit - len(problems_digits[total_test + 2])
            second_row_formatted = (' ' * second_row_spaces) + problems_digits[total_test + 2]
            second_row += " " + second_row_formatted + "    "

            # Underline row
            underline_row_spaces = longest_digit
            underline_formatted = ('-' * underline_row_spaces)
            underline_row += "--" + underline_formatted + "    "

            # Results row
            add = int(problems_digits[total_test]) + int(problems_digits[total_test + 1]) * int(problems_digits[total_test + 2])
            result_spaces = (2 + longest_digit) - len(str(add))
            result_formatted = (' ' * result_spaces) + str(add)
            results += result_formatted + "    "

            total_test += 3

        test_arrangement = first_row[:-4] + "\n" + second_row[:-4] + "\n" + underline_row[:-4]
        test_solutions = test_arrangement + "\n" + results[:-4]

        if show_results:
            arranged_problems = test_solutions
        else:
            arranged_problems = test_arrangement

    return arranged_problems
