"""Convenient function set

Author:
    Axelle (LassaInora) VIANDIER
    axelleviandier@lassainora.fr
Version:
    3.0.1
"""


def detailed_object(value, *, detailed=False, __tab_number=0):
    """Shows information about an object.

    Parameters:
        value (Any) : A value of any type or class.
        detailed (bool) : Should the function send detailed content?
        __tab_number (int) : The default number of tabs to put in front of the printout.
    """

    class _sort:
        def __init__(self, obj):
            self._obj = obj
            if not isinstance(obj, type):
                self._not_called_obj = type(obj)
            else:
                self._not_called_obj = None

            self._attributes = self._init_attributes()

        def _init_attributes(self):
            def get_all_attr(obj):
                all = dir(obj)
                if '__class__' in all:
                    all.remove('__class__')
                if '__init__' in all:
                    all.remove('__init__')
                if '__dict__' in all:
                    all.remove('__dict__')
                if '__doc__' in all:
                    all.remove('__doc__')
                if '__module__' in all:
                    all.remove('__module__')
                if '__weakref__' in all:
                    all.remove('__weakref__')
                return {attr: getattr(obj, attr) for attr in all}

            attr_not_called = get_all_attr(self._not_called_obj) if self._not_called_obj else {}
            attr_called = get_all_attr(self._obj)

            vars = {
                # Attributes
                'class_attribute': [],
                'instance_attribute': [],
                'property_attribute': [],

                # Method
                'static_method': [],
                'class_method': [],
                'instance_method': [],

                'magic_method': [],
                'init_method': []
            }

            for attr in attr_called:
                called = type(attr_called[attr])
                not_called = type(attr_not_called[attr]) if attr in attr_not_called else None

                vars[self.types().get_type_attribute(called, not_called, attr)].append(attr)

            return vars

        class types:
            def get_type_attribute(self, called, not_called=None, name=''):
                if not_called is None:
                    if called == self.function:
                        return 'instance_method'
                    elif called == self.getset_descriptor:
                        return 'class_method'
                    elif called == self.builtin_function_or_method:
                        return 'init_method'
                    elif called == self.method_descriptor:
                        if name.startswith('__'):
                            return 'magic_method'
                        else:
                            return 'instance_method'
                    elif called == self.wrapper_descriptor:
                        return 'magic_method'
                    elif called == property:
                        return 'property_attribute'
                    elif called == self.method:
                        return 'class_method'
                    else:
                        return 'instance_attribute'
                else:
                    if called == self.method_wrapper and not_called == self.wrapper_descriptor:
                        return 'magic_method'
                    elif called == self.builtin_function_or_method and not_called == self.method_descriptor:
                        if name.startswith('__'):
                            return 'magic_method'
                        else:
                            return 'instance_method'
                    elif called == self.builtin_function_or_method and not_called == self.builtin_function_or_method:
                        return 'init_method'
                    elif called == self.method and not_called == self.method:
                        return 'class_method'
                    elif called == self.function and not_called == self.function:
                        return 'static_method'
                    elif called == self.method and not_called == self.function:
                        return 'instance_method'
                    elif not_called == property:
                        return 'property_attribute'
                    else:
                        return 'class_attribute'

            @property
            def method(self):
                return type(self._method)

            @property
            def function(self):
                return type(self._function)

            @property
            def method_wrapper(self):
                return type(self.__eq__)

            @property
            def builtin_function_or_method(self):
                return type(self.__dir__)

            @property
            def wrapper_descriptor(self):
                return type(int.__abs__)

            @property
            def method_descriptor(self):
                return type(int.__ceil__)

            @property
            def getset_descriptor(self):
                return type(int.denominator)

            @classmethod
            def _method(cls):
                pass

            @staticmethod
            def _function(self):
                pass

        @property
        def str(self):
            return str(self._obj)

        @property
        def repr(self):
            return repr(self._obj)

        @property
        def type(self):
            return type(self._obj)

        @property
        def class_attribute(self):
            return self._attributes['class_attribute']

        @property
        def instance_attribute(self):
            return self._attributes['instance_attribute']

        @property
        def property_attribute(self):
            return self._attributes['property_attribute']

        @property
        def static_method(self):
            return self._attributes['static_method']

        @property
        def class_method(self):
            return self._attributes['class_method']

        @property
        def instance_method(self):
            return self._attributes['instance_method']

        @property
        def magic_method(self):
            return self._attributes['magic_method']

        @property
        def init_method(self):
            return self._attributes['init_method']

        def get(self, attr):
            return getattr(self._obj, attr)

    def get_function_signature(f):
        i = -1
        signature = []

        varnames = list(f.__code__.co_varnames[:f.__code__.co_argcount])
        try:
            defaults = list(f.__defaults__)
        except TypeError:
            defaults = []

        while i >= -len(varnames):
            signature.append(
                f"{varnames[i]}" +
                (
                    f"={defaults[i]}"
                    if i >= -len(defaults) else
                    ''
                )
            )
            i -= 1
        signature.reverse()
        return f"{f.__name__}(" + ', '.join(signature) + ')'

    obj = _sort(value)

    print("\t" * __tab_number + f"{obj.str} ({obj.type.__name__}): ")
    print("\t" * (__tab_number + 1) + f"Canonical string representation : {obj.repr}")
    if detailed:
        print("\t" * (__tab_number + 1) + f"Magic and init methods : ")
        print("\t" * (__tab_number + 2) + f"MagicMethods : ")
        for mm in obj.magic_method:
            print("\t" * (__tab_number + 3) + f"{mm}")
        print("\t" * (__tab_number + 2) + f"InitMethods : ")
        for im in obj.init_method:
            print("\t" * (__tab_number + 3) + f"{im}")
    print("\t" * (__tab_number + 1) + f"Methods : ")
    print("\t" * (__tab_number + 2) + f"StaticMethods : ")
    for sm in obj.static_method:
        print("\t" * (__tab_number + 3) + f"{get_function_signature(obj.get(sm))}")
    print("\t" * (__tab_number + 2) + f"ClassMethods : ")
    for cm in obj.class_method:
        print("\t" * (__tab_number + 3) + f"{get_function_signature(obj.get(cm))}")
    print("\t" * (__tab_number + 2) + f"InstanceMethods : ")
    for im in obj.instance_method:
        print("\t" * (__tab_number + 3) + f"{get_function_signature(obj.get(im))}")
    print("\t" * (__tab_number + 1) + f"Attributes : ")
    print("\t" * (__tab_number + 2) + f"ClassAttributes : ")
    for ca in obj.class_attribute:
        print("\t" * (__tab_number + 3) + f"{ca} ({type(getattr(value, ca)).__name__}): ", end='')
        if type(getattr(value, ca)) in [list, tuple, set, dict]:
            display_iterable(getattr(value, ca), __tab_number=__tab_number + 3)
        else:
            print(f"{getattr(value, ca)}")
    print("\t" * (__tab_number + 2) + f"InstanceAttributes : ")
    for ia in obj.instance_attribute:
        print("\t" * (__tab_number + 3) + f"{ia} ({type(getattr(value, ia)).__name__}): ", end='')
        if type(getattr(value, ia)) in [list, tuple, set, dict]:
            display_iterable(getattr(value, ia), __tab_number=__tab_number + 3)
        else:
            print(f"{getattr(value, ia)}")
    print("\t" * (__tab_number + 2) + f"Properties : ")
    for pa in obj.property_attribute:
        print("\t" * (__tab_number + 3) + f"{pa} ({type(getattr(value, pa)).__name__}): ", end='')
        if type(getattr(value, pa)) in [list, tuple, set, dict]:
            display_iterable(getattr(value, pa), __tab_number=__tab_number + 3)
        else:
            print(f"{getattr(value, pa)}")


def display_iterable(iterable, *, __tab_number=0):
    """Displays iterables in a human-readable way.

    Parameters:
        iterable (list or tuple or set or dict) : An iterable.
        __tab_number (int) : The default number of tabs to put in front of the printout.

    Return:
        None : Print the iterable to the console
    """
    t = type(iterable)
    s = '[]' if t == list else '()' if t == tuple else '{}'

    print(f"{s[0]}")
    for i in range(len(iterable)):
        if isinstance(iterable, dict):
            key = list(iterable.keys())[i]
            value = list(iterable.values())[i]
        else:
            key = i
            value = list(iterable)[i]

        print("\t" * __tab_number + f"\t {repr(key)} ({type(value).__name__}): ", end='')
        if type(value) in [list, tuple, set, dict]:
            display_iterable(value, __tab_number=__tab_number+1)
        else:
            print(value)
    print("\t"*__tab_number + s[1])


def enter(__prompt='', __type=int):
    """This function allows to input any type.

    Types:
    ------
    - bool
    - complex
    - float
    - int
    - list
    - set
    - slice
    - str

    Parameters:
        __prompt (str) : Text to print before recovery.
        __type (type) : The type to recover.

    Raises:
        TypeError : If __type is not in return type.

    Return:
        Any : The input in the requested type.
    """
    if __type not in [
        bool, complex, float, int, list, set, slice, str
    ]:
        raise TypeError(f'{__type} is not a possible type.')
    var: str = input(__prompt)
    while True:
        try:
            '''  '''
            if __type == bool:
                if var.lower() in [
                    "yes", "是的", "हां", "sí", "si", "نعم", "হ্যাঁ", "oui", "да", "sim", "جی ہاں",
                    "y", "1", "true"
                ]:
                    return True
                elif var.lower() in [
                    "no", "不", "नहीं", "no", "لا", "না", "non", "нет", "não", "nao", "نہیں",
                    "n", "0", "false"
                ]:
                    return False
                else:
                    raise ValueError(f"could not convert string to bool: '{var}'")
            return __type(var)
        except ValueError:
            print(f"\"{var}\" is not the type {__type.__name__}")
            var: str = input(__prompt)


def last_iteration(list_of_think, obj):
    """Return the index of the last iteration on list.

    Parameters:
        list_of_think (str/list/tuple) : The searched iteration.
        obj (Any) : The object to search in.

    Return:
        int : The index of last iteration.
    """
    if isinstance(list_of_think, list):
        try:
            list_of_think.reverse()
            i = list_of_think.index(obj) + 1
            return len(list_of_think) - i
        except ValueError:
            return -1
    else:
        mem = []
        try:
            while obj in list_of_think:
                mem += [list_of_think[0]]
                list_of_think = list_of_think[1:]
        except TypeError:
            pass
        return len(mem) - 1


def menu(choices, title, *, can_back=False, prompt='>> ', desc=None, name_back='Back'):
    """Create a menu.

    Parameters:
        choices (list) : The liste of choice.
        title (str) : Title of menu.
        desc (str) : Description of menu.
        prompt (str) : The prompt before choice.
        can_back (bool) : The menu displays the choice of return at 0)?
        name_back (str) : Name of back.

    Return:
        int: The index of choice with 'Back' in index 0 and other index + 1.
    """

    """
    Model:
            ╔═════════════╗         
    ╔═══════╣  Menu name  ╠════════╗
    ║       ╚═════════════╝        ║
    ║   ┌──────────────────────┐   ║
    ║   │ Description of menu  │   ║
    ║   └──────────────────────┘   ║
    ║                              ║
    ║ ┌───┐ ┌────────────────┐     ║
    ║ │ 1 ├─┤ Text of choice │     ║
    ║ └───┘ └────────────────┘     ║
    ║ ┌───┐ ┌────────────────┐     ║
    ║ │ 2 ├─┤ Text of choice │     ║
    ║ └───┘ └────────────────┘     ║
    ╟------------------------------╢
    ║ ┌───┐ ┌────────────────────┐ ║
    ║ │ 0 ├─┤ Return choice text │ ║
    ║ └───┘ └────────────────────┘ ║
    ╚══════════════════════════════╝
    """

    def choice_button(num, texte):
        """Create a button of choice"""
        ln = length_num
        lt = length_choice

        num = position('right', str(num), ln, ' ')
        texte = position('center', texte, lt, ' ')

        u = position('left', f" ┌──" + ("─" * ln) + "┐ ┌──" + ("─" * lt) + "┐ ", largeur - 2, ' ')
        m = position('left', f" │ {num} ├─┤ {texte} │ ", largeur - 2, ' ')
        b = position('left', f" └──" + ("─" * ln) + "┘ └──" + ("─" * lt) + "┘ ", largeur - 2, ' ')

        return (
                "║" + u + "║\n" +
                "║" + m + "║\n" +
                "║" + b + "║"
        )

    largeur_choice = max([len(desc) for desc in choices]) if len(choices) > 0 else 0
    largeur_desc = max([len(word) for word in desc.split()]) if desc else 0
    length_num = len(str(len(choices)))
    largeur = max(
        18,
        len(f"╔══╣  {title}  ╠══╗"),
        len(f"║ │ {' ' * largeur_desc} │ ║"),
        len(f"║ │ {' ' * length_num} ├─┤ {' ' * largeur_choice} │ ║"),
        len(f"║ │ 0 ├─┤ {name_back} │ ║"),
    )
    length_choice = largeur - 13 - len(str(len(choices)))

    back_button = (
            "║" + position('left', f" ┌───┐ ┌─{'─' * len(name_back)}─┐ ", largeur - 2, ' ') + "║\n" +
            "║" + position('left', f" │ 0 ├─┤ {name_back} │ ", largeur - 2, ' ') + "║\n" +
            "║" + position('left', f" └───┘ └─{'─' * len(name_back)}─┘ ", largeur - 2, ' ') + "║"
    )

    # =-= =-= =< Menu >= =-= =-=
    print(position('center', f"╔══{'═' * len(title)}══╗", largeur, ' '))
    print("╔" + position('center', f"══╣  {title}  ╠══", largeur - 2, '═') + "╗")
    print("║" + position('center', f"╚══{'═' * len(title)}══╝", largeur - 2, ' ') + "║")

    if desc:
        desc = desc.replace("\n", " ¤linebreak$ ")
        desc_lines = ['']
        for word in desc.split():
            if word == '¤linebreak$':
                desc_lines.append('')
            elif len(desc_lines[-1]) > 0:
                if len(f"║ │ {desc_lines[-1]} {word} │ ║") > largeur:
                    desc_lines.append(word)
                else:
                    desc_lines[-1] += f" {word}"
            else:
                desc_lines[-1] = word

        print(f"║ ┌{'─' * (largeur - 6)}┐ ║")
        for line in desc_lines:
            print(f"║ │ {line.center(largeur - 8, ' ')} │ ║")
        print(f"║ └{'─' * (largeur - 6)}┘ ║")
        print(f"║{' ' * (largeur - 2)}║")

    i = 1
    for choice in choices:
        print(choice_button(i, choice))
        i += 1

    if can_back:
        print("╟" + '-' * (largeur - 2) + "╢")
        print(back_button)
    print("╚" + '═' * (largeur - 2) + "╝")

    chx = enter(prompt + ' ')
    while chx not in range(0 if can_back else 1, len(choices) + 1):
        print(f'"{chx}" not in possibility')
        chx = enter(prompt + ' ')
    return chx


def position(pos, txt, length, fill):
    """Push in the position the text with correct length.

    Parameters:
        pos (str) : left, center or right.
        txt (str) : The text to move.
        length (int) : The length of the final string.
        fill (str) : String filler.

    Returns:
        str : The string filled.
    """
    if pos == 'center':
        return txt.center(length, fill)
    else:
        while len(txt) < length:
            if pos == 'right':
                txt = fill + txt
            else:
                txt += fill
    return txt


def replace_last(sub_string, new_string, string):
    """Replaces the last iteration of the substring entered with the string chosen in the quoted string.

    Parameters:
        sub_string (str) : The substring entered.
        new_string (str) : The string chosen.
        string (str) : The quoted string.

    Return:
        str : The quoted string with the last iteration of the substring replaced by the chosen string.
    """
    li = last_iteration(string, sub_string)
    if li is None:
        return string
    return string[0:li] + new_string + string[li + len(sub_string):]


def space_number(number, *, separator=' '):
    """Separate with character defines the number entered every 3 digits.

    Parameters:
        number (int, float) : A value.
        separator (str) : A character.

    Returns:
        str : A string of number separate.
    """
    if isinstance(number, int):
        number_list = list(str(number))
        txt = ""
        i = 0
        while len(number_list) != 0:
            if i == 3:
                i = 0
                txt = separator + txt
            txt = number_list.pop() + txt
            i += 1
        return txt
    else:
        return space_number(int(number), separator=separator) + '.' + str(number).split('.')[1]
