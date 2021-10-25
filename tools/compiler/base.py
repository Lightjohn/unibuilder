class Base:

    files = []

    def is_valid(self, local_files):
        for local_file in local_files:
            if local_file in self.files:
                return True
        return False

    def init(self):
        print("STUB: Fake init")

    def compile(self):
        print("STUB: Fake compile")

    def install(self):
        print("STUB: Fake install")
