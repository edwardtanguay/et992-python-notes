def get_http_code():
	return 200, "OK"

response = get_http_code()
print(response)
print(type(response))