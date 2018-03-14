#!/usr/bin/python

from subprocess import check_output, call
from os import rename

module_path = "/usr/lib/apache2/modules"

removed = set()
needed = set()

def mod_filename(mod):
    return 'mod_' + mod.split('_module')[0] + '.so'

#get list of modules
modules = check_output([ 'apache2ctl', '-M']).rstrip().split('\n')
# remove whitespace from each
modules = [ m.rstrip().split(' ') for m in modules ]

for mod in (modules - needed):

    # remove mod

    # restart apache2
    print 'restarting apache2...'
    restart_code = call(['systemctl', 'restart', 'apache2'])
    status_code  = call(['systemctl', 'status', 'apache2'])

    # apache2 started successfully
    if status_code == 0:
        print 'removing', mod[0]
        removed += mod
    else:
        print 'determined necessary', mod[0]
        needed += mod
