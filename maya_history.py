
import os
import maya.cmds
import maya.utils

def write_history():
	def history_callback():
		path = maya.cmds.internalVar( usd=True )
		filename = 'script_editor_history.txt'
		maya.cmds.scriptEditorInfo( historyFilename=os.path.join( path , filename ), writeHistory=True )

	maya.utils.executeDeferred( history_callback )
	del history_callback

if not maya.cmds.about( batch=True ):
	print '--[ Enabling script editor log file.'
	write_history()
