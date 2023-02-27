"""
Implements the Fibonacci sequence using recursion and memoization.
"""
import sys


def r_fibonacci(n: int) -> int:
    """Recursive Fibonacci."""
    if n == 0 or n == 1:
        return 1

    return r_fibonacci(n - 1) + r_fibonacci(n - 2)


def m_fibonacci(n: int, memo: dict = {}) -> int:
    """Memoization Fibonacci."""
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        result = m_fibonacci(n - 1, memo) + m_fibonacci(n - 2, memo)
        memo[n] = result
        return result


def main():
    """Entry point"""
    sys.setrecursionlimit(999999)
    n: int = int(input("Enter a number: "))
    print(m_fibonacci(n))


if __name__ == "__main__":
    main()
