import asyncio

async def cook_eggs():
    print("Начинаем варить яйца")
    await asyncio.sleep(2)  # Симулируем время приготовления
    print("Яйца готовы")

async def fry_bacon():
    print("Начинаем жарить бекон")
    await asyncio.sleep(3)  # Симулируем время приготовления
    print("Бекон готов")

async def main():
    await asyncio.gather(cook_eggs(), fry_bacon())

asyncio.run(main())