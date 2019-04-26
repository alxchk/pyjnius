include "config.pxi"

cdef extern from "jni.h":
    int JNI_OK
    jboolean JNI_FALSE

import jvm as _jvm

from cpython cimport PyCapsule_GetPointer

cdef first_time = 1

cdef extern from 'NativeInvocationHandler.class.h':
    jbyte NativeInvocationHandler_bytes[]
    int NativeInvocationHandler_bytes_size

cdef void load_NativeInvocationHandler(JNIEnv *env):
    cdef jclass class_loader
    cdef jmethodID get_system_loader
    cdef jint jni_result

    global first_time

    if first_time == 0:
        return

    context_class_loader_capsule = _jvm.get_preferred_classloader()
    context_class_loader_ptr = <jobject> PyCapsule_GetPointer(
        context_class_loader_capsule, "PreferredClassLoader")

    if context_class_loader_ptr == NULL:
        raise SystemError("Preferred ClassLoader not found")

    first_time = 0

    # Init NativeInvocationHandler
    if env[0].DefineClass(
        env,
        "org/jnius/NativeInvocationHandler", context_class_loader_ptr,
            NativeInvocationHandler_bytes, NativeInvocationHandler_bytes_size) == NULL:
        raise SystemError("Could not define class org/jnius/NativeInvocationHandler (size={})".format(
            NativeInvocationHandler_bytes_size))


cdef JNIEnv *get_platform_jnienv() except NULL:
    cdef JNIEnv *platform_env = NULL
    cdef JavaVM* jvm_ptr = NULL
    cdef jobject context_class_loader = NULL
    cdef int ret

    import jnius_config

    jvm_capsule = _jvm.get_jvm()

    jvm_ptr = <JavaVM *> PyCapsule_GetPointer(jvm_capsule, "JVM")

    if jvm_ptr == NULL:
        raise SystemError("JVM Context not found")

    ret = jvm_ptr[0].AttachCurrentThread(<JavaVM*> jvm_ptr, &platform_env, NULL)
    if ret != JNI_OK:
        raise SystemError("JVM failed to start: {0}".format(ret))

    load_NativeInvocationHandler(platform_env)
    jnius_config.vm_running = True

    return platform_env
