import requests
from datetime import datetime, timedelta
import os
import zipfile
import pandas as pd

# Obter a data de D-1 (ontem)
d1 = datetime.now() - timedelta(days=1)
d1_str = d1.strftime('%Y-%m-%d')  # Formato: 2024-10-04

# Montar a URL de download
download_url = f'https://arquivos.b3.com.br/rapinegocios/tickercsv/{d1_str}'

# Definir o diretório onde o arquivo será salvo
diretorio_destino = 'C:/Users/augus/OneDrive/FIAP/Fase_2/tech_challenge_2/data'  # Substitua pelo caminho da pasta onde deseja salvar o arquivo

# Verificar se o diretório existe, se não, criar
if not os.path.exists(diretorio_destino):
    os.makedirs(diretorio_destino)

# Nome do arquivo ZIP a ser salvo
zip_file_name = f'cotacoes_b3_d1_{d1_str}.zip'
caminho_zip = os.path.join(diretorio_destino, zip_file_name)

# Fazer a requisição GET para o link de download
response = requests.get(download_url)

# Verificar se o download foi bem-sucedido
if response.status_code == 200:
    # Salvar o arquivo ZIP no diretório especificado
    with open(caminho_zip, 'wb') as file:
        file.write(response.content)
    print(f"Arquivo ZIP baixado com sucesso: {caminho_zip}")

    # Descompactar o arquivo ZIP
    with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
        zip_ref.extractall(diretorio_destino)
    print(f"Arquivo descompactado com sucesso no diretório: {diretorio_destino}")

    # Apagar o arquivo ZIP
    os.remove(caminho_zip)
    print(f"Arquivo ZIP apagado: {caminho_zip}")

    # Exibir o nome dos arquivos extraídos
    arquivos_extraidos = os.listdir(diretorio_destino)
    for arquivo in arquivos_extraidos:
        if arquivo.endswith('.txt'):
            print(f"Arquivo TXT extraído: {arquivo}")
            
            # Caminho completo do arquivo TXT extraído
            caminho_txt = os.path.join(diretorio_destino, arquivo)

            # Ler o arquivo TXT em um DataFrame pandas
            #df = pd.read_csv(caminho_txt, delimiter=';', encoding='ISO-8859-1')

            # Nome do arquivo Parquet
            parquet_file_name = f'NEGOCIOSAVISTA_{d1_str}.parquet'
            caminho_parquet = os.path.join(diretorio_destino, parquet_file_name)

            # Salvar o DataFrame em formato Parquet
            #df.to_parquet(caminho_parquet, engine='pyarrow', index=False)
            print(f"Arquivo Parquet salvo com sucesso: {caminho_parquet}")
else:
    print(f"Arquivo de D-1 não encontrado. Tentando D-2...")

    # Tentar D-2 caso D-1 não esteja disponível
    d2 = datetime.now() - timedelta(days=2)
    d2_str = d2.strftime('%Y-%m-%d')
    download_url_d2 = f'https://arquivos.b3.com.br/rapinegocios/tickercsv/{d2_str}'
    
    response_d2 = requests.get(download_url_d2)
    if response_d2.status_code == 200:
        zip_file_name_d2 = f'cotacoes_b3_d2_{d2_str}.zip'
        caminho_zip_d2 = os.path.join(diretorio_destino, zip_file_name_d2)
        
        with open(caminho_zip_d2, 'wb') as file:
            file.write(response_d2.content)
        print(f"Arquivo ZIP de D-2 baixado com sucesso: {caminho_zip_d2}")
        
        # Descompactar o arquivo ZIP de D-2
        with zipfile.ZipFile(caminho_zip_d2, 'r') as zip_ref:
            zip_ref.extractall(diretorio_destino)
        print(f"Arquivo de D-2 descompactado com sucesso no diretório: {diretorio_destino}")

        # Apagar o arquivo ZIP de D-2
        os.remove(caminho_zip_d2)
        print(f"Arquivo ZIP de D-2 apagado: {caminho_zip_d2}")

        # Exibir o nome dos arquivos extraídos
        arquivos_extraidos = os.listdir(diretorio_destino)
        for arquivo in arquivos_extraidos:
            if arquivo.endswith('.txt'):
                print(f"Arquivo TXT de D-2 extraído: {arquivo}")
                
                # Caminho completo do arquivo TXT extraído
                caminho_txt_d2 = os.path.join(diretorio_destino, arquivo)

                # Ler o arquivo TXT em um DataFrame pandas
                #df_d2 = pd.read_csv(caminho_txt_d2, delimiter=';', encoding='ISO-8859-1')

                # Nome do arquivo Parquet
                parquet_file_name_d2 = f'NEGOCIOSAVISTA_{d2_str}.parquet'
                caminho_parquet_d2 = os.path.join(diretorio_destino, parquet_file_name_d2)

                # Salvar o DataFrame em formato Parquet
                #df_d2.to_parquet(caminho_parquet_d2, engine='pyarrow', index=False)
                print(f"Arquivo Parquet de D-2 salvo com sucesso: {caminho_parquet_d2}")
    else:
        print(f"Erro ao fazer o download do arquivo de D-2: {response_d2.status_code}")