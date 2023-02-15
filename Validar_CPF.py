# Inicializando variáveis
cpf_digitado = []
soma_parcial1 = 0
soma_parcial2 = 0
multiplicador1 = 10
multiplicador2 = 11

while True:
    # Solicitando entrada de CPF do usuário e verificando se a entrada é alfanumérica
    cpf = input('Por favor, digite seu CPF sem pontos ou traços: ').strip()

    # Verificando se a entrada é numérica e tem exatamente 11 caracteres
    if not cpf.isdigit() or len(cpf) != 11:
        print('CPF inválido. Por favor, digite apenas números e verifique se seu CPF tem 11 caracteres.')
    else:
        # Adicionando entrada do usuário a uma lista
        cpf_digitado.append(cpf)
        for palavra in cpf:
            for letra in palavra:
                cpf_digitado.append(letra)
        cpf_digitado.pop(0)
        
        # Calculando o primeiro dígito de verificação do CPF
        num1 = cpf_digitado[0:9]
        for digito in num1:
            valor = multiplicador1 * int(digito)
            soma_parcial1 += valor
            if multiplicador1 >= 2:
                multiplicador1 -= 1
            elif multiplicador1 < 2:
                break
        digito_verificador1 = (soma_parcial1 * 10) % 11
        digito_verificador1 = digito_verificador1 if digito_verificador1 <= 9 else 0
        
        # Calculando o segundo dígito de verificação do CPF
        num2 = cpf_digitado[0:10]
        for i, digito in enumerate(num2):
            valor2 = multiplicador2 * int(digito)
            soma_parcial2 += valor2
            if multiplicador2 >= 2:
                multiplicador2 -= 1
            elif multiplicador2 < 2:
                break
        digito_verificador2 = (soma_parcial2 * 10) % 11
        digito_verificador2 = digito_verificador2 if digito_verificador2 <= 9 else 0
        
        # Extraindo as partes do dígito da entrada do CPF original e comparando com o CPF calculado
        digitos_verificadores = [digito for digito in cpf_digitado if isinstance(digito, str) and digito.isdigit()]
        cpf_formatado = "".join(digitos_verificadores)
        
        digitos_verificadores2 = [digito for digito in num1 if isinstance(digito, str) and digito.isdigit()]
        cpf_formatado2 = "".join(digitos_verificadores2)
        cpf_verificado = f'{cpf_formatado2}{digito_verificador1}{digito_verificador2}'
        
        # Verificando se o CPF calculado corresponde ao CPF de entrada
        if cpf_formatado == cpf_verificado:
            print('CPF válido')
            break
        else:
            print('CPF não válido. Verifique se o número digitado está correto e tente novamente.')
