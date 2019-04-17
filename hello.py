# test file 

print("hello kitty")

var_file = "index.html"
with open(var_file) as file_in:
    contents = file_in.readlines()

print("contents:")
print(contents)

print("\nwe printed the index.html file contents")
