BOT_TOKEN: str = "NzE2NzM5OTM2NjQ4Mjk4NDk5.G5q85y.DktsADCXlIqNGHN9GdbJLYTvZPzUOA4tAu4tV8"
SPOTIFY_ID: str = ""
SPOTIFY_SECRET: str = ""

BOT_PREFIX = "!"

EMBED_COLOR = 0x4dd4d0  #replace after'0x' with desired hex code ex. '#ff0188' >> '0xff0188'

SUPPORTED_EXTENSIONS = ('.webm', '.mp4', '.mp3', '.avi', '.wav', '.m4v', '.ogg', '.mov')

MAX_SONG_PRELOAD = 25  #maximum of 25

COOKIE_PATH = "/config/cookies/cookies.txt"

GLOBAL_DISABLE_AUTOJOIN_VC = False

VC_TIMEOUT = 600 #seconds
VC_TIMOUT_DEFAULT = True  #default template setting for VC timeout true= yes, timeout false= no timeout
ALLOW_VC_TIMEOUT_EDIT = True  #allow or disallow editing the vc_timeout guild setting


STARTUP_MESSAGE = "Mkupsov_Sound_Bot -> Запуск"
STARTUP_COMPLETE_MESSAGE = "Mkupsov_Sound_Bot -> Запущен"

NO_GUILD_MESSAGE = 'Ошибка: Пожалуйста, подключитесь к голосовому каналу или введите команду в основном чате'
USER_NOT_IN_VC_MESSAGE = "Ошибка: Пожалуйста, подключитесь к активному голосовому каналу для использования команд"
WRONG_CHANNEL_MESSAGE = "Ошибка: Пожалуйста, используйте командный канал"
NOT_CONNECTED_MESSAGE = "Ошибка: Бот не подключен к голосовому каналу"
ALREADY_CONNECTED_MESSAGE = "Ошибка: Бот уже подключен к голосовому каналу"
CHANNEL_NOT_FOUND_MESSAGE = "Ошибка: Не удалось найти канал"
DEFAULT_CHANNEL_JOIN_FAILED = "Ошибка: Не удалось подключиться к основному голосовому каналу"
INVALID_INVITE_MESSAGE = "Ошибка: Недействительная ссылка на приглашение"

ADD_MESSAGE= "Чтобы добавить этого бота на свой собственный сервер, нажмите [здесь]" #brackets will be the link text

INFO_HISTORY_TITLE = "Играет песня:"
MAX_HISTORY_LENGTH = 10
MAX_TRACKNAME_HISTORY_LENGTH = 15

SONGINFO_UPLOADER = "Загрузчик: "
SONGINFO_DURATION = "Длительность: "
SONGINFO_SECONDS = "секунд"
SONGINFO_LIKES = "Лайков: "
SONGINFO_DISLIKES = "Дизлайков: "
SONGINFO_NOW_PLAYING = "Сейчас играет"
SONGINFO_QUEUE_ADDED = "Добавлено в очередь"
SONGINFO_SONGINFO = "Информация о песне"
SONGINFO_ERROR = "Информация о песне не найдена"
SONGINFO_PLAYLIST_QUEUED = "Список воспроизведения:page_with_curl:"
SONGINFO_UNKNOWN_DURATION = "Неизвестно"

HELP_ADDBOT_SHORT = "Добавить бота на другой сервер"
HELP_ADDBOT_LONG = "Дает вам ссылку для добавления этого бота на другой ваш сервер."
HELP_CONNECT_SHORT = "Подключает бота к голосовому каналу"
HELP_CONNECT_LONG = "Подключает бота к голосовому каналу, в котором вы сейчас находитесь"
HELP_DISCONNECT_SHORT = "Отключает бота от голосового канала"
HELP_DISCONNECT_LONG = "Отключает бота от голосового канала и остановливает звук."

HELP_SETTINGS_SHORT = "Просмотр и изменение настроек бота"
HELP_SETTINGS_LONG = "Просмотр и настройка настроек бота на сервере. Использование: {}settings setting_name value".format(BOT_PREFIX)

HELP_HISTORY_SHORT = "Просмотреть историю песен"
HELP_HISTORY_LONG = "Показывает " + str(MAX_TRACKNAME_HISTORY_LENGTH) + " последние воспроизведенные песни."
HELP_PAUSE_SHORT = "Останавливает музыку"
HELP_PAUSE_LONG = "Приостанавливает аудиоплеер. Воспроизведение можно продолжить с помощью команды возобновить."
HELP_VOL_SHORT = "Изменяет громкость %"
HELP_VOL_LONG = "Изменяет громкость аудиоплеера. Аргумент указывает %, на который должна быть установлена громкость."
HELP_PREV_SHORT = "Возвращает на одну песню назад"
HELP_PREV_LONG = "Снова воспроизводит предыдущую песню."
HELP_RESUME_SHORT = "Возобновляет воспроизведение музыки"
HELP_RESUME_LONG = "Возобновляет аудиоплеер."
HELP_SKIP_SHORT = "Пропускает песню"
HELP_SKIP_LONG = "Пропускает воспроизводимую в данный момент песню и переходит к следующему элементу в очереди."
HELP_SONGINFO_SHORT = "Показывает информацию о песне"
HELP_SONGINFO_LONG = "Останавливает аудиоплеер и очищает очередь песен, показывает подробную информацию о воспроизводимой в данный момент песне и публикует ссылку на песню."
HELP_STOP_SHORT = "Остановить музыку"
HELP_STOP_LONG = "Останавливает аудиопроигрыватель и очищает очередь песен"
HELP_MOVE_LONG = f"{BOT_PREFIX}move [позиция] [новая позиция]"
HELP_MOVE_SHORT = 'Перемещает треки в очереди'
HELP_YT_SHORT = "Включает поддерживаемое видео с сайта youtube.com"
HELP_YT_LONG = ("{BOT_PREFIX}p [ссылка/название видео/ключевые слова/ссылка на плейлист/ссылка на soundcloud/ссылка на spotify/ссылка на bandcamp/ссылка на twitter]")
HELP_PING_SHORT = "Пинг"
HELP_PING_LONG = "Проверить статус бота"
HELP_CLEAR_SHORT = "Очистить очередь."
HELP_CLEAR_LONG = "Очищает очередь и пропускает текущую песню."
HELP_LOOP_SHORT = "Зацикливает воспроизводимую в данный момент песню, включает / выключает."
HELP_LOOP_LONG = "Зацикливает воспроизводимую в данный момент песню и блокирует очередь. Используйте команду еще раз, чтобы отключить цикл."
HELP_QUEUE_SHORT = "Показывает песни в очереди."
HELP_QUEUE_LONG = "Показывает количество песен в очереди, до 10."
HELP_SHUFFLE_SHORT = "Перетасовать очередь"
HELP_SHUFFLE_LONG = "Произвольная сортировка песен в текущей очереди"
HELP_CHANGECHANNEL_SHORT = "Измените канал бота"
HELP_CHANGECHANNEL_LONG = "Измените канал бота в котором вы находитесь"

ABSOLUTE_PATH = '' #do not modify