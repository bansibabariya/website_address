from odoo import fields, http, tools, _
from odoo.http import request
from odoo.addons.website.controllers.main import Website
from odoo.addons.auth_signup.controllers.main import AuthSignupHome as Home

class AuthSignupHome(Home):

    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        values = { key: qcontext.get(key) for key in ('login', 'name','line1','lat','lng','password') }
        if not values:
            raise UserError(_("The form was not properly filled in."))
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match; please retype them."))
        supported_lang_codes = [code for code, _ in request.env['res.lang'].get_installed()]
        lang = request.context.get('lang', '').split('_')[0]
        if lang in supported_lang_codes:
            values['lang'] = lang
        self._signup_with_values(qcontext.get('token'), values)
        user = request.env['res.users'].sudo().search([('id','=',request.uid)])
        user.partner_id.street = values.get('line1')
        user.partner_id.lat = values.get('lat')
        user.partner_id.lng = values.get('lng')
        request.env.cr.commit()
