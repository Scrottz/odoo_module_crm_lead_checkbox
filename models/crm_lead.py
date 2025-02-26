from odoo import models, fields, api

class CrmLeadChecklist(models.Model):
    _name = 'crm.lead.checklist'
    _description = 'CRM Lead Checklist'

    name = fields.Char(string="Aufgabe", required=True)
    is_done = fields.Boolean(string="Erledigt", default=False)
    lead_id = fields.Many2one('crm.lead', string="Zugehöriger Lead", ondelete="cascade")

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    checklist_ids = fields.One2many('crm.lead.checklist', 'lead_id', string="Checkliste")
    checklist_progress = fields.Float(string="Checklisten-Fortschritt", compute="_compute_checklist_progress")

    @api.depends('checklist_ids.is_done')
    def _compute_checklist_progress(self):
        for lead in self:
            if lead.checklist_ids:
                total = len(lead.checklist_ids)
                done = sum(1 for item in lead.checklist_ids if item.is_done)
                lead.checklist_progress = (done / total) * 100
            else:
                lead.checklist_progress = 0
