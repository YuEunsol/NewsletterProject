from config import *

def createXl(keyword, news_list):
    wb = Workbook()
    createNewsTitleFont(wb)
    ws = wb.active
    ws.title = keyword

    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=2)
    ws["A1"] = keyword
    setSheetTitleFont(ws["A1"])
    # ws.merge_cells(start_row=1, start_column=3, end_row=1, end_column=4)
    ws["C1"] = today
    setSheetTitleFont(ws["C1"])

    setColumnWidthToSlim(ws, "A")
    setColumnWidthToSlim(ws, "B")
    setColumnWidthToWide(ws, "C")
    setColumnWidthToWide(ws, "D")

    for i, each in enumerate(columns):
        cell_number = f"{ascii_uppercase[i]}2"
        ws[cell_number] = each
        setColumnFont(ws[cell_number])
        setHorizontalCenter(ws[cell_number])

    for row_index, news_dict in enumerate(news_list):
        for column_index, each in enumerate(news_dict.values()):
            if column_index == len(news_dict):
                continue
            # 높이 지정
            setColumnWidthToHigh(ws, row_index + 3)

            cell_number = f"{ascii_uppercase[column_index]}{row_index + 3}"

            setVerticalCenter(ws[cell_number])

            # A, B, C 열은 가운데 정렬
            if ascii_uppercase[column_index] in ["A", "B"]:
                setBothCenter(ws[cell_number])
            elif ascii_uppercase[column_index] in ["C"]:
                ws[cell_number].hyperlink = news_dict["link"]
                setNewsTitleFont(ws[cell_number])
            elif ascii_uppercase[column_index] in ["D"]:
                setLineBreak(ws[cell_number])

            ws[cell_number] = each


    save_path = f"{xl_path}/{keyword}_{today}.xlsx"
    wb.save(save_path)
    print(f"{save_path}에 저장 했습니다.")


def setSheetTitleFont(cell):
    cell.font = Font(size=18, italic=True, bold=True)

def createNewsTitleFont(wb):
    if not "news_title_style" in wb.named_styles:
        news_title_style = named_styles.NamedStyle(name='news_title_style')
        news_title_style.alignment = Alignment(vertical='center', horizontal='center')
        news_title_style.font = Font(size=12, bold=True, color='000000FF', underline='single')
        news_title_style.style = 'Hyperlink'

        wb.add_named_style(news_title_style)

def setNewsTitleFont(cell):
    cell.style = 'news_title_style'

def setColumnFont(cell):
    cell.font = Font(size=14, bold=True)
    cell.border = Border(left=Side(border_style="double", color="000000"),
                         right=Side(border_style="double", color="000000"),
                         top=Side(border_style="double", color="000000"),
                         bottom=Side(border_style="double", color="000000"))
    cell.fill = PatternFill(start_color='FFFF33', fill_type='solid')

def setColumnWidthToSlim(sheet, column):
    sheet.column_dimensions[column].width = 20

def setColumnWidthToWide(sheet, column):
    sheet.column_dimensions[column].width = 80

def setColumnWidthToHigh(sheet, row):
    sheet.row_dimensions[row].height = 50

def setBothCenter(cell):
    cell.alignment = Alignment(vertical='center', horizontal='center')

def setVerticalCenter(cell):
    cell.alignment = Alignment(vertical='center')

def setHorizontalCenter(cell):
    cell.alignment = Alignment(horizontal='center')

def setLineBreak(sheet, column):
    sheet.column_dimensions[column].wrap_text = True

def setLineBreak(cell):
    cell.alignment = Alignment(wrap_text=True)