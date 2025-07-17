# Antifitnes

### Команды для запуска **Docker Compose**
1. `docker compose build` - сборка контейнера  
2. `docker compose run web python manage.py makemigrations` - создание миграций для Django  
3. `docker compose run web python manage.py migrate` - применение миграций для Django  
4. `docker compose run web python manage.py createsuperuser` - создание пользователя admin панели  
5. `docker compose up` - запуск контейнера  
---
### Задачи
 - [x] аутентификация и синхронизация с CRM
 - [x] личный кабинет 
 - [x] ведение статистики и ее анализ 
 - [x] запись на тренировку 
 - [x] составление топа/рейтинга участников клуба 
-  [x] админка (рассылки) 
 - [x] тестирование всех модулей 
---
### CRM
- обработка 1754 пользователей
- добавить в модель **профиля** пункт статуса логирования в telegram (true or false)
- добавить кнопку добавления пользователя на сайте
- добавить в _/admin_ инлайн кнопку о загрузке данных в бд 
