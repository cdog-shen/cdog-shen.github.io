# solder and gun

class solder:
    """士兵类"""

    def __init__(self,name):
        """姓名, 枪支,"""
        self.name = name
        print("生成了%s" %(self.name))

    def equip(self,own):
        """装备"""
        self.own = own
        print("%s装备%s" %(self.name,self.own))

    def fire(self,time):
        """开火 time-->射击次数"""
        for i in range(1,time + 1):
            self.own.shoot()

    def reload(self):
        """装填"""
        print("Reloading!")
        self.own.bullets = self.own.max_b


class gun:
    """枪类"""

    def __init__(self,name,max_b,sound,bullets=0):
        """型号, 声音, 满载子弹数, 实时子弹数量"""
        self.name = name
        self.max_b = max_b
        self.sound = sound
        self.bullets = bullets

    def shoot(self):
        """射击"""
        self.count()

    def count(self):
        """弹药管理"""
        if self.bullets <= 0:
            print("ka...")
        else:
            self.bullets -= 1
            print(self.sound)

    def __str__(self):
        return "%s" %self.name


old_6 = solder("老六")
r8 = gun("R8",8,"bang~")

old_6.equip(r8)

old_6.reload()
old_6.fire(6)
old_6.fire(3)
