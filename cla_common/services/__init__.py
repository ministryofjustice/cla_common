class BaseAdapter(object):
    _instance = None
    _adapter_factory = None
    @classmethod
    def set_adapter_factory(cls, adapter_factory):
        # The staticmethod for the factory is needed because this will be an unbound callable, Not needed got Python3
        cls._adapter_factory = staticmethod(adapter_factory)
        cls._instance = None

    @classmethod
    def get_adapter(cls):
        if not cls._instance and cls._adapter_factory:
            cls._instance = cls._get_instance_from_factory(cls._adapter_factory)
        return cls._instance

    @staticmethod
    def _get_instance_from_factory(factory):
        return factory()


class TranslationAdapter(BaseAdapter):
    @staticmethod
    def _get_instance_from_factory(factory):
        return staticmethod(factory())


class CacheAdapter(BaseAdapter):
    pass


def translate(string):
    translator = TranslationAdapter.get_adapter()
    if translator:
        return translator(string)
    return string
