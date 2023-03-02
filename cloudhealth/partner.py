from datetime import datetime
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


    def create_customer(self, name=None, street1=None, street2=None,city=None, state=None, zipcode=None, country=None, classification=None,trial_expiration=None, billing_contact=None,partner_billing_configuration=False,partner_billing_configuration_folder=None, tags=None):
        uri = '/v1/customers'
        data = {
            "name": name,
            "address": {
                "street1": street1,
                "street2": street2,
                "city": city,
                "state": state,
                "zipcode": zipcode,
                "country": country
            },
            "partner_billing_configuration": {}
        }

        if classification:
            data['classification'] = classification
        if isinstance(trial_expiration, datetime):
            data['trial_expiration'] = trial_expiration.isoformat()
        if isinstance(trial_expiration, str):
            data['trial_expiration'] = trial_expiration
        if billing_contact:
            data['billing_contact'] = billing_contact
        if partner_billing_configuration:
            data['partner_billing_configuration']['enabled'] = partner_billing_configuration
        if partner_billing_configuration_folder:
            data['partner_billing_configuration']['folder'] = partner_billing_configuration_folder
        if tags:
            data['tags'] = tags

        customer = self.client.query(uri, method='POST', data=data)

        return customer


    def update_customer(self, client_api_id, name=None, street1=None, street2=None, city=None, state=None, zipcode=None, country=None, classification=None, trial_expiration=None, billing_contact=None, partner_billing_configuration=False, partner_billing_configuration_folder=None, tags=None):
        uri = f'/v1/customers/{client_api_id}'
        data = {
            "partner_billing_configuration": {},
            "address": {}
        }

        if name:
            data['name'] = name
        if street1:
            data['street1'] = street1
        if street2:
            data['street2'] = street2
        if city:
            data['city'] = city
        if state:
            data['state'] = state
        if zipcode:
            data['zipcode'] = zipcode
        if country:
            data['country'] = country
        if classification:
            data['classification'] = classification
        if isinstance(trial_expiration, datetime):
            data['trial_expiration'] = trial_expiration.isoformat()
        if isinstance(trial_expiration, str):
            data['trial_expiration'] = trial_expiration
        if billing_contact:
            data['billing_contact'] = billing_contact
        if partner_billing_configuration:
            data['partner_billing_configuration']['enabled'] = partner_billing_configuration
        if partner_billing_configuration_folder:
            data['partner_billing_configuration']['folder'] = partner_billing_configuration_folder
        if tags:
            data['tags'] = tags

        if not data['address']:
            del data['address']
        if not data['partner_billing_configuration']:
            del data['partner_billing_configuration']


        customer = self.client.query(uri, method='PUT', data=data)

        return customer


    def get_customer(self, client_api_id):
        uri = f'/v1/customers/{client_api_id}'

        customer = self.client.query(uri, method='GET')

        return customer


    def delete_customer(self, client_api_id):
        uri = f'/v1/customers/{client_api_id}'
        
        response = self.client.query(uri, method='DELETE')

        return response


