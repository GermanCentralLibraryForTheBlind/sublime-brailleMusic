# sublime-brailleMusic
Sublime Text 3 syntax support for Ascii- Braille Music text files
![Sublime Braille Music with theme Monokai][screenshot]
[screenshot]:/screenshot_monokai.png
             "Sublime Braille Music with theme Monokai"
## Introduction
> Braille music is a Braille code that allows music to be notated using Braille cells so music can be read by visually impaired musicians. 
> 
> -- <cite>[From Wikpedia](https://en.wikipedia.org/wiki/Braille_music)</cite>

This is a Sublime Text 3 - package for sighted people to help them to read, produce or correct music scores for blind
or visual impaired people.

## Features
- syntax highlighting
- shows scope name under the cursor (like *note>accidental*) in the status bar
### Configuration
- loads specific settings for braille editing (ruler for end-of-line, tab-size etc.), see *Braille.sublime-settings*
### Commands
- align commands in relation to the setted ruler ("line width") 
  in the plugins config (default: 36):
  - Center: *Ctrl+Alt+c*
  - Right: *Ctrl+r*
  - Headline: *Ctrl+Alt+u* = center + underline
- font switcher: *F10* : toggle between normal and braille font
  (default: blistabraille6+)

### TODO:
- see [Issues](https://github.com/GermanCentralLibraryForTheBlind/sublime-brailleMusic/issues?q=is%3Aopen+is%3Aissue+label%3Aenhancement)


## Installation
- Download and install [Sublime Text](https://www.sublimetext.com/3) for your platform (to be fair, please register!)
- Download, unpack this repo and copy it to your Packages folder, i.e. situated under windows in *%appdata%\Sublime Text 3\Packages*
(the package is not yet listed in package control):

  `git clone https://github.com/GermanCentralLibraryForTheBlind/sublime-brailleMusic.git Braillemusic`

- for Braille- Music files, set syntax to "Braille"
- in order to use the font toggler, install a braille font,
  like [*Blistabraille*](http://www.braille.ch/blista-d.htm)
- for examples, check the 'examples' subfolder folder
- until we deliver an own color scheme, please install the "Phix Dark Color Scheme" over Package Control (recommended theme: "Theme Soda dark"), the default theme "Monokai" works decent as well
## Particular Syntax requirements for ASCII Braille Music Files
**Look at the examples!**
- all characters must be lower case
- Music prefixes (e.g key or left/right hand) **must** be preceded by at least one whitespace 
- Music prefixes with ending char containing braille points 4-6 (e.g piano LH/RH) **must not** be followed by a char containing Braille- points  1 to 3
- Following lines in the staff **must not** be preceded by whitespace or tab
- particular order of prefixes/ postfixes in the notes required like defined:
    
        ({{value_sign}})?({{phrase_start}})?({{ornaments}})?({{pedal_on}})?((?:{{accent}})+)?''?({{accidental}})?({{octave}})?({{note}})(\.{,2})((?:{{finger}})+)?((?:{{bow_after}}){,2})?((?:{{interval}})+)?({{fermate}})?({{phrase_end}})?({{pedal_off}})?
 - in general we follow the standards as shown at http://braille.ch  
   especially those defined in the *New International Manual
of Braille Music Notation*

# WARNING
This software is still under development and optimized for use at the [German Central Library for the blind and visual impaired](http://dzb.de).
It may not work with your own braille- music- text files.
Especially the current builds are made for german ascii braille and may not work with other language character sets.

