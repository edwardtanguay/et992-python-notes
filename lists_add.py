def is_color_present(color):
	if color in colors:
		print(f"{color} is a member")
	else:
		print(f"{color} is NOT a member")

colors = ['red', 'blue', 'green', 'amber', 'brown', 'violet']
print(colors)
new_colors = ['indigo', 'chartreuse']
colors.extend(new_colors)
print(colors)

is_color_present('brown')
is_color_present('periwinkle')
