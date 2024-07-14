import json

from deep_translator import GoogleTranslator
from openpyxl import Workbook
import requests
import math
import data

#Функция для выполнения запросов
def data_request(type, cookies, headers, json_data):
    response = requests.post(
        type,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return response

#Функция для выбора классификаторов
def cpvs():
    with open('classificators.json', 'r') as file:
        dirr = json.load(file)
    print("Введите номер группы классификаторов\n"
          "1.Беспилотники\n"
          "2.Военная техника (ремонт)\n"
          "3.Похоронные услуги\n"
          "4.Радиотехника\n"
          "5.Питание\n"
          "6.Боеприпасы\n"
          "7.Обучение\n"
          "8.Исследования\n"
          "9.Топливо\n"
          "10.Ремонтные работы\n"
          "11.Машины для обработки данных\n"
          "12.Энергетика")
    cpvs_list = dirr['classificators'][int(input())-1]
    print(f"Поиск по классификаторам:\n{cpvs_list}")
    data.json_data["SearchFilter"]["Cpvs"] = cpvs_list  #Добавление классификаторов в запрос

#Функция выбора и ввода периода выгрузки
def date_choice():
    print("\nВыберите за какой период выгрузить данные:\n"
          "1.За один день\n"
          "2.За несколько дней")
    match str(input()):
        case "1":
            try:
                print("Введите нужную дату для выгрузки данных (Формат: ДД.ММ.ГГГГ):")
                date = str(input()).split(".")
                data.json_data["SearchFilter"][
                    "tenderCreationTimeFrom"] = f'{date[2]}-{date[1]}-{date[0]}T00:00:00.000Z'
                data.json_data["SearchFilter"]["tenderCreationTimeTo"] = f'{date[2]}-{date[1]}-{date[0]}T23:59:59.000Z'
            except:
                print("Некорректный ввод. Попробуйте еще раз.")
                date_choice()
        case "2":
            try:
                print("Введите c какой даты выгрузить данные (Формат: ДД.ММ.ГГГГ):")
                date = str(input()).split(".")
                data.json_data["SearchFilter"][
                    "tenderCreationTimeFrom"] = f'{date[2]}-{date[1]}-{date[0]}T00:00:01.000Z'
                print("Введите по какую дату выгрузить данные (Формат: ДД.ММ.ГГГГ):")
                date = str(input()).split(".")
                data.json_data["SearchFilter"]["tenderCreationTimeTo"] = f'{date[2]}-{date[1]}-{date[0]}T23:59:59.000Z'
            except:
                print("Некорректный ввод. Попробуйте еще раз.")
                date_choice()
        case _:
            print("Некорректный ввод. Попробуйте еще раз.")
            date_choice()

#Функция получения ссылок на тендеры
def get_links(type):
    links = []
    match type:
        case 1:
            data.json_data["SearchFilter"]["ProcurementMethod"] = ["limited"]
            data.json_data["SearchFilter"]["statuses"] = ['active', 'unsuccessful', 'complete', 'cancelled']
            print("Кол-во неконкурентных тендеров: ")
        case 2:
            data.json_data["SearchFilter"]["ProcurementMethod"] = ['open', 'selective']
            data.json_data["SearchFilter"]["statuses"] = ['active.enquiries', 'active.tendering',
                                                          'active.pre-qualification',
                                                          'active.pre-qualification.stand-still',
                                                          'active.stage2.pending',
                                                          'active.stage2.waiting', 'active.auction',
                                                          'active.qualification',
                                                          'active.qualification.stand-still', 'active.awarded',
                                                          'unsuccessful', 'complete', 'cancelled']
            print("Кол-во конкурентных тендеров: ")

    response = data_request(read, data.cookies, data.headers, data.json_data)
    page = response.json()
    records = page["result"]["countAllRecords"]
    page_count = math.ceil(records / 20)
    print(str(records))

    for i in range(page_count):
        data.json_data["Page"] = i + 1
        response = data_request(read, data.cookies, data.headers, data.json_data)
        page = response.json()
        keys = [x for x in page["result"]["tender"]]
        for j in keys:
            links.append(j["url"])
    return links

#Функция получения данных из тендеров
def get_data(links, type, count):
    arr = []
    for link in links:
        try:
            parts = link.split("/")
        except:
            continue

        json_data_get = {
            'id': None,
            'userName': None,
            'display': None,
            'url': parts[2],
            'categoryUrl': parts[1],
        }
        response = data_request(get, data.cookies, data.headers, json_data_get)

        page = response.json()
        quantity = 0
        count += 1
        value = 0
        startDate = ''
        endDate = ''
        deliveryDate = page["result"]["lots"][0]["items"][0]["deliveryDate"]["endDate"].split("T")[0].split("-")
        deliveryDate = f"{deliveryDate[2]}.{deliveryDate[1]}.{deliveryDate[0]}"
        address = page["result"]["organization"]["address"]
        for j in page["result"]["lots"]:
            for q in j["items"]:
                quantity += q["quantity"]
        p_name = 'Нет'
        o_name = 'Нет'
        try:
            value = page["result"]["value"]["amount"]
        except:
            pass
        try:
            p_name = page["result"]["organization"]["contactPoint"]["name"]
        except:
            pass
        try:
            o_name = page["result"]["organization"]["name"]
        except:
            pass
        match type:
            case 1:
                startDate = page["result"]["creationTime"].split("T")[0].split("-")
                startDate = startDate[2] + "." + startDate[1] + "." + startDate[0]
                endDate = "Нет данных"
            case 2:
                startDate = page["result"]["tenderPeriod"]["startDate"].split("T")[0].split("-")
                startDate = startDate[2] + "." + startDate[1] + "." + startDate[0]
                endDate = page["result"]["tenderPeriod"]["endDate"].split("T")[0].split("-")
                endDate = endDate[2] + "." + endDate[1] + "." + endDate[0]

        arr.append([count,
                        translator.translate(page["result"]["title"]),
                        page["result"]["status"],
                        quantity,
                        value,
                        value * 0.025,
                        startDate,
                        endDate,
                        deliveryDate,
                        translator.translate(address["region"]["title"]),
                        translator.translate(
                            f"{address["postIndex"]}, {address["country"]["title"]}, {address["region"]["title"]}, {address["city"]["title"]}, {address["addressStr"]}"),
                        translator.translate(p_name),
                        translator.translate(o_name)
                        ])
        print(arr[-1])
    return arr

#Функция сохрания файла
def save_tenders(tenders):
    wb = Workbook()
    ws = wb.active
    for i in tenders:
        try:
            ws.append(i)
        except:
            ws.append(["Ошибка"])
    wb.save("tender.xlsx")
    print("Результаты сохранены в файле tender.xlsx на рабочем столе")


if __name__ == "__main__":
    read = "https://gov.e-tender.ua/api/services/etender/readTender/GetTenders"
    get = "https://gov.e-tender.ua/api/services/etender/getTender/GetTender"

    translator = GoogleTranslator(source='auto', target='ru')

    tenders = [["№", "Название тендера", "Статус", "Кол-во", "Сумма в гривнах", "Сумма в долларах", "Дата начала",
                "Дата завершения", "Дата доставки", "Область", "Адресс", "Контактное лицо", "Заказчик"]]
    count = 0

    print("\nПарсер сайта тендерных закупок Украины.\n"
          "Данный парсер работает по тематикам определенным далее.\n"
          "Для работы выберите необходимый пункт по порядку и нажмите Enter\n"
          "ВНИМАНИЕ! Перед работой обязательно включите VPN и закройте Excel файлы!")

    date_choice()
    cpvs()

    tend1 = get_data(get_links(1), 1, 0)
    tend2 = get_data(get_links(2), 2, tend1[-1][0])
    tenders += tend1 + tend2
    save_tenders(tenders)