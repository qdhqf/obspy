#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This tests TauP_Path.
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import *  # NOQA


import os
import subprocess
import sys
from unittest import TestCase

from obspy.taup import TauPyModel
from obspy.taup.taup_path import TauP_Path


class TestTauPPath(TestCase):
    def test_script_output_h10_deg35_iasp91(self):
        tp = TauP_Path(degrees=35, depth=10, modelName="iasp91",
                       phaseList=["P"])
        stdout = sys.stdout
        with open('data/tmp_tauppath_test_output', 'wt') as sys.stdout:
            tp.run(printOutput=True)
        sys.stdout = stdout
        subprocess.check_call("diff -wB data/TauP_test_data/taup_path_-o_"
                              "stdout_-h_10_-ph_P_-deg_35 "
                              "data/tmp_tauppath_test_output", shell=True)
        os.remove("data/tmp_tauppath_test_output")

    def test_script_output_h10_deg35_ak135(self):
        tp = TauP_Path(degrees=35, depth=10, modelName="ak135",
                       phaseList=["P"])
        stdout = sys.stdout
        with open('data/tmp_tauppath_test_output', 'wt') as sys.stdout:
            tp.run(printOutput=True)
        sys.stdout = stdout
        subprocess.check_call("diff -wB data/TauP_test_data/taup_path_-o_"
                              "stdout_-h_10_-ph_P_-deg_35_-mod_ak135 "
                              "data/tmp_tauppath_test_output", shell=True)
        os.remove("data/tmp_tauppath_test_output")

    def test_script_output_h10_deg35_iasp91_with_tau_interface(self):
        i91 = TauPyModel("iasp91")

        stdout = sys.stdout
        with open('data/tmp_tauppath_test_output', 'wt') as sys.stdout:
            i91.get_ray_paths(10, 35, ["P"], print_output=True)
        sys.stdout = stdout
        subprocess.check_call("diff -wB data/TauP_test_data/taup_path_-o_"
                              "stdout_-h_10_-ph_P_-deg_35 "
                              "data/tmp_tauppath_test_output", shell=True)
        os.remove("data/tmp_tauppath_test_output")

        # Just a check that coordinates are also passed through.
        i91.get_ray_paths(10, coordinate_list=[10, 20, 30, 40],
                          phase_list=["P", "PcS"])

        # This doesn't work as subprocess, but to check cli execution use:
        # ../taup_path.py -mod iasp91 -d 10 -ph P,PcS -deg 30
        # in bash.
