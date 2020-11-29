from App.Models.Model import Model

class Palette(Model):

    class Meta:
        database = Model.db()

    def getPalettes():
        return db.select().where(Person.name == 'Grandma L.').get()