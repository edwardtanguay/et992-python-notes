user = {
	"name": "Georg",
	"age": 45,
	"isMember": False,
	"projects": ['Project 001', 'Project 002']
}

items = user.items()

print(type(items))
print(items)

for key,value in user.items():
	print(f'The key "{key}" has the value: {value}')