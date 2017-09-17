from collections import defaultdict

def dots2utf8(dots):
     """ braille dots to utf-8 hex codes"""
     code=0
     for number in dots:
          code += 2**(int(number)-1)
     return hex(0x2800 + code)     




# german ascii to braille dots
ascii2dots={
     #'\s':'0',
     'A':'1',
     'B':'12',
     'C':'14',
     'D':'145',
     'E':'15',
     'F':'124',
     'G':'1245',
     'H':'125',
     'I':'24',
     'J':'245',
     'K':'13',
     'L':'123',
     'M':'134',
     'N':'1345',
     'O':'135',
     'P':'1234',
     'Q':'12345',
     'R':'1235',
     'S':'234',
     'T':'2345',
     'U':'136',
     'V':'1236',
     'X':'1346',
     'Y':'13456',
     'Z':'1356',
     '&':'12346',
     '%':'123456',
     '{':'12356',
     '~':'2346',
     '}':'23456',
     '1':'16',
     '2':'126',
     '3':'146',
     '4':'1456',
     '5':'156',
     '6':'1246',
     '7':'12456',
     '8':'1256',
     '9':'246',
     'W':'2456',
     ',':'2',
     ';':'23',
     ':':'25',
     '/':'256',
     '?':'26',
     '+':'235',
     '=':'2356',
     '(':'236',
     '*':'35',
     ')':'356',
     '.':'3',
     '-':'36',
     '\\':'34',
     '0':'346',
     '@':'345',
     '#':'3456',
     '"':'4',
     '!':'5',
     '>':'45',
     '$':'46',
     '_':'456',
     '<':'56',
     '\'':'6'
}
def dots2html(dot_nr):
    """returns html encoded utf-8 char for braille char"""
    return '&#x{};'.format(dots2utf8(dot_nr))

def bme_print_table_german():
     """German table for braille music editor 2"""     
     for char, dots in sorted(ascii2dots.items()):
          code = ord(char)
          if code>60 and code<95:
               code=code+32
          print(dots+'='+str(code))

def print_utf8_chars():
     for char, dots in ascii2dots.items():
          code = dots2utf8(dots)
          print(char,chr(int(code, 16)),sep=' ',end='  ')

# tiefgestellte (inferior) Zahlen in Blindenschrift umwandeln
inumbers2ascii = {
     '1' : ',', '2' : ';', '3' : ':',
     '4' : '/', '5' : '?', '6' : '+',
     '7' : '=', '8' : '(', '9' : '*',
     '0' : ')'
}
    
notes2ascii=defaultdict(dict)

notes2ascii['a']['whole']='~'
notes2ascii['a']['half']='s'
notes2ascii['a']['quarter']='9'

notes2ascii['b']['whole']='}'
notes2ascii['b']['half']='t'
notes2ascii['b']['quarter']='w'

notes2ascii['c']['whole']='y'
notes2ascii['c']['half']='n'
notes2ascii['c']['quarter']='4'

notes2ascii['d']['whole']='z'
notes2ascii['d']['half']='o'
notes2ascii['d']['quarter']='5'

notes2ascii['e']['whole']='&'
notes2ascii['e']['half']='p'
notes2ascii['e']['quarter']='6'

notes2ascii['f']['whole']='%'
notes2ascii['f']['half']='q'
notes2ascii['f']['quarter']='7'

notes2ascii['g']['whole']='{'
notes2ascii['g']['half']='r'
notes2ascii['g']['quarter']='8'


notes2ascii['a']['eighth']='i'
notes2ascii['a']['16th']='~'
notes2ascii['a']['32nd']='s'

notes2ascii['b']['eighth']='j'
notes2ascii['b']['16th']='}'
notes2ascii['b']['32nd']='t'

notes2ascii['c']['eighth']='d'
notes2ascii['c']['16th']='y'
notes2ascii['c']['32nd']='n'

notes2ascii['d']['eighth']='e'
notes2ascii['d']['16th']='z'
notes2ascii['d']['32nd']='o'

notes2ascii['e']['eighth']='f'
notes2ascii['e']['16th']='&'
notes2ascii['e']['32nd']='p'

notes2ascii['f']['eighth']='g'
notes2ascii['f']['16th']='%'
notes2ascii['f']['32nd']='q'

notes2ascii['g']['eighth']='h'
notes2ascii['g']['16th']='{'
notes2ascii['g']['32nd']='r'


notes2ascii['a']['64th']='9'
notes2ascii['a']['128th']='i'
notes2ascii['a']['256th']='<2'

notes2ascii['b']['64th']='w'
notes2ascii['b']['128th']='j'
notes2ascii['b']['256th']='<2'

notes2ascii['c']['64th']='4'
notes2ascii['c']['128th']='d'
notes2ascii['c']['256th']='<2'

notes2ascii['d']['64th']='5'
notes2ascii['d']['128th']='e'
notes2ascii['d']['256th']='<2'

notes2ascii['e']['64th']='6'
notes2ascii['e']['128th']='f'
notes2ascii['e']['256th']='<2'

notes2ascii['f']['64th']='7'
notes2ascii['f']['128th']='g'
notes2ascii['f']['256th']='<2'
 
notes2ascii['g']['64th']='8'
notes2ascii['g']['128th']='h'
notes2ascii['g']['256th']='<2'


rests2ascii = {
     'maxima' : 'm>c>c>cm',
     'longa': 'm>c>cm',
     'brevis' :'m>cm',
     'whole' : 'm', 'half' : 'u', 'quarter': 'v',
     'eighth': 'x', '16th' : 'm', '32nd' : 'u',
     '64th':  'v', '128th': 'x',
     'faulenzer-single': '=',
     'faulenzer-normal': '=',
     'faulenzer-double': '='
}

octave2ascii={
     '0': '""', '1': '"', '2': '>',
     '3': '_',  '4': '!',  '5': '$',
     '6': '<',  '7': '\'', '8': '\'\''
}
note_types_bmml={
     'whole' :  'whole_or_16th',
     'half'  :  'half_or_32nd',
     'quarter': 'quarter_or_64th',
     'eighth':  '8th_or_128th',
     '16th':   'whole_or_16th',
     '32nd':   'half_or_32nd',
     '64th':   'quarter_or_64th',
     '128th':    '8th_or_128th'
}

fifths2ascii = {
     '0': '',
     '-1': '2',
     '-2': '22',
     '-3': '222',
     '-4': '#d2',
     '-5': '#e2',
     '-6': '#f2',
     '-7': '#g2',
     '1': '3',
     '2': '33',
     '3': '333',
     '4': '#d3',
     '5': '#e3',
     '6': '#f3',
     '7': '#g3'
}     

#Intervallzeichen in Blindennoten darstellen
intervals2ascii = {
     'isecond' : '|', 'ithird' : '0', 'ifourth' :  '#',
     'ififth' :  '*', 'isixth' : ')', 'iseventh' : ':',
     'ioctave' : '-',
     'iseconds' : '||', 'ithirds' : '00', 'ifourths' :  '##',
     'ififths' :  '**', 'isixths' : '))', 'isevenths' : '::',
     'ioctaves' : '--'
}

def octave2utf8(o_number):
     out = ''
     for char in octave2ascii[str(o_number)]:
          out=out+dots2html(ascii2dots[char])
     return out          

