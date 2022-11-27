#!/usr/bin/python3
'''
init model: makes directories be treated as packages
'''


from models.engine.file_storage import FileStorage


# creating a File Storage instance

storage = FileStorage()
storage.reload()
