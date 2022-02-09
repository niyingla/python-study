class Star(object):
    def __init__(self,name,movie):
        self.name = name
        self.movie = movie
    def playing(self):
        print(f'{self.name}出演了{self.movie},非常好看')
    def __str__(self):
        return f"{self.name}是我的偶像,我非常喜欢她的电影{self.movie}"
zxc = Star('周星驰','功夫')
cl = Star('成龙','神话')
zxc.playing()
cl.playing()
print(zxc)
print(cl)


