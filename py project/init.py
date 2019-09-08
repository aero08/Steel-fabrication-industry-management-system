from Tkinter import *
from sqlite3 import *

con=Connection('data')
cur=con.cursor()
#cur.execute('drop table orders')
cur.execute("create table if not exists orders(order_id varchar2(5) PRIMARY KEY,cname varchar2(10),cphone varchar2(10),c_add varchar2(20))")

def fun():
    #print v1.get()
    if v1.get()==1:
        nwo=Tk()
        nwo.title('New order')
        Label(nwo,text="New order-",font='calibri 15').grid(row=1,column=0)
        Label(nwo,text="Enter customer name:").grid(row=2,column=0)
        cname=Entry(nwo)
        cname.grid(row=2,column=1)
        Label(nwo,text="Enter customer phone no:").grid(row=3,column=0)
        pno=Entry(nwo)
        pno.grid(row=3,column=1)
        Label(nwo,text="Enter customer address:").grid(row=4,column=0)
        add=Entry(nwo)
        add.grid(row=4,column=1)
       

        def fun1():
            cur.execute("select count(*) from orders")
            or_id=cur.fetchall()[0][0]
            print or_id
            cur.execute("insert into orders values(?,?,?,?)",(or_id,cname.get(),pno.get(),add.get()))
            con.commit()

            if v2.get()==1:
                rs=Tk()
                rs.title('Dimensions(rolling shutter)-')
                Label(rs,text="Enter dimensions for rolling shutter-").grid(row=0,column=0)
                Label(rs,text="Length:").grid(row=1,column=0)
                l=Entry(rs)
                l.grid(row=1,column=1)
                Label(rs,text="Breadth").grid(row=2,column=0)
                b=Entry(rs)
                b.grid(row=2,column=1)
                def insertd1():
                    cname.delete(0,END)
                    pno.delete(0,END)
                    add.delete(0,END)
                    l.delete(0,END)
                    b.delete(0,END)
                    rs.destroy()
                    
                Button(rs,text="Submit",command=insertd1).grid(row=3,column=0)
                rs.mainloop()
                
            if v2.get()==2:
                aw=Tk()
                aw.title('Dimensions(awnings)')
                Label(aw,text="Enter dimensions for Awnings-").grid(row=0,column=0)
                Label(aw,text="Length:").grid(row=1,column=0)
                l=Entry(aw)
                l.grid(row=1,column=1)
                Label(aw,text="Breadth").grid(row=2,column=0)
                b=Entry(aw)
                b.grid(row=2,column=1)
                def insertd2():
                    cname.delete(0,END)
                    pno.delete(0,END)
                    add.delete(0,END)
                    l.delete(0,END)
                    b.delete(0,END)
                    aw.destroy()
                Button(aw,text="Submit",command=insertd2).grid(row=3,column=0)
                aw.mainloop()

            if v2.get()==3:
                g=Tk()
                g.title('weight(gate)-')
                Label(g,text="Enter weight in kg(for gate)-").grid(row=0,column=0)
                Label(g,text="Weight:").grid(row=1,column=0)
                wg=Entry(g)
                wg.grid(row=1,column=1)
                def insertd3():
                    cname.delete(0,END)
                    pno.delete(0,END)
                    add.delete(0,END)
                    wg.delete(0,END)
                    g.destroy()
                Button(g,text="Submit",command=insertd3).grid(row=2,column=0)
                g.mainloop()

            if v2.get()==4:
                gr=Tk()
                gr.title('Weight(grill)-')
                Label(gr,text="Enter weight in kg(for grill)-").grid(row=0,column=0)
                Label(gr,text="Weight:").grid(row=1,column=0)
                wg=Entry(gr)
                wg.grid(row=1,column=1)
                def insertd4():
                    cname.delete(0,END)
                    pno.delete(0,END)
                    add.delete(0,END)
                    wg.delete(0,END)
                    gr.destroy()
                Button(gr,text="Submit",command=insertd4).grid(row=2,column=0)
                gr.mainloop()
                
        v2=IntVar(nwo)
        
        Label(nwo,text="Select product/s-").grid(row=5,column=0)
        Radiobutton(nwo,text='Rolling Shutter',variable=v2,value=1).grid(row=6,column=0)
        Radiobutton(nwo,text='Awnings',variable=v2,value=2).grid(row=7,column=0)
        Radiobutton(nwo,text='Gates',variable=v2,value=3).grid(row=8,column=0)
        Radiobutton(nwo,text='Grills',variable=v2,value=4).grid(row=9,column=0)
        #print 'herrere',v2.get()
        Button(nwo,text="Submit",command=fun1).grid(row=10,column=0)
        nwo.mainloop()

        
    if v1.get()==2:
        sod=Tk()
        sod.title('Search order details')
        Label(sod,text="Search order details-",font='calibri 15').grid(row=1,column=0)
        Label(sod,text="Enter order id to searched:").grid(row=2,column=0)
        or_id1=Entry(sod)
        or_id1.grid(row=2,column=1)
        def fun2():
            Label(sod,text="Order details-",font='calibri 15').grid(row=3,column=0)
            showId=str(or_id1.get())
            if showId=="":
                Label(sod,text="         Invalid Entry           ").grid(row=4,column=0)
            else:
                comm='select order_id,cname from orders where order_id='+showId    
                cur.execute(comm)
                x=cur.fetchall()
                if x==[]:
                    print 'Error!!'
                else:
                    cname2=str(x[0][1])
                    orderid2=str(x[0][0])
                    Label(sod,text="Order id-"+orderid2,font='calibri 15').grid(row=5,column=0)
                    Label(sod,text="customer name-"+cname2,font='calibri 15').grid(row=6,column=0)
                    print cname2,orderid2
                
                
        
        Button(sod,text="Submit",command=fun2).grid(row=7,column=0)
        sod.mainloop()

    if v1.get()==3:
        rp=Tk()
        rp.title('Repair')
        Label(rp,text="Repair-",font='calibri 15').grid(row=1,column=0)
        Label(rp,text="Enter customer name:").grid(row=2,column=0)
        cname=Entry(rp)
        cname.grid(row=2,column=1)
        Label(rp,text="Enter customer phone no:").grid(row=3,column=0)
        pno=Entry(rp)
        pno.grid(row=3,column=1)
        Label(rp,text="Enter customer address:").grid(row=4,column=0)
        add=Entry(rp)
        add.grid(row=4,column=1)
        def insert3():
            cur.execute("select count(*) from orders")
            or_id=cur.fetchall()[0][0]
            #print or_id
            cur.execute("insert into orders values(?,?,?,?)",(or_id,cname.get(),pno.get(),add.get()))
            con.commit()
            cname.delete(0,END)
            pno.delete(0,END)
            add.delete(0,END)
        Button(rp,text="Submit",command=insert3).grid(row=5,column=0)
        rp.mainloop()

    if v1.get()==4:
        mnt=Tk()
        mnt.title('Maintainance')
        Label(mnt,text="Maintainance-",font='calibri 15').grid(row=1,column=0)
        Label(mnt,text="Enter customer name:").grid(row=2,column=0)
        cname=Entry(mnt)
        cname.grid(row=2,column=1)
        Label(mnt,text="Enter customer phone no:").grid(row=3,column=0)
        pno=Entry(mnt)
        pno.grid(row=3,column=1)
        Label(mnt,text="Enter customer address:").grid(row=4,column=0)
        add=Entry(mnt)
        add.grid(row=4,column=1)
        def insert4():
            cur.execute("select count(*) from orders")
            or_id=cur.fetchall()[0][0]
            print or_id
            cur.execute("insert into orders values(?,?,?,?)",(or_id,cname.get(),pno.get(),add.get()))
            con.commit()
            cname.delete(0,END)
            pno.delete(0,END)
            add.delete(0,END)
        Button(mnt,text="Submit",command=insert4).grid(row=5,column=0)
        mnt.mainloop()
        

root=Tk()
root.title('Steel fabrication industry')
Label(root,text="Steel fabrication industry",font='calibri 20 bold').grid(row=0,column=0)
Label(root,text="Service type-",font='calibri 15').grid(row=1,column=0)
Label(root,text="--------",font='calibri 15').grid(row=2,column=0)
v1=IntVar(root)

Radiobutton(root,text='New order',variable=v1,value=1).grid(row=3,column=0)
Label(root,text="--------").grid(row=4,column=0)
Radiobutton(root,text='Search order details',variable=v1,value=2).grid(row=5,column=0)
Label(root,text="--------").grid(row=6,column=0)
Radiobutton(root,text='Repair',variable=v1,value=3).grid(row=7,column=0)
Radiobutton(root,text='Maintainance',variable=v1,value=4).grid(row=8,column=0)
Label(root,text="--------",).grid(row=9,column=0)
Button(root,text="Submit",command=fun).grid(row=10,column=0)



root.mainloop()



    
