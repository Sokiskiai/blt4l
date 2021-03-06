#!/usr/bin/python2.7
# Parameters: a localconfig.vdf path
# What this script does:
#   Sets the launch parameters for PAYDAY 2 to load the BLT hook

import sys
sys.path.append(".")
import keyvalues

vdf = keyvalues.keyvalues()
vdf.load_from_file(sys.argv[1])

vdf.kv['UserLocalConfigStore']['Software']['Valve']['Steam']['apps']['218620']['LaunchOptions'] = 'env LD_PRELOAD=\\"$LD_PRELOAD ./libblt_loader.so\\" %command%'

vdf.save_to_file(sys.argv[1])
