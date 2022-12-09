file = input("Enter the file name : ")

def find_start_marker(code, n):
    stack = list(code[:n-1])
    count = n-1

    for ch in code[n-1:]:
        if len(set(stack + [ch])) == len(stack) + 1:
            break

        stack.pop(0)
        stack.append(ch)
        count += 1

    return count + 1


with open(file, 'r') as inp_file:
    code = inp_file.read().strip()
    count = find_start_marker(code, 4)
    print(count)
    count = find_start_marker(code, 14)
    print(count)
