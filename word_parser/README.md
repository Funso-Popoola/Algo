# String Parser
A basic tool to parse strings; verifying that it contains chunks of existent words meshed together.

The tool allows user to determine the validity of a bunch of words stringed together by removing the spaces in between a 
valid sentence.

Well, the tool doesn't ascertain the semantic validity of the sentence produced.

## Dependencies
To spell check words using a dictionary, for example, the english dictionary:
this tool depends on ``PyEnchant`` https://pythonhosted.org/pyenchant/

## Basic Usage
It's more of a commandline tool.
Inputs and preferences are provided via the terminal.
``$ python main.py [-s [STRING_TO_BE_VALIDATED]] [-o [SPELL_CHECK_OPTION]]``

Spell Check Options: Use 0 to spell check using a Dictionary 
                     and 1 using a list of curated words (which you can always alter)

The default string is "darkskinneduglygoodlookingrichgeneroussmalldickcumsintenminutesorless".
The default spell check option is 

To check for the validity of a string such as "icecreamismybestdessert", for instance, use
 ``$ python main.py -s icecreamismybestdessert``

Basic usage can always be looked up by using the help line :)
``$ python main.py --help``

