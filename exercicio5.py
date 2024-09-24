def inverter_string(texto):
    string_invertida = ''
    for char in texto:
        string_invertida = char + string_invertida
    return string_invertida

# Exemplo de uso
texto = "Exemplo de string"
print(inverter_string(texto))
