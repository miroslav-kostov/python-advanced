numbers = list(map(int, input().split()))
negatives = [i for i in numbers if i < 0]
positives = [i for i in numbers if i > 0]

print(sum(negatives))
print(sum(positives))

if abs(sum(negatives)) > sum(positives):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")