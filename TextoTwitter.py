from DaxQuery import execute_dax_query
from Formatar import fn
from Formatar import dh
from Formatar import dt
from Formatar import fd

def corpo():

    valor = execute_dax_query()

    Recorde = ''

    if valor[11] > valor[10]:
        Recorde = f'🚨 Recorde 🚨\n\n'

    texto = (
        f'{Recorde}'
        f'⌚️ Hora da atualização: {dh(valor[7])}\n'
        f'🚀 Validados: {fn(valor[0])} ({ fd(valor[0] / valor[1] * 100 )}%)\n'
        f'🎯 Necessários: {fn(valor[1])}\n'
        f'🗓️ Projeção da conclusão: {dt(valor[6])}\n'
        f'📈 Média diária: {fn(valor[9])}\n'
        f'✅ Estados que atingiram o mínimo: {valor[5]}\n\n'
        f'🌐 Relatório completo: https://bit.ly/4fjX8Zy\n\n'
        f'@PartidoMissao\n'
    )

    return texto