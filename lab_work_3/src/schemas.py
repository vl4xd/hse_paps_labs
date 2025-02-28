from datetime import date
from pydantic import BaseModel, ConfigDict


class SeasonPostDTO(BaseModel):
    start_year: date
    end_year: date
    

class SeasonGetDTO(SeasonPostDTO):
    season_id: int