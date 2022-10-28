def clean_string(text):
    output = ""
    for char in text:
        if (char >= "a" and char <= "z") or (char >= "A" and char <= "Z"):
            output += char
    # inside print as like question
    print("inside func: ", output)
    return output


s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
# printing the result outside of the func
print("outside func: ", output)
