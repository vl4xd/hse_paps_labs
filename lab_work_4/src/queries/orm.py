from sqlalchemy import select
from sqlalchemy.orm import joinedload
from database import async_session_factory
from models import * # noqa
from schemas import * # noqa

class AsyncORM:
    @staticmethod
    async def delete_base_tables_data():
        async with async_session_factory() as session:
            try:
                # Получаем все таблицы из метаданных
                tables: list[DeclarativeMeta] = Base.metadata.sorted_tables
                
                # Отключаем проверку внешних ключей
                await session.execute(text("SET session_replication_role = replica;"))
                
                # Удаляем данные из всех таблиц с TRUNCATE
                for table in tables:
                    await session.execute(
                        text(f"TRUNCATE TABLE {table.name} RESTART IDENTITY CASCADE;")
                    )
                
                # Включаем проверку внешних ключей
                await session.execute(text("SET session_replication_role = DEFAULT;"))
                
                await session.commit()
                return {"msg": "Все данные в таблицах успешно удалены"}
            
            except Exception as e:
                await session.rollback()
                raise e
     
          
    @staticmethod
    async def insert_test_data():
        async with async_session_factory() as session:
            zenit = TeamOrm(
                    name="Зенит",
                    town="Санкт-Петербург",
                    stadium="Газпром Арена (Санкт-Петербург)"
                )
            spartak = TeamOrm(
                    name="Спартак М",
                    town="Москва",
                    stadium="Лукойл Арена"
                )
            session.add_all([zenit, spartak])
            await session.flush()
            
        
            season = SeasonOrm(
                    start_date=date(2023, 7, 1),
                    end_date=date(2024, 6, 30)
                )
            session.add(season)
            await session.flush()
            
            
            status_game_active = StatusGameOrm(
                status_game="Активная"
            )
            status_game_future = StatusGameOrm(
                status_game="Будущая"
            )
            status_game_completed = StatusGameOrm(
                status_game="Завершенная"
            )
            session.add_all([status_game_active, 
                             status_game_future, 
                             status_game_completed])
            await session.flush()
            
            
            role_forward = RoleOrm(role="Нападающий")
            role_defender = RoleOrm(role="Защитник")
            role_midfielder = RoleOrm(role="Полузащитник")
            role_gk = RoleOrm(role="Вратарь")
            session.add_all([role_forward,
                             role_defender,
                             role_midfielder,
                             role_gk])
            await session.flush()
            
            
            referee = RefereeOrm(first_name="Виталий",
                                 last_name="Мешков")
            session.add(referee)
            await session.flush()
            
            
            coach_zenit = CoachOrm(first_name="Сергей",
                                     last_name="Семак",
                                     middle_name="Богданович")
            coach_spartak = CoachOrm(first_name="Деян",
                                     last_name="Станкович")
            session.add_all([coach_zenit,
                             coach_spartak])
            await session.flush()
            
            
            goal_type_pen = GoalTypeOrm(goal_type="Пенальти")
            goal_type_reg = GoalTypeOrm(goal_type="Обычный")
            session.add_all([goal_type_pen,
                             goal_type_reg])
            await session.flush()
            
            
            penalty_type_yellow = PenaltyTypeOrm(penalty_type="Желтая карточка")
            session.add(penalty_type_yellow)
            await session.flush()
            
            
            player_s_88 = PlayerOrm(first_name="Илья",
                                    last_name="Свинов")
            player_s_4 =  PlayerOrm(first_name="Алексис",
                                    last_name="Дуарте")
            player_s_14 =  PlayerOrm(first_name="Георгий",
                                    last_name="Джикия")
            player_s_97 =  PlayerOrm(first_name="Даниил",
                                    last_name="Денисов")
            player_s_2 =  PlayerOrm(first_name="Олег",
                                    last_name="Рябчук")
            player_s_35 =  PlayerOrm(first_name="Кристофер",
                                    last_name="Мартинс")
            player_s_8 =  PlayerOrm(first_name="Виктор",
                                    last_name="Мозес")
            player_s_22 =  PlayerOrm(first_name="Михаил",
                                    last_name="Игнатов")
            player_s_7 =  PlayerOrm(first_name="Александр",
                                    last_name="Соболев")
            player_s_10 =  PlayerOrm(first_name="Квинси",
                                    last_name="Промес")
            player_s_19 =  PlayerOrm(first_name="Хесус",
                                    last_name="Медина")
            player_s_47 =  PlayerOrm(first_name="Роман",
                                    last_name="Зобнин")
            player_s_18 =  PlayerOrm(first_name="Наиль",
                                    last_name="Умяров")
            player_s_77 =  PlayerOrm(first_name="Тео",
                                    last_name="Бонгонда")
            player_s_82 =  PlayerOrm(first_name="Даниил",
                                    last_name="Хлусевич")
            player_s_17 =  PlayerOrm(first_name="Антон",
                                    last_name="Зиньковский")
            
            player_z_41 = PlayerOrm(first_name="Михаил", last_name="Кержаков")
            player_z_25 = PlayerOrm(first_name="Страхиня", last_name="Эракович")
            player_z_28 = PlayerOrm(first_name="Нуралы", last_name="Алип")
            player_z_3 = PlayerOrm(first_name="Дуглас", last_name="дос Сантос")
            player_z_6 = PlayerOrm(first_name="Марио", last_name="Фернандес")
            player_z_15 = PlayerOrm(first_name="Вячеслав", last_name="Караваев")
            player_z_11 = PlayerOrm(first_name="Клаудиньо", last_name=None)  
            player_z_8 = PlayerOrm(first_name="Вендел", last_name=None)      
            player_z_5 = PlayerOrm(first_name="Вильмар", last_name="Барриос")
            player_z_31 = PlayerOrm(first_name="Густаво", last_name="Мантуан")
            player_z_33 = PlayerOrm(first_name="Иван", last_name="Сергеев")
            player_z_30 = PlayerOrm(first_name="Матео", last_name="Кассьерра")
            player_z_19 = PlayerOrm(first_name="Алексей", last_name="Сутормин")
            player_z_79 = PlayerOrm(first_name="Дмитрий", last_name="Васильев")
            player_z_21 = PlayerOrm(first_name="Александр", last_name="Ерохин")
            player_z_37 = PlayerOrm(first_name="Эдуардо", last_name="Кейрос")
            session.add_all([
                            player_s_88,
                            player_s_4,
                            player_s_14,
                            player_s_97,
                            player_s_2,
                            player_s_35,
                            player_s_8,
                            player_s_22,
                            player_s_7,
                            player_s_10,
                            player_s_19,
                            player_s_47,
                            player_s_18,
                            player_s_77,
                            player_s_82,
                            player_s_17,
                            player_z_41,
                            player_z_25,
                            player_z_28,
                            player_z_3,
                            player_z_6,
                            player_z_15,
                            player_z_11,
                            player_z_8,
                            player_z_5,
                            player_z_31,
                            player_z_33,
                            player_z_30,
                            player_z_19,
                            player_z_79,
                            player_z_21,
                            player_z_37
                        ])
            await session.flush()
            
            
            calendar = CalendarOrm(
                left_team_id=spartak.team_id,
                right_team_id=zenit.team_id,
                status_game_id=status_game_completed.status_game_id,
                tour=1,
                start_at=datetime(2023, 8, 20, 19, 30),
                left_team_score=1,
                right_team_score=3,
                created_at=datetime(2023, 8, 20, 19, 30),
                updated_at=datetime(2023, 8, 20, 19, 30),
            )
            session.add(calendar)
            await session.flush()
            
            
            coach_game_s = CoachGameOrm(calendar_id=calendar.calendar_id,
                                      coach_id=coach_spartak.coach_id,
                                      team_id=spartak.team_id)
            coach_game_z = CoachGameOrm(calendar_id=calendar.calendar_id,
                                      coach_id=coach_zenit.coach_id,
                                      team_id=zenit.team_id)
            session.add_all([coach_game_s, coach_game_z])
            await session.flush()
            
            
            penalty_1 = PenaltyGameOrm(
                calendar_id=calendar.calendar_id,
                team_id=spartak.team_id,
                player_id=player_s_7.player_id,
                penalty_type_id=penalty_type_yellow.penalty_type_id,
                minute=10,
            )
            penalty_2 = PenaltyGameOrm(
                calendar_id=calendar.calendar_id,
                team_id=zenit.team_id,
                player_id=player_z_30.player_id,
                penalty_type_id=penalty_type_yellow.penalty_type_id,
                minute=96,
            )
            session.add_all([penalty_1, penalty_2])
            await session.flush()
            
            
            referee_game = RefereeGameOrm(
                calendar_id=calendar.calendar_id,
                referee_id=referee.referee_id
            )
            session.add(referee_game)
            await session.flush()
            
            
            player_s_88_stat = PlayerStatOrm(
                player_id=player_s_88.player_id,
                role_id=role_gk.role_id,
                growth=193,
                weight=79,
                transfer_value=600000,
                created_at=datetime(2023, 8, 20, 19, 30),
            )
            session.add(player_s_88_stat)
            await session.flush()
            
            
            try:
                await session.commit()
                return {"msg": "Тестовые данные занесены в таблицы"}
            except Exception as e:
                await session.rollback()
                raise e
    
    
    @staticmethod
    async def select_players_with_joined_playerstat():
        async with async_session_factory() as session:
            query = (
                select(PlayerOrm)
                .options(joinedload(PlayerOrm.player_stat)
                         .joinedload(PlayerStatOrm.role))
            )
            res = await session.execute(query)
            result_orm = res.unique().scalars().all()
            result_dto = [PlayerRelPlayerStatDTO.model_validate(row, from_attributes=True) for row in result_orm]
            return result_dto
        
    
    @staticmethod
    async def select_players():
        async with async_session_factory() as session:
            query = (
                select(PlayerOrm)
            )
            res = await session.execute(query)
            result_orm = res.scalars().all()
            result_dto = [PlayerDTO.model_validate(row, from_attributes=True) for row in result_orm]
            return result_dto
        
    @staticmethod
    async def select_player(player_id: int):
        async with async_session_factory() as session:
            query = (
                select(PlayerOrm)
                .where(PlayerOrm.player_id==player_id)
            )
            res = await session.execute(query)
            result_orm = res.scalars().one_or_none()
            if not result_orm:
                return None
            result_dto = PlayerDTO.model_validate(result_orm, from_attributes=True)
            return result_dto
        
    @staticmethod
    async def select_player_stats(player_id: int):
        async with async_session_factory() as session:
            query = (
                select(PlayerOrm)
                .where(PlayerOrm.player_id==player_id)
            )
            res = await session.execute(query)
            result_orm = res.scalars().one_or_none()
            if not result_orm:
                return None
            
            query = (
                select(PlayerStatOrm)
                .where(PlayerStatOrm.player_id==player_id)
            )
            res = await session.execute(query)
            result_orm = res.scalars().all()
            result_dto = [PlayerStatDTO.model_validate(row, from_attributes=True) for row in result_orm]
            return result_dto
        
    @staticmethod
    async def insert_player_stat(player_stat: PlayerStatAddDTO):
        async with async_session_factory() as session:
            data_orm = PlayerStatOrm(
                                    player_id=player_stat.player_id,
                                    role_id=player_stat.role_id,
                                    growth=player_stat.growth,
                                    weight=player_stat.weight,
                                    transfer_value=player_stat.transfer_value,
                                    created_at=player_stat.created_at)
            session.add(data_orm)
            try:
                await session.commit()
                return {"msg": f"Запись успешно добавлена"}
            except Exception as e:
                await session.rollback()
                raise e
            
    @staticmethod
    async def select_calendars():
        async with async_session_factory() as session:
            query = (
                select(CalendarOrm)
                .options(joinedload(CalendarOrm.right_team))
                .options(joinedload(CalendarOrm.left_team))
                .options(joinedload(CalendarOrm.status_game))
            )
            res = await session.execute(query)
            result_orm = res.unique().scalars().all()
            result_dto = [CalendarRelDTO.model_validate(row, from_attributes=True) for row in result_orm]
            return result_dto
        
    @staticmethod
    async def select_calendar_coaches(calendar_id: int):
        async with async_session_factory() as session:
            query = (
                select(CalendarOrm)
                .where(CalendarOrm.calendar_id==calendar_id)
            )
            res = await session.execute(query)
            result_orm = res.scalars().one_or_none()
            if not result_orm:
                return None
            query = (
                select(CoachGameOrm)
                .options(joinedload(CoachGameOrm.team))
                .options(joinedload(CoachGameOrm.coach))
                .where(CoachGameOrm.calendar_id==calendar_id)
            )
            res = await session.execute(query)
            result_orm = res.unique().scalars().all()
            result_dto = [CoachGameRelDTO.model_validate(row, from_attributes=True) for row in result_orm]
            return result_dto
        
    @staticmethod
    async def insert_player(new_player: PlayerAddDTO):
        async with async_session_factory() as session:
            data_orm = PlayerOrm(
                first_name=new_player.first_name,
                last_name=new_player.last_name
            )
            is_exist = await session.execute(
                                  select(PlayerOrm)
                                  .where(
                                      PlayerOrm.first_name==new_player.first_name,
                                      PlayerOrm.last_name==new_player.last_name
                                  ))
            if is_exist.scalar_one_or_none():
                return None
                        
            session.add(data_orm)
            try:
                await session.commit()
                return {"msg": f"Игрок успешно добавлен"}
            except Exception as e:
                await session.rollback()
                raise e
            
    @staticmethod
    async def insert_calendar(new_calendar: CalendarAddDTO):
        async with async_session_factory() as session:
            data_orm = CalendarOrm(
                left_team_id=new_calendar.left_team_id,
                right_team_id=new_calendar.right_team_id,
                status_game_id=new_calendar.status_game_id,
                tour=new_calendar.tour,
                start_at=new_calendar.start_at,
                left_team_score=new_calendar.left_team_score,
                right_team_score=new_calendar.right_team_score,
                created_at=new_calendar.created_at,
                updated_at=new_calendar.updated_at,
            )
            session.add(data_orm)
            try:
                await session.commit()
                return {"msg": f"Игра успешно добавлена"}
            except Exception as e:
                await session.rollback()
                raise e
            
    @staticmethod
    async def insert_coach(new_coach: CoachAddDTO):
        async with async_session_factory() as session:
            data_orm = CoachOrm(
                first_name=new_coach.first_name,
                last_name=new_coach.last_name,
                middle_name=new_coach.middle_name
            )
            is_exist = await session.execute(
                                  select(CoachOrm)
                                  .where(
                                      CoachOrm.first_name==new_coach.first_name,
                                      CoachOrm.last_name==new_coach.last_name,
                                      CoachOrm.middle_name==new_coach.middle_name
                                  ))
            if is_exist.scalar_one_or_none():
                return None
                        
            session.add(data_orm)
            try:
                await session.commit()
                return {"msg": f"Тренер успешно добавлен"}
            except Exception as e:
                await session.rollback()
                raise e
    @staticmethod
    async def change_calendar_status(calendar_id: int, new_calendar_status: CalendarChgStatusDTO):
        async with async_session_factory() as session:
            past_calendar = is_exist = await session.execute(
                select(CalendarOrm)
                .where(
                    CalendarOrm.calendar_id==calendar_id
                )
            )
            caledar_orm = past_calendar.scalar_one_or_none()
            if not caledar_orm:
                return None
            
            caledar_orm.status_game_id = new_calendar_status.status_game_id
            
            try:
                await session.commit()
                await session.refresh(caledar_orm)
                return {"msg":"Каледарь успешно обновлен"}
            except Exception as e:
                await session.rollback()
                return None
            
    @staticmethod
    async def delete_calendar(calendar_id: int):
        async with async_session_factory() as session:
            # удаляем зависимую запись PK в CoachGameOrm, PenaltyGameOrm, GoalGameOrm
            # добавить 1 pk и убрать пк с calendar_id в вышеописанных таблицах
            # (необходимо изменить для правильно работы каскадного удаления)
            '''
            del_coaches = await session.execute(
                select(CoachGameOrm)
                .where(
                    CoachGameOrm.calendar_id==calendar_id
                )
            )
            coach_orm = del_coaches.scalars().all()
            if coach_orm:
                try:
                    for c in coach_orm:
                        await session.delete(c)
                    await session.commit()
                except Exception as e:
                    raise e
            '''
                    
            del_calendar = await session.execute(
                select(CalendarOrm)
                .where(
                    CalendarOrm.calendar_id==calendar_id
                )
            )
            
            
            caledar_orm = del_calendar.scalar_one_or_none()
            if not caledar_orm:
                return None
            
            try:
                
                await session.delete(caledar_orm)
                await session.commit()
                return {"msg":"Каледарь успешно удален"}
            except Exception as e:
                print(f"Ошибка {str(e)}")
                await session.rollback()
                return None
            
        