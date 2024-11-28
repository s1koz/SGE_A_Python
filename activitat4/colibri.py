class colibri:
    def __init__(self, nom, clase, age, longitud, color):
        self.nom = nom
        self.age = age
        self.clase = clase
        self.longitud = longitud
        self.color = color
        
    def getnom(self):
        return self.nom
    def setnom(self, new_nom_colibri):
        self.nom = new_nom_colibri
        
    def getclase(self):
        return self.clase
    def setclase(self, new_clase):
        self.clase = new_clase
        
    def getcolor(self):
        return self.color
    def setcolor(self, new_color_colibri):
        self.color = new_color_colibri
    
    def getlongitud(self):
        return self.longitud
    def setlongitud(self, new_longitud):
        self.longitud = new_longitud
        
    def getage(self):
        return self.age
    def setage(self, new_age_colibri):
        self.age = new_age_colibri