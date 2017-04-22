# -*- coding:utf-8 -*-
from utils.shell import Shell

__author__ = 'mio'


class CommonUtils:
    @staticmethod
    def dot_to_pdf_graphviz(input_file, output_file):
        cmd = "dot -Tpdf %s -o %s" % (input_file, output_file)
        Shell.invoke(cmd)
