from django.forms import ValidationError

class TamañoMaximoValidator:

    def __init__(self, max_file_size=1):
        self.max_file_size = max_file_size

    def __call__(self, value):
        tamaño = value.size
        maxfiletamaño = self.max_file_size * 1048576 

        if tamaño > maxfiletamaño:
            raise ValidationError(f" el tamaño maximo debe ser {self.maxfile} mb")

        return value
