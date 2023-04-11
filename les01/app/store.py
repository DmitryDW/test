class Store:
    _instances = {}
    STORE = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Store, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def set_item(self, key, value):
        self.STORE[key] = value

    def get_item(self, key):
        return self.STORE.get(key)

    def delete_item(self, key):
        del self.STORE[key]

    def __getitem__(self, item):
        return self.get_item(item)
