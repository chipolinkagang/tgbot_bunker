import asyncio
import datetime
import sys
from typing import List

import sqlalchemy as sa
from aiopg.sa import create_engine
from sqlalchemy import Table, MetaData

if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
metadata = sa.MetaData()

bunker_users = sa.Table('bunker_users', metadata,
                        sa.Column('id', sa.Integer, primary_key=True),
                        sa.Column('name', sa.String(255)),
                        sa.Column('tg_id', sa.String(255)))

async def create_table(engine):
    async with engine.acquire() as conn:
        await conn.execute('DROP TABLE IF EXISTS bunker_users')
        await conn.execute('''CREATE TABLE bunker_users (
                                          id serial PRIMARY KEY,
                                          name varchar(255),
                                          tg_id varchar(255))''')
# проверка на регистрацию
async def reg_check(engine, inp_tg_id: str) -> bool:
    async with engine.acquire() as conn:
        async for row in conn.execute(bunker_users.select().where(bunker_users.c.tg_id == inp_tg_id)):
            return True
# Добавление нового пользователя в users
async def registration(engine, person: dict) -> str:
    async with engine.acquire() as conn:
        await conn.execute(bunker_users.insert().values(name=person['name'], tg_id=person['tg_id']))
        x = 0
        async for row in conn.execute(bunker_users.select().where(bunker_users.c.tg_id == person['tg_id'])):
            if x < row.id:
                x = row.id
        return x


# async def go():
#     async with create_engine(user='postgres',
#                              database='lab1',
#                              host='127.0.0.1',
#                              password='123456') as engine:
#         await create_table(engine)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(go())
