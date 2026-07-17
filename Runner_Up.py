if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    st=set(arr)
    lst=list(st)
    lst.sort()
    print(lst[-2])
