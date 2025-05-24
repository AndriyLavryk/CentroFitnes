CentroFitnes — Flask + SQLite

ESPAÑOL
Aplicación web para gestionar clientes de un centro fitness usando Flask y SQLite para almacenamiento local. Ideal para testing y desarrollo sin configurar base de datos externa.
Requisitos: Python 3.7+, paquetes en requirements.txt.
Instalación:

git clone https://github.com/AndriyLavryk/CentroFitnes.git  
cd CentroFitnes  
python -m venv .venv  
# Windows  
.venv\Scripts\activate  
# Linux/macOS  
source .venv/bin/activate  
pip install -r requirements.txt  

Uso:

python app.py  

Abre en el navegador: http://localhost:5000
Notas:

    La base de datos SQLite app.db se crea automáticamente en la raíz del proyecto.

    Para reiniciar la base de datos, elimina app.db y reinicia la app.

    SECRET_KEY está configurado en app.py para desarrollo. Para producción, usa variables de entorno.

ENGLISH
Web application for managing fitness center clients using Flask and SQLite for local storage. Perfect for testing and development without external DB setup.
Requirements: Python 3.7+, packages in requirements.txt.
Installation:

git clone https://github.com/AndriyLavryk/CentroFitnes.git  
cd CentroFitnes  
python -m venv .venv  
# Windows  
.venv\Scripts\activate  
# Linux/macOS  
source .venv/bin/activate  
pip install -r requirements.txt  

Usage:

python app.py  

Open in browser: http://localhost:5000
Notes:

    The SQLite database file app.db is auto-created in the project root.

    To reset the DB, delete app.db and restart the app.

    SECRET_KEY is set in app.py for development. Use environment variables in production.

РУССКИЙ
Веб-приложение для управления клиентами фитнес-центра с использованием Flask и SQLite для локального хранения. Удобно для тестирования и разработки без настройки внешней базы данных.
Требования: Python 3.7+, пакеты из requirements.txt.
Установка:

git clone https://github.com/AndriyLavryk/CentroFitnes.git  
cd CentroFitnes  
python -m venv .venv  
# Windows  
.venv\Scripts\activate  
# Linux/macOS  
source .venv/bin/activate  
pip install -r requirements.txt  

Использование:

python app.py  

Откройте в браузере: http://localhost:5000
Примечания:

    Файл базы данных SQLite app.db создаётся автоматически в корне проекта.

    Для сброса базы удалите app.db и перезапустите приложение.

    SECRET_KEY прописан в app.py для разработки. Для продакшена используйте переменные окружения.