from .strategies import PrettifyStrategy, DefaultPrettifyStrategy


class LargeNumberPrettifier:
    def __init__(self, strategy: PrettifyStrategy = None):
        """
        Initialize the NumberPrettifier with a given strategy.
        If no strategy is provided, use the DefaultPrettifyStrategy.

        :param strategy: The PrettifyStrategy to use. Defaults to DefaultPrettifyStrategy.
        """
        self._strategy = strategy or DefaultPrettifyStrategy()

    def prettify(self, number: float) -> str:
        """
        Prettify a number using the selected strategy.

        :param number: The input number to prettify
        :return: The prettified number as a string
        """
        return self._strategy.prettify(number)

