import os
import signal
import threading

from handlers.menu import TaskHandler
from handlers.parser import check_coins_balance
from pywebio import *
from pywebio.input import *
from pywebio.output import *


@config(theme="dark")
async def main():
    clear()
    threading.Thread(target=check_coins_balance).start()
    with use_scope("main_scope"):
        logo_path = os.path.join("data", "logo.jpeg")
        put_image(open(logo_path, "rb").read())
        task = TaskHandler()

        put_buttons(
            ["Отслеживать монету", "Добавить монету", "Список задач"],
            onclick=[task.add_task_in_list, task.add_coin, task.get_task_list],
        )

    # page scopes initialization
    with use_scope("list_scope"):
        pass

    with use_scope("input_scope"):
        pass


if __name__ == "__main__":

    def close_server():
        stop_server(task)

    task = start_server(main, host="0.0.0.0", port=4444, on_close=close_server)

    signal.signal(signal.SIGINT, close_server)
    signal.signal(signal.SIGTERM, close_server)
    print("Сервер запущен.")
    task.wait_closed()
