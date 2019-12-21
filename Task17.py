# Write the code which will write excepted data to files below
# For example given offices of Google:
# 1) google_kazakstan.txt
# 2) google_paris.txt
# 3)google_uar.txt
# 4)google_kyrgystan.txt
# 5)google_san_francisco.txt
# 6)google_germany.txt
# 7)google_moscow.txt
# 8)google_sweden.txt
# When the user will say “Hello”
# Your code must communicate and give a choice from listed offices. After it
# has to receive a complain from user, and write it to file chosen by user.
# Hint: Use construction “with open”

google_branches = {1: 'google_kazakhstan.txt',
                   2: 'google_paris.txt',
                   3: 'google_kyrgyzstan.txt',
                   4: 'google_san_francisco.txt',
                   5: 'google_germany.txt',
                   6: 'google_moscow.txt',
                   7: 'google_sweden.txt'
                   }
hi = input("Type hello:")
if hi == "Hello" or "hello":
    print(google_branches)

user_choice = int(input("Enter branch num:"))
user_text = input("Enter your text:")

if user_choice == 1:
    with open('google_kazakhstan.txt', 'w') as the_file:
        the_file.write(user_text)

if user_choice == 2:
    with open('google_paris.txt', 'w') as the_file:
        the_file.write(user_text)

if user_choice == 3:
    with open('google_kyrgyzstan.txt', 'w') as the_file:
        the_file.write(user_text)

if user_choice == 4:
    with open('google_san_francisco.txt', 'w') as the_file:
        the_file.write(user_text)

if user_choice == 5:
    with open('google_germany.txt', 'w') as the_file:
        the_file.write(user_text)

if user_choice == 6:
    with open('google_moscow.txt', 'w') as the_file:
        the_file.write(user_text)

if user_choice == 7:
    with open('google_sweden.txt', 'w') as the_file:
        the_file.write(user_text)
