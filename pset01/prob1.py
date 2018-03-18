# Write a program that counts up the number of vowels contained in the string s

# test-string:
s = "sdjapofhaks"

vow = 0
for i in s:
    if i == 'e' or i == 'a' or i == 'i' or i == 'o' or i == 'u':
        vow += 1s
print("number of vowels:", vow)