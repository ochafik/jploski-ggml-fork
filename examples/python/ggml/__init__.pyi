#
# AUTOGENERATED STUB FILE, DO NOT EDIT
# TO REGENERATE, RUN:
#
#     python generate.py
#
import ggml.ffi as ffi

# ggml library (cffi bindings)
class lib:
  # GGML_API bool ggml_are_same_shape(const struct ggml_tensor * t0, const struct ggml_tensor * t1);
  def ggml_are_same_shape(t0: ffi.CData, t1: ffi.CData) -> bool: ...

  # GGML_API bool ggml_get_no_alloc(struct ggml_context * ctx);
  def ggml_get_no_alloc(ctx: ffi.CData) -> bool: ...

  # GGML_API bool ggml_is_contiguous(const struct ggml_tensor * tensor);
  def ggml_is_contiguous(tensor: ffi.CData) -> bool: ...

  # GGML_API bool ggml_is_numa();
  def ggml_is_numa() -> bool: ...

  # GGML_API bool ggml_is_permuted (const struct ggml_tensor * tensor);
  def ggml_is_permuted(tensor: ffi.CData) -> bool: ...

  # GGML_API bool ggml_is_quantized(enum ggml_type type);
  def ggml_is_quantized(type: int) -> bool: ...

  # GGML_API bool ggml_is_transposed(const struct ggml_tensor * tensor);
  def ggml_is_transposed(tensor: ffi.CData) -> bool: ...

  # GGML_API const char * ggml_get_name (const struct ggml_tensor * tensor);
  def ggml_get_name(tensor: ffi.CData) -> ffi.CData: ...

  # GGML_API const char * ggml_op_name (enum ggml_op op);
  def ggml_op_name(op: int) -> ffi.CData: ...

  # GGML_API const char * ggml_op_symbol(enum ggml_op op);
  def ggml_op_symbol(op: int) -> ffi.CData: ...

  # GGML_API const char * ggml_type_name(enum ggml_type type);
  def ggml_type_name(type: int) -> ffi.CData: ...

  # GGML_API enum ggml_opt_result ggml_opt(struct ggml_context * ctx,struct ggml_opt_params params,struct ggml_tensor * f);
  def ggml_opt(ctx: ffi.CData, params: ffi.CData, f: ffi.CData) -> int: ...

  # GGML_API enum ggml_opt_result ggml_opt_resume(struct ggml_context * ctx,struct ggml_opt_context * opt,struct ggml_tensor * f);
  def ggml_opt_resume(ctx: ffi.CData, opt: ffi.CData, f: ffi.CData) -> int: ...

  # GGML_API enum ggml_opt_result ggml_opt_resume_g(struct ggml_context * ctx,struct ggml_opt_context * opt,struct ggml_tensor * f,struct ggml_cgraph * gf,struct ggml_cgraph * gb);
  def ggml_opt_resume_g(ctx: ffi.CData, opt: ffi.CData, f: ffi.CData, gf: ffi.CData, gb: ffi.CData) -> int: ...

  # GGML_API enum ggml_type ggml_ftype_to_ggml_type(enum ggml_ftype ftype);
  def ggml_ftype_to_ggml_type(ftype: int) -> int: ...

  # GGML_API enum ggml_unary_op ggml_get_unary_op(const struct ggml_tensor * tensor);
  def ggml_get_unary_op(tensor: ffi.CData) -> int: ...

  # GGML_API float * ggml_get_data_f32(const struct ggml_tensor * tensor);
  def ggml_get_data_f32(tensor: ffi.CData) -> ffi.CData: ...

  # GGML_API float ggml_fp16_to_fp32(ggml_fp16_t x);
  def ggml_fp16_to_fp32(x) -> float: ...

  # GGML_API float ggml_get_f32_1d(const struct ggml_tensor * tensor, int i);
  def ggml_get_f32_1d(tensor: ffi.CData, i: int) -> float: ...

  # GGML_API float ggml_type_sizef(enum ggml_type type);
  def ggml_type_sizef(type: int) -> float: ...

  # GGML_API ggml_fp16_t ggml_fp32_to_fp16(float x);
  def ggml_fp32_to_fp16(x: float): ...

  # GGML_API int ggml_blck_size (enum ggml_type type);
  def ggml_blck_size(type: int) -> int: ...

  # GGML_API int ggml_cpu_has_arm_fma ();
  def ggml_cpu_has_arm_fma() -> int: ...

  # GGML_API int ggml_cpu_has_avx ();
  def ggml_cpu_has_avx() -> int: ...

  # GGML_API int ggml_cpu_has_avx2 ();
  def ggml_cpu_has_avx2() -> int: ...

  # GGML_API int ggml_cpu_has_avx512 ();
  def ggml_cpu_has_avx512() -> int: ...

  # GGML_API int ggml_cpu_has_avx512_vbmi();
  def ggml_cpu_has_avx512_vbmi() -> int: ...

  # GGML_API int ggml_cpu_has_avx512_vnni();
  def ggml_cpu_has_avx512_vnni() -> int: ...

  # GGML_API int ggml_cpu_has_blas ();
  def ggml_cpu_has_blas() -> int: ...

  # GGML_API int ggml_cpu_has_clblast ();
  def ggml_cpu_has_clblast() -> int: ...

  # GGML_API int ggml_cpu_has_cublas ();
  def ggml_cpu_has_cublas() -> int: ...

  # GGML_API int ggml_cpu_has_f16c ();
  def ggml_cpu_has_f16c() -> int: ...

  # GGML_API int ggml_cpu_has_fma ();
  def ggml_cpu_has_fma() -> int: ...

  # GGML_API int ggml_cpu_has_fp16_va ();
  def ggml_cpu_has_fp16_va() -> int: ...

  # GGML_API int ggml_cpu_has_gpublas ();
  def ggml_cpu_has_gpublas() -> int: ...

  # GGML_API int ggml_cpu_has_neon ();
  def ggml_cpu_has_neon() -> int: ...

  # GGML_API int ggml_cpu_has_sse3 ();
  def ggml_cpu_has_sse3() -> int: ...

  # GGML_API int ggml_cpu_has_vsx ();
  def ggml_cpu_has_vsx() -> int: ...

  # GGML_API int ggml_cpu_has_wasm_simd ();
  def ggml_cpu_has_wasm_simd() -> int: ...

  # GGML_API int ggml_graph_compute(struct ggml_cgraph * cgraph, struct ggml_cplan * cplan);
  def ggml_graph_compute(cgraph: ffi.CData, cplan: ffi.CData) -> int: ...

  # GGML_API int32_t ggml_get_i32_1d(const struct ggml_tensor * tensor, int i);
  def ggml_get_i32_1d(tensor: ffi.CData, i: int) -> int: ...

  # GGML_API int64_t ggml_cycles();
  def ggml_cycles() -> int: ...

  # GGML_API int64_t ggml_cycles_per_ms();
  def ggml_cycles_per_ms() -> int: ...

  # GGML_API int64_t ggml_nelements (const struct ggml_tensor * tensor);
  def ggml_nelements(tensor: ffi.CData) -> int: ...

  # GGML_API int64_t ggml_nrows (const struct ggml_tensor * tensor);
  def ggml_nrows(tensor: ffi.CData) -> int: ...

  # GGML_API int64_t ggml_time_ms();
  def ggml_time_ms() -> int: ...

  # GGML_API int64_t ggml_time_us();
  def ggml_time_us() -> int: ...

  # GGML_API size_t ggml_element_size(const struct ggml_tensor * tensor);
  def ggml_element_size(tensor: ffi.CData) -> int: ...

  # GGML_API size_t ggml_get_max_tensor_size(const struct ggml_context * ctx);
  def ggml_get_max_tensor_size(ctx: ffi.CData) -> int: ...

  # GGML_API size_t ggml_get_mem_size (const struct ggml_context * ctx);
  def ggml_get_mem_size(ctx: ffi.CData) -> int: ...

  # GGML_API size_t ggml_graph_overhead();
  def ggml_graph_overhead() -> int: ...

  # GGML_API size_t ggml_nbytes (const struct ggml_tensor * tensor);
  def ggml_nbytes(tensor: ffi.CData) -> int: ...

  # GGML_API size_t ggml_nbytes_split(const struct ggml_tensor * tensor, int nrows_split);
  def ggml_nbytes_split(tensor: ffi.CData, nrows_split: int) -> int: ...

  # GGML_API size_t ggml_quantize_chunk(enum ggml_type type, const float * src, void * dst, int start, int n, int64_t * hist);
  def ggml_quantize_chunk(type: int, src: ffi.CData, dst: ffi.CData, start: int, n: int, hist: ffi.CData) -> int: ...

  # GGML_API size_t ggml_quantize_q4_0(const float * src, void * dst, int n, int k, int64_t * hist);
  def ggml_quantize_q4_0(src: ffi.CData, dst: ffi.CData, n: int, k: int, hist: ffi.CData) -> int: ...

  # GGML_API size_t ggml_quantize_q4_1(const float * src, void * dst, int n, int k, int64_t * hist);
  def ggml_quantize_q4_1(src: ffi.CData, dst: ffi.CData, n: int, k: int, hist: ffi.CData) -> int: ...

  # GGML_API size_t ggml_quantize_q5_0(const float * src, void * dst, int n, int k, int64_t * hist);
  def ggml_quantize_q5_0(src: ffi.CData, dst: ffi.CData, n: int, k: int, hist: ffi.CData) -> int: ...

  # GGML_API size_t ggml_quantize_q5_1(const float * src, void * dst, int n, int k, int64_t * hist);
  def ggml_quantize_q5_1(src: ffi.CData, dst: ffi.CData, n: int, k: int, hist: ffi.CData) -> int: ...

  # GGML_API size_t ggml_quantize_q8_0(const float * src, void * dst, int n, int k, int64_t * hist);
  def ggml_quantize_q8_0(src: ffi.CData, dst: ffi.CData, n: int, k: int, hist: ffi.CData) -> int: ...

  # GGML_API size_t ggml_set_scratch (struct ggml_context * ctx, struct ggml_scratch scratch);
  def ggml_set_scratch(ctx: ffi.CData, scratch: ffi.CData) -> int: ...

  # GGML_API size_t ggml_tensor_overhead();
  def ggml_tensor_overhead() -> int: ...

  # GGML_API size_t ggml_type_size (enum ggml_type type);
  def ggml_type_size(type: int) -> int: ...

  # GGML_API size_t ggml_used_mem(const struct ggml_context * ctx);
  def ggml_used_mem(ctx: ffi.CData) -> int: ...

  # GGML_API struct ggml_cgraph * ggml_build_forward_ctx(struct ggml_context * ctx, struct ggml_tensor * tensor);
  def ggml_build_forward_ctx(ctx: ffi.CData, tensor: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_cgraph * ggml_new_graph (struct ggml_context * ctx);
  def ggml_new_graph(ctx: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_cgraph ggml_build_backward(struct ggml_context * ctx, struct ggml_cgraph * gf, bool keep);
  def ggml_build_backward(ctx: ffi.CData, gf: ffi.CData, keep: bool) -> ffi.CData: ...

  # GGML_API struct ggml_cgraph ggml_build_forward (struct ggml_tensor * tensor);
  def ggml_build_forward(tensor: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_cgraph ggml_graph_import(const char * fname, struct ggml_context ** ctx_data, struct ggml_context ** ctx_eval);
  def ggml_graph_import(fname: ffi.CData, ctx_data: ffi.CData, ctx_eval: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_context * ggml_init(struct ggml_init_params params);
  def ggml_init(params: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_cplan ggml_graph_plan (struct ggml_cgraph * cgraph, int n_threads );
  def ggml_graph_plan(cgraph: ffi.CData, n_threads: int) -> ffi.CData: ...

  # GGML_API struct ggml_opt_params ggml_opt_default_params(enum ggml_opt_type type);
  def ggml_opt_default_params(type: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_abs(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_abs(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_abs_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_abs_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_acc(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,size_t nb1,size_t nb2,size_t nb3,size_t offset);
  def ggml_acc(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, nb1: int, nb2: int, nb3: int, offset: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_acc_inplace(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,size_t nb1,size_t nb2,size_t nb3,size_t offset);
  def ggml_acc_inplace(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, nb1: int, nb2: int, nb3: int, offset: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_add(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_add(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_add1(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_add1(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_add1_inplace(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_add1_inplace(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_add_inplace(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_add_inplace(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_argmax(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_argmax(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_cont(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_cont(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_cont_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_cont_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_conv_1d(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,int s0,int p0,int d0);
  def ggml_conv_1d(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, s0: int, p0: int, d0: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_conv_1d_ph(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,int s,int d);
  def ggml_conv_1d_ph(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, s: int, d: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_conv_2d(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,int s0,int s1,int p0,int p1,int d0,int d1);
  def ggml_conv_2d(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, s0: int, s1: int, p0: int, p1: int, d0: int, d1: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_cpy(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_cpy(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_cpy_inplace(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_cpy_inplace(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_cross_entropy_loss(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_cross_entropy_loss(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_cross_entropy_loss_back(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,struct ggml_tensor * c);
  def ggml_cross_entropy_loss_back(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, c: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_diag(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_diag(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_diag_mask_inf(struct ggml_context * ctx,struct ggml_tensor * a,int n_past);
  def ggml_diag_mask_inf(ctx: ffi.CData, a: ffi.CData, n_past: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_diag_mask_inf_inplace(struct ggml_context * ctx,struct ggml_tensor * a,int n_past);
  def ggml_diag_mask_inf_inplace(ctx: ffi.CData, a: ffi.CData, n_past: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_diag_mask_zero(struct ggml_context * ctx,struct ggml_tensor * a,int n_past);
  def ggml_diag_mask_zero(ctx: ffi.CData, a: ffi.CData, n_past: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_diag_mask_zero_inplace(struct ggml_context * ctx,struct ggml_tensor * a,int n_past);
  def ggml_diag_mask_zero_inplace(ctx: ffi.CData, a: ffi.CData, n_past: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_div(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_div(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_div_inplace(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_div_inplace(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_dup(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_dup(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_dup_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_dup_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_dup_tensor (struct ggml_context * ctx, const struct ggml_tensor * src);
  def ggml_dup_tensor(ctx: ffi.CData, src: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_elu(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_elu(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_elu_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_elu_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_flash_attn(struct ggml_context * ctx,struct ggml_tensor * q,struct ggml_tensor * k,struct ggml_tensor * v,bool masked);
  def ggml_flash_attn(ctx: ffi.CData, q: ffi.CData, k: ffi.CData, v: ffi.CData, masked: bool) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_flash_attn_back(struct ggml_context * ctx,struct ggml_tensor * q,struct ggml_tensor * k,struct ggml_tensor * v,struct ggml_tensor * d,bool masked);
  def ggml_flash_attn_back(ctx: ffi.CData, q: ffi.CData, k: ffi.CData, v: ffi.CData, d: ffi.CData, masked: bool) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_flash_ff(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b0,struct ggml_tensor * b1,struct ggml_tensor * c0,struct ggml_tensor * c1);
  def ggml_flash_ff(ctx: ffi.CData, a: ffi.CData, b0: ffi.CData, b1: ffi.CData, c0: ffi.CData, c1: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_format_name( struct ggml_tensor * tensor, const char * fmt, ...);
  def ggml_format_name(tensor: ffi.CData, fmt: ffi.CData, *args) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_gelu(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_gelu(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_gelu_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_gelu_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_gelu_quick(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_gelu_quick(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_gelu_quick_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_gelu_quick_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_get_rows(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_get_rows(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_get_rows_back(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,struct ggml_tensor * c);
  def ggml_get_rows_back(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, c: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_get_tensor(struct ggml_context * ctx, const char * name);
  def ggml_get_tensor(ctx: ffi.CData, name: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_graph_get_tensor(struct ggml_cgraph * cgraph, const char * name);
  def ggml_graph_get_tensor(cgraph: ffi.CData, name: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_log(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_log(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_log_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_log_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_map_custom1(struct ggml_context * ctx,struct ggml_tensor * a,ggml_custom1_op_t fun,int n_tasks,void * userdata);
  def ggml_map_custom1(ctx: ffi.CData, a: ffi.CData, fun, n_tasks: int, userdata: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_map_custom1_inplace(struct ggml_context * ctx,struct ggml_tensor * a,ggml_custom1_op_t fun,int n_tasks,void * userdata);
  def ggml_map_custom1_inplace(ctx: ffi.CData, a: ffi.CData, fun, n_tasks: int, userdata: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_map_custom2(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,ggml_custom2_op_t fun,int n_tasks,void * userdata);
  def ggml_map_custom2(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, fun, n_tasks: int, userdata: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_map_custom2_inplace(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,ggml_custom2_op_t fun,int n_tasks,void * userdata);
  def ggml_map_custom2_inplace(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, fun, n_tasks: int, userdata: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_map_custom3(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,struct ggml_tensor * c,ggml_custom3_op_t fun,int n_tasks,void * userdata);
  def ggml_map_custom3(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, c: ffi.CData, fun, n_tasks: int, userdata: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_map_custom3_inplace(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,struct ggml_tensor * c,ggml_custom3_op_t fun,int n_tasks,void * userdata);
  def ggml_map_custom3_inplace(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, c: ffi.CData, fun, n_tasks: int, userdata: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_mean(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_mean(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_mul(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_mul(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_mul_inplace(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_mul_inplace(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_mul_mat(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_mul_mat(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_neg(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_neg(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_neg_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_neg_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_new_f32(struct ggml_context * ctx, float value);
  def ggml_new_f32(ctx: ffi.CData, value: float) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_new_i32(struct ggml_context * ctx, int32_t value);
  def ggml_new_i32(ctx: ffi.CData, value: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_new_tensor(struct ggml_context * ctx,enum ggml_type type,int n_dims,const int64_t *ne);
  def ggml_new_tensor(ctx: ffi.CData, type: int, n_dims: int, ne: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_new_tensor_1d(struct ggml_context * ctx,enum ggml_type type,int64_t ne0);
  def ggml_new_tensor_1d(ctx: ffi.CData, type: int, ne0: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_new_tensor_2d(struct ggml_context * ctx,enum ggml_type type,int64_t ne0,int64_t ne1);
  def ggml_new_tensor_2d(ctx: ffi.CData, type: int, ne0: int, ne1: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_new_tensor_3d(struct ggml_context * ctx,enum ggml_type type,int64_t ne0,int64_t ne1,int64_t ne2);
  def ggml_new_tensor_3d(ctx: ffi.CData, type: int, ne0: int, ne1: int, ne2: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_new_tensor_4d(struct ggml_context * ctx,enum ggml_type type,int64_t ne0,int64_t ne1,int64_t ne2,int64_t ne3);
  def ggml_new_tensor_4d(ctx: ffi.CData, type: int, ne0: int, ne1: int, ne2: int, ne3: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_norm(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_norm(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_norm_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_norm_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_out_prod(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_out_prod(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_permute(struct ggml_context * ctx,struct ggml_tensor * a,int axis0,int axis1,int axis2,int axis3);
  def ggml_permute(ctx: ffi.CData, a: ffi.CData, axis0: int, axis1: int, axis2: int, axis3: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_pool_1d(struct ggml_context * ctx,struct ggml_tensor * a,enum ggml_op_pool op,int k0,int s0,int p0);
  def ggml_pool_1d(ctx: ffi.CData, a: ffi.CData, op: int, k0: int, s0: int, p0: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_pool_2d(struct ggml_context * ctx,struct ggml_tensor * a,enum ggml_op_pool op,int k0,int k1,int s0,int s1,int p0,int p1);
  def ggml_pool_2d(ctx: ffi.CData, a: ffi.CData, op: int, k0: int, k1: int, s0: int, s1: int, p0: int, p1: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_relu(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_relu(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_relu_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_relu_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_repeat(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_repeat(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_repeat_back(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_repeat_back(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_reshape(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_reshape(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_reshape_1d(struct ggml_context * ctx,struct ggml_tensor * a,int64_t ne0);
  def ggml_reshape_1d(ctx: ffi.CData, a: ffi.CData, ne0: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_reshape_2d(struct ggml_context * ctx,struct ggml_tensor * a,int64_t ne0,int64_t ne1);
  def ggml_reshape_2d(ctx: ffi.CData, a: ffi.CData, ne0: int, ne1: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_reshape_3d(struct ggml_context * ctx,struct ggml_tensor * a,int64_t ne0,int64_t ne1,int64_t ne2);
  def ggml_reshape_3d(ctx: ffi.CData, a: ffi.CData, ne0: int, ne1: int, ne2: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_reshape_4d(struct ggml_context * ctx,struct ggml_tensor * a,int64_t ne0,int64_t ne1,int64_t ne2,int64_t ne3);
  def ggml_reshape_4d(ctx: ffi.CData, a: ffi.CData, ne0: int, ne1: int, ne2: int, ne3: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_rms_norm(struct ggml_context * ctx,struct ggml_tensor * a,float eps);
  def ggml_rms_norm(ctx: ffi.CData, a: ffi.CData, eps: float) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_rms_norm_back(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_rms_norm_back(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_rms_norm_inplace(struct ggml_context * ctx,struct ggml_tensor * a,float eps);
  def ggml_rms_norm_inplace(ctx: ffi.CData, a: ffi.CData, eps: float) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_rope(struct ggml_context * ctx,struct ggml_tensor * a,int n_past,int n_dims,int mode,int n_ctx);
  def ggml_rope(ctx: ffi.CData, a: ffi.CData, n_past: int, n_dims: int, mode: int, n_ctx: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_rope_back(struct ggml_context * ctx,struct ggml_tensor * a,int n_past,int n_dims,int mode,int n_ctx);
  def ggml_rope_back(ctx: ffi.CData, a: ffi.CData, n_past: int, n_dims: int, mode: int, n_ctx: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_rope_custom(struct ggml_context * ctx,struct ggml_tensor * a,int n_past,int n_dims,int mode,int n_ctx,float freq_base,float freq_scale);
  def ggml_rope_custom(ctx: ffi.CData, a: ffi.CData, n_past: int, n_dims: int, mode: int, n_ctx: int, freq_base: float, freq_scale: float) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_rope_custom_inplace(struct ggml_context * ctx,struct ggml_tensor * a,int n_past,int n_dims,int mode,int n_ctx,float freq_base,float freq_scale);
  def ggml_rope_custom_inplace(ctx: ffi.CData, a: ffi.CData, n_past: int, n_dims: int, mode: int, n_ctx: int, freq_base: float, freq_scale: float) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_rope_inplace(struct ggml_context * ctx,struct ggml_tensor * a,int n_past,int n_dims,int mode,int n_ctx);
  def ggml_rope_inplace(ctx: ffi.CData, a: ffi.CData, n_past: int, n_dims: int, mode: int, n_ctx: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_scale(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_scale(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_scale_inplace(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_scale_inplace(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_set(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,size_t nb1,size_t nb2,size_t nb3,size_t offset);
  def ggml_set(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, nb1: int, nb2: int, nb3: int, offset: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_set_1d(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,size_t offset);
  def ggml_set_1d(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, offset: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_set_1d_inplace(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,size_t offset);
  def ggml_set_1d_inplace(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, offset: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_set_2d(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,size_t nb1,size_t offset);
  def ggml_set_2d(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, nb1: int, offset: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_set_2d_inplace(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,size_t nb1,size_t offset);
  def ggml_set_2d_inplace(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, nb1: int, offset: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_set_f32 (struct ggml_tensor * tensor, float value);
  def ggml_set_f32(tensor: ffi.CData, value: float) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_set_i32 (struct ggml_tensor * tensor, int32_t value);
  def ggml_set_i32(tensor: ffi.CData, value: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_set_inplace(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b,size_t nb1,size_t nb2,size_t nb3,size_t offset);
  def ggml_set_inplace(ctx: ffi.CData, a: ffi.CData, b: ffi.CData, nb1: int, nb2: int, nb3: int, offset: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_set_name ( struct ggml_tensor * tensor, const char * name);
  def ggml_set_name(tensor: ffi.CData, name: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_set_zero(struct ggml_tensor * tensor);
  def ggml_set_zero(tensor: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_sgn(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_sgn(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_sgn_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_sgn_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_silu(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_silu(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_silu_back(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_silu_back(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_silu_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_silu_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_soft_max(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_soft_max(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_soft_max_back(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_soft_max_back(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_soft_max_back_inplace(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_soft_max_back_inplace(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_soft_max_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_soft_max_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_sqr(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_sqr(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_sqr_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_sqr_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_sqrt(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_sqrt(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_sqrt_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_sqrt_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_step(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_step(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_step_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_step_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_sub(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_sub(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_sub_inplace(struct ggml_context * ctx,struct ggml_tensor * a,struct ggml_tensor * b);
  def ggml_sub_inplace(ctx: ffi.CData, a: ffi.CData, b: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_sum(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_sum(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_sum_rows(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_sum_rows(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_tanh(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_tanh(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_tanh_inplace(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_tanh_inplace(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_transpose(struct ggml_context * ctx,struct ggml_tensor * a);
  def ggml_transpose(ctx: ffi.CData, a: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_unary(struct ggml_context * ctx,struct ggml_tensor * a,enum ggml_unary_op op);
  def ggml_unary(ctx: ffi.CData, a: ffi.CData, op: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_unary_inplace(struct ggml_context * ctx,struct ggml_tensor * a,enum ggml_unary_op op);
  def ggml_unary_inplace(ctx: ffi.CData, a: ffi.CData, op: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_view_1d(struct ggml_context * ctx,struct ggml_tensor * a,int64_t ne0,size_t offset);
  def ggml_view_1d(ctx: ffi.CData, a: ffi.CData, ne0: int, offset: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_view_2d(struct ggml_context * ctx,struct ggml_tensor * a,int64_t ne0,int64_t ne1,size_t nb1,size_t offset);
  def ggml_view_2d(ctx: ffi.CData, a: ffi.CData, ne0: int, ne1: int, nb1: int, offset: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_view_3d(struct ggml_context * ctx,struct ggml_tensor * a,int64_t ne0,int64_t ne1,int64_t ne2,size_t nb1,size_t nb2,size_t offset);
  def ggml_view_3d(ctx: ffi.CData, a: ffi.CData, ne0: int, ne1: int, ne2: int, nb1: int, nb2: int, offset: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_view_4d(struct ggml_context * ctx,struct ggml_tensor * a,int64_t ne0,int64_t ne1,int64_t ne2,int64_t ne3,size_t nb1,size_t nb2,size_t nb3,size_t offset);
  def ggml_view_4d(ctx: ffi.CData, a: ffi.CData, ne0: int, ne1: int, ne2: int, ne3: int, nb1: int, nb2: int, nb3: int, offset: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_view_tensor(struct ggml_context * ctx, const struct ggml_tensor * src);
  def ggml_view_tensor(ctx: ffi.CData, src: ffi.CData) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_win_part(struct ggml_context * ctx,struct ggml_tensor * a,int w);
  def ggml_win_part(ctx: ffi.CData, a: ffi.CData, w: int) -> ffi.CData: ...

  # GGML_API struct ggml_tensor * ggml_win_unpart(struct ggml_context * ctx,struct ggml_tensor * a,int w0,int h0,int w);
  def ggml_win_unpart(ctx: ffi.CData, a: ffi.CData, w0: int, h0: int, w: int) -> ffi.CData: ...

  # GGML_API void * ggml_get_data (const struct ggml_tensor * tensor);
  def ggml_get_data(tensor: ffi.CData) -> ffi.CData: ...

  # GGML_API void * ggml_get_mem_buffer (const struct ggml_context * ctx);
  def ggml_get_mem_buffer(ctx: ffi.CData) -> ffi.CData: ...

  # GGML_API void ggml_build_forward_expand(struct ggml_cgraph * cgraph, struct ggml_tensor * tensor);
  def ggml_build_forward_expand(cgraph: ffi.CData, tensor: ffi.CData) -> None: ...

  # GGML_API void ggml_fp16_to_fp32_row(const ggml_fp16_t * x, float * y, int n);
  def ggml_fp16_to_fp32_row(x: ffi.CData, y: ffi.CData, n: int) -> None: ...

  # GGML_API void ggml_fp32_to_fp16_row(const float * x, ggml_fp16_t * y, int n);
  def ggml_fp32_to_fp16_row(x: ffi.CData, y: ffi.CData, n: int) -> None: ...

  # GGML_API void ggml_free(struct ggml_context * ctx);
  def ggml_free(ctx: ffi.CData) -> None: ...

  # GGML_API void ggml_graph_compute_with_ctx(struct ggml_context * ctx, struct ggml_cgraph * cgraph, int n_threads);
  def ggml_graph_compute_with_ctx(ctx: ffi.CData, cgraph: ffi.CData, n_threads: int) -> None: ...

  # GGML_API void ggml_graph_dump_dot(const struct ggml_cgraph * gb, const struct ggml_cgraph * gf, const char * filename);
  def ggml_graph_dump_dot(gb: ffi.CData, gf: ffi.CData, filename: ffi.CData) -> None: ...

  # GGML_API void ggml_graph_export(const struct ggml_cgraph * cgraph, const char * fname);
  def ggml_graph_export(cgraph: ffi.CData, fname: ffi.CData) -> None: ...

  # GGML_API void ggml_graph_print(const struct ggml_cgraph * cgraph);
  def ggml_graph_print(cgraph: ffi.CData) -> None: ...

  # GGML_API void ggml_graph_reset (struct ggml_cgraph * cgraph);
  def ggml_graph_reset(cgraph: ffi.CData) -> None: ...

  # GGML_API void ggml_numa_init();
  def ggml_numa_init() -> None: ...

  # GGML_API void ggml_opt_init(struct ggml_context * ctx,struct ggml_opt_context * opt,struct ggml_opt_params params,int64_t nx);
  def ggml_opt_init(ctx: ffi.CData, opt: ffi.CData, params: ffi.CData, nx: int) -> None: ...

  # GGML_API void ggml_print_object (const struct ggml_object * obj);
  def ggml_print_object(obj: ffi.CData) -> None: ...

  # GGML_API void ggml_print_objects(const struct ggml_context * ctx);
  def ggml_print_objects(ctx: ffi.CData) -> None: ...

  # GGML_API void ggml_set_f32_1d(const struct ggml_tensor * tensor, int i, float value);
  def ggml_set_f32_1d(tensor: ffi.CData, i: int, value: float) -> None: ...

  # GGML_API void ggml_set_i32_1d(const struct ggml_tensor * tensor, int i, int32_t value);
  def ggml_set_i32_1d(tensor: ffi.CData, i: int, value: int) -> None: ...

  # GGML_API void ggml_set_no_alloc(struct ggml_context * ctx, bool no_alloc);
  def ggml_set_no_alloc(ctx: ffi.CData, no_alloc: bool) -> None: ...

  # GGML_API void ggml_set_param(struct ggml_context * ctx,struct ggml_tensor * tensor);
  def ggml_set_param(ctx: ffi.CData, tensor: ffi.CData) -> None: ...

  # GGML_API void ggml_time_init();
  def ggml_time_init() -> None: ...

