from cpython.version cimport PY_MAJOR_VERSION

def cast(destclass, obj):
    cdef JavaClass jc
    cdef JavaClass jobj = obj
    from .reflect import autoclass

    if (PY_MAJOR_VERSION < 3 and isinstance(destclass, base_string)) or \
          (PY_MAJOR_VERSION >=3 and isinstance(destclass, str)):
        destclass = autoclass(destclass)

    try:
        javaclass = destclass.getClass()
    except (JavaException, AttributeError):
        javaclass = find_javaclass(destclass.__javaclass__)

    if not javaclass.isInstance(obj):
        raise JavaException('Impossible cast')

    jc = destclass(noinstance=True)
    jc.instanciate_from(jobj.j_self)
    return jc

def find_javaclass(namestr):
    namestr = namestr.replace('.', '/')
    cdef bytes name = str_for_c(namestr)
    from .reflect import Class
    cdef JavaClass cls
    cdef jclass jc
    cdef JNIEnv *j_env = get_jnienv()

    jc = jnius_find_class(j_env, name)
    if jc == NULL:
        j_env[0].ExceptionClear(j_env)
        raise JavaException('Class not found {0!r}'.format(name))

    check_exception(j_env)

    cls = Class(noinstance=True)
    cls.instanciate_from(create_local_ref(j_env, jc))
    j_env[0].DeleteLocalRef(j_env, jc)
    return cls

def to_jobject(definiton, pyobj, shared=True):
    from .reflect import Object, get_signature

    cdef jobject jobj
    cdef JavaClass pjobj
    cdef JNIEnv *j_env = get_jnienv()

    signature = get_signature(definiton)
    print('Convert with signature', signature, pyobj)

    if signature == 'V':
        return None

    jobj = convert_python_to_jobject(
        j_env, signature, pyobj)

    if jobj == NULL:
        j_env[0].ExceptionClear(j_env)
        raise JavaException('Conversion is not possible')

    pjobj = Object(noinstance=True)
    pjobj.instanciate_from(create_local_ref(j_env, jobj))
    return pjobj


def define_class(name, data):
    from .reflect import autoclass

    cdef JNIEnv *j_env = get_jnienv()
    cdef jbyte *jdata = data
    cdef jobject jobj

    name = name.replace('.', '/')
    if name.startswith('L') and name.endswith(';'):
        name = name[1:-1]

    jobj = j_env[0].DefineClass(j_env, name, NULL, jdata, len(data))
    check_exception(j_env)

    return autoclass(name)
