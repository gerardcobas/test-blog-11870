# Malta & Breakdown

Blog de pruebas para el site 11870 de Marfeel (whisky y metalcore). Todas las páginas cargan el SDK de Marfeel con `accountId` 11870.

Regenerar: `python3 _build/build_blog.py`. Las URLs para el generador de tráfico están en `urls.txt`. Fotos con licencia Creative Commons, con el crédito en cada artículo.

## Tráfico automático

`launchd` ejecuta `_build/hourly.py` de lunes a viernes cada hora de 6:00 a 19:00. Cada ejecución espera de 0 a 40 minutos, hace entre 2 y 24 visitas según la hora y convierte (`CTA Newsletter`) entre el 10 % y el 35 %.

- Log: `~/Library/Logs/test-blog-11870/traffic.log`
- Activar: `_build/launchd/install.sh`
- Parar: `launchctl bootout gui/$(id -u)/com.test-blog-11870.traffic`
