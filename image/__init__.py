from cv2 import *
import Image
import Tkinter as tk
import threading

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.loopCondition = False
        self.quitButton=tk.Button(self, text='Quit', command=self._quit)
        self.runButton=tk.Button(self, text='Run', command=self.run)
        self.thres1Label=tk.Label(self, text='Threshold 1')
        self.threshold1=tk.Scale(self)
        self.thres2Label=tk.Label(self, text='Threshold 2')
        self.threshold2=tk.Scale(self)
        self.quitButton.grid()
        self.runButton.grid()
        self.thres1Label.grid()
        self.threshold1.grid()
        self.thres2Label.grid()
        self.threshold2.grid()        
        
    def run(self):
        self.loopCondition = True
        t=threading.Thread(target=self.loop)
        t.start()
        
    def _quit(self):
        self.loopCondition = False
        self.quit()
                
    def loop(self):
        cam = VideoCapture(0)   # 0 -> index of camera
        namedWindow("Original",CV_WINDOW_AUTOSIZE)
        namedWindow("Edge",CV_WINDOW_AUTOSIZE)
        while self.loopCondition:
            s, img = cam.read()
            thres1 = 255 * (self.threshold1.get()/float(100))
            thres2 = 255 * (self.threshold2.get()/float(100))
            if s:    # frame captured without any errors
                scaled = resize(img, (500,350))
                edged = Canny(scaled, thres1, thres2)
                imshow("Original",scaled)  
                imshow("Edge",edged) 
                waitKey(10) 
        

# initialize the camera
app = Application()
app.master.title('Image Tests')
app.mainloop()    
        
         
        