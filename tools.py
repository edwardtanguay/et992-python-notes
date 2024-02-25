import requests

def uppercase_text(text):
	return text.upper()

def get_skills():
	api_url = "https://edwardtanguay.vercel.app/share/skills.json"

	response = requests.get(api_url)
	status_code = response.status_code

	if status_code == 200:
		skills = response.json()
		return skills
