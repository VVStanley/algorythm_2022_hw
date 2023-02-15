from multiprocessing import Pool
from random import randrange

from utils.decorators import CSVOutput

NAME_FILE = "numbers.bin"


@CSVOutput(folder="dz9_line_sort")
def generate_bin_file(n):
    print("START WORK!")
    amount = 1000
    with open("../test.bin", "a") as file:
        for _ in range(amount):
            tmp = ""
            for _ in range(n):
                tmp += hex(randrange(0, 65535))
            file.write(tmp)
    print(f"DONE! generate {amount * n}")


def start_generate():
    with Pool(20) as p:
        p.map(generate_bin_file, [10000] * 100)


if __name__ == "__main__":
    start_generate()
