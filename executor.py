import subprocess
import os


directory = os.path.dirname(os.path.realpath(__file__))
miner_script = os.path.join(directory, 'pyminer.py')
config_file = os.path.join(directory, 'config.cfg')
subprocess.call(['python', miner_script, config_file])
