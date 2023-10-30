"""All global variables are present here
"""
#!/usr/bin/python3


from .engine.file_storage import FileStorage



obj_is_new = False
storage = FileStorage()
storage.reload()