# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

from dados import produtos

import copy

novo_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1,2)}
    for p in copy.deepcopy(produtos)
    ]

produtos_ordenados_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

produtos_ordenados_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
)



print(*produtos, sep='\n')
print()
print(*novo_produtos, sep='\n')
print()
print(*produtos_ordenados_nome, sep='\n')
print()
print(*produtos_ordenados_preco, sep='\n')