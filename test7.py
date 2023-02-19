from pydub import AudioSegment
import math
import speech_recognition as sr
import os
import pandas as pd

folder = input("Nhập đường link folder của bạn: ")
file_mp3 = input("Nhập tên file MP3: ")
file_wav = input("Nhập tên file WAV: ")

class SplitWavAudioMubin():
    def __init__(self, folder, filename_mp3, filename_wav):
        self.folder = folder
        self.filename_mp3 = filename_mp3
        self.filename_wav = filename_wav
        self.filepath = folder + '\\' + filename_mp3
        self.file_wav = folder + '\\' + filename_wav
        self.audio_mp3 = AudioSegment.from_mp3(self.filepath)
        self.audio_mp3.export(self.file_wav, format="wav")
        self.audio_wav = AudioSegment.from_wav(self.file_wav)

    def get_duration(self):
        return self.audio_wav.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 30 * 1000
        t2 = to_min * 30 * 1000
        split_audio_wav = self.audio_wav[t1:t2]
        split_audio_wav.export(self.folder + '\\' + split_filename, format="wav")
        
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 30)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename_wav
            self.single_split(i, i+min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')
    def audio_to_text(self):
        all_file = []
        all_text = []
        text = ""
        list = []
        cau_hoi1 = ""
        cau_hoi2 = ""
        cau_hoi3 = ""
        cau_hoi4 = ""
        cau_hoi5 = ""
        cau_hoi6 = ""
        ketqua = []
        dapan = []
        list_1 = []
        cau1 = []
        cau2 = []
        cau3 = []
        cau4 = []
        cau5 = []
        cau6 = []
        list_cau1 = []
        list_cau1_1 = []
        list_cau2 = []
        list_cau2_2 = []
        list_cau3 = []
        list_cau3_3 = []
        list_cau4 = []
        list_cau4_4 = []
        list_cau5 = []
        list_cau5_5 = []
        list_cau6 = []
        list_cau6_6 = []

        r = sr.Recognizer()
        # Change the directory
        os.chdir(self.folder)
        # iterate through all file
        for file in os.listdir():
            # Check whether file is in text format or not
            if file.endswith(".wav"):
                file_path = f"{self.folder}\{file}"
                # call read text file function
                all_file.append(file_path)
        del all_file[-1]

        for file in all_file:
        # open the file
            with sr.AudioFile(file) as source:
                # listen for the data (load audio to memory)
                audio_data = r.record(source)
                # recognize (convert from speech to text)
                text_1 = r.recognize_google(audio_data,language="vi")
                all_text.append(text_1)
        print(all_text)

        for item in all_text:
                text += ' ' + item   
                list = text.split()
        for i in range(len(list)):
        # cau 1 ------------------------------------------
            if list[i] =='câu' or list[i] == 'Câu': 
                a = i
                if list[a+1] == '1':
                    dau_1 = a
                    for j in range(len(list)):
                        if list[j] == '2':
                            b = j
                            if list[j-1] == 'câu'or list[j-1] == 'Câu':
                                if list[j-2]== 'ơn' or list[j-2]== 'Ơn':
                                    if list[j-3] == 'cảm' or list[j-3] == 'Cảm':
                                        ket_1 = j-1
                    list_cau1 = list[int(dau_1):int(ket_1)]
                    for i in range(len(list_cau1)):
                        if list_cau1[i] =='Trả' or list_cau1[i] =='trả': 
                            a = i
                            if list_cau1[a+1] == 'Lời' or list_cau1[a+1] == 'lời':
                                if list_cau1[a+2] =='Câu' or  list_cau1[a+2] =='câu':
                                    if  list_cau1[a+3] =='Hỏi' or  list_cau1[a+3] =='hỏi':
                                        if  list_cau1[a+4] =='Bắt' or  list_cau1[a+4] =='bắt':
                                            if  list_cau1[a+5] =='Đầu' or  list_cau1[a+5] =='đầu':
                                                dau_1 = a+6                    
                    list_cau1_1 = list_cau1[int(dau_1):int(ket_1)-8]
                    for i in list_cau1_1:
                        if i == 'A' or i == 'a':
                            cau1.append('A')
                            break
                        elif i == 'B'or i == 'b':
                            cau1.append('B')
                            break
                        elif i == 'C'or i == 'c':
                            cau1.append('C')
                            break
                        elif i == 'D'or i == 'd':
                            cau1.append('D')
                            break
                        else:
                            cau1.append(int(0))
                    for i in cau1:
                        if cau1[i] == 0:
                            cau1.remove(cau1[i])
                        if cau1[i] == 'A' or cau1[i] == 'a':
                            list_1.append('A')
                            break
                        if cau1[i] == 'B'or cau1[i] == 'b':
                            list_1.append('B')
                            break
                        if cau1[i] == 'C'or cau1[i] == 'c':
                            list_1.append('C')
                            break
                        if cau1[i] == 'D'or cau1[i] == 'd':
                            list_1.append('D')
                            break
                    if len(cau1) == 0:
                        list_1.append('0')

        # cau 2 ------------------------------------------
            if list[i] =='câu' or list[i] == 'Câu': 
                a = i
                if list[a+1] == '2':
                    dau_2 = a
                    for j in range(len(list)):
                        if list[j] == '3':
                            b = j
                            if list[j-1] == 'câu'or list[j-1] == 'Câu':
                                if list[j-2]== 'ơn' or list[j-2]== 'Ơn':
                                    if list[j-3] == 'cảm' or list[j-3] == 'Cảm':
                                        ket_2 = j-1
                    list_cau2 = list[int(dau_2):int(ket_2)]
                    for i in range(len(list_cau2)):
                        if list_cau2[i] =='Trả' or list_cau2[i] =='trả': 
                            a = i
                            if list_cau2[a+1] == 'Lời' or list_cau2[a+1] == 'lời':
                                if list_cau2[a+2] =='Câu' or  list_cau2[a+2] =='câu':
                                    if  list_cau2[a+3] =='Hỏi' or  list_cau2[a+3] =='hỏi':
                                        if  list_cau2[a+4] =='Bắt' or  list_cau2[a+4] =='bắt':
                                            if  list_cau2[a+5] =='Đầu' or  list_cau2[a+5] =='đầu':
                                                dau_2 = a+6
                        if list_cau2[i] =='Thời' or list_cau2[i] =='thời': 
                            a = i
                            if list_cau2[a+1] == 'Gian' or list_cau2[a+1] == 'gian':
                                if list_cau2[a+2] =='Trả' or  list_cau2[a+2] =='trả':
                                    if  list_cau2[a+3] =='Lời' or  list_cau2[a+3] =='lời':
                                        if  list_cau2[a+4] =='Kết' or  list_cau2[a+4] =='kết':
                                            if  list_cau2[a+5] =='Thúc' or  list_cau2[a+5] =='thúc':
                                                ket_2 = a
                    list_cau2_2 = list_cau2[int(dau_2):int(ket_2)]
                    for i in list_cau2_2:
                        if i == 'A' or i == 'a':
                            cau2.append('A')
                            break
                        elif i == 'B'or i == 'b':
                            cau2.append('B')
                            break
                        elif i == 'C'or i == 'c':
                            cau2.append('C')
                            break
                        elif i == 'D'or i == 'd':
                            cau2.append('D')
                            break
                        else:
                            cau2.append(int(0))
                    for i in range(len(cau2)):
                        if cau2[i] == 0:
                            cau2.remove(cau2[i])
                        if cau2[i] == 'A' or cau2[i] == 'a':
                            list_1.append('A')
                            break
                        if cau2[i] == 'B'or cau2[i] == 'b':
                            list_1.append('B')
                            break
                        if cau2[i] == 'C'or cau2[i] == 'c':
                            list_1.append('C')
                            break
                        if cau2[i] == 'D'or cau2[i] == 'd':
                            list_1.append('D')
                            break
                    if len(cau2) == 0:
                        list_1.append('0')
                
        # cau 3 ------------------------------------------
            if list[i] =='câu' or list[i] == 'Câu': 
                a = i
                if list[a+1] == '3':
                    dau_3 = a
                    for j in range(len(list)):
                        if list[j] == '4':
                            b = j
                            if list[j-1] == 'câu'or list[j-1] == 'Câu':
                                if list[j-2]== 'ơn' or list[j-2]== 'Ơn':
                                    if list[j-3] == 'cảm' or list[j-3] == 'Cảm':
                                        ket_3 = j-1
                    list_cau3 = list[int(dau_3):int(ket_3)]
                    for i in range(len(list_cau3)):
                        if list_cau3[i] =='Trả' or list_cau3[i] =='trả': 
                            a = i
                            if list_cau3[a+1] == 'Lời' or list_cau3[a+1] == 'lời':
                                if list_cau3[a+2] =='Câu' or  list_cau3[a+2] =='câu':
                                    if  list_cau3[a+3] =='Hỏi' or  list_cau3[a+3] =='hỏi':
                                        if  list_cau3[a+4] =='Bắt' or  list_cau3[a+4] =='bắt':
                                            if  list_cau3[a+5] =='Đầu' or  list_cau3[a+5] =='đầu':
                                                dau_3 = a+6  
                        if list_cau3[i] =='Thời' or list_cau3[i] =='thời': 
                            a = i
                            if list_cau3[a+1] == 'Gian' or list_cau3[a+1] == 'gian':
                                if list_cau3[a+2] =='Trả' or  list_cau3[a+2] =='trả':
                                    if  list_cau3[a+3] =='Lời' or  list_cau3[a+3] =='lời':
                                        if  list_cau3[a+4] =='Kết' or  list_cau3[a+4] =='kết':
                                            if  list_cau3[a+5] =='Thúc' or  list_cau3[a+5] =='thúc':
                                                ket_3 = a                  
                    list_cau3_3 = list_cau3[int(dau_3):int(ket_3)]
                    for i in list_cau3_3:
                        if i == 'A' or i == 'a':
                            cau3.append('A')
                            break
                        elif i == 'B'or i == 'b':
                            cau3.append('B')
                            break
                        elif i == 'C'or i == 'c':
                            cau3.append('C')
                            break
                        elif i == 'D'or i == 'd':
                            cau3.append('D')
                            break
                        else:
                            cau3.append(int(0))
                    for i in range(len(cau3)):
                        if cau3[i] == 0:
                            cau3.remove(cau3[i])
                        if cau3[i] == 'A' or cau3[i] == 'a':
                            list_1.append('A')
                            break
                        if cau3[i] == 'B'or cau3[i] == 'b':
                            list_1.append('B')
                            break
                        if cau3[i] == 'C'or cau3[i] == 'c':
                            list_1.append('C')
                            break
                        if cau3[i] == 'D'or cau3[i] == 'd':
                            list_1.append('D')
                            break
                    if len(cau3) == 0:
                        list_1.append('0')

        # cau 4 ------------------------------------------
            if list[i] =='câu' or list[i] == 'Câu': 
                a = i
                if list[a+1] == '4':
                    dau_4 = a
                    for j in range(len(list)):
                        if list[j] == '5':
                            b = j
                            if list[j-1] == 'câu'or list[j-1] == 'Câu':
                                if list[j-2]== 'ơn' or list[j-2]== 'Ơn':
                                    if list[j-3] == 'cảm' or list[j-3] == 'Cảm':
                                        ket_4 = j-1
                    list_cau4 = list[int(dau_4):int(ket_4)]
                    for i in range(len(list_cau4)):
                        if list_cau4[i] =='Trả' or list_cau4[i] =='trả': 
                            a = i
                            if list_cau4[a+1] == 'Lời' or list_cau4[a+1] == 'lời':
                                if list_cau4[a+2] =='Câu' or  list_cau4[a+2] =='câu':
                                    if  list_cau4[a+3] =='Hỏi' or  list_cau4[a+3] =='hỏi':
                                        if  list_cau4[a+4] =='Bắt' or  list_cau4[a+4] =='bắt':
                                            if  list_cau4[a+5] =='Đầu' or  list_cau4[a+5] =='đầu':
                                                dau_4 = a+6 
                        if list_cau4[i] =='Thời' or list_cau4[i] =='thời': 
                            a = i
                            if list_cau4[a+1] == 'Gian' or list_cau4[a+1] == 'gian':
                                if list_cau4[a+2] =='Trả' or  list_cau4[a+2] =='trả':
                                    if  list_cau4[a+3] =='Lời' or  list_cau4[a+3] =='lời':
                                        if  list_cau4[a+4] =='Kết' or  list_cau4[a+4] =='kết':
                                            if  list_cau4[a+5] =='Thúc' or  list_cau4[a+5] =='thúc':
                                                ket_4 = a                   
                    list_cau4_4 = list_cau4[int(dau_4):int(ket_4)]
                    for i in list_cau4_4:
                        if i == 'A' or i == 'a':
                            cau4.append('A')
                            break
                        elif i == 'B'or i == 'b':
                            cau4.append('B')
                            break
                        elif i == 'C'or i == 'c':
                            cau4.append('C')
                            break
                        elif i == 'D'or i == 'd':
                            cau4.append('D')
                            break
                        else:
                            cau4.append(int(0))
                    for i in range(len(cau2)):
                        if cau4[i] == 0:
                            cau4.remove(cau4[i])
                        if cau4[i] == 'A' or cau4[i] == 'a':
                            list_1.append('A')
                            break
                        if cau4[i] == 'B'or cau4[i] == 'b':
                            list_1.append('B')
                            break
                        if cau4[i] == 'C'or cau4[i] == 'c':
                            list_1.append('C')
                            break
                        if cau4[i] == 'D'or cau4[i] == 'd':
                            list_1.append('D')
                            break
                    if len(cau4) == 0:
                        list_1.append('0')
        # cau 5 ------------------------------------------
            if list[i] =='câu' or list[i] == 'Câu': 
                a = i
                if list[a+1] == '5':
                    dau_5 = a
                    for j in range(len(list)):
                        if list[j] == '6':
                            b = j
                            if list[j-1] == 'câu'or list[j-1] == 'Câu':
                                if list[j-2]== 'ơn' or list[j-2]== 'Ơn':
                                    if list[j-3] == 'cảm' or list[j-3] == 'Cảm':
                                        ket_5 = j-1
                    list_cau5 = list[int(dau_5):int(ket_5)]
                    for i in range(len(list_cau5)):
                        if list_cau5[i] =='Trả' or list_cau5[i] =='trả': 
                            a = i
                            if list_cau5[a+1] == 'Lời' or list_cau5[a+1] == 'lời':
                                if list_cau5[a+2] =='Câu' or  list_cau5[a+2] =='câu':
                                    if  list_cau5[a+3] =='Hỏi' or  list_cau5[a+3] =='hỏi':
                                        if  list_cau5[a+4] =='Bắt' or  list_cau5[a+4] =='bắt':
                                            if  list_cau5[a+5] =='Đầu' or  list_cau5[a+5] =='đầu':
                                                dau_5 = a+6 
                        if list_cau5[i] =='Thời' or list_cau5[i] =='thời': 
                            a = i
                            if list_cau5[a+1] == 'Gian' or list_cau5[a+1] == 'gian':
                                if list_cau5[a+2] =='Trả' or  list_cau5[a+2] =='trả':
                                    if  list_cau5[a+3] =='Lời' or  list_cau5[a+3] =='lời':
                                        if  list_cau5[a+4] =='Kết' or  list_cau5[a+4] =='kết':
                                            if  list_cau5[a+5] =='Thúc' or  list_cau5[a+5] =='thúc':
                                                ket_5 = a                   
                    list_cau5_5 = list_cau5[int(dau_5):int(ket_5)]
                    for i in list_cau5_5:
                        if i == 'A' or i == 'a':
                            cau5.append('A')
                            break
                        elif i == 'B'or i == 'b':
                            cau5.append('B')
                            break
                        elif i == 'C'or i == 'c':
                            cau5.append('C')
                            break
                        elif i == 'D'or i == 'd':
                            cau5.append('D')
                            break
                        else:
                            cau5.append(int(0))
                    for i in range(len(cau5)):
                        if cau5[i] == 0:
                            cau5.remove(cau5[i])
                        if cau5[i] == 'A' or cau5[i] == 'a':
                            list_1.append('A')
                            break
                        if cau5[i] == 'B'or cau5[i] == 'b':
                            list_1.append('B')
                            break
                        if cau5[i] == 'C'or cau5[i] == 'c':
                            list_1.append('C')
                            break
                        if cau5[i] == 'D'or cau5[i] == 'd':
                            list_1.append('D')
                            break
                    if len(cau5) == 0:
                        list_1.append('0')

        # cau 6 ------------------------------------------
            if list[i] =='câu' or list[i] == 'Câu': 
                a = i
                if list[a+1] == '6':
                    dau_6 = a
                    ket_6 = len(list)
                    list_cau6 = list[int(dau_6):int(ket_6)]
                    for i in range(len(list_cau6)):
                        if list_cau6[i] =='Trả' or list_cau6[i] =='trả': 
                            a = i
                            if list_cau6[a+1] == 'Lời' or list_cau6[a+1] == 'lời':
                                if list_cau6[a+2] =='Câu' or  list_cau6[a+2] =='câu':
                                    if  list_cau6[a+3] =='Hỏi' or  list_cau6[a+3] =='hỏi':
                                        if  list_cau6[a+4] =='Bắt' or  list_cau6[a+4] =='bắt':
                                            if  list_cau6[a+5] =='Đầu' or  list_cau6[a+5] =='đầu':
                                                dau_6 = a+6 
                        elif list_cau6[i] =='Thời' or list_cau6[i] =='thời': 
                            a = i
                            if list_cau6[a+1] == 'Gian' or list_cau6[a+1] == 'gian':
                                if list_cau6[a+2] =='Trả' or  list_cau6[a+2] =='trả':
                                    if  list_cau6[a+3] =='Lời' or  list_cau6[a+3] =='lời':
                                        if  list_cau6[a+4] =='Kết' or  list_cau6[a+4] =='kết':
                                            if  list_cau6[a+5] =='Thúc' or  list_cau6[a+5] =='thúc':
                                                ket_6 = a                  
                    list_cau6_6 = list_cau6[int(dau_6):int(ket_6)]
                    for i in list_cau6_6:
                        if i == 'A' or i == 'a':
                            cau6.append('A')
                            break
                        elif i == 'B' or i == 'b':
                            cau6.append('B')
                            break
                        elif i == 'C' or i == 'c':
                            cau6.append('C')
                            break
                        elif i == 'D'or i == 'd':
                            cau6.append('D')
                            break
                        else:
                            cau6.append(int(0))

                    for i in range(len(cau6)):
                        if cau6[i] == 0:
                            cau6.remove(cau6[i])
                        if cau6[i] == 'A' or cau6[i] == 'a':
                            list_1.append('A')
                            break
                        if cau6[i] == 'B'or cau6[i] == 'b':
                            list_1.append('B')
                            break
                        if cau6[i] == 'C'or cau6[i] == 'c':
                            list_1.append('C')
                            break
                        if cau6[i] == 'D'or cau6[i] == 'd':
                            list_1.append('D')
                            break
                    if len(cau6) == 0:
                        list_1.append('0') 
        for ghep in list_cau1:
            cau_hoi1 += ' ' + ghep
        for ghep in list_cau2:
            cau_hoi2 += ' ' + ghep
        for ghep in list_cau3:
            cau_hoi3 += ' ' + ghep
        for ghep in list_cau4:
            cau_hoi4 += ' ' + ghep
        for ghep in list_cau5:
            cau_hoi5 += ' ' + ghep
        for ghep in list_cau6:
            cau_hoi6 += ' ' + ghep
        with open(r"E:\04-02-2023\folder1\log.txt",'w', encoding='utf-8', errors='ignore') as f:
                f.write(" %s\n " %cau_hoi1)
                f.write("%s\n " %cau_hoi2)  
                f.write("%s\n " %cau_hoi3)  
                f.write("%s\n " %cau_hoi4)  
                f.write("%s\n " %cau_hoi5)  
                f.write("%s\n " %cau_hoi6) 
        dapan = ['D','D','C','B','D','C']
        for i in range(len(dapan)):
            if dapan[i] == list_1[i]:
                ketqua.append('True')
            else:
                ketqua.append('False')       
        df = pd.DataFrame(zip(list_1,dapan,ketqua), index =['Câu 1', 'Câu 2', 'Câu 3', 'Câu 4', 'Câu 5', 'Câu 6'],columns =['CÂU TRẢ LỜI','ĐÁP ÁN','KẾT QUẢ'])
        with open('df.json', 'w', encoding='utf-8') as file:
            df.to_json(file, force_ascii=False)
        print("Đây là kết quả:.........")
        print("Câu trả lời: ", list_1)
        print("Đáp án: ", dapan)
        print(df)
        
split_mp3 = SplitWavAudioMubin(folder, file_mp3,file_wav)
split_mp3.multiple_split(min_per_split=1)
split_mp3.audio_to_text()