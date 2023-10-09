from django.db import models
import csv

class Clinic(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    office = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


def import_clinics_from_csv():
    with open('telefony.csv', newline='') as csvfile:
        phonereader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in phonereader:
            print(row[0] + row[1] + row[2] + row[3] + " " + row[4])
            Clinic.objects.create(
                name=row[1],
                department=row[2],
                office=row[3],
                phone=row[4]
            )     