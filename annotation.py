from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    db_host: str       # URL-адрес базы данных
    db_user: str       # Username пользователя базы данных
    db_password: str   # Пароль к базе данных
    database: str      # Название базы данных


@dataclass
class TgBot:
    token: str             # Токен для доступа к телеграм-боту
    admin_ids: list[int]   # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig

config = Config(
    tg_bot=TgBot(token=BOT_TOKEN, admin_ids=ADMIN_IDS),
    db=DatabaseConfig(
        db_host=DB_HOST,
        db_user=DB_USER,
        db_password=DB_PASSWORD,
        database=DATABASE
    )
)
#получить токен бота:
token = config.tg_bot.token

#получить пароль к базе данных:
db_passw = config.db.db_password





def say_something(number: int, word: str) -> str:
    word = word.capitalize()
    return word * number

# forexample
# first_var  : int        = 5
# second_var : str        = 'second_var'
# third_var  : list       = []
# fourth_var : float
# fifth_var  : dict
# sixth_var  : tuple[int] = (1, 2)

# def get_something_1(arg_1: int, arg_2: list[int], arg_3: str = '') -> str:
#     pass

# def get_something_2(arg_1: tuple[int, bool]) -> None:
#     pass