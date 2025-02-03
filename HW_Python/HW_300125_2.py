

candidates = [
    {'name': 'Дмитрий', 'age': 24, 'salary': 175000, 'skills': ['c#', 'c++', 'java']},
    {'name': 'Алексей', 'age': 32, 'salary': 120000, 'skills': ['python', 'javascript', 'sql']},
    {'name': 'Иван', 'age': 26, 'salary': 135000, 'skills': ['c#', 'c++', 'go']},
    {'name': 'Екатерина', 'age': 35, 'salary': 78000, 'skills': ['c#', 'python', 'sql']},
    {'name': 'Юлия', 'age': 42, 'salary': 80000, 'skills': ['python', 'sql']},
    {'name': 'Мирон', 'age': 37, 'salary': 11000, 'skills': ['c#', 'c++', 'java']}
]

def average_age(candidates):
    ages = [i['age'] for i in candidates]
    avg_age = sum(ages) / len(ages)
    return round(avg_age)


def salary(candidates):
    salaries = [i['salary'] for i in candidates]
    avg_salary = sum(salaries) / len(salaries)
    min_salary = min(salaries)
    max_salary = max(salaries)
    return round(avg_salary), min_salary, max_salary


def candidates_python(candidates):
    python = [i['name'] for i in candidates if 'python' in i['skills']]
    return python


def candidates_without_sql(candidaties):
    sql = [i['name'] for i in candidaties if 'sql' not in i['skills']]
    return sql


print(f"Средний возраст кандидатов - {average_age(candidates)} лет")
avg_salary, min_salary, max_salary = salary(candidates)
print(f"Средняя желаемая зарплата - {avg_salary} рублей")
print(f"Минимальная желаемая зарплата - {min_salary} рублей")
print(f"Максимальная желаемая зарплата - {max_salary} рублей")
print(f"Кандидаты, знающие Python: {', '.join(candidates_python(candidates))}")
print(f"Кандидаты, не знающие SQL: {', '.join(candidates_without_sql(candidates))}")
