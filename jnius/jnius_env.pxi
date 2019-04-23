cdef JNIEnv *default_env = NULL

cdef extern int gettid()
cdef JavaVM *jvm = NULL

IF JNIUS_LIB_SUFFIX is False:
    cdef first_time = 1

    cdef extern from 'NativeInvocationHandler.class.h':
        jbyte NativeInvocationHandler_bytes[]
        int NativeInvocationHandler_bytes_size

    cdef void load_NativeInvocationHandler(JavaVM *jvm, JNIEnv *env):
        cdef jclass class_loader
        cdef jmethodID get_system_loader
        cdef jobject system_loader
        cdef jthrowable exception
        cdef jint jni_result

        global first_time
    
        if first_time == 0:
            return

        first_time = 0
    
        # Init NativeInvocationHandler
        class_loader = env[0].FindClass(env, "java/lang/ClassLoader")
        if class_loader == NULL:
            raise SystemError('Could not find java/lang/ClassLoader')

        get_system_loader = env[0].GetStaticMethodID(
            env,
            class_loader, "getSystemClassLoader", "()Ljava/lang/ClassLoader;")
        if get_system_loader == NULL:
            raise SystemError('Could not find method - getSystemClassLoader')

        system_loader = env[0].CallStaticObjectMethod(env, class_loader, get_system_loader)
        if system_loader == NULL:
            raise SystemError('Could not find system loader')

        if env[0].DefineClass(
            env,
            "org/jnius/NativeInvocationHandler", system_loader,
                NativeInvocationHandler_bytes, NativeInvocationHandler_bytes_size) == NULL:
            raise SystemError("Could not define class org/jnius/NativeInvocationHandler (size={})".format(
                NativeInvocationHandler_bytes_size))
        

cdef JNIEnv *get_jnienv() except NULL:
    global default_env
    # first call, init.
    if default_env == NULL:
        default_env = get_platform_jnienv()
        if default_env == NULL:
            return NULL
        
        default_env[0].GetJavaVM(default_env, &jvm)

    # return the current env attached to the thread
    # XXX it threads are created from C (not java), we'll leak here.
    cdef JNIEnv *env = NULL
    jvm[0].AttachCurrentThread(jvm, &env, NULL)
    
    IF JNIUS_LIB_SUFFIX is False:
        load_NativeInvocationHandler(jvm, env)
        
    return env


def detach():
    jvm[0].DetachCurrentThread(jvm)

