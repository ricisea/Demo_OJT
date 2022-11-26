
import datetime
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime,timedelta

class SaleOrder(models.Model):
    _inherit = "sale.order"

    nomor_telpon = fields.Char(string="Nomor Telpon")
    warehouse_latihan_id = fields.Many2one('stock.warehouse',string="Warehouse",required=0)
    warehouse_all = fields.Boolean(string="All Warehouse", default=False)
 
    counter_consum = fields.Float(string="Consumable")
    counter_service = fields.Float(string="Service")
    counter_store = fields.Float(string="Stockable Product")


    bool_consu= fields.Boolean(string="consu", default=False)
    bool_service= fields.Boolean(string="service", default=False)
    bool_store= fields.Boolean(string="store", default=False)


    @api.onchange('order_line')
    def get_counter_store(self):
        for i in self:
            total = 0
            for line in i.order_line:
                if line.product_id.type == "product":
                    total = total+line.price_unit*line.product_uom_qty
            i.counter_store = total
            if total == 0:
                i.bool_store = False
            else:
                i.bool_store = True

    
    @api.onchange('order_line')
    def get_counter_consu(self):
        for i in self:
            total = 0
            for line in i.order_line:
                if line.product_id.type == "consu":
                    total = total+line.price_unit*line.product_uom_qty
            i.counter_consum = total
            if total == 0:
                i.bool_consu = False
            else:
                i.bool_consu = True

    
    @api.onchange('order_line')
    def get_counter_service(self):
        for i in self:
            total = 0
            for line in i.order_line:
                if line.product_id.type == "service":
                    total = total+line.price_unit*line.product_uom_qty
            i.counter_service = total
            if total == 0:
                i.bool_service = False
            else:
                i.bool_service = True

    



    

   