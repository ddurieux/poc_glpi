from glpi import db

class OperatingSystem(db.Model):
    __tablename__ = 'glpi_operatingsystems'
    __table_args__ = { 'mysql_charset': 'utf8', 'mysql_collate': 'utf8_general_ci' }
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255, None, True))
    comment = db.Column(db.Text(None, None, True))

    def __init__(self, name):
        self.name = name