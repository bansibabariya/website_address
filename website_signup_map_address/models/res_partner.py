from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = "res.partner"

    lat = fields.Char("Latitude")
    lng = fields.Char("Longitude")

    @api.multi
    def location_redirect_map(self):
        for rec in self:
            url = "http://maps.google.com/maps?oi=map&q="
            # url = "https://maps.google.com/?q="+self.lat+","+self.lng
            if rec.street:
                url += rec.street.replace(' ', '+')
            if rec.city:
                url += '+' + rec.city.replace(' ', '+')
            if rec.state_id:
                url += '+' + rec.state_id.name.replace(' ', '+')
            if rec.country_id:
                url += '+' + rec.country_id.name.replace(' ', '+')
            if rec.zip:
                url += '+' + rec.zip.replace(' ', '+')
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': url
        }