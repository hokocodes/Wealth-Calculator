div = 0.01
c = 1000
i = 100000
interest = 0

count = 1
while count < 100:
  print("month " + str(count))
  print("invested " + str(i) )
  print("interest in total gained " + str(interest))
  print("interest gained this month " + str(i * div))
  print(" ")
  i = i + c + (i * div)
  interest = interest + (i * div)
  count += 1
  c += 200
