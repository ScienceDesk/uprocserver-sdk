import os


class Files:
    def __init__(self, paths):
        self._files = {}
        for f in paths:
            self._files.update({os.path.basename(f).replace(".","_"): f})

    def __iter__(self):
        return self._files.values().__iter__()

    def __getitem__(self, idx):
        return list(self._files.values())[idx]

    def __getattr__(self, name):
        try:
            return self._files[name]
        except KeyError:
            raise AttributeError(f"'Files' object has no attribute '{name}'")

class UpServerIo:
    def __init__(
        self,
        input_files_dir="/input",
        support_files_dir="/support",
        output_files_dir="/outputs",
    ):
        self.input_files = Files(self._get_dir_files(input_files_dir))
        self.support_files = Files(self._get_dir_files(support_files_dir))
        self.output_files_dir = output_files_dir

    def _get_dir_files(self, directory):
        return [
            f
            for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
        ]
