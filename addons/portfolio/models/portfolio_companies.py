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
    infos = fields.Text(compute="_compute_infos", store=False)
    projects_ids = fields.One2many(
        "portfolio.projects", "company_id", string="Projects")

    @api.depends('website', 'phone', 'email')
    def _compute_infos(self):
        for record in self:
            record.infos = "Website: " + record.website + "\nPhone: " + record.phone + "\nEmail: " + record.email
