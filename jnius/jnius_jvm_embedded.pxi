include "config.pxi"

from cpython cimport PyCapsule_GetPointer

cdef extern from "jni.h":
    int JNI_VERSION_1_6
    int JNI_OK
    jboolean JNI_FALSE

cdef JNIEnv *get_platform_jnienv() except NULL:
    cdef JNIEnv *platform_env = NULL
    cdef JavaVM* jvm
    cdef int ret
    import jnius_config
    
    if hasattr(sys, 'JVM'):
        jvm = <JavaVM *> PyCapsule_GetPointer(sys.JVM, "JVM")
        ret = jvm[0].AttachCurrentThread(<JavaVM*> jvm, &platform_env, NULL)
        if ret != JNI_OK:
            raise SystemError("JVM failed to start: {0}".format(ret))
 
        jnius_config.vm_running = True
    elif not JNIUS_LIB_SUFFIX:
        raise SystemError("Pyjnius built without support of CreateJavaVM")

    return platform_env
