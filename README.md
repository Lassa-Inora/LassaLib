# LassaLib

#### _Convenient function set_

Author:
-------
- [Axelle (LassaInora) VIANDIER](mailto:axelleviandier@lassainora.fr)

License:
--------
- GNU General Public License v3.0

Version:
--------
- `3.0.1`

--------
## Summary

- **[Links](#links)**
- **[Contacts](#contacts)**
- **[Methods](#methods)**
  - ***[detailed_object(value, *, detailed=False, __tab_number=0)](#detailed_object)***
  - ***[display_iterable(iterable, *, __tab_number=0)](#display_iterable)***
  - ***[enter(__prompt='', __type=int)](#enter)***
  - ***[last_iteration(list_of_think, obj)](#last_iteration)***
  - ***[menu(choices, title, *, can_back=False, prompt='>> ', desc=None)](#menu)***
  - ***[position(pos, txt, length, fill)](#position)***
  - ***[replace_last(sub_string, new_string, string)](#replace_last)***
  - ***[space_number(number, *, separator=' ')](#space_number)***
--------

## Links

- [Personal GitHub](https://github.com/LassaInora)
- [GitHub project](https://github.com/LassaInora/LassaLib)
- [Website project](https://lassainora.fr/projets/librairies/LassaLib)
- [Pypi project](https://pypi.org/project/LassaLib/)

--------
## Methods

- ### detailed_object
  #### _Shows information about an object._

  Parameters:
  - value (Any) : A value of any type or class.
  - detailed (bool) : Should the function send detailed content?
  - __tab_number (int) : The default number of tabs to put in front of the printout.

- ### display_iterable
  #### _Displays iterables in a human-readable way._

  Parameters:
  - iterable (list or tuple or set or dict) : An iterable.
  - __tab_number (int) : The default number of tabs to put in front of the printout.

  Return:
  - None : Print the iterable to the console

- ### enter
  #### _This function allows to input any type._

  Parameters:
  - __prompt (str) : Text to print before recovery.
  - __tab_number (int) : The default number of tabs to put in front of the printout.

  Raise:
  - TypeError : If __type is not in return type.

  Return:
  - bool or complex or float or int or list or set or slice or str : Print the iterable to the console

- ### last_iteration
  #### _Return the index of the last iteration on list._

  Parameters:
  - list_of_think (str/list/tuple) : The searched iteration.
  - obj (Any) : The object to search in.

  Return:
  - int : The index of last iteration.

- ### menu
  #### _Create a menu._

  Parameters:
  - choices (list) : The liste of choice.
  - title (str) : Title of menu.
  - desc (str) : Description of menu.
  - prompt (str) : The prompt before choice.
  - can_back (bool) : Menu affiche back choice at 0)?

  Return:
  - int: The index of choice with 'Back' in index 0 and other index + 1.

- ### position
  #### _Push in the position the text with correct length._

  Parameters:
  - pos (str) : left, center or right.
  - txt (str) : The text to move.
  - length (int) : The length of the final string.
  - fill (str) : String filler.

  Return:
  - str : The string filled.

- ### replace_last
  #### _Replaces the last iteration of the substring entered with the string chosen in the quoted string._

  Parameters:
  - sub_string (str) : The substring entered.
  - new_string (str) : The string chosen.
  - string (str) : The quoted string.

  Return:
  - str : The quoted string with the last iteration of the substring replaced by the chosen string.

- ### space_number
  #### _Separate with character defines the number entered every 3 digits._

  Parameters:
  - number (int, float) : A value.
  - separator (str) : A character.

  Return:
  - str : A string of number separate.
