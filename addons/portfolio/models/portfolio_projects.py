from odoo import fields, models


class PortfolioProjects(models.Model):
    _name = "portfolio.projects"
    _description = "Projects"

    name = fields.Char()
    description = fields.Text()
    website = fields.Char()
    logo = fields.Binary()
    company_id = fields.Many2one("portfolio.companies", string="Company")
