# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321

# Example 2:

# Input: x = -123
# Output: -321

# Example 3:

# Input: x = 120
# Output: 21

 

# Constraints:

#     -231 <= x <= 231 - 1


def main(x):
    min= -2**31
    max= 2**31


    negetive=False

    if x<0:negetive=True

    rev = int("".join(i for i in reversed(str(x).replace("-",""))))

    rev= rev if not negetive else 0-rev

    if rev > max or rev<min:
        return 0
    else:
        return rev


print(main(123))


