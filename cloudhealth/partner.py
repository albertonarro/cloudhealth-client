from . import exceptions

class PartnerClient():

    def __init__(self, client):
        self.client = client

    def get_report_data(self, report_type, report_id, client_api_id):
        uri = f'olap_reports/{report_type}/{report_id}'
        params = [('client_api_id', client_api_id)]

        report = self.client.query(uri, method='GET', params=params)

        return report

    def list_assets(self, client_api_id, name):
        uri = '/api/search.json'
        params = [
            ('api_version', 2),
            ('client_api_id', client_api_id),
            ('name', name)
        ]

        assets = self.client.query(uri, method='GET', params=params)

        return assets
