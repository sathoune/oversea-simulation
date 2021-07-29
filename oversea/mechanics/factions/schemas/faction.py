from typing import Tuple, List

from pydantic import BaseModel

from oversea.mechanics.factions.schemas.bank import Bank
from oversea.mechanics.factions.schemas.base_resources import BaseResources
from oversea.mechanics.factions.schemas.building import Building
from oversea.mechanics.factions.schemas.colony_data import ColonyData
from oversea.mechanics.factions.schemas.fleet import Fleet
from oversea.mechanics.factions.schemas.income import Income
from oversea.mechanics.factions.schemas.ship_data import ShipData, Stats
from oversea.mechanics.factions.schemas.technology import Technology


class Faction(BaseModel):

    name: str
    combat_factor: int
    base_resources: BaseResources
    base_income: BaseResources
    main_goal: str
    perks: Tuple[str, str]
    buildings: List[Building]
    technologies: List[Technology]
    magic_technologies: List[Technology]
    ships: List[ShipData]
    stronghold_stats: Stats
    income: Income
    bank: Bank
    fleet: Fleet
    colony_data: ColonyData
