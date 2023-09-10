senha = input('Digite a sua senha: ')

if not senha:
    print('Digite a senha!')
elif senha == '123':
    print('Senha correta!')
else:
    print('Senha inválida!')