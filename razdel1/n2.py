def repeat(value):
    while True:
        yield value

def subseq(start, end, sequence):
    return sequence[start:end]

def in_first_half(element, sequence):
    half_index = len(sequence) // 2
    return element in sequence[:half_index]

if __name__ == "__main__":
    repeater = repeat(5)
    print("Пример repeat:")
    for _ in range(5):
        print(next(repeater), end=" ")  
    print()

    print("\nПример subseq:")
    print(subseq(2, 5, range(1, 10))) 

    print("\nПример in_first_half:")
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(in_first_half(3, sequence)) 
    print(in_first_half(7, sequence))  