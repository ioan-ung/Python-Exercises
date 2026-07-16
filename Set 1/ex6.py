def camel_to_snake(text):
    result = ""

    for i,char in enumerate(text):
        if char.islower():
            result += char
        else:
            if i != 0:
                result += '_'
            result += char.lower()
    return result

print(camel_to_snake("CamelCaseText"))