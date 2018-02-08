import sublime
import sublime_plugin

buff='kjhj'
class TestexecCommand(sublime_plugin.TextCommand):
	def run(self, edit, lines):
		currvw = self.view
		texta=''
		for line in lines:
			texta += line + '\n'
		self.view.insert(edit, 0, texta)

class TextgetCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		currvw = self.view
		return currvw.substr(currvw.sel()[0])

class NewwinCommand(sublime_plugin.WindowCommand):
	def run(self):

		v = self.window.active_view()

		buffa=[]		
		for ln in v.sel():
			buffa.append(v.substr(ln))

		self.window.new_file()
		viewv = self.window.active_view()
		viewv.run_command('testexec', { "lines" : buffa })

