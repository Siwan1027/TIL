# baekjun problem no.1929
# 에라토스테네스의 채 https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
import sys

input = sys.stdin.readline

m,n = map(int,input().split())

def erasto(num):
    if num <2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
        
for i in range(m,n+1):
    if erasto(i):
        print(i)

# 타 풀이에서 찾은 좋은 예
def eratosthenes_sieve(m, n):
    n += 1  # 범위를 m에서 n까지 포함하도록 n에 1을 더함

    # 처음에는 모든 숫자가 소수라고 가정하고, 리스트의 모든 원소를 True로 설정
    sieve = [True] * n

    # 3부터 n의 제곱근까지의 모든 숫자를 확인
    # 소수의 배수는 소수가 아니므로 해당 숫자의 배수들을 모두 False로 설정
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i:: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)

        # 리스트에서 True로 남아있는 숫자들을 소수로 간주하고 이들을 모두 찾음
    # 그 중에서 m 이상인 숫자들만 선택
    primes = [a for a in range(3, n, 2) if sieve[a] and a >= m]

    # m이 2 이하인 경우 2를 소수 목록에 추가
    if m <= 2: primes = [2] + primes
    return primes  # 소수 목록을 반환


m, n = map(int, input().split())  # m과 n을 입력받음
prime_numbers = eratosthenes_sieve(m, n)  # m과 n 사이의 모든 소수를 찾음

# 찾은 소수들을 모두 출력
for prime in prime_numbers:
    print(prime)