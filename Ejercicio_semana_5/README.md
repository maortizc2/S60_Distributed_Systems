## Semana 5: Practica de RPC mediada por IA
**Dinámica de trabajo:** De la clase 4, se explicó el modelo general de RPC para comunicar un cliente con un servidor. Vamos
a practicar y entender estas comunicaciones ayudados por chatgpt

**Emite estos prompts en este orden:**
1. Como estudiante, en un curso de sistemas distribuidos, en Ingeniería de Sistemas, para la clase de hoy de comunicaciones remotas con RPC, quiero realizar un ejercicio muy rápido, de crear un programa en python, uno cliente y otro servidor, con la librería de HTTP de pyhton, que permita a un servidor implementar una calculadora que suma, resta, multiplica y y divide. El cliente envía la operación (sumar, restar, multiplicar o dividir), más 2 parámetros de números reales a y b, y retorna el resultado directamente como respuesta en el response de http. quiero hacer las 2 versiones, una por GET enviando la operación y parámetros en la URI, y otra por POST enviando la operación y parámetros en el body.
2. Explícame de forma detallada como se aplica acá el modelo de comunicación sincrónica en sistemas distribuidos basados en RPC usando http
como protocolo entre cliente y servidor se usa acá un IDL o como se resuelve el problema de la codificación de datos y generación de proxy tanto en el cliente como en el servidor
3. De los conceptos vistos en la clase de RPC, como se relacionan los conceptos con este ejemplo de la calculadora usando HTTP como RPC.
(adjunta la presentación de la clase 4 sobre rpc).