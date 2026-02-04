import requests
import jinja2
from exporters.exporter import Exporter
from filament.generic import GenericFilament
from reader.scan_result import ScanResult
import logging
import json

class WebhookExporter(Exporter):
    def __init__(self, config : dict):
        super().__init__(config)
        self.env = jinja2.Environment('{%', '%}', '{', '}')
        self.url_template = self.env.from_string(config["url"])
        self.method = str(config.get("method", "POST")).upper()
        self.headers = config.get("headers", {})
        body_json_template = config.get("body_json_template", "")
        self.body_json_template = self.env.from_string(body_json_template) if body_json_template else None
        self.timeout = float(config.get("timeout", 5.0))

    def export_data(self, scan: ScanResult, filament: GenericFilament):

        context = scan.to_dict() | filament.to_dict()

        try:
            url = str(self.url_template.render(context))
            json_data = None

            if self.body_json_template:
                body_str = self.body_json_template.render(context)
                json_data = json.loads(body_str)

            response = requests.request(
                method=self.method,
                url=url,
                json=json_data,
                headers=self.headers,
                timeout=self.timeout
            )

            response.raise_for_status()
            return True
        except Exception as e:
            logging.exception(f"Failed to export data via webhook: {e}")