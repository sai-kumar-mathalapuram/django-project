from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from studentapp.models import studentinfo
# Create your views here.
def home(request):
    return render(request,'home.html')
def addform(request):
   return render(request,'addstudent.html')
def addstudent(request):
    if request.method=='POST':
        roll_number= request.POST.get('rollnumber')
        fullname =request.POST.get('fullname')
        date_of_birth=request.POST.get('dob')
        email=request.POST.get('email')
        try:
           student=studentinfo(roll_number=roll_number,fullname=fullname,date_of_birth=date_of_birth,email=email)
           student.save()
           return render(request,'addsucessfull.html')
        except Exception as e:
            return HttpResponse(f"an error occurred:{str(e)}")
    else:
        return render(request,'addstudent.html')

def seestudent(request):
    if request.method == 'POST':
        roll_num = request.POST.get('roll_number')
        try:
            # Query the database for a matching roll number
            student = studentinfo.objects.filter(roll_number=roll_num).first()
            if student:
                # Pass the student object as context to the template
                return render(request, 'searchstudent.html', {'student': student})
            else:
                # Return an error message if no student is found
                return render(request, 'searchstudent.html', {'message': 'Student not found.'})
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")
    else:
        # Render the form for searching students
        return render(request, 'searchstudent.html')
def delstudent(request):
    if request.method=='POST':
        roll_num=request.POST.get('roll_number')
        try:
            student = studentinfo.objects.filter(roll_number=roll_num).first()
            if student:
                student.delete()
                return render(request, 'delstudent.html',{'message': 'student deleted sucessfully......!'})
            else:
                 return render(request, 'delstudent.html', {'message': 'Student not found.'})
        except Exception as e :
           return HttpResponse(f"An error occurred: {str(e)}")
    else:
       return render(request, 'delstudent.html')

def updatestudent(request):
    if request.method=='POST':
        roll_number=request.POST.get('rollnumber')
        fullname=request.POST.get('fullname')
        date_of_birth=request.POST.get('dob')
        email=request.POST.get('email')

        try:
            studentget=studentinfo.objects.filter(roll_number=roll_number).first()
            if studentget:
                student=studentinfo(roll_number=roll_number,fullname=fullname,date_of_birth=date_of_birth,email=email)
                student.save()
                return render(request,'updatestudent.html',{'message':'STUDENT UPDATED SUCESSFULLY'})
            else:
                return render(request,'updatestudent.html',{'message':' student not found'})
        except Exception as e :
            return HttpResponse(f"An error occurred: {str(e)}")
    else:
        return render(request,'updatestudent.html')