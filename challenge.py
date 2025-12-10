
def is_balanced(num):
    s = str(num)
    n = len(s)

    # Determine the split point
    half = n // 2

    if n % 2 == 0:
        left = s[:half]
        right = s[half:]
    else:
        left = s[:half]
        right = s[half+1:]

    # Compute digit sums
    left_sum = sum(int(d) for d in left)
    right_sum = sum(int(d) for d in right)

    return left_sum == right_sum

print(is_balanced(123321)) # expected True
print(is_balanced(12321)) # expected True
print(is_balanced(94049)) # expected True
print(is_balanced(11112)) # expected False
print(is_balanced(5)) # expected True (single digit is trivially balanced)
print(is_balanced(1010)) # expected False
print(is_balanced(1001)) # expected True