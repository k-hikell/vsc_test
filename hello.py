# test file 

print("hello kitty")

var_file = "index.html"
with open(var_file) as file_in:
    contents = file_in.readlines()

print("contents:")
print(contents)

print("\nwe printed the index.html file contents")

#simple dictionary
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April"
}
 
print(months.get(2))
print(months[2])
