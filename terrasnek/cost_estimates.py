"""
Module for Terraform Cloud API Endpoint: Cost Estimates.
"""

from .endpoint import TFCEndpoint

class TFCCostEstimates(TFCEndpoint):
    """
    `API Docs \
        <https://www.terraform.io/docs/cloud/api/cost-estimates.html>`_
    """

    def __init__(self, instance_url, org_name, headers, well_known_paths, verify, log_level):
        super().__init__(instance_url, org_name, headers, well_known_paths, verify, log_level)
        self._endpoint_base_url = f"{self._api_v2_base_url}/cost-estimates"

    def required_entitlements(self):
        return []

    def show(self, cost_est_id):
        """
        ``GET /cost-estimates/:id``

        `API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/cost-estimates.html#show-a-cost-estimate>`_
        """
        url = f"{self._endpoint_base_url}/{cost_est_id}"
        return self._show(url)
