# Write a program that prints the number of times the string 'bob' occurs in s

# test-string s:
s = 'bobcbboboooboopsadbob'
counter = 0
y = 0
for i in range(len(s)-2):
    if s[y:y+3] == 'bob':
        counter +=1
    y += 1
print("Number of times bob occurs is:", counter)