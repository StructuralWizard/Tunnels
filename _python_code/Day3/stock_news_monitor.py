from dotenv import load_dotenv
import requests, os


# Cargar variables de entorno desde el archivo .env
load_dotenv()

# # Precio de las acciones
# stock_params = {"symbol": "AAPL", "apikey": os.getenv("ALPHA_API_KEY")}
# stock_response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY", params=stock_params)
# data = stock_response.json()
# yesterday = list(data["Time Series (Daily)"].keys())[0]
# # print(f"Fecha de ayer: {yesterday}")
# # today = list(data["Time Series (Daily)"].keys())[1]
# # print(f"Fecha de hoy: {today}")
# price = float(data["Time Series (Daily)"][yesterday]["4. close"])
# print(f"Precio de cierre de AAPL ayer {yesterday}: ${price}")

# API de noticias
import finnhub
import datetime

# Obtener fechas
today = datetime.datetime.now().strftime('%Y-%m-%d')
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

# Configurar cliente
finnhub_client = finnhub.Client(api_key=os.environ.get("FINNHUB_API_KEY"))
# Noticias de la empresa
# Es necesario usar _from en lugar de from para evitar conflictos
latest_news = finnhub_client.company_news('AAPL', _from=yesterday, to=today)
print(f"Últimas noticias de AAPL desde {yesterday} hasta {today}:")

for news in latest_news[:5]:
    print(f"Título: {news['headline']}")
    print(f"Fuente: {news['source']}")
    print(f"Fecha: {news['datetime']}")
    print(f"Resumen: {news['summary']}")
    print("-" * 50)

# Enviar mensaje a través de Twilio WhatsApp
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token =  os.environ.get('TWILIO_AUTH_TOKEN')
print("SID de la cuenta de Twilio:", account_sid)
print("Token de autenticación de Twilio:", auth_token)
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    #content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e', # Su cita es el {1} a las {2}
    #content_variables='{"1":"12/1","2":"3pm"}',
    #content_sid='HX350d429d32e64a552466cafecbe95f3c', # Gracias por su pedido. Su entrega está programada para el {1} a las {2}
    #content_variables='{"1":"12/1","2":"3pm"}',
    #content_sid='HX229f5a04fd0510ce1b071852155d3e75', # {1} es su código de verificación. Por su seguridad, no comparta este código.
    #content_variables='{"1":"409173"}',    
    content_sid='HX38f4a38e390bfec8bfe8760c5d013619', # Precio de cierre de TSLA: ${{1}}
    content_variables=f'{{"1":"{price}"}}',
    to='whatsapp:+447818912097'
)

print(message.sid)