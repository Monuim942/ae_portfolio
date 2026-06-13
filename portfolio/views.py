# portfolio/views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project

def contact_view(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name', 'Unknown Entity')
        user_email = request.POST.get('email')
        message_content = request.POST.get('message')
        
        subject = f"⚽ [AE DataTactics] New Briefing from: {client_name}"
        full_message = (
            f"📥 OPERATIONAL INTAKE BRIEFING\n"
            f"----------------------------------------\n"
            f"🏢 Entity / Client Name: {client_name}\n"
            f"📧 Secure Intake Email : {user_email}\n"
            f"----------------------------------------\n"
            f"📋 Tactical Parameters & Requirements:\n"
            f"{message_content}\n"
            f"----------------------------------------\n"
            f"Generated via AE DataTactics Secure Channel."
        )
        
        try:
            send_mail(
                subject=subject,
                message=full_message,
                from_email='your-email@gmail.com', 
                recipient_list=['your-email@gmail.com'], 
                fail_silently=False,
            )
            messages.success(request, "Operational data transmitted successfully!")
        except Exception as e:
            messages.error(request, "Transmission failed. Protocol error. Please try again.")
            
        # بعد نجاح أو فشل الـ POST، نعيد توجيهه لنفس الصفحة لتحديث الفورم ومنع تكرار الإرسال
        return redirect('projects_list') 
    projects = Project.objects.all()
    # 🔥 هنا الحل السحري: إذا دخل المستخدم بشكل عادي (GET)، نقوم بعرض ملف الـ HTML مباشرة بدلاً من الـ redirect اللانهائي!
    # تأكد من أن اسم ملف الـ HTML الخاص بك مطابق للاسم المكتوب أدناه (مثلاً: index.html أو portfolio.html)
    return render(request, 'portfolio/projects_list.html', {
    'projects': projects
    })