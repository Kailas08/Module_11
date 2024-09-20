import inspect

def introspection_info(obj):
    # Получение типа объекта
    obj_type = type(obj).__name__

    # Получение атрибутов объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получение методов объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получение модуля, к которому принадлежит объект
    obj_module = obj.__module__

    # Создаем словарь с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
    }

    return info



class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


obj = MyClass(10)
object_info = introspection_info(obj)
print(object_info)