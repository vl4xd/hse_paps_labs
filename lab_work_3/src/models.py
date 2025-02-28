from datetime import date, datetime, timezone
from typing import Annotated
from sqlalchemy import ForeignKey, Index, CheckConstraint, text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base, str_25, str_100


intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.now(timezone.utc),
)]


class TeamOrm(Base):
    __tablename__ = "team"
    
    team_id: Mapped[intpk]
    name: Mapped[str_100]
    town: Mapped[str_100 | None]
    stadium: Mapped[str_100 | None]
    
    __table_args__ = (
        Index("name_index", "name"),
    )


class SeasonOrm(Base):
    __tablename__ = "season"
    
    season_id: Mapped[intpk]
    start_date: Mapped[date]
    end_date: Mapped[date]
    
    __table_args__ = (
        Index("season_time_index", "start_time", "end_time"),
    )
    
    
class PlayerOrm(Base):
    __tablename__ = "player"
    
    player_id: Mapped[intpk] 
    first_name: Mapped[str_100]
    last_name: Mapped[str_100 | None]
    
    
class CoachOrm(Base):
    __tablename__ = "coach"
    
    coach_id: Mapped[intpk]
    first_name: Mapped[str_100]
    last_name: Mapped[str_100 | None]
    middle_name: Mapped[str_100 | None]
    
    
class RefereeOrm(Base):
    __tablename__ = "referee"
    
    referee_id: Mapped[intpk]
    first_name: Mapped[str_100]
    last_name: Mapped[str_100 | None]


class GoalTypeOrm(Base):
    __tablename__ = "goal_type"
    
    goal_type_id: Mapped[intpk]
    goal_type: Mapped[str_25]
    

class PenaltyTypeOrm(Base):
    __tablename__ = "penalty_type"
    
    penalty_type_id: Mapped[intpk]
    penalty_type: Mapped[str_25]


class StatusGameOrm(Base):
    __tablename__ = "status_game"
    
    status_game_id: Mapped[intpk]
    status_game: Mapped[str_25]
    
    
class RoleOrm(Base):
    __tablename__ = "role"
    
    role_id: Mapped[intpk]
    role: Mapped[str_25]
    

class PlayerStatOrm(Base):
    __tablename__ = "player_stat"
    
    player_stat_id: Mapped[intpk]
    player_id: Mapped[int] = mapped_column(ForeignKey("player.player_id", ondelete="CASCADE"))
    role_id: Mapped[int] = mapped_column(ForeignKey("role.role_id", ondelete="CASCADE"))
    growth: Mapped[int | None]
    weight: Mapped[int | None]
    tansfer_value: Mapped[int | None]
    created_at: Mapped[created_at | None]
    

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
    game_count: Mapped[int]
    game_minutes: Mapped[int]
    start_count: Mapped[int]
    in_change_count: Mapped[int]
    change_output_count: Mapped[int]
    reserve_count: Mapped[int]
    regular_goal: Mapped[int]
    penalties_goal: Mapped[int]
    missed_goal: Mapped[int]
    yellow_card: Mapped[int]
    double_yellow_card: Mapped[int]
    red_card: Mapped[int]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    
    
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
    

class CalendarOrm(Base):
    __tablename__ = "calendar"
    
    calendar_id: Mapped[intpk]
    left_team_id: Mapped[int] = mapped_column(ForeignKey("team.team_id", ondelete="CASCADE"))
    right_team_id: Mapped[int] = mapped_column(ForeignKey("team.team_id", ondelete="CASCADE"))
    status_game_id: Mapped[int] = mapped_column(ForeignKey("status_game.status_game_id", ondelete="CASCADE"))
    tour: Mapped[int]
    start_at: Mapped[datetime]
    left_team_score: Mapped[int]
    right_team_score: Mapped[int]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


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
    created_at: Mapped[created_at]
    
    
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
    start_at: Mapped[int]
    end_at: Mapped[int]
    
    
class GoalGameOrm(Base):
    __tablename__ = "goal_game"
    
    goal_game_id: Mapped[intpk]
    calendar_id: Mapped[int] = mapped_column(ForeignKey("calendar.calendar_id", ondelete="CASCADE"))
    team_id: Mapped[int] = mapped_column(ForeignKey("team.team_id", ondelete="CASCADE"))
    goal_player_id: Mapped[int] = mapped_column(ForeignKey("player.player_id", ondelete="CASCADE"))
    pass_player_id: Mapped[int | None] = mapped_column(ForeignKey("player.player_id", ondelete="CASCADE"))
    goal_type_id: Mapped[int] = mapped_column(ForeignKey("goal_type.goal_type_id", ondelete="CASCADE"))
    minute: Mapped[int]
    
    
class PenaltyGameOrm(Base):
    __tablename__ = "penalty_game"
    
    penalty_game_id: Mapped[intpk]
    calendar_id: Mapped[int] = mapped_column(ForeignKey("calendar.calendar_id", ondelete="CASCADE"))
    team_id: Mapped[int] = mapped_column(ForeignKey("team.team_id", ondelete="CASCADE"))
    player_id: Mapped[int] = mapped_column(ForeignKey("player.player_id", ondelete="CASCADE"))
    penalty_type_id: Mapped[int] = mapped_column(ForeignKey("penalty_type.penalty_type_id", ondelete="CASCADE"))
    minute: Mapped[int]
    

class StatGameOrm(Base):
    __tablename__ = "stat_game"
    
    stat_game_id: Mapped[intpk]
    calendar_id: Mapped[int] = mapped_column(ForeignKey("calendar.calendar_id", ondelete="CASCADE"))
    team_id: Mapped[int] = mapped_column(ForeignKey("team.team_id", ondelete="CASCADE"))
    minute: Mapped[int]
    created_at: Mapped[created_at]
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
