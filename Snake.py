import random
import time
import mido

colours = [3, 77, 58, 56, 52, 49, 80, 22, 72, 45, 66]

class Snake:
    start_pos =         0
    speed =             0
    colour =            0
    snake_length =      4
    width =             9
    height =            9
    port = 0
    
    def __init__(self, port):
        self.start_pos = 10+random.randint(1, 9)
        self.speed = random.randint(1, 1000)
        self.colour = random.choice(colours)
        self.snake_length = random.randint(1,8)
        self.port = port
        
    
    # def __init__(self, start_pos, speed, colour) -> None:
    #     self.start_pos = start_pos
    #     self.speed = speed
    #     self.colour = colour
    
    def makeSnake(self):
        print("snake_length:", self.snake_length)
        for i in range(self.height + self.snake_length):
            noteon = self.start_pos+(i*10)
            if (i <= self.height):
                msg = mido.Message('note_on', note = noteon, velocity = self.colour)
                self.port.send(msg)
            note_off = self.start_pos + ((i-(self.snake_length))*10)
            if (i >= self.snake_length):
                msg_off = mido.Message('note_off', note = note_off)
                self.port.send(msg_off)
            time.sleep(self.speed/1000.0)
        return 0

class Explosion:
    width = 9
    height = 9
    colour = 0
    
    def __init__(self,port) -> None:
        self.port = port
        self.colour = random.choice(colours)
    
    def makeExplosion(self):
        center = int((((self.width+1)/2)*10)+(self.height+1)/2)
        self.colour = random.choice(colours)
        msg = mido.Message('note_on', note=center, velocity=self.colour)
        self.port.send(msg)
        for t in range(5):
            for x in range(9):
                for y in range(9):
                    print("x",x,"x-5:",abs(x-5),"t:",t)
                    if abs(x - 4) == t or abs(y - 4) == t:
                        print("ye")
                        note = ((x+1)*10) + (y+1)
                        msg = mido.Message('note_on',note= note, velocity=self.colour)
                        self.port.send(msg)
            time.sleep(0.1)
            self.all_off()            
        # time.sleep()
        msg_off = mido.Message('note_off', note=center)
        self.port.send(msg_off)
    
    def evens(self, ms):
        
        self.colour = random.choice(colours)
        for i in range(self.width):
            for j in range(self.height):
                if (i+j)%2 is 0:
                    note = ((i+1)*10)+j+1
                    msg = mido.Message('note_on', note = note, velocity = self.colour)
                    port.send(msg)
                    time.sleep(0.005)
        time.sleep(ms)
        
    def threevens(self, factor, ms):
        
        self.colour = random.choice(colours)
        for i in range(self.width):
            for j in range(self.height):
                if (i+j)%factor is 0:
                    note = ((i+1)*10)+j+1
                    msg = mido.Message('note_on', note = note, velocity = self.colour)
                    port.send(msg)
                time.sleep(0.005)
        time.sleep(ms)


    def odds(self, ms):
        self.colour = random.choice(colours)
        for i in range(self.width):
            for j in range(self.height):
                if (i+j)%2 == 1:
                    note = ((i+1)*10)+j+1
                    msg = mido.Message('note_on', note = note, velocity = self.colour)
                    port.send(msg)
                    time.sleep(0.005)
        time.sleep(ms)
                
    def evens_and_off(self):
        self.colour = random.choice(colours)
        for i in range(self.width):
            for j in range(self.height):
                if (i+j)%2 is 0:
                    note = ((i+1)*10)+j+1
                    msg = mido.Message('note_on', note = note, velocity = self.colour)
                    port.send(msg)
                    time.sleep(0.005)
        time.sleep(1)
        for i in range(self.width):
            for j in range(self.height):
                note = ((i+1)*10)+j+1
                msg_off = mido.Message('note_off', note = note)
                port.send(msg_off)
                time.sleep(0.005)


    def odds_and_off(self):
        self.colour = random.choice(colours)
        for i in range(self.width):
            for j in range(self.height):
                if (i+j)%2 == 1:
                    note = ((i+1)*10)+j+1
                    msg = mido.Message('note_on', note = note, velocity = self.colour)
                    port.send(msg)
                    time.sleep(0.005)
        time.sleep(1)
        for i in range(self.width):
            for j in range(self.height):
                note = ((i+1)*10)+j+1
                msg_off = mido.Message('note_off', note = note)
                port.send(msg_off)
                time.sleep(0.005)
    
    
                
    def all_off(self):
        for i in range(self.width):
            for j in range(self.height):
                note = ((i+1)*10)+j+1
                msg_off = mido.Message('note_off', note = note)
                port.send(msg_off)

if __name__ == "__main__":
    # port = mido.open_output('Launchpad Mini MK3 LPMiniMK3 MIDI In')
    port = mido.open_output('to Max 1')
    print(mido.get_output_names())
    
    snake1 = Snake(port)
    expl = Explosion(port)
    snake1.makeSnake()
    # expl.makeExplosion()
    for i in range(18):
        expl.evens(0)
        # expl.odds(0)
        # expl.threevens(8, 0)
        # expl.makeExplosion()
        # pass
    expl.all_off()