colors = ('red', 'blue', 'green', 'amber', 'brown', 'violet')
print(type(colors))
print(colors[1])

user = ('ralf', 45, 'developer', True)
user_name, age, _, is_speaker = user

if is_speaker:
	speaker_text = "is a speaker"
else:
	speaker_text = "is NOT a speaker"
print(f'The user has the user name "{user_name}", the user is {age} years old and {speaker_text}.')
