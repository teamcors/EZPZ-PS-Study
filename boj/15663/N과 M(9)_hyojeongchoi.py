def main():
    n,m = map(int,input().split())
    nums = list(map(int, input().split()))
    visited = [False] * n 
    answers = []

    def permuatation(nums,n,m,arr):
        if len(arr) == m:
            answers.append(arr[:]) 
            return

        for i in range(len(nums)):
            if not visited[i]: 
                visited[i] = True 
                arr.append(nums[i])
                permuatation(nums,n,m,arr)
                visited[i] = False 
                arr.pop()

    permuatation(nums,n,m,[])
    answers = sorted(list(set(map(tuple, answers)))) 
    for answer in answers:
        print(*answer,sep=' ')

if __name__ == '__main__':
    main()
