class CombustibleInvalidoException(Exception):
    pass

class CombustibleInsuficienteException(Exception):
    pass

raise CombustibleInsuficienteException("El combustible no puede ser gasolina")