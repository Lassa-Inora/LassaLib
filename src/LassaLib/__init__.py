"""Convenient function set"""
import os

import LassaLib

try:
    import text_editing

    COLOR = True
except ModuleNotFoundError:
    COLOR = False

import typing

_LANGUAGE = {
    'yes': ["yes", "是的", "हां", "sí", "si", "نعم", "হ্যাঁ", "oui", "да", "sim", "جی ہاں", "y", "1", "true"],
    'no': ["no", "不", "नहीं", "no", "لا", "না", "non", "нет", "não", "nao", "نہیں", "n", "0", "false"]
}


def enter(__prompt='', __type=int):
    """This function allows to input any type

    :param __prompt: Text to print before recovery
    :type __prompt: str
    :param __type: The type to recover
    :type __type: type
    :return: The input in the requested type
    :rtype: Any
    """
    var: str = input(__prompt)
    while True:
        try:
            '''  '''
            if __type == bool:
                if var.lower() in _LANGUAGE['yes']:
                    return True
                elif var.lower() in _LANGUAGE['false']:
                    return False
                else:
                    raise ValueError(f"could not convert string to bool: '{var}'")
            return __type(var)
        except ValueError:
            print(f"\"{var}\" is not the type {__type.__name__}")
            var: str = input(__prompt)


def last_iteration(iteration_text, txt):
    """Return the index of the last iteration on string.

    :param iteration_text: The searched iteration
    :type iteration_text: str
    :param txt: The text to search in.
    :type txt: str
    :return: The index of last iteration.
    :rtype: int
    """
    liste = txt.split(iteration_text)
    if len(liste) == 1:
        return None
    else:
        return len(txt) - (len(liste[-1]) + len(iteration_text))


def menu(__list, __name, __desc="", back=True):
    """Print a list of choice and user choice one.

    :param __list: The list of choice
    :type __list: list
    :param __name: The name of choice
    :type __name: str
    :param __desc: A description of choice.
    :type __desc: str
    :param back: Can he go back?
    :type back: bool
    :return: The choice of the user.
    :rtype: int
    """

    def get_number(n):
        return ('0' * (len(str(len(__list))) - len(str(n)))) + str(n)

    def get_view():
        length = max([len(__name) + 12, 6 + len(str(len(__list))) + max([len(choice) for choice in __list])])
        mi_length = [
            int((length - (12 + len(__name))) / 2),
            int((length - (12 + len(__name))) / 2) + (1 if length % 2 == 1 else 0)
        ]

        desc = [""]
        for word in __desc.split():
            if len(desc[-1] + " " + word) > (length - 5):
                desc.append("")
            desc[-1] += " " + word

        text = ""
        text += f"    {' ' * mi_length[0]}┌─{'─' * len(__name)}─┐{' ' * mi_length[1]}    \n"
        text += f"┌───{'─' * mi_length[0]}┤ {__name} ├{'─' * mi_length[1]}───┐\n"
        text += f"│   {' ' * mi_length[0]}└─{'─' * len(__name)}─┘{' ' * mi_length[1]}   │\n"
        for line in desc:
            text += f"│ {line} {' ' * (length - (5 + len(line)))} │\n"
        text += f"├{'-' * (length - 2)}┤\n"
        for i in range(len(__list)):
            text += f"│ {get_number(i + 1)}) {__list[i]} {' ' * (length - 6 - len(str(len(__list))) - len(__list[i]))}│\n"
        if back:
            text += f"│{' ' * (length - 2)}│\n"
            text += f"│ 0) Back {' ' * (length - 11)}│\n"
        text += f"└{'─' * (length - 2)}┘\n"

        return text

    print(get_view())
    chx = -1
    while chx not in range(0 if back else 1, len(__list) + 1):
        chx = enter(">> ")
    return chx


def replace_last(sub_string, new_string, string):
    """Replaces the last iteration of the substring entered with the string chosen in the quoted string.

    :param sub_string: The substring entered.
    :type sub_string: str
    :param new_string: The string chosen.
    :type new_string: str
    :param string: The quoted string.
    :type string: str
    :return: The quoted string with the last iteration of the substring replaced by the chosen string.
    :rtype: str
    """
    li = last_iteration(sub_string, string)
    if li is None:
        return string
    return string[0:li] + new_string + string[li + len(sub_string):]


def show_value(value: typing.Any, tab_number: int = 0) -> None:
    """
    Prints in the terminal all the elements of a list, a dictionary or a tuple and its sub-elements.
    Prints in the terminal the other types and class.
    :param value: A value of any type or class.
    :param tab_number: The default number of tabs to put in front of the printout.
    :return: None
    """

    def sort_key(dico):
        if isinstance(dico, dict):
            liste_key = list(dico.keys())
            sorted_liste_key = []
            while len(liste_key) > 0:
                best = liste_key[0]
                for key_from_list in liste_key:
                    i = 0
                    stop = False
                    while i < min(len(str(best)), len(str(key_from_list))) and not stop:
                        if ord(str(best)[i]) > ord(str(key_from_list)[i]):
                            best = key_from_list
                            stop = True
                        elif ord(str(best)[i]) < ord(str(key_from_list)[i]):
                            stop = True
                        i += 1
                    if not stop:
                        if len(str(key_from_list)) < len(str(best)):
                            best = key_from_list
                liste_key.remove(best)
                sorted_liste_key.append(best)
            return sorted_liste_key
        else:
            return []

    print(f"{text_editing.color.COLOR_PURPLE if COLOR else ''}{type(value)}", end="")
    if isinstance(value, list) and isinstance(value, dict) and isinstance(value, tuple):
        print(f" ({len(value)} items):")
        for key in (sort_key(value) if isinstance(value, dict) else range(len(value))):
            print("\t" * tab_number + f"{text_editing.color.COLOR_GREEN if COLOR else ''}{key}: ", end='')
            show_value(value[key], tab_number + 1)
    else:
        print(f" : {text_editing.color.COLOR_YELLOW if COLOR else ''}"
              f"{value}{text_editing.color.STOP_COLOR if COLOR else ''}")


def space_number(number: typing.Union[int, float], spacing: str = ' ') -> str:
    """
    Separate with character defines the number entered every 3 digits.
    :param number: A value.
    :param spacing: A character.
    :return: A string of number separate.
    """
    if isinstance(number, int):
        number_list = list(str(number))
        txt = ""
        i = 0
        while len(number_list) != 0:
            if i == 3:
                i = 0
                txt = spacing + txt
            txt = number_list.pop() + txt
            i += 1
        return txt
    else:
        return space_number(int(number), spacing) + '.' + str(number).split('.')[1]


def str_object(obj):
    """Create a string of all info about an object regardless of its class.

    :param obj: An object from Any type or class.
    :type obj: Any
    :return: A string that summarizes the object in detail.
    :rtype: str
    """
    try:
        max_key_length = max([len(key) for key in obj.__dict__])
        txt = f"{obj.__class__.__name__} : \n"

        for key in obj.__dict__:
            txt += f"\t - {key.center(max_key_length, ' ')} : {obj.__dict__[key]}\n"

        return txt
    except Exception as e:
        str(e)
        return f"{obj.__class__.__name__} : {str(obj)}\n"


if __name__ == '__main__':
    menu(["Banane", "Fraise", "Ananas"], "Salade de fruits", "Choix pour une salade de fruit délicieuse!")
