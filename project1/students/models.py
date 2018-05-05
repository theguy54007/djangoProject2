from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50, blank=False)
    birth_date = models.DateField('birthday', blank=False)

    BOY = 'BOY'
    GIRL = 'GIRL'
    GENDER_CHOICES = (
        (BOY, 'Boy'),
        (GIRL, 'Girl'),
    )
    gender = models.CharField(
        max_length=5,
        choices=GENDER_CHOICES,
        default=BOY,
        blank=False,
    )

    current_school_name = models.CharField(max_length=50)

    KINDER1 = '幼末'
    KINDER2 = '幼小'
    KINDER3 = '幼中'
    KINDER4 = '幼大'
    PRIMARY1 = '小一'
    PRIMARY2 = '小二'
    YEAR_IN_SCHOOL_CHOICES = (
        (KINDER1, '幼末'),
        (KINDER2, '幼小'),
        (KINDER3, '幼中'),
        (KINDER4, '幼大'),
        (PRIMARY1, '小一'),
        (PRIMARY2, '小二'),
    )
    current_school_grade = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=KINDER1,
        blank=False,
    )

    name_en = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Diagnostic(models.Model):
    name = models.CharField(max_length=50, blank=False)
    test_datetime = models.DateTimeField('test_time', blank=False)


    MK = 'MK'
    MP1 = 'MP1'
    MP2 = 'MP2'
    MP3 = 'MP3'
    MP4 = 'MP4'
    TEST_LEVEL_CHOICES = (
        (MK, 'MK'),
        (MP1, 'MP1'),
        (MP2, 'MP2'),
        (MP3, 'MP3'),
        (MP4, 'MP4'),
    )
    test_level = models.CharField(
        max_length=3,
        choices=TEST_LEVEL_CHOICES,
        default=MK,
        blank=False,
    )


    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_level