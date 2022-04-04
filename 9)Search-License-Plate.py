#The cities list are the cities in Turkey.
cities = ['ADANA','ADIYAMAN','AFYON','AGRI','AMASYA','ANKARA','ANTALYA','ARTVIN','AYDIN','BALIKESIR','BILECIK',
          'BINGOL','BITLIS','BOLU','BURDUR','BURSA','CANAKKALE','CANKIRI','CORUM','DENIZLI','DIYARBAKIR',
          'EDIRNE','ELAZIG','ERZINCAN','ERZURUM','ESKISEHIR','GAZIANTEP','GIRESUN','GUMUSHANE','HAKKARI',
          'HATAY','ISPARTA','MERSIN','ISTANBUL','IZMIR','KARS','KASTAMONU','KAYSERI','KIRKLARELI','KIRSEHIR',
          'KOCAELI','KONYA','KUTAHYA','MALATYA','MANISA','KAHRAMANMARAS','MARDIN','MUGLA','MUS','NEVSEHIR','NIGDE',
          'ORDU','RIZE','SAKARYA','SAMSUN','SIIRT','SINOP','SIVAS','TEKIDAG','TOKAT','TRABZON','TUNCELI','SANLIURFA',
          'USAK','VAN','YOZGAT','ZONGULDAK','AKSARAY','BAYBURT','KARAMAN','KIRIKKALE','BATMAN','SIRNAK','BARTIN',
          'ARDAHAN','IGDIR','YALOVA','KARABUK','KILIS','OSMANIYE','DUZCE']


cityDict = {}
for i,v in enumerate(cities,start = 1):
    cityDict[i] = v
 
cityDict2 = {v : i for i,v in enumerate(cities,start = 1)}


#Searching which city it is with the city plate
def searchWithLicensePlate():
    for i in range(int(input('Number of license plates you want to learn: '))):
        while True:
            try:
                licensePlate = int(input('License Plate: '))
                if licensePlate < 10:
                    city = cityDict[licensePlate]
                    print(f"0{licensePlate} {city}")
                    break
                else:
                    city = cityDict[licensePlate]
                    print(f"{licensePlate} {city}")
                    break
            except ValueError:
                print('Value Error')
                print('You must enter just a number.Try again.')
            except KeyError:
                print('Key Error')
                print('You must enter between 1 and 81 numbers.(1 and 81 include)')
                
                
#Searching which license plate is by the name of the city
def searchWithNameOfCity():
    for j in range(int(input('Number of city you want to learn: '))):
        while True:
            try:
                city = input('City: ').upper()
                licensePlate = cityDict2[city]
                if city in cities[:9]:
                    print(f"{city} 0{licensePlate}")
                    break
                else:
                    print(f"{city} {licensePlate}")
                    break
            except KeyError:
                print('Key Error. Deficient word input.Try again please.')