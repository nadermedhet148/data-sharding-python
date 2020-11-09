from django.db.models import Model
import uuid


class ShardManger:

    databases = ['db0', 'db1', 'db2']

    def pickup_db(self, key):
        char_code = ord(key[0])
        db_index = char_code % len(self.databases)
        return self.databases[db_index]

    def unique_id_generator(self, key):
        db = self.pickup_db(key)
        return db + "__" + uuid.uuid1().hex

    def get_db_from_unique_id(self, key):
        return key.split('__')[0]


