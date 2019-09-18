# get user email adress

email = input("What is yout email adress?: ").strip()

# slice out user name

user = email[:email.index("@")]

# slice domain name

domain = email[email.index("@")+ 1:]

#format message

output = "Your username is {} and your domain name is {}".format(user, domain)

#display output message

print (output)
