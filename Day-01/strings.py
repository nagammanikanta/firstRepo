message = "hello world"

print(message)

print(message[1])

print(message[0:5])


print(message[:4])

print(message.upper())

print(message.lower())

print(message.count('hello'))

print(message.find('yes'))

message = message.replace('world', 'Universe')
print(message)

greeting = 'hello'

name = 'manikanta'

data = greeting +', '+ name + '. welcome!'

print(data)

data = '{}, {}. welcome!'.format(greeting, name)

print(data)


data = f'{greeting.upper()}, {name.upper()}. welcome!'

print(data)