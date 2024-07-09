email = input("Enter the E-mail:")
domain = email.find('.')
website = email.find('@')
print('main:', email[:website])
print('Website',email[website:domain])
print('Domain:',email[domain:])

