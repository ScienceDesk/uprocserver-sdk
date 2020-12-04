import os
import requests
from uuid import uuid4


class UPSProcessRequest:
    def __init__(
        self,
        client,
        bucket,
        runner_file,
        output_files_dir,
        process_id=None,
        http_callback=None,
    ):
        self.client = client
        self.bucket = bucket
        self.runner_file = runner_file
        self.output_files_dir = output_files_dir
        self.process_id = process_id
        self.http_callback = http_callback
        self._support_files = set()
        self._input_files = set()

    def add_support(self, filepath):
        self._support_files.add(filepath)

    def add_input(self, filepath):
        self._input_files.add(filepath)

    def process(self):
        self.client.process(
            bucket=self.bucket,
            runner_file=self.runner_file,
            support_files=list(self._support_files),
            input_files=list(self._input_files),
            output_files_dir=self.output_files_dir,
            process_id=self.process_id,
            http_callback=self.http_callback,
        )


class UPSClient:
    def __init__(self, endpoint, jwtoken):
        self.endpoint = endpoint.strip().strip("/") + "/api/v1"
        self.authotization = dict(Authorization=f"Bearer {jwtoken}")

    def create_request(
        self,
        bucket,
        runner_file,
        output_files_dir,
        process_id=None,
        http_callback=None,
    ):
        return UPSProcessRequest(
            client=self,
            bucket=bucket,
            runner_file=runner_file,
            output_files_dir=output_files_dir,
            process_id=process_id,
            http_callback=http_callback,
        )

    def process(
        self,
        bucket,
        runner_file,
        support_files,
        input_files,
        output_files_dir,
        process_id=None,
        http_callback=None,
    ):
        payload = dict(
            bucket=bucket,
            runner_file=runner_file,
            support_files=support_files,
            input_files=input_files,
            output_files_dir=output_files_dir,
        )
        payload.update(dict(process_id=process_id)) if process_id else None
        payload.update(dict(http_callback=http_callback)) if http_callback else None
        return requests.post(
            self.endpoint + "/process",
            headers=self.authotization,
            json=payload,
        ).ok
