from django.db import models
import pickle
import os 
# Create your models here.
class doctrine(models.Model):
    name = models.CharField(max_length=300)

class fitting(models.Model):
    doctrine = models.ForeignKey('doctrine', on_delete=models.SET_NULL, blank=True, null=True)
    EFT = models.TextField(max_length=9000)
    def mod_array(self,mod):
        return [pickle.load(open(os.path.dirname(os.path.realpath(__file__))+'/nametoid.pickle','rb'))[mod],mod]

    def parseEFT(self):
        fit = {'name':'','ship':'','high':[],'mid':[],'low':[],'rig':[],'cargo':[]}
        i = 0;
        y = 0;
        item = ['low','mid','high','rig','cargo'];
        for line in (self.EFT.splitlines()):
            if (i == 0):
                fit['name'] = line[1:-1].split(',')[1].strip();
                fit['ship'] = self.mod_array(line[1:-1].split(',')[0].strip());
            else:
                if (line == "" and y != 4):
                    y = y + 1;
                else:
                    if (line.split(',')[0][-2:-1] == "x" and line.split(',')[0][-1:].isnumeric()):
                        for amount in range(0,int(line.split(',')[0][-1:])):
                            fit[item[y]].append(self.mod_array(line.split(',')[0][:-3]))
                    else:
                        fit[item[y]].append(self.mod_array(line.split(',')[0]))
            i = i + 1;
        return fit
