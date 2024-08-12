from abc import ABC, abstractmethod


class PrettifyStrategy(ABC):
    @abstractmethod
    def prettify(self, number: float) -> str:
        pass


class DefaultPrettifyStrategy(PrettifyStrategy):
    def prettify(self, number: float) -> str:
        """
        Prettify a number using the default strategy with suffixes for millions (M), billions (B), and trillions (T).

        :param number: The input number to prettify
        :return: The prettified number as a string
        """
        suffixes = {1_000_000_000_000: 'T', 1_000_000_000: 'B', 1_000_000: 'M'}

        for value, suffix in sorted(suffixes.items(), reverse=True):
            if number >= value:
                prettified_number = number / value
                # Format the number with one decimal place if it's not an integer
                if prettified_number.is_integer():
                    return f"{int(prettified_number)}{suffix}"
                else:
                    return f"{prettified_number:.1f}{suffix}"

        # Return the number as is if less than a million
        return str(number)

