
import time
def meeting_room_reservations05(st, r):

    total = []
    v = []
    sum = 0

    while (len(st) != 0):
        if sum == r :
            total.append(v)
            sum = 0
            v = []
        else:
            if st[0] + sum <= r:
                sum = sum + st[0] 
                v.append(st[0])
                st.pop(0)
            elif st[-1] + sum <= r:
                sum = sum + st[-1] 
                v.append(st[-1])
                st.pop(-1)
            else:
                total.append(v)
                sum = 0
                v = []
    else:
        if len(v) > 0:
            total.append(v)
        return total

def get_result(content, t):
    a = 0
    for line in content:
        for i in line:
            if a >= 2:
                if i.isdigit() == True:
                    t.append(int(i))
        a += 1 
    return t

def write_output_file(total):
    c = 0
    flie2.write("Rooms required : %s\n"%(len(total)) )
    flie2.write("The reservation time\n********************\n")
    for room in total:
        c += 1
        flie2.write("%s: "%(c))
        for i in room:
            flie2.write("%s "%i)
        flie2.write("\n")

# Require file here
flie1 = open("Midterm Project/meeting_room10.txt","r") # อ่านไฟล์
flie2 = open("Midterm Project/room_reservation10.txt","w") # เขียนไฟล์
content = flie1.readlines()

t = get_result(content, [])
t.sort(reverse=True)
r = 7
s_time = time.time()
total = meeting_room_reservations05(t, r)
e_time = time.time()

print("%f" %((e_time - s_time) / 1000))

write_output_file(total)

flie1.close()
flie2.close()
