from odoo import fields, models


class PortfolioScreenshots(models.Model):
    _name = 'portfolio.screenshots'
    _description = 'Screenshots of projects'

    name = fields.Char()
    screenshot = fields.Binary()
    project_id = fields.Many2one('portfolio.projects', string='Project')
