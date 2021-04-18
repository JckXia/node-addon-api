{
  'target_defaults': {
    'includes': ['../common.gypi'],
    'sources': [
        'addon.cc',
        'addon_data.cc',
        'arraybuffer.cc',
        'asynccontext.cc',
        'asyncprogressqueueworker.cc',
        'asyncprogressworker.cc',
        'asyncworker.cc',
        'asyncworker-persistent.cc',
        'basic_types/array.cc',
        'basic_types/boolean.cc',
        'basic_types/number.cc',
        'basic_types/value.cc',
        'bigint.cc',
        'date.cc',
        'binding.cc',
        'buffer.cc',
        'callbackscope.cc',
        'dataview/dataview.cc',
        'dataview/dataview_read_write.cc',
        'error.cc',
        'external.cc',
        'function.cc',
        'handlescope.cc',
        'movable_callbacks.cc',
        'memory_management.cc',
        'name.cc',
        'globalObject/global_object_delete_property.cc',
        'globalObject/global_object_has_own_property.cc',
        'globalObject/global_object_set_property.cc',
        'globalObject/global_object_get_property.cc',
        'globalObject/global_object.cc',
        'object/delete_property.cc',
        'object/finalizer.cc',
        'object/get_property.cc',
        'object/has_own_property.cc',
        'object/has_property.cc',
        'object/object.cc',
        'object/object_freeze_seal.cc',
        'object/set_property.cc',
        'object/subscript_operator.cc',
        'promise.cc',
        'run_script.cc',
        "symbol.cc",
        'threadsafe_function/threadsafe_function_ctx.cc',
        'threadsafe_function/threadsafe_function_existing_tsfn.cc',
        'threadsafe_function/threadsafe_function_ptr.cc',
        'threadsafe_function/threadsafe_function_sum.cc',
        'threadsafe_function/threadsafe_function_unref.cc',
        'threadsafe_function/threadsafe_function.cc',
        'typed_threadsafe_function/typed_threadsafe_function_ctx.cc',
        'typed_threadsafe_function/typed_threadsafe_function_existing_tsfn.cc',
        'typed_threadsafe_function/typed_threadsafe_function_ptr.cc',
        'typed_threadsafe_function/typed_threadsafe_function_sum.cc',
        'typed_threadsafe_function/typed_threadsafe_function_unref.cc',
        'typed_threadsafe_function/typed_threadsafe_function.cc',
        'typedarray.cc',
        'objectwrap.cc',
        'objectwrap_constructor_exception.cc',
        'objectwrap-removewrap.cc',
        'objectwrap_multiple_inheritance.cc',
        'objectreference.cc',
        'reference.cc',
        'version_management.cc',
        'thunking_manual.cc',
      ],
      'conditions': [
        ['disable_deprecated!="true"', {
          'sources': ['object/object_deprecated.cc']
        }]
      ],
  },
  'targets': [
    {
      'target_name': 'binding',
      'includes': ['../except.gypi']
    },
    {
      'target_name': 'binding_noexcept',
      'includes': ['../noexcept.gypi']
    },
  ],
}
