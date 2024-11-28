class cotxe:
    def __init__(self, marca, model, age, puertas, color):
        self.model = model
        self.age = age
        self.marca = marca
        self.puertas = puertas
        self.color = color
        
    def getmodel(self):
        return self.model
    def setmodel(self, new_model):
        self.model = new_model
        
    def getmarca(self):
        return self.marca
    def setmarca(self, new_marca):
        self.marca = new_marca
        
    def getcolor(self):
        return self.color
    def setcolor(self, new_color_cotxe):
        self.color = new_color_cotxe
    
    def getpuertas(self):
        return self.puertas
    def setpuertas(self, new_puertas):
        self.puertas = new_puertas
        
    def getage(self):
        return self.age
    def setage(self, new_age_cotxe):
        self.age = new_age_cotxe