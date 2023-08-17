"""
  This generates bindings for the ggml library using cffi and .pyi stubs for the Python bindings.

  See the various environment variables at the top of this file for options.
"""
import sys, re, itertools
sys.path.extend(['.', '..']) # for pycparser

from pycparser import c_ast, parse_file, CParser
import pycparser.plyparser
from pycparser.c_ast import PtrDecl, TypeDecl, FuncDecl, EllipsisParam, IdentifierType, Struct, Enum, Typedef
from typing import Tuple

__c_type_to_python_type = {
    'void': 'None', '_Bool': 'bool',
    'char': 'int', 'short': 'int', 'int': 'int', 'long': 'int',
    'ptrdiff_t': 'int', 'size_t': 'int',
    'int8_t': 'int', 'uint8_t': 'int',
    'int16_t': 'int', 'uint16_t': 'int',
    'int32_t': 'int', 'uint32_t': 'int',
    'int64_t': 'int', 'uint64_t': 'int',
    'float': 'float', 'double': 'float',
    'ggml_fp16_t': 'np.float16',
}

def format_type(t: TypeDecl):
    if isinstance(t, PtrDecl) or isinstance(t, Struct):
        return 'ffi.CData'
    if isinstance(t, Enum):
        return 'int'
    if isinstance(t, TypeDecl):
        return format_type(t.type)
    if isinstance(t, IdentifierType):
        assert len(t.names) == 1, f'Expected a single name, got {t.names}'
        return __c_type_to_python_type.get(t.names[0]) or 'ffi.CData'
    return t.name

class PythonStubFuncDeclVisitor(c_ast.NodeVisitor):
    def __init__(self):
        self.sigs = {}
        self.sources = {}

    def get_source_snippet_lines(self, coord: pycparser.plyparser.Coord) -> Tuple[list[str], list[str]]:
        if coord.file not in self.sources:
            with open(coord.file, 'rt') as f:
                self.sources[coord.file] = f.readlines()
        source_lines = self.sources[coord.file]
        ncomment_lines = len(list(itertools.takewhile(lambda i: re.search(r'^\s*(//|/\*)', source_lines[i]), range(coord.line - 2, -1, -1))))
        comment_lines = [l.strip() for l in source_lines[coord.line - 1 - ncomment_lines:coord.line - 1]]
        decl_lines = []
        for line in source_lines[coord.line - 1:]:
            decl_lines.append(line.rstrip())
            if (';' in line) or ('{' in line): break
        return (comment_lines, decl_lines)

    def visit_Enum(self, node: Enum):
        if node.values is not None:
          for e in node.values.enumerators:
              self.sigs[e.name] = f'  @property\n  def {e.name}(self) -> int: ...'

    def visit_Typedef(self, node: Typedef):
        pass

    def visit_FuncDecl(self, node: FuncDecl):
        ret_type = node.type
        is_ptr = False
        while isinstance(ret_type, PtrDecl):
            ret_type = ret_type.type
            is_ptr = True
        
        fun_name = ret_type.declname
        if fun_name.startswith('__'):
            return
        
        args = []
        argnames = []
        def gen_name(stem):
            i = 1
            while True:
                new_name = stem if i == 1 else f'{stem}{i}'
                if new_name not in argnames: return new_name
                i += 1
        
        for a in node.args.params:
            if isinstance(a, EllipsisParam):
                arg_name = gen_name('args')
                argnames.append(arg_name)
                args.append('*' + gen_name('args'))
            elif format_type(a.type) == 'None':
                continue
            else:
                arg_name = a.name or gen_name('arg')
                argnames.append(arg_name)
                args.append(f'{arg_name}: {format_type(a.type)}')

        ret = format_type(ret_type if not is_ptr else node.type)

        comment_lines, decl_lines = self.get_source_snippet_lines(node.coord)

        lines = [f'  def {fun_name}({", ".join(args)}) -> {ret}:']
        if len(comment_lines) == 0 and len(decl_lines) == 1:
            lines += [f'    """{decl_lines[0]}"""']
        else:
            lines += ['    """']
            lines += [f'    {c.lstrip("/* ")}' for c in comment_lines]
            if len(comment_lines) > 0:
                lines += ['']
            lines += [f'    {d}' for d in decl_lines]
            lines += ['    """']
        lines += ['    ...']
        self.sigs[fun_name] = '\n'.join(lines)

def generate_stubs(header: str):
    """
      Generates a .pyi Python stub file for the GGML API using C header files.
    """

    with open('stubs.h', 'wt') as f:
        f.write(header)

    v = PythonStubFuncDeclVisitor()
    v.visit(CParser().parse(header, "<input>"))

    keys = list(v.sigs.keys())
    keys.sort()

    return '\n'.join([
        '# auto-generated file',
        'import ggml.ffi as ffi',
        'import numpy as np',
        'from typing import Union',
        '',
        'class ffi:',
        '  def typeof(x) -> ffi.CType: ...',
        '  def new(type: ffi.CType, *args, **kwargs) -> ffi.CData: ...',
        '  def cast(type: Union[ffi.CType, str], data: ffi.CData) -> ffi.CData: ...',
        '  def from_buffer(data: Union[bytes, bytearray, memoryview]) -> ffi.CData: ...',
        '  def buffer(data: ffi.CData, size: int) -> Union[bytes, bytearray, memoryview]: ...',
        '  def string(data: ffi.CData) -> str: ...',
        '',
        'class lib:',
        *[v.sigs[k] for k in keys]
    ])