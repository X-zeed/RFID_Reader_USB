import keyboard

buffer=""

def block_all(e):
    global buffer
    
    if e.event_type == "down":
        if e.name == "enter":
            print("RFID:", buffer)
            buffer=""
        elif len(e.name)==1:
            buffer+=e.name
    
    return False  # block ไม่ให้ไปโปรแกรมอื่น

keyboard.hook(block_all)
keyboard.wait()
