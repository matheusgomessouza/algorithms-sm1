numbers = [6, 2, 9, 4, 7, 3]
first_bucket = numbers[0:4]
second_bucket = numbers[4:4]

def sorting(numbers):
    for i in range(first_bucket.len(first_bucket)):
        if first_bucket[i] > first_bucket[i + 1]:
            previous = first_bucket[i]
            first_bucket[i] = first_bucket[i + 1]
            first_bucket[i + 1] = previous

    for i in range(second_bucket.len(second_bucket)):
        if second_bucket[i] > second_bucket[i + 1]:
            previous = second_bucket[i]
            second_bucket[i] = second_bucket[i + 1]
            second_bucket[i + 1] = previous

    sorted_bucket = first_bucket + second_bucket

    print(sorted_bucket)

sorting(numbers)
    