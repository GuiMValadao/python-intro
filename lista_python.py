if __name__ == '__main__':
    N = int(input())


arr = []
cmd = []
for i in range(N):
    cmd = input().split()
    if cmd[0] == 'print':
        print(arr)
    elif cmd[0] == 'sort':
        arr.sort()
    elif cmd[0] == 'pop':
        arr.pop()
    elif cmd[0] == 'reverse':
        arr.reverse()
    elif cmd[0] == 'insert':
        arg = (int(cmd[1]), int(cmd[2]))
        arr.insert(arg[0], arg[1])
    elif cmd[0] == 'remove':
        arr.remove(int(cmd[1]))
    else:
        arr.append(int(cmd[1]))
