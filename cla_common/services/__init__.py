class TranslationAdapter(object):
    _translation_adapter_factory = None

    @classmethod
    def set_translation_adapter_factory(cls, translation_adapter_factory):
        cls._translation_adapter_factory = translation_adapter_factory

    @classmethod
    def get_translation_adapter(cls):
        if cls._translation_adapter_factory:
            factory = cls._translation_adapter_factory
            return factory()
        return None


class CacheAdapter(object):
    _cache_adapter_factory = None

    @classmethod
    def set_cache_adapter_factory(cls, cache_adapter_factory):
        cls._cache_adapter_factory = staticmethod(cache_adapter_factory)

    @classmethod
    def get_cache_adapter(cls):
        if cls._cache_adapter_factory:
            factory = cls._cache_adapter_factory
            return factory()
        return None


def translate(string):
    translator = TranslationAdapter.get_translation_adapter()
    if translator:
        return translator(string)
    return string
