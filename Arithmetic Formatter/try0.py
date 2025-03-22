def arithmetic_arranger(problems, show_answers=False):
    if len(problems)>5:
        raise TypeError('Error: Too many problems.')

    else:
        for problem in problems:
            pass







print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "45-55" ], True)