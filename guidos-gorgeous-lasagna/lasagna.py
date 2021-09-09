EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the prep time of lasagna, based on the number of layers added.
    
    param: int number_of_layers: how many layers are added to the lasagna.
    return: int total time in minutes of preparation of all layers.

    Function that takes the decided number of layers of the lasagna as 
    an argument and returns how many minutes the lasagna will be ready at 
    for baking based on the `PREPARATION_TIME` for each layer.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate elapsed cooking time.
 
    param: int number_of_layers: the number of layers added to the lasagna
    param: int elapsed_bake_time: the number of minutes the lasagna has been baking in the oven.
    return: int total time in minutes of cooking (prep + bake).

    Function that takes the prepared number of layers of the lasagna and the elapsed time they 
    have been baking in the oven as arguments and return the total time in minutes that the lasagna
    have been cooking.
    """
    prep = PREPARATION_TIME * number_of_layers
    return prep + elapsed_bake_time
