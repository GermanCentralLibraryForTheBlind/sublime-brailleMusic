import sublime
import sublime_plugin
from .data.tables import *

def plugin_loaded():
    pass


class ViewUtils(object):
    @property
    def cursor(self):
        return self.view.sel()[0]

    @property
    def cur_line_region(self):
        """get line region at (first cursor)"""
        return self.view.line(self.cursor)

    @property 
    def cur_line(self):
        return self.view.substr(self.cur_line_region)
 
    @property    
    def line_width(self):
        return self.view.settings().get('rulers')[0]

    @property
    def cur_scope_name(self):
        """Scope name at first cursor"""
        return self.view.scope_name(self.cursor.b).strip()



class AlignCommands(ViewUtils):
   
    def center_current_line(self):
        return '{:^{width}}'.format(self.cur_line.strip(), width=self.line_width)    
    
    def right_align_current_line(self):
        return '{:>{width}}'.format(self.cur_line.strip()+'  ', width=self.line_width)                

    def left_align_current_line(self):
        return '{:<{width}}'.format(self.cur_line.strip(), width=self.line_width)

    def underline(self, char=':'):
        return '\n' + '{:^{width}}'.format(char*7, width=self.line_width)


###### Commands  #########
class BrailleHeadlineCommand(sublime_plugin.TextCommand, AlignCommands):
    """
        Make centered headline with underline chars
    """
    def run(self, edit, underline_char=':'):
        self.view.replace(edit,
        self.cur_line_region,
        self.center_current_line()+self.underline(underline_char)
        )
       

class BrailleCenterCommand(sublime_plugin.TextCommand, AlignCommands):
    """
        Center current line
    """
    def run(self, edit):
        self.view.replace(edit,
            self.cur_line_region, 
            self.center_current_line()
            )

class BrailleRightAlignCommand(sublime_plugin.TextCommand, AlignCommands):
    """
        Right align current line
    """
    def run(self, edit):
        self.view.replace(edit,
            self.cur_line_region, 
            self.right_align_current_line()
            )        

class BrailleLeftAlignCommand(sublime_plugin.TextCommand, AlignCommands):
    """
        Left align current line
    """
    def run(self, edit):
        self.view.replace(edit,
            self.cur_line_region,
            self.left_align_current_line()
            )     

class BrailleToggleFontCommand(sublime_plugin.TextCommand):
    """Toogle between normal and braille font"""
    default_font=''
    def run(self, edit):
        settings = self.view.settings()
        braille_font = settings.get('braille_font')
        if braille_font is not None:
            if settings.get('font_face') != braille_font:
                self.__class__.default_font = settings.get('font_face')
                settings.set("font_face", braille_font)
            else:
                settings.set("font_face", self.default_font)




#######Events##############

class BrailleStatus(sublime_plugin.EventListener, ViewUtils):
    """
        View relevant braille scope under the cursor in the status bar
    """
    def on_selection_modified_async(self, view):
        self.view = view
        if 'Braille' in view.settings().get('syntax'):
            cursor = view.sel()[0]
            #scope_name = view.scope_name(cursor.b).strip()
            scope_list = self.cur_scope_name.split(' ')
            showed_scope = self.get_relevant_scope_part(scope_list[-1])
            if len(scope_list)>2: 
                outer_scope = scope_list[-2]
                if outer_scope.endswith('braille') and outer_scope!=showed_scope and 'error' not in outer_scope:
                    showed_scope = self.get_relevant_scope_part(outer_scope) + '>' + showed_scope
                    current_scope_content = view.extract_scope(cursor.b)
            view.set_status(
                'current_scope', 
                showed_scope+'   '  #+view.substr(current_scope_content)+' '
                )
            # if showed_scope == 'note>note_name':
            #     view.set_status('current_scope_content',
            #     view.substr(cursor.b))
    def get_relevant_scope_part(self, scope):
        parts = scope.split('.')
        if parts[-2] in ['start','end','repeat']:
            return parts[-3]+'.'+parts[-2]
        else:
            return parts[-2]
            
    
class BrailleLineBreak(sublime_plugin.EventListener, ViewUtils):
    """docstring for BrailleLineBreak"""
  
    def on_modified_async(self, view):
        self.view = view
        if 'measure.end' in self.cur_scope_name:
            line_pos = self.cur_line_region.b-self.cur_line_region.a
            # if line_pos == self.line_width:
                # self.view.sel().clear()
                # self.view.sel().add(sublime.Region(self.cur_line_region.b+1, self.cur_line_region.b+1))
                # print(line_pos)





