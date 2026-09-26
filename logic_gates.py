def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def XOR(a, b):
    return a != b

def half_adder(a, b):
    sum_bit = XOR(a, b)
    carry_bit = AND(a, b)
    return sum_bit, carry_bit

def main():
    print("Digital Logic Simulator")
    print("Testing basic gates:\n")

    for a in [False, True]:
        for b in [False, True]:
            print(f"AND({int(a)}, {int(b)}) = {int(AND(a, b))}")

    print()
    for a in [False, True]:
        for b in [False, True]:
            print(f"OR({int(a)}, {int(b)}) = {int(OR(a, b))}")

    print()
    for a in [False, True]:
        print(f"NOT({int(a)}) = {int(NOT(a))}")

    print("\nHalf-Adder (adds two binary digits):")
    for a in [False, True]:
        for b in [False, True]:
            s, c = half_adder(a, b)
            print(f"{int(a)} + {int(b)} = Sum: {int(s)}, Carry: {int(c)}")

if __name__ == "__main__":
    main()