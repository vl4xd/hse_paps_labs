from datetime import date, datetime
from pydantic import BaseModel, ConfigDict


class TeamAddDTO(BaseModel):
    name: str
    town: str
    stadium: str

class TeamDTO(TeamAddDTO):
    team_id: int
    
class RoleDTO(BaseModel):
    role_id: int
    role: str

class PlayerAddDTO(BaseModel):
    first_name: str
    last_name: str | None
    
class PlayerDTO(PlayerAddDTO):
    player_id: int
    
class PlayerStatAddDTO(BaseModel):
    player_id: int
    role_id: int
    growth: int
    weight: int
    transfer_value: int
    created_at: datetime | None
    
class PlayerStatDTO(PlayerStatAddDTO):
    player_stat_id: int
    
class PlayerStatRelRoleDTO(PlayerStatDTO):
    role: "RoleDTO"

class PlayerRelPlayerStatDTO(PlayerDTO):
    player_stat: list["PlayerStatRelRoleDTO"]
    
class RefereeAddDTO(BaseModel):
    first_name: str
    last_name: str | None
        
class RefereeDTO(RefereeAddDTO):
    referee_id: int
    
class TeamAddDTO(BaseModel):
    name: str
    town: str
    stadium: str
    
class TeamDTO(TeamAddDTO):
    team_id: int
    
class StatusGameDTO(BaseModel):
    status_game_id: int
    status_game: str

class CalendarAddDTO(BaseModel):
    left_team_id: int
    right_team_id: int
    status_game_id: int
    tour: int
    start_at: datetime
    left_team_score: int
    right_team_score: int
    created_at: datetime
    updated_at: datetime

class CalendarDTO(CalendarAddDTO):
    calendar_id: int
    
class CalendarChgStatusDTO(BaseModel):
    status_game_id: int
    
class CalendarRelDTO(CalendarDTO):
    left_team: "TeamDTO"
    right_team: "TeamDTO"
    status_game: "StatusGameDTO"
    
class CoachAddDTO(BaseModel):
    first_name: str
    last_name: str | None
    middle_name: str | None   
    
class CoachDTO(CoachAddDTO):
    coach_id: int 
    
class CoachGameRelDTO(BaseModel):
    coach: "CoachDTO"
    team: "TeamDTO"