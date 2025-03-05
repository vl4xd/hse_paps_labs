from datetime import date, datetime, timezone
from typing import Annotated
from sqlalchemy import ForeignKey, Index, CheckConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeMeta

from database import Base, str_25, str_100


intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class TeamOrm(Base):
    __tablename__ = "team"
    
    team_id: Mapped[intpk]
    name: Mapped[str_100]
    town: Mapped[str_100 | None]
    stadium: Mapped[str_100 | None]
    
    __table_args__ = (
        Index("name_index", "name"),
    )
    
    player_game_stat: Mapped[list["PlayerGameStatOrm"]] = relationship(
        back_populates="team",
    )
    left_calendar: Mapped[list["CalendarOrm"]] = relationship(
        foreign_keys="CalendarOrm.left_team_id",
        back_populates="left_team",
    )
    right_calendar: Mapped[list["CalendarOrm"]] = relationship(
        foreign_keys="CalendarOrm.right_team_id",
        back_populates="right_team",
    )
    standings: Mapped[list["StandingsOrm"]] = relationship(
        back_populates="team",
    )
    player_structure: Mapped[list["PlayerStructreOrm"]] = relationship(
        back_populates="team",
    )
    goal_game: Mapped[list["GoalGameOrm"]] = relationship(
        back_populates="team",
    )
    penalty_game: Mapped[list["PenaltyGameOrm"]] = relationship(
        back_populates="team",
    )
    stat_game: Mapped[list["StatGameOrm"]] = relationship(
        back_populates="team",
    )
    coach_game: Mapped[list["CoachGameOrm"]] = relationship(
        back_populates="team",
    )
    
    


class SeasonOrm(Base):
    __tablename__ = "season"
    
    season_id: Mapped[intpk]
    start_date: Mapped[date]
    end_date: Mapped[date]
    
    __table_args__ = (
        Index("season_time_index", "start_date", "end_date"),
    )
    
    player_game_stat: Mapped[list["PlayerGameStatOrm"]] = relationship(
        back_populates="season",
    )
    standings: Mapped[list["StandingsOrm"]] = relationship(
        back_populates="season",
    )
    
    
    
class PlayerOrm(Base):
    __tablename__ = "player"
    
    player_id: Mapped[intpk] 
    first_name: Mapped[str_100]
    last_name: Mapped[str_100 | None]
    
    player_stat: Mapped[list["PlayerStatOrm"]] = relationship(
        back_populates="player",
    )
    player_game_stat: Mapped[list["PlayerGameStatOrm"]] = relationship(
        back_populates="player",
    )
    player_structure: Mapped[list["PlayerStructreOrm"]] = relationship(
        back_populates="player",
    )
    goal_player_goal_game: Mapped[list["GoalGameOrm"]] = relationship(
        foreign_keys="GoalGameOrm.goal_player_id",
        back_populates="goal_player",
    )
    pass_player_goal_game: Mapped[list["GoalGameOrm"]] = relationship(
        foreign_keys="GoalGameOrm.pass_player_id",
        back_populates="pass_player",
    )
    penalty_game: Mapped[list["PenaltyGameOrm"]] = relationship(
        back_populates="player",
    )
    
    
class CoachOrm(Base):
    __tablename__ = "coach"
    
    coach_id: Mapped[intpk]
    first_name: Mapped[str_100]
    last_name: Mapped[str_100 | None]
    middle_name: Mapped[str_100 | None]
    
    coach_game: Mapped[list["CoachGameOrm"]] = relationship(
        back_populates="coach",
    )
    
    
class RefereeOrm(Base):
    __tablename__ = "referee"
    
    referee_id: Mapped[intpk]
    first_name: Mapped[str_100]
    last_name: Mapped[str_100 | None]

    referee_game: Mapped[list["RefereeGameOrm"]] = relationship(
        back_populates="referee",
    )
    

class GoalTypeOrm(Base):
    __tablename__ = "goal_type"
    
    goal_type_id: Mapped[intpk]
    goal_type: Mapped[str_25]
    
    goal_game: Mapped[list["GoalGameOrm"]] = relationship(
        back_populates="goal_type",
    )
    

class PenaltyTypeOrm(Base):
    __tablename__ = "penalty_type"
    
    penalty_type_id: Mapped[intpk]
    penalty_type: Mapped[str_25]
    
    penalty_game: Mapped[list["PenaltyGameOrm"]] = relationship(
        back_populates="penalty_type",
    )


class StatusGameOrm(Base):
    __tablename__ = "status_game"
    
    status_game_id: Mapped[intpk]
    status_game: Mapped[str_25]
    
    calendar: Mapped[list["CalendarOrm"]] = relationship(
        back_populates="status_game",
    )
    
    
class RoleOrm(Base):
    __tablename__ = "role"
    
    role_id: Mapped[intpk]
    role: Mapped[str_25]
    
    player_stat: Mapped[list["PlayerStatOrm"]] = relationship(
        back_populates="role",
    )

class PlayerStatOrm(Base):
    __tablename__ = "player_stat"
    
    player_stat_id: Mapped[intpk]
    player_id: Mapped[int] = mapped_column(ForeignKey("player.player_id", ondelete="CASCADE"))
    role_id: Mapped[int] = mapped_column(ForeignKey("role.role_id", ondelete="CASCADE"))
    growth: Mapped[int | None]
    weight: Mapped[int | None]
    transfer_value: Mapped[int | None]
    created_at: Mapped[datetime]
    
    player: Mapped["PlayerOrm"] = relationship(
        back_populates="player_stat",
    )
    role: Mapped["RoleOrm"] = relationship(
        back_populates="player_stat",
    )
    

class PlayerGameStatOrm(Base):
    __tablename__ = "player_game_stat"
    
    player_id: Mapped[int] = mapped_column(
        ForeignKey("player.player_id", ondelete="CASCADE"),
        primary_key=True
    )
    season_id: Mapped[int] = mapped_column(
        ForeignKey("season.season_id", ondelete="CASCADE"),
        primary_key=True
    )
    team_id: Mapped[int] = mapped_column(
        ForeignKey("team.team_id", ondelete="CASCADE"),
        primary_key=True
    )
    number: Mapped[int]
    game_count: Mapped[int] # 
    game_minutes: Mapped[int]
    start_count: Mapped[int]
    in_change_count: Mapped[int]
    change_output_count: Mapped[int]
    reserve_count: Mapped[int]
    regular_goal: Mapped[int]
    penalties_goal: Mapped[int]
    missed_goal: Mapped[int]
    yellow_card: Mapped[int] # количество ж.карточек
    double_yellow_card: Mapped[int] # количество двойных ж.карточек
    red_card: Mapped[int] # количество к.карточек
    created_at: Mapped[datetime] # время создания записи (мск)
    updated_at: Mapped[datetime] # время обновления записи (мск)
    
    season: Mapped["SeasonOrm"] = relationship(
        back_populates="player_game_stat",
    )
    team: Mapped["TeamOrm"] = relationship(
        back_populates="player_game_stat",
    )
    player: Mapped["PlayerOrm"] = relationship(
        back_populates="player_game_stat",
    )
    
class RefereeGameOrm(Base):
    __tablename__ = "referee_game"
    
    calendar_id: Mapped[int] = mapped_column(
        ForeignKey("calendar.calendar_id", ondelete="CASCADE"),
        primary_key=True
    )
    referee_id: Mapped[int] = mapped_column(
        ForeignKey("referee.referee_id", ondelete="CASCADE"),
        primary_key=True
    )
    
    referee: Mapped["RefereeOrm"] = relationship(
        back_populates="referee_game",
    )
    
    
class CoachGameOrm(Base):
    __tablename__ = "coach_game"
    
    calendar_id: Mapped[int] = mapped_column(
        ForeignKey("calendar.calendar_id", ondelete="CASCADE"),
        primary_key=True
    )
    coach_id: Mapped[int] = mapped_column(
        ForeignKey("coach.coach_id", ondelete="CASCADE"),
        primary_key=True
    )
    team_id: Mapped[int] = mapped_column(
        ForeignKey("team.team_id", ondelete="CASCADE"),
        primary_key=True
    )
    
    calendar: Mapped["CalendarOrm"] = relationship(
        back_populates="coach_game",
    )
    coach: Mapped["CoachOrm"] = relationship(
        back_populates="coach_game",
    )
    team: Mapped["TeamOrm"] = relationship(
        back_populates="coach_game",
    )

class CalendarOrm(Base):
    __tablename__ = "calendar"
    
    calendar_id: Mapped[intpk]
    left_team_id: Mapped[int] = mapped_column(ForeignKey("team.team_id", ondelete="CASCADE")) # домашняя
    right_team_id: Mapped[int] = mapped_column(ForeignKey("team.team_id", ondelete="CASCADE")) # выездная
    status_game_id: Mapped[int] = mapped_column(ForeignKey("status_game.status_game_id", ondelete="CASCADE"))
    tour: Mapped[int]
    start_at: Mapped[datetime]
    left_team_score: Mapped[int]
    right_team_score: Mapped[int]
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]

    left_team: Mapped["TeamOrm"] = relationship(
        foreign_keys=[left_team_id],
        back_populates="left_calendar",
    )
    right_team: Mapped["TeamOrm"] = relationship(
        foreign_keys=[right_team_id],
        back_populates="right_calendar",
    )
    status_game: Mapped["StatusGameOrm"] = relationship(
        back_populates="calendar",
    )
    player_structure: Mapped[list["PlayerStructreOrm"]] = relationship(
        back_populates="calendar",
    )
    goal_game: Mapped[list["GoalGameOrm"]] = relationship(
        back_populates="calendar",
    )
    penalty_game: Mapped[list["PenaltyGameOrm"]] = relationship(
        back_populates="calendar",
    )
    stat_game: Mapped[list["StatGameOrm"]] = relationship(
        back_populates="calendar",
    )
    coach_game: Mapped[list["CoachGameOrm"]] = relationship(
        back_populates="calendar"
    )

class StandingsOrm(Base):
    __tablename__ = "standings"
    
    standings_id: Mapped[intpk]
    team_id: Mapped[int] = mapped_column(ForeignKey("team.team_id", ondelete="CASCADE"))
    season_id: Mapped[int] = mapped_column(ForeignKey("season.season_id", ondelete="CASCADE"))
    game_count: Mapped[int]
    win_count: Mapped[int]
    draw_count: Mapped[int]
    loss_count: Mapped[int]
    scored_goal: Mapped[int]
    missed_goal: Mapped[int]
    score: Mapped[int]
    created_at: Mapped[datetime]
    
    season: Mapped["SeasonOrm"] = relationship(
        back_populates="standings",
    )
    team: Mapped["TeamOrm"] = relationship(
        back_populates="standings",
    )
    
    
class PlayerStructreOrm(Base):
    __tablename__ = "player_structure"
    
    calendar_id: Mapped[int] = mapped_column(
        ForeignKey("calendar.calendar_id", ondelete="CASCADE"),
        primary_key=True
    )
    team_id: Mapped[int] = mapped_column(
        ForeignKey("team.team_id", ondelete="CASCADE"),
        primary_key=True
    )
    player_id: Mapped[int] = mapped_column(
        ForeignKey("player.player_id", ondelete="CASCADE"),
        primary_key=True
    )
    start_at: Mapped[int] # минута
    end_at: Mapped[int] # минута
    
    team: Mapped["TeamOrm"] = relationship(
        back_populates="player_structure",
    )
    player: Mapped["PlayerOrm"] = relationship(
        back_populates="player_structure",
    )
    calendar: Mapped["CalendarOrm"] = relationship(
        back_populates="player_structure",
    )
    
class GoalGameOrm(Base):
    __tablename__ = "goal_game"
    
    goal_game_id: Mapped[intpk]
    calendar_id: Mapped[int] = mapped_column(ForeignKey("calendar.calendar_id", ondelete="CASCADE"))
    team_id: Mapped[int] = mapped_column(ForeignKey("team.team_id", ondelete="CASCADE"))
    goal_player_id: Mapped[int] = mapped_column(ForeignKey("player.player_id", ondelete="CASCADE"))
    pass_player_id: Mapped[int | None] = mapped_column(ForeignKey("player.player_id", ondelete="CASCADE"))
    goal_type_id: Mapped[int] = mapped_column(ForeignKey("goal_type.goal_type_id", ondelete="CASCADE"))
    minute: Mapped[int]
    
    team: Mapped["TeamOrm"] = relationship(
        back_populates="goal_game",
    )
    goal_player: Mapped["PlayerOrm"] = relationship(
        foreign_keys=[goal_player_id],
        back_populates="goal_player_goal_game",
    )
    pass_player: Mapped["PlayerOrm"] = relationship(
        foreign_keys=[pass_player_id],
        back_populates="pass_player_goal_game",
    )
    goal_type: Mapped["GoalTypeOrm"] = relationship(
        back_populates="goal_game",
    )
    calendar: Mapped["CalendarOrm"] = relationship(
        back_populates="goal_game",
    )
    
    
class PenaltyGameOrm(Base):
    __tablename__ = "penalty_game"
    
    penalty_game_id: Mapped[intpk]
    calendar_id: Mapped[int] = mapped_column(ForeignKey("calendar.calendar_id", ondelete="CASCADE"))
    team_id: Mapped[int] = mapped_column(ForeignKey("team.team_id", ondelete="CASCADE"))
    player_id: Mapped[int] = mapped_column(ForeignKey("player.player_id", ondelete="CASCADE"))
    penalty_type_id: Mapped[int] = mapped_column(ForeignKey("penalty_type.penalty_type_id", ondelete="CASCADE"))
    minute: Mapped[int]
    
    team: Mapped["TeamOrm"] = relationship(
        back_populates="penalty_game",
    )
    player: Mapped["PlayerOrm"] = relationship(
        back_populates="penalty_game",
    )
    penalty_type: Mapped["PenaltyTypeOrm"] = relationship(
        back_populates="penalty_game",
    )
    calendar: Mapped["CalendarOrm"] = relationship(
        back_populates="penalty_game",
    )
    

class StatGameOrm(Base):
    __tablename__ = "stat_game"
    
    stat_game_id: Mapped[intpk]
    calendar_id: Mapped[int] = mapped_column(ForeignKey("calendar.calendar_id", ondelete="CASCADE"))
    team_id: Mapped[int] = mapped_column(ForeignKey("team.team_id", ondelete="CASCADE"))
    minute: Mapped[int]
    created_at: Mapped[datetime]
    attacks: Mapped[int]
    deletions: Mapped[int]
    warnings: Mapped[int]
    outs: Mapped[int]
    blocked_shots: Mapped[int]
    shots_from_goal: Mapped[int]
    free_kicks: Mapped[int]
    ball_possession_percent: Mapped[int]
    offsides: Mapped[int]
    corners: Mapped[int]
    shots_hit_post: Mapped[int]
    fouls: Mapped[int]
    shots_on_target: Mapped[int]
    shots_on_goal: Mapped[int]
    goal_scoring_chances: Mapped[int]
    dangerous_moments: Mapped[int]
    
    team: Mapped["TeamOrm"] = relationship(
        back_populates="stat_game",
    )
    calendar: Mapped["CalendarOrm"] = relationship(
        back_populates="stat_game",
    )
