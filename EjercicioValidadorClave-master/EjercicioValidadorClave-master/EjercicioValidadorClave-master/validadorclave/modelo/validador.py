# Importamos las excepciones definidas en el módulo errores.py
from errores import *

# La clase ReglaValidacion es una clase abstracta y su método es_valida es igualmente abstracto
class ReglaValidacion:
    def __init__(self, longitud_esperada): # _longitud_esperada lo inicializamos como el constructor de la clase e indica la longitud que la clave debe superar.
        self._longitud_esperada = longitud_esperada

# El método _validar_longitud de la clase ReglaValidacion implementa la lógica para verificar la longitud de la clave. 
    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada # Para implementar dicho método debes tener en cuenta el atributo _longitud_esperada.

"""Los métodos _contiene_mayuscula, _contiene_minuscula y _contiene_numero de la clase ReglaValidacion
implementan correspondientemente la lógica que verifica si una clave tiene una letra mayúscula, tiene 
una letra minúscula y tiene un número. Para implementar dichos métodos puedes utilizar los métodos de la 
clase str isupper(), islower() e isdigit()."""

# La clase ReglaValidacionGanimedes tiene un método contiene_caracter_especial donde debes implementar la lógica para verificar si una clave contiene al menos uno de los caracteres especiales @ _ # $ %.

class ReglaValidacionGanimedes(ReglaValidacion):
    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)

    def contiene_caracter_especial(self, clave):
        caracteres_especiales = ['@', '_', '#', '$', '%']
        return any(c in clave for c in caracteres_especiales)

    def es_valida(self, clave):
        self._validar_longitud(clave)
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError()
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError()
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError()
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError()
        return True

# La clase ReglaValidacionCalisto tiene un método contiene_calisto donde debes implementar la lógica para verificar si una clave contiene la palabra calisto escrita con al menos dos letras mayúsculas, pero no con todas las letras mayúsculas.

class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(self, clave):
        return 'calisto' in clave.lower()

    def es_valida(self, clave):
        self._validar_longitud(clave)
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError()
        return True

# Los métodos es_valida en las clases ReglaValidacionGanimedes y ReglaValidacionCalisto son las implementaciones del método abstracto de la clase padre. En estos métodos debes implementar las reglas correspondientes a cada tipo de validación, utilizando los demás métodos donde están definidas cada una de las reglas.

class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave): # El método es_valida de la clase Validador debe retornar el resultado de invocar el método es_valida en el objeto regla que tiene como atributo.
        return self.regla.es_valida(clave)

# Ejemplo
def main():
    clave_ganimedes = "P@ssw0rd"
    clave_calisto = "cAliStO2023"

    validador_ganimedes = Validador(ReglaValidacionGanimedes(8))
    validador_calisto = Validador(ReglaValidacionCalisto(6))

    try:
        print("Validando clave con regla de Validación Ganímedes:")
        print(validador_ganimedes.es_valida(clave_ganimedes))
    except ValidadorError as e:
        print(f"Error: {e}")

    try:
        print("Validando clave con regla de Validación Calisto:")
        print(validador_calisto.es_valida(clave_calisto))
    except ValidadorError as e:
        print(f"Error: {e}")
main()