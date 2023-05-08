# AirBnB: the console

<div align="center">
 <img src="./hack/hbnb_console.png" height="250" />
</div>

Part: `The console` <br/>
This is the first part of the AirBnB project series.

This is a clone of the AirBnB website that partly covers these concepts: console(command interpreter), Python OOP, file storage etc.

---
### Basic Functionality

Specifications:
```bash
    - create data model - Python Object Orientation.
    - manage (create, update, destroy, etc) objects via a console / command interpreter
    - store and persist objects to a file (JSON file)
```
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and `RESTfull API` (built later in subsequent series), you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.<br/>
The console will be a tool to validate this storage engine...

## File Hierarchy:
This section is all file info.
```bash
├── README.md - project documentation.
├── AUTHORS - Docker specified formatted file for contributers
├── console.py - single-use command interpreter(uses Python `cmd` module).
├── models/ - the main driver of the project; lays out Python Object Orientation, initialization, (de)serialization etc.
│   ├── base_model.py - Includes base (class) models ; for subclassing/inheritance. Is the superclass.
│   ├── __init__.py - make a Python package out of this modules.
│   ├── user.py - sample file with subclass of BaseModel(from module base_model)
│   ├── name.py - placeholder for other files for classes that inherit from BaseModel
│   ├── engine/ - abstracted storage engine/system for persisting data.
│   │   ├── file_storage.py - JSON file(save serialized data).
│   │   ├── __init__.py - effectively make it Py-Package
├── tests/ - directory for unit testing, test cases/test suites etc.
└── * miscellaneous/anything else
```
## Command Interprter
> `command-line interface`<br/>
A shell implementation that uses the `Python` module `cmd`: which provides a simple framework for writing line-oriented command interpreters.


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

- ### Actual `Shell` Behavior:
Is a `CRUD` simulated behavior. Example of the interpreter features: [`create`, `update`, `destroy`, etc] - operations on objects in command-line.
```bash
# to be pasted here from commandline later on
```

## Authors
You can find a list of contributers/project developers in the [authors](./AUTHORS) file.
If you like this project, take us out for `coffee` :)

### [to be continued...]
