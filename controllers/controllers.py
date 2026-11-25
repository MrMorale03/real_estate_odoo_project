# from odoo import http


# class RealEstateNge(http.Controller):
#     @http.route('/real_estate_nge/real_estate_nge', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/real_estate_nge/real_estate_nge/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('real_estate_nge.listing', {
#             'root': '/real_estate_nge/real_estate_nge',
#             'objects': http.request.env['real_estate_nge.real_estate_nge'].search([]),
#         })

#     @http.route('/real_estate_nge/real_estate_nge/objects/<model("real_estate_nge.real_estate_nge"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('real_estate_nge.object', {
#             'object': obj
#         })

