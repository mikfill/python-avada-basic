import logging
import pytest


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="avada.log",
)


def is_plants_win_zombies(plants: list[int], zombies: list[int]) -> bool:
    plants_count = len(plants)
    zombies_count = len(zombies)
    plants_power = sum(plants)
    zombies_power = sum(zombies)
    plants_survive = 0
    zombies_survive = 0

    if plants_count > zombies_count:
        plants_survive += plants_count - zombies_count
    if zombies_count > plants_count:
        zombies_survive += zombies_count - plants_count

    for value in zip(plants, zombies):
        if value[0] - value[1] > 0:
            plants_survive += 1
        if value[1] - value[0] > 0:
            zombies_survive += 1

    if plants_survive == zombies_survive:
        return plants_power >= zombies_power

    return plants_survive > zombies_survive


if __name__ == "__main__":
    pytest.main()
