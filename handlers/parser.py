import time

import requests
from bs4 import BeautifulSoup
from core.config import project_settings
from handlers.menu import TaskHandler
from handlers.telegram import send_notify


def get_crypto_rank(coins):
    result = {}
    html_resp = requests.get(project_settings.SERVICE_URL + "/ru").text
    block = BeautifulSoup(html_resp, "lxml")
    rows = block.find_all("tr", class_="table__row--full-width")

    for row in rows:
        ticker = row.find("span", class_="profile__subtitle-name")
        h24_stat = row.find("div", class_="change--positive")
        full_name = row.find("a", class_="profile__link")
        if ticker:
            ticker = ticker.text.strip().lower()
            result[ticker.lower()] = {}
            if h24_stat:
                h24_stat = h24_stat.text.strip().lower()
                result[ticker.lower()]["stat"] = h24_stat
            result[ticker.lower()]["full_name"] = full_name.text.strip()
            result[ticker.lower()]["href"] = full_name.get("href")

            if ticker in coins:
                price = row.find("td", class_="table__cell--responsive")
                if price:
                    price = float(
                        price.find("div", class_="valuta--light")
                        .text.replace("$", "")
                        .replace(",", ".")
                        .replace(" ", "")
                        .replace("\n", "")
                        .replace("\xa0", "")
                    )
                result[ticker.lower()]["price"] = price
    return result


def check_coins_balance():
    while True:
        coins = TaskHandler.read_task_file()
        coin_dict = get_crypto_rank(coins.keys())

        for name, price in coins.items():
            if name in coin_dict:
                if coin_dict[name]["price"] <= int(price):
                    message = (
                        f"[{name.upper()}] - {coin_dict[name]['full_name']}\n"
                        f"Price: {coin_dict[name]['price']}$\nLast 24h: {coin_dict[name]['stat']}\n"
                        f"Coin profile: {project_settings.SERVICE_URL}{coin_dict[name]['href']}"
                    )
                    send_notify(message)
                    TaskHandler.delete_task_in_file(name.upper(), update=False)

        time.sleep(20)
