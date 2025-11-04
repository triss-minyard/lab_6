commenters = []
flag = -1
while flag != 0:
    user_input = input()
    if user_input == "":
        flag =0
    else:
        name, comment = user_input.split(":")
        commenters.append(name.strip())
unique_commenters = []
for commenter in commenters:
    if commenter not in unique_commenters:
        unique_commenters.append(commenter)
print (len(unique_commenters))
