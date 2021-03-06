class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.decription = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths_update(paths)
