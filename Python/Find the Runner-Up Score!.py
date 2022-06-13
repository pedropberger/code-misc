if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    
arr=list(arr)
m = max(arr)
min = min(arr)

second = [arr[i] if arr[i]<m else min for i in range(0,n)]

print(max(second))
