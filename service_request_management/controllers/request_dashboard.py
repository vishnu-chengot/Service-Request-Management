from odoo import http
from odoo.http import request
import json


class RequestDashboardController(http.Controller):

    @http.route('/request/dashboard/status', type='json', auth='user')
    def get_request_status_data(self, **kwargs):
        """
        Returns count of requests grouped by status
        """
        try:
            # Replace 'request.model' with your actual model name
            Request = request.env['service.request']

            # Query to get count by status
            query = """
                SELECT state, COUNT(*) as count
                FROM service_request
                GROUP BY state
                ORDER BY state
            """

            request.env.cr.execute(query)
            results = request.env.cr.dictfetchall()

            return {
                'status_counts': results,
                'success': True
            }

        except Exception as e:
            return {
                'status_counts': [],
                'success': False,
                'error': str(e)
            }