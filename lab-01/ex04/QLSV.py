from SinhVien import SinhVien

class QLSV:
    list_sv = []
    
    def generateID(self):
        maxId = 1
        if(self.soluongSV() > 0):
            maxId = self.list_sv[0]._id
            for sv in self.list_sv:
                if maxId < sv._id:
                    maxId = sv._id
            maxId += 1
        return maxId
    
    def soluongSV(self):
        return self.list_sv.__len__()
    
    def addSV(self):
        svId = self.generateID()
        svName = input("Nhap ten sinh vien: ")
        svSex = input("Nhap gioi tinh (Nam/Nu): ")
        svMajor = input("Nhap nganh hoc: ")
        svGPA = float(input("Nhap diem GPA: "))
        sv = SinhVien(svId, svName, svSex, svMajor, svGPA)
        self.xepRank(sv)
        self.list_sv.append(sv)
        print(f"Da them sinh vien: {sv._name} (ID: {sv._id})")
        
    def updateSV(self, ID):
        sv: SinhVien = self.findbyID(ID)
        if(sv != None):
            name = input("Nhap ten sv: ")
            sex = input("Nhap gioi tinh (Nam/Nu): ")
            major = input("Nhap nganh hoc: ")
            gpa = float(input("Nhap diem GPA: "))
            
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._gpa = gpa
            self.xepRank(sv)
            print(f"Da cap nhat sinh vien: {sv._name} (ID: {sv._id})")
        else:
            print(f"Khong tim thay sinh vien voi ID: {ID}")
            
    def sortbyID(self):
        self.list_sv.sort(key=lambda sv: sv._id, reverse=False)
        
    def sortbyName(self):
        self.list_sv.sort(key=lambda sv: sv._name, reverse=False)
        
    def sortbyGPA(self):
        self.list_sv.sort(key=lambda sv: sv._gpa, reverse=False)
        
    def findbyID(self, ID):
        search_result = None
        if(self.soluongSV() > 0):
            for sv in self.list_sv:
                if sv._id == ID:
                    search_result = sv
        return search_result
    
    def findbyName(self, keyword):
        listSV = []
        if(self.soluongSV() > 0):
            for sv in self.list_sv:
                if sv._name.upper().find(keyword.upper()) != -1:
                    listSV.append(sv)
        return listSV
    
    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findbyID(ID)
        if(sv != None):
            self.list_sv.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepRank(self, sv: SinhVien):
        if(sv._gpa >= 8):
            sv._rank = "Gioi"
        elif(sv._gpa >= 6.5):
            sv._rank = "Kha"
        elif(sv._gpa >= 5):
            sv._rank = "Trung Binh"
        else:
            sv._rank = "Yeu"
            
    def showListSV(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}".format("ID", "Ten", "Gioi Tinh", "Nganh", "GPA", "Xep Hang"))
        if(listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._gpa, sv._rank))
        print("\n")
        
    def getListSV(self):
        return self.list_sv
        
    
            