# <p id="title">LassaLib</p>

Convenient function set.

Python library by LassaInora.

--------
## Summary

- **[Links](#links)**
- **[Contacts](#contact)**
- **[Methods](#methods)**
  - ***[enter(__prompt: str = '', __type: type = int) -> typing.Any](#enter)***
  - ***[str_object(obj: typing.Any) -> str](#str_object)***
  - ***[show_value(value: typing.Any, tab_number: int = 0) -> None](#show_value)***
  - ***[space_number(number: typing.Union[int, float], spacing: str = ' ') -> str](#space_number)***
  - ***[last_iteration(iteration_text: str, txt: str) -> int | None](#last_iteration)***
  - ***[replace_last(sub_string: str, new_string: str, string: str) -> str](#replace_last)***
--------

## <p id="links">Links</p>

- [Personal GitHub](https://github.com/LassaInora)
- [GitHub project](https://github.com/LassaInora/Timedate)
- [Website project](https://lassainora.fr/projet/librairies/Timedate)

## <p id="contact">Contacts</p>

- [Personal email](mailto:axelleviandier@lassainora.fr)
- [Professional email](mailto:lassainora@lassainora.fr)
--------
<p id="methods">Methods:</p>
-------

### <p id="enter">enter(__prompt: str = '', __type: type = int) -> typing.Any</p>

- This function allows to input any type.
  - __prompt (str) : Text to print before recovery.
  - __type (type) : The type to recover.

+ Can return:
  + Any type.

### <p id="str_object">str_object(obj: typing.Any) -> str</p>

- Create a string of all info about an object regardless of its class.
  - obj (Any) : An object from Any type or class.

+ Can return:
  + str

### <p id="show_value">show_value(value: typing.Any, tab_number: int = 0) -> None</p>

- Prints in the terminal all the elements of a list, a dictionary or a tuple and its sub-elements.</br> 
  Prints in the terminal the other types and class.
  - value (Any) : A value of any type or class.
  - tab_number (int) : The default number of tabs to put in front of the printout.

+ Can return:
  + None

### <p id="space_number">space_number(number: typing.Union[int, float], spacing: str = ' ') -> str</p>

- Separate with character defines the number entered every 3 digits.
  - number (int or float) : A value.
  - spacing (str) : A character.

+ Can return:
  + str

### <p id="last_iteration">last_iteration(iteration_text: str, txt: str) -> int | None</p>

- Return the index of the last iteration on string.
  - iteration_text (str) : The searched iteration
  - txt (str) : The text to search in.

+ Can return:
  + int
  + None

### <p id="replace_last">replace_last(sub_string: str, new_string: str, string: str) -> str</p>

- Replaces the last iteration of the substring entered with the string chosen in the quoted string.
  - sub_string (str) : The substring entered.
  - new_string (str) : The string chosen.
  - string (str) : The quoted string.

+ Can return:
  + str