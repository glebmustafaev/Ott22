class User:
    def __init__(self,nickname: str,hashpass: int,age: int):
        self.nickname = nickname
        self.password = hashpass
        self.age = age
class Video:
    def __init__(self,title: str,duration: int,time_now,adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
class UrTube:
    def __init__(self,users,videos,current_user):
        self.users = []
        self.videos = []
        self.current_user = None
    def log_in(self,nickname: str,password: str):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
    def register(self,nickname: str, password: str, age: int):
        hashpass = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
            else: self.users.append(nickname)
    def log_out(self):
        self.current_user = None
    def add(self,*args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)
    def get_videos(self,word: str):
        list.videoS = []
        for video in self.videos:
            if word.lower() in 
