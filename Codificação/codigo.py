import re

def validar_cpf(cpf: str) -> bool:
    # Remover caracteres especiais
    cpf = re.sub(r'\D', '', cpf)

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcular os dois dígitos verificadores
    def calcular_digito(cpf, digito):
        peso = list(range(digito, 1, -1))
        soma = sum(int(cpf[i]) * peso[i] for i in range(digito - 1))
        resto = (soma * 10) % 11
        return 0 if resto == 10 else resto

    digito1 = calcular_digito(cpf, 10)
    digito2 = calcular_digito(cpf + str(digito1), 11)

    # Verificar se os dígitos verificadores estão corretos
    return cpf[-2:] == f'{digito1}{digito2}'

# Testando a função
cpf = '123.456.789-09'
if validar_cpf(cpf):
    print(f'O CPF {cpf} é válido.')
else:
    print(f'O CPF {cpf} é inválido.')
