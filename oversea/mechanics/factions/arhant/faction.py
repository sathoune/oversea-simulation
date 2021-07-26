from oversea.mechanics.factions.arhant.buildings import arhant_buildings
from oversea.mechanics.factions.arhant.magic_technologies import (
    arhant_magic_technologies,
)
from oversea.mechanics.factions.arhant.ships import arhant_ships
from oversea.mechanics.factions.arhant.technologies import arhant_technologies
from oversea.mechanics.factions.schemas.base_resources import BaseResources
from oversea.mechanics.factions.schemas.cost import Cost
from oversea.mechanics.factions.schemas.fraction import Faction
from oversea.mechanics.factions.schemas.ship_data import Stats

arhant = Faction(
    name="Arhant",
    combat_factor=2,
    base_resources=BaseResources(
        cash=4,
        geist=3,
        intrigue_cards=2,
    ),
    base_income=Cost(
        cash=2,
        geist=0,
    ),
    main_goal="Destroy three cities, including one capital city.",
    perks=(
        "Once a round you can discard a Intrigue or Magic card to draw a new one or gain 2 cash "
        "or 1 geist.",
        "Sacrifice 1 geist when playing a card to draw a new one of the same type.",
    ),
    buildings=arhant_buildings,
    technologies=arhant_technologies,
    magic_technologies=arhant_magic_technologies,
    ships=arhant_ships,
    stronghold_stats=Stats(
        range=5,
        fire_power=3,
        resilience=4,
        hit_points=1,
        speed=0,
    ),
    colony_cost=Cost(cash=4),
    colony_income=Cost(cash=2),
)