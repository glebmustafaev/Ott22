import time


class User:
    def __init__(self, nickname: str, hashpass: int, age: int):
        self.nickname = nickname
        self.password = hashpass
        self.age = age


class Video:
    def __init__(self, title: str, duration: int, time_now, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname: str, password: str, age: int):
        hashpass = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
            else:
                self.users.append(nickname)
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, keyword):
        lkeyword = keyword.lower()
        name_videos = []
        for video in self.videos:
            if video.title.lower().find(lkeyword) != -1:
                name_videos.append(video.title)
        return name_videos

    def watch_video(self, title):

        if not self.current_user:
            print('Войдите в аккаунт чтобы смотреть видео')
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and (self.current_user.age < 18):
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return

                for time_pos in range(video.duration):
                    sleep(1)
                    video.time_now += 1
                    print(video.time_now, end=' ')

                print('Конец видео')
                video.time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

