import asyncio
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from fastapi import FastAPI, status, HTTPException
import uvicorn
from queries.orm import AsyncORM
from schemas import * # noqa


app = FastAPI()


@app.delete(path="/delete_base_tables_data", tags=["Тестовые записи БД"])
async def delete_base_tables_data():
    try:
        return await AsyncORM.delete_base_tables_data()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    

@app.post(path="/insert_test_data", tags=["Тестовые записи БД"])
async def insert_test_data():
    try:
        return await AsyncORM.insert_test_data()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    

@app.get(path="/players", tags=["Игроки"])
async def select_players():
    try:
        res = await AsyncORM.select_players()
        return res
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
        

@app.get(path="/players/{player_id}", tags=["Игроки"])
async def select_player(player_id: int):
    res = await AsyncORM.select_player(player_id)
    if not res:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Элемент не найден"
        )
    return res


@app.get(path="/players/{player_id}/stats", tags=["Статистика игроков"]) 
async def select_player_stats(player_id: int):
    res = await AsyncORM.select_player_stats(player_id)
    if res is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Элемент не найден"
        )
    return res

@app.post(path="/players/{player_id}/stats", tags=["Статистика игроков"]) 
async def create_stat(data: PlayerStatAddDTO):
    try:
        return await AsyncORM.insert_player_stat(data)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@app.get(path="/all_players_with_stats", tags=["Статистика игроков"])
async def players_with_stats():
    try:
        return await AsyncORM.select_players_with_joined_playerstat()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.get(path="/calendars", tags=["Календарь игр"])
async def select_calendars():
    try:
        return await AsyncORM.select_calendars()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
        
@app.get(path="/calendars/{calendar_id}/coaches", tags=["Тренеры"])
async def select_calendar_coaches(calendar_id: int):
    res = await AsyncORM.select_calendar_coaches(calendar_id)
    if res is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Элемент не найден"
        )
    return res


@app.post(path="/players", tags=["Игроки"])
async def insert_player(data: PlayerAddDTO):
    res = await AsyncORM.insert_player(data)
    if res is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Игрок с таким именем и фамилией уже существует"
        )
    return {"msg":"Игрок успешно добавлен"}

@app.post(path="/calendars", tags=["Календарь игр"])
async def insert_calendar(data: CalendarAddDTO):
    try:
        return await AsyncORM.insert_calendar(data)
    except Exception as e:
        return {"errror": f"{str(e)}"}
    
@app.post(path="/coaches", tags=["Тренеры"])
async def insert_coach(data: CoachAddDTO):
    res = await AsyncORM.insert_player(data)
    if res is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Тренер с таким ФИО уже существует"
        )
    return {"msg":"Тренер успешно добавлен"}

@app.put(path="/calendars/{calendar_id}", tags=["Календарь игр"])
async def change_calendar_status(calendar_id: int, new_calendar_status: CalendarChgStatusDTO):
    res = await AsyncORM.change_calendar_status(calendar_id, new_calendar_status)
    if res is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Элемент не найден"
        )
    return res

@app.delete(path="/calendars/{calendar_id}", tags=["Календарь игр"])
async def delete_calendar(calendar_id: int):
    res = await AsyncORM.delete_calendar(calendar_id)
    if res is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Элемент не найден"
        )
    return res
    

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)        
