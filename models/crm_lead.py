from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    access_crm_lead_user = fields.Many2one('res.users', string="Assigned User")
