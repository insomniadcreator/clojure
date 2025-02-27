
increment = lambda n: n + 1
double = lambda n: n * 2
square = lambda n: n ** 2
process_number = lambda n: n + 2 if n % 2 == 0 else 3 * n - 1


if __name__ == "__main__":
    print("Пример increment, double и square:")
    print(increment(5)) 
    print(double(5))  
    print(square(5))  

    print("\nПример process_number:")
    print(process_number(4))  
    print(process_number(5)) 