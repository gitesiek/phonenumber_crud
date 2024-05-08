from django.db import models
import csv


class Contacts(models.Model):
    contact_id = models.AutoField(primary_key=True)
    jd_organizcyjnej = models.CharField(max_length=255)
    lokalizacja = models.CharField(max_length=255)
    num_wew = models.CharField(max_length=255)
    num_tel = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.jd_organizcyjnej


def import_clinics_from_csv():
    with open('telefony.csv', newline='') as csvfile:
        phonereader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in phonereader:
            print(row[0] + row[1] + row[2] + row[3] + " " + row[4])
            Contacts.objects.create(
                jd_organizcyjnej=row[1],
                lokalizacja=row[2],
                num_wew=row[3],
                num_tel=row[4],
                active = True
            )
