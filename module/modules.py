import pickle

class Modules:

    def __init__(self):
        self.modules = []
    
    def add(self, module):
        self.modules.append(module)

    def get(self):
        return self.modules

    def load(self):
        with open('store.modules', 'rb') as config_dictionary_file:
            self.modules = pickle.load(config_dictionary_file)
            

    def store(self):        
        with open('store.modules', 'wb') as config_dictionary_file:
            pickle.dump(self.modules, config_dictionary_file)