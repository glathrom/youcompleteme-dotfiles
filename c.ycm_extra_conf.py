import os
import ycm_core

flags = [
        '-Wall',
        '-Wextra',
        '-Wno-long-long',
        '-Wno-variadic-macros',
        '-fexceptions',
        '-ferror-limit=10000',
        '-DNDEBUG',
        '-std=c99',
        '-xc',
        '-isystem/usr/include/',
        '-isystem/usr/include/mysql',
        ]

SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', ]

HEADER_EXTENSIONS = [ '.h', '.hxx', '.hpp', '.hh' ]

def Settings( **kwargs ):
    return {
            'flags': flags,
            'do_cache': True
            }

