from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.



class Equipment_class(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Collectpoint_type(models.Model):
    ALLTYPE = [(0, 'int'), (1, 'float')]
    typename = models.IntegerField(choices=ALLTYPE)
    remark = models.CharField(max_length=20, null=True)
    owner_equipment_class = models.ForeignKey(
        Equipment_class,
        verbose_name='所属设备种类',
        related_name='Collectpoint_types')

    def __str__(self):
        return self.remark


class Equipment(models.Model):
    name = models.CharField(max_length=30, unique=True)
    equipment_class = models.ForeignKey(Equipment_class, verbose_name='所属设备种类', related_name='equipments')

    def __str__(self):
        return self.name

    def update_tags(self):
        property = Collectpoint_type.objects.filter(owner_equipment_class_id=self.equipment_class.id).all()
        for p in property:
            has_flag = False
            # find if tag has existed
            for tag in self.tags.all():
                if tag.tag_from_type_id == p.id:
                    #tag is existed
                    has_flag =True
                    break
            # we should add this tag
            if has_flag == False:
                temp = WebAcess_tag(tag_from_type=p, owner_equipment=self)
                temp.save()

    def create_tags(self):
        property = Collectpoint_type.objects.filter(owner_equipment_class_id=self.equipment_class.id).all()
        for p in property:
            temp = WebAcess_tag(tag_from_type=p, owner_equipment=self)
            temp.save()


class WebAcess_tag(models.Model):
    tag_name = models.CharField(max_length=30)
    owner_equipment = models.ForeignKey(Equipment, verbose_name='所属设备',related_name='tags')
    tag_from_type = models.ForeignKey(Collectpoint_type, verbose_name='所属采集点', null=True)


class WebAcess_analog_recorde(models.Model):
    projectid = models.IntegerField()
    tag_name = models.CharField(max_length=30)
    value = models.FloatField()
    time = models.TimeField()

@receiver([post_save,], sender=Equipment)
def add_additional(sender, **kwargs):
    object = kwargs['instance']
    if kwargs['created'] == True and object is not None:
        object.create_tags()

@receiver([post_save,], sender=Collectpoint_type)
def update_tags(sender, **kwargs):
    object1 = kwargs['instance']
    equipment_class =object1.owner_equipment_class
    #equipment_class =Equipment_class.objects.get(id =  object1.owner_equipment_class_id)
    print (equipment_class.equipments.all())
    for obj in equipment_class.equipments.all():
        if kwargs['created'] == True and obj is not None:
            obj.update_tags()
