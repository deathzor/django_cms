from django.db import models
import pickle
import os 
# Create your models here.
class doctrine(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name;

class fitting(models.Model):
    doctrine = models.ManyToManyField('doctrine',blank=True)
    EFT = models.TextField(max_length=9000)
    def mod_array(self,mod):
        try:
            return [pickle.load(open(os.path.dirname(os.path.realpath(__file__))+'/nametoid.pickle','rb'))[mod],mod]
        except KeyError as e:
            return [0,mod]
    def __str__(self):
        return self.parseEFT()['name']

    def parseEFT(self):
        fit = {'name':'','ship':'','high':[],'mid':[],'low':[],'rig':[],'cargo':[]}
        i = 0;
        y = 0;
        item = ['low','mid','high','rig','cargo'];
        for line in (self.EFT.splitlines()):
            if (i == 0):
                try:
                    fit['name'] = line[1:-1].split(',')[1].strip();
                except IndexError as e:
                    fit['name'] = "Invalid";
                    return fit;
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

