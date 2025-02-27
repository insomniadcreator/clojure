
def my_rest(sequence):
    if not sequence:
        return None
    return sequence[1:]

def gcd(a, b):

    match (a, b):
        case (0, b):  
            return b
        case (a, 0): 
            return a
        case _:  
            return gcd(b, a % b)

if __name__ == "__main__":

    print("Пример my_rest:")
    print(my_rest([1, 2, 3, 4]))  
    print(my_rest([])) 


    print("\nПример gcd:")
    print(gcd(48, 18)) 
    print(gcd(17, 5)) 