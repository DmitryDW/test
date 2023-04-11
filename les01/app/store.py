class Store:
    _instances = None
    STORE = {}

    def __new__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super(Store, cls).__new__(cls)
        return cls._instances

    def set_item(self, key, value):
        self.STORE[key] = value

    def get_item(self, key):
        return self.STORE.get(key)

    def delete_item(self, key):
        del self.STORE[key]

    def __getitem__(self, item):
        return self.get_item(item)
