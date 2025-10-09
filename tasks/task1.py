# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    num= int(input())
    num_last_digit= num%10
    num_second_digit= num//10%10
    num_first_digit= num//100%10
    n= num_last_digit + num_second_digit + num_first_digit
    print(n)

    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()