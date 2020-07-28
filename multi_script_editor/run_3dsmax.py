import sys, os
path = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
if not path in sys.path:
    sys.path.append(path)
print path
import multi_script_editor
reload(multi_script_editor)
multi_script_editor.show3DSMax()