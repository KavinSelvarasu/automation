princpleAmount = int(input('Enter Princple Amount: '))
percentage = int(input('Enter GST Percentage: '))

addSub = input('if u want add or subtract GST Amount(type add / sub): ').lower()


def add():
    total = ((princpleAmount * percentage) / 100)
    print(total)


def subtract():
    total = (princpleAmount - (princpleAmount * (100 / (100 + percentage))))
    print(total)


if addSub == 'add':
    add()
else:
    subtract()
