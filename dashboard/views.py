from django.shortcuts import render, redirect
from .models import Candidate


# Create your views here.
def dashboard_home(request):
    if request.user.is_authenticated:
        candidates = Candidate.objects.all()
        context = {
            'title' : "NACOS EVOTING DASHBOARD",
            "candidates" : candidates
        }
        return render(request, 'dashboard/index.html', context)
    else:
        return redirect('loginuser')

def cast_votes(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            if request.user.is_active:
                presidents = Candidate.objects.filter(position="President")
                vice_presidents = Candidate.objects.filter(position="Vice President")
                gen_secs = Candidate.objects.filter(position="General Secretary")
                ass_gen_secs = Candidate.objects.filter(position="Assistant General Secretary")
                fin_secs = Candidate.objects.filter(position="Financial Secretary")
                software = Candidate.objects.filter(position="Software Director")
                hardware = Candidate.objects.filter(position="Hardware Director")
                welfare = Candidate.objects.filter(position="Welfare Director")
                sports = Candidate.objects.filter(position="Sports Director")
                socials = Candidate.objects.filter(position="Social Director")
                pro = Candidate.objects.filter(position="Public Relations Officer")
                context = {
                    'title' : "Vote Wisely!",
                    "presidents" : presidents,
                    "vices" : vice_presidents,
                    "gen_secs" : gen_secs,
                    "ass_gen_secs" : ass_gen_secs,
                    "fin_secs" : fin_secs,
                    "softwares" : software,
                    "hardwares" : hardware,
                    "welfares" : welfare,
                    "sports" : sports,
                    "socials" : socials,
                    "pros" : pro
                }
                return render(request, 'dashboard/vote.html', context)
            else:
                return redirect('thanks')
        else:
            president_id = request.POST['president']
            print(f'President ID ---> {president_id}')

            try:
                selected_president = Candidate.objects.get(id=request.POST['president'])
                selected_president.votes = selected_president.votes + 1
                selected_president.save(update_fields=['votes'])
            except:
                pass

            try:
                selected_vice_president = Candidate.objects.get(id=request.POST['vicepresident'])
                selected_vice_president.votes = selected_vice_president.votes + 1
                selected_vice_president.save(update_fields=['votes'])
            except:
                pass

            try:
                selected_gensec = Candidate.objects.get(id=request.POST['gensec'])
                selected_gensec.votes = selected_gensec.votes + 1
                selected_gensec.save(update_fields=['votes'])
            except:
                pass
            
            try:
                selected_assgensec = Candidate.objects.get(id=request.POST['assgensec'])
                selected_assgensec.votes = selected_assgensec.votes + 1
                selected_assgensec.save(update_fields=['votes'])
            except:
                pass

            try:
                selected_finsec = Candidate.objects.get(id=request.POST['finsec'])
                selected_finsec.votes = selected_finsec.votes + 1
                selected_finsec.save(update_fields=['votes'])
            except:
                pass

            try:
                selected_software = Candidate.objects.get(id=request.POST['software'])
                selected_software.votes = selected_software.votes + 1
                selected_software.save(update_fields=['votes'])
            except:
                pass

            try:
                selected_hardware = Candidate.objects.get(id=request.POST['hardware'])
                selected_hardware.votes = selected_hardware.votes + 1
                selected_hardware.save(update_fields=['votes'])
            except:
                pass


            try:
                selected_welfare = Candidate.objects.get(id=request.POST['welfare'])
                selected_welfare.votes = selected_welfare.votes + 1
                selected_welfare.save(update_fields=['votes'])
            except:
                pass

            try:
                selected_sports = Candidate.objects.get(id=request.POST['sports'])
                selected_sports.votes = selected_sports.votes + 1
                selected_sports.save(update_fields=['votes'])
            except:
                pass

            try:
                selected_socials = Candidate.objects.get(id=request.POST['socials'])
                selected_socials.votes = selected_socials.votes + 1
                selected_socials.save(update_fields=['votes'])
            except:
                pass

            try:
                selected_pros = Candidate.objects.get(id=request.POST['pros'])
                selected_pros.votes = selected_pros.votes + 1
                selected_pros.save(update_fields=['votes'])
            except:
                pass

            request.user.is_active = False
            request.user.save(update_fields=['is_active'])

            return redirect("thanks")
    else:
        return redirect('loginuser')

def thanks(request):
    context = {
            'title' : "Thank You"
        }

    return render(request, 'dashboard/thanks.html', context)
