import math

def second_largest(numbers):
    return sorted(numbers)[-2]

numbers = [10, 5, 20, 8, 15]
second = second_largest(numbers)
print(second)

def count_vowels(text):
    count = 0
    vowels="AEIOU"
    for char in text.upper():
        if char in vowels :
            count = count+1
    return count

text = "Hello World"
vowel_count = count_vowels(text)
print(vowel_count)


n = int(input("Enter a number : "))

def print_prime(n):
    prime_list=[]
    for num in range(2, n+1):
        isPrime = True
        for i in range(2,int(math.sqrt(num))+1):
            if num % i ==0:
                isPrime = False
                break

        if isPrime:
            prime_list.append(num)
    return prime_list

print(print_prime(n))


def merge_sorted_list(list1, list2):
    result=[]
    a=b=0

    while a < len(list1) and b <len(list2) :
        if list1[a] < list2[b] :
            result.append(list1[a])
            a += 1
        else:
            result.append(list2[b])
            b += 1

    result.extend(list1[a:])
    result.extend(list2[b:])
    return result

list1 = [1, 4, 5]
list2 = [1, 3, 4]
merged = merge_sorted_list(list1,list2)
print(merged)



    