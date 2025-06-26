# Bot Telegram Gerador de CEPs Brasileiros (Render Ready)

## Função
Gera CEPs brasileiros aleatórios e válidos, consultando endereço real via ViaCEP.

## Como usar no Render:
1. Crie um novo serviço **"Web Service"** no Render.
2. Conecte este projeto (após subir no GitHub ou enviar o ZIP).
3. No Render, configure a build para **Python 3.10 ou superior**.
4. Edite o `main.py` e insira seu TOKEN do BotFather:

```
TELEGRAM_TOKEN = "SEU_TOKEN_AQUI"
```

5. Deploy e pronto!

## Requisitos:
- python-telegram-bot==20.3
- requests==2.31.0

## Comando disponível:
/gerarcep
