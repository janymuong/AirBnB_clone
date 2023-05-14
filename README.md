# AirBnB clone - The console

<div align="center">
 <img src="./hack/hbnb_console.png" height="150" width="600" />
</div>

Part: `0x00 - the console` <br/>
This is the first part of the `AirBnB Clones` project series.

This is a clone of the [AirBnB website](https://www.airbnb.com/). This specific part partly covers these concepts:  
`console(command interpreter)`, `Python Object Oriented Programming(OOP)`, `file storage` etc.

---
### Basic Functionality

`Specifications`:
```bash
    - create data model - Python Object Orientation.
    - manage (create, update, destroy, etc) objects via a console / command interpreter
    - store and persist objects to a file (JSON file)
```
The first piece is to manipulate a storage system. This storage engine will give us an abstraction between model ***objects*** and ***storage(persisting to storage)***. This means: from the console code (the developed command interpreter itself) and from the front-end and `RESTfull API` (built later on in subsequent series).

This abstraction will also allow you to change the type of storage easily without updating all of your codebase eg using a **storage db**.<br/>
The console will be a tool to validate the storage engine...

## File Hierarchy:
This section is all file info.
```bash
.
├── AUTHORS - Docker specified formatted file for contributors
├── README.md - project documentation.
├── console.py - single-use command interpreter(uses Python `cmd` module).
├── models/ - the main driver of the project; lays out Python Object Orientation, initialization,  serialization, (de)serialization etc.
│   ├── __init__.py - effectively make a `Python` Package out of these modules, unique FileStorage instance for app
│   ├── base_model.py  - includes base (class) model ; for subclassing/inheritance - is the superclass.
│   ├── user.py - sample file with subclass of BaseModel(from module base_model)
│   ├── engine/ - abstracted storage engine/system for persisting data.
│   │   ├── __init__.py - effectively make a `Python` Package out of these modules
│   │   └── file_storage.py - module with methodes meant to interact with file storage(read from/write to JSON file), and models
└── tests/ - directory for unit testing, test cases/test suites etc.
    ├── __init__.py - effectively make a `Python` Package out of these modules, for Python test discovery.
    └── test_models/ - files that test models eg test_base_model.py, test_user.py, test_review.py
        └── __init__.py - effectively make a `Python` Package out of these modules, for Python test discovery.
```

## Command Interprter
> `command-line interface`<br/>
> a shell implementation that uses the `Python` module `cmd`, which provides a simple framework for writing line-oriented command interpreters.


### `usage`
- Supposed theoretical behavior in interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

- Supposed behavior in non-interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Actual `Shell` Behavior:
Is a `CRUD` simulated behavior - operations on objects in command-line.

> **Note**: <br/>
> start interpreter in interactive mode: `./console.py`;- quit interpreter: type `quit` or `EOF`, or press `Ctrl + D` <br/>
> sample interpreter features: `create`, `show`, `update`, `destroy`, etc<br/>  

> #### command syntax:  
>> create a new object: `$ create ClassName`, for example to create a base instance do `$ create BaseModel`<br/>
>> display objects from storage: `$ all`<br/>
>> destroy/delete objects from storage: `$ destroy ClassName valid-id`<br/>
>> use the `help` menu as a manual/reference: `$ help destroy`<br/>

> see the shell session below for reference on how to use the command interpreter/console:
```bash
root@HP:/alx-SE/AirBnB_clone# ./console.py
(hbnb) show User e57df8d1-1910-491d-b1ed-0166c102a3d9
[User] (e57df8d1-1910-491d-b1ed-0166c102a3d9) {'id': 'e57df8d1-1910-491d-b1ed-0166c102a3d9', 'created_at': datetime.datetime(2023, 5, 13, 10, 34, 49, 790134), 'updated_at': datetime.datetime(2023, 5, 13, 10, 34, 49, 790148), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}
(hbnb) show Use e57df8d1-1910-491d-b1ed-0166c102a3d9
** class doesn't exist **
(hbnb) all
["[BaseModel] (48b65c1f-9106-4113-8d37-cc7ab2d90ba6) {'id': '48b65c1f-9106-4113-8d37-cc7ab2d90ba6', 'created_at': datetime.datetime(2023, 5, 12, 14, 9, 49, 502137), 'updated_at': datetime.datetime(2023, 5, 12, 14, 9, 49, 502161), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (2d4dd2fd-6266-4c1b-8a65-727b641d83e3) {'id': '2d4dd2fd-6266-4c1b-8a65-727b641d83e3', 'created_at': datetime.datetime(2023, 5, 12, 14, 10, 7, 226227), 'updated_at': datetime.datetime(2023, 5, 12, 14, 10, 7, 226261), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (33595b8b-8ee1-43d5-ab35-c777565628b4) {'id': '33595b8b-8ee1-43d5-ab35-c777565628b4', 'created_at': datetime.datetime(2023, 5, 12, 14, 10, 22, 464350), 'updated_at': datetime.datetime(2023, 5, 12, 14, 10, 22, 464414), 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (b9c7dd00-15d9-4069-964f-05de4a22bc32) {'id': 'b9c7dd00-15d9-4069-964f-05de4a22bc32', 'created_at': datetime.datetime(2023, 5, 12, 20, 24, 40, 392247), 'updated_at': datetime.datetime(2023, 5, 12, 20, 24, 40, 392346)}", "[User] (458405dd-1c31-486e-a306-bc232443dfaf) {'id': '458405dd-1c31-486e-a306-bc232443dfaf', 'created_at': datetime.datetime(2023, 5, 13, 10, 34, 49, 789439), 'updated_at': datetime.datetime(2023, 5, 13, 10, 34, 49, 789513), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (e57df8d1-1910-491d-b1ed-0166c102a3d9) {'id': 'e57df8d1-1910-491d-b1ed-0166c102a3d9', 'created_at': datetime.datetime(2023, 5, 13, 10, 34, 49, 790134), 'updated_at': datetime.datetime(2023, 5, 13, 10, 34, 49, 790148), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}"]
(hbnb) stuff BaseModel
*** Unknown syntax: stuff BaseModel
(hbnb) help update
update
        updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        usage: update <class name> <id> <attribute name> "<attribute value>"

(hbnb)
(hbnb) create BaseModel
2956e421-eecf-4ac7-bf49-7f493646738f
(hbnb) EOF

root@HP:/alx-SE/AirBnB_clone#
```

## Python Unit Tests
> uses the `unittest` module for testing.<br/>
> `path` to test files/for test coverage - directory: `tests/test_models`

Running tests using Python test discovery...
```bash
# execute tests using this command for all tests(pwd == AirBnB root dir): 
$ python3 -m unittest discover tests
# test file by file by using this command: 
$ python3 -m unittest tests/test_models/test_base_model.py
```

## Authors
You can find a list of contributors/project developers in the [authors](./AUTHORS) file.  
If you like this project, take us out for `coffee` :)
