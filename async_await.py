import asyncio


async def print_nums():
    num = 1
    while num < 1000:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while count < 1000:
        if count % 3 == 0:
            print(f'{count} seconds have passed')
        count += 1
        await asyncio.sleep(1)


@asyncio.coroutine
def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.ensure_future(print_time())

    yield from asyncio.gather(task1, task2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
