def tulis(teks):
    print(teks)

def konversi_ke_biner(angka, basis):
    return bin(int(angka, basis))[2:]

def konversi_ke_oktal(angka, basis):
    return oct(int(angka, basis))[2:]

def konversi_ke_desimal(angka, basis):
    return str(int(angka, basis))

def konversi_ke_heksadesimal(angka, basis):
    return hex(int(angka, basis))[2:].upper()

def is_valid_input(angka, basis):
    try:
        if basis == 2:
            int(angka, 2)
        elif basis == 8:
            int(angka, 8)
        elif basis == 10:
            int(angka)
        elif basis == 16:
            int(angka, 16)
        return True
    except ValueError:
        return False

def load_instructions(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
        return lines
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan.")
        return []

def pilih_basis():
    tulis("Pilih basis asal bilangan yang ingin dikonversi:")
    tulis("Biner")
    tulis("Oktal")
    tulis("Desimal")
    tulis("Heksadesimal")
    
    while True:
        pilihan = input("Masukkan basis asal: ").strip().lower()
        if pilihan == "biner":
            return 2, "biner"
        elif pilihan == "oktal":
            return 8, "oktal"
        elif pilihan == "desimal":
            return 10, "desimal"
        elif pilihan == "heksadesimal":
            return 16, "heksadesimal"
        else:
            tulis("Pilihan tidak valid. Silakan pilih lagi.")

def interpret(instructions):
    """Interpret and execute instructions in Javanese."""
    lanjut = True 

    while lanjut:
        for instruksi in instructions:
            if instruksi == "ASAL BASISE":
                basis_asal, nama_basis = pilih_basis()

            elif instruksi == "LEBOKNO ANGKANE":
                while True:
                    bilangan = input(f"Masukkan bilangan dalam basis {nama_basis}: ")
                    if is_valid_input(bilangan, basis_asal):
                        break
                    else:
                        tulis("Bilangan tidak valid untuk basis yang dipilih. Silakan coba lagi.")

            elif instruksi == "HASIL KONVERSINE":
                tulis("Hasil konversi:")
                tulis(f"Desimal: {konversi_ke_desimal(bilangan, basis_asal)}")
                tulis(f"Biner: {konversi_ke_biner(bilangan, basis_asal)}")
                tulis(f"Oktal: {konversi_ke_oktal(bilangan, basis_asal)}")
                tulis(f"Heksadesimal: {konversi_ke_heksadesimal(bilangan, basis_asal)}")

            elif instruksi == "LANJUTNO":
                pilihan = input("Ketik 'lanjut' untuk konversi lagi atau 'berhenti' untuk mengakhiri: ").strip().lower()
                if pilihan == "lanjut":
                    lanjut = True  
                    break  
                elif pilihan == "berhenti":
                    lanjut = False  
                    tulis("Program dihentikan.")
                    return  
                else:
                    tulis("Pilihan tidak valid. Silakan pilih 'lanjut' atau 'berhenti'.")
                        
            elif instruksi == "WES MARI":
                tulis("Program dihentikan.")
                return  

if __name__ == "__main__":
    file_path = "main.oll"
    instructions = load_instructions(file_path)
    interpret(instructions)