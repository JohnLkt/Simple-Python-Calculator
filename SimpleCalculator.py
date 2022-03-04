# inputs

print("Ketik Angka 1: ")
a = int(input())
print("Ketik Angka 2: ")
b = int(input())
print("Ketik Operator: ")
c = input()

# calculations

match c:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)