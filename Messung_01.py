# Code Writing by Mohamed Amine Guedria
# Guedria.amine@gmail.com
# This code give out the frequency and Effective Voltage (Vrms) reading from a microphone amplifier and  a .wav-file
# All informations will be saved in Excel table
# Überarbeitung Bernhard Lau -01

# ------- All needed Modules -------- #
from tkinter import * # Graphical user interface (GUI)
from tkinter import messagebox # GUI
# import matplotlib.pyplot as plt
# import pyaudio
# import numpy as np
import wave
# from Ver import AR # Verstärkungseinstellung Spannungsteiler
from rms import voltage
# from Excel import Datei

# ------- Lists ------- #

liste = []  # frequency list to fill
wavliste = []  # frequency list for the .wav-file to fill
Peaklist = []  # peak list to fill
Mpeaklist = []  # .wav peak list to fill
Wv = []  # .wav Effective Voltage(Vrms) list to fill
v = []  # Effective Voltage(Vrms) list  to fill
frqlist = ["16", "20", "25", "31,5", "40", "50", "63", "80", "100", "125", "160", "200", "250",\
           "315", "400", "500", "630", "800", "1000", "1250", "1600", "2000", "2500", "3150", "4000"]
# frequency list, Messfrequenzen gemäß der akustische Terzfolge

run = False
pause = False
text = ""


# ------- a method to detect and calculate the Frequency and the Effective Voltage (Vrms) from the microphone -------- #
def detecting():
    chunk = 2048  # is the number of frames in the buffer.
    RATE = 44100  # rate is the number of samples of audio carried per second
#     p = pyaudio.PyAudio()
#    stream1 = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
#                     frames_per_buffer=chunk)  # bits pro Sekunde=samplrate*samplebreite*kanäle

    if run:  # Run the program if start Button pushed

        data = stream1.read(chunk)  # read the informations from microphone
        indata = np.fromstring(stream1.read(chunk),
                               dtype=np.int16)  # 1-D array initialized from raw binary data in a string

        fftData = abs(np.fft.rfft(indata)) ** 2  # Take the fft and square each value

        which = fftData[1:].argmax() + 1  # find the maximum

        peak = np.average(np.abs(indata))  # find the average
        bars = "#" * int(20 * peak / 2 ** 16)

        if which != len(fftData) - 1:
            # find the frequency and output it
            y0, y1, y2 = np.log(fftData[which - 1:which + 2:])
            x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
            thefreq = (which + x1) * RATE / chunk
            print("%f Hz %05d %s" % (thefreq, peak, bars))
            a = str(thefreq)
            text = a + " hz\n"
            output.insert(END, text)  # output in the GUI Window
            liste.append(thefreq)  # fill the list
            Mpeaklist.append(peak)  # fill the list
            wavfile()  # call the method for the .wav-file
            print("Vrms = ", voltage.get_rms(data))
            v.append(voltage.get_rms(data))  # fill the list

            plt.plot(indata[:3000])  # plot the microphone output


        else:
            thefreq = which * RATE / chunk
            print("%f Hz  %05d %s" % (thefreq, peak, bars))
            liste.append(thefreq)
            Mpeaklist.append(peak)
            wavfile()
            print("Vrms", voltage.get_rms(data))

#    stream1.stop_stream()
#    stream1.close()
#    p.terminate()

    root.after(1, detecting)  # a callback function that will be called after a 1 ms


# -------- a method to detect and calculate the Frequency and the Effective Voltage(Vrms) from .wav-file -------- # 

def wavfile():
    chunk = 2048

    s = "sin_" + selection() + "Hz_0dBFS_5s.wav"  # name of the wave file
    wf = wave.open(s, 'rb')  # open the wav.file
    swidth = wf.getsampwidth()  # get the samp width
    RATE = wf.getframerate()  # get the frame rate
    # use a Blackman window
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


# -------- GUI Methoden --------#


def choose_Re():
    global run
    global pause

    if var_CB.get() == 0:  # control of automatic or not
        if var_chek1.get() == 0:  # if not automatic control if a resistance slected
            output.delete(1.0, END)
            output.insert(1.0, "Signalpegel wählen")  # output message out in window of GUI
            messagebox.showerror("Signalpegel wählen", "Sie haben keinen Signalpegel gewählt!") # error message window
        elif var_chek2.get() == 0:  # if not automatic control if the type of sound slected
            output.delete(1.0, END)
            output.insert(1.0, "Lautsprecher wählen")  # output message in window of GUI
            messagebox.showerror("Lautsprecher wählen ", "Sie haben keinen Lautsprecher gewählt!") # error message window
        else:
            AR.manuVerstarken(var_chek1.get(), var_chek2.get())  # call the Method manuVerstarken from the module 'Ver'
            run = True
    elif (selection() != ''):  # control if frequency selected

        f = int(selection())  # save the value of the Method selection in f
        AR.autoVerstarken(f)  # call the Method autoVerstarken from the module 'Ver'
        run = True
        pause = False


def start():  # Start the program
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


def ppause():  # pause to select the next frequency
    global run
    global pause

    pause = True
    run = False
    output.delete(1.0, END)
    output.insert(1.0, "Pause")  # output message in window of GUI
    liste.append(0000)
    wavliste.append(0000)
    v.append(0000)


def stop():  # Stop the program
    global run
    global pause
    pause = False
    run = False
    # call the Method excel3 from the module 'Excel'
    Datei.excel3(frqlist, v, selection(), var_chek3.get())
    # call the Method excel1 from the module 'Excel'
    Datei.excel1(liste, wavliste, frqlist)
    # call the Method excel2 from the module 'Excel'
    Datei.excel2(Wv, v, 0)

    output.delete(1.0, END)
    output.insert(1.0, "Stop")
    print("stop")


def selection():  # get the slected frequency
    s = ''
    a = listbox.curselection()
    for i in a:
        s = listbox.get(i)

    return (s)


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


def show():  # plot the graphic
    plt.title("Ausgangssignal des Mikrofon-Verstärkers")
    plt.ylabel("Amplitude in bit")
    plt.xlabel("Zeit in ms")
    plt.grid(),
    plt.show()


# ---------------GUI--------------#
# make a window
root = Tk()
root.geometry("300x450")
root.title("MENU")
app = Frame(root)
app.grid()

# ---------------Button--------------#
start = Button(app, text="Start", bg="green", fg="black", command=start)
stop = Button(app, text="Stop", bg="red", fg="white", command=stop)
Bpause = Button(app, text="Pause", bg="blue", fg="yellow", command=ppause)
Graphik = Button(app, text="Grafik", bg="grey", command=show)

Bpause.grid(row=0, column=3)
start.grid(row=0, column=0)
stop.grid(row=0, column=2)
Graphik.grid(row=0, column=4)

# ---------------RadioButton--------------#
var_chek1 = IntVar()
var_chek2 = IntVar()
var_chek3 = IntVar()
var_chek3.set(0)
radA = Radiobutton(root, text=" Pegel Stufe 4", variable=var_chek1, value=1)
radB = Radiobutton(root, text=" Pegel Stufe 3", variable=var_chek1, value=2)
radC = Radiobutton(root, text=" Pegel Stufe 2", variable=var_chek1, value=3)
radD = Radiobutton(root, text=" Pegel Stufe 1", variable=var_chek1, value=4)

radtief = Radiobutton(root, text="Tieftöner (bis 80 Hz)", bg="white", variable=var_chek2, value=5)
radhoch = Radiobutton(root, text="Hochtöner (ab 100 Hz)", bg="red", variable=var_chek2, value=6)
radohne = Radiobutton(root, text=" Pegel Stufe 5", variable=var_chek1, value=7)

radmicro = Radiobutton(root, text='Mikofon      ', variable=var_chek3, bg='yellow', value=1)
radstatho = Radiobutton(root, text='Stethoskop', variable=var_chek3, bg='gold', value=2)
radiobox = Radiobutton(root, text='Box            ', variable=var_chek3, bg='dark goldenrod', value=3)

# postion
radohne.place(x=100, y=110)
radA.place(x=200, y=80)
radB.place(x=100, y=80)
radC.place(x=200, y=50)
radD.place(x=100, y=50)
radhoch.place(x=100, y=175)
radtief.place(x=100, y=150)

radmicro.place(x=150, y=205)
radstatho.place(x=150, y=230)
radiobox.place(x=150, y=255)

# ---------------ListBox--------------#
listbox = Listbox(root, bg="black", fg="white")
listbox.place(x=10, y=80, width=60, height=360)
listbox.insert(END)
label = Label(root, text="Frequenzen / Hz")
label.place(x=5, y=50)
# fill the listbox
for item in frqlist:
    listbox.insert(END, item)

# --------------CheckBox---------------#

var_CB = IntVar(value=0)
checkB = Checkbutton(app, variable=var_CB, text=" Signalpegel automatisch anpassen", onvalue=1, offvalue=0, command=Check_Automatic)
checkB.grid(row=2, column=4)

# -------------Text_Field----------------#

output = Text(root,
              height=9,
              width=19,
              relief=GROOVE,
              background='black',
              foreground='white')
output.place(x=100, y=300)

# ---------------Main--------------#

detecting()

app.mainloop()  # main loop
app.destroy()  # window destroy
