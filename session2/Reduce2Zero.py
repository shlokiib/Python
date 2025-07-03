def numberOfSteps(self, num):
    if num == 0:
        return 0
    if num % 2 == 0:
        return 1 + self.numberOfSteps(num // 2)
    else:
        return 1 + self.numberOfSteps(num - 1)

result = numberOfSteps(0,90)
print(result)