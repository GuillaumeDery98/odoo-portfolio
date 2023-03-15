from odoo import fields, models


class PortfolioCompanies(models.Model):
    _name = "portfolio.companies"
    _description = "Companies"

    name = fields.Char()
