from package.antiwirus import AntiWirus, IndexFile


antywirus = AntiWirus()

scan_path = "/home/kuba/v2/testy"

antywirus.get_files_to_index(scan_path)

antywi