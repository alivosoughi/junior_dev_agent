def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ensure that the function can be tested in a standalone manner by adding this block
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        try:
            number = int(sys.argv[1])
            print(is_prime(number))
        except ValueError:
            print('Please provide a valid integer.')
        except Exception as e:
            print(f'An error occurred: {e}')