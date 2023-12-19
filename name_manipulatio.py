       #first part
#taking name from the user
print("\t\tfirst part")
name = input("enter your name ")
print("your name is: " + name)
#printing the number n of characters from the name of the user
n = int(input("how much character you want to display from your name?"))
print(name[:n] + "\n\n")
      #second part
#countting the number of vowels in the name of the user
print("\t\tsecond part")
count = 0
i = 0
j = 0
while i < len(name):
    j = 0
    vowel = "aeuoi"
    while j < 5:
        if vowel[j] == name[i]:
            count = count + 1
        j = j +1
    i = i + 1
print("the number of vowels in your name is: " + str(count) + "\n\n")
        #third part
#printing the name of the user in reverse
print("\t\tthird part")
num = len(name) - 1
reverse_name = ''
while num >= 0:
    reverse_name = reverse_name + name[num]
    num = num - 1
print("your reveresed name is:")
print(reverse_name)
    
