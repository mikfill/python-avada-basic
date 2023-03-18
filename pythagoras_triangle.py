import logging
import pytest


class LengthArrayError(Exception):
    pass


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="avada.log",
)


def is_pythagoras_triangle(arr: list[int, float]) -> bool:
    len_arr = len(arr)
    logging.debug(f"Length of array is {len_arr}")
    try:
        if len_arr != 3:
            logging.critical("This is not triangle!")
            raise LengthArrayError
        for number in arr:
            if number <= 0:
                logging.critical("Incorrect values in list!")
                raise ValueError

        sorted_arr = arr[:]
        sorted_arr.sort(reverse=True)
        c, a, b = sorted_arr
        logging.debug(f"Hypotenuse={c}, Side1={a}, Side2={b}")
        result = a**2 + b**2 == c**2
        logging.debug(f"Result is {result}")

        return result

    except LengthArrayError:
        print("Exception occurred: List must contains three number's")
    except ValueError:
        print("Exception occurred: List must contains only positive number's")


if __name__ == "__main__":
    pytest.main()
