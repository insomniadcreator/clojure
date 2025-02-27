
def increment(n):
    return n + 1

def double(n):
    return n * 2

def square(n):
    return n ** 2

def process_number(n):
    if n % 2 == 0: 
        return n + 2
    else:
        return 3 * n - 1

if __name__ == "__main__":
    print("Пример increment, double и square:")
    print(increment(5)) 
    print(double(5)) 
    print(square(5))  

    print("\nПример process_number:")
    print(process_number(4))  
    print(process_number(5))  