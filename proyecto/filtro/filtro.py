from os import getcwd, path
# from proyecto.filtro.events_ids import event_ids  # Descomentar esta linea para probar localmente

class Filtro:
    """
    Clase Filtro con metodos para filtrar datos del archivo wls_day-20 en la ruta /proyecto/filtro/data_sets/wls_day-20
    """

    # Atributos
    def __init__(self):
        self.working_directory = getcwd()
        # Cambiar ruta a data_sets\\wls_day-20\\wls_day-20 para correr localmente
        self.archivo = path.join(getcwd(), 'filtro\\data_sets\\wls_day-20\\wls_day-20')
        self.contenido = []
        self.contenido_filtrado = []
        self.user_name = None
        self.event_id = None
        self.logon_host = None
        self.domain_name = None
        self.fecha_inicial = None
        self.fecha_final = None
        # self.id = event_ids()  # Descomentar esta linea para probar localmente

    def leer_por_pedazos(self, archivo, lineas=-1):
        """
        Lee pedazos de contenido
        :param archivo: Ruta del archivo a leer
        :param tamano: Tamaño del pedazo a leer
        :return: None
        """
        i = 1
        while True:
            datos = archivo.readline()
            i = i + 1
            if not datos or i == lineas:
                break
            yield datos

    def get_contenido_del_archivo(self):
        """
        Guarda el contenido del archivo en el atributo self.contenido
        :return: None
        """
        self.borrar_contenido_filtrado()
        self.contenido = []

        with open(self.archivo) as archivo:
            for linea in self.leer_por_pedazos(archivo, lineas=1002):
                self.contenido.append(f"<li>{linea}</li>")
        return self.contenido

    def borrar_contenido_filtrado(self):
        """
        Borra el contenido en el atributo self.contenido_filtrado
        :return: None
        :return:
        """
        self.contenido_filtrado = []

    def print_contenido(self):
        """
        Imprime el contenido guardado en el atributo self.contenido
        :return: None
        """
        if len(self.contenido) <= 0:
            self.get_contenido_del_archivo()
        for linea in self.contenido:
            print(linea)

    def print_contenido_filtrado(self):
        """
        Imprime el contenido guardado en el atributo self.contenido_filtrado
        :return: None
        """
        for linea in self.contenido_filtrado:
            print(linea)

    def filtrar_por_user_name(self, user_name):
        """
        Lee el contenido del archivo, filtra los datos por UserName y guarda el
        contenido filtrado en el atrubuto self.contenido_filtrado
        :param user_name: String del UserName que se desea fitlrar
        :return: Arreglo filtrado
        """
        self.borrar_contenido_filtrado()
        with open(self.archivo) as archivo:
            for linea in self.leer_por_pedazos(archivo, lineas=-1):
                if f'"UserName": "{user_name}"' in linea:
                    self.contenido_filtrado.append(f"<li>{linea}</li>")
        return self.contenido_filtrado

    def filtrar_por_event_id(self, event_id):
        """
        Lee el contenido del archivo, filtra los datos por EventID y guarda el
        contenido filtrado en el atrubuto self.contenido_filtrado
        :param event_id: Numero entero del ID que se desea fitlrar
        :return: Arreglo filtrado
        """
        self.borrar_contenido_filtrado()
        with open(self.archivo) as archivo:
            for linea in self.leer_por_pedazos(archivo):
                if str(f'"EventID": {event_id}') in linea:
                    self.contenido_filtrado.append(linea)
        return self.contenido_filtrado

    def filtrar_por_log_host(self, log_host):
        """
        Lee el contenido del archivo, filtra los datos por LogHost y guarda el
        contenido filtrado en el atrubuto self.contenido_filtrado
        :param log_host: String del LogHost que se desea fitlrar
        :return: Arreglo filtrado
        """
        self.borrar_contenido_filtrado()
        with open(self.archivo) as archivo:
            for linea in self.leer_por_pedazos(archivo):
                if f'"LogHost": "{log_host}"' in linea:
                    self.contenido_filtrado.append(linea)
        return self.contenido_filtrado

    def filtrar_por_domain_name(self, domain_name):
        """
        Lee el contenido del archivo, filtra los datos por DomainName y guarda el
        contenido filtrado en el atrubuto self.contenido_filtrado
        :param domain_name: String del DomainName que se desea fitlrar
        :return: Arreglo filtrado
        """
        self.borrar_contenido_filtrado()
        with open(self.archivo) as archivo:
            for linea in self.leer_por_pedazos(archivo):
                if f'"DomainName": "{domain_name}"' in linea:
                    self.contenido_filtrado.append(linea)
        return self.contenido_filtrado

    def filtrar_por_tiempo(self, tiempo_inicial=None, tiempo_final=None):
        """
        Lee el contenido del archivo, filtra los datos por el rango de tiempo deseado y guarda el
        contenido filtrado en el atrubuto self.contenido_filtrado. Si no se especifica tiempo final
        ni inicial se toman todos los datos. Si se especifica unicamente el tiempo inicial, se filtran
        desde es ese tiempo en adelante. Si se especifica unicamente el tiempo final, se filtrar hasta ese tiempo
        :param tiempo_inicial: Tiempo inicial para filtrar
        :param tiempo_final: Tiempo final para filtrar
        :return: Arreglo filtrado
        """
        self.borrar_contenido_filtrado()
        # Si no se especifica el tiempo inicial ni el tiempo final
        if not tiempo_inicial and not tiempo_final:
            self.contenido_filtrado = ["NO SE FILTRARON DATOS, DEBE ESPECIFICAR TIEMPOS"]
        else:
            with open(self.archivo) as archivo:
                for linea in self.leer_por_pedazos(archivo):
                    # Si se especifica solo el tiempo inicial se filtra desde el tiempo inicial en adelante
                    if tiempo_inicial and not tiempo_final:
                        for linea in self.contenido:
                            indice = linea.find('"Time": ')
                            if indice >= 0:
                                tiempo_del_paquete = int(linea[indice + 8:indice + 15])
                                if tiempo_del_paquete >= int(tiempo_inicial):
                                    self.contenido_filtrado.append(linea)

                    # Si se especifica solo el tiempo final se filtra desde el paquete mas antiguo hasta el tiempo final
                    elif not tiempo_inicial and tiempo_final:
                        for linea in self.contenido:
                            indice = linea.find('"Time": ')
                            if indice >= 0:
                                tiempo_del_paquete = int(linea[indice + 8:indice + 15])
                                if tiempo_del_paquete <= int(tiempo_final):
                                    self.contenido_filtrado.append(linea)

                    # Si se especifica el tiempo inicial y el tiempo final se filtran los paquentes entre el tiempo inicial y final
                    elif tiempo_inicial and tiempo_final:
                        for linea in self.contenido:
                            indice = linea.find('"Time": ')
                            if indice >= 0:
                                tiempo_del_paquete = int(linea[indice + 8:indice + 15])
                                if int(tiempo_inicial) <= tiempo_del_paquete <= int(tiempo_final):
                                    self.contenido_filtrado.append(linea)
        return self.contenido_filtrado

# filtro = Filtro()
#
# # Muestra todos los paquetes que tengan un UserName deseado
# filtro.filtrar_por_user_name(user_name="system")
# print("\n\n******************************************\n"
#       "** Contenido filtrado por user name system ***\n"
#       "******************************************\n\n")
# filtro.print_contenido_filtrado()
#
# # Muestra todos los paquetes que tengan un EventID deseado
# filtro.filtrar_por_event_id(event_id=filtro.id.process_start)
# print("\n\n******************************************\n"
#       f"** Contenido filtrado por event id {filtro.id.process_start} ***\n"
#       "******************************************\n\n")
# filtro.print_contenido_filtrado()
#
# # Muestra todos los paquetes que tengan un LogHost deseado
# filtro.filtrar_por_log_host(log_host="Comp309261")
# print("\n\n******************************************\n"
#       "***  Contenido filtrado por log host Comp309261 ***\n"
#       "******************************************\n\n")
# filtro.print_contenido_filtrado()
#
# # Muestra todos los paquetes que tengan un DomainName deseado
# filtro.filtrar_por_domain_name(domain_name="Domain001")
# print("\n\n******************************************\n"
#       "***  Contenido filtrado por domain name Domain001\n"
#       "******************************************\n\n")
# filtro.print_contenido_filtrado()
#
# # Muestra todos los paquetes de entre cierto rango de tiempo
# filtro.filtrar_por_tiempo()
# print("\n\n******************************************\n"
#       "***  Contenido filtrado por tiempo NA ***\n"
#       "******************************************\n\n")
# filtro.print_contenido_filtrado()
#
# # Muestra todos los paquetes de entre cierto rango de tiempo
# filtro.filtrar_por_tiempo(tiempo_inicial=1641600)
# print("\n\n******************************************\n"
#       "***  Contenido filtrado por tiempo TI 1641600 ***\n"
#       "******************************************\n\n")
# filtro.print_contenido_filtrado()
#
# # Muestra todos los paquetes de entre cierto rango de tiempo
# filtro.filtrar_por_tiempo(tiempo_final=1641600)
# print("\n\n******************************************\n"
#       "***  Contenido filtrado por tiempo TF 1641600 ***\n"
#       "******************************************\n\n")
# filtro.print_contenido_filtrado()
#
# # Muestra todos los paquetes de entre cierto rango de tiempo
# filtro.filtrar_por_tiempo(tiempo_inicial=1641500, tiempo_final=1641600)
# print("\n\n******************************************\n"
#       "***  Contenido filtrado por tiempo 1641500 - 1641600 ***\n"
#       "******************************************\n\n")
# filtro.print_contenido_filtrado()
