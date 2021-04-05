# BSC - Buy Sell Car
# Техническое задание

## Описание предметной области
Сервис по поиску и продаже подержанных автомобилей.

Основные сущности:
* Пользователь - человек, осуществляющий поиск или продажу автомобиля.
* Объявление - список параметров, характеризующих конкретный автомобиль.
* Администратор - доверенное лицо, обладающее правами внесения новых марок и моделей автомобилей.
* Модератор - доверенное лицо, обладающее правами принятия и отклонения новых объявлений.

## Функциональные требования
### Сценарии покупателя

**Регистрация**

* Пользователь заполняет форму регистрации: электронная почта, имя, фамилия, страна, город, пароль, подтверждение пароля
> e-mail пользователя не верифицируется
* Пользователь нажимает кнопку "Зарегистрироваться"
* Пользователь получает подтверждение об успешной регистрации и попадает в личный кабинет пользователя

**Авторизация**

* Пользователь заполняет форму авторизации (электронная почта, пароль)
* Пользователь нажимает кнопку "Войти"
* Пользователь попадает в личный кабинет пользователя

**Редактирование профиля**

* Пользователь переходит в личный кабинет пользователя
* Пользователь нажимает на кнопку редактировать профиль
* Пользователь заполняет форму редактирования профиля (имя, фамилия, электронная почта, страна, город)
* Пользователь нажимает кнопку "Сохранить"
* Пользователь получает подтверждение об успешном изменении профиля

**Добавление объявления в избранные**
* Пользовтель открывает интересующее его объявление
* Пользователь нажимает на кнопку "Добавить в избранное"
* Пользователь получает уведомление о добавлении объявления в список избранных

**Удаление объявления из избранных**
* Пользователь переходит в личный кабинет пользователя
* Пользователь нажимает на кнопку "Избранные объявления"
* Пользователь нажимает на кнопку "Удалить из избранного" рядом с определенным объявлением в данном списке
* Пользователь получает уведомление об удалении объявления из списка избранных

**Осуществление звонка по объявлению**
* Пользователь открывает интересующее его объявление
* Пользователь нажимает на номер телефона продавца
> Активная ссылка телефона. Данный протокол tel поддерживается не всеми браузерами!
* Пользователь переходит в приложение для звонков по умолчанию с введеным номером телефона

### Сценарии продавца
**Регистрация**

* Пользователь заполняет форму регистрации: электронная почта, имя, фамилия, страна, город, пароль, подтверждение пароля
> e-mail пользователя не верифицируется
* Пользователь нажимает кнопку "Зарегистрироваться"
* Пользователь получает подтверждение об успешной регистрации и попадает в личный кабинет пользователя

**Авторизация**

* Пользователь заполняет форму авторизации (электронная почта, пароль)
* Пользователь нажимает кнопку "Войти"
* Пользователь попадает в личный кабинет пользователя

**Публикация объявления**

* Пользователь нажимает на кнопку "Подать объявление"
* Пользователь заполняет форму, содержащую параметры продаваемого автомобиля
* Пользователь нажимает на кнопку "Опубликовать"
* Пользотель получает уведомление об успешной публикации объявления

**Изменение статуса объявления**

* Пользователь переходит в личный кабинет пользователя
* Пользователь переходит в список активных объявлений
* Пользователь нажимает кнопку снять объявление с публикации рядом с определенным объявлением в данном списке

# Технологический стек
## Backend
* Python 3.8.6
* Django 3.1.7
* Django Rest Framework
* sqlite
## Frontend
* Vue.js
* HTML5
* CSS
* SASS/SCSS
## Система контроля версий
* git

# Системные требования
## Серверная часть
* ОС: Linux Ubuntu 20.10
* RAM: 4 Gb
* CPU: Intel Core i3-8xxx/AMD Ryzen 3 1400
* HDD/SSD: 20 Gb

## Клиентская часть
* Browser: Google Chrome 80+

# Состав команды

<table>
<tr>
<td>

<img src="https://portfolio.bmstu.ru/uploads/portfolio/276fa002-5f0b-11e7-b208-005056962143/profile_1555950051.jpg" alt="Amiyan E. A." height="200"/>

</td>
<td>

<img src="https://scontent-waw1-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/p640x640/131702156_384226715975534_3167088004480947849_n.jpg?tp=1&_nc_ht=scontent-waw1-1.cdninstagram.com&_nc_cat=102&_nc_ohc=glDx19t7N_UAX8_MFQ_&ccb=7-4&oh=eabb86e78e09fe82941e40874a2139c5&oe=608ADEE8&_nc_sid=4f375e" alt="Shestakov A. R." height="200"/>

</td>
<tr>
<td>
<b>Амиян Эдгар Геннадиевич</b>
<div>Frontend-разработчик</div>
<div>Telegram: <a href="https://t.me/ed_amiyan">@ed_amiyan</a></div>
<div>e-mail: <a>ed.amiyan@ya.ru</a></div>
</td>
<td>
<b>Шестаков Андрей Романович</b>
<div>Backend-разработчик</div>
<div>Telegram: <a href="https://t.me/shestakovar">@shestakovar</a></div>
<div>e-mail: <a>shestakovar@ya.ru</a></div>
</td>
</table>

# Таблица рисков

### Риск 1

| Свойство       | Описание                             |
| ---------------|--------------------------------------|
| Приоритет      | 1                                    |
| Риск           | Нехватка времени из-за учебной и рабочей нагрузки|
| Состояние      | Анализ                               |  
| Вероятность    | Высокая                              |  
| Урон           | Высокий                              | 
| Воздействие    | Высокое                              | 
| Тип стратегии  | Принятие                             | 
| Стратегия      | Сокращение покрытия тестами, не реализуем добавление объявлений в избранные| 
| Ответственный  | Все  |

### Риск 2

| Свойство       | Описание                             |
| ---------------|--------------------------------------|
| Приоритет      | 2                                    |
| Риск           | Болезнь участника команды            |
| Состояние      | Анализ                               |  
| Вероятность    | Средняя                              |  
| Урон           | Высокий                              | 
| Воздействие    | Высокое                              | 
| Тип стратегии  | Принятие                             | 
| Стратегия      | Другой участник берет на себя работу заболевшего| 
| Ответственный  | Все  |

### Риск 3

| Свойство       | Описание                             |
| ---------------|--------------------------------------|
| Приоритет      | 3                                    |
| Риск           | Взаимодействие с новыми технологиями|
| Состояние      | Анализ                               |  
| Вероятность    | Средняя                              |  
| Урон           | Средний                              | 
| Воздействие    | Среднее                              | 
| Тип стратегии  | Снижение                             | 
| Стратегия      | Обращение к интернет-ресурсам и профессиональной литературе| 
| Ответственный  | Все  | 

