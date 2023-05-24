from tkinter import*



def rules_window():
    window = Tk()
    window.title("Правила")
    text = Text(window, width=30, height=12, bg="light blue",
                fg='black', wrap=WORD)
    scroll = Scrollbar(window, command=text.yview)
    scroll.pack(side=RIGHT, fill=Y)
    text.insert(1.0, "Правила игры"
                     "\nПравила игры предельно просты."
                     "\n"
                     "\nВаша задача - убрать все цветные блоки с игрового поля."
                     "\n"
                     "\nЧтобы удалить блок, игрок должен нажать на любой блок, который стоит рядом (вертикально или горизонтально) с другим блоком того же цвета."
                     "\n"
                     "\nТаким образом, будет уничтожена целая цепочка блоков одного цвета."
                     "\n"
                     "\nБлоки, которые были сверху, одновременно спустятся вниз, заполняя пустое пространство."
                     "\n"
                     "\nКогда удаляется весь столбец, столбцы справа сдвигаются влево, занимая пустое место."
                     "\n"
                     "\nИгра заканчивается, когда у на игровом поле заканчиваются цветные блоки.")

    text.tag_add('title', 1.0, '1.end')
    text.tag_config('title', justify=CENTER,
                    font=("Verdana", 24, 'bold'))
    text.pack()
    window.geometry("250x200")