from prettifier import LargeNumberPrettifier

if __name__ == "__main__":
    prettifier = LargeNumberPrettifier()
    print(prettifier.prettify(1000000))  # Output: "1M"
