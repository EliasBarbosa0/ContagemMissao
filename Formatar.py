from datetime import datetime

def fn(numero):
    # Converte o número para um inteiro (remove casas decimais)
    numero_inteiro = int(round(numero,0))
    
    # Converte o número para string e formata com separador de milhar
    numero_formatado = f'{numero_inteiro:,}'.replace(',', '.')
    
    return numero_formatado


def dh(data_hora):
    # Verifica se data_hora é uma string e converte para datetime se necessário
    if isinstance(data_hora, str):
        data_hora = datetime.fromisoformat(data_hora)
    
    # Formata a data e hora no formato brasileiro
    data_hora_formatada = data_hora.strftime('%d/%m/%Y %H:%M')
    
    return data_hora_formatada

def dt(data_hora):
    # Verifica se data_hora é uma string e converte para datetime se necessário
    if isinstance(data_hora, str):
        data_hora = datetime.fromisoformat(data_hora)
    
    # Formata a data e hora no formato brasileiro
    data_hora_formatada = data_hora.strftime('%d/%m/%Y')
    
    return data_hora_formatada

def fd(numero):
    # Converte o número para um inteiro (remove casas decimais)
    numero_inteiro = round(numero,2)
    
    # Converte o número para string e formata com separador de milhar
    numero_formatado = f'{numero_inteiro:,}'.replace('.', ',')
    
    return numero_formatado