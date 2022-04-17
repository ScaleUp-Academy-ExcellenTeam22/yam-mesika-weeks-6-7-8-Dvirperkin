def group_by(function, iterable):
    """
    :param function: A function to execute on each iterable element.
    :param iterable: An iterable object.
    :return: A dictionary that its keys is the results of the function on the elements and the values is the elements.
    """
    function_results_dict = {}

    for element in iterable:
        res = function(element)
        if function_results_dict.get(res):
            function_results_dict[res] += [element]
        else:
            function_results_dict[res] = [element]
    return function_results_dict


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
