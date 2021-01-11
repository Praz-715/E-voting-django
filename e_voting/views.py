from django.shortcuts import render, redirect
from e_admin.models import GrupKandidat, Kandidat, Voting, Pemilih
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.views.generic import View


class VotingHomeView2(View):
    
    def cekbatas(self, batas, umum):
        angka = 0
        if umum:
            if 'pil1' in self.request.session:
                angka += 1
            if 'pil2' in self.request.session:
                angka += 1
            if 'pil3' in self.request.session:
                angka += 1
            if 'pil4' in self.request.session:
                angka += 1
            if 'pil5' in self.request.session:
                angka += 1
            if 'pil6' in self.request.session:
                angka += 1
        else:
            pemilih = Pemilih.objects.get(token=self.request.session['token'])
            if pemilih.pil1 != None:
                angka += 1
            if pemilih.pil2 != None:
                angka += 1
            if pemilih.pil3 != None:
                angka += 1
            if pemilih.pil4 != None:
                angka += 1
            if pemilih.pil5 != None:
                angka += 1
            if pemilih.pil6 != None:
                angka += 1
        return batas - angka
        
    def logout(self, umum):
        if umum:
            if 'loginumum' in self.request.session:
                del self.request.session['loginumum']
                for i in range(6):
                    if 'pil{}'.format(i+1) in self.request.session:
                        del self.request.session['pil{}'.format(i+1)]
        else:
            if 'token' in self.request.session:
                pemilih = Pemilih.objects.filter(token=self.request.session['token'])
                pemilih.update(status='SUDAH')
                del self.request.session['token']

    
    def get(self, *args, **kwargs):
        if 'loginumum' in self.request.session or 'token' in self.request.session:
            voting      = Voting.objects.get(slug=kwargs['slug'])
            grup_list   = GrupKandidat.objects.filter(voting=voting)
            kandidat    = Kandidat.objects.filter(grup__in=grup_list).order_by('id')
            i = 1
            grup_all  = []
            for grup in grup_list:
                context_grup = {'id': grup.id, 'namagrup': grup.group_name, 'pilih': False}
                if i == 1:
                    if voting.pilihanumum:
                        if 'pil1' in self.request.session:
                            context_grup['pilih'] = True
                            kan = kandidat.filter(id=self.request.session['pil1'])
                        else:
                            kan = kandidat.filter(grup=grup.id)
                    else:
                        pemilih = Pemilih.objects.get(token=self.request.session['token'])
                        if pemilih.pil1 == None:
                            kan = kandidat.filter(grup=grup.id)
                        else:
                            context_grup['pilih'] = True
                            kan = kandidat.filter(id=pemilih.pil1)
                elif i == 2:
                    if voting.pilihanumum:
                        if 'pil2' in self.request.session:
                            context_grup['pilih'] = True
                            kan = kandidat.filter(id=self.request.session['pil2'])
                        else:
                            kan = kandidat.filter(grup=grup.id)
                    else:
                        pemilih = Pemilih.objects.get(token=self.request.session['token'])
                        if pemilih.pil2 == None:
                            kan = kandidat.filter(grup=grup.id)
                        else:
                            context_grup['pilih'] = True
                            kan = kandidat.filter(id=pemilih.pil2)
                elif i == 3:
                    if voting.pilihanumum:
                        if 'pil3' in self.request.session:
                            context_grup['pilih'] = True
                            kan = kandidat.filter(id=self.request.session['pil3'])
                        else:
                            kan = kandidat.filter(grup=grup.id)
                    else:
                        pemilih = Pemilih.objects.get(token=self.request.session['token'])
                        if pemilih.pil3 == None:
                            kan = kandidat.filter(grup=grup.id)
                        else:
                            context_grup['pilih'] = True
                            kan = kandidat.filter(id=pemilih.pil3)
                elif i == 4:
                    if voting.pilihanumum:
                        if 'pil4' in self.request.session:
                            context_grup['pilih'] = True
                            kan = kandidat.filter(id=self.request.session['pil4'])
                        else:
                            kan = kandidat.filter(grup=grup.id)
                    else:
                        pemilih = Pemilih.objects.get(token=self.request.session['token'])
                        if pemilih.pil4 == None:
                            kan = kandidat.filter(grup=grup.id)
                        else:
                            context_grup['pilih'] = True
                            kan = kandidat.filter(id=pemilih.pil4)
                elif i == 5:
                    if voting.pilihanumum:
                        if 'pil5' in self.request.session:
                            context_grup['pilih'] = True
                            kan = kandidat.filter(id=self.request.session['pil5'])
                        else:
                            kan = kandidat.filter(grup=grup.id)
                    else:
                        pemilih = Pemilih.objects.get(token=self.request.session['token'])
                        if pemilih.pil5 == None:
                            kan = kandidat.filter(grup=grup.id)
                        else:
                            context_grup['pilih'] = True
                            kan = kandidat.filter(id=pemilih.pil5)
                elif i == 6:
                    if voting.pilihanumum:
                        if 'pil6' in self.request.session:
                            context_grup['pilih'] = True
                            kan = kandidat.filter(id=self.request.session['pil6'])
                        else:
                            kan = kandidat.filter(grup=grup.id)
                    else:
                        pemilih = Pemilih.objects.get(token=self.request.session['token'])
                        if pemilih.pil6 == None:
                            kan = kandidat.filter(grup=grup.id)
                        else:
                            context_grup['pilih'] = True
                            kan = kandidat.filter(id=pemilih.pil6)
                i += 1
                context_grup['kandidat'] = kan
                grup_all.append(context_grup)
        
            if self.cekbatas(voting.batas, voting.pilihanumum) == 0:
                pass
            print(self.request.META['HTTP_HOST'])
            context = {
                'voting':voting, 
                'batas':self.cekbatas(voting.batas, voting.pilihanumum), 
                'grup_all':grup_all
                }
            self.kwargs.update(context)
            return render(self.request, 'voting/voting_home.html', self.kwargs)

        
        else:
            messages.error(self.request, 'Login dahulu')
            return redirect('votinglogin', self.kwargs['slug'])

    def post(self, *args, **kwargs):
        voting  = Voting.objects.get(slug=self.kwargs['slug'])
        grup_valuelist   = list(GrupKandidat.objects.filter(voting=voting).values_list('id',flat=True))
        if 'logout' in self.request.POST:
            self.logout(voting.pilihanumum)
            return redirect('votinglogout', self.kwargs['slug'])
        elif 'pilih' in self.request.POST:
            if self.cekbatas(voting.batas, voting.pilihanumum) == 0:
                messages.error(self.request, 'Anda sudah mencapai batas vote')
            else:
                if voting.pilihanumum:
                    kandidat = Kandidat.objects.filter(id=self.request.POST.get('kandidatpk'))
                    suara = kandiat.suara
                    index = grup_valuelist.index(int(self.request.POST.get('gruppk'))) + 1
                    if index == 1 and not 'pil1' in self.request.session:
                        self.request.session['pil1'] = int(self.request.POST.get('kandidatpk'))
                        kandidat.update(suara=suara+1)
                    elif index == 2 and not 'pil2' in self.request.session:
                        self.request.session['pil2'] = int(self.request.POST.get('kandidatpk'))
                        kandidat.update(suara=suara+1)
                    elif index == 3 and not 'pil3' in self.request.session:
                        self.request.session['pil3'] = int(self.request.POST.get('kandidatpk'))
                        kandidat.update(suara=suara+1)
                    elif index == 4 and not 'pil4' in self.request.session:
                        self.request.session['pil4'] = int(self.request.POST.get('kandidatpk'))
                        kandidat.update(suara=suara+1)
                    elif index == 5 and not 'pil5' in self.request.session:
                        self.request.session['pil5'] = int(self.request.POST.get('kandidatpk'))
                        kandidat.update(suara=suara+1)
                    elif index == 6 and not 'pil6' in self.request.session:
                        self.request.session['pil6'] = int(self.request.POST.get('kandidatpk'))
                        kandidat.update(suara=suara+1)
                    else:
                        messages.error(self.request, 'Anda sudah memilih')
                else:
                    pemilih     = Pemilih.objects.filter(token=self.request.session['token'])
                    index = grup_valuelist.index(int(self.request.POST.get('gruppk'))) + 1
                    if index == 1 and pemilih[0].pil1 == None:
                        pemilih.update(pil1=self.request.POST.get('kandidatpk'))
                    elif index == 2 and pemilih[0].pil2 == None:
                        pemilih.update(pil2=self.request.POST.get('kandidatpk'))
                    elif index == 3 and pemilih[0].pil3 == None:
                        pemilih.update(pil3=self.request.POST.get('kandidatpk'))
                    elif index == 4 and pemilih[0].pil4 == None:
                        pemilih.update(pil4=self.request.POST.get('kandidatpk'))
                    elif index == 5 and pemilih[0].pil5 == None:
                        pemilih.update(pil5=self.request.POST.get('kandidatpk'))
                    elif index == 6 and pemilih[0].pil6 == None:
                        pemilih.update(pil6=self.request.POST.get('kandidatpk'))
                    else:
                        messages.error(self.request, 'Anda sudah memilih')
        return redirect('votinghome', self.kwargs['slug'])




        



class VotingHomeView(View):

    def cekbatas(self, batas):
        angka = 0
        pemilih     = Pemilih.objects.filter(token=self.request.session['token']).first()
        print(pemilih)
        if pemilih.pil1 != None:
            angka += 1
        if pemilih.pil2 != None:
            angka += 1
        if pemilih.pil3 != None:
            angka += 1
        if pemilih.pil4 != None:
            angka += 1
        if pemilih.pil5 != None:
            angka += 1
        if pemilih.pil6 != None:
            angka += 1
        print('angka=',angka,'  batas=',batas)
        return batas - angka
    
    def logout(self):
        if 'token' in self.request.session:
            del self.request.session['token']

    def get(self, *args, **kwargs):
        voting      = Voting.objects.get(slug=kwargs['slug'])
        grup_list   = GrupKandidat.objects.filter(voting=voting)
        kandidat    = Kandidat.objects.filter(grup__in=grup_list).order_by('id')

        if voting.pilihanumum == True:
            print(self.cekbatas(voting.batas))
            i = 1
            grup_all  = []
            for grup in grup_list:
                context_grup = {'id': grup.id, 'namagrup': grup.group_name}
                kan = []
                if i == 1:
                    for x in kandidat:
                        if x.grup.id == grup.id:
                            kan.append(x)
                    context_grup['kandidat'] = kan
                elif i == 2:
                    for x in kandidat:
                        if x.grup.id == grup.id:
                            kan.append(x)
                    context_grup['kandidat'] = kan
                elif i == 3:
                    for x in kandidat:
                        if x.grup.id == grup.id:
                            kan.append(x)
                    context_grup['kandidat'] = kan
                elif i == 4:
                    for x in kandidat:
                        if x.grup.id == grup.id:
                            kan.append(x)
                    context_grup['kandidat'] = kan
                elif i == 5:
                    for x in kandidat:
                        if x.grup.id == grup.id:
                            kan.append(x)
                    context_grup['kandidat'] = kan
                elif i == 6:
                    for x in kandidat:
                        if x.grup.id == grup.id:
                            kan.append(x)
                    context_grup['kandidat'] = kan
                else:
                    context_grup['kandidat'] = [False]
                i += 1
                grup_all.append(context_grup)

            self.kwargs.update({'voting':voting,'grup_all':grup_all,'batas':self.cekbatas(voting.batas)})
            return render(self.request, 'voting/voting_home.html', self.kwargs)

        else:
            print(kandidat.filter(grup=5))
            pemilih     = Pemilih.objects.get(token=self.request.session['token'])
            print(self.cekbatas(voting.batas))
            if 'token' not in self.request.session:
                messages.error(self.request, 'Login Dahulu')
                return redirect('votinglogin', self.kwargs['slug'])
            else:
                i = 1
                grup_all  = []
                for grup in grup_list:
                    context_grup = {'id': grup.id, 'namagrup': grup.group_name}
                    kan = []
                    if i == 1 and pemilih.pil1 == None:
                        for x in kandidat:
                            if x.grup.id == grup.id:
                                kan.append(x)
                        context_grup['kandidat'] = kan
                    elif i == 2 and pemilih.pil2 == None:
                        for x in kandidat:
                            if x.grup.id == grup.id:
                                kan.append(x)
                        context_grup['kandidat'] = kan
                    elif i == 3 and pemilih.pil3 == None:
                        for x in kandidat:
                            if x.grup.id == grup.id:
                                kan.append(x)
                        context_grup['kandidat'] = kan
                    elif i == 4 and pemilih.pil4 == None:
                        for x in kandidat:
                            if x.grup.id == grup.id:
                                kan.append(x)
                        context_grup['kandidat'] = kan
                    elif i == 5 and pemilih.pil5 == None:
                        for x in kandidat:
                            if x.grup.id == grup.id:
                                kan.append(x)
                        context_grup['kandidat'] = kan
                    elif i == 6 and pemilih.pil6 == None:
                        for x in kandidat:
                            if x.grup.id == grup.id:
                                kan.append(x)
                        context_grup['kandidat'] = kan
                    else:
                        context_grup['kandidat'] = [False]
                    i += 1
                    grup_all.append(context_grup)

                self.kwargs.update({'voting':voting,'grup_all':grup_all,'batas':self.cekbatas(voting.batas)})
                return render(self.request, 'voting/voting_home.html', self.kwargs)

        
    def post(self, *args, **kwargs):
        if 'logout' in self.request.POST:
            self.logout()
        voting      = Voting.objects.get(slug=kwargs['slug'])
        grup_valuelist   = GrupKandidat.objects.filter(voting=voting).values_list('id',flat=True)
        if voting.pilihanumum == True:
            pass
        else:
            pemilih     = Pemilih.objects.filter(token=self.request.session['token'])
            if self.cekbatas(voting.batas) > 0:
                if 'pilih' in self.request.POST:
                    grup_valuelist = list(grup_valuelist)
                    index = grup_valuelist.index(int(self.request.POST.get('gruppk')))+1
                    if index == 1 and pemilih[0].pil1 == None:
                        pemilih.update(pil1=self.request.POST.get('pk'))
                    elif index == 2 and pemilih[0].pil2 == None:
                        pemilih.update(pil2=self.request.POST.get('pk'))
                    elif index == 3 and pemilih[0].pil3 == None:
                        pemilih.update(pil3=self.request.POST.get('pk'))
                    elif index == 4 and pemilih[0].pil4 == None:
                        pemilih.update(pil4=self.request.POST.get('pk'))
                    elif index == 5 and pemilih[0].pil5 == None:
                        pemilih.update(pil5=self.request.POST.get('pk'))
                    elif index == 6 and pemilih[0].pil6 == None:
                        pemilih.update(pil6=self.request.POST.get('pk'))
            else:
                self.logout()
                pemilih.update(status='SUDAH')

        return redirect('votinghome', self.kwargs['slug'])




class VotingLoginView(View):
    template_name = 'voting/voting_login.html'

    def get(self, *args, **kwargs):
        voting      = Voting.objects.get(slug=self.kwargs['slug'])
        context     = {
            'voting' : voting
        }
        if voting.pilihanumum == True:
            context['umum'] = True
        self.kwargs.update(context)
        # print(self.kwargs)
        return render(self.request, 'voting/voting_login.html', self.kwargs)

    def post(self, *args, **kwargs):
        token       = self.request.POST.get('token')

        cek         = Pemilih.objects.filter(token=token).first()
        cekbelum    = Pemilih.objects.filter(token=token,status='BELUM').first()


        if cek:
            print('================ Cek True')
            if cekbelum:
                self.request.session['token'] = token
                return redirect('votinghome', self.kwargs['slug'])
            else:
                messages.error(self.request, 'Token sudah digunakan')
        else:
            messages.error(self.request, 'Token Tidak Ditemukan')
        return redirect('votinglogin', self.kwargs['slug'])

