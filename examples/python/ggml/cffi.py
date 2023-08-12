#
# AUTOGENERATED *SLOW* BINDINGS FILE (--mode=dynamic_load)
#
# This file is versioned and can be used to power Python interop
# provided libllama.so can be found, but it is not the fastest mode supported.
#
# If you need to make so many calls to the ggml API that per-call overhead becomes
# a concern, please regenerate the bindings as a native extension.
# To do so, run *something* like:
#
#     python generate.py --mode=static_link ...
#
import {ggml_package}.ffi as ffi

# auto-generated file
import _cffi_backend

ffi = _cffi_backend.FFI('ggml.cffi',
    _version = 0x2601,
    _types = b'\x00\x00\x85\x0D\x00\x00\x09\x0B\x00\x00\x00\x0F\x00\x00\x85\x0D\x00\x02\xE0\x03\x00\x00\x00\x0F\x00\x00\x85\x0D\x00\x02\xE9\x03\x00\x00\x00\x0F\x00\x00\x85\x0D\x00\x00\x07\x11\x00\x00\x07\x11\x00\x00\x00\x0F\x00\x00\x85\x0D\x00\x02\xFB\x03\x00\x00\x00\x0F\x00\x00\x85\x0D\x00\x00\x00\x0F\x00\x00\x7E\x0D\x00\x00\x04\x0B\x00\x00\x00\x0F\x00\x00\x7E\x0D\x00\x00\x01\x11\x00\x00\x00\x0F\x00\x00\x7E\x0D\x00\x00\x07\x11\x00\x00\x00\x0F\x00\x02\xC7\x0D\x00\x00\x04\x11\x00\x02\xE4\x03\x00\x02\xE9\x03\x00\x00\x00\x0F\x00\x02\xC7\x0D\x00\x00\x04\x11\x00\x00\x1D\x11\x00\x00\x1E\x11\x00\x02\xDE\x03\x00\x00\x24\x11\x00\x00\x00\x0F\x00\x02\xC7\x0D\x00\x00\x04\x11\x00\x00\x12\x09\x00\x00\x1E\x11\x00\x00\x00\x0F\x00\x00\x01\x0D\x00\x00\x01\x0B\x00\x00\x00\x0F\x00\x00\xDE\x0D\x00\x00\x07\x11\x00\x00\x00\x0F\x00\x01\xF7\x0D\x00\x00\x07\x11\x00\x00\x00\x0F\x00\x00\xBE\x0D\x00\x00\x01\x11\x00\x00\x00\x0F\x00\x00\xBE\x0D\x00\x00\x07\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\xBE\x0D\x00\x00\x14\x01\x00\x00\x00\x0F\x00\x02\xC9\x0D\x00\x00\x01\x11\x00\x00\x00\x0F\x00\x00\x3A\x0D\x00\x00\x01\x11\x00\x00\x00\x0F\x00\x00\x3A\x0D\x00\x00\x24\x11\x00\x02\xE1\x03\x00\x00\x00\x0F\x00\x00\x3A\x0D\x00\x00\x00\x0F\x00\x00\xC2\x0D\x00\x00\x07\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\xA5\x0D\x00\x00\x07\x11\x00\x00\x00\x0F\x00\x00\xA5\x0D\x00\x00\x00\x0F\x00\x01\x31\x0D\x00\x00\x01\x11\x00\x00\x00\x0F\x00\x01\x31\x0D\x00\x00\x01\x11\x00\x00\xBE\x03\x00\x00\x0E\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\xA5\x03\x00\x00\x00\x0F\x00\x01\x31\x0D\x00\x00\x59\x11\x00\x00\x0E\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x5D\x11\x00\x00\x00\x0F\x00\x01\x31\x0D\x00\x00\x04\x11\x00\x00\x13\x09\x00\x00\x00\x0F\x00\x01\x31\x0D\x00\x02\xE0\x03\x00\x00\x00\x0F\x00\x01\x31\x0D\x00\x00\x07\x11\x00\x00\x00\x0F\x00\x01\x31\x0D\x00\x00\x07\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x01\x31\x0D\x00\x00\x00\x0F\x00\x00\x24\x0D\x00\x00\x04\x11\x00\x00\x00\x0F\x00\x00\x24\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x00\x0F\x00\x02\xDE\x0D\x00\x02\xBF\x03\x00\x00\x04\x03\x00\x00\x7F\x11\x00\x00\x00\x0F\x00\x02\xDE\x0D\x00\x00\x04\x11\x00\x00\x24\x11\x00\x00\x01\x01\x00\x00\x00\x0F\x00\x02\xDE\x0D\x00\x00\x1E\x11\x00\x00\x00\x0F\x00\x00\x04\x0D\x00\x00\x0F\x09\x00\x00\x00\x0F\x00\x02\xE1\x0D\x00\x00\x24\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x29\x0D\x00\x00\x07\x0B\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x24\x11\x00\x00\x7E\x11\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x7E\x11\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x01\x11\x00\x00\x07\x01\x00\x00\xA5\x03\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x01\x11\x00\x00\x17\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x01\x11\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x01\x11\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x01\x11\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x0D\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x15\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x05\x0B\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\xCB\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x0A\x0B\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x0D\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x0D\x01\x00\x00\x0D\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x0D\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x0D\x01\x00\x00\x0D\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x17\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x1C\x01\x00\x00\x1C\x01\x00\x00\x1C\x01\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x1C\x01\x00\x00\x1C\x01\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x17\x01\x00\x00\x17\x01\x00\x00\x1C\x01\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x17\x01\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x1C\x01\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x1C\x01\x00\x00\x1C\x01\x00\x00\x1C\x01\x00\x00\x1C\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x01\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x01\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x02\x93\x03\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x02\x99\x03\x00\x00\x07\x01\x00\x00\x0E\x11\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x02\x40\x03\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x02\x86\x03\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x1E\x11\x00\x02\x8B\x03\x00\x00\x07\x01\x00\x00\x0E\x11\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x02\x3B\x03\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x02\x7B\x03\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x02\x7F\x03\x00\x00\x07\x01\x00\x00\x0E\x11\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x04\x11\x00\x00\x07\x11\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x1E\x11\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x1E\x11\x00\x00\x7E\x11\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x1E\x11\x00\x00\x7E\x11\x00\x00\x01\x0F\x00\x00\x1E\x0D\x00\x00\x1E\x11\x00\x00\x0D\x01\x00\x00\x00\x0F\x00\x00\x1E\x0D\x00\x00\x1E\x11\x00\x00\x15\x01\x00\x00\x00\x0F\x00\x00\x3D\x0D\x00\x00\x0D\x01\x00\x00\x00\x0F\x00\x00\x0E\x0D\x00\x00\x6B\x11\x00\x00\x00\x0F\x00\x00\x0E\x0D\x00\x00\x07\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x02\xB9\x03\x00\x00\xBE\x03\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x02\xBA\x03\x00\x01\xF7\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x02\xBB\x03\x00\x01\xF7\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x02\xBC\x03\x00\x01\xF7\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x02\xBD\x03\x00\x01\xF7\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x02\xBE\x03\x00\x01\xF7\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x59\x11\x00\x02\xB9\x03\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x59\x11\x00\x02\xBA\x03\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x59\x11\x00\x02\xBB\x03\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x59\x11\x00\x02\xBC\x03\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x59\x11\x00\x02\xBD\x03\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x59\x11\x00\x02\xBE\x03\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x59\x11\x00\x00\x3D\x03\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x59\x11\x00\x00\x0E\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x07\x01\x00\x01\xF7\x11\x00\x00\x59\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x07\x01\x00\x01\xF7\x11\x00\x00\x59\x11\x00\x00\x59\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x07\x01\x00\x01\xF7\x11\x00\x02\xFB\x03\x00\x02\x49\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x24\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x24\x11\x00\x00\x1E\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x02\xDE\x03\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x02\x54\x11\x00\x00\x7E\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x02\x54\x11\x00\x02\x54\x11\x00\x00\x7E\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x04\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x04\x11\x00\x00\x01\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x04\x11\x00\x00\x24\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x04\x11\x00\x00\x1D\x11\x00\x00\x29\x11\x00\x00\x17\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x04\x11\x00\x00\x1E\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x6B\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x02\xE3\x03\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x1E\x11\x00\x00\x07\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x1E\x11\x00\x00\x07\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x0E\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x1E\x11\x00\x00\x07\x11\x00\x00\x07\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x1E\x11\x00\x00\x07\x11\x00\x00\x07\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x0E\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x1E\x11\x00\x00\x07\x11\x00\x00\x07\x11\x00\x00\x07\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x1E\x11\x00\x00\x07\x11\x00\x00\x07\x11\x00\x00\x07\x11\x00\x00\x07\x01\x00\x00\x07\x01\x00\x00\x0E\x11\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x07\x11\x00\x00\x07\x01\x00\x00\x0D\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x07\x11\x00\x00\x07\x01\x00\x00\x15\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x3D\x03\x00\x01\xF7\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x02\x49\x11\x00\x01\xF7\x11\x00\x00\x07\x01\x00\x00\x00\x0F\x00\x02\xFB\x0D\x00\x00\x00\x0F\x00\x00\x0D\x03\x00\x00\x04\x09\x00\x00\x05\x09\x00\x00\x06\x09\x00\x00\x07\x09\x00\x00\x08\x09\x00\x00\x09\x09\x00\x00\x02\x01\x00\x02\xBF\x05\x00\x00\x00\x30\x00\x02\xBF\x05\x00\x00\x00\x04\x00\x00\x00\x0B\x00\x00\x02\x0B\x00\x00\x03\x0B\x00\x00\x06\x0B\x00\x00\x08\x0B\x00\x00\x0A\x09\x00\x00\x13\x01\x00\x02\xCA\x05\x00\x00\x00\x10\x00\x00\xC2\x05\x00\x00\x00\x08\x00\x00\xA5\x05\x00\x00\x00\x04\x00\x00\x11\x01\x00\x02\xD1\x05\x00\x00\x00\x10\x00\x02\xD1\x05\x00\x00\x01\x00\x00\x00\x3A\x05\x00\x00\x10\x00\x00\x01\x31\x05\x00\x00\x00\x04\x00\x00\x00\x09\x00\x00\x01\x09\x00\x00\x02\x09\x00\x00\x03\x09\x00\x00\x0B\x09\x00\x00\x0C\x09\x00\x00\x0D\x09\x00\x00\x0E\x09\x00\x02\xE3\x03\x00\x00\x10\x09\x00\x00\x11\x09\x00\x00\x1E\x05\x00\x00\x10\x00\x00\x00\x1E\x05\x00\x00\x00\x06\x00\x00\x14\x09\x00\x02\xEB\x03\x00\x00\x12\x01\x00\x02\xEB\x05\x00\x00\x00\x80\x00\x02\xEB\x05\x00\x00\x00\x0C\x00\x02\xEB\x05\x00\x00\x00\x10\x00\x02\xEB\x05\x00\x00\x00\x20\x00\x02\xEB\x05\x00\x00\x00\x40\x00\x00\x0E\x05\x00\x00\x20\x51\x00\x02\x36\x03\x00\x02\x46\x03\x00\x02\xB1\x03\x00\x00\x00\x01',
    _globals = (b'\xFF\xFF\xFF\x0BGGML_BACKEND_CPU',0,b'\xFF\xFF\xFF\x0BGGML_BACKEND_GPU',10,b'\xFF\xFF\xFF\x0BGGML_BACKEND_GPU_SPLIT',20,b'\xFF\xFF\xFF\x0BGGML_FTYPE_ALL_F32',0,b'\xFF\xFF\xFF\x0BGGML_FTYPE_MOSTLY_F16',1,b'\xFF\xFF\xFF\x0BGGML_FTYPE_MOSTLY_Q2_K',10,b'\xFF\xFF\xFF\x0BGGML_FTYPE_MOSTLY_Q3_K',11,b'\xFF\xFF\xFF\x0BGGML_FTYPE_MOSTLY_Q4_0',2,b'\xFF\xFF\xFF\x0BGGML_FTYPE_MOSTLY_Q4_1',3,b'\xFF\xFF\xFF\x0BGGML_FTYPE_MOSTLY_Q4_1_SOME_F16',4,b'\xFF\xFF\xFF\x0BGGML_FTYPE_MOSTLY_Q4_K',12,b'\xFF\xFF\xFF\x0BGGML_FTYPE_MOSTLY_Q5_0',8,b'\xFF\xFF\xFF\x0BGGML_FTYPE_MOSTLY_Q5_1',9,b'\xFF\xFF\xFF\x0BGGML_FTYPE_MOSTLY_Q5_K',13,b'\xFF\xFF\xFF\x0BGGML_FTYPE_MOSTLY_Q6_K',14,b'\xFF\xFF\xFF\x0BGGML_FTYPE_MOSTLY_Q8_0',7,b'\xFF\xFF\xFF\x0BGGML_FTYPE_UNKNOWN',-1,b'\xFF\xFF\xFF\x1FGGML_GRAPH_SIZE',164520,b'\xFF\xFF\xFF\x0BGGML_LINESEARCH_BACKTRACKING_ARMIJO',0,b'\xFF\xFF\xFF\x0BGGML_LINESEARCH_BACKTRACKING_STRONG_WOLFE',2,b'\xFF\xFF\xFF\x0BGGML_LINESEARCH_BACKTRACKING_WOLFE',1,b'\xFF\xFF\xFF\x0BGGML_LINESEARCH_DEFAULT',1,b'\xFF\xFF\xFF\x0BGGML_LINESEARCH_FAIL',-128,b'\xFF\xFF\xFF\x0BGGML_LINESEARCH_INVALID_PARAMETERS',-124,b'\xFF\xFF\xFF\x0BGGML_LINESEARCH_MAXIMUM_ITERATIONS',-125,b'\xFF\xFF\xFF\x0BGGML_LINESEARCH_MAXIMUM_STEP',-126,b'\xFF\xFF\xFF\x0BGGML_LINESEARCH_MINIMUM_STEP',-127,b'\xFF\xFF\xFF\x0BGGML_OBJECT_GRAPH',1,b'\xFF\xFF\xFF\x1FGGML_OBJECT_SIZE',32,b'\xFF\xFF\xFF\x0BGGML_OBJECT_TENSOR',0,b'\xFF\xFF\xFF\x0BGGML_OBJECT_WORK_BUFFER',2,b'\xFF\xFF\xFF\x0BGGML_OPT_ADAM',0,b'\xFF\xFF\xFF\x0BGGML_OPT_DID_NOT_CONVERGE',1,b'\xFF\xFF\xFF\x0BGGML_OPT_FAIL',4,b'\xFF\xFF\xFF\x0BGGML_OPT_INVALID_WOLFE',3,b'\xFF\xFF\xFF\x0BGGML_OPT_LBFGS',1,b'\xFF\xFF\xFF\x0BGGML_OPT_NO_CONTEXT',2,b'\xFF\xFF\xFF\x0BGGML_OPT_OK',0,b'\xFF\xFF\xFF\x0BGGML_OP_ACC',4,b'\xFF\xFF\xFF\x0BGGML_OP_ADD',2,b'\xFF\xFF\xFF\x0BGGML_OP_ADD1',3,b'\xFF\xFF\xFF\x0BGGML_OP_ALIBI',40,b'\xFF\xFF\xFF\x0BGGML_OP_ARGMAX',14,b'\xFF\xFF\xFF\x0BGGML_OP_CLAMP',41,b'\xFF\xFF\xFF\x0BGGML_OP_CONT',26,b'\xFF\xFF\xFF\x0BGGML_OP_CONV_1D',42,b'\xFF\xFF\xFF\x0BGGML_OP_CONV_2D',43,b'\xFF\xFF\xFF\x0BGGML_OP_COUNT',62,b'\xFF\xFF\xFF\x0BGGML_OP_CPY',25,b'\xFF\xFF\xFF\x0BGGML_OP_CROSS_ENTROPY_LOSS',60,b'\xFF\xFF\xFF\x0BGGML_OP_CROSS_ENTROPY_LOSS_BACK',61,b'\xFF\xFF\xFF\x0BGGML_OP_DIAG',33,b'\xFF\xFF\xFF\x0BGGML_OP_DIAG_MASK_INF',34,b'\xFF\xFF\xFF\x0BGGML_OP_DIAG_MASK_ZERO',35,b'\xFF\xFF\xFF\x0BGGML_OP_DIV',7,b'\xFF\xFF\xFF\x0BGGML_OP_DUP',1,b'\xFF\xFF\xFF\x0BGGML_OP_FLASH_ATTN',46,b'\xFF\xFF\xFF\x0BGGML_OP_FLASH_ATTN_BACK',48,b'\xFF\xFF\xFF\x0BGGML_OP_FLASH_FF',47,b'\xFF\xFF\xFF\x0BGGML_OP_GET_ROWS',31,b'\xFF\xFF\xFF\x0BGGML_OP_GET_ROWS_BACK',32,b'\xFF\xFF\xFF\x0BGGML_OP_LOG',10,b'\xFF\xFF\xFF\x0BGGML_OP_MAP_BINARY',53,b'\xFF\xFF\xFF\x0BGGML_OP_MAP_CUSTOM1',57,b'\xFF\xFF\xFF\x0BGGML_OP_MAP_CUSTOM1_F32',54,b'\xFF\xFF\xFF\x0BGGML_OP_MAP_CUSTOM2',58,b'\xFF\xFF\xFF\x0BGGML_OP_MAP_CUSTOM2_F32',55,b'\xFF\xFF\xFF\x0BGGML_OP_MAP_CUSTOM3',59,b'\xFF\xFF\xFF\x0BGGML_OP_MAP_CUSTOM3_F32',56,b'\xFF\xFF\xFF\x0BGGML_OP_MAP_UNARY',52,b'\xFF\xFF\xFF\x0BGGML_OP_MEAN',13,b'\xFF\xFF\xFF\x0BGGML_OP_MUL',6,b'\xFF\xFF\xFF\x0BGGML_OP_MUL_MAT',21,b'\xFF\xFF\xFF\x0BGGML_OP_NONE',0,b'\xFF\xFF\xFF\x0BGGML_OP_NORM',18,b'\xFF\xFF\xFF\x0BGGML_OP_OUT_PROD',22,b'\xFF\xFF\xFF\x0BGGML_OP_PERMUTE',29,b'\xFF\xFF\xFF\x0BGGML_OP_POOL_1D',44,b'\xFF\xFF\xFF\x0BGGML_OP_POOL_2D',45,b'\xFF\xFF\xFF\x0BGGML_OP_POOL_AVG',1,b'\xFF\xFF\xFF\x0BGGML_OP_POOL_COUNT',2,b'\xFF\xFF\xFF\x0BGGML_OP_POOL_MAX',0,b'\xFF\xFF\xFF\x0BGGML_OP_REPEAT',15,b'\xFF\xFF\xFF\x0BGGML_OP_REPEAT_BACK',16,b'\xFF\xFF\xFF\x0BGGML_OP_RESHAPE',27,b'\xFF\xFF\xFF\x0BGGML_OP_RMS_NORM',19,b'\xFF\xFF\xFF\x0BGGML_OP_RMS_NORM_BACK',20,b'\xFF\xFF\xFF\x0BGGML_OP_ROPE',38,b'\xFF\xFF\xFF\x0BGGML_OP_ROPE_BACK',39,b'\xFF\xFF\xFF\x0BGGML_OP_SCALE',23,b'\xFF\xFF\xFF\x0BGGML_OP_SET',24,b'\xFF\xFF\xFF\x0BGGML_OP_SILU_BACK',17,b'\xFF\xFF\xFF\x0BGGML_OP_SOFT_MAX',36,b'\xFF\xFF\xFF\x0BGGML_OP_SOFT_MAX_BACK',37,b'\xFF\xFF\xFF\x0BGGML_OP_SQR',8,b'\xFF\xFF\xFF\x0BGGML_OP_SQRT',9,b'\xFF\xFF\xFF\x0BGGML_OP_SUB',5,b'\xFF\xFF\xFF\x0BGGML_OP_SUM',11,b'\xFF\xFF\xFF\x0BGGML_OP_SUM_ROWS',12,b'\xFF\xFF\xFF\x0BGGML_OP_TRANSPOSE',30,b'\xFF\xFF\xFF\x0BGGML_OP_UNARY',51,b'\xFF\xFF\xFF\x0BGGML_OP_VIEW',28,b'\xFF\xFF\xFF\x0BGGML_OP_WIN_PART',49,b'\xFF\xFF\xFF\x0BGGML_OP_WIN_UNPART',50,b'\xFF\xFF\xFF\x0BGGML_TASK_COMPUTE',1,b'\xFF\xFF\xFF\x0BGGML_TASK_FINALIZE',2,b'\xFF\xFF\xFF\x0BGGML_TASK_INIT',0,b'\xFF\xFF\xFF\x1FGGML_TENSOR_SIZE',272,b'\xFF\xFF\xFF\x0BGGML_TYPE_COUNT',19,b'\xFF\xFF\xFF\x0BGGML_TYPE_F16',1,b'\xFF\xFF\xFF\x0BGGML_TYPE_F32',0,b'\xFF\xFF\xFF\x0BGGML_TYPE_I16',17,b'\xFF\xFF\xFF\x0BGGML_TYPE_I32',18,b'\xFF\xFF\xFF\x0BGGML_TYPE_I8',16,b'\xFF\xFF\xFF\x0BGGML_TYPE_Q2_K',10,b'\xFF\xFF\xFF\x0BGGML_TYPE_Q3_K',11,b'\xFF\xFF\xFF\x0BGGML_TYPE_Q4_0',2,b'\xFF\xFF\xFF\x0BGGML_TYPE_Q4_1',3,b'\xFF\xFF\xFF\x0BGGML_TYPE_Q4_K',12,b'\xFF\xFF\xFF\x0BGGML_TYPE_Q5_0',6,b'\xFF\xFF\xFF\x0BGGML_TYPE_Q5_1',7,b'\xFF\xFF\xFF\x0BGGML_TYPE_Q5_K',13,b'\xFF\xFF\xFF\x0BGGML_TYPE_Q6_K',14,b'\xFF\xFF\xFF\x0BGGML_TYPE_Q8_0',8,b'\xFF\xFF\xFF\x0BGGML_TYPE_Q8_1',9,b'\xFF\xFF\xFF\x0BGGML_TYPE_Q8_K',15,b'\xFF\xFF\xFF\x0BGGML_UNARY_OP_ABS',0,b'\xFF\xFF\xFF\x0BGGML_UNARY_OP_ELU',5,b'\xFF\xFF\xFF\x0BGGML_UNARY_OP_GELU',7,b'\xFF\xFF\xFF\x0BGGML_UNARY_OP_GELU_QUICK',8,b'\xFF\xFF\xFF\x0BGGML_UNARY_OP_NEG',2,b'\xFF\xFF\xFF\x0BGGML_UNARY_OP_RELU',6,b'\xFF\xFF\xFF\x0BGGML_UNARY_OP_SGN',1,b'\xFF\xFF\xFF\x0BGGML_UNARY_OP_SILU',9,b'\xFF\xFF\xFF\x0BGGML_UNARY_OP_STEP',3,b'\xFF\xFF\xFF\x0BGGML_UNARY_OP_TANH',4,b'\x00\x01\xF5\x23dequantize_row_q2_K',0,b'\x00\x01\xFA\x23dequantize_row_q3_K',0,b'\x00\x01\xFF\x23dequantize_row_q4_K',0,b'\x00\x02\x04\x23dequantize_row_q5_K',0,b'\x00\x02\x09\x23dequantize_row_q6_K',0,b'\x00\x02\x0E\x23dequantize_row_q8_K',0,b'\x00\x00\xC4\x23ggml_abs',0,b'\x00\x00\xC4\x23ggml_abs_inplace',0,b'\x00\x01\x7A\x23ggml_acc',0,b'\x00\x01\x7A\x23ggml_acc_inplace',0,b'\x00\x01\x4E\x23ggml_add',0,b'\x00\x01\x4E\x23ggml_add1',0,b'\x00\x01\x4E\x23ggml_add1_inplace',0,b'\x00\x01\x4E\x23ggml_add_inplace',0,b'\x00\x00\xF0\x23ggml_alibi',0,b'\x00\x00\x09\x23ggml_are_same_shape',0,b'\x00\x00\xC4\x23ggml_argmax',0,b'\x00\x00\x42\x23ggml_blck_size',0,b'\x00\x00\x82\x23ggml_build_backward',0,b'\x00\x00\x87\x23ggml_build_forward',0,b'\x00\x00\x79\x23ggml_build_forward_ctx',0,b'\x00\x02\x4F\x23ggml_build_forward_expand',0,b'\x00\x00\xE5\x23ggml_clamp',0,b'\x00\x00\xC4\x23ggml_cont',0,b'\x00\x00\xC4\x23ggml_cont_inplace',0,b'\x00\x01\x5A\x23ggml_conv_1d',0,b'\x00\x01\x53\x23ggml_conv_1d_ph',0,b'\x00\x01\x62\x23ggml_conv_2d',0,b'\x00\x00\x49\x23ggml_cpu_has_arm_fma',0,b'\x00\x00\x49\x23ggml_cpu_has_avx',0,b'\x00\x00\x49\x23ggml_cpu_has_avx2',0,b'\x00\x00\x49\x23ggml_cpu_has_avx512',0,b'\x00\x00\x49\x23ggml_cpu_has_avx512_vbmi',0,b'\x00\x00\x49\x23ggml_cpu_has_avx512_vnni',0,b'\x00\x00\x49\x23ggml_cpu_has_blas',0,b'\x00\x00\x49\x23ggml_cpu_has_clblast',0,b'\x00\x00\x49\x23ggml_cpu_has_cublas',0,b'\x00\x00\x49\x23ggml_cpu_has_f16c',0,b'\x00\x00\x49\x23ggml_cpu_has_fma',0,b'\x00\x00\x49\x23ggml_cpu_has_fp16_va',0,b'\x00\x00\x49\x23ggml_cpu_has_gpublas',0,b'\x00\x00\x49\x23ggml_cpu_has_neon',0,b'\x00\x00\x49\x23ggml_cpu_has_sse3',0,b'\x00\x00\x49\x23ggml_cpu_has_vsx',0,b'\x00\x00\x49\x23ggml_cpu_has_wasm_simd',0,b'\x00\x01\x4E\x23ggml_cpy',0,b'\x00\x01\x4E\x23ggml_cpy_inplace',0,b'\x00\x01\x4E\x23ggml_cross_entropy_loss',0,b'\x00\x01\x83\x23ggml_cross_entropy_loss_back',0,b'\x00\x00\x52\x23ggml_cycles',0,b'\x00\x00\x52\x23ggml_cycles_per_ms',0,b'\x00\x00\xC4\x23ggml_diag',0,b'\x00\x00\xEB\x23ggml_diag_mask_inf',0,b'\x00\x00\xEB\x23ggml_diag_mask_inf_inplace',0,b'\x00\x00\xEB\x23ggml_diag_mask_zero',0,b'\x00\x00\xEB\x23ggml_diag_mask_zero_inplace',0,b'\x00\x01\x4E\x23ggml_div',0,b'\x00\x01\x4E\x23ggml_div_inplace',0,b'\x00\x00\xC4\x23ggml_dup',0,b'\x00\x00\xC4\x23ggml_dup_inplace',0,b'\x00\x01\xD5\x23ggml_dup_tensor',0,b'\x00\x00\x6D\x23ggml_element_size',0,b'\x00\x00\xC4\x23ggml_elu',0,b'\x00\x00\xC4\x23ggml_elu_inplace',0,b'\x00\x01\x89\x23ggml_flash_attn',0,b'\x00\x01\x90\x23ggml_flash_attn_back',0,b'\x00\x01\x98\x23ggml_flash_ff',0,b'\x00\x01\xE0\x23ggml_format_name',0,b'\x00\x00\x3C\x23ggml_fp16_to_fp32',0,b'\x00\x02\xAC\x23ggml_fp16_to_fp32_row',0,b'\x00\x01\xEC\x23ggml_fp32_to_fp16',0,b'\x00\x02\x31\x23ggml_fp32_to_fp16_row',0,b'\x00\x02\x5F\x23ggml_free',0,b'\x00\x00\x2C\x23ggml_ftype_to_ggml_type',0,b'\x00\x00\xC4\x23ggml_gelu',0,b'\x00\x00\xC4\x23ggml_gelu_inplace',0,b'\x00\x00\xC4\x23ggml_gelu_quick',0,b'\x00\x00\xC4\x23ggml_gelu_quick_inplace',0,b'\x00\x01\xF2\x23ggml_get_data',0,b'\x00\x00\x32\x23ggml_get_data_f32',0,b'\x00\x00\x38\x23ggml_get_f32_1d',0,b'\x00\x00\x4B\x23ggml_get_i32_1d',0,b'\x00\x00\x6A\x23ggml_get_max_tensor_size',0,b'\x00\x01\xEF\x23ggml_get_mem_buffer',0,b'\x00\x00\x6A\x23ggml_get_mem_size',0,b'\x00\x00\x18\x23ggml_get_name',0,b'\x00\x00\x03\x23ggml_get_no_alloc',0,b'\x00\x01\x4E\x23ggml_get_rows',0,b'\x00\x01\x83\x23ggml_get_rows_back',0,b'\x00\x00\x98\x23ggml_get_tensor',0,b'\x00\x00\x2F\x23ggml_get_unary_op',0,b'\x00\x00\x45\x23ggml_graph_compute',0,b'\x00\x02\x66\x23ggml_graph_compute_with_ctx',0,b'\x00\x02\x5A\x23ggml_graph_dump_dot',0,b'\x00\x02\x56\x23ggml_graph_export',0,b'\x00\x00\x94\x23ggml_graph_get_tensor',0,b'\x00\x00\x7D\x23ggml_graph_import',0,b'\x00\x00\x74\x23ggml_graph_overhead',0,b'\x00\x00\x8D\x23ggml_graph_plan',0,b'\x00\x02\x53\x23ggml_graph_print',0,b'\x00\x02\x4C\x23ggml_graph_reset',0,b'\x00\x00\x8A\x23ggml_init',0,b'\x00\x00\x3F\x23ggml_internal_get_type_traits',0,b'\x00\x00\x06\x23ggml_is_contiguous',0,b'\x00\x00\x10\x23ggml_is_numa',0,b'\x00\x00\x06\x23ggml_is_permuted',0,b'\x00\x00\x00\x23ggml_is_quantized',0,b'\x00\x00\x06\x23ggml_is_transposed',0,b'\x00\x00\xC4\x23ggml_log',0,b'\x00\x00\xC4\x23ggml_log_inplace',0,b'\x00\x01\xB0\x23ggml_map_binary_f32',0,b'\x00\x01\xB0\x23ggml_map_binary_inplace_f32',0,b'\x00\x01\xCE\x23ggml_map_custom1',0,b'\x00\x01\xC9\x23ggml_map_custom1_f32',0,b'\x00\x01\xCE\x23ggml_map_custom1_inplace',0,b'\x00\x01\xC9\x23ggml_map_custom1_inplace_f32',0,b'\x00\x01\xBC\x23ggml_map_custom2',0,b'\x00\x01\xB6\x23ggml_map_custom2_f32',0,b'\x00\x01\xBC\x23ggml_map_custom2_inplace',0,b'\x00\x01\xB6\x23ggml_map_custom2_inplace_f32',0,b'\x00\x01\xA7\x23ggml_map_custom3',0,b'\x00\x01\xA0\x23ggml_map_custom3_f32',0,b'\x00\x01\xA7\x23ggml_map_custom3_inplace',0,b'\x00\x01\xA0\x23ggml_map_custom3_inplace_f32',0,b'\x00\x01\xC4\x23ggml_map_unary_f32',0,b'\x00\x01\xC4\x23ggml_map_unary_inplace_f32',0,b'\x00\x00\xC4\x23ggml_mean',0,b'\x00\x01\x4E\x23ggml_mul',0,b'\x00\x01\x4E\x23ggml_mul_inplace',0,b'\x00\x01\x4E\x23ggml_mul_mat',0,b'\x00\x00\x6D\x23ggml_nbytes',0,b'\x00\x00\x70\x23ggml_nbytes_split',0,b'\x00\x00\xC4\x23ggml_neg',0,b'\x00\x00\xC4\x23ggml_neg_inplace',0,b'\x00\x00\x4F\x23ggml_nelements',0,b'\x00\x00\xBC\x23ggml_new_f32',0,b'\x00\x00\x76\x23ggml_new_graph',0,b'\x00\x00\xC0\x23ggml_new_i32',0,b'\x00\x00\x9C\x23ggml_new_tensor',0,b'\x00\x00\xA2\x23ggml_new_tensor_1d',0,b'\x00\x00\xA7\x23ggml_new_tensor_2d',0,b'\x00\x00\xAD\x23ggml_new_tensor_3d',0,b'\x00\x00\xB4\x23ggml_new_tensor_4d',0,b'\x00\x00\xC4\x23ggml_norm',0,b'\x00\x00\xC4\x23ggml_norm_inplace',0,b'\x00\x00\x4F\x23ggml_nrows',0,b'\x00\x02\xB6\x23ggml_numa_init',0,b'\x00\x00\x12\x23ggml_op_name',0,b'\x00\x00\x12\x23ggml_op_symbol',0,b'\x00\x00\x27\x23ggml_opt',0,b'\x00\x00\x91\x23ggml_opt_default_params',0,b'\x00\x02\x6B\x23ggml_opt_init',0,b'\x00\x00\x1B\x23ggml_opt_resume',0,b'\x00\x00\x20\x23ggml_opt_resume_g',0,b'\x00\x01\x4E\x23ggml_out_prod',0,b'\x00\x00\xFE\x23ggml_permute',0,b'\x00\x00\xC8\x23ggml_pool_1d',0,b'\x00\x00\xD0\x23ggml_pool_2d',0,b'\x00\x02\x78\x23ggml_print_object',0,b'\x00\x02\x75\x23ggml_print_objects',0,b'\x00\x00\x57\x23ggml_quantize_chunk',0,b'\x00\x00\x5F\x23ggml_quantize_q2_K',0,b'\x00\x00\x5F\x23ggml_quantize_q3_K',0,b'\x00\x00\x5F\x23ggml_quantize_q4_0',0,b'\x00\x00\x5F\x23ggml_quantize_q4_1',0,b'\x00\x00\x5F\x23ggml_quantize_q4_K',0,b'\x00\x00\x5F\x23ggml_quantize_q5_0',0,b'\x00\x00\x5F\x23ggml_quantize_q5_1',0,b'\x00\x00\x5F\x23ggml_quantize_q5_K',0,b'\x00\x00\x5F\x23ggml_quantize_q6_K',0,b'\x00\x00\x5F\x23ggml_quantize_q8_0',0,b'\x00\x00\xC4\x23ggml_relu',0,b'\x00\x00\xC4\x23ggml_relu_inplace',0,b'\x00\x01\x4E\x23ggml_repeat',0,b'\x00\x01\x4E\x23ggml_repeat_back',0,b'\x00\x01\x4E\x23ggml_reshape',0,b'\x00\x01\x10\x23ggml_reshape_1d',0,b'\x00\x01\x15\x23ggml_reshape_2d',0,b'\x00\x01\x1B\x23ggml_reshape_3d',0,b'\x00\x01\x22\x23ggml_reshape_4d',0,b'\x00\x00\xE0\x23ggml_rms_norm',0,b'\x00\x01\x4E\x23ggml_rms_norm_back',0,b'\x00\x00\xE0\x23ggml_rms_norm_inplace',0,b'\x00\x00\xFE\x23ggml_rope',0,b'\x00\x00\xFE\x23ggml_rope_back',0,b'\x00\x01\x06\x23ggml_rope_custom',0,b'\x00\x01\x06\x23ggml_rope_custom_inplace',0,b'\x00\x00\xFE\x23ggml_rope_inplace',0,b'\x00\x01\x4E\x23ggml_scale',0,b'\x00\x01\x4E\x23ggml_scale_inplace',0,b'\x00\x01\x7A\x23ggml_set',0,b'\x00\x01\x6D\x23ggml_set_1d',0,b'\x00\x01\x6D\x23ggml_set_1d_inplace',0,b'\x00\x01\x73\x23ggml_set_2d',0,b'\x00\x01\x73\x23ggml_set_2d_inplace',0,b'\x00\x01\xE4\x23ggml_set_f32',0,b'\x00\x02\xA2\x23ggml_set_f32_1d',0,b'\x00\x01\xE8\x23ggml_set_i32',0,b'\x00\x02\xA7\x23ggml_set_i32_1d',0,b'\x00\x01\x7A\x23ggml_set_inplace',0,b'\x00\x01\xDC\x23ggml_set_name',0,b'\x00\x02\x62\x23ggml_set_no_alloc',0,b'\x00\x02\x71\x23ggml_set_param',0,b'\x00\x00\x66\x23ggml_set_scratch',0,b'\x00\x01\xD9\x23ggml_set_zero',0,b'\x00\x00\xC4\x23ggml_sgn',0,b'\x00\x00\xC4\x23ggml_sgn_inplace',0,b'\x00\x00\xC4\x23ggml_silu',0,b'\x00\x01\x4E\x23ggml_silu_back',0,b'\x00\x00\xC4\x23ggml_silu_inplace',0,b'\x00\x00\xC4\x23ggml_soft_max',0,b'\x00\x01\x4E\x23ggml_soft_max_back',0,b'\x00\x01\x4E\x23ggml_soft_max_back_inplace',0,b'\x00\x00\xC4\x23ggml_soft_max_inplace',0,b'\x00\x00\xC4\x23ggml_sqr',0,b'\x00\x00\xC4\x23ggml_sqr_inplace',0,b'\x00\x00\xC4\x23ggml_sqrt',0,b'\x00\x00\xC4\x23ggml_sqrt_inplace',0,b'\x00\x00\xC4\x23ggml_step',0,b'\x00\x00\xC4\x23ggml_step_inplace',0,b'\x00\x01\x4E\x23ggml_sub',0,b'\x00\x01\x4E\x23ggml_sub_inplace',0,b'\x00\x00\xC4\x23ggml_sum',0,b'\x00\x00\xC4\x23ggml_sum_rows',0,b'\x00\x00\xC4\x23ggml_tanh',0,b'\x00\x00\xC4\x23ggml_tanh_inplace',0,b'\x00\x00\x74\x23ggml_tensor_overhead',0,b'\x00\x02\xB6\x23ggml_time_init',0,b'\x00\x00\x52\x23ggml_time_ms',0,b'\x00\x00\x52\x23ggml_time_us',0,b'\x00\x00\xC4\x23ggml_transpose',0,b'\x00\x00\x15\x23ggml_type_name',0,b'\x00\x00\x54\x23ggml_type_size',0,b'\x00\x00\x35\x23ggml_type_sizef',0,b'\x00\x00\xDB\x23ggml_unary',0,b'\x00\x00\xDB\x23ggml_unary_inplace',0,b'\x00\x00\x6A\x23ggml_used_mem',0,b'\x00\x02\x46\x23ggml_vec_dot_q2_K_q8_K',0,b'\x00\x02\x46\x23ggml_vec_dot_q3_K_q8_K',0,b'\x00\x02\x46\x23ggml_vec_dot_q4_K_q8_K',0,b'\x00\x02\x46\x23ggml_vec_dot_q5_K_q8_K',0,b'\x00\x02\x46\x23ggml_vec_dot_q6_K_q8_K',0,b'\x00\x01\x48\x23ggml_view_1d',0,b'\x00\x01\x40\x23ggml_view_2d',0,b'\x00\x01\x36\x23ggml_view_3d',0,b'\x00\x01\x2A\x23ggml_view_4d',0,b'\x00\x01\xD5\x23ggml_view_tensor',0,b'\x00\x00\xEB\x23ggml_win_part',0,b'\x00\x00\xF7\x23ggml_win_unpart',0,b'\x00\x02\x36\x23quantize_row_q2_K',0,b'\x00\x02\x13\x23quantize_row_q2_K_reference',0,b'\x00\x02\x36\x23quantize_row_q3_K',0,b'\x00\x02\x18\x23quantize_row_q3_K_reference',0,b'\x00\x02\x36\x23quantize_row_q4_K',0,b'\x00\x02\x1D\x23quantize_row_q4_K_reference',0,b'\x00\x02\x36\x23quantize_row_q5_K',0,b'\x00\x02\x22\x23quantize_row_q5_K_reference',0,b'\x00\x02\x36\x23quantize_row_q6_K',0,b'\x00\x02\x27\x23quantize_row_q6_K_reference',0,b'\x00\x02\x36\x23quantize_row_q8_K',0,b'\x00\x02\x2C\x23quantize_row_q8_K_reference',0),
    _struct_unions = ((b'\x00\x00\x02\xDA\x00\x00\x00\x02$1',b'\x00\x00\x3A\x11n_iter',b'\x00\x00\xBE\x11sched',b'\x00\x00\xBE\x11decay',b'\x00\x00\xBE\x11alpha',b'\x00\x00\xBE\x11beta1',b'\x00\x00\xBE\x11beta2',b'\x00\x00\xBE\x11eps',b'\x00\x00\xBE\x11eps_f',b'\x00\x00\xBE\x11eps_g'),(b'\x00\x00\x02\xDB\x00\x00\x00\x02$2',b'\x00\x00\x3A\x11m',b'\x00\x00\x3A\x11n_iter',b'\x00\x00\x3A\x11max_linesearch',b'\x00\x00\xBE\x11eps',b'\x00\x00\xBE\x11ftol',b'\x00\x00\xBE\x11wolfe',b'\x00\x00\xBE\x11min_step',b'\x00\x00\xBE\x11max_step',b'\x00\x02\xC5\x11linesearch'),(b'\x00\x00\x02\xDC\x00\x00\x00\x02$3',b'\x00\x00\x1E\x11x',b'\x00\x00\x1E\x11g1',b'\x00\x00\x1E\x11g2',b'\x00\x00\x1E\x11m',b'\x00\x00\x1E\x11v',b'\x00\x00\x1E\x11mh',b'\x00\x00\x1E\x11vh',b'\x00\x00\x1E\x11pf',b'\x00\x00\xBE\x11fx_best',b'\x00\x00\xBE\x11fx_prev',b'\x00\x00\x3A\x11n_no_improvement'),(b'\x00\x00\x02\xDD\x00\x00\x00\x02$4',b'\x00\x00\x1E\x11x',b'\x00\x00\x1E\x11xp',b'\x00\x00\x1E\x11g',b'\x00\x00\x1E\x11gp',b'\x00\x00\x1E\x11d',b'\x00\x00\x1E\x11pf',b'\x00\x00\x1E\x11lmal',b'\x00\x00\x1E\x11lmys',b'\x00\x00\x1E\x11lms',b'\x00\x00\x1E\x11lmy',b'\x00\x00\xBE\x11fx_best',b'\x00\x00\xBE\x11step',b'\x00\x00\x3A\x11j',b'\x00\x00\x3A\x11k',b'\x00\x00\x3A\x11end',b'\x00\x00\x3A\x11n_no_improvement'),(b'\x00\x00\x02\xB9\x00\x00\x00\x02$block_q2_K',b'\x00\x02\xF0\x11scales',b'\x00\x02\xF4\x11qs',b'\x00\x00\x3D\x11d',b'\x00\x00\x3D\x11dmin'),(b'\x00\x00\x02\xBA\x00\x00\x00\x02$block_q3_K',b'\x00\x02\xF2\x11hmask',b'\x00\x02\xF4\x11qs',b'\x00\x02\xEE\x11scales',b'\x00\x00\x3D\x11d'),(b'\x00\x00\x02\xBB\x00\x00\x00\x02$block_q4_K',b'\x00\x00\x3D\x11d',b'\x00\x00\x3D\x11dmin',b'\x00\x02\xEE\x11scales',b'\x00\x02\xEC\x11qs'),(b'\x00\x00\x02\xBC\x00\x00\x00\x02$block_q5_K',b'\x00\x00\x3D\x11d',b'\x00\x00\x3D\x11dmin',b'\x00\x02\xEE\x11scales',b'\x00\x02\xF2\x11qh',b'\x00\x02\xEC\x11qs'),(b'\x00\x00\x02\xBD\x00\x00\x00\x02$block_q6_K',b'\x00\x02\xEC\x11ql',b'\x00\x02\xF4\x11qh',b'\x00\x02\xD2\x11scales',b'\x00\x00\x3D\x11d'),(b'\x00\x00\x02\xBE\x00\x00\x00\x02$block_q8_K',b'\x00\x00\xBE\x11d',b'\x00\x02\xD4\x11qs',b'\x00\x02\xCB\x11bsums'),(b'\x00\x00\x02\xC9\x00\x00\x00\x02$ggml_type_traits_t',b'\x00\x02\xFA\x11to_float',b'\x00\x02\xF8\x11from_float',b'\x00\x02\xF8\x11from_float_reference',b'\x00\x02\xF9\x11vec_dot',b'\x00\x00\x01\x11vec_dot_type'),(b'\x00\x00\x02\xDE\x00\x00\x00\x02ggml_cgraph',b'\x00\x00\x3A\x11n_nodes',b'\x00\x00\x3A\x11n_leafs',b'\x00\x02\xE5\x11nodes',b'\x00\x02\xE5\x11grads',b'\x00\x02\xE5\x11leafs',b'\x00\x02\xF6\x11visited_hash_table',b'\x00\x00\x3A\x11perf_runs',b'\x00\x00\xA5\x11perf_cycles',b'\x00\x00\xA5\x11perf_time_us'),(b'\x00\x00\x02\xDF\x00\x00\x00\x02ggml_compute_params',b'\x00\x02\xC8\x11type',b'\x00\x00\x3A\x11ith',b'\x00\x00\x3A\x11nth',b'\x00\x01\x31\x11wsize',b'\x00\x00\x0E\x11wdata'),(b'\x00\x00\x02\xE0\x00\x00\x00\x10ggml_context',),(b'\x00\x00\x02\xE1\x00\x00\x00\x02ggml_cplan',b'\x00\x01\x31\x11work_size',b'\x00\x02\xEA\x11work_data',b'\x00\x00\x3A\x11n_threads',b'\x00\x02\xD6\x11n_tasks',b'\x00\x02\xB8\x11abort_callback',b'\x00\x00\x0E\x11abort_callback_data'),(b'\x00\x00\x00\x8B\x00\x00\x00\x02ggml_init_params',b'\x00\x01\x31\x11mem_size',b'\x00\x00\x0E\x11mem_buffer',b'\x00\x00\x85\x11no_alloc'),(b'\x00\x00\x02\xE3\x00\x00\x00\x02ggml_object',b'\x00\x01\x31\x11offs',b'\x00\x01\x31\x11size',b'\x00\x02\xE2\x11next',b'\x00\x02\xC6\x11type',b'\x00\x02\xC2\x11padding'),(b'\x00\x00\x02\xE4\x00\x00\x00\x02ggml_opt_context',b'\x00\x00\x04\x11ctx',b'\x00\x00\x29\x11params',b'\x00\x00\x3A\x11iter',b'\x00\x00\xA5\x11nx',b'\x00\x00\x85\x11just_initialized',b'\x00\x02\xDC\x11adam',b'\x00\x02\xDD\x11lbfgs'),(b'\x00\x00\x00\x29\x00\x00\x00\x02ggml_opt_params',b'\x00\x00\x92\x11type',b'\x00\x00\x3A\x11n_threads',b'\x00\x00\x3A\x11past',b'\x00\x00\xBE\x11delta',b'\x00\x00\x3A\x11max_no_improvement',b'\x00\x00\x85\x11print_forward_graph',b'\x00\x00\x85\x11print_backward_graph',b'\x00\x02\xDA\x11adam',b'\x00\x02\xDB\x11lbfgs'),(b'\x00\x00\x00\x68\x00\x00\x00\x02ggml_scratch',b'\x00\x01\x31\x11offs',b'\x00\x01\x31\x11size',b'\x00\x00\x0E\x11data'),(b'\x00\x00\x02\xE9\x00\x00\x00\x02ggml_tensor',b'\x00\x00\x01\x11type',b'\x00\x02\xC4\x11backend',b'\x00\x00\x3A\x11n_dims',b'\x00\x02\xCF\x11ne',b'\x00\x02\xD8\x11nb',b'\x00\x00\x13\x11op',b'\x00\x02\xCD\x11op_params',b'\x00\x00\x85\x11is_param',b'\x00\x00\x1E\x11grad',b'\x00\x02\xE7\x11src',b'\x00\x00\x3A\x11perf_runs',b'\x00\x00\xA5\x11perf_cycles',b'\x00\x00\xA5\x11perf_time_us',b'\x00\x00\x0E\x11data',b'\x00\x02\xC0\x11name',b'\x00\x00\x0E\x11extra',b'\x00\x02\xC2\x11padding')),
    _enums = (b'\x00\x00\x02\xC4\x00\x00\x00\x16ggml_backend\x00GGML_BACKEND_CPU,GGML_BACKEND_GPU,GGML_BACKEND_GPU_SPLIT',b'\x00\x00\x00\x2D\x00\x00\x00\x15ggml_ftype\x00GGML_FTYPE_UNKNOWN,GGML_FTYPE_ALL_F32,GGML_FTYPE_MOSTLY_F16,GGML_FTYPE_MOSTLY_Q4_0,GGML_FTYPE_MOSTLY_Q4_1,GGML_FTYPE_MOSTLY_Q4_1_SOME_F16,GGML_FTYPE_MOSTLY_Q8_0,GGML_FTYPE_MOSTLY_Q5_0,GGML_FTYPE_MOSTLY_Q5_1,GGML_FTYPE_MOSTLY_Q2_K,GGML_FTYPE_MOSTLY_Q3_K,GGML_FTYPE_MOSTLY_Q4_K,GGML_FTYPE_MOSTLY_Q5_K,GGML_FTYPE_MOSTLY_Q6_K',b'\x00\x00\x02\xC5\x00\x00\x00\x16ggml_linesearch\x00GGML_LINESEARCH_DEFAULT,GGML_LINESEARCH_BACKTRACKING_ARMIJO,GGML_LINESEARCH_BACKTRACKING_WOLFE,GGML_LINESEARCH_BACKTRACKING_STRONG_WOLFE',b'\x00\x00\x02\xC6\x00\x00\x00\x16ggml_object_type\x00GGML_OBJECT_TENSOR,GGML_OBJECT_GRAPH,GGML_OBJECT_WORK_BUFFER',b'\x00\x00\x00\x13\x00\x00\x00\x16ggml_op\x00GGML_OP_NONE,GGML_OP_DUP,GGML_OP_ADD,GGML_OP_ADD1,GGML_OP_ACC,GGML_OP_SUB,GGML_OP_MUL,GGML_OP_DIV,GGML_OP_SQR,GGML_OP_SQRT,GGML_OP_LOG,GGML_OP_SUM,GGML_OP_SUM_ROWS,GGML_OP_MEAN,GGML_OP_ARGMAX,GGML_OP_REPEAT,GGML_OP_REPEAT_BACK,GGML_OP_SILU_BACK,GGML_OP_NORM,GGML_OP_RMS_NORM,GGML_OP_RMS_NORM_BACK,GGML_OP_MUL_MAT,GGML_OP_OUT_PROD,GGML_OP_SCALE,GGML_OP_SET,GGML_OP_CPY,GGML_OP_CONT,GGML_OP_RESHAPE,GGML_OP_VIEW,GGML_OP_PERMUTE,GGML_OP_TRANSPOSE,GGML_OP_GET_ROWS,GGML_OP_GET_ROWS_BACK,GGML_OP_DIAG,GGML_OP_DIAG_MASK_INF,GGML_OP_DIAG_MASK_ZERO,GGML_OP_SOFT_MAX,GGML_OP_SOFT_MAX_BACK,GGML_OP_ROPE,GGML_OP_ROPE_BACK,GGML_OP_ALIBI,GGML_OP_CLAMP,GGML_OP_CONV_1D,GGML_OP_CONV_2D,GGML_OP_POOL_1D,GGML_OP_POOL_2D,GGML_OP_FLASH_ATTN,GGML_OP_FLASH_FF,GGML_OP_FLASH_ATTN_BACK,GGML_OP_WIN_PART,GGML_OP_WIN_UNPART,GGML_OP_UNARY,GGML_OP_MAP_UNARY,GGML_OP_MAP_BINARY,GGML_OP_MAP_CUSTOM1_F32,GGML_OP_MAP_CUSTOM2_F32,GGML_OP_MAP_CUSTOM3_F32,GGML_OP_MAP_CUSTOM1,GGML_OP_MAP_CUSTOM2,GGML_OP_MAP_CUSTOM3,GGML_OP_CROSS_ENTROPY_LOSS,GGML_OP_CROSS_ENTROPY_LOSS_BACK,GGML_OP_COUNT',b'\x00\x00\x00\xCB\x00\x00\x00\x16ggml_op_pool\x00GGML_OP_POOL_MAX,GGML_OP_POOL_AVG,GGML_OP_POOL_COUNT',b'\x00\x00\x02\xC7\x00\x00\x00\x15ggml_opt_result\x00GGML_OPT_OK,GGML_OPT_DID_NOT_CONVERGE,GGML_OPT_NO_CONTEXT,GGML_OPT_INVALID_WOLFE,GGML_OPT_FAIL,GGML_LINESEARCH_FAIL,GGML_LINESEARCH_MINIMUM_STEP,GGML_LINESEARCH_MAXIMUM_STEP,GGML_LINESEARCH_MAXIMUM_ITERATIONS,GGML_LINESEARCH_INVALID_PARAMETERS',b'\x00\x00\x00\x92\x00\x00\x00\x16ggml_opt_type\x00GGML_OPT_ADAM,GGML_OPT_LBFGS',b'\x00\x00\x02\xC8\x00\x00\x00\x16ggml_task_type\x00GGML_TASK_INIT,GGML_TASK_COMPUTE,GGML_TASK_FINALIZE',b'\x00\x00\x00\x01\x00\x00\x00\x16ggml_type\x00GGML_TYPE_F32,GGML_TYPE_F16,GGML_TYPE_Q4_0,GGML_TYPE_Q4_1,GGML_TYPE_Q5_0,GGML_TYPE_Q5_1,GGML_TYPE_Q8_0,GGML_TYPE_Q8_1,GGML_TYPE_Q2_K,GGML_TYPE_Q3_K,GGML_TYPE_Q4_K,GGML_TYPE_Q5_K,GGML_TYPE_Q6_K,GGML_TYPE_Q8_K,GGML_TYPE_I8,GGML_TYPE_I16,GGML_TYPE_I32,GGML_TYPE_COUNT',b'\x00\x00\x00\xDE\x00\x00\x00\x16ggml_unary_op\x00GGML_UNARY_OP_ABS,GGML_UNARY_OP_SGN,GGML_UNARY_OP_NEG,GGML_UNARY_OP_STEP,GGML_UNARY_OP_TANH,GGML_UNARY_OP_ELU,GGML_UNARY_OP_RELU,GGML_UNARY_OP_GELU,GGML_UNARY_OP_GELU_QUICK,GGML_UNARY_OP_SILU'),
    _typenames = (b'\x00\x00\x00\x3D__fp16',b'\x00\x00\x02\xB9block_q2_K',b'\x00\x00\x02\xBAblock_q3_K',b'\x00\x00\x02\xBBblock_q4_K',b'\x00\x00\x02\xBCblock_q5_K',b'\x00\x00\x02\xBDblock_q6_K',b'\x00\x00\x02\xBEblock_q8_K',b'\x00\x00\x01\xB4ggml_binary_op_f32_t',b'\x00\x00\x01\xCCggml_custom1_op_f32_t',b'\x00\x00\x01\xD1ggml_custom1_op_t',b'\x00\x00\x01\xBAggml_custom2_op_f32_t',b'\x00\x00\x01\xC0ggml_custom2_op_t',b'\x00\x00\x01\xA5ggml_custom3_op_f32_t',b'\x00\x00\x01\xACggml_custom3_op_t',b'\x00\x00\x00\x3Dggml_fp16_t',b'\x00\x00\x02\xF8ggml_from_float_t',b'\x00\x00\x02\xFAggml_to_float_t',b'\x00\x00\x02\xC9ggml_type_traits_t',b'\x00\x00\x01\xC7ggml_unary_op_f32_t',b'\x00\x00\x02\xF9ggml_vec_dot_t'),
)
