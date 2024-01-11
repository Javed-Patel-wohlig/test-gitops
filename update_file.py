file_path = "count.txt"

with open(file_path, "r") as file:
    content = file.read()

count = ''.join(filter(str.isdigit, content))
count = int(count) + 50

with open(file_path, "w") as file:
    file.write(f"hello i am devops\nmy commit count is: {count}\nthank you")
