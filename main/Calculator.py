from CalculatorHelper import getNumbers


class Calculator(object):

    def _string_split(self, param):
        splitter = ","
        tail = param

        if param.startswith("//"):
            split = param.split("\n")
            splitter = split[0].replace("//", "")
            tail = split[1]

        clean_tail = tail.replace(splitter, ",").replace("\n", ",")
        return clean_tail

    def _inner_loop(self, param):
        delimiter = self._string_split(param)
        num_string = delimiter
        nums = getNumbers(num_string, ",")
        acc = 0
        for num in nums:
            acc += num
        return acc

    def add(self, param):
        if param != "":
            return self._inner_loop(param)
        else:
            return 0
