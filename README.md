# sublime-brailleMusic
Sublime Text 3 syntax support for Ascii- Braille Music text files
![Screenshot](http://martinmueller.space/assets/images/sublime-brailleMusic.png)
## Introduction
> Braille music is a Braille code that allows music to be notated using Braille cells so music can be read by visually impaired musicians. 
> 
> -- <cite>[From Wikpedia](https://en.wikipedia.org/wiki/Braille_music)</cite>

This is a Sublime Text 3 - package for sighted people to help them to read, produce or correct music scores for blind
or visual impaired people.

## Features
- syntax highlighting
- shows scope name under the cursor (like *note.braille*) in the status bar
### TODO:
- show braille signs/contexts in popup


## Installation
- Download and install [Sublime Text](https://www.sublimetext.com/3) for your platform (to be fair, please register!)
- Download, unpack this repo and copy it to your Packages folder, i.e. situated under windows in *%appdata%\Sublime Text 3\Packages*
(the package is not yet listed in package control)
- for Braille- Music files, set syntax to "Braille"
- for examples, check the 'examples' subfolder folder
- until we deliver an own color scheme, please install the "Phix Dark Color Scheme" over Package Control (recommended theme: "Theme Soda dark")
## Particular Syntax requirements for ASCII Braille Music Files
- look at the examples:
  - whitespace indentation required for music
  - particular order of prefixes/ postfixes in the notes required like defined:
  
  
        ({{value_diff}})?({{phrase_start}})?({{ornaments}})?((?:{{accent}})+)?({{pedal_on}})?''?({{accidental}})?
        ({{octave}})?({{note}})(\.{,2})
        ((?:{{fingers}})+)?({{bow_after}})?({{interval}}+)?({{pedal_off}})?
 - in general we follow the standards as shown at http://braille.ch  
   especially those defined in the *New International Manual
of Braille Music Notation*

# WARNING
This is an alpha- version under heavy development, optimized for use at the [German Central Library for the blind and visual impaired](http://dzb.de).
It may not work with your own braille- music- text files.

