def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def main():
    try:
        n = int(input("Enter the value of n for Fibonacci calculation: "))
        result = fibonacci(n)
        print(f"The {n}th Fibonacci number is: {result}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
