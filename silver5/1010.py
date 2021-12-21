#왼쪽에 N, 오른쪽에 M개의 사이트에서 다리를 만들 때(N <= M), 만들 수 있는 경우의 수. 이 때 다리는 겹칠 수 없다.
T = int(input())
def factorial(m):
    if(m <= 1):
        return 1
    return m * factorial(m - 1)

def C(m, n):
    x = factorial(m)
    y = factorial(n)
    z = factorial(m - n)

    return int(x / (y * z))


for i in range(T):
    N, M = map(int, input().split())
    print(C(M, N))