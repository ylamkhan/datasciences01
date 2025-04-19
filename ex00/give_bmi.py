
def chekList(lst):
    for i in range(len(lst)):
        if type(lst[i]) is not int and type(lst[i]) is not float:
            return False
    return True


def give_bmi(
        height: list[int | float],
        weight: list[int | float]) -> list[int | float]:
    """
        To calculate BMI (Body Mass Index), you use the following formula:
               weight in kilograms
        BMI = ---------------------
               (height in meters)^2
    """
    try:
        if height is None or weight is None:
            raise AssertionError("the List is None")
        if not isinstance(height, list) or not isinstance(weight, list):
            raise AssertionError("not a list")
        if len(height) != len(weight):
            raise AssertionError("the lista height and weight are Bad")
        if chekList(height) is False or chekList(weight) is False:
            raise AssertionError("The List is bad")
        result = []
        i = 0
        while i < len(height):
            if height[i] <= 0:
                raise AssertionError("the height is bad")
            if weight[i] <= 0:
                raise AssertionError("the weight is bad")
            bmi = weight[i] / height[i]**2
            result .append(bmi)
            i += 1
        return result
    except AssertionError as ve:
        print("\033[91mAssertionError\033[0m", ve)
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        this function return list the bool;
        if bmi[i] > limit is True
        else is False
    """
    try:
        if bmi is None or limit is None:
            raise AssertionError("the list bmi or limit is None")
        if not isinstance(bmi, list):
            raise AssertionError("not a list")
        if chekList(bmi) is False:
            raise AssertionError("the list is bad")
        if not isinstance(limit, int):
            raise AssertionError("the limit bad")
        result = []
        for i in range(len(bmi)):
            result.append(bmi[i] > limit)
        return result
    except AssertionError as ve:
        print("\033[91mAssertionError\033[0m", ve)
        return None
