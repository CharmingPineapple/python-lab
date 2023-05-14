# Вариант 19. Дана произвольная строка.
# Преобразовать ее, заменив звездочками все буквы "п", встречающиеся в
# её левой половине.

someStr = "программирование погромистов пора прекратить"
center = int(len(someStr)/2)
# print(center)
leftPart = someStr[:center]
leftPart = leftPart.replace("п", "*")
rightPart = someStr[center:len(someStr)]
result = leftPart + rightPart
print(result)
