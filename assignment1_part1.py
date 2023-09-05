class ListDivideException(Exception):
    pass

def list_divide(numbers, divide=2):
    count = 0
    for num in numbers:
        if num % divide == 0:
            count += 1
    return count

def test_list_divide():
    result = list_divide([1, 2, 3, 4, 5])
    if result != 2:
        raise ListDivideException("Test 1 failed")

    result = list_divide([2, 4, 6, 8, 10])
    if result != 5:
        raise ListDivideException("Test 2 failed")

    result = list_divide([30, 54, 63, 98, 100], divide=10)
    if result != 2:
        raise ListDivideException("Test 3 failed")

    result = list_divide([])
    if result != 0:
        raise ListDivideException("Test 4 failed")

    result = list_divide([1, 2, 3, 4, 5], 1)
    if result != 5:
        raise ListDivideException("Test 5 failed")

    print("All tests passed!")

if __name__ == "__main__":
    try:
        test_list_divide()
    except ListDivideException as e:
        print(f"Exception: {e}")
