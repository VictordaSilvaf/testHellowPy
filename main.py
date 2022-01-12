from datetime import datetime
from pytz import timezone

def criarDataAtual():
    data_e_hora_atuais = datetime.now()
    fuso_horario = timezone('America/Sao_Paulo')
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

    arquivo = open("dataAtual.txt", "a")
    arquivo.write(str(data_e_hora_sao_paulo_em_texto))
    arquivo.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    criarDataAtual()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
