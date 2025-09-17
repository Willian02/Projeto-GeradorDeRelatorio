import os
import datetime

# Verifica e cria o diretório de saída caso não exista.
if os.path.exists("reports") == False:
    os.mkdir("reports")

# Captura a data/hora atual
now_date = datetime.datetime.now()
# Nome do arquivo com timestamp: YYYY-MM-DD_HH-MM-SS.txt
file_name = f"{now_date.strftime("%Y-%m-%d_%H-%M-%S")}.txt"
report_path = os.path.join("reports", file_name)

# Conteúdo do relatório: data/hora legível
report_content = f"Relatório feito em {now_date.strftime("%d/%m/%Y %H:%M:%S")}" 

with open(report_path, "w") as file:
    # Escreve o conteúdo no arquivo
    file.write(report_content)

print("Relatório gerado com sucesso!")