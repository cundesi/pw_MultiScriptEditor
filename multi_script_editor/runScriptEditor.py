from multi_script_editor import scriptEditor
from Qt import QtWidgets

app = QtWidgets.QApplication([])
w = scriptEditor.scriptEditorClass()
w.setWindowStyle()
w.show()
app.exec_()
