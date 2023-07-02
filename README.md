
# CryptoTracker
![top-language](https://img.shields.io/github/languages/top/dimitrieidifesk/CryptoTracker)

![watchers](https://img.shields.io/github/watchers/dimitrieidifesk/CryptoTracker?style=social)
![forks](https://img.shields.io/github/forks/dimitrieidifesk/CryptoTracker?style=social)
![start](https://img.shields.io/github/stars/dimitrieidifesk/CryptoTracker?style=social)

CryptoTracker is a Python script with a user-friendly web interface that parses cryptocurrency data from a cryptocurrency exchange and sends notifications to Telegram when the price of a selected currency reaches a specified threshold or falls below it.
The script helps traders to buy cryptocurrency at a low price in a timely manner.

CryptoTracker - это Python скрипт с удобным web-интерфейсом, который парсит данные о криптовалюте с криптобиржи и отправляет уведомления в Telegram, когда цена на выбранную валюту достигает заданного порога или опускается ниже.
Скрипт помогает трейдерам вовремя покупать криптовалюту, пока не неё низкая цена.
## Installation

1. Clone the repository on your computer:
   
       git clone https://github.com/ваш-пользователь/CryptoTracker.git
     
3. Install all dependencies using `pip`:
      
       pip install -r requirements.txt

4. Make sure you have a Telegram account and create a bot following the official instructions [Telegram Bot API](https://core.telegram.org/bots#creating-a-new-bot).

5. Change the file `config.env.example` to `config.env` by adding the following variables:
      
       TG_BOT_API_KEY=your bot`s api key (get it here @BotFather)
       TG_USER_ID=your user id (get it here @LeadConverterToolkitBot)
   
6. Run the script `run_cryptotracker.sh` or:

       python main.py
   
7. The web interface for setting currencies and prices will be available to you after starting the application. Just look at the console and follow the link.

   Веб-интерфейс для настройки валют и цен вам будет доступен после старта приложения. Просто посмотрите в консоль и перейдите по ссылке.

## Interface

![image](https://github.com/dimitrieidifesk/CryptoTracker/assets/123076304/2bcda634-6b92-4dcf-a6b1-a802c33bb8ca)

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact:

- Email: dimitrieidifesk1@yandex.ru
- Telegram: @DenisDDim
