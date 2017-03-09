#--
# hummingbird/util.py
#--
# it inclues various utility functions 
#
#   get_path      : parse a path string from path fragments
#   format_string : format a string given a string template
#   create_dir    : check wether the directory already exists. if not, create it 
#   create_config : create a configurate file given a dictionary containing parameters
#

import os

def get_path (*frags):
    ''' 
        generates a path string from path fragments 
        frags: path fragments. 
    '''
    path = []
    
    for part in frags:
        if part.startswith("/"):
            part = part[1:]
        if part.endswith("/"):
            part = part[:-1]
        path.append(part)

    # check whether to use an absoulte or an relative path
    path[0] = path[0] if path[0].startswith('.') else "/" + path[0]

    return "/".join(path)

def format_string(template, *args):
    ''' 
        simple function to format a string 
        template: a template to format against
        args    : variables to be formatted 
        ex_code : exit code (0: success, 1: failure)
    '''
    return template.format(*args)

def create_dir(path_to_dir):
    ''' check wether the directory already exists. if not, create it '''
    ex_code = 0       # exit code
    
    if not os.path.isdir(path_to_dir):
        os.makedirs(path_to_dir)
        ex_code = 0
    else: 
        ex_code = 1 

    return ex_code

def create_config(file_name, config_dict):
    '''
        
    '''
    ex_code = 0       # exit code
    
    return 
