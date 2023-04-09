import os
from savefile import SaveFile

path = '/Users/phil/Library/Application Support/Steam/steamapps/common/SlayTheSpire/SlayTheSpire.app/Contents/Resources/saves/DEFECT.autosave'

SaveFile(path).import_json(path + '.json')

