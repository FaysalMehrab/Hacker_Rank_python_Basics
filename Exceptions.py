t = int(input())

for i in range(t):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except Exception as e:
        print(f"Error Code: {e}")