import random
import os

def create_test_file(filename, k, m, sequence):
    # tests folder exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as f: # write mode
        f.write(str(k) + " " + str(m) + "\n")

        seq_strings = []
        for num in sequence:
            seq_strings.append(str(num))
        f.write(" ".join(seq_strings) + "\n")
    print("Successfully created " + filename + " (k=" + str(k) + ", m=" + str(m) + ")")

def main():
    print("Starting test file generation..")

    # 1
    k1 = 5
    m1 = 60
    seq1 = []

    for i in range(m1):
        chance = random.random()
        if chance < 0.80:
            # hot
            seq1.append(random.choice([1, 2, 3, 4, 5, 6]))
        else:
            # cold
            seq1.append(random.choice([7, 8, 9, 10, 11, 12, 13, 14, 15]))

    create_test_file("tests/file1.in", k1, m1, seq1)

    #2
    k2 = 10
    m2 = 100
    seq2 = []

    for i in range(m2):
        random_num = random.randint(1, 30)
        seq2.append(random_num)

    create_test_file("tests/file2.in", k2, m2, seq2)

    # 3
    k3 = 3
    m3 = 75
    seq3 = []

    for i in range(m3):
        # i % 4 gives 0, 1, 2, 3. Add 1 to get 1, 2, 3, 4.
        val = (i % 4) + 1
        seq3.append(val)

    create_test_file("tests/file3.in", k3, m3, seq3)

    print("Done generating tests!")

if __name__ == "__main__":
    main()