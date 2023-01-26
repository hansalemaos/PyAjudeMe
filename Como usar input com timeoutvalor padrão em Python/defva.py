from input_timeout import InputTimeout

i = InputTimeout(
    timeout=3,
    input_message=("Quem é você? Responda" " dentro de 3 segundos"),
    timeout_message=("Lento, hein?"),
    defaultvalue=("preguiçoso"),
    cancelbutton="esc",
).finalvalue
nome = input()
print(f"Valor: {i}")
