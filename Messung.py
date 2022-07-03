# Code Writing by Mohamed Amine Guedria
# Guedria.amine@gmail.com
# This code give out the frequency and Effective Voltage (Vrms) reading from a microphone amplifier and a .wav-file
# All informations will be saved in Excel table
# Überarbeitung Bernhard Lau -01

# ------- All needed Modules -------- #
from tkinter import * # Graphical user interface (GUI)
from tkinter import messagebox # GUI
import matplotlib.pyplot as plt
import pyaudio
import numpy as np
import wave
from serial import SerialException
from Ver import AR
# Verstärkungseinstellung Spannungsteiler
from rms import voltage
from Excel import Datei
import math as m

import pygame
import matplotlib.backends.backend_tkagg
from matplotlib.figure import Figure

# ------- Lists ------- #
logliste=[]
liste = []  # frequency list to fill
wavliste = []  # frequency list for the .wav-file to fill
Peaklist = []  # peak list to fill
Mpeaklist = []  # .wav peak list to fill
Wv = []  # .wav Effective Voltage (Vrms) list to fill
v = []  # Effective Voltage(Vrms) list  to fill
frqlist = ["16", "20", "25", "31", "40", "50", "63", "80", "100", "125", "160", "200", "250",\
           "315", "400", "500", "630", "800", "1000", "1250", "1600", "2000", "2500", "3150", "4000"]
buchstaben = ["A_", "B_", "C_", "D_", "E_", "F_", "G_", "H_", "I_", "J_", "K_", "L_", "M_",\
           "N_", "O_", "P_", "Q_", "R_", "S_", "T_", "U_", "V_", "W_", "X_", "Y_"]
# frequency list, Messfrequenzen gemäß der akustische Terzfolge

run = False
pause = False
text = ""
counter1=0
counter2=0
i=0
control=0


# ------- Pygame Init ------- #
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
pygame.mixer.init()

# ------- a method to detect and calculate the Frequency and the Effective Voltage (Vrms) from the microphone amplifier -------- #
def detecting():
    global i
    global control
    global counter2
    global counter1


    chunk = 2048  # is the number of frames in the buffer.
    RATE = 44100  # rate is the number of samples of audio carried per second
    p = pyaudio.PyAudio()
    stream1 = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                     frames_per_buffer=chunk)  # bits pro Sekunde=Samplerate*Samplebreite*Kanäle

    if run:  # Run the program if start Button pushed

        data = stream1.read(chunk)  # read the informations from microphone
        indata = np.fromstring(stream1.read(chunk),
                               dtype=np.int16)  # 1-D array initialized from raw binary data in a string

        fftData = abs(np.fft.rfft(indata)) ** 2  # Take the fft and square each value

        which = fftData[1:].argmax() + 1  # find the maximum

        peak = np.average(np.abs(indata))  # find the average
        a = voltage.get_rms(data)
        bars = "#" * int(100 * a / 0.1)
        grenze = " " * (int(100 * 0.1 / 0.1) - int(100 * a / 0.1))

        if which != len(fftData) - 1:
            # find the frequency and output it
            y0, y1, y2 = np.log(fftData[which - 1:which + 2:])
            x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
            thefreq = (which + x1) * RATE / chunk
            a=voltage.get_rms(data)
            thevolt=m.log10(a)

           # print("%.2fHz /%05d/ %.4fV / %s" % (thefreq, peak,m.log10(thevolt),bars))
            print("%f V /%f LOG %5d Hz / %06d [%s %s]" % (a, thevolt, thefreq, peak, bars, grenze))

            output.insert(0.0,"%.2fHz / %.4fV " % (thefreq,a))  # output in the GUI Window
            liste.append(thefreq)  # fill the list
            Mpeaklist.append(peak)  # fill the list
            wavfile()  # call the method for the .wav-file
            v.append(voltage.get_rms(data))  # fill the list


            makeFig()

            if (var_CB.get() == 1):
                if control == i:
                    if counter1 > 4 or counter2 > 4:
                        "Sie Haben pegelstufe 5 erreicht!!!!!"
                        pass
                    else:

                        if var_chek2.get() == 5:
                            counter1 += 1
                        elif var_chek2.get() == 6:
                            counter2 += 1

                        AR.autoVer(counter1, counter2, v, var_chek2.get())

                        control += 5
                i += 1


        else:
            thefreq = which * RATE / chunk
            print("%f Hz  %05d %s" % (thefreq, peak, bars))
            liste.append(thefreq)
            Mpeaklist.append(peak)
            wavfile()
            print("Vrms", voltage.get_rms(data))

    stream1.stop_stream()
    stream1.close()
    p.terminate()



    root.after(1, detecting)  # a callback function that will be called after a 1 ms
# ---------------------------------------------------------------------------------------- Ende detecting


# -------- a method to detect and calculate the Frequency and the Effective Voltage(Vrms) from .wav-file -------- # 
def wavfile():
    chunk = 2048
    if selection() == '':
        s="sweep_20Hz_3500Hz_0dBFS_5s.wav"
    else:
        s = "sin_" + selection() + "Hz_0dBFS_5s.wav"  # name of the wave file
    wf = wave.open(s, 'rb')  # open the wav.file
    swidth = wf.getsampwidth()  # get the samp width
    RATE = wf.getframerate()  # get the frame rate
    # use a Blackman window"     sweep_20Hz_3500Hz_0dBFS_5s.wav"
    window = np.blackman(chunk)
    # open stream
    p = pyaudio.PyAudio()
    data = wf.readframes(chunk)  # read the informations from .wav file

    # unpack the data and times by the hamming window
    indata = np.array(wave.struct.unpack("%dh" % (len(data) / swidth), \
 \
                                         data)) * window

    # Take the fft and square each value
    fftData = abs(np.fft.rfft(indata)) ** 2
    # find the maximum
    which = fftData[1:].argmax() + 1

    if which != len(fftData) - 1:
        y0, y1, y2 = np.log(fftData[which - 1:which + 2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which + x1) * RATE / chunk
        peak = np.max(np.abs(indata))
        wavliste.append(thefreq)
        Peaklist.append(peak)
        Wv.append(voltage.get_rms(data))

    else:
        thefreq = which * RATE / chunk
        peak = np.max(np.abs(indata))
        Peaklist.append(peak)
        wavliste.append(thefreq)

    p.terminate()
# ---------------------------------------------------------------------------------------- Ende wavfile


# -------- GUI Methoden --------#


def makeFig():
    new_list = v[1:]


    fig = Figure(figsize=(7, 7), dpi=100)

    a1 = fig.add_subplot(221)
    a2 = fig.add_subplot((222))
    a3 = fig.add_subplot((212))



    if selection() =='':
        plt.ion()


        a1.set_ylabel('Amplitude [Hz]')
        a1.set_title('Frequency')
        a1.plot(liste, 'ro-')
        a1.grid()


        a2.set_xlabel('Time')
        a2.set_ylabel('Amplitude [V]')
        a2.set_title('Effective volt')
        a2.plot(v, 'bo-')
        a2.grid()


        a3.set_xlabel('Frequency')
        a3.set_ylabel('Amplitude [V]')
        a3.plot(liste, new_list, 'go-')
        a3.grid()




        #fig.tight_layout()
        fig.set_tight_layout(True)

        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().place(x=370, y=10)




    else:
        plt.ion()

        fig = Figure(figsize=(7, 7), dpi=100)

        a5 = fig.add_subplot(211)
        a5.set_ylabel('Amplitude [Hz]')
        a5.set_title('Frequency')
        a5.plot(liste, 'ro-')
        a5.grid()

        a4 = fig.add_subplot(212)
        a4.set_xlabel('Time')
        a4.set_ylabel('Amplitude [V]')
        a4.set_title('Effective volt')
        #a4.set_ylim(0,0.1)
        a4.autoscale(True)
        a4.plot(new_list, 'bo-')
        a4.grid()






        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().place(x=370, y=10)





def choose_Re():
    global run
    global pause
    global  counter1
    global  counter2

    if var_CB.get() == 0:  # control of automatic or not
        if var_chek1.get() == 0:  # if not automatic control if a resistance selected
            output.delete(1.0, END)
            output.insert(1.0, "Signalpegel wählen")  # output message out in window of GUI
            messagebox.showerror("Signalpegel wählen", "Sie haben keinen Signalpegel gewählt!")  # error message window
        elif var_chek2.get() == 0:  # if not automatic control if the type of sound selected
            output.delete(1.0, END)
            output.insert(1.0, "Lautsprecher wählen")  # output message in window of GUI
            messagebox.showerror("Lautsprecher wählen ", "Sie haben keinen Lautsprecher gewählt!")  # error message window
        else:
            AR.manuVerstarken(var_chek1.get(), var_chek2.get())  # call the Method manuVerstarken from the module 'Ver'
#           Parameter: Pegelstufe (Widerstand), Lautsprecher; siehe "Arduino-Protokoll.xlsx"
            run = True
    elif (selection() != ''):  # control if frequency selected

        f = int(selection())  # save the value of the Method selection in f
        AR.autoVer(counter1, counter1, v, var_chek2.get())
        run = True
        pause = False
# ---------------------------------------------------------------------------------------- Ende choose


def start():  # Start the program
    try:
        if var_chek3.get() == 0:  # check if kind of test selected
            messagebox.showerror("Welche Art Messung?",
                             "Welche Art Messung? (Mikrofon, Stethoskop oder Box?)")  # error message window
        else:
            if selection() == '':
                output.insert(1.0, "Frequenz wählen")  # output message in window of GUI
                messagebox.showerror("Frequenz wählen", "Sie haben keine Frequenz gewählt!")  # error message window
            else:
                choose_Re()  # call the method
                wert = selection()
                select = int(wert)  # string to integer
                v.append(select)
                pygame.mixer.music.load("sin_" + selection() + "Hz_0dBFS_5s.wav")
                pygame.mixer.music.play(-1)

    except SerialException as e :
        print("Fehler",e)
        output.insert(1.0, e)
        messagebox.showerror("Ardiuno Port COM3", "Port COM3 is not connected!")
# ---------------------------------------------------------------------------------------- Ende start


def ppause():  # pause to select the next frequency
    global run
    global pause

    pause = True
    run = False
    output.delete(1.0, END)
    output.insert(1.0, "Pause\n")  # output message in window of GUI
    liste.append(0000)
    wavliste.append(0000)
    v.append(0000)
    pygame.mixer.music.stop()
# ---------------------------------------------------------------------------------------- Ende ppause


def stop():  # Stop the program
    global run
    global pause
    global  counter2
    global  counter1
    counter2=0
    counter1=0
    pause = False
    run = False
    # call the Method excel3 from the module 'Excel'
#    Datei.excel3(frqlist, v, selection(), var_chek3.get())
    # call the Method excel1 from the module 'Excel'
  #  Datei.excel1(liste, wavliste, frqlist)
    # call the Method excel2 from the module 'Excel'
 #   Datei.excel2(Wv, v, 0)

    output.delete(1.0, END)
    output.insert(1.0, "------Stop-----")
    print("-----stop-----")
    pygame.mixer.music.stop()
# ---------------------------------------------------------------------------------------- Ende stop


def selection():  # get the selected frequency
    s =''
    a = listbox.curselection()
    for i in a:
        s = listbox.get(i)

    return (s)
# ---------------------------------------------------------------------------------------- Ende selection


def Check_Automatic():  # disable or enable the radiobutton "Signalpegel" it depends on the checkbox "Signalpegel automatisch anpassen"
    if (var_CB.get() == 1):	
        radA.configure(state=DISABLED)
        radB.configure(state=DISABLED)
        radC.configure(state=DISABLED)
        radD.configure(state=DISABLED)
        radhoch.config(state=NORMAL)
        radtief.config(state=NORMAL)
        radohne.config(state=DISABLED)
        var_chek1.set(0)
        var_chek2.set(0)
        output.delete(1.0, END)

    elif (var_CB.get() == 0):
        radA.configure(state=NORMAL)
        radB.configure(state=NORMAL)
        radC.configure(state=NORMAL)
        radD.configure(state=NORMAL)
        radhoch.config(state=NORMAL)
        radtief.config(state=NORMAL)
        radohne.config(state=NORMAL)
# ------------------------------------------------------------------------------ Ende Check_Automatic
def sweep_on():
    global run

    run=True
    AR.leise(AR)
    radA.configure(state=DISABLED)
    radB.configure(state=DISABLED)
    radC.configure(state=DISABLED)
    radD.configure(state=DISABLED)
    radhoch.config(state=NORMAL)
    radtief.config(state=NORMAL)
    radohne.config(state=DISABLED)
    listbox.config(state=DISABLED)
    var_chek1.set(0)
    var_chek2.set(0)
    output.delete(1.0, END)


    pygame.mixer.music.load("sweep_20Hz_3500Hz_0dBFS_5s.wav")
    pygame.mixer.music.play(-1)
def sweep_off():

    global run

    run=False

    radA.configure(state=NORMAL)
    radB.configure(state=NORMAL)
    radC.configure(state=NORMAL)
    radD.configure(state=NORMAL)
    radhoch.config(state=NORMAL)
    radtief.config(state=NORMAL)
    radohne.config(state=NORMAL)
    listbox.config(state=NORMAL)
    pygame.mixer.music.stop()

# ---------------------------------------------------------------------------------------- Ende sweep

# --------------- GUI -------------- #

# make a window
root = Tk()
root.geometry("1120x800")
root.title("MENU")
app = Frame(root)
app.grid()


# --------------- Buttons --------------#
start = Button(app, text="Start", bg="green", fg="black", command=start)
stop = Button(app, text="Stop", bg="red", fg="white", command=stop)
Bpause = Button(app, text="Pause", bg="blue", fg="yellow", command=ppause)
Sweepon = Button(app, text="Play Sweep", bg="grey70", command=sweep_on)
Sweepoff = Button(app, text="Stop Sweep", bg="grey60", command=sweep_off)


start.grid(row=0, column=0)
stop.grid(row=0, column=2)
Bpause.grid(row=0, column=3)
Sweepon.place(x=140,y=0)
Sweepoff.place(x=210, y=0)

# --------------- RadioButtons --------------#
var_chek1 = IntVar()
var_chek2 = IntVar()
var_chek3 = IntVar()
var_chek3.set(0)
radA = Radiobutton(root, text=" Pegel Stufe 4", variable=var_chek1, value=1)
radB = Radiobutton(root, text=" Pegel Stufe 3", variable=var_chek1, value=2)
radC = Radiobutton(root, text=" Pegel Stufe 2", variable=var_chek1, value=3)
radD = Radiobutton(root, text=" Pegel Stufe 1", variable=var_chek1, value=4)

radtief = Radiobutton(root, text="Tieftöner (bis 80 Hz)", bg="white", variable=var_chek2, value=5)
radhoch = Radiobutton(root, text="Hochtöner (ab 100 Hz) ", bg="red", variable=var_chek2, value=6)
radohne = Radiobutton(root, text=" Pegel Stufe 5", variable=var_chek1, value=7)

radmicro = Radiobutton(root, text='Mikofon     ', variable=var_chek3, bg='yellow', value=1)
radstatho = Radiobutton(root, text='Stethoskop', variable=var_chek3, bg='gold', value=2)
radiobox = Radiobutton(root, text='Box            ', variable=var_chek3, bg='dark goldenrod', value=3)

# position
radohne.place(x=125, y=140)
radA.place(x=250, y=110)
radB.place(x=125, y=110)
radC.place(x=250, y=80)
radD.place(x=125, y=80)
radhoch.place(x=125, y=205)
radtief.place(x=125, y=175)

radmicro.place(x=150, y=240)
radstatho.place(x=150, y=270)
radiobox.place(x=150, y=300)

# --------------- ListBoxes --------------#
listbox = Listbox(root, bg="black", fg="yellow")
listbox.place(x=10, y=80, width=22, height=535)
listbox.insert(END)
# fill the listbox
for item in buchstaben:
    listbox.insert(END, item)
listbox = Listbox(root, bg="black", fg="white")
listbox.place(x=28, y=80, width=60, height=535)
listbox.insert(END)
label = Label(root, text="Frequenzen / Hz")
label.place(x=5, y=50)
# fill the listbox
for item in frqlist:
    listbox.insert(END, item)

# -------------- CheckBox ---------------#
var_CB = IntVar(value=0)
checkB = Checkbutton(app, variable=var_CB, text=" Signalpegel automatisch anpassen", onvalue=1, offvalue=0, command=Check_Automatic)
checkB.grid(row=4, column=4)


# ------------- Text_Field ----------------#
output = Text(root,
              height=20,
              width=30,
              relief=GROOVE,
              background='black',
              foreground='white')
output.place(x=100, y=340)

output.insert(1.0, "Programms gestartet,\nbeide Lautsprecher\nauf Pegelstufe 1")
#AR.leise(AR)



#----------------Live_Graph--------#

fig = Figure(figsize=(7, 7), dpi=100)
a = fig.add_subplot(211)
a.grid()
a.set_ylabel('Amplitude [Hz]')
a.set_title('Frequency')


a=fig.add_subplot((212))
a.grid()
a.set_xlabel('Time')
a.set_ylabel('Amplitude [V]')
a.set_title('Effective volt')

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)

#canvas.get_tk_widget().place(x=370, y=10)
#c=Canvas(root,height=50,width=100,bg="black")
#arcc=c.create_arc(10,50,140,210,extent=359,fill="red")
#c.place(x=370, y=10)

# ---------------------------------------------------------------------------------------- Ende GUI


##### ---------------Main--------------#####

detecting()


app.mainloop()  # main loop


# ------------------------------------------------------------------------------------ Ende Main
