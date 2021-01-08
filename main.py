from package.antiwirus import AntiWirus, IndexFile


antywirus = AntiWirus()

scan_path = "/home/kuba/v2/testy"

antywirus.scan_for_files_to_index(scan_path)

antywirus.index_to_file()


