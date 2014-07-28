from glpi import db

class Computer(db.Model):
    __tablename__ = 'glpi_computers'
    __table_args__ = { 'mysql_charset': 'utf8', 'mysql_collate': 'utf8_general_ci' }
    id = db.Column(db.Integer, primary_key = True)
    entities_id = db.Column(db.Integer)
    name = db.Column(db.String(255, None, True))
    serial = db.Column(db.String(255, None, True))
    otherserial= db.Column(db.String(255, None, True))
    contact = db.Column(db.String(255, None, True))
    contact_num = db.Column(db.String(255, None, True))
    users_id_tech = db.Column(db.Integer)
    groups_id_tech = db.Column(db.Integer)
    comment = db.Column(db.Text(None, None, True))
    date_mod = db.Column(db.DateTime)
    operatingsystems_id = db.Column(db.Integer, db.ForeignKey('glpi_operatingsystems.id'))
    operatingsystemversions_id = db.Column(db.Integer)
    operatingsystemservicepacks_id = db.Column(db.Integer)
    os_license_number= db.Column(db.String(255, None, True))
    os_licenseid = db.Column(db.String(255, None, True))
    autoupdatesystems_id = db.Column(db.Integer)
    locations_id = db.Column(db.Integer)
    domains_id = db.Column(db.Integer)
    networks_id = db.Column(db.Integer)
    computermodels_id= db.Column(db.Integer)
    computertypes_id = db.Column(db.Integer)
    is_template = db.Column(db.Boolean)
    template_name = db.Column(db.String(255, None, True))
    manufacturers_id = db.Column(db.Integer)
    is_deleted = db.Column(db.Boolean)
    is_dynamic = db.Column(db.Boolean)
    users_id = db.Column(db.Integer)
    groups_id = db.Column(db.Integer)
    states_id = db.Column(db.Integer)
    ticket_tco = db.Column(db.Float)
    uuid = db.Column(db.String(255, None, True))

    