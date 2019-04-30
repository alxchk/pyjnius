from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
__all__ = ('autoclass', 'ensureclass')
from six import with_metaclass

from .jnius import (
    JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod,
    JavaField, JavaStaticField, JavaMultipleMethod, find_javaclass,
    JavaException
)


class Class(with_metaclass(MetaJavaClass, JavaClass)):
    __javaclass__ = 'java/lang/Class'

    desiredAssertionStatus = JavaMethod('()Z')
    forName = JavaMultipleMethod([
        ('(Ljava/lang/StringZLjava/lang/ClassLoader;)Ljava/lang/Class;', True, False),
        ('(Ljava/lang/String;)Ljava/lang/Class;', True, False), ])
    getClassLoader = JavaMethod('()Ljava/lang/ClassLoader;')
    getClasses = JavaMethod('()[Ljava/lang/Class;')
    getComponentType = JavaMethod('()Ljava/lang/Class;')
    getConstructor = JavaMethod('([Ljava/lang/Class;)Ljava/lang/reflect/Constructor;')
    getConstructors = JavaMethod('()[Ljava/lang/reflect/Constructor;')
    getDeclaredClasses = JavaMethod('()[Ljava/lang/Class;')
    getDeclaredConstructor = JavaMethod('([Ljava/lang/Class;)Ljava/lang/reflect/Constructor;')
    getDeclaredConstructors = JavaMethod('()[Ljava/lang/reflect/Constructor;')
    getDeclaredField = JavaMethod('(Ljava/lang/String;)Ljava/lang/reflect/Field;')
    getDeclaredFields = JavaMethod('()[Ljava/lang/reflect/Field;')
    getDeclaredMethod = JavaMethod('(Ljava/lang/String,[Ljava/lang/Class;)Ljava/lang/reflect/Method;')
    getDeclaredMethods = JavaMethod('()[Ljava/lang/reflect/Method;')
    getDeclaringClass = JavaMethod('()Ljava/lang/Class;')
    getField = JavaMethod('(Ljava/lang/String;)Ljava/lang/reflect/Field;')
    getFields = JavaMethod('()[Ljava/lang/reflect/Field;')
    getInterfaces = JavaMethod('()[Ljava/lang/Class;')
    getMethod = JavaMethod('(Ljava/lang/String,[Ljava/lang/Class;)Ljava/lang/reflect/Method;')
    getMethods = JavaMethod('()[Ljava/lang/reflect/Method;')
    getModifiers = JavaMethod('()[I')
    getName = JavaMethod('()Ljava/lang/String;')
    getPackage = JavaMethod('()Ljava/lang/Package;')
    getProtectionDomain = JavaMethod('()Ljava/security/ProtectionDomain;')
    getResource = JavaMethod('(Ljava/lang/String;)Ljava/net/URL;')
    getResourceAsStream = JavaMethod('(Ljava/lang/String;)Ljava/io/InputStream;')
    getSigners = JavaMethod('()[Ljava/lang/Object;')
    getSuperclass = JavaMethod('()Ljava/lang/Class;')
    isArray = JavaMethod('()Z')
    isAssignableFrom = JavaMethod('(Ljava/lang/reflect/Class;)Z')
    isInstance = JavaMethod('(Ljava/lang/Object;)Z')
    isInterface = JavaMethod('()Z')
    isPrimitive = JavaMethod('()Z')
    newInstance = JavaMethod('()Ljava/lang/Object;')
    toString = JavaMethod('()Ljava/lang/String;')


class Object(with_metaclass(MetaJavaClass, JavaClass)):
    __javaclass__ = 'java/lang/Object'

    getClass = JavaMethod('()Ljava/lang/Class;')
    hashCode = JavaMethod('()I')


class Modifier(with_metaclass(MetaJavaClass, JavaClass)):
    __javaclass__ = 'java/lang/reflect/Modifier'

    isAbstract = JavaStaticMethod('(I)Z')
    isFinal = JavaStaticMethod('(I)Z')
    isInterface = JavaStaticMethod('(I)Z')
    isNative = JavaStaticMethod('(I)Z')
    isPrivate = JavaStaticMethod('(I)Z')
    isProtected = JavaStaticMethod('(I)Z')
    isPublic = JavaStaticMethod('(I)Z')
    isStatic = JavaStaticMethod('(I)Z')
    isStrict = JavaStaticMethod('(I)Z')
    isSynchronized = JavaStaticMethod('(I)Z')
    isTransient = JavaStaticMethod('(I)Z')
    isVolatile = JavaStaticMethod('(I)Z')


class Method(with_metaclass(MetaJavaClass, JavaClass)):
    __javaclass__ = 'java/lang/reflect/Method'

    getName = JavaMethod('()Ljava/lang/String;')
    toString = JavaMethod('()Ljava/lang/String;')
    getParameterTypes = JavaMethod('()[Ljava/lang/Class;')
    getReturnType = JavaMethod('()Ljava/lang/Class;')
    getModifiers = JavaMethod('()I')
    isVarArgs = JavaMethod('()Z')
    hasGenericInformation = JavaMethod('()Z')
    getAnnotationBytes = JavaMethod('()[B')
    getDeclaringClass = JavaMethod('()Ljava/lang/Class;')
    getModifiers = JavaMethod('()I')
    getTypeParameters = JavaMethod('()[Ljava/lang/reflect/TypeVariable;')
    getReturnType = JavaMethod('()Ljava/lang/Class;')
    getGenericReturnType = JavaMethod('()Ljava/lang/reflect/Type;')
    getSharedParameterTypes = JavaMethod('()[Ljava/lang/Class;')
    getSharedExceptionTypes = JavaMethod('()[Ljava/lang/Class;')
    getParameterTypes = JavaMethod('()[Ljava/lang/Class;')
    getParameterCount = JavaMethod('()I')
    getGenericParameterTypes = JavaMethod('()[Ljava/lang/reflect/Type;')
    getExceptionTypes = JavaMethod('()[Ljava/lang/Class;')
    getGenericExceptionTypes = JavaMethod('()[Ljava/lang/reflect/Type;')
    equals = JavaMethod('(Ljava/lang/Object;)Z')
    hashCode = JavaMethod('()I')
    invoke = JavaMethod('(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;')
    isBridge = JavaMethod('()Z')
    isVarArgs = JavaMethod('()Z')
    isSynthetic = JavaMethod('()Z')
    isDefault = JavaMethod('()Z')
    getMethodAccessor = JavaMethod('()Ljdk/internal/reflect/MethodAccessor;')
    setMethodAccessor = JavaMethod('(Ljdk/internal/reflect/MethodAccessor;)V')
    getDefaultValue = JavaMethod('()Ljava/lang/Object;')


class Field(with_metaclass(MetaJavaClass, JavaClass)):
    __javaclass__ = 'java/lang/reflect/Field'

    getName = JavaMethod('()Ljava/lang/String;')
    toString = JavaMethod('()Ljava/lang/String;')
    getType = JavaMethod('()Ljava/lang/Class;')
    getModifiers = JavaMethod('()I')
    setAccessible = JavaMethod('(Z)V')
    checkCanSetAccessible = JavaMethod('(Ljava/lang/Class;)V')
    getDeclaringClass = JavaMethod('()Ljava/lang/Class;')
    isEnumConstant = JavaMethod('()Z')
    isSynthetic = JavaMethod('()Z')
    getGenericType = JavaMethod('()Ljava/lang/reflect/Type;')
    equals = JavaMethod('(Ljava/lang/Object;)Z')
    hashCode = JavaMethod('()I')
    get = JavaMethod('(Ljava/lang/Object;)Ljava/lang/Object;')
    getBoolean = JavaMethod('(Ljava/lang/Object;)Z')
    getByte = JavaMethod('(Ljava/lang/Object;)B')
    getChar = JavaMethod('(Ljava/lang/Object;)C')
    getShort = JavaMethod('(Ljava/lang/Object;)S')
    getInt = JavaMethod('(Ljava/lang/Object;)I')
    getLong = JavaMethod('(Ljava/lang/Object;)J')
    getFloat = JavaMethod('(Ljava/lang/Object;)F')
    getDouble = JavaMethod('(Ljava/lang/Object;)D')
    set = JavaMethod('(Ljava/lang/Object;Ljava/lang/Object;)V')
    setBoolean = JavaMethod('(Ljava/lang/Object;Z)V')
    setByte = JavaMethod('(Ljava/lang/Object;B)V')
    setChar = JavaMethod('(Ljava/lang/Object;C)V')
    setShort = JavaMethod('(Ljava/lang/Object;S)V')
    setInt = JavaMethod('(Ljava/lang/Object;I)V')
    setLong = JavaMethod('(Ljava/lang/Object;J)V')
    setFloat = JavaMethod('(Ljava/lang/Object;F)V')
    setDouble = JavaMethod('(Ljava/lang/Object;D)V')


class Constructor(with_metaclass(MetaJavaClass, JavaClass)):
    __javaclass__ = 'java/lang/reflect/Constructor'

    toString = JavaMethod('()Ljava/lang/String;')
    getParameterTypes = JavaMethod('()[Ljava/lang/Class;')
    getModifiers = JavaMethod('()I')
    isVarArgs = JavaMethod('()Z')


def get_signature(cls_tp):
    tp = cls_tp.getName()
    if tp[0] == '[':
        return tp.replace('.', '/')
    signatures = {
        'void': 'V', 'boolean': 'Z', 'byte': 'B',
        'char': 'C', 'short': 'S', 'int': 'I',
        'long': 'J', 'float': 'F', 'double': 'D'}
    ret = signatures.get(tp)
    if ret:
        return ret
    # don't do it in recursive way for the moment,
    # error on the JNI/android: JNI ERROR (app bug): local reference table
    # overflow (max=512)

    # ensureclass(tp)
    return 'L{0};'.format(tp.replace('.', '/'))


registers = []


def ensureclass(clsname):
    if clsname in registers:
        return
    jniname = clsname.replace('.', '/')
    if MetaJavaClass.get_javaclass(jniname):
        return
    registers.append(clsname)
    autoclass(clsname)


def lower_name(s):
    return s[:1].lower() + s[1:] if s else ''


def bean_getter(s):
    return (s.startswith('get') and len(s) > 3 and s[3].isupper()) or (s.startswith('is') and len(s) > 2 and s[2].isupper())


def autoclass(clsname):
    jniname = clsname.replace('.', '/')
    cls = MetaJavaClass.get_javaclass(jniname)
    if cls:
        return cls

    classDict = {}

    c = find_javaclass(clsname)

    constructors = []
    for constructor in c.getConstructors():
        sig = '({0})V'.format(
            ''.join([get_signature(x) for x in constructor.getParameterTypes()]))
        constructors.append((sig, constructor.isVarArgs()))
    classDict['__javaconstructor__'] = constructors

    parent_class = c
    while parent_class is not None:
        methods = parent_class.getDeclaredMethods()
        methods_name = [x.getName() for x in methods]

        for index, method in enumerate(methods):
            name = methods_name[index]
            if name in classDict:
                continue
            count = methods_name.count(name)

            # only one method available
            if count == 1:
                static = Modifier.isStatic(method.getModifiers())
                varargs = method.isVarArgs()
                sig = '({0}){1}'.format(
                    ''.join([get_signature(x) for x in method.getParameterTypes()]),
                    get_signature(method.getReturnType()))
                cls = JavaStaticMethod if static else JavaMethod
                classDict[name] = cls(sig, varargs=varargs)
                if name != 'getClass' and bean_getter(name) and len(method.getParameterTypes()) == 0:
                    lowername = lower_name(name[2 if name.startswith('is') else 3:])
                    classDict[lowername] = (lambda n: property(lambda self: getattr(self, n)()))(name)
                continue

            # multiple signatures
            signatures = []
            for index, subname in enumerate(methods_name):
                if subname != name:
                    continue
                method = methods[index]
                sig = '({0}){1}'.format(
                    ''.join([get_signature(x) for x in method.getParameterTypes()]),
                    get_signature(method.getReturnType()))
                '''
                print 'm', name, sig, method.getModifiers()
                m = method.getModifiers()
                print 'Public', Modifier.isPublic(m)
                print 'Private', Modifier.isPrivate(m)
                print 'Protected', Modifier.isProtected(m)
                print 'Static', Modifier.isStatic(m)
                print 'Final', Modifier.isFinal(m)
                print 'Synchronized', Modifier.isSynchronized(m)
                print 'Volatile', Modifier.isVolatile(m)
                print 'Transient', Modifier.isTransient(m)
                print 'Native', Modifier.isNative(m)
                print 'Interface', Modifier.isInterface(m)
                print 'Abstract', Modifier.isAbstract(m)
                print 'Strict', Modifier.isStrict(m)
                '''
                signatures.append((sig, Modifier.isStatic(method.getModifiers()), method.isVarArgs()))

            classDict[name] = JavaMultipleMethod(signatures)

        parent_class = parent_class.getSuperclass()

    def _getitem(self, index):
        try:
            return self.get(index)
        except JavaException as e:
            # initialize the subclass before getting the Class.forName
            # otherwise isInstance does not know of the subclass
            mock_exception_object = autoclass(e.classname)()
            if find_javaclass("java.lang.IndexOutOfBoundsException").isInstance(mock_exception_object):
                # python for...in iteration checks for end of list by waiting for IndexError
                raise IndexError()
            else:
                raise

    for iclass in c.getInterfaces():
        if iclass.getName() == 'java.util.List':
            classDict['__getitem__'] = _getitem
            classDict['__len__'] = lambda self: self.size()
            break

    for field in c.getFields():
        static = Modifier.isStatic(field.getModifiers())
        sig = get_signature(field.getType())
        cls = JavaStaticField if static else JavaField
        classDict[field.getName()] = cls(sig)

    classDict['__javaclass__'] = clsname.replace('.', '/')

    return MetaJavaClass.__new__(
        MetaJavaClass,
        clsname,  # .replace('.', '_'),
        (JavaClass, ),
        classDict)
