# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Biomes(models.Model):
    mht_code = models.BigIntegerField(db_column='MHT_CODE', blank=True, null=True)  # Field name made lowercase.
    biome = models.TextField(db_column='BIOME', blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    date_created = models.TextField(db_column='DATE_CREATED', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.TextField(db_column='MODIFIED_BY', blank=True, null=True)  # Field name made lowercase.
    date_modified = models.TextField(db_column='DATE_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    short_biome = models.TextField(db_column='SHORT_BIOME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'biomes'


class Class(models.Model):
    class_id = models.BigIntegerField(db_column='CLASS_ID', blank=True, null=True)  # Field name made lowercase.
    class_field = models.TextField(db_column='CLASS', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    date_created = models.TextField(db_column='DATE_CREATED', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.TextField(db_column='MODIFIED_BY', blank=True, null=True)  # Field name made lowercase.
    date_modified = models.TextField(db_column='DATE_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'class'


class ColumnTranslation(models.Model):
    table_name = models.TextField(db_column='TABLE_NAME', blank=True, null=True)  # Field name made lowercase.
    column_name = models.TextField(db_column='COLUMN_NAME', blank=True, null=True)  # Field name made lowercase.
    display_name = models.TextField(db_column='DISPLAY_NAME', blank=True, null=True)  # Field name made lowercase.
    _id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'column_translation'


class CommonNames(models.Model):
    common_name_id = models.BigIntegerField(db_column='COMMON_NAME_ID', blank=True, null=True)  # Field name made lowercase.
    common_name = models.TextField(db_column='COMMON_NAME', blank=True, null=True)  # Field name made lowercase.
    species_id = models.BigIntegerField(db_column='SPECIES_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    date_created = models.TextField(db_column='DATE_CREATED', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.TextField(db_column='MODIFIED_BY', blank=True, null=True)  # Field name made lowercase.
    date_modified = models.TextField(db_column='DATE_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'common_names'


class ConservationSts(models.Model):
    conservation_status = models.BigIntegerField(db_column='CONSERVATION_STATUS', blank=True, null=True)  # Field name made lowercase.
    conservation_status_desc = models.TextField(db_column='CONSERVATION_STATUS_DESC', blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    date_created = models.TextField(db_column='DATE_CREATED', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.TextField(db_column='MODIFIED_BY', blank=True, null=True)  # Field name made lowercase.
    date_modified = models.TextField(db_column='DATE_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conservation_sts'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EcoregionSpecies(models.Model):
    ecoregion_code = models.TextField(db_column='ECOREGION_CODE', blank=True, null=True)  # Field name made lowercase.
    species_id = models.BigIntegerField(db_column='SPECIES_ID', blank=True, null=True)  # Field name made lowercase.
    eco_endemic = models.TextField(db_column='ECO_ENDEMIC', blank=True, null=True)  # Field name made lowercase.
    deleted = models.TextField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.
    date_created = models.TextField(db_column='DATE_CREATED', blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    date_modified = models.TextField(db_column='DATE_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.TextField(db_column='MODIFIED_BY', blank=True, null=True)  # Field name made lowercase.
    introduced = models.TextField(db_column='INTRODUCED', blank=True, null=True)  # Field name made lowercase.
    _id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ecoregion_species'


class Ecoregions(models.Model):
    ecoregion_code = models.TextField(db_column='ECOREGION_CODE', blank=True, null=True)  # Field name made lowercase.
    ecoregion_name = models.TextField(db_column='ECOREGION_NAME', blank=True, null=True)  # Field name made lowercase.
    ecoregion_area = models.BigIntegerField(db_column='ECOREGION_AREA', blank=True, null=True)  # Field name made lowercase.
    global200_num = models.BigIntegerField(db_column='GLOBAL200_NUM', blank=True, null=True)  # Field name made lowercase.
    conservation_status = models.BigIntegerField(db_column='CONSERVATION_STATUS', blank=True, null=True)  # Field name made lowercase.
    analysis = models.TextField(db_column='ANALYSIS', blank=True, null=True)  # Field name made lowercase.
    realm_code = models.TextField(db_column='REALM_CODE', blank=True, null=True)  # Field name made lowercase.
    mht_code = models.BigIntegerField(db_column='MHT_CODE', blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    date_created = models.TextField(db_column='DATE_CREATED', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.TextField(db_column='MODIFIED_BY', blank=True, null=True)  # Field name made lowercase.
    date_modified = models.TextField(db_column='DATE_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    info_location = models.TextField(db_column='INFO_LOCATION', blank=True, null=True)  # Field name made lowercase.
    alternate_name = models.TextField(db_column='ALTERNATE_NAME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ecoregions'


class Family(models.Model):
    family_id = models.BigIntegerField(db_column='FAMILY_ID', blank=True, null=True)  # Field name made lowercase.
    family = models.TextField(db_column='FAMILY', blank=True, null=True)  # Field name made lowercase.
    order_id = models.BigIntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    date_created = models.TextField(db_column='DATE_CREATED', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.TextField(db_column='MODIFIED_BY', blank=True, null=True)  # Field name made lowercase.
    date_modified = models.TextField(db_column='DATE_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'family'


class Genus(models.Model):
    genus_id = models.BigIntegerField(db_column='GENUS_ID', blank=True, null=True)  # Field name made lowercase.
    genus = models.TextField(db_column='GENUS', blank=True, null=True)  # Field name made lowercase.
    family_id = models.BigIntegerField(db_column='FAMILY_ID', blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    date_created = models.TextField(db_column='DATE_CREATED', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.TextField(db_column='MODIFIED_BY', blank=True, null=True)  # Field name made lowercase.
    date_modified = models.TextField(db_column='DATE_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'genus'


class Global200(models.Model):
    global200_num = models.BigIntegerField(db_column='GLOBAL200_NUM', blank=True, null=True)  # Field name made lowercase.
    global200_name = models.TextField(db_column='GLOBAL200_NAME', blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    date_created = models.TextField(db_column='DATE_CREATED', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.TextField(db_column='MODIFIED_BY', blank=True, null=True)  # Field name made lowercase.
    date_modified = models.TextField(db_column='DATE_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'global_200'


class RealmCode(models.Model):
    realm_code = models.TextField(db_column='REALM_CODE', blank=True, null=True)  # Field name made lowercase.
    realm = models.TextField(db_column='REALM', blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    date_created = models.TextField(db_column='DATE_CREATED', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.TextField(db_column='MODIFIED_BY', blank=True, null=True)  # Field name made lowercase.
    date_modified = models.TextField(db_column='DATE_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'realm_code'


class RedlistCategory(models.Model):
    red_list_category = models.TextField(db_column='RED_LIST_CATEGORY', blank=True, null=True)  # Field name made lowercase.
    red_list_cat_desc = models.TextField(db_column='RED_LIST_CAT_DESC', blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    date_created = models.TextField(db_column='DATE_CREATED', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.TextField(db_column='MODIFIED_BY', blank=True, null=True)  # Field name made lowercase.
    date_modified = models.TextField(db_column='DATE_MODIFIED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'redlist_category'


class RedlistSpecies(models.Model):
    redlist_id = models.BigIntegerField(db_column='REDLIST_ID', blank=True, null=True)  # Field name made lowercase.
    genus = models.TextField(db_column='GENUS', blank=True, null=True)  # Field name made lowercase.
    species = models.TextField(db_column='SPECIES', blank=True, null=True)  # Field name made lowercase.
    red_list_category = models.TextField(db_column='RED_LIST_CATEGORY', blank=True, null=True)  # Field name made lowercase.
    rlscrit = models.TextField(db_column='RLSCRIT', blank=True, null=True)  # Field name made lowercase.
    wwf_species_id = models.TextField(db_column='WWF_SPECIES_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'redlist_species'


class Species(models.Model):
    species_id = models.BigIntegerField(db_column='SPECIES_ID', blank=True, null=True)  # Field name made lowercase.
    species = models.TextField(db_column='SPECIES', blank=True, null=True)  # Field name made lowercase.
    genus_id = models.BigIntegerField(db_column='GENUS_ID', blank=True, null=True)  # Field name made lowercase.
    mapped = models.TextField(db_column='MAPPED', blank=True, null=True)  # Field name made lowercase.
    deleted = models.TextField(db_column='DELETED', blank=True, null=True)  # Field name made lowercase.
    strict_endemism = models.TextField(db_column='STRICT_ENDEMISM', blank=True, null=True)  # Field name made lowercase.
    modified_by = models.TextField(db_column='MODIFIED_BY', blank=True, null=True)  # Field name made lowercase.
    date_modified = models.TextField(db_column='DATE_MODIFIED', blank=True, null=True)  # Field name made lowercase.
    created_by = models.TextField(db_column='CREATED_BY', blank=True, null=True)  # Field name made lowercase.
    date_created = models.TextField(db_column='DATE_CREATED', blank=True, null=True)  # Field name made lowercase.
    info_location = models.TextField(db_column='INFO_LOCATION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'species'
