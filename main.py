import logging
import random
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Insira seu token aqui
TELEGRAM_TOKEN = "COLOQUE_SEU_TOKEN_AQUI"

# Configurar o logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Função para gerar CEP válido e buscar endereço
async def gerar_cep(update: Update, context: ContextTypes.DEFAULT_TYPE):
    while True:
        cep_aleatorio = "".join([str(random.randint(0, 9)) for _ in range(8)])
        url = f"https://viacep.com.br/ws/{cep_aleatorio}/json/"

        try:
            response = requests.get(url, timeout=5)
            data = response.json()

            if "erro" not in data:
                endereco = (
                    f"📍 CEP Gerado: {data['cep']}
"
                    f"Logradouro: {data['logradouro']}
"
                    f"Bairro: {data['bairro']}
"
                    f"Cidade: {data['localidade']} - {data['uf']}"
                )
                await update.message.reply_text(endereco)
                break
        except Exception as e:
            logging.error(f"Erro ao consultar CEP: {e}")
            await update.message.reply_text("❌ Erro ao consultar o ViaCEP. Tente novamente mais tarde.")
            break

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("gerarcep", gerar_cep))

    print("Bot rodando...")
    app.run_polling()
