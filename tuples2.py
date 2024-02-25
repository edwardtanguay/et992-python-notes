user = ('ralf', 45, 'developer', False)
user_name, age, _, is_speaker = user

print(f'The user has the user name "{user_name}", the user is {age} years old and {"is a speaker" if is_speaker else "is NOT a speaker"}.')
