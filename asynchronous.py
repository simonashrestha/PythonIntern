import asyncio

async def first_statement():
    print("First statement executedd")

async def second_statement():
    print("Second statement executedd")

async def third_statement():
    print("Third statement executedd")

async def main():
    await first_statement()
    await second_statement()
    await third_statement()

# Run the main coroutine
asyncio.run(main())
