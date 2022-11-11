
import datetime
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime,timedelta

class SaleOrder(models.Model):
    _inherit = "sale.order"

    nomor_telpon = fields.Char(string="Nomor Telpon")
