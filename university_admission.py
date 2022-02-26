N = int(input())
departments = {department: {} for department in ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']}
preferences = []
with open('applicants.txt', 'rt', encoding='utf-8') as file:
    for line in file.read().split('\n'):
        columns = [col for col in line.split() if len(line.split()) == 10]
        [name, surname, physics, chemistry, math, computer_science, special, department1, department2, department3] = columns
        weights =  [[chemistry, physics], [chemistry], [computer_science, math], [math], [physics, math]]
        for order, department in enumerate([department1, department2, department3], start=1):  # department preferences = choices
            preferences.append([name + ' ' + surname, order, department, {discipline: (sum([float(grade) for grade in grades])) / len(grades) if (sum([float(grade) for grade in grades])) / len(grades) > float(special) else float(special) for discipline, grades in zip(departments, weights)}[department]])
for name, order, department, result  in sorted(preferences, key=lambda x: [x[1], -x[3], x[0]]):  # sort by: order, -grade, name+surname:
    if len(departments[department]) < N and name not in '×'.join(['×'.join(list(departments[department])) for department in departments if list(departments[department])]).replace('××', '').split('×'):  # if under N and the name didn't appear
        departments[department][name] = result  # {'Physics': {John Ritchie, 89}, ...}
for department in departments:
    with open(f'{department}.txt', 'wt', encoding='utf-8') as file:
        file.write('\n'.join([f'{name} {result}' for name, result in sorted(departments[department].items(), key=lambda x: [-x[1], x[0]])])) # sort by: -grade, name
