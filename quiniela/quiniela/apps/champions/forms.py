from django import forms

class Upload(forms.Form):
    nombre= forms.CharField(max_length=50)
    
class QuinielaForm(forms.Form):
    gol1_1=forms.IntegerField(min_value=0)
    gol2_1=forms.IntegerField(min_value=0)
    gol1_2=forms.IntegerField(min_value=0)
    gol2_2=forms.IntegerField(min_value=0)
    gol1_3=forms.IntegerField(min_value=0)
    gol2_3=forms.IntegerField(min_value=0)
    gol1_4=forms.IntegerField(min_value=0)
    gol2_4=forms.IntegerField(min_value=0)
    gol1_5=forms.IntegerField(min_value=0)
    gol2_5=forms.IntegerField(min_value=0)
    gol1_6=forms.IntegerField(min_value=0)
    gol2_6=forms.IntegerField(min_value=0)
    gol1_7=forms.IntegerField(min_value=0)
    gol2_7=forms.IntegerField(min_value=0)
    gol1_8=forms.IntegerField(min_value=0)
    gol2_8=forms.IntegerField(min_value=0)
    date =forms.CharField(max_length=20)

class QuinielaForm4(forms.Form):
    gol1_1=forms.IntegerField(min_value=0)
    gol2_1=forms.IntegerField(min_value=0)
    gol1_2=forms.IntegerField(min_value=0)
    gol2_2=forms.IntegerField(min_value=0)
    gol1_3=forms.IntegerField(min_value=0)
    gol2_3=forms.IntegerField(min_value=0)
    gol1_4=forms.IntegerField(min_value=0)
    gol2_4=forms.IntegerField(min_value=0)
    gol1_5=forms.IntegerField(min_value=0)
    gol2_5=forms.IntegerField(min_value=0)
    gol1_6=forms.IntegerField(min_value=0)
    gol2_6=forms.IntegerField(min_value=0)
    gol1_7=forms.IntegerField(min_value=0)
    gol2_7=forms.IntegerField(min_value=0)
    gol1_8=forms.IntegerField(min_value=0)
    gol2_8=forms.IntegerField(min_value=0)

       
class Quiniela2Form(forms.Form):
    gol1_1=forms.IntegerField(min_value=0)
    gol2_1=forms.IntegerField(min_value=0)
    gol1_2=forms.IntegerField(min_value=0)
    gol2_2=forms.IntegerField(min_value=0)
    gol1_3=forms.IntegerField(min_value=0)
    gol2_3=forms.IntegerField(min_value=0)
    gol1_4=forms.IntegerField(min_value=0)
    gol2_4=forms.IntegerField(min_value=0)
    
class Quiniela1Form(forms.Form):
    gol1_1=forms.IntegerField(min_value=0)
    gol2_1=forms.IntegerField(min_value=0)

class QuinielaFormFinal(forms.Form):
    gol1_1=forms.IntegerField(min_value=0)
    gol2_1=forms.IntegerField(min_value=0)
    gol1_2=forms.IntegerField(min_value=0)
    gol2_2=forms.IntegerField(min_value=0)
    gol1_3=forms.IntegerField(min_value=0)
    gol2_3=forms.IntegerField(min_value=0)
    gol1_4=forms.IntegerField(min_value=0)
    gol2_4=forms.IntegerField(min_value=0)
    gol1_5=forms.IntegerField(min_value=0)
    gol2_5=forms.IntegerField(min_value=0)
    gol1_6=forms.IntegerField(min_value=0)
    gol2_6=forms.IntegerField(min_value=0)
    gol1_7=forms.IntegerField(min_value=0)
    gol2_7=forms.IntegerField(min_value=0)
    gol1_8=forms.IntegerField(min_value=0)
    gol2_8=forms.IntegerField(min_value=0)
    equipo1_1=forms.CharField(max_length=20)
    equipo2_1=forms.CharField(max_length=20)
    equipo1_2=forms.CharField(max_length=20)
    equipo2_2=forms.CharField(max_length=20)
    goleq1_1=forms.IntegerField(min_value=0)
    goleq2_1=forms.IntegerField(min_value=0)
    goleq1_2=forms.IntegerField(min_value=0)
    goleq2_2=forms.IntegerField(min_value=0)
    gol1_f=forms.IntegerField(min_value=0)
    gol2_f=forms.IntegerField(min_value=0)
    equipo1_f=forms.CharField(max_length=20)
    equipo2_f=forms.CharField(max_length=20)
    

class nombreForm(forms.Form):
    equip=forms.CharField(max_length=20)
    
    
class modificarForm(forms.Form):
    gol1=forms.IntegerField(min_value=0)
    gol2=forms.IntegerField(min_value=0)
    fase=forms.CharField(max_length=20)
    equipo1=forms.CharField(max_length=20)
    equipo2=forms.CharField(max_length=20)