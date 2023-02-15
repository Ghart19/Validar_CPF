# Validar_CPF
Este é um código Python que solicita que o usuário insira seu CPF, verifica se a entrada é válida e calcula os dígitos de verificação do CPF. Em seguida, compara os dígitos de verificação calculados com os dígitos de verificação no CPF de entrada e informa se o CPF é válido ou inválido.

O código começa inicializando algumas variáveis, incluindo uma lista vazia chamada "cpf_digitado" para armazenar o CPF digitado pelo usuário, duas variáveis para as somas parciais dos dígitos de verificação e dois multiplicadores (10 e 11) para calcular os dígitos de verificação.

O código utiliza um loop "while True" que solicita que o usuário digite seu CPF sem pontos ou traços e verifica se a entrada é numérica e tem exatamente 11 caracteres. Se a entrada não for válida, o código informa o usuário do erro e solicita que ele tente novamente. Se a entrada for válida, o código adiciona o CPF à lista "cpf_digitado", calcula os dígitos de verificação e compara os dígitos de verificação calculados com os dígitos de verificação no CPF de entrada.

O primeiro dígito de verificação é calculado somando-se o produto de cada um dos nove primeiros dígitos do CPF pelo seu respectivo multiplicador (começando em 10 e diminuindo para 2). O resultado dessa soma é dividido por 11, e o dígito de verificação é o resto da divisão. Se o resto da divisão for maior ou igual a 10, o dígito de verificação é definido como 0.

O segundo dígito de verificação é calculado de maneira semelhante, exceto que o cálculo é feito usando os dez primeiros dígitos do CPF (incluindo o primeiro dígito de verificação calculado anteriormente).

Depois que os dígitos de verificação são calculados, o código extrai as partes do CPF original que são dígitos e compara essas partes com o CPF calculado para determinar se o CPF é válido. Se o CPF calculado corresponder ao CPF de entrada, o código informa ao usuário que o CPF é válido e sai do loop "while True". Caso contrário, o código informa ao usuário que o CPF é inválido e solicita que ele tente novamente.
