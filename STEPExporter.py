# Copyright 2024 Cadwork Informatique Inc.
# All rights reserved.
# This file is part of STEPExporter,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import attribute_controller as ac
import element_controller as ec
import file_controller as fc
import utility_controller as uc

active_elements = ec.get_active_identifiable_element_ids()

production_number_element_map = {}

for element in active_elements:
    production_number = ac.get_production_number(element)
    if production_number not in production_number_element_map:
        production_number_element_map[production_number] = element

all_elements = ec.get_all_identifiable_element_ids()

production_number_count_map = {}

for element in active_elements:
    production_number = ac.get_production_number(element)
    if production_number not in production_number_count_map:
        production_number_count_map[production_number] = 1
    else:
        production_number_count_map[production_number] += 1

destination_folder = uc.get_user_path_from_dialog()

if destination_folder:
    for production_number in production_number_element_map:
        filename = destination_folder + '/' + f'{production_number}_{production_number_count_map[production_number]}.step'
        fc.export_step_file_extrude_drillings([production_number_element_map[production_number]],
                                              filename,
                                              1000,
                                              214,
                                              True,
                                              False)
