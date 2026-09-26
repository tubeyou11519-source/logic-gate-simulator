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

def full_adder(a, b, carry_in):
    sum1, carry1 = half_adder(a, b)
    sum2, carry2 = half_adder(sum1, carry_in)
    total_sum = sum2
    carry_out = OR(carry1, carry2)
    return total_sum, carry_out

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

    print("\nFull-Adder (adds two bits plus a carry-in):")
    for a in [False, True]:
        for b in [False, True]:
            for c_in in [False, True]:
                s, c_out = full_adder(a, b, c_in)
                print(f"{int(a)} + {int(b)} + carry_in={int(c_in)} = Sum: {int(s)}, Carry_out: {int(c_out)}")

if __name__ == "__main__":
    main()