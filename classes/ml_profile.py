from peewee import Model, CharField, IntegerField, FloatField, ForeignKeyField, SqliteDatabase

db = SqliteDatabase('aic_regression.db')


class MLProfile(Model):
    name = CharField()
    profile_id = CharField(unique=True)
    test_size = FloatField()
    epoch = IntegerField()
    batch_size = IntegerField()
    id = IntegerField(primary_key=True)
    input_columns = CharField()
    target_column = CharField()

    class Meta:
        database = db
        table_name = 'ml_profiles'
