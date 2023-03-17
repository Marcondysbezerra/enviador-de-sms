from twilio.rest import Client
import pandas as pd


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'SID'
auth_token = 'TOKEN'
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        message = client.messages \
                        .create(
                             body=f"Você {vendedor} bateu a meta de vendas {vendas} no mês de {mes} e foi contemplado com R$10.000,00.",
                             from_='+15673613184_NÚMERO_DA_PLATAFORMA_TWILIO',
                             to='+5570_NÚMERO_DO_DESTINATÁRIO'
                         )

        print(message.sid)
