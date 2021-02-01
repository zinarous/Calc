import pygame,math
pygame.init()

window_height = 500
window_width = 500
window  = pygame.display.set_mode((window_height,window_width))

font = pygame.font.SysFont('comicsans', 60)

    # the buttons for the shop MENU
class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.over = False
        self.image = font.render(self.text, 1, (0,0,0))

    def draw(self,window,outline=None):
                #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(window, outline, (self.x-2,self.y-4,self.width+4,self.height+8),0)
                    
        pygame.draw.rect(window, self.color, (self.x,self.y-2,self.width,self.height+4),0)
                
        if self.text != '':
            w, h = self.image.get_size()
            window.blit(self.image, (self.x + (self.width//2 - w//2), self.y + (self.height//2 - h//2 + 2)))

    def isOver(self, pos):
                #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
                    
        return False

    def playSoundIfMouseIsOver(self, pos, sound):
        if self.isOver(pos):            
            if not self.over:
                beepsound.play()
                self.over = True
        else:
            self.over = False

class Calculate:
    def __init__(self):
        self.currentValue = 0
        self.newNumber = 0
        self.currentOperation = None
        self.currentText = ""
    def newDigit(self, text):
        self.newNumber = self.newNumber * 10 + int(text) 
        self.currentText = str(self.newNumber)
    def newOperation(self, op):
        try:
            if self.currentOperation == '+':
                self.currentValue += self.newNumber
            elif self.currentOperation == '-':
                self.currentValue -= self.newNumber
            elif self.currentOperation == 'x':
                self.currentValue *= self.newNumber
            elif self.currentOperation == '÷':
                self.currentValue /= self.newNumber
            elif self.currentOperation != "=":
                self.currentValue = self.newNumber
        except:
            self.currentValue = 0
        self.currentOperation = op
        self.currentText = str(self.currentValue)
        self.newNumber = 0

calculator = Calculate()
        
                    
white = (255,255,255)
# the numbers for the calcaltor
s_1s = Button((0,255,0),40,450,30,30, '1')
s_2s = Button((0,255,0),40,400,30,30, '2')
s_3s = Button((0,255,0),40,350,30,30, '3')
s_4s = Button((0,255,0),100,450,30,30, '4')
s_5s = Button((0,255,0),100,400,30,30, '5')
s_6s = Button((0,255,0),100,350,30,30, '6')
s_7s = Button((0,255,0),150,450,30,30, '7')
s_8s = Button((0,255,0),150,400,30,30, '8')
s_9s = Button((0,255,0),150,350,30,30, '9')
s_0s = Button((0,255,0),200,450,30,30, '0')

numbers = [s_1s,s_2s,s_3s,s_4s,s_5s,s_6s,s_7s,s_8s,s_9s,s_0s]

# the symbols!
d_1s = Button((0,255,0),260,450,30,30, '+')
d_2s = Button((0,255,0),260,400,30,30, '-')
d_3s = Button((0,255,0),260,350,30,30, 'x')
d_4s = Button((0,255,0),200,400,30,30, '÷')
d_5s = Button((0,255,0),320,450,30,30, '=')

symbols = [d_1s,d_2s,d_3s,d_4s,d_5s]

clearButton = Button((0,255,0),200,350,30,30, 'C')

allButtons = numbers + symbols + [clearButton]

# input tap
inputtap = Button((253,100,32),10,280,450,50,"")

# redraw window
def redraw():
    for button in allButtons:
        button.draw(window)

    inputtap.draw(window)
    inputtext = font.render(calculator.currentText, True, (0, 0, 0))
    window.blit(inputtext, (inputtap.x + inputtap.width - inputtext.get_width() - 4, inputtap.y + 4))
 
def Symbols():  
    global calculator
    if event.type == pygame.MOUSEBUTTONDOWN:
        for button in symbols:
            if button.isOver(event.pos):
                print(button.text)
                calculator.newOperation(button.text)
        if clearButton.isOver(event.pos):
            calculator = Calculate()
    
def MOUSEOVERnumbers():
    if event.type == pygame.MOUSEBUTTONDOWN:
        for button in numbers:
            if button.isOver(event.pos):
                print(button.text)  
                calculator.newDigit(button.text)

# the main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        MOUSEOVERnumbers()
        Symbols()

    redraw()
    pygame.display.update()
pygmae.quit()