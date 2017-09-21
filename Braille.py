import sublime
import sublime_plugin

def plugin_loaded():
    pass

class AlignCommand(object):
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
        

    def center_current_line(self):
        return '{:^{width}}'.format(self.cur_line.strip(), width=self.line_width)    
    
    def right_align_current_line(self):
        return '{:>{width}}'.format(self.cur_line.strip()+'  ', width=self.line_width)                

    def left_align_current_line(self):
        return '{:<{width}}'.format(self.cur_line.strip(), width=self.line_width)

    def underline(self, char=':'):
        return '\n' + '{:^{width}}'.format(char*7, width=self.line_width)

class BrailleHeadlineCommand(sublime_plugin.TextCommand, AlignCommand):
    """
        Make centered headline with underline chars
    """
    def run(self, edit, underline_char=':'):
        self.view.replace(edit,
        self.cur_line_region,
        self.center_current_line()+self.underline(underline_char)
        )
       

class BrailleCenterCommand(sublime_plugin.TextCommand, AlignCommand):
    """
        Center current line
    """
    def run(self, edit):
        self.view.replace(edit,
            self.cur_line_region, 
            self.center_current_line()
            )

class BrailleRightAlignCommand(sublime_plugin.TextCommand, AlignCommand):
    """
        Right align current line
    """
    def run(self, edit):
        self.view.replace(edit,
            self.cur_line_region, 
            self.right_align_current_line()
            )        

class BrailleLeftAlignCommand(sublime_plugin.TextCommand, AlignCommand):
    """
        Left align current line
    """
    def run(self, edit):
        self.view.replace(edit,
            self.cur_line_region,
            self.left_align_current_line()
            )                


class BrailleStatus(sublime_plugin.EventListener, AlignCommand):
    """
        View relecant braille scope under the cursor in the status bar
    """
    def on_selection_modified(self, view):
        cursor = view.sel()[0]
        scope_name = view.scope_name(cursor.b).strip()
        self.scope_list = scope_name.split(' ')
        if (self.scope_list and (self.scope_list[0] == 'text.braille')):
            showed_scope = self.scope_list[-1]
            if len(self.scope_list)>2 and self.scope_list[-2].endswith('braille') and self.scope_list[-2]!=showed_scope:
                showed_scope = self.scope_list[-2] + ' ' + showed_scope
            current_scope_content = view.extract_scope(cursor.a)
            view.set_status(
                'current_scope_content', 
                showed_scope+' '+view.substr(current_scope_content)+' '
                )

    