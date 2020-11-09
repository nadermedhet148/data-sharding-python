from django.db.models import Model


class ShardManger:

    databases = ['db0', 'db1', 'db2']

    def pickup_db(self,key):
        char_code = ord(key[0])
        db_index = char_code % len(self.databases)
        return self.databases[db_index]

