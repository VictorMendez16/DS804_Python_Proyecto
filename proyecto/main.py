from flask import Flask
from flask import request
from filtro.filtro import Filtro

app = Flask(__name__) # Instancia de flask llamada app
filtro = Filtro()

@app.route('/')  # Anotador para unicamente modificar el codigo sin tener que hacer una instancia de app
def index():
    """
    Metodo index que contiene la pagina web

    :return: Contenido hacia el navegador
    """
    paquetes = filtro.get_contenido_del_archivo()

    # Crea una lista para los paquetes
    # for linea in paquetes:
    #     paquetes_html = paquetes_html + f"<li>{linea}</li><br>"
    # Contenido html
    html = '<div>' \
           '    <h1>Bienvenido a la pagina principal</h1>' \
           '    <h2>Del siguiente data set se puede filtrar los paquetes por uno de los siguientes campos.</h2>' \
           '' \
           '    <h3>Para tomar un criterio en cuenta llena la informacion deseada. ' \
           '        Para ignorar el atributo deja el campo en blanco</h3>' \
           '</div>' \
           '<div id="filtros">' \
           '    <h3>Filtros</h3>' \
           '    <form action="data_set_filtrado" method="post">' \
           '        <label for="user_name">User Name</label>' \
           '        <input type="text" name="user_name" id="user_name">' \
           '' \
           '        <label for="event_id">Event ID</label>' \
           '        <input type="text" name="event_id" id="event_id">' \
           '' \
           '        <label for="log_host">Log Host</label>' \
           '        <input type="text" name="log_host" id="log_host">' \
           '' \
           '        <label for="damain_name">Domain Name</label>' \
           '        <input type="text" name="domain_name" id="domain_name">' \
           '<br><br>' \
           '        <label for="tiempo_inicial">Tiempo Inicial</label>' \
           '        <input type="text" name="tiempo_inicial" id="tiempo_inicial">' \
           '' \
           '        <label for="tiempo_final">Tiempo Final</label>' \
           '        <input type="text" name="tiempo_final" id="tiempo_final">' \
           '<br><br>' \
           '        <input type="submit" name="filtrar" value="Filtrar">' \
           '    </form>' \
           '</div>' \
           '<div>' \
           '    <br><br>' \
           f'    <h2>Contenido del data set:</h2>' \
           f'    <p>Primeros 1000 paquetes</p>' \
           f'    <ol>' \
           f'       {paquetes}' \
           f'    </ol>' \
           f'</div>'

    return html

@app.post('/data_set_filtrado')
def getInput():
    """
    Metodo que contiene la pagina para los paquetes filtrados

    :return: Contenido html hacia el navegador
    """
    user_name = request.form.get('user_name')
    event_id = request.form.get('event_id')
    log_host = request.form.get('log_host')
    domain_name = request.form.get('domain_name')
    tiempo_inicial = request.form.get('tiempo_inicial')
    tiempo_final = request.form.get('tiempo_final')
    paquetes = filtrar_data_set(user_name=user_name, event_id=event_id, log_host=log_host, domain_name=domain_name,
                                tiempo_inical=tiempo_inicial, tiempo_final=tiempo_final)

    # # Crea una lista para los paquetes fitlrados
    # for linea in paquetes:
    #     paquetes_html = paquetes_html + f"<li>{linea}</li><br>"

    # Contenido de la pagina de los paquetes filtrados
    html = "<p>Data set filtrado con los siguientes atributos:</p>" \
           f"<p>" \
           f"   User Name: {user_name}<br>Event ID: {event_id}<br>" \
           f"   Log Host: {log_host}<br>Domain Name: {domain_name}<br>" \
           f"   Tiempo: ({tiempo_inicial}) - ({tiempo_final})<br>" \
           f"</p><br>" \
           f"<ol>" \
           f"{paquetes}" \
           f"</ol>"  # Inserta la lista de los paquetes filtrados

    return html

def filtrar_data_set(user_name=None, event_id=None, log_host=None, domain_name=None,
                     tiempo_inical=None, tiempo_final=None):
    """
    Filtra los datos en base a UserName, EventID, LogHost, DomainName o un rango de tiempo

    :param user_name: String del User Name a filtrar
    :param event_id: Int del ID del evento a filtrar
    :param log_host: String del LongHost a filtrar
    :param domain_name: String del Damain Name a filtrar
    :param tiempo_inical: Int del tiempo inical a filtar
    :param tiempo_final: Int del tiempo final a filtrar
    :return:
    """
    if user_name and not (event_id or log_host or domain_name or tiempo_inical or tiempo_final):
        return filtro.filtrar_por_user_name(user_name=user_name)
    elif event_id and not (user_name or log_host or domain_name or tiempo_inical or tiempo_final):
        return filtro.filtrar_por_event_id(event_id=event_id)
    elif log_host and not (user_name or event_id or domain_name or tiempo_inical or tiempo_final):
        return filtro.filtrar_por_log_host(log_host=log_host)
    elif domain_name and not (user_name or event_id or log_host or tiempo_inical or tiempo_final):
        return filtro.filtrar_por_domain_name(domain_name=domain_name)
    elif tiempo_inical or tiempo_final and not (user_name or event_id or log_host or domain_name):
        return filtro.filtrar_por_tiempo(tiempo_inicial=tiempo_inical, tiempo_final=tiempo_final)
    else:
        return ["TIEMPO DE INICIO DEBE SER MAYOR O IGUAL AL TIEMPO FINAL"]
