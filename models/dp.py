
import datetime
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime,timedelta

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    dp = fields.Float(string="Down Payment")
    total = fields.Float(string="Total",compute="get_total")
    email = fields.Char(string="Email")

    @api.depends('amount_total','dp')
    def get_total(self):
        totals = self.amount_total - self.dp
        self.total =totals

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    cost_price = fields.Float(string="cost",related="product_id.standard_price")
    diff_cost = fields.Float(string="Price Diff", compute="get_difference")

    # @api.onchange("product_id","price_unit")
    # def get_diff(self):
    #     self.diff_cost = self.price_unit - self.cost_price

    @api.depends("price_unit","cost_price")
    def get_difference(self):
        for i in self:
            i.diff_cost= i.price_unit - i.cost_price
            

