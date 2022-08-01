
from .Test.test import run_test
from .Test.test_lib import defineArguments, processInput

availableTests = {
    "teo:buildmodel": run_test
}


def init():
    # DO NOT CHANGE FROM THIS POINT BELOW
    # UNLESS YOU KNOW WHAT YOUR DOING
    args = defineArguments(availableTests)

    try:
        processInput(args, availableTests)
    except Exception as e:
        print(e)
