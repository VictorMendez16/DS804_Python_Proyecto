# DS804_Python

Este repositorio contiene el proyecto para la clase de DS804_Python
Trata sobre un sitio web en donde se analizaran datos bajo riesgo de seguridad dada una fecha

Para correr el proyecto 
1.- Cambia la direccion al folder de proyecto
cd proyecto

2.-Ejecuta la aplicacion
flask --app main run 
deberas ver un output como el siguiente: 

 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

3.- Sigue la liga para ver el navegador

4.- ctrl + C para terminar la ejecucion

Muestra todos los paquetes que tengan un UserName deseado
Muestra todos los paquetes que tengan un EventID deseado
Muestra todos los paquetes que tengan un LogHost deseado
Muestra todos los paquetes que tengan un DomainName deseado
Muestra todos los paquetes de entre cierto rango de tiempo

Lista de EventIDs disponibles:
4768	Kerberos authentication ticket was requested (TGT)
4769	Kerberos service ticket was requested (TGS)
4770	Kerberos service ticket was renewed
4774	An account was mapped for logon
4776	The domain controller attempted to validate the credentials for an account
4624	An account was successfully logged on
4625	An account failed to logon on
4634	An account was logged on
4647	User initiated logon
4648	A logon was attempted using explicit credentials
4672	Special privileges assigned to a new logon
4800	The workstation was locked
4801	The workstation was unlocked
4802	The screensaver was invoked
4803	The screensaver was dismissed
4688	Process start
4689	Process end
4608	Windows is starting up
4609	Windows is shutting down
1100	Event logging service has shut down (often recorded instead of EventID 4609)