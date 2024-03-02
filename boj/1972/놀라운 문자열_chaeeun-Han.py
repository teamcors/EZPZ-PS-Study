while True:
    exit_state = False
    str = input()
    if str == '*':
        break

    for dis in range(1, len(str)-1):
        hash = {}
        for i in range(len(str)-dis):
            pair = str[i] + str[i+dis]
            if pair in hash:
                exit_state = True
                print(str,"is NOT surprising.")
                break
            else:
                hash[pair] = 1
        if exit_state:
            break
    else:
        print(str,"is surprising.")
