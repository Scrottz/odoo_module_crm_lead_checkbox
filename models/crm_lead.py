from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'  # Erweitert das bestehende CRM-Lead-Modell

    checklist_ids = fields.One2many(
        'crm.lead.checklist',  # Verknüpfung zum Checklisten-Modell
        'lead_id',
        string="Checkliste"
    )

    checklist_progress = fields.Float(
        string="Checklisten-Fortschritt",
        compute="_compute_checklist_progress",
        store=True
    )

    @api.depends('checklist_ids.is_done')
    def _compute_checklist_progress(self):
        """ Berechnet den Fortschrittswert der Checkliste in Prozent. """
        for lead in self:
            total_items = len(lead.checklist_ids)
            if total_items > 0:
                done_items = sum(1 for item in lead.checklist_ids if item.is_done)
                lead.checklist_progress = (done_items / total_items) * 100
            else:
                lead.checklist_progress = 0.0