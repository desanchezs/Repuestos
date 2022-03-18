import pandas as pd


class Reporte(object):
    """DESCRIPCION DE LA CLASE"""

    def __init__(self, dataFrame):
        """
        Constructor
        Args:
            ots: lista de diccionarios
        """
        self.df = dataFrame
        self.buses = self.df['BUS']
        self.tipo_ot = self.df['TIPO DE OT']
        self.parte_afectada = self.df['PARTE_AFECTADA']
        self.fecha_origen = self.df['FECHA DE ORIGEN']
        self.fecha_cierre = self.df['FECHA DE CIERRE']
        self.cuenta = self.df['CUENTA']
        self.valor_unitario = self.df['$ UNITARIO']
        self.valor_total = self.df['$ TOTAL']

    def cambio_de_parte_segun_bus(self, bus, parte):
        """
        Para un bus fijo y una parte fija observa qué tan seguido se está cambiando ficha parte en el bus dado
        Args:
            bus: str, identificador del bus
            parte: str, parte que se desea identificar
        Return:
             fechas: list, lista de datetimes en los cuales se le efectuo una reparacion al bus ingresado por parametro
        """
        # DataFrame de el bus seleccionado con la parte seleccionada
        df_bus_parte = self.df[(self.df['BUS'] == bus) & (self.df['PARTE_AFECTADA'] == parte)]

        # Extrae las fechas en las que se ha realizado un cambio para este repuesto
        fechas = list(df_bus_parte['FECHA DE ORIGEN'])
        return fechas

    def frecuencias_repuestos_bus(self, bus):
        """

        :param bus:
        :return:
        """
        pass

    def evolucion_precios_parte(self, parte):
        """
        Muestra la evolucion de los precios de una parte dada en todo el intervalo de tiempo disponible
        Args:
            parte: str, la parte que se quiere analizar
        Return:
            df_precios: DataFrame, dos columnas ('FECHA DE FACTURA' y 'PRECIO PROMEDIO') donde en la primera columna
            estan las fechas en las cuales hay informacion de la parte ingresada por parametro y en la segunda estan
            estan los precios promedios
        """
        # Se crea un DataFrame con solo los datos de la parte afectada
        df_parte = self.df[self.df['PARTE_AFECTADA'] == parte]

        # Fechas en la que la parte seleccionada estuvo disponible
        fechas = list(df_parte['FECHA DE FACTURA'].unique())

        # Para cada mes disponible selecciona el promedio de los precios
        # TODO: Hacerlo con la media truncada eliminando outliers
        precio_medio = []
        for fecha in fechas:
            precio = df_parte[df_parte['FECHA DE FACTURA'] == fecha]['FECHA DE FACTURA'].mean()
            precio_medio.append(precio)

        diccionario_precios = {'FECHAS': fechas, 'PRECIO MEDIO': precio_medio}
        df_precios = pd.DataFrame(data=diccionario_precios)
        return df_precios

    def gastos_cuenta_intervalo(self, cuenta, intervalo):
        """
        Dada una cuenta, retorna la suma de los valores totales de los items que hicieron parte de esta
        en un intervalo de tiempo dado.
        Args:
            cuenta: str, tipo de cuenta de la cual se van a extraer los valores. 'CARROCERIA', 'PLATAFORMA', etc.
            intervalo: lists of dates, fecha inicial y fecha final del itervalo de tiempo
        Return:
            valor_total: float, suma de los valores de las facturas de las cuentas
        """
        # Se crea un DataFrame solo con las filas asociadas a la cuenta dada
        df_cuenta = self.df[self.df['CUENTA'] == cuenta]

        # Mira aquellas filas que entran en el intervalo de tiempo ingresado por parametro
        df_cuenta_filtrada = df_cuenta[(df_cuenta['FECHA DE ORIGEN'] <= intervalo[0]) & (df_cuenta['FECHA DE ORIGEN']
                                                                                         >= intervalo[1])]

        valor_total = df_cuenta_filtrada['$ TOTAL'].sum()
        return valor_total
    
    def 
