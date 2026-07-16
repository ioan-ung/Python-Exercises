def pheasant(char_len,*strings):
    last_letters=""
    for i,string in enumerate(strings):
        first_letters=string[:char_len]
        if i and last_letters != first_letters:
            return False
        last_letters = string[-char_len:]
    return True


print(pheasant(2,"ana","vasile","nasu"))