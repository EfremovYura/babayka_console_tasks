"""
Реализовать функцию, которая замеряет время на исполнение 100 запросов к адресу: http://httpbin.org/delay/3.
Запросы должны выполняться асинхронно. Допускается написание вспомогательных функций и использование сторонних
библиотек. Результат замера времени выводит в консоль. Ожидаемое время не должно превышать 10 секунд.
"""

import asyncio
import aiohttp
from time import time

URL = "http://httpbin.org/delay/3"
N = 100


async def async_gather_http_get(url: str, times: int):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(times):
            tasks.append(asyncio.create_task(session.get(url)))

        responses = await asyncio.gather(*tasks)
        return [response.status for response in responses]


def run_async_http_get(func=async_gather_http_get, url: str = URL, times: int = N):
    start = time()

    result = asyncio.run(func(url, times))

    task_time = time() - start

    print(f"Время выполнения {func.__name__}: {task_time} сек.")

    return result
