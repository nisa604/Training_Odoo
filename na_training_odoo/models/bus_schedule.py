from odoo import models, fields, api, _
from odoo.exceptions import UserError

class BusSchedule(models.Model):
    _name = 'bus.schedule'
    _description="Jadwal keberangkatan setiap bus"

    name = fields.Char(string='Name')
    schedule = fields.Datetime(string='Schedule')
    payment_type = fields.Selection([("cash","Tunai"),("transfer","NonTunai")], string='Payment')
    departure = fields.Datetime(string='Departure')
    arrival = fields.Datetime(string='Arrival')
    bus_id = fields.Many2one(
        comodel_name='res.bus',
        string='Bus',
    )
    route_id = fields.Many2one(
        comodel_name='bus.route',
        string='Route',
    )
    baggage_line_ids = fields.One2many(
        comodel_name='baggage.baggage',
        inverse_name='schedule_id',
        string='Baggage(s)',
    )
    passenger_ids = fields.Many2many(
        comodel_name='res.passenger', 
        string='Passenger(s)'
    )
    capacity = fields.Integer(
        string='Capacity',
        related='bus_id.capacity',
    )
    state = fields.Selection(
        selection=[
            ("draft","Draft"),
            ("submit","Submitted"),
            ("run","On Going"),
            ("done","Done")
            ], 
        string='Status', 
        default='draft'
        )

    @api.model
    def create(self, values):
        result = super(BusSchedule, self).create(values)

        result['name'] = self.env['ir.sequence'].next_by_code('bus.schedule.sequence')

        return result
    
    def button_submit(self):
        for rec in self:
            rec.write ({
                'state' : 'submit'
            })
    def button_run(self):
        for rec in self:
            rec.write({
                'state': 'run'
            })
    def button_done(self):
        for rec in self:
            rec.write({
                'state': 'done'
            })

class Baggage(models.Model):
    _name = 'baggage.baggage'
    _description = 'Baggage'

    name = fields.Char(string='Name')
    weight = fields.Float(string='Weight(Kg)')
    schedule_id = fields.Many2one(
        comodel_name='bus.schedule',
        string='Schedule',
    )