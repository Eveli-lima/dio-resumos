email = input().strip()


usuario = email.count("@")

if usuario == 1 and email[0] != "@" and email[-1] != "@" and " " not in email:
    print("E-mail válido")
else:
    print("E-mail inválido")



#print(email.index("@"))
#print(email.count("@"))