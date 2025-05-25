from QLSV import QLSV

qlsv = QLSV()
while(True):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*********************MENU*********************")
    print("**   1. Them sinh vien.                     **")   
    print("**   2. Cap nhat thong tin sinh vien.       **") 
    print("**   3. Xoa sinh vien boii ID.              **")
    print("**   4. Tim kiem sinh vien theo ten.        **")
    print("**   5. Sap xep sinh vien theo gpa.         **")
    print("**   6. Sap xep sinh vien theo ten.         **")
    print("**   7. Hien thi danh sach.                 **")
    print("**   8. Thoat chuong trinh.                 **")
    print("**********************************************")
    
    key = int(input("Nhap lua chon: "))
    if key == 1:
        qlsv.addSV()
    elif key == 2:
        if(qlsv.soluongSV() > 0):
            ID = int(input("Nhap ID sinh vien can cap nhat: "))
            qlsv.updateSV(ID)
        else:
            print("Khong co sinh vien nao trong danh sach.")
    elif key == 3:
        if(qlsv.soluongSV() > 0):
            ID = int(input("Nhap ID sinh vien can xoa: "))
            isDeleted = qlsv.deleteByID(ID)
            if(isDeleted):
                print(f"Da xoa sinh vien voi ID: {ID}")
            else:
                print(f"Khong tim thay sinh vien voi ID: {ID}")
        else:
            print("Khong co sinh vien nao trong danh sach.")
    elif key == 4:
        if(qlsv.soluongSV() > 0):
            keyword = input("Nhap ten sinh vien can tim: ")
            listSV = qlsv.findbyName(keyword)
            qlsv.showListSV(listSV)
        else:
            print("Khong co sinh vien nao trong danh sach.")
    elif key == 5:
        if(qlsv.soluongSV() > 0):
            qlsv.sortbyGPA()
            print("Da sap xep danh sach sinh vien theo GPA.")
            qlsv.showListSV(qlsv.list_sv)
        else:
            print("Khong co sinh vien nao trong danh sach.")
    elif key == 6:
        if(qlsv.soluongSV() > 0):
            qlsv.sortbyName()
            print("Da sap xep danh sach sinh vien theo ten.")
            qlsv.showListSV(qlsv.list_sv)
        else:
            print("Khong co sinh vien nao trong danh sach.")
    elif key == 7:
        if(qlsv.soluongSV() > 0):
            qlsv.showListSV(qlsv.list_sv)
        else:
            print("Khong co sinh vien nao trong danh sach.")
    elif key == 8:
        print("Cam on ban da su dung chuong trinh!")
        break
    else:
        print("Lua chon khong hop le. Vui long chon lai.")