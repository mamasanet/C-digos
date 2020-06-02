from ClaseAuto import Auto
import abc

class AutoNuevo(Auto):
    __marca = 'Fiat'
    __version = ''

    def __init__(self, modelo, puertas, color, precio, version):
        super().__init__(modelo, puertas, color, precio)
        self.__version = version

    @abc.abstractmethod
    def getPat(self):
        pass

    def getImporte(self):
        porcentaje = 0.1
        p = (porcentaje * self.getPrecio()) / 100
        if self.__version == 'Full':
            k = (0.02 * self.getPrecio()) / 100
        else:
            k = 0
        return (self.getPrecio() + p + k)

    def toJSON(self):
        return dict(
                    __class__ = self.__class__.__name__,
                    __atributos__ = dict(
                                            modelo = self.getModelo(),
                                            puertas = self.getPuertas(),
                                            color = self.getColor(),
                                            precio = self.getPrecio(),
                                            version = self.__version
                                        )
                    )

    def __str__(self):
        super().mostrar()
        return 'MARCA: %s - VERSIÓN: %s - IMPORTE DE VENTA: %s' % (self.__marca, self.__version, self.getImporte())