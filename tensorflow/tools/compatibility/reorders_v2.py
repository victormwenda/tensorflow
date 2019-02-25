# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
# pylint: disable=line-too-long
"""List of renames to apply when converting from TF 1.0 to TF 2.0.

THIS FILE IS AUTOGENERATED: To update, please run:
  bazel build tensorflow/tools/compatibility/update:generate_v2_reorders_map
  bazel-bin/tensorflow/tools/compatibility/update/generate_v2_reorders_map
This file should be updated whenever a function is added to
self.reordered_function_names in tf_upgrade_v2.py.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

reorders = {
    'tf.argmax': ['input', 'axis', 'name', 'dimension', 'output_type'],
    'tf.argmin': ['input', 'axis', 'name', 'dimension', 'output_type'],
    'tf.batch_to_space': ['input', 'crops', 'block_size', 'name', 'block_shape'],
    'tf.boolean_mask': ['tensor', 'mask', 'name', 'axis'],
    'tf.cond': ['pred', 'true_fn', 'false_fn', 'strict', 'name', 'fn1', 'fn2'],
    'tf.confusion_matrix': ['labels', 'predictions', 'num_classes', 'dtype', 'name', 'weights'],
    'tf.convert_to_tensor': ['value', 'dtype', 'name', 'preferred_dtype', 'dtype_hint'],
    'tf.decode_csv': ['records', 'record_defaults', 'field_delim', 'use_quote_delim', 'name', 'na_value', 'select_cols'],
    'tf.depth_to_space': ['input', 'block_size', 'name', 'data_format'],
    'tf.feature_column.categorical_column_with_vocabulary_file': ['key', 'vocabulary_file', 'vocabulary_size', 'num_oov_buckets', 'default_value', 'dtype'],
    'tf.gradients': ['ys', 'xs', 'grad_ys', 'name', 'colocate_gradients_with_ops', 'gate_gradients', 'aggregation_method', 'stop_gradients', 'unconnected_gradients'],
    'tf.hessians': ['ys', 'xs', 'name', 'colocate_gradients_with_ops', 'gate_gradients', 'aggregation_method'],
    'tf.image.sample_distorted_bounding_box': ['image_size', 'bounding_boxes', 'seed', 'seed2', 'min_object_covered', 'aspect_ratio_range', 'area_range', 'max_attempts', 'use_image_if_no_bounding_boxes', 'name'],
    'tf.io.decode_csv': ['records', 'record_defaults', 'field_delim', 'use_quote_delim', 'name', 'na_value', 'select_cols'],
    'tf.io.parse_example': ['serialized', 'features', 'name', 'example_names'],
    'tf.io.parse_single_example': ['serialized', 'features', 'name', 'example_names'],
    'tf.io.serialize_many_sparse': ['sp_input', 'name', 'out_type'],
    'tf.io.serialize_sparse': ['sp_input', 'name', 'out_type'],
    'tf.linalg.norm': ['tensor', 'ord', 'axis', 'keepdims', 'name', 'keep_dims'],
    'tf.math.argmax': ['input', 'axis', 'name', 'dimension', 'output_type'],
    'tf.math.argmin': ['input', 'axis', 'name', 'dimension', 'output_type'],
    'tf.math.confusion_matrix': ['labels', 'predictions', 'num_classes', 'dtype', 'name', 'weights'],
    'tf.math.in_top_k': ['predictions', 'targets', 'k', 'name'],
    'tf.math.reduce_all': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.math.reduce_any': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.math.reduce_logsumexp': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.math.reduce_max': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.math.reduce_mean': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.math.reduce_min': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.math.reduce_prod': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.math.reduce_sum': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.multinomial': ['logits', 'num_samples', 'seed', 'name', 'output_dtype'],
    'tf.nn.avg_pool': ['value', 'ksize', 'strides', 'padding', 'data_format', 'name', 'input'],
    'tf.nn.conv1d': ['value', 'filters', 'stride', 'padding', 'use_cudnn_on_gpu', 'data_format', 'name', 'input', 'dilations'],
    'tf.nn.conv2d': ['input', 'filter', 'strides', 'padding', 'use_cudnn_on_gpu', 'data_format', 'dilations', 'name', 'filters'],
    'tf.nn.conv2d_backprop_input': ['input_sizes', 'filter', 'out_backprop', 'strides', 'padding', 'use_cudnn_on_gpu', 'data_format', 'dilations', 'name', 'filters'],
    'tf.nn.convolution': ['input', 'filter', 'padding', 'strides', 'dilation_rate', 'name', 'data_format', 'filters', 'dilations'],
    'tf.nn.crelu': ['features', 'name', 'axis'],
    'tf.nn.ctc_beam_search_decoder': ['inputs', 'sequence_length', 'beam_width', 'top_paths', 'merge_repeated'],
    'tf.nn.depth_to_space': ['input', 'block_size', 'name', 'data_format'],
    'tf.nn.depthwise_conv2d': ['input', 'filter', 'strides', 'padding', 'rate', 'name', 'data_format', 'dilations'],
    'tf.nn.embedding_lookup': ['params', 'ids', 'partition_strategy', 'name', 'validate_indices', 'max_norm'],
    'tf.nn.embedding_lookup_sparse': ['params', 'sp_ids', 'sp_weights', 'partition_strategy', 'name', 'combiner', 'max_norm'],
    'tf.nn.fractional_avg_pool': ['value', 'pooling_ratio', 'pseudo_random', 'overlapping', 'deterministic', 'seed', 'seed2', 'name'],
    'tf.nn.fractional_max_pool': ['value', 'pooling_ratio', 'pseudo_random', 'overlapping', 'deterministic', 'seed', 'seed2', 'name'],
    'tf.nn.in_top_k': ['predictions', 'targets', 'k', 'name'],
    'tf.nn.max_pool': ['value', 'ksize', 'strides', 'padding', 'data_format', 'name', 'input'],
    'tf.nn.moments': ['x', 'axes', 'shift', 'name', 'keep_dims', 'keepdims'],
    'tf.nn.pool': ['input', 'window_shape', 'pooling_type', 'padding', 'dilation_rate', 'strides', 'name', 'data_format', 'dilations'],
    'tf.nn.separable_conv2d': ['input', 'depthwise_filter', 'pointwise_filter', 'strides', 'padding', 'rate', 'name', 'data_format', 'dilations'],
    'tf.nn.softmax_cross_entropy_with_logits': ['_sentinel', 'labels', 'logits', 'dim', 'name', 'axis'],
    'tf.nn.space_to_batch': ['input', 'paddings', 'block_size', 'name', 'block_shape'],
    'tf.nn.space_to_depth': ['input', 'block_size', 'name', 'data_format'],
    'tf.nn.weighted_moments': ['x', 'axes', 'frequency_weights', 'name', 'keep_dims', 'keepdims'],
    'tf.norm': ['tensor', 'ord', 'axis', 'keepdims', 'name', 'keep_dims'],
    'tf.pad': ['tensor', 'paddings', 'mode', 'name', 'constant_values'],
    'tf.parse_example': ['serialized', 'features', 'name', 'example_names'],
    'tf.parse_single_example': ['serialized', 'features', 'name', 'example_names'],
    'tf.quantize_v2': ['input', 'min_range', 'max_range', 'T', 'mode', 'name', 'round_mode'],
    'tf.random.multinomial': ['logits', 'num_samples', 'seed', 'name', 'output_dtype'],
    'tf.random.poisson': ['lam', 'shape', 'dtype', 'seed', 'name'],
    'tf.random_poisson': ['lam', 'shape', 'dtype', 'seed', 'name'],
    'tf.reduce_all': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.reduce_any': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.reduce_join': ['inputs', 'axis', 'keep_dims', 'separator', 'name', 'reduction_indices', 'keepdims'],
    'tf.reduce_logsumexp': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.reduce_max': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.reduce_mean': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.reduce_min': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.reduce_prod': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.reduce_sum': ['input_tensor', 'axis', 'keepdims', 'name', 'reduction_indices', 'keep_dims'],
    'tf.reverse_sequence': ['input', 'seq_lengths', 'seq_axis', 'batch_axis', 'name', 'seq_dim', 'batch_dim'],
    'tf.serialize_many_sparse': ['sp_input', 'name', 'out_type'],
    'tf.serialize_sparse': ['sp_input', 'name', 'out_type'],
    'tf.shape': ['input', 'name', 'out_type'],
    'tf.size': ['input', 'name', 'out_type'],
    'tf.space_to_batch': ['input', 'paddings', 'block_size', 'name', 'block_shape'],
    'tf.space_to_depth': ['input', 'block_size', 'name', 'data_format'],
    'tf.sparse.add': ['a', 'b', 'threshold', 'thresh'],
    'tf.sparse.concat': ['axis', 'sp_inputs', 'name', 'expand_nonconcat_dim', 'concat_dim', 'expand_nonconcat_dims'],
    'tf.sparse.reduce_max': ['sp_input', 'axis', 'keepdims', 'reduction_axes', 'keep_dims'],
    'tf.sparse.segment_mean': ['data', 'indices', 'segment_ids', 'name', 'num_segments'],
    'tf.sparse.segment_sqrt_n': ['data', 'indices', 'segment_ids', 'name', 'num_segments'],
    'tf.sparse.segment_sum': ['data', 'indices', 'segment_ids', 'name', 'num_segments'],
    'tf.sparse.split': ['keyword_required', 'sp_input', 'num_split', 'axis', 'name', 'split_dim'],
    'tf.sparse_add': ['a', 'b', 'threshold', 'thresh'],
    'tf.sparse_concat': ['axis', 'sp_inputs', 'name', 'expand_nonconcat_dim', 'concat_dim', 'expand_nonconcat_dims'],
    'tf.sparse_matmul': ['a', 'b', 'transpose_a', 'transpose_b', 'a_is_sparse', 'b_is_sparse', 'name'],
    'tf.sparse_reduce_max': ['sp_input', 'axis', 'keepdims', 'reduction_axes', 'keep_dims'],
    'tf.sparse_segment_mean': ['data', 'indices', 'segment_ids', 'name', 'num_segments'],
    'tf.sparse_segment_sqrt_n': ['data', 'indices', 'segment_ids', 'name', 'num_segments'],
    'tf.sparse_segment_sum': ['data', 'indices', 'segment_ids', 'name', 'num_segments'],
    'tf.sparse_split': ['keyword_required', 'sp_input', 'num_split', 'axis', 'name', 'split_dim'],
    'tf.strings.length': ['input', 'name', 'unit'],
    'tf.strings.reduce_join': ['inputs', 'axis', 'keep_dims', 'separator', 'name', 'reduction_indices', 'keepdims'],
    'tf.strings.substr': ['input', 'pos', 'len', 'name', 'unit'],
    'tf.substr': ['input', 'pos', 'len', 'name', 'unit'],
    'tf.test.assert_equal_graph_def': ['actual', 'expected', 'checkpoint_v2'],
    'tf.transpose': ['a', 'perm', 'name', 'conjugate'],
    'tf.tuple': ['tensors', 'name', 'control_inputs'],
    'tf.while_loop': ['cond', 'body', 'loop_vars', 'shape_invariants', 'parallel_iterations', 'back_prop', 'swap_memory', 'name', 'maximum_iterations', 'return_same_structure']
}
