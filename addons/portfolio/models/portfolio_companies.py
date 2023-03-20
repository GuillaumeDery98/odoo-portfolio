from odoo import fields, models


class PortfolioCompanies(models.Model):
    _name = "portfolio.companies"
    _description = "Companies"

    name = fields.Char()
    post = fields.Char()
    description = fields.Text()
    website = fields.Char()
    phone = fields.Char()
    email = fields.Char()
