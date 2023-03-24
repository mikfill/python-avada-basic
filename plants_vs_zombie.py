import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="plants_vs_zombie.log",
)


def is_plants_win_zombies(plants: list[int], zombies: list[int]) -> bool:
    try:
        plants_count = len(plants)
        zombies_count = len(zombies)
        plants_power = sum(plants)
        zombies_power = sum(zombies)

        plants_survive = sum(1 for p, z in zip(plants, zombies) if p > z)
        zombies_survive = sum(1 for p, z in zip(plants, zombies) if z > p)

        plants_survive += max(0, plants_count - zombies_count)
        zombies_survive += max(0, zombies_count - plants_count)

        if plants_survive == zombies_survive:
            return plants_power >= zombies_power

        return plants_survive > zombies_survive
    except TypeError:
        logging.error("Invalid Input data")
        return False
