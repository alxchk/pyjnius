cdef jclass jnius_find_class(JNIEnv *j_env, bytes name):
    return j_env[0].FindClass(j_env, name)
