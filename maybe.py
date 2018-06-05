class Maybe:
    """
    Provide method chaining with Try: Except: wrapping
    """

    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, name):
        if name == "text":
            try:
                return self.obj.text
            except:
                return None
        return lambda *args, **kwargs: self.__proxy_method(name, *args, **kwargs)

    def __proxy_method(self, method_name, *args, **kwargs):
        if self.obj is None:
            return self
        try:
            result = getattr(self.obj, method_name)(*args, **kwargs)
            self.obj = result
        except:
            self.obj = None
        return self

    def resolve(self):
        """
        Return inner value
        """
        return self.obj
