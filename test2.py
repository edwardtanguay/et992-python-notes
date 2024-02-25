import requests

api_url = "https://edwardtanguay.vercel.app/share/skills.json"

response = requests.get(api_url)
status_code = response.status_code

if status_code == 200:
	skills = response.json()
	print(f"{len(skills)} skills:")
	for skill in skills:
		print(f"{skill['name']} - {skill['description']}")

