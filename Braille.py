import sublime
import sublime_plugin


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



class UeberschriftCommand(sublime_plugin.TextCommand, AlignCommand):
    """
        Überschrift zentrieren und mit '::::::' unterstreichen
    """
    def run(self, edit):
        print('Hallo')
        new_line = '{:^{width}}'.format(self.cur_line.strip(), width=self.line_width)
        new_line+= '\n' + '{:^{width}}'.format('::::::', width=self.line_width)
        self.view.replace(edit, self.cur_line_region, new_line)
       

class ZentriereCommand(sublime_plugin.TextCommand, AlignCommand):
    """
        Überschrift zentrieren und mit '::::::' unterstreichen
    """
    def run(self, edit):
        new_line = '{:^{width}}'.format(self.cur_line.strip(), width=self.line_width)
        self.view.replace(edit, self.cur_line_region, new_line)