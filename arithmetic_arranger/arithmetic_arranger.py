def arithmetic_arranger(problems, with_solution=False):
    problems_split = [problem.split() for problem in problems]
    if len(problems_split) > 5:
        return "Error: Too many problems."
    if any(len(problem) != 3 for problem in problems_split):
        return "Error: wrong format."
    if any(problem[1] not in ('+', '-') for problem in problems_split):
        return "Error: Operator must be '+' or '-'."
    if any(not problem[0].isdigit() or not problem[2].isdigit() for problem in problems_split):
        return "Error: Numbers must only contain digits."

    max_lens = [max(len(problem[0]), len(problem[2])) for problem in problems_split]
    if any(ml > 4 for ml in max_lens):
        return "Error: Numbers cannot be more than four digits."

    lines = [
        [problem[0].rjust(ml + 2) for problem, ml in zip(problems_split, max_lens)],
        [problem[1] + problem[2].rjust(ml + 1) for problem, ml in zip(problems_split, max_lens)],
        ['-' * (ml + 2) for ml in max_lens]
    ]

    if with_solution:
        solutions = []
        for task in problems_split:
            if task[1] == '+':
                solutions.append(str(int(task[0]) + int(task[2])))
            elif task[1] == '-':
                solutions.append(str(int(task[0]) - int(task[2])))

        lines.append([solution.rjust(ml + 2) for solution, ml in zip(solutions, max_lens)])

    sep = ' ' * 4
    arranged_problems = '\n'.join(sep.join(line) for line in lines)
    return arranged_problems
