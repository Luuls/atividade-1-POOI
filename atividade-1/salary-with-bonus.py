COMISSION = 0.15

name = input()
salary = float(input())
value_sold = float(input())

final_salary = salary + COMISSION * value_sold

print(f'TOTAL = R$ {final_salary:.2f}')
