import asyncio
import datetime
import json
from functools import partial

import pywebio.input as inp
from core.config import project_settings
from pywebio.output import *
from pywebio.session import run_js


class TaskHandler:
    def __init__(self):
        self.__coins = list(self.read_coins_file())

    @staticmethod
    def read_task_file():
        with open(project_settings.TASKS_JSON_PATH, encoding="utf-8") as file:
            return json.load(file)

    def read_coins_file(self):
        with open(project_settings.COINS_JSON_PATH, encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def add_task_to_file(data: dict):
        last_changes = TaskHandler.read_task_file()
        last_changes[data["name"]] = data["price to alert"]
        with open(project_settings.TASKS_JSON_PATH, "w", encoding="utf-8") as file:
            json.dump(last_changes, file, indent=4)

    @staticmethod
    def delete_task_in_file(coin_name, update=True):
        """Deleting a task from JSON"""
        last_changes = TaskHandler.read_task_file()
        try:
            del last_changes[coin_name.lower()]

            with open(project_settings.TASKS_JSON_PATH, "w", encoding="utf-8") as file:
                json.dump(last_changes, file, indent=4)
        except KeyError:
            print("Ключ отсутствует в списке заданий")
        if update:
            run_js("location.reload()")

    @staticmethod
    def get_task_list():
        """Getting a list of active tasks"""
        try:
            clear("list_scope")
        except AssertionError:
            pass
        result = []
        tasks = TaskHandler.read_task_file()

        for name, price in tasks.items():
            result.append(
                [
                    name,
                    price,
                    put_button(
                        f"DELETE {name}",
                        onclick=partial(TaskHandler.delete_task_in_file, name),
                        scope="list_scope",
                    ),
                ]
            )

        put_table(result, header=["Монета", "Триггерная цена", "Действие"], scope="list_scope")

    @staticmethod
    def add_task_validate(data):
        """Form validation for submission"""
        if data is None or data == "":
            return "price", "Необходимо заполнить поле"

    async def add_coin_to_file(self, data: str):
        """Saving a coin in JSON"""
        last_changes = self.read_coins_file()
        if data in last_changes.keys():
            return "Монета уже существует"
        last_changes[data] = {"created_at": str(datetime.datetime.now())}
        with open(project_settings.COINS_JSON_PATH, "w", encoding="utf-8") as file:
            json.dump(last_changes, file, indent=4)
        return "Монета успешно добавлена"

    async def add_coin(self):
        """Adding coins to the list"""
        coin = await inp.input(
            "Введите сокращенное название монеты",
            validate=TaskHandler.add_task_validate,
            scope="input_scope",
        )
        if coin:
            response = await self.add_coin_to_file(coin.upper())
            toast(response)
            await asyncio.sleep(1)
            clear("input_scope")

    async def add_task_in_list(self):
        """Adding a coin tracking task"""
        if self.__coins == []:
            toast("Не создано ни одной монеты для отслеживания")
            await asyncio.sleep(1)
            run_js("location.reload()")
        coin_ticker = await inp.select(
            "Выберите монету", self.__coins, multiple=False, scope="list_scope"
        )
        price = await inp.input(
            "Введите ожидаемую цену", validate=TaskHandler.add_task_validate, scope="list_scope"
        )
        if price:
            toast("Задание успешно создано")
            await asyncio.sleep(1)
            clear("list_scope")
            TaskHandler.add_task_to_file(
                {
                    "name": coin_ticker.lower(),
                    "price to alert": price.replace(
                        ".",
                        "",
                    )
                    .replace(",", "")
                    .lower(),
                }
            )
