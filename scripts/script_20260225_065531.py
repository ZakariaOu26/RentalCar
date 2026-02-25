# Auto-generated script
# Created: 2026-02-25T06:55:31.207058
# Account: Account 1

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    print("Script executed successfully!")
