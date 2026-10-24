def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

if __name__ == "__main__":
    n = 5
    print_numbers(n)