# Cheat Sheet

reserved words
----------------

* `next` is a reserved word that calls a class's  __next__() iterator method, use `next_` instead for naming in say 
  linked lists.


basics
-------
* Doc comments use set of triple quotes (`"""`) AFTER the beginning of the function
* use `is not None` and not something like `not None` or `!= None`
* you can only chain things if he method returns something like `self`.. ie. `Node("A").append("B").append("C")`


classes
--------

* Don't forget that methods of a class start with `self` as the first parameter
* Classes start with `class` instead of `def` and take `object` as a parameter by default
* Classes inheriting from another would replase `object` with the class being inherited.
* Only add class variables if you want them to be shared across class instances, otherwise set them in `__init__`
* As of python 2.2, inherit classes from `object` which gives them `.super(ClassType, self)`(2.7) functionality.
* Creation methods
    * `__new__(cls, )` - rarely used, but can be used to reuse class instances.
    * `__init__(self, *args)` (constructor) - very common. Runs after `__new__()` if it created an instance.
    * `__del__(self)` (destructor) - can be used to do some cleanup when a class is deleted, ie linked list.
    * `__str__(self)` A string representation .. used when `str(myclass)` is called.
    * Find more details at https://docs.python.org/2/reference/datamodel.html#basic-customization

dicts
-----

* remove an item using `del mydict[key]` or `mydict.pop(key, None)` if you want to get the value at the same time.
* to check if a key is defined, use `mydict.key_exists(key)` or `mydict.get(key)` which will return `None`.
* to add an item to a dict, use `mydict[new_key] = new_item`
