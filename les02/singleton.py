class Storage:
    _instances = None
    STORAGE = {}

    def __new__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super(Storage, cls).__new__(cls)
        return cls._instances

    def set_item(self, key, value):
        self.STORAGE[key] = value

    def get_item(self, key):
        return self.STORAGE.get(key)

    def delete_item(self, key):
        del self.STORAGE[key]

    def __getitem__(self, item):
        return self.get_item(item)


storage1 = Storage()
storage2 = Storage()

print(storage1)
print(storage2)