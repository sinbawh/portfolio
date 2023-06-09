from django.shortcuts import render

# Create your views here.

def index_view(request):
    context ={'phone': '09362511485', 'fullname': 'سینا بهمنی ','gender': 'مرد', 'email':'sina2016bahmani@gmail.com',
              'birthday': '1380/05/29' , 'location': 'ایران ، کرج', 'millitaryServices': 'معافیت تحصیلی', 
              'nationality': 'ایرانی' , 'maritalStatus': 'مجرد' , 'salary': 'تعیین نشده' , 
              'biography': 'فردی فعال و علاقه مند در حوزه برنامه نویسی هستم و حدودا یک سال است که به طور تخصصی در حال یادگیری زبان برنامه نویسی پایتون و سپس فریمورک جنگو هستم.در حال حاضر در یک شرکت مسافربری بین شهری مشغول به حسابداری هستم. ',
              'JobOne' : 'دراین سال ها به عنوان کارآموز در یک مغازه موبایل فروشی به عنوان فروشنده و مسئول نرم افزار مشغول به کار شدم و سپس بعد از تمام شدن دوران کارآموزی مدتی را در این مغازه مشغول به کار بودم.',
              'JobTwo': 'پس از گرفتن گواهینامه و خریدن ماشین مدتی را برای گذران زندگی و کار دانشجویی در تاکسی های اینترنتی مشغول به کار بودم.',
              'JobThree': 'درآبان سال 1399 در شرکت کاسپین سفر ایرانیان به عنوان مدیر مالی و حسابدار مشغول به کار شدم. این شرکت در بخش حمل و نقل سواری های بین شهری فعالیت دارد و واقع در تهران،خیابان برادران رحمانی ، ترمینال غرب است.',
              'Diploma':'مدرک دیپلم رشته شبکه و نرم افزار ', 'schoolname':'هنرستان شهید صدوقی', 'moadel':'معدل : 16',
              'TTc':'مدرک تدریس زبان انگلیسی | TTC', 'institute':'راه کیش | KishWay' , 'moadelzaban' : "معدل : 18.5" , 
              'Kardani': 'مدرک کاردانی رشته برنامه نویسی و نرم افزار', 'university':'دانشگاه شهید بابایی' , 'city':'شهر : قزوین | نجف آباد','moadelekardani':'معدل : 17.5'}
    return render(request , 'website/index.html' , context)