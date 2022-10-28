def replace_comma_with_space(text):
    l = s.split(",")
    return " ".join(l)


s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)
