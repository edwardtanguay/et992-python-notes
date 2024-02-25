user = {
	"name": "Georg",
	"age": 45,
	"isMember": False,
	"projects": ['Project 001', 'Project 002']
}

print("user:", user)
print(f"Age is: {user['age']}")
# print("error", user["insurance"])
print("no error:", user.get("insurance"))
print("insurance:", user.get("insurance", "Sorry, no insurance entry found."))
print("projects:", user.get("projects", "Sorry, no projects entry found."))
