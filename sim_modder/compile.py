"""
compile module

Used to compile script mods.
"""
import os
import sys
from zipfile import PyZipFile, ZIP_STORED
from sim_modder.constants import *


def compile(input):
    """
    compile_module
    """
    print("compile called for module: ", input.module)

    input_path = f'{LOCAL_MODS}/{input.module}'

    if not os.path.exists(input_path):
        print(f'No mod found named {input.module}!')
        print('Make sure you have the path set correctly in constants.')
        sys.exit(1)

    output_path = f'{SIMS_MODS}/{CREATOR}_{input.module}.ts4script'

    _zipfile = PyZipFile(output_path, mode='w',
                        compression=ZIP_STORED,
                        allowZip64=True, optimize=2)

    for folder, subs, files in os.walk(input_path):
        _zipfile.writepy(folder)
        for file in files:
            if '__pycache__' not in folder:
                _zipfile.write(input_path, f'{input.module}/{file}')

    _zipfile.close()
