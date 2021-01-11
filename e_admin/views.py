from django.shortcuts import render, redirect
from random import randint
import secrets
from django.views.generic import ListView, CreateView, View, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
# Create your views here.
from .models import Kandidat, GrupKandidat, Pemilih, Voting
from .forms import GrupKandidatForm, KandidatForm, VotingForm ,PemilihVotingForm


class WaktunyaVoting:
    pass

class DashboardView(View):
    def get(self, *args, **kwargs):
        voting_list = Voting.objects.filter(user=self.request.user)
        grup_list   = GrupKandidat.objects.filter(voting__in=voting_list)
        kandidat_list   = Kandidat.objects.filter(grup__in=grup_list)
        pemilih_list    = Pemilih.objects.filter(voting__in=voting_list)
        voting_all  = []
        for voting in voting_list:
            vot_con  = {'nama':voting.namavoting,'suaramasuk': pemilih_list.filter(voting=voting, status='SUDAH').count()}
            grup_all = []
            i = 1
            for grup in grup_list:
                grup_con = {'nama': grup.group_name}
                kandidat_all = []
                if i == 1:
                    for kandidat in kandidat_list:
                        if kandidat.grup.id == grup.id:
                            kan_con = {'nama': kandidat.nama}
                            if voting.pilihanumum:
                                kan_con['suara'] = kandidat.suara
                            else:
                                kan_con['suara'] = Pemilih.objects.filter(pil1=kandidat.id).count()
                            kandidat_all.append(kan_con)
                    
                elif i == 2:
                    for kandidat in kandidat_list:
                        if kandidat.grup.id == grup.id:
                            kan_con = {'nama': kandidat.nama}
                            if voting.pilihanumum:
                                kan_con['suara'] = kandidat.suara
                            else:
                                kan_con['suara'] = Pemilih.objects.filter(pil2=kandidat.id).count()
                            kandidat_all.append(kan_con)
                elif i == 3:
                    for kandidat in kandidat_list:
                        if kandidat.grup.id == grup.id:
                            kan_con = {'nama': kandidat.nama}
                            if voting.pilihanumum:
                                kan_con['suara'] = kandidat.suara
                            else:
                                kan_con['suara'] = Pemilih.objects.filter(pil3=kandidat.id).count()
                            kandidat_all.append(kan_con)
                elif i == 4:
                    for kandidat in kandidat_list:
                        if kandidat.grup.id == grup.id:
                            kan_con = {'nama': kandidat.nama}
                            if voting.pilihanumum:
                                kan_con['suara'] = kandidat.suara
                            else:
                                kan_con['suara'] = Pemilih.objects.filter(pil4=kandidat.id).count()
                            kandidat_all.append(kan_con)
                elif i == 5:
                    for kandidat in kandidat_list:
                        if kandidat.grup.id == grup.id:
                            kan_con = {'nama': kandidat.nama}
                            if voting.pilihanumum:
                                kan_con['suara'] = kandidat.suara
                            else:
                                kan_con['suara'] = Pemilih.objects.filter(pil5=kandidat.id).count()
                            kandidat_all.append(kan_con)
                elif i == 6:
                    for kandidat in kandidat_list:
                        if kandidat.grup.id == grup.id:
                            kan_con = {'nama': kandidat.nama}
                            if voting.pilihanumum:
                                kan_con['suara'] = kandidat.suara
                            else:
                                kan_con['suara'] = Pemilih.objects.filter(pil6=kandidat.id).count()
                            kandidat_all.append(kan_con)
                i += 1
                grup_con['kandidat'] = kandidat_all
                grup_all.append(grup_con)
            vot_con['grup'] = grup_all
            voting_all.append(vot_con)
        print(voting_all)
        self.kwargs.update({'voting_list': voting_all})
        return render(self.request, 'e_admin/dashboard.html', self.kwargs)

class PemilihView(View):
    template_name = "e_admin/pemilih.html"
    context = {}

    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def get(self, request):
        self.context['voting_valuelist']    = Voting.objects.filter(user=request.user.id).values_list('id', flat=True)
        self.context['pemilih']             = Pemilih.objects.filter(voting__in=self.context['voting_valuelist'])
        self.context['grup_count']          = [x+1 for x in range(GrupKandidat.objects.filter(voting__in=self.context['voting_valuelist']).count())]
        self.context['voting_list']         = Voting.objects.filter(user=request.user.id)
        self.context['formvoting']          = PemilihVotingForm
        return render(request, self.template_name, self.context)

    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def post(self, request):
        if 'updatepemilih' in request.POST:
            form = PemilihVotingForm(request.POST, instance=Voting.objects.get(id=request.POST.get('votinger')))
            if form.is_valid():
                form.save()
        if 'createvoters' in request.POST and request.POST.get('voting'):
            jumlahvoter = int(request.POST.get('jumlahvoter'))
            for x in range(jumlahvoter):
                text = secrets.token_urlsafe(7)
                p = Pemilih.objects.filter(token=text).first()
                if (p is None):
                    Pemilih.objects.create(token=text,voting=Voting.objects.get(id=request.POST.get('voting')))
        if 'deletevoters' in request.POST and request.POST.get('voting'):
            jumlahvoter = int(request.POST.get('jumlahvoter'))
            for x in range(jumlahvoter):
                Pemilih.objects.filter(voting=Voting.objects.get(id=request.POST.get('voting')), status=request.POST.get('status'))[0].delete()
        return redirect('e_admin:pemilih')


class AdminKandidatView(View):
    template_name = "e_admin/kandidat_home.html"
    context = {}

    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def get(self,request):
        self.context['formgrup']            = GrupKandidatForm
        self.context['formkandidat']        = KandidatForm
        self.context['formvoting']          = VotingForm
        self.context['grup']                = GrupKandidat.objects.values_list('id', flat=True).distinct()
        self.context['voting_valuelist']    = Voting.objects.filter(user=request.user.id).values_list('id', flat=True)
        self.context['grup_list']           = GrupKandidat.objects.filter(voting__in=self.context['voting_valuelist']).order_by('id','voting')
        self.context['grup_valuelist']      = self.context['grup_list'].values_list('id', flat=True)
        self.context['kandidat']            = Kandidat.objects.filter(grup__in=self.context['grup_valuelist'])
        self.context['voting']              = True
        self.context['voting_list']         = Voting.objects.filter(user=request.user.id)
        return render(request, self.template_name, self.context)

    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def post(self, request):
        if 'creategrup' in request.POST:
            formgrup = GrupKandidatForm(request.POST or None)
            if formgrup.is_valid():
                formgrup.save()

        if 'createkandidat' in request.POST:
            formgrup = KandidatForm(request.POST or None, request.FILES)
            if formgrup.is_valid():
                formgrup.save()

        if 'createvoting' in request.POST:
            formgrup = VotingForm(request.POST or None)
            if formgrup.is_valid():
                formgrup.save()

        if 'deletekandidat' in request.POST:
            Kandidat.objects.get(id=request.POST.get('pk')).delete()

        if 'deletevoting' in request.POST:
            Voting.objects.get(id=request.POST.get('deletevoting')).delete()

        if 'deletegroup' in request.POST:
            GrupKandidat.objects.get(id=request.POST.get('deletegroup')).delete()
        
        messages.success(request, 'Data ditambahkan')
        return redirect('e_admin:list')


class ALLUpdateView(View):
    template_name = "e_admin/update_all.html"
    context = {}

    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def get(self, *args, **kwargs):
        if kwargs['nama'] == 'grup':
            form = GrupKandidatForm(instance=GrupKandidat.objects.get(id=kwargs['id']))
        elif kwargs['nama'] == 'voting':
            form = VotingForm(instance=Voting.objects.get(id=kwargs['id']))
        elif kwargs['nama'] == 'kandidat':
            form = KandidatForm(instance=Kandidat.objects.get(id=kwargs['id']))
        self.kwargs.update({'form':form})
        return render(self.request, self.template_name, self.kwargs)

    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def post(self, *args, **kwargs):
        if kwargs['nama'] == 'grup':
            form = GrupKandidatForm(self.request.POST, instance=GrupKandidat.objects.get(id=kwargs['id']))
        elif kwargs['nama'] == 'voting':
            form = VotingForm(self.request.POST, instance=Voting.objects.get(id=kwargs['id']))
        elif kwargs['nama'] == 'kandidat':
            form = KandidatForm(self.request.POST, self.request.FILES, instance=Kandidat.objects.get(id=kwargs['id']))

        if form.is_valid():
            form.save()
            return redirect('e_admin:list')
        else:
            return redirect('e_admin:pemilih')