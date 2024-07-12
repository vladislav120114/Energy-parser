cookies = {
    'cf_clearance': 'OgI9BUFTQ4nlImM2CV58jN.LvlmOYj4N8PATPSTD2gQ-1708609524-1.0-AbYy2S1dGot/SQyf+z8y19V0Spw2KYNY0JqbPlfvIZipzzHInq1rS8F2Lk+NRcCCsRv8l6+OA3BRvCXlKPLkZiY=',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-02-20%2014%3A31%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fe-tender.ua%2Fru%7C%7C%7Crf%3Dhttps%3A%2F%2Fe-tender.ua%2Fru%3F__cf_chl_tk%3DFOr8Uy3dKzHjq7GeEnC2WpeAEDJGRVTXrcQ_KYzInyo-1708428655-0.0-4114',
    'sbjs_first_add': 'fd%3D2024-02-20%2014%3A31%3A34%7C%7C%7Cep%3Dhttps%3A%2F%2Fe-tender.ua%2Fru%7C%7C%7Crf%3Dhttps%3A%2F%2Fe-tender.ua%2Fru%3F__cf_chl_tk%3DFOr8Uy3dKzHjq7GeEnC2WpeAEDJGRVTXrcQ_KYzInyo-1708428655-0.0-4114',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29',
    'sbjs_udata': 'vst%3D3%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20rv%3A123.0%29%20Gecko%2F20100101%20Firefox%2F123.0',
    '_gcl_au': '1.1.1146963663.1708428695',
    '_ga_D5H0FNS3KB': 'GS1.1.1708674184.15.0.1708674184.60.0.0',
    '_ga': 'GA1.2.1115955458.1708428695',
    '_gid': 'GA1.2.966994951.1708428695',
    '_ga_VBSZ98FXHX': 'GS1.2.1708671754.16.1.1708671996.60.0.0',
    '_fbp': 'fb.1.1708428696715.672350185',
    'Abp.Localization.CultureName': 'ru',
    'ASP.NET_SessionId': 'ubk3f130qgbujepdiooxfbbj',
    '_gali': 'searchParameters',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'https://gov.e-tender.ua',
    'Connection': 'keep-alive',
    'Referer': 'https://gov.e-tender.ua/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

json_data = {
    'Page': 1,
    'PageSize': 20,
    'OrderColumn': '',
    'OrderDirection': 'desc',
    'SearchFilter': {
        'description': None,
        'PriceFrom': None,
        'PriceTo': None,
        'ProcurementMethod': [
            'limited',
        ],
        'procurementMethodTypes': [],
        'regions': [],
        'statuses': [
            'active',
            'unsuccessful',
            'complete',
            'cancelled',
        ],

        'IsStasusesDefaulted': True,
        'Cpvs': '',
        'Dkpp': None,
        'isProductionMode': True,
        'parentCodesEDRPOU': [],
        'codeEDRPOUs': None,
        'Title': None,
        'OrganizationName': None,
        'FunderId': None,
        'searchTimeType': None,
        'tenderPeriodEndFrom': None,
        'tenderPeriodEndTo': None,
        'tenderCreationTimeFrom': '',
        'tenderCreationTimeTo': '',
        'tenderPeriodStartFrom': None,
        'tenderPeriodStartTo': None,
        'CustomerRegion': None,
        'isShowOnlyTendersCreatedOnOurSite': False,
        'mainProcurementCategory': None,
        'milestoneCodeType': None,
        'myBidsOnly': False,
        'bidsFilter': None,
        'lotsFilter': None,
        'isCovid19': False,
        'isDirectOrder': False,
        'contractingsFilter': None,
        'milestoneFilter': None,
        'statusSearchText': None,
        'selectedStatuses': [],
        'checkedStatuses': [],
        'selectedProcTypes': [],
        'isWarForFreedom': False,
        'IsRealTendersForTestMode': False,
        'isFavourite': False,
    }
}
json_data_second = {
    'Page': 1,
    'PageSize': 20,
    'OrderColumn': '',
    'OrderDirection': 'desc',
    'SearchFilter': {
        'description': None,
        'PriceFrom': None,
        'PriceTo': None,
        'ProcurementMethod': [
            'open',
            'selective',
        ],
        'procurementMethodTypes': [],
        'regions': [],
        'statuses': [
            'active.enquiries',
            'active.tendering',
            'active.pre-qualification',
            'active.pre-qualification.stand-still',
            'active.stage2.pending',
            'active.stage2.waiting',
            'active.auction',
            'active.qualification',
            'active.qualification.stand-still',
            'active.awarded',
            'unsuccessful',
            'complete',
            'cancelled',
        ],
        'IsStasusesDefaulted': True,
        'Cpvs': '',
        'Dkpp': None,
        'isProductionMode': True,
        'codeEDRPOUs': None,
        'Title': None,
        'OrganizationName': None,
        'FunderId': None,
        'searchTimeType': None,
        'tenderPeriodEndFrom': None,
        'tenderPeriodEndTo': None,
        'tenderCreationTimeFrom': '',
        'tenderCreationTimeTo': '',
        'tenderPeriodStartFrom': None,
        'tenderPeriodStartTo': None,
        'CustomerRegion': None,
        'isShowOnlyTendersCreatedOnOurSite': False,
        'mainProcurementCategory': None,
        'milestoneCodeType': None,
        'myBidsOnly': False,
        'bidsFilter': None,
        'lotsFilter': None,
        'isCovid19': False,
        'isWarForFreedom': False,
        'isDirectOrder': False,
        'contractingsFilter': None,
        'milestoneFilter': None,
        'statusSearchText': None,
        'selectedStatuses': [],
        'checkedStatuses': [],
        'selectedProcTypes': [],
        'IsRealTendersForTestMode': False,
        'isFavourite': False,
    },
}