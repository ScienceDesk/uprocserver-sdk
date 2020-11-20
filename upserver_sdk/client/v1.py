import os
import requests
from uuid import uuid4


# class UPSRequest:
#     def __init__(self, runner_file, support_files_dir, client):
#         self.id = uuid4().hex
#         self.runner_file = runner_file
#         self.support_files_dir = support_files_dir

#     @property
#     def input_files_dir(self):
#         return os.path.join("/", self.id, "inputs")

#     @property
#     def output_files_dir(self):
#         return os.path.join("/", self.id, "inputs")


class UPSClient:
    def __init__(self, endpoint, jwtoken):
        self.endpoint = endpoint.strip().strip("/") + "/api/v1"
        self.authotization = dict(Authorization=f"Bearer {jwtoken}")

    # @classmethod
    # def create_request(self, runner_file, support_files_dir):
    #     return UPSRequest(runner_file, support_files_dir, self)

    def process(
        self,
        runner_file,
        support_files_dir,
        input_files_dir,
        output_files_dir,
        process_id=None,
        http_callback=None,
    ):
        payload = {
            "runner_file": runner_file,
            "support_files_dir": support_files_dir,
            "input_files_dir": input_files_dir,
            "output_files_dir": output_files_dir,
        }
        payload.update(dict(process_id=process_id)) if process_id else None
        payload.update(dict(http_callback=http_callback)) if http_callback else None
        return requests.post(
            self.endpoint + "/process", headers=self.authotization, json=payload,
        ).ok
