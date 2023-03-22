from odoo import api, fields, models


class PortfolioCompanies(models.Model):
    _name = "portfolio.companies"
    _description = "Companies"

    name = fields.Char()
    post = fields.Char()
    description = fields.Text()
    website = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    logo = fields.Binary()
    info = fields.Char(compute="_compute_info", store=False)
    projects_ids = fields.One2many(
        "portfolio.projects", "company_id", string="Projects")

    @api.depends('website', 'phone', 'email')
    def _compute_info(self):
        for record in self:
            record.info = record.website + record.phone + record.email
