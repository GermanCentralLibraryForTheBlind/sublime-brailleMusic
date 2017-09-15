import sublime
import sublime_plugin

def plugin_loaded():
    pass
    # settings = sublime.load_settings('Braille.sublime-settings')
    # sublime.window.view.settings().set('tab_size', settings.get('tab_size'))

class AlignCommand():
    @property
    def cur_line_region(self):
        """get line region at (first cursor)"""
        return self.view.line(self.view.sel()[0])

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

class BrailleHeadlineCommand(sublime_plugin.TextCommand, AlignCommand):
    """
        Überschrift zentrieren und mit '::::::' unterstreichen
    """
    def run(self, edit):
        new_line = self.center_current_line()
        new_line+= '\n' + '{:^{width}}'.format('::::::', width=self.line_width)
        self.view.replace(edit, self.cur_line_region, new_line)
       

class BrailleCenterCommand(sublime_plugin.TextCommand, AlignCommand):
    """
        Überschrift zentrieren und mit '::::::' unterstreichen
    """
    def run(self, edit):
        new_line = self.center_current_line()
        self.view.replace(edit, self.cur_line_region, new_line)

class BrailleRightAlignCommand(sublime_plugin.TextCommand, AlignCommand):
    """
        Überschrift zentrieren und mit '::::::' unterstreichen
    """
    def run(self, edit):
        new_line = self.right_align_current_line()
        self.view.replace(edit, self.cur_line_region, new_line)        

class BrailleLeftAlignCommand(sublime_plugin.TextCommand, AlignCommand):
    """
        Überschrift zentrieren und mit '::::::' unterstreichen
    """
    def run(self, edit):
        new_line = self.left_align_current_line()
        self.view.replace(edit, self.cur_line_region, new_line)                


